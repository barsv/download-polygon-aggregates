
import type { Bar } from './api';

export class ChartEngine {
    canvas: HTMLCanvasElement;
    ctx: CanvasRenderingContext2D;
    bars: Bar[] = [];

    // Viewport logic
    startTime: number = 0;
    endTime: number = 0;
    minPrice: number = 0;
    maxPrice: number = 0;

    width: number = 0;
    height: number = 0;
    padding = { top: 20, right: 60, bottom: 40, left: 0 };

    constructor(canvas: HTMLCanvasElement) {
        this.canvas = canvas;
        const ctx = canvas.getContext('2d');
        if (!ctx) throw new Error("Could not get 2d context");
        this.ctx = ctx;

        this.resize();
        window.addEventListener('resize', () => this.resize());
    }

    resize() {
        this.width = this.canvas.parentElement?.clientWidth || window.innerWidth;
        this.height = this.canvas.parentElement?.clientHeight || window.innerHeight;

        // Handle high DPI
        const dpr = window.devicePixelRatio || 1;
        this.canvas.width = this.width * dpr;
        this.canvas.height = this.height * dpr;
        this.canvas.style.width = `${this.width}px`;
        this.canvas.style.height = `${this.height}px`;

        this.ctx.scale(dpr, dpr);
        this.render();
    }

    setData(bars: Bar[]) {
        this.bars = bars;
        this.autoScaleY();
        this.render();
    }

    setTimeRange(start: number, end: number) {
        this.startTime = start;
        this.endTime = end;
        this.render();
    }

    autoScaleY() {
        if (this.bars.length === 0) return;

        // Find min/max price in visible range?
        // Or just global for the chunk?
        // Let's do visible range for infinite zoom feeling (y-axis resizes as you pan)

        let min = Infinity;
        let max = -Infinity;

        // Filter bars somewhat inside range (plus some buffer)
        // Optimization: Binary search start/end indices?
        // For now, simple loop is okay for <5000 points.

        let visible = false;
        for (const bar of this.bars) {
            if (bar.time >= this.startTime && bar.time <= this.endTime) {
                if (bar.low < min) min = bar.low;
                if (bar.high > max) max = bar.high;
                visible = true;
            }
        }

        if (!visible) {
            // Fallback to all data
            for (const bar of this.bars) {
                if (bar.low < min) min = bar.low;
                if (bar.high > max) max = bar.high;
            }
        }

        if (min === Infinity) { min = 0; max = 100; }
        if (min === max) { min -= 1; max += 1; }

        // Add padding
        const range = max - min;
        this.minPrice = min - range * 0.1;
        this.maxPrice = max + range * 0.1;
    }

    // Coordinate Transformers
    timeToPixel(t: number): number {
        const duration = this.endTime - this.startTime;
        const fraction = (t - this.startTime) / duration;
        const drawWidth = this.width - this.padding.left - this.padding.right;
        return this.padding.left + fraction * drawWidth;
    }

    pixelToTime(x: number): number {
        const drawWidth = this.width - this.padding.left - this.padding.right;
        const fraction = (x - this.padding.left) / drawWidth;
        const duration = this.endTime - this.startTime;
        return this.startTime + fraction * duration;
    }

    priceToPixel(p: number): number {
        const range = this.maxPrice - this.minPrice;
        const fraction = (p - this.minPrice) / range;
        const drawHeight = this.height - this.padding.top - this.padding.bottom;
        // Y is inverted (0 is top)
        return (this.padding.top + drawHeight) - (fraction * drawHeight);
    }

    render() {
        const { width, height, ctx } = this;

        // Clear background
        ctx.fillStyle = "#1e1e1e";
        ctx.fillRect(0, 0, width, height);

        if (this.bars.length === 0) return;

        // Clip to drawing area
        ctx.save();
        ctx.beginPath();
        const drawAreaWidth = width - this.padding.right - this.padding.left;
        const drawAreaHeight = height - this.padding.bottom - this.padding.top;
        ctx.rect(this.padding.left, this.padding.top, drawAreaWidth, drawAreaHeight);
        ctx.clip();

        // 1. Draw Range Area (High - Low)
        ctx.fillStyle = "rgba(74, 144, 226, 0.1)";
        ctx.beginPath();

        let first = true;
        for (const bar of this.bars) {
            const x = this.timeToPixel(bar.time);
            const yLow = this.priceToPixel(bar.low);
            if (first) {
                ctx.moveTo(x, yLow);
                first = false;
            } else {
                ctx.lineTo(x, yLow);
            }
        }

        for (let i = this.bars.length - 1; i >= 0; i--) {
            const bar = this.bars[i];
            const x = this.timeToPixel(bar.time);
            const yHigh = this.priceToPixel(bar.high);
            ctx.lineTo(x, yHigh);
        }

        ctx.closePath();
        ctx.fill();

        // 2. Draw Close Line
        ctx.strokeStyle = "#4a90e2";
        ctx.lineWidth = 1.5;
        ctx.lineJoin = "miter";
        ctx.lineCap = "butt";

        ctx.beginPath();
        first = true;
        for (const bar of this.bars) {
            const x = this.timeToPixel(bar.time);
            const yClose = this.priceToPixel(bar.close);
            if (first) {
                ctx.moveTo(x, yClose);
                first = false;
            } else {
                ctx.lineTo(x, yClose);
            }
        }
        ctx.stroke();

        ctx.restore();

        // 3. Draw Axes
        this.drawXAxis();
        this.drawYAxis();
    }

