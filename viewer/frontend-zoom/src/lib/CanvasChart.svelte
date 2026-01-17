
<script lang="ts">
    import { onMount, onDestroy } from 'svelte';
    import { ChartEngine } from './ChartEngine';
    import type { Bar } from './api';

    export let bars: Bar[] = [];
    export let startTime: number;
    export let endTime: number;
    export let onViewportChange: (start: number, end: number) => void;

    let canvas: HTMLCanvasElement;
    let engine: ChartEngine;
    
    // Interaction handling
    let isDragging = false;
    let lastX = 0;

    onMount(() => {
        engine = new ChartEngine(canvas);
        engine.setTimeRange(startTime, endTime);
        if (bars.length > 0) engine.setData(bars);
    });

    $: if (engine && bars) {
        engine.setData(bars);
    }
    $: if (engine && (startTime !== engine.startTime || endTime !== engine.endTime)) {
        engine.setTimeRange(startTime, endTime);
    }

    function handleWheel(e: WheelEvent) {
        e.preventDefault();
        
        // TradingView style:
        // shiftKey + Wheel -> Scroll (Pan) in TV, but standard trackpad use is:
        // Two fingers horizontal -> deltaX -> Pan
        // Two fingers vertical -> deltaY -> Zoom (or Pan if ctrl not pressed, but user asked for zoom)
        // User requested: "vertical movements answer for zoom, horizontal for pan"
        
        // 1. Horizontal Pan
        if (Math.abs(e.deltaX) > 0) {
            // Pan logic
            // Calculate dt per pixel
            const t1 = engine.pixelToTime(0);
            const t2 = engine.pixelToTime(1);
            const dtPerPx = t2 - t1;
            
            // e.deltaX is usually pixels scrolled
            const dt = e.deltaX * dtPerPx; // Scroll right (positive) -> move "camera" right -> effectively move window right? 
            // In trackpad: swipe left (deltaX > 0) means move content left? 
            // Actually, usually:
            // Swipe two fingers LEFT -> DeltaX > 0 (scrolling right) -> Text moves LEFT.
            // For chart: If I swipe LEFT, I expect to see FUTURE (move viewport RIGHT).
            // So Viewport start/end should INCREASE.
            
            onViewportChange(startTime + dt, endTime + dt);
        }

        // 2. Vertical Zoom
        if (Math.abs(e.deltaY) > 0) {
             // Zoom centered on mouse
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const timeAtMouse = engine.pixelToTime(x);
            
            // Scale factor
            // deltaY is often ~100 per tick or much smaller for trackpad.
            // Sensible zoom intensity
            const zoomIntensity = 0.001 * Math.abs(e.deltaY); 
            // Cap intensity
            const safeIntensity = Math.min(Math.max(zoomIntensity, 0.01), 0.5);
            
            const scale = e.deltaY > 0 ? (1 + safeIntensity) : (1 - safeIntensity);
            
            const duration = endTime - startTime;
            const newDuration = duration * scale;
            
            // Pivot around mouse
            const leftRatio = (timeAtMouse - startTime) / duration;
            
            const newStartTime = timeAtMouse - (newDuration * leftRatio);
            const newEndTime = timeAtMouse + (newDuration * (1 - leftRatio));
            
            onViewportChange(newStartTime, newEndTime);
        }
    }
    
    function handlePointerDown(e: PointerEvent) {
        isDragging = true;
        lastX = e.clientX;
        canvas.setPointerCapture(e.pointerId);
    }
    
    function handlePointerMove(e: PointerEvent) {
        if (!isDragging) return;
        
        const dx = e.clientX - lastX;
        lastX = e.clientX;
        
        // Convert pixel delta to time delta
        const duration = endTime - startTime;
        const width = canvas.width / (window.devicePixelRatio || 1); // logical pixels
        const secondsPerPixel = duration / width; // approximately
        
        // Logic inside engine might use padding. 
        // Better:
        const t1 = engine.pixelToTime(0);
        const t2 = engine.pixelToTime(1);
        const dtPerPx = t2 - t1;
        
        const dt = -dx * dtPerPx; // Drag right -> move time left (subtract)
        
        onViewportChange(startTime + dt, endTime + dt);
    }
    
    function handlePointerUp(e: PointerEvent) {
        isDragging = false;
        canvas.releasePointerCapture(e.pointerId);
    }

</script>

<div class="chart-container">
    <canvas 
        bind:this={canvas} 
        on:wheel={handleWheel}
        on:pointerdown={handlePointerDown}
        on:pointermove={handlePointerMove}
        on:pointerup={handlePointerUp}
        on:pointercancel={handlePointerUp}
    ></canvas>
</div>

<style>
    .chart-container {
        width: 100%;
        height: 100%;
        position: relative;
        overflow: hidden;
        background: #1e1e1e;
    }
    canvas {
        display: block;
        width: 100%;
        height: 100%;
        cursor: crosshair;
    }
</style>
