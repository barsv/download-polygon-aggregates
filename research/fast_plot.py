import matplotlib.pyplot as plt
import numpy as np
import threading
import time
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.patches import Rectangle
from io import BytesIO
import matplotlib.image as mpimg

class FastInteractivePlot:
    def __init__(self, figsize=(10, 8), dpi=100):
        # Main figure for display
        self.fig, self.ax = plt.subplots(figsize=figsize, dpi=dpi)
        self.canvas = self.fig.canvas
        
        # Data for plotting
        self.plot_data = None
        self.plot_func = None
        
        # Interaction state
        self.is_interacting = False
        self.render_timer = None
        self.last_xlim = None
        self.last_ylim = None
        
        # Raster cache
        self.cached_image = None
        self.cached_xlim = None
        self.cached_ylim = None
        self.cache_dpi = 150  # High resolution for cache
        
        # Setup interactivity
        self.setup_interaction()
        
        print("FastInteractivePlot created. Use set_data() to add data.")
    
    def set_data(self, x, y, plot_type='scatter', **kwargs):
        """
        Sets data for plotting
        plot_type: 'scatter', 'plot', 'hist2d'
        """
        self.plot_data = (x, y)
        self.plot_kwargs = kwargs
        
        if plot_type == 'scatter':
            self.plot_func = self._scatter_plot
        elif plot_type == 'plot':
            self.plot_func = self._line_plot
        elif plot_type == 'hist2d':
            self.plot_func = self._hist2d_plot
        else:
            raise ValueError(f"Неподдерживаемый тип графика: {plot_type}")
        
        print(f"Data set: {len(x)} points, type: {plot_type}")
        
        # Set initial limits
        self.ax.set_xlim(np.min(x), np.max(x))
        self.ax.set_ylim(np.min(y), np.max(y))
        
        # Do initial render
        self.high_quality_render()
    
    def _scatter_plot(self, ax, x, y, **kwargs):
        default_kwargs = {'s': 1, 'alpha': 0.6, 'c': 'blue'}
        default_kwargs.update(kwargs)
        ax.scatter(x, y, **default_kwargs)
    
    def _line_plot(self, ax, x, y, **kwargs):
        default_kwargs = {'linewidth': 1, 'alpha': 0.8}
        default_kwargs.update(kwargs)
        ax.plot(x, y, **default_kwargs)
    
    def _hist2d_plot(self, ax, x, y, **kwargs):
        default_kwargs = {'bins': 50, 'cmap': 'Blues'}
        default_kwargs.update(kwargs)
        ax.hist2d(x, y, **default_kwargs)
    
    def setup_interaction(self):
        """Sets up event handlers for interactivity"""
        
        # Variables for panning
        self.pan_start = None
        self.original_xlim = None
        self.original_ylim = None
        
        # Mouse events
        self.canvas.mpl_connect('button_press_event', self.on_press)
        self.canvas.mpl_connect('button_release_event', self.on_release)
        self.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.canvas.mpl_connect('scroll_event', self.on_scroll)
    
    def on_press(self, event):
        if event.inaxes != self.ax:
            return
        if event.button == 1:  # Left mouse button
            self.start_interaction()
            self.pan_start = (event.xdata, event.ydata)
            self.original_xlim = self.ax.get_xlim()
            self.original_ylim = self.ax.get_ylim()
    
    def on_motion(self, event):
        if self.pan_start is None or event.inaxes != self.ax:
            return
        
        # During panning, show cached image
        if self.cached_image is not None and self.is_interacting:
            dx = self.pan_start[0] - event.xdata
            dy = self.pan_start[1] - event.ydata
            
            # Calculate new limits
            xlim = self.original_xlim
            ylim = self.original_ylim
            new_xlim = (xlim[0] + dx, xlim[1] + dx)
            new_ylim = (ylim[0] + dy, ylim[1] + dy)
            
            # Quickly update only view without recalculating data
            self.show_cached_view(new_xlim, new_ylim)
        else:
            # Fallback to old method if no cache
            dx = self.pan_start[0] - event.xdata
            dy = self.pan_start[1] - event.ydata
            
            xlim = self.original_xlim
            ylim = self.original_ylim
            
            self.ax.set_xlim(xlim[0] + dx, xlim[1] + dx)
            self.ax.set_ylim(ylim[0] + dy, ylim[1] + dy)
            
            # Just update canvas without redrawing data
            self.canvas.draw_idle()
    
    def on_release(self, event):
        self.pan_start = None
        self.end_interaction()
    
    def on_scroll(self, event):
        if event.inaxes != self.ax:
            return
        
        self.start_interaction()
        
        # Zoom to cursor position
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        
        # Calculate zoom center
        xdata, ydata = event.xdata, event.ydata
        
        # Zoom factor
        zoom_factor = 0.8 if event.step > 0 else 1.25
        
        # New limits
        x_left = xdata - (xdata - xlim[0]) * zoom_factor
        x_right = xdata + (xlim[1] - xdata) * zoom_factor
        y_bottom = ydata - (ydata - ylim[0]) * zoom_factor
        y_top = ydata + (ylim[1] - ydata) * zoom_factor
        
        new_xlim = (x_left, x_right)
        new_ylim = (y_bottom, y_top)
        
        # Show cached image during zoom
        if self.cached_image is not None:
            self.show_cached_view(new_xlim, new_ylim)
        else:
            self.ax.set_xlim(x_left, x_right)
            self.ax.set_ylim(y_bottom, y_top)
            self.canvas.draw_idle()
        
        self.end_interaction()
    
    def start_interaction(self):
        """Начинаем интерактивное взаимодействие"""
        self.is_interacting = True
        if self.render_timer:
            self.render_timer.cancel()
            self.render_timer = None
        print("Interactive mode")
    
    def end_interaction(self):
        """End interactive interaction"""
        self.is_interacting = False
        self.trigger_high_quality_render()
    
    def create_cache(self, xlim, ylim):
        """Creates raster cache for current view"""
        print("Creating raster cache...")
        
        # Create temporary figure with high resolution
        cache_fig, cache_ax = plt.subplots(figsize=self.fig.get_size_inches(), dpi=self.cache_dpi)
        
        # Filter data for cache (with large margins)
        x, y = self.plot_data
        x_min, x_max = xlim
        y_min, y_max = ylim
        
        # Large margins for cache to cover area for panning
        x_margin = (x_max - x_min) * 1.5  # Уменьшил с 2.0 до 1.5
        y_margin = (y_max - y_min) * 1.5
        
        cache_mask = ((x >= x_min - x_margin) & (x <= x_max + x_margin) & 
                     (y >= y_min - y_margin) & (y <= y_max + y_margin))
        
        if np.any(cache_mask):
            x_cache = x[cache_mask]
            y_cache = y[cache_mask]
            print(f"Caching {len(x_cache)} of {len(x)} points")
            
            # If too many points, use sampling for cache
            if len(x_cache) > 1000000:  # 1 million points max for cache
                indices = np.random.choice(len(x_cache), 1000000, replace=False)
                x_cache = x_cache[indices]
                y_cache = y_cache[indices]
                print(f"Sampling down to {len(x_cache)} points for cache")
        else:
            x_cache, y_cache = x, y
            print(f"Caching all {len(x)} points")
        
        # Draw data in cache
        self.plot_func(cache_ax, x_cache, y_cache, **self.plot_kwargs)
        
        # Set cache limits
        cache_xlim = (x_min - x_margin, x_max + x_margin)
        cache_ylim = (y_min - y_margin, y_max + y_margin)
        cache_ax.set_xlim(cache_xlim)
        cache_ax.set_ylim(cache_ylim)
        
        # Remove axes and margins
        cache_ax.set_xticks([])
        cache_ax.set_yticks([])
        cache_ax.set_axis_off()
        cache_fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
        
        # Render to array
        cache_fig.canvas.draw()
        
        # Get raster data (new matplotlib API)
        try:
            # New way (matplotlib >= 3.3)
            buf = cache_fig.canvas.buffer_rgba()
            buf = np.asarray(buf)
            # Convert RGBA to RGB
            buf = buf[:, :, :3]
        except AttributeError:
            # Old way for compatibility
            try:
                print('fallback1')
                buf = np.frombuffer(cache_fig.canvas.tostring_rgb(), dtype=np.uint8)
                buf = buf.reshape(cache_fig.canvas.get_width_height()[::-1] + (3,))
            except AttributeError:
                print('fallback2')
                # Another fallback
                buf = np.frombuffer(cache_fig.canvas.renderer.tostring_rgb(), dtype=np.uint8)
                buf = buf.reshape(cache_fig.canvas.get_width_height()[::-1] + (3,))
        
        # Save cache
        self.cached_image = buf
        self.cached_xlim = cache_xlim
        self.cached_ylim = cache_ylim
        
        plt.close(cache_fig)
        print("Raster cache created")
    
    def show_cached_view(self, xlim, ylim):
        """Shows part of cached image"""
        if self.cached_image is None:
            return
        
        # Clear axes
        self.ax.clear()
        self.ax.set_xlim(xlim)
        self.ax.set_ylim(ylim)
        
        # Calculate which part of cache to show
        cache_xlim = self.cached_xlim
        cache_ylim = self.cached_ylim
        
        # Show cached image
        self.ax.imshow(self.cached_image, extent=[cache_xlim[0], cache_xlim[1], cache_ylim[0], cache_ylim[1]], 
                      aspect='auto', interpolation='bilinear')
        
        # Set correct limits
        self.ax.set_xlim(xlim)
        self.ax.set_ylim(ylim)
        
        self.canvas.draw_idle()
    
    def trigger_high_quality_render(self):
        """Triggers delayed high-quality render"""
        if self.render_timer:
            self.render_timer.cancel()
        
        # Debounce - wait 500ms after last interaction
        self.render_timer = threading.Timer(0.5, self.delayed_render)
        self.render_timer.start()
    
    def delayed_render(self):
        """Triggers render via matplotlib's after_idle"""
        if hasattr(self.canvas, 'get_tk_widget'):
            # Tkinter backend
            self.canvas.get_tk_widget().after_idle(self.high_quality_render)
        else:
            # Other backends - just call directly
            self.high_quality_render()
    
    def high_quality_render(self):
        """High-quality render"""
        if self.is_interacting or self.plot_data is None:
            return
        
        current_xlim = self.ax.get_xlim()
        current_ylim = self.ax.get_ylim()
        
        # Проверяем, изменились ли пределы
        if (self.last_xlim == current_xlim and self.last_ylim == current_ylim):
            return
        
        print("Starting high-quality render...")
        
        # Clear plot
        self.ax.clear()
        
        # Filter data by current limits for speed
        x, y = self.plot_data
        x_min, x_max = current_xlim
        y_min, y_max = current_ylim
        
        # Slightly expand area for smoothness
        x_margin = (x_max - x_min) * 0.1
        y_margin = (y_max - y_min) * 0.1
        
        mask = ((x >= x_min - x_margin) & (x <= x_max + x_margin) & 
                (y >= y_min - y_margin) & (y <= y_max + y_margin))
        
        if np.any(mask):
            x_filtered = x[mask]
            y_filtered = y[mask]
            print(f"Rendering {len(x_filtered)} of {len(x)} points")
        else:
            x_filtered, y_filtered = x, y
            print(f"Rendering all {len(x)} points")
        
        # Render data
        self.plot_func(self.ax, x_filtered, y_filtered, **self.plot_kwargs)
        
        # Restore limits
        self.ax.set_xlim(current_xlim)
        self.ax.set_ylim(current_ylim)
        
        # Add labels
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_title(f'Fast Interactive Plot ({len(x)} points total)')
        
        # Save current limits
        self.last_xlim = current_xlim
        self.last_ylim = current_ylim
        
        # Update display
        self.canvas.draw()
        
        # Create new cache for future interactions
        self.create_cache(current_xlim, current_ylim)
        
        print("High-quality render finished")
    
    def show(self):
        """Shows the plot"""
        if self.plot_data is None:
            print("No data to display. Use set_data().")
            return
        
        plt.show()


# Example usage
if __name__ == "__main__":
    # Create large dataset
    n_points = 5000000
    print(f"Generating {n_points} points...")
    
    x = np.random.randn(n_points) * 10
    y = np.random.randn(n_points) * 10 + x * 0.5 + np.random.randn(n_points) * 3
    
    print("Creating fast interactive plot...")
    
    # Create fast interactive plot
    plotter = FastInteractivePlot(figsize=(12, 8))
    
    # Set data (scatter plot)
    plotter.set_data(x, y, plot_type='scatter', s=0.5, alpha=0.6, c='blue')
    
    # Show plot
    plotter.show()