    drawXAxis() {
        const { ctx, width, height } = this;
        ctx.strokeStyle = "rgba(255, 255, 255, 0.1)";
        ctx.lineWidth = 1;

        const y = height - this.padding.bottom;
        ctx.beginPath();
        ctx.moveTo(this.padding.left, y);
        ctx.lineTo(width - this.padding.right, y);
        ctx.stroke();

        // Ticks
        // Simple adaptive ticks
        const duration = this.endTime - this.startTime;
        const xStart = this.padding.left;
        const xEnd = width - this.padding.right;

        const possibleSteps = [
            1, 5, 10, 30, // seconds
            60, 300, 600, 1800, // minutes
            3600, 3600 * 4, 3600 * 12, // hours
            86400, 86400 * 7, 86400 * 30, 86400 * 365 // days, weeks, months, years
        ];

        // find visual pixel width per second
        // we want a tick every ~100px
        const pixelsPerSecond = (xEnd - xStart) / duration;
        const targetStepSeconds = 100 / pixelsPerSecond;

        const step = possibleSteps.find(s => s >= targetStepSeconds) || possibleSteps[possibleSteps.length - 1];

        // Align start
        let t = Math.ceil(this.startTime / step) * step;

        ctx.fillStyle = "rgba(255, 255, 255, 0.5)";
        ctx.font = "11px 'Inter', sans-serif";
        ctx.textAlign = "center";

        while (t <= this.endTime) {
            const x = this.timeToPixel(t);
            if (x >= xStart && x <= xEnd) {
                ctx.beginPath();
                ctx.moveTo(x, y);
                ctx.lineTo(x, y + 5);
                ctx.stroke();

                // Format date
                const date = new Date(t * 1000);
                let label = "";
                if (step < 60) label = date.toLocaleTimeString(); // seconds
                else if (step < 86400) label = date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
                else label = date.toLocaleDateString();

                ctx.fillText(label, x, y + 15);
            }
            t += step;
        }
    }

    drawYAxis() {
        const { ctx, width, height } = this;
        ctx.strokeStyle = "rgba(255, 255, 255, 0.1)";
        ctx.beginPath();
        const x = width - this.padding.right;
        ctx.moveTo(x, this.padding.top);
        ctx.lineTo(x, height - this.padding.bottom);
        ctx.stroke();

        // Ticks
        const range = this.maxPrice - this.minPrice;
        const heightPixels = height - this.padding.top - this.padding.bottom;
        const targetStep = range / (heightPixels / 50); // every 50px

        // Round to nice number logic omitted for brevity, simple systematic
        const step = Math.pow(10, Math.floor(Math.log10(targetStep)));
        const niceStep = targetStep / step < 2 ? step : (targetStep / step < 5 ? step * 2 : step * 5);

        let p = Math.ceil(this.minPrice / niceStep) * niceStep;

        ctx.fillStyle = "rgba(255, 255, 255, 0.5)";
        ctx.font = "11px 'Inter', sans-serif";
        ctx.textAlign = "left";

        while (p <= this.maxPrice) {
            const y = this.priceToPixel(p);
            if (y >= this.padding.top && y <= height - this.padding.bottom) {
                ctx.beginPath();
                ctx.moveTo(x, y);
                ctx.lineTo(x + 5, y);
                ctx.stroke();

                ctx.fillText(p.toFixed(2), x + 8, y + 3);

                // Grid line
                ctx.save();
                ctx.strokeStyle = "rgba(255, 255, 255, 0.05)";
                ctx.setLineDash([2, 4]);
                ctx.beginPath();
                ctx.moveTo(this.padding.left, y);
                ctx.lineTo(x, y);
                ctx.stroke();
                ctx.restore();
            }
            p += niceStep;
        }
    }
}
