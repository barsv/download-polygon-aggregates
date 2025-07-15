└── website
    └── tutorials
        ├── _usage-guide-partial.mdx
        ├── a11y
            ├── _category_.yml
            ├── assets
            │   └── a11y-chart.html
            ├── conclusion.mdx
            ├── intro.mdx
            ├── keyboard.mdx
            ├── readability.mdx
            └── screenreader.mdx
        ├── analysis-indicators.mdx
        ├── customization
            ├── .eslintrc.js
            ├── _apply-options-tabs-partial.mdx
            ├── _category_.yml
            ├── _iterative-guide-warning-partial.mdx
            ├── assets
            │   ├── start.html
            │   ├── step1.html
            │   ├── step10.html
            │   ├── step2.html
            │   ├── step3.html
            │   ├── step4.html
            │   ├── step5.html
            │   ├── step6.html
            │   ├── step7.html
            │   ├── step8.html
            │   └── step9.html
            ├── chart-colors.mdx
            ├── conclusion.mdx
            ├── creating-a-chart.mdx
            ├── crosshair.mdx
            ├── data-points.mdx
            ├── finishing-touches.mdx
            ├── intro.mdx
            ├── price-format.mdx
            ├── price-scale.mdx
            ├── second-series.mdx
            ├── series.mdx
            └── time-scale.mdx
        ├── demos
            ├── .eslintrc.js
            ├── compare-multiple-series.js
            ├── compare-multiple-series.mdx
            ├── custom-font-family.js
            ├── custom-font-family.mdx
            ├── custom-locale.js
            ├── custom-locale.mdx
            ├── infinite-history.js
            ├── infinite-history.mdx
            ├── moving-average.js
            ├── moving-average.mdx
            ├── range-switcher.js
            ├── range-switcher.mdx
            ├── realtime-updates.js
            ├── realtime-updates.mdx
            ├── whitespace.js
            ├── whitespace.mdx
            ├── yield-curve-with-update-markers.js
            └── yield-curve-with-update-markers.mdx
        ├── how_to
            ├── .eslintrc.js
            ├── _usage-guide-partial.mdx
            ├── horizontal-price-scale.js
            ├── horizontal-price-scale.mdx
            ├── inverted-price-scale.js
            ├── inverted-price-scale.mdx
            ├── legend-3line.js
            ├── legend.js
            ├── legends.mdx
            ├── no-time-scale.js
            ├── panes.js
            ├── panes.mdx
            ├── price-and-volume.js
            ├── price-and-volume.mdx
            ├── price-line.js
            ├── price-line.mdx
            ├── series-markers.js
            ├── series-markers.mdx
            ├── set-crosshair-position-syncing.js
            ├── set-crosshair-position-tracking.js
            ├── set-crosshair-position.mdx
            ├── tooltip-floating.js
            ├── tooltip-magnifier.js
            ├── tooltip-tracking.js
            ├── tooltips.mdx
            ├── two-price-scales.js
            ├── two-price-scales.mdx
            ├── watermark-advanced.js
            ├── watermark-simple.js
            └── watermark.mdx
        ├── index.mdx
        ├── react
            ├── 01-simple.mdx
            ├── 02-advanced.mdx
            └── _category_.yml
        ├── vuejs
            ├── 01-wrapper.mdx
            ├── _category_.yml
            └── assets
            │   ├── .eslintrc.js
            │   ├── app.vue
            │   ├── composition-api.vue
            │   ├── options-api.vue
            │   └── web-component.js
        └── webcomponents
            ├── 01-custom-element.mdx
            ├── _category_.yml
            └── assets
                ├── .eslintrc.js
                ├── lw-chart.js
                └── wc-example.js


/website/tutorials/_usage-guide-partial.mdx:
--------------------------------------------------------------------------------
 1 | <details>
 2 | <summary>How to use the code sample</summary>
 3 | <strong>The code presented below requires:</strong>
 4 | 
 5 | - That `createChart` has already been imported. See [Getting Started](/docs#creating-a-chart) for more information,
 6 | - and that there is an html div element on the page with an `id` of `container`.
 7 | 
 8 | Here is an example skeleton setup: [Code Sandbox](https://codesandbox.io/s/lightweight-charts-skeleton-n67pm6).
 9 | You can paste the provided code below the `// REPLACE EVERYTHING BELOW HERE` comment.
10 | 
11 | :::tip
12 | 
13 | Some code may be hidden to improve readability. Toggle the checkbox above the code block to reveal all the code.
14 | 
15 | :::
16 | </details>
17 | 


--------------------------------------------------------------------------------
/website/tutorials/a11y/_category_.yml:
--------------------------------------------------------------------------------
1 | label: "Accessibility"
2 | 


--------------------------------------------------------------------------------
/website/tutorials/a11y/assets/a11y-chart.html:
--------------------------------------------------------------------------------
  1 | <!DOCTYPE html>
  2 | <html>
  3 | 
  4 | <head>
  5 | 	<meta charset="UTF-8" />
  6 | 	<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0" />
  7 | 	<title>Lightweight Charts™ A11y Tutorial</title>
  8 | 	<script type="text/javascript"
  9 | 		src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"></script>
 10 | 	<style>
 11 | 		:host {
 12 | 			display: block;
 13 | 			font-family: -apple-system, BlinkMacSystemFont, 'Trebuchet MS', Roboto,
 14 | 				Ubuntu, sans-serif;
 15 | 		}
 16 | 
 17 | 		:host[hidden] {
 18 | 			display: none;
 19 | 		}
 20 | 
 21 | 		#example {
 22 | 			display: flex;
 23 | 			flex-direction: column;
 24 | 			height: 100%;
 25 | 			width: 100%;
 26 | 		}
 27 | 
 28 | 		#chart {
 29 | 			flex-grow: 1;
 30 | 		}
 31 | 
 32 | 		.buttons {
 33 | 			display: inline-flex;
 34 | 			flex-wrap: wrap;
 35 | 			flex-direction: row;
 36 | 			padding-inline: 30px;
 37 | 			gap: 8px;
 38 | 		}
 39 | 
 40 | 		button {
 41 | 			all: initial;
 42 | 			font-family: -apple-system, BlinkMacSystemFont, 'Trebuchet MS', Roboto,
 43 | 				Ubuntu, sans-serif;
 44 | 			font-size: 16px;
 45 | 			font-style: normal;
 46 | 			line-height: 24px;
 47 | 			/* 150% */
 48 | 			letter-spacing: -0.32px;
 49 | 			padding: 8px 24px;
 50 | 			color: #fff;
 51 | 			background-color: rgba(41, 98, 255, 1);
 52 | 			border-radius: 8px;
 53 | 			cursor: pointer;
 54 | 		}
 55 | 
 56 | 		button:hover {
 57 | 			background-color: rgba(30, 83, 229, 1);
 58 | 		}
 59 | 
 60 | 		button:active {
 61 | 			background-color: rgba(24, 72, 204, 1);
 62 | 		}
 63 | 
 64 | 		button.grey {
 65 | 			color: rgba(19, 23, 34, 1);
 66 | 			background-color: rgba(240, 243, 250, 1);
 67 | 		}
 68 | 
 69 | 		button.grey:hover {
 70 | 			background-color: rgba(224, 227, 235, 1);
 71 | 		}
 72 | 
 73 | 		button.grey:active {
 74 | 			background-color: rgba(209, 212, 220, 1);
 75 | 		}
 76 | 
 77 | 		#chart {
 78 | 			height: var(--lwchart-height, 240px);
 79 | 			border-radius: 8px;
 80 | 		}
 81 | 
 82 | 		#chart:focus,
 83 | 		button:focus {
 84 | 			outline-offset: 3px;
 85 | 			outline: blue;
 86 | 			outline-style: solid;
 87 | 			outline-width: 3px;
 88 | 		}
 89 | 
 90 | 		key {
 91 | 			display: inline-block;
 92 | 			width: 18px;
 93 | 			margin: 3px 5px 3px 0px;
 94 | 			font-weight: 590;
 95 | 			text-align: center;
 96 | 			color: #000;
 97 | 			background-color: #fff;
 98 | 			border: 2px solid rgba(0, 0, 0, 0.25);
 99 | 			border-radius: 2px;
100 | 		}
101 | 
102 | 		*[role='alert'] {
103 | 			position: absolute;
104 | 			opacity: 0;
105 | 			pointer-events: none;
106 | 		}
107 | 
108 | 		.tooltip {
109 | 			position: absolute;
110 | 			font-family: -apple-system, BlinkMacSystemFont, 'Trebuchet MS', Roboto,
111 | 				Ubuntu, sans-serif;
112 | 			pointer-events: none;
113 | 			left: 10px;
114 | 			top: 10px;
115 | 			border-radius: 5px;
116 | 			background-color: rgba(0, 0, 0, 0.8);
117 | 			color: white;
118 | 			padding: 5px 10px;
119 | 			z-index: 10;
120 | 			opacity: 0;
121 | 		}
122 | 
123 | 		label {
124 | 			font-family: -apple-system, BlinkMacSystemFont, 'Trebuchet MS', Roboto,
125 | 				Ubuntu, sans-serif;
126 | 		}
127 | 
128 | 		.group {
129 | 			display: inline-block;
130 | 			padding: 8px 8px;
131 | 			border-radius: 8px;
132 | 			border: 2px solid rgba(0, 0, 0, 0.25);
133 | 		}
134 | 
135 | 		input[type="checkbox"],
136 | 		input[type="checkbox"]+label {
137 | 			cursor: pointer;
138 | 		}
139 | 	</style>
140 | </head>
141 | 
142 | <body>
143 | 	<div id="example">
144 | 		<div class="buttons">
145 | 			<button id="random-data-button" type="button" tabindex="0">
146 | 				Randomise Data
147 | 			</button>
148 | 			<div class="group">
149 | 				<input type="checkbox" id="high-contrast-checkbox" tabindex="0" />
150 | 				<label for="high-contrast-checkbox">Toggle Higher Contrast</label>
151 | 			</div>
152 | 			<div class="group">
153 | 				<input type="checkbox" id="large-font-checkbox" tabindex="0" />
154 | 				<label for="large-font-checkbox">Toggle Larger Font</label>
155 | 			</div>
156 | 		</div>
157 | 		<figure id="chart"></figure>
158 | 	</div>
159 | 	<div class="buttons">
160 | 		<button id="reset-chart-button" type="button" tabindex="0">
161 | 			Reset Chart
162 | 		</button>
163 | 	</div>
164 | 
165 | 	<template id="status-tooltip-content"><span>Press <key>h</key>to list commands</span></template>
166 | 	<template id="status-tooltip-expanded-content"><span>
167 | 			<key>h</key>hide commands
168 | 		</span><br />
169 | 		<span>
170 | 			<key>←</key>move backwards
171 | 		</span><br />
172 | 		<span>
173 | 			<key>→</key>move forwards
174 | 		</span><br />
175 | 		<span>
176 | 			<key>↑</key>zoom in
177 | 		</span><br />
178 | 		<span>
179 | 			<key>↓</key>zoom out
180 | 		</span></template>
181 | 	<!-- Template for HTML elements added to the chart container for the A11y improvements -->
182 | 	<template id="a11y-helpers">
183 | 		<div tabindex="-1" role="alert" aria-live="assertive"></div>
184 | 		<div class="tooltip" tabindex="-1" aria-hidden="true"></div>
185 | 	</template>
186 | 
187 | 	<script type="text/javascript">
188 | 		const { createChart, LineSeries } = LightweightCharts;
189 | 		function generateSampleData() {
190 | 			const randomFactor = 25 + Math.random() * 25;
191 | 			const samplePoint = i =>
192 | 				i *
193 | 				(0.5 +
194 | 					Math.sin(i / 10) * 0.2 +
195 | 					Math.sin(i / 20) * 0.4 +
196 | 					Math.sin(i / randomFactor) * 0.8 +
197 | 					Math.sin(i / 500) * 0.5) +
198 | 				200;
199 | 
200 | 			const res = [];
201 | 			const date = new Date(Date.UTC(2018, 0, 1, 0, 0, 0, 0));
202 | 			const numberOfPoints = 500;
203 | 			for (let i = 0; i < numberOfPoints; ++i) {
204 | 				const time = date.getTime() / 1000;
205 | 				const value = samplePoint(i);
206 | 
207 | 				res.push({
208 | 					time,
209 | 					value,
210 | 				});
211 | 
212 | 				date.setUTCDate(date.getUTCDate() + 1);
213 | 			}
214 | 
215 | 			return res;
216 | 		}
217 | 
218 | 		const seriesBaseContrastSettings = {
219 | 			color: 'rgb(41, 98, 255)',
220 | 			lineWidth: 2,
221 | 		};
222 | 		const chartBaseContrastSettings = {
223 | 			layout: {
224 | 				textColor: '#191919',
225 | 			},
226 | 			grid: {
227 | 				vertLines: {
228 | 					color: '#D6DCDE',
229 | 				},
230 | 				horzLines: {
231 | 					color: '#D6DCDE',
232 | 				},
233 | 			},
234 | 		};
235 | 		const seriesHighContrastSettings = {
236 | 			color: 'rgb(0, 0, 0)',
237 | 			lineWidth: 4,
238 | 		};
239 | 		const chartHighContrastSettings = {
240 | 			layout: {
241 | 				textColor: '#000000',
242 | 			},
243 | 			grid: {
244 | 				vertLines: {
245 | 					color: '#777777',
246 | 				},
247 | 				horzLines: {
248 | 					color: '#777777',
249 | 				},
250 | 			},
251 | 		};
252 | 
253 | 		const chart = createChart('chart', {
254 | 			autoSize: true,
255 | 			timeScale: {
256 | 				rightOffset: 20,
257 | 				barSpacing: 3,
258 | 			},
259 | 		});
260 | 
261 | 		const mainSeries = chart.addSeries(LineSeries, {
262 | 			priceFormat: {
263 | 				minMove: 1,
264 | 				precision: 0,
265 | 			},
266 | 			title: 'A11y',
267 | 		});
268 | 
269 | 		mainSeries.setData(generateSampleData());
270 | 
271 | 		function setHighContrast(enabled) {
272 | 			mainSeries.applyOptions(
273 | 				enabled ? seriesHighContrastSettings : seriesBaseContrastSettings
274 | 			);
275 | 			chart.applyOptions(
276 | 				enabled ? chartHighContrastSettings : chartBaseContrastSettings
277 | 			);
278 | 		}
279 | 
280 | 		function setFontSize(large) {
281 | 			chart.applyOptions({
282 | 				layout: {
283 | 					fontSize: large ? 16 : 12,
284 | 				},
285 | 			});
286 | 		}
287 | 
288 | 		// Check if user prefers high contrast mode
289 | 		function checkHighContrast() {
290 | 			// Use window.matchMedia to check 'prefers-contrast' media feature
291 | 			const highContrast = window.matchMedia(
292 | 				'(prefers-contrast: high)'
293 | 			).matches;
294 | 			return highContrast; // returns true if high contrast is enabled, false otherwise
295 | 		}
296 | 
297 | 		if (checkHighContrast()) {
298 | 			setHighContrast(true);
299 | 			document.getElementById('high-contrast-checkbox').checked = true;
300 | 		}
301 | 		setFontSize(false);
302 | 
303 | 		document
304 | 			.querySelector('#random-data-button')
305 | 			?.addEventListener('click', () => {
306 | 				mainSeries.setData(generateSampleData());
307 | 			});
308 | 		document
309 | 			.querySelector('#high-contrast-checkbox')
310 | 			?.addEventListener('change', event => {
311 | 				setHighContrast(event.target.checked);
312 | 			});
313 | 		document
314 | 			.querySelector('#large-font-checkbox')
315 | 			?.addEventListener('change', event => {
316 | 				setFontSize(event.target.checked);
317 | 			});
318 | 		document
319 | 			.querySelector('#reset-chart-button')
320 | 			?.addEventListener('click', () => {
321 | 				chart.timeScale().resetTimeScale();
322 | 				mainSeries.priceScale().applyOptions({
323 | 					autoScale: true,
324 | 				});
325 | 			});
326 | 
327 | 		function formatDate(time) {
328 | 			return new Date(time * 1000).toDateString();
329 | 		}
330 | 
331 | 		function formatValue(value) {
332 | 			return `${value < 0 ? '-' : ''}${Math.abs(value).toFixed(2)}`;
333 | 		}
334 | 
335 | 		function getStats(data) {
336 | 			const stats = {
337 | 				start: data[0],
338 | 				close: data[data.length - 1],
339 | 				low: data[0],
340 | 				high: data[0],
341 | 			};
342 | 
343 | 			for (const point of data) {
344 | 				if (point.value > stats.high.value) {
345 | 					stats.high = point;
346 | 				}
347 | 				if (point.value < stats.low.value) {
348 | 					stats.low = point;
349 | 				}
350 | 			}
351 | 
352 | 			return stats;
353 | 		}
354 | 
355 | 		function getVisibleSeriesData(chart, series) {
356 | 			const timeScale = chart.timeScale();
357 | 			const visibleRange = timeScale.getVisibleLogicalRange();
358 | 			const data = [];
359 | 			for (let i = Math.round(visibleRange.from); i <= visibleRange.to; i++) {
360 | 				const d = series.dataByIndex(i, 0);
361 | 				if (d !== null) {
362 | 					data.push(d);
363 | 				}
364 | 			}
365 | 			return data;
366 | 		}
367 | 
368 | 		function describeFinanceChart(data) {
369 | 			if (!data || data.length === 0) {
370 | 				return 'The data set is empty.';
371 | 			}
372 | 
373 | 			const stats = getStats(data);
374 | 
375 | 			const firstPrice = `The first price is ${formatValue(
376 | 				stats.start.value
377 | 			)} at ${formatDate(stats.start.time)}.`;
378 | 			const lastPrice = `The last price is ${formatValue(
379 | 				stats.close.value
380 | 			)} at ${formatDate(stats.close.time)}.`;
381 | 
382 | 			const actualChange = stats.close.value - stats.start.value;
383 | 			const percentChange = (actualChange / stats.start.value) * 100;
384 | 
385 | 			const changeDescription = `The actual change in price was ${formatValue(
386 | 				actualChange
387 | 			)}, corresponding to a percentage change of ${percentChange.toFixed(
388 | 				2
389 | 			)}%.`;
390 | 
391 | 			let lowHigh = '';
392 | 			if (
393 | 				stats.low.time !== stats.start.time &&
394 | 				stats.low.time !== stats.close.time
395 | 			) {
396 | 				lowHigh += `The lowest price was ${formatValue(
397 | 					stats.low.value
398 | 				)} at ${formatDate(stats.low.time)}.`;
399 | 			}
400 | 			if (
401 | 				stats.high.time !== stats.start.time &&
402 | 				stats.high.time !== stats.close.time
403 | 			) {
404 | 				lowHigh += ` The highest price was ${formatValue(
405 | 					stats.high.value
406 | 				)} at ${formatDate(stats.high.time)}.`;
407 | 			}
408 | 
409 | 			return `${firstPrice} ${lastPrice} ${changeDescription} ${lowHigh}`.trim();
410 | 		}
411 | 
412 | 		function makeA11y(chart, series) {
413 | 			const containerEl = chart.chartElement().parentElement;
414 | 			if (!containerEl) return;
415 | 			// make focusable
416 | 			containerEl.tabIndex = 0;
417 | 			containerEl.style.position = 'relative';
418 | 			containerEl.ariaLabel =
419 | 				'Line plot of Accessibility stock price. Press the H key to display the available interaction keys.';
420 | 			chart.chartElement().ariaHidden = 'true';
421 | 
422 | 			const templateElement = document.getElementById('a11y-helpers');
423 | 			const clone = templateElement.content.cloneNode(true);
424 | 			containerEl.appendChild(clone);
425 | 			const alerter = containerEl.querySelector('[role="alert"]');
426 | 			const tooltip = containerEl.querySelector('.tooltip');
427 | 
428 | 			let tooltipDetailedVisible = false;
429 | 
430 | 			function shiftChart(diff) {
431 | 				const currentPos = chart.timeScale().scrollPosition();
432 | 				chart.timeScale().scrollToPosition(currentPos + diff, false);
433 | 			}
434 | 
435 | 			function scaleChart(pct, zoomIn) {
436 | 				const currentRange = chart.timeScale().getVisibleLogicalRange();
437 | 				if (currentRange) {
438 | 					const bars = currentRange.to - currentRange.from;
439 | 					const direction = zoomIn ? -1 : 1;
440 | 					const newRangeBars = bars * pct * direction + bars;
441 | 					chart.timeScale().setVisibleLogicalRange({
442 | 						to: currentRange.to,
443 | 						from: currentRange.to - newRangeBars,
444 | 					});
445 | 				}
446 | 			}
447 | 
448 | 			function setTooltipContentFromTemplate(id) {
449 | 				const tooltipContent = document
450 | 					.querySelector(id)
451 | 					.content.cloneNode(true);
452 | 				tooltip.innerHTML = '';
453 | 				tooltip.appendChild(tooltipContent);
454 | 			}
455 | 
456 | 			containerEl.addEventListener('focusin', () => {
457 | 				tooltipDetailedVisible = false;
458 | 				setTooltipContentFromTemplate('#status-tooltip-content');
459 | 				tooltip.style.opacity = '1';
460 | 			});
461 | 			containerEl.addEventListener('focusout', () => {
462 | 				tooltip.innerHTML = '';
463 | 				tooltip.style.opacity = '0';
464 | 			});
465 | 			containerEl.addEventListener('keydown', e => {
466 | 				const keys = [
467 | 					'h',
468 | 					'ArrowLeft',
469 | 					'ArrowRight',
470 | 					'ArrowUp',
471 | 					'ArrowDown',
472 | 					' ',
473 | 				];
474 | 				if (keys.includes(e.key)) {
475 | 					e.preventDefault();
476 | 				}
477 | 				switch (e.key) {
478 | 					case 'h':
479 | 						alerter.innerText = `Press space to describe the chart.
480 |                                 Press left arrow to move backwards.
481 |                                 Press right arrow to move forwards.
482 |                                 Press up arrow to zoom in.
483 |                                 Press down arrow to zoom out.
484 |                                 `;
485 | 						tooltipDetailedVisible = !tooltipDetailedVisible;
486 | 						if (tooltipDetailedVisible) {
487 | 							setTooltipContentFromTemplate(
488 | 								'#status-tooltip-expanded-content'
489 | 							);
490 | 						} else {
491 | 							setTooltipContentFromTemplate('#status-tooltip-content');
492 | 						}
493 | 						break;
494 | 					case 'ArrowLeft':
495 | 						shiftChart(-10);
496 | 						break;
497 | 					case 'ArrowRight':
498 | 						shiftChart(10);
499 | 						break;
500 | 					case 'ArrowUp':
501 | 						scaleChart(1 / 8, true);
502 | 						break;
503 | 					case 'ArrowDown':
504 | 						scaleChart(1 / 8, false);
505 | 						break;
506 | 					case ' ':
507 | 						const data = getVisibleSeriesData(chart, mainSeries);
508 | 						alerter.innerText = describeFinanceChart(data);
509 | 						break;
510 | 					default:
511 | 						break;
512 | 				}
513 | 			});
514 | 		}
515 | 
516 | 		makeA11y(chart, mainSeries);
517 | 	</script>
518 | </body>
519 | 
520 | </html>
521 | 


--------------------------------------------------------------------------------
/website/tutorials/a11y/conclusion.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 4
 3 | title: Conclusion
 4 | pagination_title: Conclusion
 5 | sidebar_label: Conclusion
 6 | description: Conclusion to the accessibility tutorial
 7 | keywords:
 8 |   - a11y
 9 |   - accessibility
10 |   - screenreaders
11 |   - keyboard
12 |   - assistive
13 | pagination_prev: a11y/readability
14 | pagination_next: null
15 | ---
16 | 
17 | # Conclusion
18 | 
19 | This tutorial demonstrated a wide array of accessibility improvements that can
20 | be introduced to line charts, making them usable for a broader spectrum of
21 | users. The considerations and methods presented illustrate the importance of
22 | creating inclusive web applications.
23 | 
24 | Among the discussed topics were:
25 | 
26 | 1. **Keyboard navigation:** The implementation of
27 | keyboard-only navigation on our chart, allowing for interaction exclusively
28 | through keystrokes.
29 | 2. **ARIA roles and descriptive content:** The additions of ARIA
30 | labels, live regions, and the hiding of non-consequential elements to enhance
31 | the usefulness of assistive technologies and to communicate context better to
32 | all users.
33 | 3. **High contrast and scalable font size:** The detection of the user's
34 | preference for higher contrast and the inclusion of customizable text sizes for
35 | better readability.
36 | 
37 | The example provided has even more improvements not directly discussed during the
38 | the tutorial. One such enhancement is an informative tooltip that lists available
39 | commands, adding another helpful layer of user instruction.
40 | 
41 | :::tip
42 | 
43 | The complete example code provides further insights, and reviewing it is
44 | recommended for a comprehensive understanding of the accessibility improvements
45 | discussed in this tutorial.
46 | 
47 | :::
48 | 
49 | This tutorial aimed to foster a better understanding of these practices,
50 | promoting an inclusive web where applications are made with everyone in mind.
51 | Thank you for following along and continue putting accessibility at the
52 | forefront of your web development endeavors.
53 | 
54 | ## Complete example
55 | 
56 | You can view the example in a new window, or download the source file below:
57 | 
58 | <ul>
59 | 	<li>
60 | 		<a
61 | 			href={require('!!file-loader!./assets/a11y-chart.html').default}
62 | 			target="\_blank"
63 | 		>
64 | 			View in a new window
65 | 		</a>
66 | 	</li>
67 | 	<li>
68 | 		<a
69 | 			href={require('!!file-loader!./assets/a11y-chart.html').default}
70 | 			download="a11y-chart.html"
71 | 			target="\_blank"
72 | 		>
73 | 			Download the file
74 | 		</a>
75 | 	</li>
76 | </ul>
77 | 


--------------------------------------------------------------------------------
/website/tutorials/a11y/intro.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_position: 0
  3 | sidebar_label: Introduction
  4 | pagination_title: Introduction
  5 | title: Improving accessibility
  6 | description:
  7 |   This tutorial provides an introduction to making a Lightweight Charts™' chart
  8 |   more accessible.
  9 | keywords:
 10 |   - a11y
 11 |   - accessibility
 12 |   - screenreaders
 13 |   - keyboard
 14 |   - assistive
 15 | pagination_prev: null
 16 | pagination_next: a11y/keyboard
 17 | ---
 18 | 
 19 | # Improving accessibility
 20 | 
 21 | ## Introduction
 22 | 
 23 | This tutorial introduces how to make charts with Lightweight Charts™ more
 24 | accessible. Lightweight Charts™ does not have built-in accessibility attributes
 25 | and behaviors. This gives you the flexibility to customize and implement them on
 26 | your own, seamlessly integrating the charts into your site's existing
 27 | accessibility policy.
 28 | 
 29 | :::info
 30 | 
 31 | The tutorial serves as a starting point and provides ideas
 32 | for creating a fully accessible chart based on your users' needs. **It is not
 33 | intended to be a comprehensive tutorial.**
 34 | 
 35 | :::
 36 | 
 37 | Graphical data representation, although visually appealing and informative, can
 38 | sometimes pose challenges to individuals with varying abilities and needs. In
 39 | line with the principles of inclusivity and universal design, we aim to
 40 | demonstrate how to make your charts more accessible to a broader audience.
 41 | 
 42 | ## What we will be building
 43 | 
 44 | Before we get started, let us have a look at what we will be building in this
 45 | tutorial.
 46 | 
 47 | {/*
 48 |   note: iframe won't display correctly when using `docusaurus serve`,
 49 |   however it works correctly when hosted. https://github.com/facebook/docusaurus/issues/7991
 50 | */}
 51 | 
 52 | <iframe
 53 | 	className="standalone-iframe h400"
 54 | 	src={require('!!file-loader!./assets/a11y-chart.html').default}
 55 | ></iframe>
 56 | <ul>
 57 | 	<li>
 58 | 		<a
 59 | 			href={require('!!file-loader!./assets/a11y-chart.html').default}
 60 | 			target="\_blank"
 61 | 		>
 62 | 			View in a new window
 63 | 		</a>
 64 | 	</li>
 65 | 	<li>
 66 | 		<a
 67 | 			href={require('!!file-loader!./assets/a11y-chart.html').default}
 68 | 			download="a11y-chart.html"
 69 | 			target="\_blank"
 70 | 		>
 71 | 			Download the file
 72 | 		</a>
 73 | 	</li>
 74 | </ul>
 75 | 
 76 | ## Topics to be covered
 77 | 
 78 | The following topics will be covered within the tutorial:
 79 | 
 80 | - **Enabling Keyboard Navigation:** Keyboard users predominantly interact with
 81 |   web content using only their keyboard. We will guide you on setting up
 82 |   keyboard navigation for our charts, thereby providing a seamless user
 83 |   experience.
 84 | - **Implementing ARIA (Accessible Rich Internet Applications) Suite:** We'll
 85 |   delve into how to integrate ARIA attributes which aid in improving the access
 86 |   and understanding of our charts for users with disabilities.
 87 | - **Generating Descriptive Content for Charts:** Often, providing a textual
 88 |   description for charts becomes invaluable for certain users, especially for
 89 |   those using screen reading technology. We demonstrate how to automate this
 90 |   process and facilitate a more comprehensive understanding of data being
 91 |   represented.
 92 | 
 93 | ## Prerequisite knowledge
 94 | 
 95 | To fully benefit from this guide, we assume that you are already familiar with:
 96 | 
 97 | - Basic HTML structure and elements.
 98 | - JavaScript fundamentals, especially event handling.
 99 | - The basics of using the Lightweight Charts™ JavaScript library, including chart
100 |   creation and providing data.
101 | 
102 | :::tip
103 | 
104 | The tutorial will assume that you've already read the [Getting Started](/docs)
105 | section. Additionally it is recommended that you read the
106 | [Customization tutorial](/tutorials/customization/intro)
107 | 
108 | :::
109 | 
110 | ## Terminology
111 | 
112 | - **Accessibility:** The practice of making your websites usable by as many
113 |   people as possible, including individuals with disabilities or special needs.
114 | - **ARIA (Accessible Rich Internet Applications):** A set of attributes that
115 |   define ways to make web content and web applications more accessible to people
116 |   with disabilities.
117 | - **Assistive technologies:** Software or devices that people with disabilities
118 |   use to improve interaction with the web, such as screen readers, alternative
119 |   keyboards, or speech recognition software.
120 | - **Keyboard Navigation:** The ability to navigate through a website using only
121 |   the keyboard, which is important for those who cannot use a mouse.
122 | - **High Contrast Mode:** A version of a webpage that has been designed to be
123 |   easy on the eyes and readable, typically with black text on a white
124 |   background, used by people with visual impairments.
125 | - **Media Queries:** A CSS technique used to apply different style rules to
126 |   different devices based on their characteristics, such as color scheme
127 |   preference (such as high contrast), display type, height, width, etc.
128 | - **Screen Reader:** A type of software that interprets and reads aloud the
129 |   information displayed on a screen, such as text, images, buttons, and menus.
130 |   It's primarily used by people with visual impairments or those who have
131 |   difficulties reading text on a screen. Examples include JAWS, NVDA, and
132 |   VoiceOver.
133 | 


--------------------------------------------------------------------------------
/website/tutorials/a11y/keyboard.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_position: 1
  3 | sidebar_label: Keyboard navigation
  4 | pagination_title: Keyboard navigation
  5 | title: Keyboard navigation
  6 | description: In this section we will add keyboard navigation to the chart.
  7 | keywords:
  8 |   - a11y
  9 |   - accessibility
 10 |   - screenreaders
 11 |   - keyboard
 12 |   - assistive
 13 | pagination_prev: a11y/intro
 14 | pagination_next: a11y/screenreader
 15 | ---
 16 | 
 17 | # Keyboard navigation
 18 | 
 19 | ## Purpose of keyboard navigation
 20 | 
 21 | One cornerstone of web accessibility is ensuring that sites and applications are
 22 | fully operable via keyboard alone. This navigation method benefits a wide range
 23 | of users, especially those who are unable to use a mouse or have visual
 24 | impairments.
 25 | 
 26 | Screen readers and other assistive technologies rely heavily on keyboard
 27 | interaction, and some users choose this method due to an acquired skill set or
 28 | personal preference. By including keyboard navigation in our charts, we make the
 29 | tool more accessible and user-friendly, living up to the principles of inclusive
 30 | design.
 31 | 
 32 | ## Implementing keyboard actions with Lightweight Charts™
 33 | 
 34 | The Lightweight Charts™ API provides numerous methods that enable handling chart
 35 | actions programmatically, making it possible to tie these actions to keyboard
 36 | events.
 37 | 
 38 | Here's a walk-through of how to add keyboard navigation to the chart.
 39 | 
 40 | ### Setting focus on the chart
 41 | 
 42 | Firstly, we must ensure the chart is programmatically focusable for keyboard
 43 | interaction. We can achieve this by placing a `tabindex` attribute to the
 44 | chart's container div:
 45 | 
 46 | ```html
 47 | <div id="chart" tabindex="0"></div>
 48 | ```
 49 | 
 50 | This can also be achieved via JavaScript:
 51 | 
 52 | ```js
 53 | const containerEl = chart.chartElement().parentElement;
 54 | containerEl.tabIndex = 0;
 55 | ```
 56 | 
 57 | ### Adding event listener for keyboard actions
 58 | 
 59 | Following that, we will tie specific chart interactions to keypress events using
 60 | JavaScript's `addEventListener` method. This will allow us to control the chart
 61 | using specific keystrokes:
 62 | 
 63 | ```js
 64 | const chartContainer = document.getElementById('chart');
 65 | chartContainer.addEventListener('keydown', event => {
 66 |     switch (event.key) {
 67 |     case 'ArrowLeft':
 68 |         // Action for ArrowLeft key
 69 |         break;
 70 |     case 'ArrowRight':
 71 |         // Action for ArrowRight key
 72 |         break;
 73 |         // ... more cases
 74 |     }
 75 | });
 76 | ```
 77 | 
 78 | The `addEventListener` function lets us listen to `keydown` events that occur
 79 | when the user presses a key.
 80 | 
 81 | ### Utilizing Lightweight Chart's API for actions
 82 | 
 83 | Next, for each case, we use Lightweight Chart's API for desired actions.
 84 | 
 85 | Let's assume we want the left arrow key to scroll the chart to the left, and the
 86 | right arrow key to scroll it to the right:
 87 | 
 88 | ```js
 89 | function shiftChart(diff) {
 90 |     const currentPos = chart.timeScale().scrollPosition();
 91 |     chart.timeScale().scrollToPosition(currentPos + diff, false);
 92 | }
 93 | 
 94 | chartContainer.addEventListener('keydown', event => {
 95 |     switch (event.key) {
 96 |     case 'ArrowLeft':
 97 |         shiftChart(-10);
 98 |         break;
 99 |     case 'ArrowRight':
100 |         shiftChart(10);
101 |         break;
102 |     }
103 | });
104 | ```
105 | 
106 | In the above JavaScript code, the `timeScale().scrollToPosition()` method from
107 | Lightweight Charts™ API is used inside the event listener to scroll the chart
108 | whenever the left or right arrow key is pressed.
109 | 
110 | Additionally, we can assign the up and down arrow keys to adjust the zoom level
111 | of the chart:
112 | 
113 | ```js
114 | function scaleChart(pct, zoomIn) {
115 |     const currentRange = chart.timeScale().getVisibleLogicalRange();
116 |     if (currentRange) {
117 |         const bars = currentRange.to - currentRange.from;
118 |         const direction = zoomIn ? -1 : 1;
119 |         const newRangeBars = bars * pct * direction + bars;
120 |         chart.timeScale().setVisibleLogicalRange({
121 |             to: currentRange.to,
122 |             from: currentRange.to - newRangeBars,
123 |         });
124 |     }
125 | }
126 | 
127 | chartContainer.addEventListener('keydown', event => {
128 |     switch (event.key) {
129 |     // ...
130 |     case 'ArrowUp':
131 |         scaleChart(1 / 8, true);
132 |         break;
133 |     case 'ArrowDown':
134 |         scaleChart(1 / 8, false);
135 |         break;
136 |     }
137 | });
138 | ```
139 | 
140 | We are scaling the chart by adjusting the `visibleLogicalRange` instead of
141 | changing the `barSpacing` option on the time scale. In this example, we are
142 | keeping the right data point fixed when zooming in or out by retaining the `to`
143 | value and only modifying the `from` value.
144 | 
145 | ---
146 | 
147 | This keyboard navigation inclusion makes the chart's underlying data more
148 | accessible to a wider audience, ensuring a diverse user base can fully interact
149 | with the chart's functions.
150 | 
151 | :::tip
152 | 
153 | Note that more keyboard actions can be added according to
154 | project-specific requirements, thereby further enhancing the navigation controls
155 | and accessibility.
156 | 
157 | :::
158 | 
159 | In the next section, we'll continue enhancing our accessible charts by
160 | integrating ARIA (Accessible Rich Internet Applications) roles and properties and generating descriptive content.
161 | 


--------------------------------------------------------------------------------
/website/tutorials/a11y/readability.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_position: 3
  3 | sidebar_label: Readability
  4 | pagination_title: Readability
  5 | title: Readability
  6 | description: Improving the readability of the chart for visually impaired users.
  7 | keywords:
  8 |   - a11y
  9 |   - accessibility
 10 |   - screenreaders
 11 |   - keyboard
 12 |   - assistive
 13 | pagination_prev: a11y/screenreader
 14 | pagination_next: a11y/conclusion
 15 | ---
 16 | 
 17 | ## High contrast and scalable font size
 18 | 
 19 | Ensuring accessibility in web development means accommodating various user
 20 | preferences and physical abilities. High contrast mode and scalable font size
 21 | are two such distinct features that have been included in our chart, catering to
 22 | diverse user needs.
 23 | 
 24 | ### High contrast mode
 25 | 
 26 | Certain users with specific visual impairments may struggle to distinguish
 27 | between colors or interpret text and image details in low contrast. For these
 28 | users, a high-contrast mode can be immensely helpful.
 29 | 
 30 | In our chart application, we leverage the built-in browser feature
 31 | `window.matchMedia()` to ascertain if the user has indicated a preference for
 32 | higher contrast in their system settings.
 33 | 
 34 | Here's how we determine if the user prefers a high-contrast mode:
 35 | 
 36 | ```js
 37 | // Check if user prefers high contrast mode
 38 | function checkHighContrast() {
 39 |     // Use window.matchMedia to check 'prefers-contrast' media feature
 40 |     const highContrast = window.matchMedia('(prefers-contrast: high)').matches;
 41 |     return highContrast; // Returns true if high contrast is enabled, false otherwise
 42 | }
 43 | 
 44 | // Subscribe to changes
 45 | const highContrastMediaQuery = window.matchMedia('(prefers-contrast: high)');
 46 | highContrastMediaQuery.addListener(() => {
 47 |     setHighContrast(highContrastMediaQuery.matches);
 48 | });
 49 | ```
 50 | 
 51 | A `setHighContrast` function could be implemented as follows:
 52 | 
 53 | ```js
 54 | const seriesBaseContrastSettings = {
 55 |     color: 'rgb(41, 98, 255)',
 56 |     lineWidth: 2,
 57 | };
 58 | const chartBaseContrastSettings = {
 59 |     layout: {
 60 |         textColor: '#191919',
 61 |     },
 62 |     grid: {
 63 |         vertLines: {
 64 |             color: '#D6DCDE',
 65 |         },
 66 |         horzLines: {
 67 |             color: '#D6DCDE',
 68 |         },
 69 |     },
 70 | };
 71 | const seriesHighContrastSettings = {
 72 |     color: 'rgb(0, 0, 0)',
 73 |     lineWidth: 4,
 74 | };
 75 | const chartHighContrastSettings = {
 76 |     layout: {
 77 |         textColor: '#000000',
 78 |     },
 79 |     grid: {
 80 |         vertLines: {
 81 |             color: '#777777',
 82 |         },
 83 |         horzLines: {
 84 |             color: '#777777',
 85 |         },
 86 |     },
 87 | };
 88 | 
 89 | function setHighContrast(enabled) {
 90 |     mainSeries.applyOptions(
 91 |         enabled ? seriesHighContrastSettings : seriesBaseContrastSettings
 92 |     );
 93 |     chart.applyOptions(
 94 |         enabled ? chartHighContrastSettings : chartBaseContrastSettings
 95 |     );
 96 | }
 97 | ```
 98 | 
 99 | Our `setHighContrast(highContrast)` function updates the chart's colors based on
100 | the user's preference. If the user prefers high contrast, a higher contrast
101 | color scheme is applied. If not, the colors switch back to the default, low-contrast scheme.
102 | 
103 | ### Scalable font size
104 | 
105 | Another key aspect of web accessibility is the option to scale font sizes.
106 | Users with visual impairments may benefit from larger text sizes, improving
107 | readability.
108 | 
109 | We provide an option for these users to adjust the text size through a checkbox,
110 | which changes text size in the chart:
111 | 
112 | ```html
113 | <input type="checkbox" id="large-font-checkbox" tabindex="0" />
114 | <label for="large-font-checkbox">Toggle Larger Font</label>
115 | ```
116 | 
117 | Then, we create an event listener in JavaScript for this checkbox input, which increases
118 | the text size:
119 | 
120 | ```js
121 | function setFontSize(large) {
122 |     chart.applyOptions({
123 |         layout: {
124 |             fontSize: large ? 16 : 12,
125 |         },
126 |     });
127 | }
128 | 
129 | document
130 |     .querySelector('#large-font-checkbox')
131 |     .addEventListener('change', event => {
132 |         setFontSize(event.target.checked);
133 |     });
134 | ```
135 | 
136 | In this example, when the 'Increase Font Size' input is checked, the font size
137 | in the chart increases to 16px.
138 | 
139 | Including these additional accessibility features adheres to the principles of
140 | creating an inclusive web, where design embraces all user types, abilities, and
141 | preferences. Note that you should conduct rigorous accessibility testing before deployment.
142 | 


--------------------------------------------------------------------------------
/website/tutorials/a11y/screenreader.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_position: 2
  3 | sidebar_label: Screen Readers
  4 | pagination_title: Screen Readers
  5 | title: Screen Readers
  6 | description: In this section we will add screen reader support to the chart.
  7 | keywords:
  8 |   - a11y
  9 |   - accessibility
 10 |   - screenreaders
 11 |   - keyboard
 12 |   - assistive
 13 | pagination_prev: a11y/keyboard
 14 | pagination_next: a11y/readability
 15 | ---
 16 | 
 17 | # Integrating ARIA roles and descriptive content for enhanced accessibility
 18 | 
 19 | Accessibility in web development extends beyond just accommodating keyboard-only
 20 | users. Many users with varying abilities make use of assistive technologies like
 21 | screen readers to effectively interact with web applications.
 22 | [ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)
 23 | (Accessible Rich Internet Applications) roles and states offer a powerful
 24 | toolkit to improve this interaction by conveying information about the behavior
 25 | and purpose of interface components.
 26 | 
 27 | In the context of our line chart, we'll be looking at how to implement ARIA
 28 | attributes to further enhance its accessibility in addition to generating
 29 | descriptive content for our graph.
 30 | 
 31 | :::info
 32 | 
 33 | In this tutorial we will only make use of
 34 | the `aria-live`, `aria-label`, and `aria-hidden` attributes. You can explore
 35 | a [more comprehensive list of attributes on this MDN page]
 36 | (https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes).
 37 | 
 38 | :::
 39 | 
 40 | ## Use of ARIA attributes in the chart
 41 | 
 42 | ### aria-live
 43 | 
 44 | To provide real-time updates about the chart to assistive technologies, we use
 45 | the `aria-live` attribute. It accepts a few potential values, although
 46 | `"polite"` and `"assertive"` are the most common.
 47 | 
 48 | With `aria-live="polite"`, updates are presented at the user's next convenient
 49 | opportunity, such as when they stop typing or when a task is completed. With
 50 | `aria-live="assertive"`, updates are presented immediately.
 51 | 
 52 | Our chart uses the `"assertive"` value because the description should be read
 53 | out based on a user action (keyboard action):
 54 | 
 55 | ```html
 56 | <div id="chart" aria-live="assertive" tabindex="0"></div>
 57 | ```
 58 | 
 59 | ### aria-label
 60 | 
 61 | The `aria-label` attribute is used to specify a string that labels the current
 62 | element. It's useful when there isn't any text content that describes this
 63 | element.
 64 | 
 65 | On our chart, it could read something like this:
 66 | 
 67 | ```html
 68 | <div
 69 |     id="chart"
 70 |     aria-live="polite"
 71 |     aria-label="interactive line chart"
 72 |     tabindex="0"
 73 | ></div>
 74 | ```
 75 | 
 76 | ### aria-hidden
 77 | 
 78 | The `aria-hidden` attribute is used to hide irrelevant or redundant
 79 | information from assistive technologies. Its value is either "true" or "false".
 80 | 
 81 | For example, if our chart contained a decorative element with no semantic
 82 | meaning, we could use `aria-hidden="true"` to hide it from screen readers:
 83 | 
 84 | ```html
 85 | <div id="decorative-element" aria-hidden="true"></div>
 86 | ```
 87 | 
 88 | ### Adding the ARIA attributes to an existing chart via JavaScript
 89 | 
 90 | ```html
 91 | <!-- Template for HTML elements added to the chart container for the A11y improvements -->
 92 | <template id="a11y-helpers">
 93 |     <div tabindex="-1" role="alert" aria-live="assertive"></div>
 94 | </template>
 95 | 
 96 | <script>
 97 |     function addAriaAttributesAndAlerter(chart) {
 98 |         const containerEl = chart.chartElement().parentElement;
 99 |         if (!containerEl) return;
100 |         // make focusable
101 |         containerEl.tabIndex = 0;
102 |         containerEl.style.position = 'relative';
103 |         containerEl.ariaLabel =
104 |             'Line plot of Accessibility stock price. Press the H key to display the available interaction keys.';
105 |         chart.chartElement().ariaHidden = 'true';
106 | 
107 |         const templateElement = document.getElementById('a11y-helpers');
108 |         const clone = templateElement.content.cloneNode(true);
109 |         containerEl.appendChild(clone);
110 |     }
111 | </script>
112 | ```
113 | 
114 | ## Generating a description of the chart
115 | 
116 | In addition to ARIA roles, providing a textual description for our charts helps
117 | all users, especially those relying on screen readers or other assistive
118 | technologies.
119 | 
120 | You may generate a description of a chart by applying domain-specific knowledge.
121 | It's beneficial to outline the general trend or patterns of the data, highlight
122 | any notable points or anomalies, and summarize the implications of the data.
123 | 
124 | You can add a descriptive section to the chart:
125 | 
126 | ```html
127 | <div id="chart-description" aria-live="assertive">
128 |     <!-- The content here should be dynamically generated based on the chart data -->
129 | </div>
130 | ```
131 | 
132 | You can use JavaScript to change the content inside this div whenever the chart
133 | data is updated:
134 | 
135 | ```js
136 | const descriptionElement = document.getElementById('chart-description');
137 | descriptionElement.textContent = generateDescription(mainSeries.data());
138 | ```
139 | 
140 | Here, `generateDescription(data)` would be a function that you write to
141 | translate the chart's data into human-readable insights. The function would vary
142 | greatly based on what the charts represent and how much detail you wish to
143 | provide.
144 | 
145 | The example describes the chart based on its first and last visible data
146 | points in addition to the highest and lowest points displayed. This is used to
147 | generate a description like this:
148 | 
149 | > The first price is $679.10 at Wed Sep 19 2018. The last price is $555.37 at
150 | > Wed May 15 2019. The actual change in price was -$123.73, corresponding to a
151 | > percentage change of -18.22%. The lowest price was $32.76 at Fri Dec 21 2018.
152 | > The highest price was $951.33 at Sun Mar 24 2019.
153 | 
154 | The following code could be used as a starting point for generating chart
155 | descriptions:
156 | 
157 | ```js
158 | function formatDate(time) {
159 |     return new Date(time * 1000).toDateString();
160 | }
161 | 
162 | function formatValue(value) {
163 |     return `${value < 0 ? '-' : ''}${Math.abs(value).toFixed(2)}`;
164 | }
165 | 
166 | function getStats(data) {
167 |     const stats = {
168 |         start: data[0],
169 |         close: data[data.length - 1],
170 |         low: data[0],
171 |         high: data[0],
172 |     };
173 | 
174 |     for (const point of data) {
175 |         if (point.value > stats.high.value) {
176 |             stats.high = point;
177 |         }
178 |         if (point.value < stats.low.value) {
179 |             stats.low = point;
180 |         }
181 |     }
182 | 
183 |     return stats;
184 | }
185 | 
186 | function getVisibleSeriesData(chart, series) {
187 |     const timeScale = chart.timeScale();
188 |     const visibleRange = timeScale.getVisibleLogicalRange();
189 |     const data = [];
190 |     for (let i = Math.round(visibleRange.from); i <= visibleRange.to; i++) {
191 |         const d = series.dataByIndex(i, 0);
192 |         if (d !== null) {
193 |             data.push(d);
194 |         }
195 |     }
196 |     return data;
197 | }
198 | 
199 | function describeFinanceChart(data) {
200 |     if (!data || data.length === 0) {
201 |         return 'The data set is empty.';
202 |     }
203 | 
204 |     const stats = getStats(data);
205 | 
206 |     const firstPrice = `The first price is ${formatValue(
207 |         stats.start.value
208 |     )} at ${formatDate(stats.start.time)}.`;
209 |     const lastPrice = `The last price is ${formatValue(
210 |         stats.close.value
211 |     )} at ${formatDate(stats.close.time)}.`;
212 | 
213 |     const actualChange = stats.close.value - stats.start.value;
214 |     const percentChange = (actualChange / stats.start.value) * 100;
215 | 
216 |     const changeDescription = `The actual change in price was ${formatValue(
217 |         actualChange
218 |     )}, corresponding to a percentage change of ${percentChange.toFixed(2)}%.`;
219 | 
220 |     let lowHigh = '';
221 |     if (
222 |         stats.low.time !== stats.start.time &&
223 |         stats.low.time !== stats.close.time
224 |     ) {
225 |         lowHigh += `The lowest price was ${formatValue(
226 |             stats.low.value
227 |         )} at ${formatDate(stats.low.time)}.`;
228 |     }
229 |     if (
230 |         stats.high.time !== stats.start.time &&
231 |         stats.high.time !== stats.close.time
232 |     ) {
233 |         lowHigh += ` The highest price was ${formatValue(
234 |             stats.high.value
235 |         )} at ${formatDate(stats.high.time)}.`;
236 |     }
237 | 
238 |     return `${firstPrice} ${lastPrice} ${changeDescription} ${lowHigh}`.trim();
239 | }
240 | ```
241 | 
242 | ## Semantic HTML
243 | 
244 | Using
245 | [Semantic HTML](https://developer.mozilla.org/en-US/docs/Glossary/Semantics#semantics_in_html)
246 | elements offers several benefits. Firstly, they enhance the accessibility of web
247 | content as they provide specific meaning to the browser and assistive technology
248 | like screen readers, helping them understand the content's structure and
249 | purpose. This is crucial for users with disabilities.
250 | 
251 | It is suggested that the container provided to the `createChart` method should
252 | use a semantic element such as `<figure>` instead of a generic element like
253 | `div`.
254 | 
255 | ```html
256 | <figure id="chart"></figure>
257 | ```
258 | 
259 | In the next part, we'll discuss contrast control and font scaling.
260 | 


--------------------------------------------------------------------------------
/website/tutorials/analysis-indicators.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_position: 3
  3 | title: Analysis indicators
  4 | pagination_title: Conclusion
  5 | sidebar_label: Analysis indicators
  6 | id: analysis-indicators
  7 | # description: Conclusion to the customization tutorial
  8 | # keywords:
  9 | #   - customization
 10 | #   - appearance
 11 | #   - styling
 12 | # pagination_prev: customization/finishing-touches
 13 | # pagination_next: null
 14 | ---
 15 | 
 16 | ## Overview
 17 | 
 18 | This guide provides an overview of the custom indicator examples.
 19 | These examples serve as a starting point for creating your own indicators.
 20 | You can use them directly in your projects.
 21 | 
 22 | ### Available indicators
 23 | 
 24 | Below is a list of indicators where each link points to their source code on GitHub.
 25 | - [Average Price](https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/average-price)
 26 | - [Correlation](https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/correlation)
 27 | - [Median Price](https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/median-price)
 28 | - [Momentum](https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/momentum)
 29 | - [Simple Moving Average](https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/moving-average)
 30 | - [Percent Change](https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/percent-change)
 31 | - [Product](https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/product)
 32 | - [Ratio](https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/ratio)
 33 | - [Spread](https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/spread)
 34 | - [Sum](https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/sum)
 35 | - [Weighted Close](https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/weighted-close)
 36 | 
 37 | ### Live demos
 38 | 
 39 | You can see all the indicators in action on the [live demos page](https://tradingview.github.io/lightweight-charts/indicator-examples/).
 40 | Each indicator has two demos:
 41 | 
 42 | * **Helper**: shows the recommended method with automatic updates.
 43 | * **Direct calculation**: shows the method with a pure function.
 44 | 
 45 | ## How to use the examples
 46 | 
 47 | The examples are self-contained and not available on a package manager like NPM.
 48 | Therefore, you have two options for integrating them into your project.
 49 | 
 50 | ### Option 1: copy the source code
 51 | 
 52 | The simplest way to use an indicator is to copy its source code directly into your project.
 53 | For example, if you want to use the Moving Average indicator, copy the following files into your project's source tree.
 54 | 
 55 | - `indicator-examples/src/indicators/moving-average/moving-average.ts`
 56 | - `indicator-examples/src/indicators/moving-average/moving-average-calculation.ts`
 57 | - `indicator-examples/src/helpers/timestamp-data.ts` (dependency for the calculation)
 58 | 
 59 | You can then import the `applyMovingAverageIndicator` helper or the `calculateMovingAverageIndicatorValues` function directly into your code.
 60 | 
 61 | ### Option 2: compile the examples
 62 | 
 63 | If you prefer to use a compiled JavaScript module, you can build the examples yourself.
 64 | 
 65 | 1. Clone the `lightweight-charts` repository.
 66 | 2. Build the main library first:
 67 |     ```shell
 68 |     npm install
 69 |     npm run build:prod
 70 |     ```
 71 | 3. Navigate to the examples directory, install dependencies, and run the compile script:
 72 |     ```shell
 73 |     cd indicator-examples
 74 |     npm install
 75 |     npm run compile
 76 |     ```
 77 | 4. The compiled output will be available in the `indicator-examples/compiled` folder. You can then copy this folder into your project and import the modules.
 78 | 
 79 | ## How to add indicator
 80 | 
 81 | There are two distinct approaches to applying these indicators to your chart.
 82 | 
 83 | - Using a [helper function](#helper-function-recommended) that creates the indicator series and automatically keeps it in sync with the source series' data.
 84 | - Using a [pure function](#direct-calculation) to directly calculate the indicator data from a static dataset.
 85 | 
 86 | :::tip
 87 | 
 88 | We recommend using the [Helper function](#helper-function-recommended) for its simplicity and automatic data synchronization.
 89 | 
 90 | :::
 91 | 
 92 | ### Helper function (recommended)
 93 | 
 94 | Each indicator includes an `apply…` function (e.g., `applyMovingAverageIndicator`). This is the preferred and easier method.
 95 | 
 96 | This function takes the source series API object itself (not the data) and the options.
 97 | It handles everything for you:
 98 | 
 99 | - Creates the new indicator series.
100 | - Performs the initial calculation.
101 | - Automatically listens for data changes on the source series and recalculates the indicator whenever the source data is updated.
102 | 
103 | #### Example
104 | 
105 | The example below shows how to add an Exponential Moving Average (EMA) with the helper function.
106 | 
107 | ```ts
108 | import { createChart, CandlestickSeries, LineStyle } from 'lightweight-charts';
109 | import { applyMovingAverageIndicator } from './indicators/moving-average/moving-average';
110 | import { symbolData } from './my-data-source';
111 | 
112 | const chart = createChart(document.body);
113 | const mainSeries = chart.addSeries(CandlestickSeries);
114 | mainSeries.setData(symbolData.slice(0, 100)); // Set initial data
115 | 
116 | // 1. Apply the indicator directly to the source series
117 | const emaSeries = applyMovingAverageIndicator(mainSeries, {
118 | 	length: 10,
119 | 	source: 'close',
120 | 	smoothingLine: 'EMA',
121 | });
122 | 
123 | // 2. (Optional) Customize the new indicator series
124 | emaSeries.applyOptions({
125 | 	color: 'orange',
126 | 	lineWidth: 2,
127 | 	lineStyle: LineStyle.Dotted,
128 | });
129 | 
130 | // Now, when we update the mainSeries, the emaSeries will update automatically
131 | setInterval(() => {
132 |     const nextBar = getNextRealTimeBar();
133 |     mainSeries.update(nextBar); // The EMA series will update itself
134 | }, 1000);
135 | ```
136 | 
137 | The `apply…` helper attaches a lightweight `ISeriesPrimitive` to the source series.
138 | This primitive subscribes to the series' data changes.
139 | When a change is detected, it refetches the data, runs the calculation, and updates the indicator series automatically.
140 | 
141 | This approach is more robust, requires less code, and is the recommended way to use these examples.
142 | 
143 | ### Direct calculation
144 | 
145 | Each indicator includes a `calculate…` function (e.g., `calculateMovingAverageIndicatorValues`).
146 | This is a pure function that takes your series data and a set of options as input and returns an array of calculated data points for the indicator.
147 | 
148 | This method is useful if you have a static dataset or want full control over when the indicator is recalculated.
149 | 
150 | #### Example
151 | 
152 | The example below shows how to add a Simple Moving Average (SMA).
153 | 
154 | ```ts
155 | import { createChart, LineSeries, CandlestickSeries } from 'lightweight-charts';
156 | import { calculateMovingAverageIndicatorValues } from './indicators/moving-average/moving-average-calculation';
157 | import { symbolData } from './my-data-source';
158 | 
159 | const chart = createChart(document.body);
160 | const mainSeries = chart.addSeries(CandlestickSeries);
161 | mainSeries.setData(symbolData);
162 | 
163 | // 1. Calculate the indicator data from the source data
164 | const smaData = calculateMovingAverageIndicatorValues(symbolData, {
165 | 	length: 20,
166 | 	source: 'close',
167 | });
168 | 
169 | // 2. Create a new series for the indicator
170 | const smaSeries = chart.addSeries(LineSeries, {
171 | 	color: 'blue',
172 | 	lineWidth: 2,
173 | });
174 | 
175 | // 3. Set the calculated data on the new series
176 | smaSeries.setData(smaData);
177 | ```
178 | 
179 | :::warning
180 | 
181 | This approach is **not reactive**. If you update the `mainSeries` with new data (e.g., from a real-time feed), the `smaSeries` will **not** update automatically.
182 | You are responsible for manually recalculating the indicator and calling `smaSeries.setData()` again.
183 | 
184 | :::
185 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/.eslintrc.js:
--------------------------------------------------------------------------------
1 | module.exports = {
2 | 	ignorePatterns: ['_apply-options-tabs-partial.mdx'],
3 | };
4 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/_apply-options-tabs-partial.mdx:
--------------------------------------------------------------------------------
 1 | <!--
 2 |     ESLint throws an error when trying to use TabItem.
 3 |     Created this partial file so it can be ignored by ESLint (using ignorePattern within .eslintrc.js)
 4 | -->
 5 | 
 6 | import Tabs from "@theme/Tabs";
 7 | import TabItem from "@theme/TabItem";
 8 | 
 9 | <Tabs>
10 | <TabItem value="creation" label="During Creation">
11 | 
12 | ```js
13 | const lineSeries = chart.addSeries(LineSeries, {
14 |     color: '#2962FF',
15 | });
16 | ```
17 | 
18 | </TabItem>
19 | <TabItem value="applyOptions" label="Using applyOptions">
20 | 
21 | ```js
22 | const lineSeries = chart.addSeries(LineSeries, {
23 | });
24 | 
25 | lineSeries.applyOptions({
26 |     color: '#2962FF',
27 | });
28 | ```
29 | 
30 | </TabItem>
31 | </Tabs>
32 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/_category_.yml:
--------------------------------------------------------------------------------
1 | label: "Customization"
2 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/_iterative-guide-warning-partial.mdx:
--------------------------------------------------------------------------------
1 | :::info
2 | 
3 | **This page is part of an iterative guide (where we build onto code from the previous steps).**
4 | 
5 | It is recommend that you follow the guide from the [start](intro). However, if you are only interested in the content on this page then take a look at the [full code](#complete-code) at the bottom of page for context of how this code fits into a working example.
6 | 
7 | :::
8 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/assets/start.html:
--------------------------------------------------------------------------------
   1 | <!DOCTYPE html>
   2 | <!-- Please visit https://tradingview.github.io/lightweight-charts/tutorials/customization for more information on this tutorial. -->
   3 | <html>
   4 |   <head>
   5 |     <meta charset="UTF-8" />
   6 |     <meta
   7 |       name="viewport"
   8 |       content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0"
   9 |     />
  10 |     <title>Lightweight Charts™ Customization Tutorial</title>
  11 |     <style>
  12 |       body {
  13 |         padding: 0;
  14 |         margin: 0;
  15 |       }
  16 |     </style>
  17 |   </head>
  18 | 
  19 |   <body style="padding: 0; margin: 0">
  20 |     <div
  21 |       id="container"
  22 |       style="position: absolute; width: 100%; height: 100%"
  23 |     ></div>
  24 |     <script type="text/javascript">
  25 |       // Function to generate a sample set of Candlestick datapoints
  26 |       function generateCandlestickData() {
  27 |         return [
  28 |           {
  29 |             time: "2018-10-19",
  30 |             open: 180.34,
  31 |             high: 180.99,
  32 |             low: 178.57,
  33 |             close: 179.85,
  34 |           },
  35 |           {
  36 |             time: "2018-10-22",
  37 |             open: 180.82,
  38 |             high: 181.4,
  39 |             low: 177.56,
  40 |             close: 178.75,
  41 |           },
  42 |           {
  43 |             time: "2018-10-23",
  44 |             open: 175.77,
  45 |             high: 179.49,
  46 |             low: 175.44,
  47 |             close: 178.53,
  48 |           },
  49 |           {
  50 |             time: "2018-10-24",
  51 |             open: 178.58,
  52 |             high: 182.37,
  53 |             low: 176.31,
  54 |             close: 176.97,
  55 |           },
  56 |           {
  57 |             time: "2018-10-25",
  58 |             open: 177.52,
  59 |             high: 180.5,
  60 |             low: 176.83,
  61 |             close: 179.07,
  62 |           },
  63 |           {
  64 |             time: "2018-10-26",
  65 |             open: 176.88,
  66 |             high: 177.34,
  67 |             low: 170.91,
  68 |             close: 172.23,
  69 |           },
  70 |           {
  71 |             time: "2018-10-29",
  72 |             open: 173.74,
  73 |             high: 175.99,
  74 |             low: 170.95,
  75 |             close: 173.2,
  76 |           },
  77 |           {
  78 |             time: "2018-10-30",
  79 |             open: 173.16,
  80 |             high: 176.43,
  81 |             low: 172.64,
  82 |             close: 176.24,
  83 |           },
  84 |           {
  85 |             time: "2018-10-31",
  86 |             open: 177.98,
  87 |             high: 178.85,
  88 |             low: 175.59,
  89 |             close: 175.88,
  90 |           },
  91 |           {
  92 |             time: "2018-11-01",
  93 |             open: 176.84,
  94 |             high: 180.86,
  95 |             low: 175.9,
  96 |             close: 180.46,
  97 |           },
  98 |           {
  99 |             time: "2018-11-02",
 100 |             open: 182.47,
 101 |             high: 183.01,
 102 |             low: 177.39,
 103 |             close: 179.93,
 104 |           },
 105 |           {
 106 |             time: "2018-11-05",
 107 |             open: 181.02,
 108 |             high: 182.41,
 109 |             low: 179.3,
 110 |             close: 182.19,
 111 |           },
 112 |           {
 113 |             time: "2018-11-06",
 114 |             open: 181.93,
 115 |             high: 182.65,
 116 |             low: 180.05,
 117 |             close: 182.01,
 118 |           },
 119 |           {
 120 |             time: "2018-11-07",
 121 |             open: 183.79,
 122 |             high: 187.68,
 123 |             low: 182.06,
 124 |             close: 187.23,
 125 |           },
 126 |           {
 127 |             time: "2018-11-08",
 128 |             open: 187.13,
 129 |             high: 188.69,
 130 |             low: 185.72,
 131 |             close: 188.0,
 132 |           },
 133 |           {
 134 |             time: "2018-11-09",
 135 |             open: 188.32,
 136 |             high: 188.48,
 137 |             low: 184.96,
 138 |             close: 185.99,
 139 |           },
 140 |           {
 141 |             time: "2018-11-12",
 142 |             open: 185.23,
 143 |             high: 186.95,
 144 |             low: 179.02,
 145 |             close: 179.43,
 146 |           },
 147 |           {
 148 |             time: "2018-11-13",
 149 |             open: 177.3,
 150 |             high: 181.62,
 151 |             low: 172.85,
 152 |             close: 179.0,
 153 |           },
 154 |           {
 155 |             time: "2018-11-14",
 156 |             open: 182.61,
 157 |             high: 182.9,
 158 |             low: 179.15,
 159 |             close: 179.9,
 160 |           },
 161 |           {
 162 |             time: "2018-11-15",
 163 |             open: 179.01,
 164 |             high: 179.67,
 165 |             low: 173.61,
 166 |             close: 177.36,
 167 |           },
 168 |           {
 169 |             time: "2018-11-16",
 170 |             open: 173.99,
 171 |             high: 177.6,
 172 |             low: 173.51,
 173 |             close: 177.02,
 174 |           },
 175 |           {
 176 |             time: "2018-11-19",
 177 |             open: 176.71,
 178 |             high: 178.88,
 179 |             low: 172.3,
 180 |             close: 173.59,
 181 |           },
 182 |           {
 183 |             time: "2018-11-20",
 184 |             open: 169.25,
 185 |             high: 172.0,
 186 |             low: 167.0,
 187 |             close: 169.05,
 188 |           },
 189 |           {
 190 |             time: "2018-11-21",
 191 |             open: 170.0,
 192 |             high: 170.93,
 193 |             low: 169.15,
 194 |             close: 169.3,
 195 |           },
 196 |           {
 197 |             time: "2018-11-23",
 198 |             open: 169.39,
 199 |             high: 170.33,
 200 |             low: 168.47,
 201 |             close: 168.85,
 202 |           },
 203 |           {
 204 |             time: "2018-11-26",
 205 |             open: 170.2,
 206 |             high: 172.39,
 207 |             low: 168.87,
 208 |             close: 169.82,
 209 |           },
 210 |           {
 211 |             time: "2018-11-27",
 212 |             open: 169.11,
 213 |             high: 173.38,
 214 |             low: 168.82,
 215 |             close: 173.22,
 216 |           },
 217 |           {
 218 |             time: "2018-11-28",
 219 |             open: 172.91,
 220 |             high: 177.65,
 221 |             low: 170.62,
 222 |             close: 177.43,
 223 |           },
 224 |           {
 225 |             time: "2018-11-29",
 226 |             open: 176.8,
 227 |             high: 177.27,
 228 |             low: 174.92,
 229 |             close: 175.66,
 230 |           },
 231 |           {
 232 |             time: "2018-11-30",
 233 |             open: 175.75,
 234 |             high: 180.37,
 235 |             low: 175.11,
 236 |             close: 180.32,
 237 |           },
 238 |           {
 239 |             time: "2018-12-03",
 240 |             open: 183.29,
 241 |             high: 183.5,
 242 |             low: 179.35,
 243 |             close: 181.74,
 244 |           },
 245 |           {
 246 |             time: "2018-12-04",
 247 |             open: 181.06,
 248 |             high: 182.23,
 249 |             low: 174.55,
 250 |             close: 175.3,
 251 |           },
 252 |           {
 253 |             time: "2018-12-06",
 254 |             open: 173.5,
 255 |             high: 176.04,
 256 |             low: 170.46,
 257 |             close: 175.96,
 258 |           },
 259 |           {
 260 |             time: "2018-12-07",
 261 |             open: 175.35,
 262 |             high: 178.36,
 263 |             low: 172.24,
 264 |             close: 172.79,
 265 |           },
 266 |           {
 267 |             time: "2018-12-10",
 268 |             open: 173.39,
 269 |             high: 173.99,
 270 |             low: 167.73,
 271 |             close: 171.69,
 272 |           },
 273 |           {
 274 |             time: "2018-12-11",
 275 |             open: 174.3,
 276 |             high: 175.6,
 277 |             low: 171.24,
 278 |             close: 172.21,
 279 |           },
 280 |           {
 281 |             time: "2018-12-12",
 282 |             open: 173.75,
 283 |             high: 176.87,
 284 |             low: 172.81,
 285 |             close: 174.21,
 286 |           },
 287 |           {
 288 |             time: "2018-12-13",
 289 |             open: 174.31,
 290 |             high: 174.91,
 291 |             low: 172.07,
 292 |             close: 173.87,
 293 |           },
 294 |           {
 295 |             time: "2018-12-14",
 296 |             open: 172.98,
 297 |             high: 175.14,
 298 |             low: 171.95,
 299 |             close: 172.29,
 300 |           },
 301 |           {
 302 |             time: "2018-12-17",
 303 |             open: 171.51,
 304 |             high: 171.99,
 305 |             low: 166.93,
 306 |             close: 167.97,
 307 |           },
 308 |           {
 309 |             time: "2018-12-18",
 310 |             open: 168.9,
 311 |             high: 171.95,
 312 |             low: 168.5,
 313 |             close: 170.04,
 314 |           },
 315 |           {
 316 |             time: "2018-12-19",
 317 |             open: 170.92,
 318 |             high: 174.95,
 319 |             low: 166.77,
 320 |             close: 167.56,
 321 |           },
 322 |           {
 323 |             time: "2018-12-20",
 324 |             open: 166.28,
 325 |             high: 167.31,
 326 |             low: 162.23,
 327 |             close: 164.16,
 328 |           },
 329 |           {
 330 |             time: "2018-12-21",
 331 |             open: 162.81,
 332 |             high: 167.96,
 333 |             low: 160.17,
 334 |             close: 160.48,
 335 |           },
 336 |           {
 337 |             time: "2018-12-24",
 338 |             open: 160.16,
 339 |             high: 161.4,
 340 |             low: 158.09,
 341 |             close: 158.14,
 342 |           },
 343 |           {
 344 |             time: "2018-12-26",
 345 |             open: 159.46,
 346 |             high: 168.28,
 347 |             low: 159.44,
 348 |             close: 168.28,
 349 |           },
 350 |           {
 351 |             time: "2018-12-27",
 352 |             open: 166.44,
 353 |             high: 170.46,
 354 |             low: 163.36,
 355 |             close: 170.32,
 356 |           },
 357 |           {
 358 |             time: "2018-12-28",
 359 |             open: 171.22,
 360 |             high: 173.12,
 361 |             low: 168.6,
 362 |             close: 170.22,
 363 |           },
 364 |           {
 365 |             time: "2018-12-31",
 366 |             open: 171.47,
 367 |             high: 173.24,
 368 |             low: 170.65,
 369 |             close: 171.82,
 370 |           },
 371 |           {
 372 |             time: "2019-01-02",
 373 |             open: 169.71,
 374 |             high: 173.18,
 375 |             low: 169.05,
 376 |             close: 172.41,
 377 |           },
 378 |           {
 379 |             time: "2019-01-03",
 380 |             open: 171.84,
 381 |             high: 171.84,
 382 |             low: 168.21,
 383 |             close: 168.61,
 384 |           },
 385 |           {
 386 |             time: "2019-01-04",
 387 |             open: 170.18,
 388 |             high: 174.74,
 389 |             low: 169.52,
 390 |             close: 173.62,
 391 |           },
 392 |           {
 393 |             time: "2019-01-07",
 394 |             open: 173.83,
 395 |             high: 178.18,
 396 |             low: 173.83,
 397 |             close: 177.04,
 398 |           },
 399 |           {
 400 |             time: "2019-01-08",
 401 |             open: 178.57,
 402 |             high: 179.59,
 403 |             low: 175.61,
 404 |             close: 177.89,
 405 |           },
 406 |           {
 407 |             time: "2019-01-09",
 408 |             open: 177.87,
 409 |             high: 181.27,
 410 |             low: 177.1,
 411 |             close: 179.73,
 412 |           },
 413 |           {
 414 |             time: "2019-01-10",
 415 |             open: 178.03,
 416 |             high: 179.24,
 417 |             low: 176.34,
 418 |             close: 179.06,
 419 |           },
 420 |           {
 421 |             time: "2019-01-11",
 422 |             open: 177.93,
 423 |             high: 180.26,
 424 |             low: 177.12,
 425 |             close: 179.41,
 426 |           },
 427 |           {
 428 |             time: "2019-01-14",
 429 |             open: 177.59,
 430 |             high: 179.23,
 431 |             low: 176.9,
 432 |             close: 178.81,
 433 |           },
 434 |           {
 435 |             time: "2019-01-15",
 436 |             open: 176.08,
 437 |             high: 177.82,
 438 |             low: 175.2,
 439 |             close: 176.47,
 440 |           },
 441 |           {
 442 |             time: "2019-01-16",
 443 |             open: 177.09,
 444 |             high: 177.93,
 445 |             low: 175.86,
 446 |             close: 177.04,
 447 |           },
 448 |           {
 449 |             time: "2019-01-17",
 450 |             open: 174.01,
 451 |             high: 175.46,
 452 |             low: 172.0,
 453 |             close: 174.87,
 454 |           },
 455 |           {
 456 |             time: "2019-01-18",
 457 |             open: 176.98,
 458 |             high: 180.04,
 459 |             low: 176.18,
 460 |             close: 179.58,
 461 |           },
 462 |           {
 463 |             time: "2019-01-22",
 464 |             open: 177.49,
 465 |             high: 178.6,
 466 |             low: 175.36,
 467 |             close: 177.11,
 468 |           },
 469 |           {
 470 |             time: "2019-01-23",
 471 |             open: 176.59,
 472 |             high: 178.06,
 473 |             low: 174.53,
 474 |             close: 176.89,
 475 |           },
 476 |           {
 477 |             time: "2019-01-24",
 478 |             open: 177.0,
 479 |             high: 177.53,
 480 |             low: 175.3,
 481 |             close: 177.29,
 482 |           },
 483 |           {
 484 |             time: "2019-01-25",
 485 |             open: 179.78,
 486 |             high: 180.87,
 487 |             low: 178.61,
 488 |             close: 180.4,
 489 |           },
 490 |           {
 491 |             time: "2019-01-28",
 492 |             open: 178.97,
 493 |             high: 179.99,
 494 |             low: 177.41,
 495 |             close: 179.83,
 496 |           },
 497 |           {
 498 |             time: "2019-01-29",
 499 |             open: 178.96,
 500 |             high: 180.15,
 501 |             low: 178.09,
 502 |             close: 179.69,
 503 |           },
 504 |           {
 505 |             time: "2019-01-30",
 506 |             open: 180.47,
 507 |             high: 184.2,
 508 |             low: 179.78,
 509 |             close: 182.18,
 510 |           },
 511 |           {
 512 |             time: "2019-01-31",
 513 |             open: 181.5,
 514 |             high: 184.67,
 515 |             low: 181.06,
 516 |             close: 183.53,
 517 |           },
 518 |           {
 519 |             time: "2019-02-01",
 520 |             open: 184.03,
 521 |             high: 185.15,
 522 |             low: 182.83,
 523 |             close: 184.37,
 524 |           },
 525 |           {
 526 |             time: "2019-02-04",
 527 |             open: 184.3,
 528 |             high: 186.43,
 529 |             low: 183.84,
 530 |             close: 186.43,
 531 |           },
 532 |           {
 533 |             time: "2019-02-05",
 534 |             open: 186.89,
 535 |             high: 186.99,
 536 |             low: 184.69,
 537 |             close: 186.39,
 538 |           },
 539 |           {
 540 |             time: "2019-02-06",
 541 |             open: 186.69,
 542 |             high: 186.69,
 543 |             low: 184.06,
 544 |             close: 184.72,
 545 |           },
 546 |           {
 547 |             time: "2019-02-07",
 548 |             open: 183.74,
 549 |             high: 184.92,
 550 |             low: 182.45,
 551 |             close: 184.07,
 552 |           },
 553 |           {
 554 |             time: "2019-02-08",
 555 |             open: 183.05,
 556 |             high: 184.58,
 557 |             low: 182.72,
 558 |             close: 184.54,
 559 |           },
 560 |           {
 561 |             time: "2019-02-11",
 562 |             open: 185.0,
 563 |             high: 185.42,
 564 |             low: 182.75,
 565 |             close: 182.92,
 566 |           },
 567 |           {
 568 |             time: "2019-02-12",
 569 |             open: 183.84,
 570 |             high: 186.4,
 571 |             low: 183.52,
 572 |             close: 185.52,
 573 |           },
 574 |           {
 575 |             time: "2019-02-13",
 576 |             open: 186.3,
 577 |             high: 188.68,
 578 |             low: 185.92,
 579 |             close: 188.41,
 580 |           },
 581 |           {
 582 |             time: "2019-02-14",
 583 |             open: 187.5,
 584 |             high: 188.93,
 585 |             low: 186.0,
 586 |             close: 187.71,
 587 |           },
 588 |           {
 589 |             time: "2019-02-15",
 590 |             open: 189.87,
 591 |             high: 192.62,
 592 |             low: 189.05,
 593 |             close: 192.39,
 594 |           },
 595 |           {
 596 |             time: "2019-02-19",
 597 |             open: 191.71,
 598 |             high: 193.19,
 599 |             low: 191.28,
 600 |             close: 192.33,
 601 |           },
 602 |           {
 603 |             time: "2019-02-20",
 604 |             open: 192.39,
 605 |             high: 192.4,
 606 |             low: 191.11,
 607 |             close: 191.85,
 608 |           },
 609 |           {
 610 |             time: "2019-02-21",
 611 |             open: 191.85,
 612 |             high: 192.37,
 613 |             low: 190.61,
 614 |             close: 191.82,
 615 |           },
 616 |           {
 617 |             time: "2019-02-22",
 618 |             open: 191.69,
 619 |             high: 192.54,
 620 |             low: 191.62,
 621 |             close: 192.39,
 622 |           },
 623 |           {
 624 |             time: "2019-02-25",
 625 |             open: 192.75,
 626 |             high: 193.42,
 627 |             low: 189.96,
 628 |             close: 189.98,
 629 |           },
 630 |           {
 631 |             time: "2019-02-26",
 632 |             open: 185.59,
 633 |             high: 188.47,
 634 |             low: 182.8,
 635 |             close: 188.3,
 636 |           },
 637 |           {
 638 |             time: "2019-02-27",
 639 |             open: 187.9,
 640 |             high: 188.5,
 641 |             low: 183.21,
 642 |             close: 183.67,
 643 |           },
 644 |           {
 645 |             time: "2019-02-28",
 646 |             open: 183.6,
 647 |             high: 185.19,
 648 |             low: 183.11,
 649 |             close: 185.14,
 650 |           },
 651 |           {
 652 |             time: "2019-03-01",
 653 |             open: 185.82,
 654 |             high: 186.56,
 655 |             low: 182.86,
 656 |             close: 185.17,
 657 |           },
 658 |           {
 659 |             time: "2019-03-04",
 660 |             open: 186.2,
 661 |             high: 186.24,
 662 |             low: 182.1,
 663 |             close: 183.81,
 664 |           },
 665 |           {
 666 |             time: "2019-03-05",
 667 |             open: 184.24,
 668 |             high: 185.12,
 669 |             low: 183.25,
 670 |             close: 184.0,
 671 |           },
 672 |           {
 673 |             time: "2019-03-06",
 674 |             open: 184.53,
 675 |             high: 184.97,
 676 |             low: 183.84,
 677 |             close: 184.45,
 678 |           },
 679 |           {
 680 |             time: "2019-03-07",
 681 |             open: 184.39,
 682 |             high: 184.62,
 683 |             low: 181.58,
 684 |             close: 182.51,
 685 |           },
 686 |           {
 687 |             time: "2019-03-08",
 688 |             open: 181.49,
 689 |             high: 181.91,
 690 |             low: 179.52,
 691 |             close: 181.23,
 692 |           },
 693 |           {
 694 |             time: "2019-03-11",
 695 |             open: 182.0,
 696 |             high: 183.2,
 697 |             low: 181.2,
 698 |             close: 182.44,
 699 |           },
 700 |           {
 701 |             time: "2019-03-12",
 702 |             open: 183.43,
 703 |             high: 184.27,
 704 |             low: 182.33,
 705 |             close: 184.0,
 706 |           },
 707 |           {
 708 |             time: "2019-03-13",
 709 |             open: 183.24,
 710 |             high: 183.78,
 711 |             low: 181.08,
 712 |             close: 181.14,
 713 |           },
 714 |           {
 715 |             time: "2019-03-14",
 716 |             open: 181.28,
 717 |             high: 181.74,
 718 |             low: 180.5,
 719 |             close: 181.61,
 720 |           },
 721 |           {
 722 |             time: "2019-03-15",
 723 |             open: 182.3,
 724 |             high: 182.49,
 725 |             low: 179.57,
 726 |             close: 182.23,
 727 |           },
 728 |           {
 729 |             time: "2019-03-18",
 730 |             open: 182.53,
 731 |             high: 183.48,
 732 |             low: 182.33,
 733 |             close: 183.42,
 734 |           },
 735 |           {
 736 |             time: "2019-03-19",
 737 |             open: 184.19,
 738 |             high: 185.82,
 739 |             low: 183.48,
 740 |             close: 184.13,
 741 |           },
 742 |           {
 743 |             time: "2019-03-20",
 744 |             open: 184.3,
 745 |             high: 187.12,
 746 |             low: 183.43,
 747 |             close: 186.1,
 748 |           },
 749 |           {
 750 |             time: "2019-03-21",
 751 |             open: 185.5,
 752 |             high: 190.0,
 753 |             low: 185.5,
 754 |             close: 189.97,
 755 |           },
 756 |           {
 757 |             time: "2019-03-22",
 758 |             open: 189.31,
 759 |             high: 192.05,
 760 |             low: 188.67,
 761 |             close: 188.75,
 762 |           },
 763 |           {
 764 |             time: "2019-03-25",
 765 |             open: 188.75,
 766 |             high: 191.71,
 767 |             low: 188.51,
 768 |             close: 189.68,
 769 |           },
 770 |           {
 771 |             time: "2019-03-26",
 772 |             open: 190.69,
 773 |             high: 192.19,
 774 |             low: 188.74,
 775 |             close: 189.34,
 776 |           },
 777 |           {
 778 |             time: "2019-03-27",
 779 |             open: 189.65,
 780 |             high: 191.61,
 781 |             low: 188.39,
 782 |             close: 189.25,
 783 |           },
 784 |           {
 785 |             time: "2019-03-28",
 786 |             open: 189.91,
 787 |             high: 191.4,
 788 |             low: 189.16,
 789 |             close: 190.06,
 790 |           },
 791 |           {
 792 |             time: "2019-03-29",
 793 |             open: 190.85,
 794 |             high: 192.04,
 795 |             low: 190.14,
 796 |             close: 191.89,
 797 |           },
 798 |           {
 799 |             time: "2019-04-01",
 800 |             open: 192.99,
 801 |             high: 195.9,
 802 |             low: 192.85,
 803 |             close: 195.64,
 804 |           },
 805 |           {
 806 |             time: "2019-04-02",
 807 |             open: 195.5,
 808 |             high: 195.5,
 809 |             low: 194.01,
 810 |             close: 194.31,
 811 |           },
 812 |           {
 813 |             time: "2019-04-03",
 814 |             open: 194.98,
 815 |             high: 198.78,
 816 |             low: 194.11,
 817 |             close: 198.61,
 818 |           },
 819 |           {
 820 |             time: "2019-04-04",
 821 |             open: 199.0,
 822 |             high: 200.49,
 823 |             low: 198.02,
 824 |             close: 200.45,
 825 |           },
 826 |           {
 827 |             time: "2019-04-05",
 828 |             open: 200.86,
 829 |             high: 203.13,
 830 |             low: 200.61,
 831 |             close: 202.06,
 832 |           },
 833 |           {
 834 |             time: "2019-04-08",
 835 |             open: 201.37,
 836 |             high: 203.79,
 837 |             low: 201.24,
 838 |             close: 203.55,
 839 |           },
 840 |           {
 841 |             time: "2019-04-09",
 842 |             open: 202.26,
 843 |             high: 202.71,
 844 |             low: 200.46,
 845 |             close: 200.9,
 846 |           },
 847 |           {
 848 |             time: "2019-04-10",
 849 |             open: 201.26,
 850 |             high: 201.6,
 851 |             low: 198.02,
 852 |             close: 199.43,
 853 |           },
 854 |           {
 855 |             time: "2019-04-11",
 856 |             open: 199.9,
 857 |             high: 201.5,
 858 |             low: 199.03,
 859 |             close: 201.48,
 860 |           },
 861 |           {
 862 |             time: "2019-04-12",
 863 |             open: 202.13,
 864 |             high: 204.26,
 865 |             low: 202.13,
 866 |             close: 203.85,
 867 |           },
 868 |           {
 869 |             time: "2019-04-15",
 870 |             open: 204.16,
 871 |             high: 205.14,
 872 |             low: 203.4,
 873 |             close: 204.86,
 874 |           },
 875 |           {
 876 |             time: "2019-04-16",
 877 |             open: 205.25,
 878 |             high: 205.99,
 879 |             low: 204.29,
 880 |             close: 204.47,
 881 |           },
 882 |           {
 883 |             time: "2019-04-17",
 884 |             open: 205.34,
 885 |             high: 206.84,
 886 |             low: 205.32,
 887 |             close: 206.55,
 888 |           },
 889 |           {
 890 |             time: "2019-04-18",
 891 |             open: 206.02,
 892 |             high: 207.78,
 893 |             low: 205.1,
 894 |             close: 205.66,
 895 |           },
 896 |           {
 897 |             time: "2019-04-22",
 898 |             open: 204.11,
 899 |             high: 206.25,
 900 |             low: 204.0,
 901 |             close: 204.78,
 902 |           },
 903 |           {
 904 |             time: "2019-04-23",
 905 |             open: 205.14,
 906 |             high: 207.33,
 907 |             low: 203.43,
 908 |             close: 206.05,
 909 |           },
 910 |           {
 911 |             time: "2019-04-24",
 912 |             open: 206.16,
 913 |             high: 208.29,
 914 |             low: 205.54,
 915 |             close: 206.72,
 916 |           },
 917 |           {
 918 |             time: "2019-04-25",
 919 |             open: 206.01,
 920 |             high: 207.72,
 921 |             low: 205.06,
 922 |             close: 206.5,
 923 |           },
 924 |           {
 925 |             time: "2019-04-26",
 926 |             open: 205.88,
 927 |             high: 206.14,
 928 |             low: 203.34,
 929 |             close: 203.61,
 930 |           },
 931 |           {
 932 |             time: "2019-04-29",
 933 |             open: 203.31,
 934 |             high: 203.8,
 935 |             low: 200.34,
 936 |             close: 202.16,
 937 |           },
 938 |           {
 939 |             time: "2019-04-30",
 940 |             open: 201.55,
 941 |             high: 203.75,
 942 |             low: 200.79,
 943 |             close: 203.7,
 944 |           },
 945 |           {
 946 |             time: "2019-05-01",
 947 |             open: 203.2,
 948 |             high: 203.52,
 949 |             low: 198.66,
 950 |             close: 198.8,
 951 |           },
 952 |           {
 953 |             time: "2019-05-02",
 954 |             open: 199.3,
 955 |             high: 201.06,
 956 |             low: 198.8,
 957 |             close: 201.01,
 958 |           },
 959 |           {
 960 |             time: "2019-05-03",
 961 |             open: 202.0,
 962 |             high: 202.31,
 963 |             low: 200.32,
 964 |             close: 200.56,
 965 |           },
 966 |           {
 967 |             time: "2019-05-06",
 968 |             open: 198.74,
 969 |             high: 199.93,
 970 |             low: 198.31,
 971 |             close: 199.63,
 972 |           },
 973 |           {
 974 |             time: "2019-05-07",
 975 |             open: 196.75,
 976 |             high: 197.65,
 977 |             low: 192.96,
 978 |             close: 194.77,
 979 |           },
 980 |           {
 981 |             time: "2019-05-08",
 982 |             open: 194.49,
 983 |             high: 196.61,
 984 |             low: 193.68,
 985 |             close: 195.17,
 986 |           },
 987 |           {
 988 |             time: "2019-05-09",
 989 |             open: 193.31,
 990 |             high: 195.08,
 991 |             low: 191.59,
 992 |             close: 194.58,
 993 |           },
 994 |           {
 995 |             time: "2019-05-10",
 996 |             open: 193.21,
 997 |             high: 195.49,
 998 |             low: 190.01,
 999 |             close: 194.58,
1000 |           },
1001 |           {
1002 |             time: "2019-05-13",
1003 |             open: 191.0,
1004 |             high: 191.66,
1005 |             low: 189.14,
1006 |             close: 190.34,
1007 |           },
1008 |           {
1009 |             time: "2019-05-14",
1010 |             open: 190.5,
1011 |             high: 192.76,
1012 |             low: 190.01,
1013 |             close: 191.62,
1014 |           },
1015 |           {
1016 |             time: "2019-05-15",
1017 |             open: 190.81,
1018 |             high: 192.81,
1019 |             low: 190.27,
1020 |             close: 191.76,
1021 |           },
1022 |           {
1023 |             time: "2019-05-16",
1024 |             open: 192.47,
1025 |             high: 194.96,
1026 |             low: 192.2,
1027 |             close: 192.38,
1028 |           },
1029 |           {
1030 |             time: "2019-05-17",
1031 |             open: 190.86,
1032 |             high: 194.5,
1033 |             low: 190.75,
1034 |             close: 192.58,
1035 |           },
1036 |           {
1037 |             time: "2019-05-20",
1038 |             open: 191.13,
1039 |             high: 192.86,
1040 |             low: 190.61,
1041 |             close: 190.95,
1042 |           },
1043 |           {
1044 |             time: "2019-05-21",
1045 |             open: 187.13,
1046 |             high: 192.52,
1047 |             low: 186.34,
1048 |             close: 191.45,
1049 |           },
1050 |           {
1051 |             time: "2019-05-22",
1052 |             open: 190.49,
1053 |             high: 192.22,
1054 |             low: 188.05,
1055 |             close: 188.91,
1056 |           },
1057 |           {
1058 |             time: "2019-05-23",
1059 |             open: 188.45,
1060 |             high: 192.54,
1061 |             low: 186.27,
1062 |             close: 192.0,
1063 |           },
1064 |           {
1065 |             time: "2019-05-24",
1066 |             open: 192.54,
1067 |             high: 193.86,
1068 |             low: 190.41,
1069 |             close: 193.59,
1070 |           },
1071 |         ];
1072 |       }
1073 | 
1074 |       // Your code here:
1075 |     </script>
1076 |   </body>
1077 | </html>
1078 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/assets/step1.html:
--------------------------------------------------------------------------------
   1 | <!DOCTYPE html>
   2 | <html>
   3 |   <head>
   4 |     <meta charset="UTF-8" />
   5 |     <meta
   6 |       name="viewport"
   7 |       content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0"
   8 |     />
   9 |     <title>Lightweight Charts™ Customization Tutorial</title>
  10 |     <!-- Adding the standalone version of Lightweight charts -->
  11 |     <script
  12 |       type="text/javascript"
  13 |       src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"
  14 |     ></script>
  15 |     <style>
  16 |       body {
  17 |         padding: 0;
  18 |         margin: 0;
  19 |       }
  20 |     </style>
  21 |   </head>
  22 | 
  23 |   <body>
  24 |     <div
  25 |       id="container"
  26 |       style="position: absolute; width: 100%; height: 100%"
  27 |     ></div>
  28 |     <script type="text/javascript">
  29 |       // Function to generate a sample set of Candlestick datapoints
  30 |       function generateCandlestickData() {
  31 |         return [
  32 |           {
  33 |             time: "2018-10-19",
  34 |             open: 180.34,
  35 |             high: 180.99,
  36 |             low: 178.57,
  37 |             close: 179.85,
  38 |           },
  39 |           {
  40 |             time: "2018-10-22",
  41 |             open: 180.82,
  42 |             high: 181.4,
  43 |             low: 177.56,
  44 |             close: 178.75,
  45 |           },
  46 |           {
  47 |             time: "2018-10-23",
  48 |             open: 175.77,
  49 |             high: 179.49,
  50 |             low: 175.44,
  51 |             close: 178.53,
  52 |           },
  53 |           {
  54 |             time: "2018-10-24",
  55 |             open: 178.58,
  56 |             high: 182.37,
  57 |             low: 176.31,
  58 |             close: 176.97,
  59 |           },
  60 |           {
  61 |             time: "2018-10-25",
  62 |             open: 177.52,
  63 |             high: 180.5,
  64 |             low: 176.83,
  65 |             close: 179.07,
  66 |           },
  67 |           {
  68 |             time: "2018-10-26",
  69 |             open: 176.88,
  70 |             high: 177.34,
  71 |             low: 170.91,
  72 |             close: 172.23,
  73 |           },
  74 |           {
  75 |             time: "2018-10-29",
  76 |             open: 173.74,
  77 |             high: 175.99,
  78 |             low: 170.95,
  79 |             close: 173.2,
  80 |           },
  81 |           {
  82 |             time: "2018-10-30",
  83 |             open: 173.16,
  84 |             high: 176.43,
  85 |             low: 172.64,
  86 |             close: 176.24,
  87 |           },
  88 |           {
  89 |             time: "2018-10-31",
  90 |             open: 177.98,
  91 |             high: 178.85,
  92 |             low: 175.59,
  93 |             close: 175.88,
  94 |           },
  95 |           {
  96 |             time: "2018-11-01",
  97 |             open: 176.84,
  98 |             high: 180.86,
  99 |             low: 175.9,
 100 |             close: 180.46,
 101 |           },
 102 |           {
 103 |             time: "2018-11-02",
 104 |             open: 182.47,
 105 |             high: 183.01,
 106 |             low: 177.39,
 107 |             close: 179.93,
 108 |           },
 109 |           {
 110 |             time: "2018-11-05",
 111 |             open: 181.02,
 112 |             high: 182.41,
 113 |             low: 179.3,
 114 |             close: 182.19,
 115 |           },
 116 |           {
 117 |             time: "2018-11-06",
 118 |             open: 181.93,
 119 |             high: 182.65,
 120 |             low: 180.05,
 121 |             close: 182.01,
 122 |           },
 123 |           {
 124 |             time: "2018-11-07",
 125 |             open: 183.79,
 126 |             high: 187.68,
 127 |             low: 182.06,
 128 |             close: 187.23,
 129 |           },
 130 |           {
 131 |             time: "2018-11-08",
 132 |             open: 187.13,
 133 |             high: 188.69,
 134 |             low: 185.72,
 135 |             close: 188.0,
 136 |           },
 137 |           {
 138 |             time: "2018-11-09",
 139 |             open: 188.32,
 140 |             high: 188.48,
 141 |             low: 184.96,
 142 |             close: 185.99,
 143 |           },
 144 |           {
 145 |             time: "2018-11-12",
 146 |             open: 185.23,
 147 |             high: 186.95,
 148 |             low: 179.02,
 149 |             close: 179.43,
 150 |           },
 151 |           {
 152 |             time: "2018-11-13",
 153 |             open: 177.3,
 154 |             high: 181.62,
 155 |             low: 172.85,
 156 |             close: 179.0,
 157 |           },
 158 |           {
 159 |             time: "2018-11-14",
 160 |             open: 182.61,
 161 |             high: 182.9,
 162 |             low: 179.15,
 163 |             close: 179.9,
 164 |           },
 165 |           {
 166 |             time: "2018-11-15",
 167 |             open: 179.01,
 168 |             high: 179.67,
 169 |             low: 173.61,
 170 |             close: 177.36,
 171 |           },
 172 |           {
 173 |             time: "2018-11-16",
 174 |             open: 173.99,
 175 |             high: 177.6,
 176 |             low: 173.51,
 177 |             close: 177.02,
 178 |           },
 179 |           {
 180 |             time: "2018-11-19",
 181 |             open: 176.71,
 182 |             high: 178.88,
 183 |             low: 172.3,
 184 |             close: 173.59,
 185 |           },
 186 |           {
 187 |             time: "2018-11-20",
 188 |             open: 169.25,
 189 |             high: 172.0,
 190 |             low: 167.0,
 191 |             close: 169.05,
 192 |           },
 193 |           {
 194 |             time: "2018-11-21",
 195 |             open: 170.0,
 196 |             high: 170.93,
 197 |             low: 169.15,
 198 |             close: 169.3,
 199 |           },
 200 |           {
 201 |             time: "2018-11-23",
 202 |             open: 169.39,
 203 |             high: 170.33,
 204 |             low: 168.47,
 205 |             close: 168.85,
 206 |           },
 207 |           {
 208 |             time: "2018-11-26",
 209 |             open: 170.2,
 210 |             high: 172.39,
 211 |             low: 168.87,
 212 |             close: 169.82,
 213 |           },
 214 |           {
 215 |             time: "2018-11-27",
 216 |             open: 169.11,
 217 |             high: 173.38,
 218 |             low: 168.82,
 219 |             close: 173.22,
 220 |           },
 221 |           {
 222 |             time: "2018-11-28",
 223 |             open: 172.91,
 224 |             high: 177.65,
 225 |             low: 170.62,
 226 |             close: 177.43,
 227 |           },
 228 |           {
 229 |             time: "2018-11-29",
 230 |             open: 176.8,
 231 |             high: 177.27,
 232 |             low: 174.92,
 233 |             close: 175.66,
 234 |           },
 235 |           {
 236 |             time: "2018-11-30",
 237 |             open: 175.75,
 238 |             high: 180.37,
 239 |             low: 175.11,
 240 |             close: 180.32,
 241 |           },
 242 |           {
 243 |             time: "2018-12-03",
 244 |             open: 183.29,
 245 |             high: 183.5,
 246 |             low: 179.35,
 247 |             close: 181.74,
 248 |           },
 249 |           {
 250 |             time: "2018-12-04",
 251 |             open: 181.06,
 252 |             high: 182.23,
 253 |             low: 174.55,
 254 |             close: 175.3,
 255 |           },
 256 |           {
 257 |             time: "2018-12-06",
 258 |             open: 173.5,
 259 |             high: 176.04,
 260 |             low: 170.46,
 261 |             close: 175.96,
 262 |           },
 263 |           {
 264 |             time: "2018-12-07",
 265 |             open: 175.35,
 266 |             high: 178.36,
 267 |             low: 172.24,
 268 |             close: 172.79,
 269 |           },
 270 |           {
 271 |             time: "2018-12-10",
 272 |             open: 173.39,
 273 |             high: 173.99,
 274 |             low: 167.73,
 275 |             close: 171.69,
 276 |           },
 277 |           {
 278 |             time: "2018-12-11",
 279 |             open: 174.3,
 280 |             high: 175.6,
 281 |             low: 171.24,
 282 |             close: 172.21,
 283 |           },
 284 |           {
 285 |             time: "2018-12-12",
 286 |             open: 173.75,
 287 |             high: 176.87,
 288 |             low: 172.81,
 289 |             close: 174.21,
 290 |           },
 291 |           {
 292 |             time: "2018-12-13",
 293 |             open: 174.31,
 294 |             high: 174.91,
 295 |             low: 172.07,
 296 |             close: 173.87,
 297 |           },
 298 |           {
 299 |             time: "2018-12-14",
 300 |             open: 172.98,
 301 |             high: 175.14,
 302 |             low: 171.95,
 303 |             close: 172.29,
 304 |           },
 305 |           {
 306 |             time: "2018-12-17",
 307 |             open: 171.51,
 308 |             high: 171.99,
 309 |             low: 166.93,
 310 |             close: 167.97,
 311 |           },
 312 |           {
 313 |             time: "2018-12-18",
 314 |             open: 168.9,
 315 |             high: 171.95,
 316 |             low: 168.5,
 317 |             close: 170.04,
 318 |           },
 319 |           {
 320 |             time: "2018-12-19",
 321 |             open: 170.92,
 322 |             high: 174.95,
 323 |             low: 166.77,
 324 |             close: 167.56,
 325 |           },
 326 |           {
 327 |             time: "2018-12-20",
 328 |             open: 166.28,
 329 |             high: 167.31,
 330 |             low: 162.23,
 331 |             close: 164.16,
 332 |           },
 333 |           {
 334 |             time: "2018-12-21",
 335 |             open: 162.81,
 336 |             high: 167.96,
 337 |             low: 160.17,
 338 |             close: 160.48,
 339 |           },
 340 |           {
 341 |             time: "2018-12-24",
 342 |             open: 160.16,
 343 |             high: 161.4,
 344 |             low: 158.09,
 345 |             close: 158.14,
 346 |           },
 347 |           {
 348 |             time: "2018-12-26",
 349 |             open: 159.46,
 350 |             high: 168.28,
 351 |             low: 159.44,
 352 |             close: 168.28,
 353 |           },
 354 |           {
 355 |             time: "2018-12-27",
 356 |             open: 166.44,
 357 |             high: 170.46,
 358 |             low: 163.36,
 359 |             close: 170.32,
 360 |           },
 361 |           {
 362 |             time: "2018-12-28",
 363 |             open: 171.22,
 364 |             high: 173.12,
 365 |             low: 168.6,
 366 |             close: 170.22,
 367 |           },
 368 |           {
 369 |             time: "2018-12-31",
 370 |             open: 171.47,
 371 |             high: 173.24,
 372 |             low: 170.65,
 373 |             close: 171.82,
 374 |           },
 375 |           {
 376 |             time: "2019-01-02",
 377 |             open: 169.71,
 378 |             high: 173.18,
 379 |             low: 169.05,
 380 |             close: 172.41,
 381 |           },
 382 |           {
 383 |             time: "2019-01-03",
 384 |             open: 171.84,
 385 |             high: 171.84,
 386 |             low: 168.21,
 387 |             close: 168.61,
 388 |           },
 389 |           {
 390 |             time: "2019-01-04",
 391 |             open: 170.18,
 392 |             high: 174.74,
 393 |             low: 169.52,
 394 |             close: 173.62,
 395 |           },
 396 |           {
 397 |             time: "2019-01-07",
 398 |             open: 173.83,
 399 |             high: 178.18,
 400 |             low: 173.83,
 401 |             close: 177.04,
 402 |           },
 403 |           {
 404 |             time: "2019-01-08",
 405 |             open: 178.57,
 406 |             high: 179.59,
 407 |             low: 175.61,
 408 |             close: 177.89,
 409 |           },
 410 |           {
 411 |             time: "2019-01-09",
 412 |             open: 177.87,
 413 |             high: 181.27,
 414 |             low: 177.1,
 415 |             close: 179.73,
 416 |           },
 417 |           {
 418 |             time: "2019-01-10",
 419 |             open: 178.03,
 420 |             high: 179.24,
 421 |             low: 176.34,
 422 |             close: 179.06,
 423 |           },
 424 |           {
 425 |             time: "2019-01-11",
 426 |             open: 177.93,
 427 |             high: 180.26,
 428 |             low: 177.12,
 429 |             close: 179.41,
 430 |           },
 431 |           {
 432 |             time: "2019-01-14",
 433 |             open: 177.59,
 434 |             high: 179.23,
 435 |             low: 176.9,
 436 |             close: 178.81,
 437 |           },
 438 |           {
 439 |             time: "2019-01-15",
 440 |             open: 176.08,
 441 |             high: 177.82,
 442 |             low: 175.2,
 443 |             close: 176.47,
 444 |           },
 445 |           {
 446 |             time: "2019-01-16",
 447 |             open: 177.09,
 448 |             high: 177.93,
 449 |             low: 175.86,
 450 |             close: 177.04,
 451 |           },
 452 |           {
 453 |             time: "2019-01-17",
 454 |             open: 174.01,
 455 |             high: 175.46,
 456 |             low: 172.0,
 457 |             close: 174.87,
 458 |           },
 459 |           {
 460 |             time: "2019-01-18",
 461 |             open: 176.98,
 462 |             high: 180.04,
 463 |             low: 176.18,
 464 |             close: 179.58,
 465 |           },
 466 |           {
 467 |             time: "2019-01-22",
 468 |             open: 177.49,
 469 |             high: 178.6,
 470 |             low: 175.36,
 471 |             close: 177.11,
 472 |           },
 473 |           {
 474 |             time: "2019-01-23",
 475 |             open: 176.59,
 476 |             high: 178.06,
 477 |             low: 174.53,
 478 |             close: 176.89,
 479 |           },
 480 |           {
 481 |             time: "2019-01-24",
 482 |             open: 177.0,
 483 |             high: 177.53,
 484 |             low: 175.3,
 485 |             close: 177.29,
 486 |           },
 487 |           {
 488 |             time: "2019-01-25",
 489 |             open: 179.78,
 490 |             high: 180.87,
 491 |             low: 178.61,
 492 |             close: 180.4,
 493 |           },
 494 |           {
 495 |             time: "2019-01-28",
 496 |             open: 178.97,
 497 |             high: 179.99,
 498 |             low: 177.41,
 499 |             close: 179.83,
 500 |           },
 501 |           {
 502 |             time: "2019-01-29",
 503 |             open: 178.96,
 504 |             high: 180.15,
 505 |             low: 178.09,
 506 |             close: 179.69,
 507 |           },
 508 |           {
 509 |             time: "2019-01-30",
 510 |             open: 180.47,
 511 |             high: 184.2,
 512 |             low: 179.78,
 513 |             close: 182.18,
 514 |           },
 515 |           {
 516 |             time: "2019-01-31",
 517 |             open: 181.5,
 518 |             high: 184.67,
 519 |             low: 181.06,
 520 |             close: 183.53,
 521 |           },
 522 |           {
 523 |             time: "2019-02-01",
 524 |             open: 184.03,
 525 |             high: 185.15,
 526 |             low: 182.83,
 527 |             close: 184.37,
 528 |           },
 529 |           {
 530 |             time: "2019-02-04",
 531 |             open: 184.3,
 532 |             high: 186.43,
 533 |             low: 183.84,
 534 |             close: 186.43,
 535 |           },
 536 |           {
 537 |             time: "2019-02-05",
 538 |             open: 186.89,
 539 |             high: 186.99,
 540 |             low: 184.69,
 541 |             close: 186.39,
 542 |           },
 543 |           {
 544 |             time: "2019-02-06",
 545 |             open: 186.69,
 546 |             high: 186.69,
 547 |             low: 184.06,
 548 |             close: 184.72,
 549 |           },
 550 |           {
 551 |             time: "2019-02-07",
 552 |             open: 183.74,
 553 |             high: 184.92,
 554 |             low: 182.45,
 555 |             close: 184.07,
 556 |           },
 557 |           {
 558 |             time: "2019-02-08",
 559 |             open: 183.05,
 560 |             high: 184.58,
 561 |             low: 182.72,
 562 |             close: 184.54,
 563 |           },
 564 |           {
 565 |             time: "2019-02-11",
 566 |             open: 185.0,
 567 |             high: 185.42,
 568 |             low: 182.75,
 569 |             close: 182.92,
 570 |           },
 571 |           {
 572 |             time: "2019-02-12",
 573 |             open: 183.84,
 574 |             high: 186.4,
 575 |             low: 183.52,
 576 |             close: 185.52,
 577 |           },
 578 |           {
 579 |             time: "2019-02-13",
 580 |             open: 186.3,
 581 |             high: 188.68,
 582 |             low: 185.92,
 583 |             close: 188.41,
 584 |           },
 585 |           {
 586 |             time: "2019-02-14",
 587 |             open: 187.5,
 588 |             high: 188.93,
 589 |             low: 186.0,
 590 |             close: 187.71,
 591 |           },
 592 |           {
 593 |             time: "2019-02-15",
 594 |             open: 189.87,
 595 |             high: 192.62,
 596 |             low: 189.05,
 597 |             close: 192.39,
 598 |           },
 599 |           {
 600 |             time: "2019-02-19",
 601 |             open: 191.71,
 602 |             high: 193.19,
 603 |             low: 191.28,
 604 |             close: 192.33,
 605 |           },
 606 |           {
 607 |             time: "2019-02-20",
 608 |             open: 192.39,
 609 |             high: 192.4,
 610 |             low: 191.11,
 611 |             close: 191.85,
 612 |           },
 613 |           {
 614 |             time: "2019-02-21",
 615 |             open: 191.85,
 616 |             high: 192.37,
 617 |             low: 190.61,
 618 |             close: 191.82,
 619 |           },
 620 |           {
 621 |             time: "2019-02-22",
 622 |             open: 191.69,
 623 |             high: 192.54,
 624 |             low: 191.62,
 625 |             close: 192.39,
 626 |           },
 627 |           {
 628 |             time: "2019-02-25",
 629 |             open: 192.75,
 630 |             high: 193.42,
 631 |             low: 189.96,
 632 |             close: 189.98,
 633 |           },
 634 |           {
 635 |             time: "2019-02-26",
 636 |             open: 185.59,
 637 |             high: 188.47,
 638 |             low: 182.8,
 639 |             close: 188.3,
 640 |           },
 641 |           {
 642 |             time: "2019-02-27",
 643 |             open: 187.9,
 644 |             high: 188.5,
 645 |             low: 183.21,
 646 |             close: 183.67,
 647 |           },
 648 |           {
 649 |             time: "2019-02-28",
 650 |             open: 183.6,
 651 |             high: 185.19,
 652 |             low: 183.11,
 653 |             close: 185.14,
 654 |           },
 655 |           {
 656 |             time: "2019-03-01",
 657 |             open: 185.82,
 658 |             high: 186.56,
 659 |             low: 182.86,
 660 |             close: 185.17,
 661 |           },
 662 |           {
 663 |             time: "2019-03-04",
 664 |             open: 186.2,
 665 |             high: 186.24,
 666 |             low: 182.1,
 667 |             close: 183.81,
 668 |           },
 669 |           {
 670 |             time: "2019-03-05",
 671 |             open: 184.24,
 672 |             high: 185.12,
 673 |             low: 183.25,
 674 |             close: 184.0,
 675 |           },
 676 |           {
 677 |             time: "2019-03-06",
 678 |             open: 184.53,
 679 |             high: 184.97,
 680 |             low: 183.84,
 681 |             close: 184.45,
 682 |           },
 683 |           {
 684 |             time: "2019-03-07",
 685 |             open: 184.39,
 686 |             high: 184.62,
 687 |             low: 181.58,
 688 |             close: 182.51,
 689 |           },
 690 |           {
 691 |             time: "2019-03-08",
 692 |             open: 181.49,
 693 |             high: 181.91,
 694 |             low: 179.52,
 695 |             close: 181.23,
 696 |           },
 697 |           {
 698 |             time: "2019-03-11",
 699 |             open: 182.0,
 700 |             high: 183.2,
 701 |             low: 181.2,
 702 |             close: 182.44,
 703 |           },
 704 |           {
 705 |             time: "2019-03-12",
 706 |             open: 183.43,
 707 |             high: 184.27,
 708 |             low: 182.33,
 709 |             close: 184.0,
 710 |           },
 711 |           {
 712 |             time: "2019-03-13",
 713 |             open: 183.24,
 714 |             high: 183.78,
 715 |             low: 181.08,
 716 |             close: 181.14,
 717 |           },
 718 |           {
 719 |             time: "2019-03-14",
 720 |             open: 181.28,
 721 |             high: 181.74,
 722 |             low: 180.5,
 723 |             close: 181.61,
 724 |           },
 725 |           {
 726 |             time: "2019-03-15",
 727 |             open: 182.3,
 728 |             high: 182.49,
 729 |             low: 179.57,
 730 |             close: 182.23,
 731 |           },
 732 |           {
 733 |             time: "2019-03-18",
 734 |             open: 182.53,
 735 |             high: 183.48,
 736 |             low: 182.33,
 737 |             close: 183.42,
 738 |           },
 739 |           {
 740 |             time: "2019-03-19",
 741 |             open: 184.19,
 742 |             high: 185.82,
 743 |             low: 183.48,
 744 |             close: 184.13,
 745 |           },
 746 |           {
 747 |             time: "2019-03-20",
 748 |             open: 184.3,
 749 |             high: 187.12,
 750 |             low: 183.43,
 751 |             close: 186.1,
 752 |           },
 753 |           {
 754 |             time: "2019-03-21",
 755 |             open: 185.5,
 756 |             high: 190.0,
 757 |             low: 185.5,
 758 |             close: 189.97,
 759 |           },
 760 |           {
 761 |             time: "2019-03-22",
 762 |             open: 189.31,
 763 |             high: 192.05,
 764 |             low: 188.67,
 765 |             close: 188.75,
 766 |           },
 767 |           {
 768 |             time: "2019-03-25",
 769 |             open: 188.75,
 770 |             high: 191.71,
 771 |             low: 188.51,
 772 |             close: 189.68,
 773 |           },
 774 |           {
 775 |             time: "2019-03-26",
 776 |             open: 190.69,
 777 |             high: 192.19,
 778 |             low: 188.74,
 779 |             close: 189.34,
 780 |           },
 781 |           {
 782 |             time: "2019-03-27",
 783 |             open: 189.65,
 784 |             high: 191.61,
 785 |             low: 188.39,
 786 |             close: 189.25,
 787 |           },
 788 |           {
 789 |             time: "2019-03-28",
 790 |             open: 189.91,
 791 |             high: 191.4,
 792 |             low: 189.16,
 793 |             close: 190.06,
 794 |           },
 795 |           {
 796 |             time: "2019-03-29",
 797 |             open: 190.85,
 798 |             high: 192.04,
 799 |             low: 190.14,
 800 |             close: 191.89,
 801 |           },
 802 |           {
 803 |             time: "2019-04-01",
 804 |             open: 192.99,
 805 |             high: 195.9,
 806 |             low: 192.85,
 807 |             close: 195.64,
 808 |           },
 809 |           {
 810 |             time: "2019-04-02",
 811 |             open: 195.5,
 812 |             high: 195.5,
 813 |             low: 194.01,
 814 |             close: 194.31,
 815 |           },
 816 |           {
 817 |             time: "2019-04-03",
 818 |             open: 194.98,
 819 |             high: 198.78,
 820 |             low: 194.11,
 821 |             close: 198.61,
 822 |           },
 823 |           {
 824 |             time: "2019-04-04",
 825 |             open: 199.0,
 826 |             high: 200.49,
 827 |             low: 198.02,
 828 |             close: 200.45,
 829 |           },
 830 |           {
 831 |             time: "2019-04-05",
 832 |             open: 200.86,
 833 |             high: 203.13,
 834 |             low: 200.61,
 835 |             close: 202.06,
 836 |           },
 837 |           {
 838 |             time: "2019-04-08",
 839 |             open: 201.37,
 840 |             high: 203.79,
 841 |             low: 201.24,
 842 |             close: 203.55,
 843 |           },
 844 |           {
 845 |             time: "2019-04-09",
 846 |             open: 202.26,
 847 |             high: 202.71,
 848 |             low: 200.46,
 849 |             close: 200.9,
 850 |           },
 851 |           {
 852 |             time: "2019-04-10",
 853 |             open: 201.26,
 854 |             high: 201.6,
 855 |             low: 198.02,
 856 |             close: 199.43,
 857 |           },
 858 |           {
 859 |             time: "2019-04-11",
 860 |             open: 199.9,
 861 |             high: 201.5,
 862 |             low: 199.03,
 863 |             close: 201.48,
 864 |           },
 865 |           {
 866 |             time: "2019-04-12",
 867 |             open: 202.13,
 868 |             high: 204.26,
 869 |             low: 202.13,
 870 |             close: 203.85,
 871 |           },
 872 |           {
 873 |             time: "2019-04-15",
 874 |             open: 204.16,
 875 |             high: 205.14,
 876 |             low: 203.4,
 877 |             close: 204.86,
 878 |           },
 879 |           {
 880 |             time: "2019-04-16",
 881 |             open: 205.25,
 882 |             high: 205.99,
 883 |             low: 204.29,
 884 |             close: 204.47,
 885 |           },
 886 |           {
 887 |             time: "2019-04-17",
 888 |             open: 205.34,
 889 |             high: 206.84,
 890 |             low: 205.32,
 891 |             close: 206.55,
 892 |           },
 893 |           {
 894 |             time: "2019-04-18",
 895 |             open: 206.02,
 896 |             high: 207.78,
 897 |             low: 205.1,
 898 |             close: 205.66,
 899 |           },
 900 |           {
 901 |             time: "2019-04-22",
 902 |             open: 204.11,
 903 |             high: 206.25,
 904 |             low: 204.0,
 905 |             close: 204.78,
 906 |           },
 907 |           {
 908 |             time: "2019-04-23",
 909 |             open: 205.14,
 910 |             high: 207.33,
 911 |             low: 203.43,
 912 |             close: 206.05,
 913 |           },
 914 |           {
 915 |             time: "2019-04-24",
 916 |             open: 206.16,
 917 |             high: 208.29,
 918 |             low: 205.54,
 919 |             close: 206.72,
 920 |           },
 921 |           {
 922 |             time: "2019-04-25",
 923 |             open: 206.01,
 924 |             high: 207.72,
 925 |             low: 205.06,
 926 |             close: 206.5,
 927 |           },
 928 |           {
 929 |             time: "2019-04-26",
 930 |             open: 205.88,
 931 |             high: 206.14,
 932 |             low: 203.34,
 933 |             close: 203.61,
 934 |           },
 935 |           {
 936 |             time: "2019-04-29",
 937 |             open: 203.31,
 938 |             high: 203.8,
 939 |             low: 200.34,
 940 |             close: 202.16,
 941 |           },
 942 |           {
 943 |             time: "2019-04-30",
 944 |             open: 201.55,
 945 |             high: 203.75,
 946 |             low: 200.79,
 947 |             close: 203.7,
 948 |           },
 949 |           {
 950 |             time: "2019-05-01",
 951 |             open: 203.2,
 952 |             high: 203.52,
 953 |             low: 198.66,
 954 |             close: 198.8,
 955 |           },
 956 |           {
 957 |             time: "2019-05-02",
 958 |             open: 199.3,
 959 |             high: 201.06,
 960 |             low: 198.8,
 961 |             close: 201.01,
 962 |           },
 963 |           {
 964 |             time: "2019-05-03",
 965 |             open: 202.0,
 966 |             high: 202.31,
 967 |             low: 200.32,
 968 |             close: 200.56,
 969 |           },
 970 |           {
 971 |             time: "2019-05-06",
 972 |             open: 198.74,
 973 |             high: 199.93,
 974 |             low: 198.31,
 975 |             close: 199.63,
 976 |           },
 977 |           {
 978 |             time: "2019-05-07",
 979 |             open: 196.75,
 980 |             high: 197.65,
 981 |             low: 192.96,
 982 |             close: 194.77,
 983 |           },
 984 |           {
 985 |             time: "2019-05-08",
 986 |             open: 194.49,
 987 |             high: 196.61,
 988 |             low: 193.68,
 989 |             close: 195.17,
 990 |           },
 991 |           {
 992 |             time: "2019-05-09",
 993 |             open: 193.31,
 994 |             high: 195.08,
 995 |             low: 191.59,
 996 |             close: 194.58,
 997 |           },
 998 |           {
 999 |             time: "2019-05-10",
1000 |             open: 193.21,
1001 |             high: 195.49,
1002 |             low: 190.01,
1003 |             close: 194.58,
1004 |           },
1005 |           {
1006 |             time: "2019-05-13",
1007 |             open: 191.0,
1008 |             high: 191.66,
1009 |             low: 189.14,
1010 |             close: 190.34,
1011 |           },
1012 |           {
1013 |             time: "2019-05-14",
1014 |             open: 190.5,
1015 |             high: 192.76,
1016 |             low: 190.01,
1017 |             close: 191.62,
1018 |           },
1019 |           {
1020 |             time: "2019-05-15",
1021 |             open: 190.81,
1022 |             high: 192.81,
1023 |             low: 190.27,
1024 |             close: 191.76,
1025 |           },
1026 |           {
1027 |             time: "2019-05-16",
1028 |             open: 192.47,
1029 |             high: 194.96,
1030 |             low: 192.2,
1031 |             close: 192.38,
1032 |           },
1033 |           {
1034 |             time: "2019-05-17",
1035 |             open: 190.86,
1036 |             high: 194.5,
1037 |             low: 190.75,
1038 |             close: 192.58,
1039 |           },
1040 |           {
1041 |             time: "2019-05-20",
1042 |             open: 191.13,
1043 |             high: 192.86,
1044 |             low: 190.61,
1045 |             close: 190.95,
1046 |           },
1047 |           {
1048 |             time: "2019-05-21",
1049 |             open: 187.13,
1050 |             high: 192.52,
1051 |             low: 186.34,
1052 |             close: 191.45,
1053 |           },
1054 |           {
1055 |             time: "2019-05-22",
1056 |             open: 190.49,
1057 |             high: 192.22,
1058 |             low: 188.05,
1059 |             close: 188.91,
1060 |           },
1061 |           {
1062 |             time: "2019-05-23",
1063 |             open: 188.45,
1064 |             high: 192.54,
1065 |             low: 186.27,
1066 |             close: 192.0,
1067 |           },
1068 |           {
1069 |             time: "2019-05-24",
1070 |             open: 192.54,
1071 |             high: 193.86,
1072 |             low: 190.41,
1073 |             close: 193.59,
1074 |           },
1075 |         ];
1076 |       }
1077 | 
1078 |       // Create the Lightweight Chart within the container element
1079 |       const chart = LightweightCharts.createChart(
1080 |         document.getElementById('container')
1081 |       );
1082 | 
1083 |       // Generate sample data to use within a candlestick series
1084 |       const candleStickData = generateCandlestickData();
1085 | 
1086 |       // Create the Main Series (Candlesticks)
1087 |       const mainSeries = chart.addSeries(LightweightCharts.CandlestickSeries);
1088 |       // Set the data for the Main Series
1089 |       mainSeries.setData(candleStickData);
1090 | 
1091 |       // Adding a window resize event handler to resize the chart when
1092 |       // the window size changes.
1093 |       // Note: for more advanced examples (when the chart doesn't fill the entire window)
1094 |       // you may need to use ResizeObserver -> https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver
1095 |       window.addEventListener("resize", () => {
1096 |         chart.resize(window.innerWidth, window.innerHeight);
1097 |       });
1098 |     </script>
1099 |   </body>
1100 | </html>
1101 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/assets/step10.html:
--------------------------------------------------------------------------------
   1 | <!DOCTYPE html>
   2 | <!-- Please visit https://tradingview.github.io/lightweight-charts/tutorials/customization for more information on this tutorial. -->
   3 | <html>
   4 |   <head>
   5 |     <meta charset="UTF-8" />
   6 |     <meta
   7 |       name="viewport"
   8 |       content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0"
   9 |     />
  10 |     <title>Lightweight Charts™ Customization Tutorial</title>
  11 |     <!-- Adding Google Font -->
  12 |     <link rel="preconnect" href="https://fonts.googleapis.com" />
  13 |     <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  14 |     <link
  15 |       href="https://fonts.googleapis.com/css2?family=Roboto&display=swap"
  16 |       rel="stylesheet"
  17 |     />
  18 |     <!-- Adding the standalone version of Lightweight charts -->
  19 |     <script
  20 |       type="text/javascript"
  21 |       src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"
  22 |     ></script>
  23 |     <style>
  24 |       body {
  25 |         padding: 0;
  26 |         margin: 0;
  27 |         /* Add a background color to match the chart */
  28 |         background-color: #222;
  29 |       }
  30 |     </style>
  31 |   </head>
  32 | 
  33 |   <body>
  34 |     <div id="container" style="position: absolute; width: 100%; height: 100%"></div>
  35 |     <script type="text/javascript">
  36 |       // Function to generate a sample set of Candlestick datapoints
  37 |       function generateCandlestickData() {
  38 |         return [
  39 |           {
  40 |             time: "2018-10-19",
  41 |             open: 180.34,
  42 |             high: 180.99,
  43 |             low: 178.57,
  44 |             close: 179.85,
  45 |           },
  46 |           {
  47 |             time: "2018-10-22",
  48 |             open: 180.82,
  49 |             high: 181.4,
  50 |             low: 177.56,
  51 |             close: 178.75,
  52 |           },
  53 |           {
  54 |             time: "2018-10-23",
  55 |             open: 175.77,
  56 |             high: 179.49,
  57 |             low: 175.44,
  58 |             close: 178.53,
  59 |           },
  60 |           {
  61 |             time: "2018-10-24",
  62 |             open: 178.58,
  63 |             high: 182.37,
  64 |             low: 176.31,
  65 |             close: 176.97,
  66 |           },
  67 |           {
  68 |             time: "2018-10-25",
  69 |             open: 177.52,
  70 |             high: 180.5,
  71 |             low: 176.83,
  72 |             close: 179.07,
  73 |           },
  74 |           {
  75 |             time: "2018-10-26",
  76 |             open: 176.88,
  77 |             high: 177.34,
  78 |             low: 170.91,
  79 |             close: 172.23,
  80 |           },
  81 |           {
  82 |             time: "2018-10-29",
  83 |             open: 173.74,
  84 |             high: 175.99,
  85 |             low: 170.95,
  86 |             close: 173.2,
  87 |           },
  88 |           {
  89 |             time: "2018-10-30",
  90 |             open: 173.16,
  91 |             high: 176.43,
  92 |             low: 172.64,
  93 |             close: 176.24,
  94 |           },
  95 |           {
  96 |             time: "2018-10-31",
  97 |             open: 177.98,
  98 |             high: 178.85,
  99 |             low: 175.59,
 100 |             close: 175.88,
 101 |           },
 102 |           {
 103 |             time: "2018-11-01",
 104 |             open: 176.84,
 105 |             high: 180.86,
 106 |             low: 175.9,
 107 |             close: 180.46,
 108 |           },
 109 |           {
 110 |             time: "2018-11-02",
 111 |             open: 182.47,
 112 |             high: 183.01,
 113 |             low: 177.39,
 114 |             close: 179.93,
 115 |           },
 116 |           {
 117 |             time: "2018-11-05",
 118 |             open: 181.02,
 119 |             high: 182.41,
 120 |             low: 179.3,
 121 |             close: 182.19,
 122 |           },
 123 |           {
 124 |             time: "2018-11-06",
 125 |             open: 181.93,
 126 |             high: 182.65,
 127 |             low: 180.05,
 128 |             close: 182.01,
 129 |           },
 130 |           {
 131 |             time: "2018-11-07",
 132 |             open: 183.79,
 133 |             high: 187.68,
 134 |             low: 182.06,
 135 |             close: 187.23,
 136 |           },
 137 |           {
 138 |             time: "2018-11-08",
 139 |             open: 187.13,
 140 |             high: 188.69,
 141 |             low: 185.72,
 142 |             close: 188.0,
 143 |           },
 144 |           {
 145 |             time: "2018-11-09",
 146 |             open: 188.32,
 147 |             high: 188.48,
 148 |             low: 184.96,
 149 |             close: 185.99,
 150 |           },
 151 |           {
 152 |             time: "2018-11-12",
 153 |             open: 185.23,
 154 |             high: 186.95,
 155 |             low: 179.02,
 156 |             close: 179.43,
 157 |           },
 158 |           {
 159 |             time: "2018-11-13",
 160 |             open: 177.3,
 161 |             high: 181.62,
 162 |             low: 172.85,
 163 |             close: 179.0,
 164 |           },
 165 |           {
 166 |             time: "2018-11-14",
 167 |             open: 182.61,
 168 |             high: 182.9,
 169 |             low: 179.15,
 170 |             close: 179.9,
 171 |           },
 172 |           {
 173 |             time: "2018-11-15",
 174 |             open: 179.01,
 175 |             high: 179.67,
 176 |             low: 173.61,
 177 |             close: 177.36,
 178 |           },
 179 |           {
 180 |             time: "2018-11-16",
 181 |             open: 173.99,
 182 |             high: 177.6,
 183 |             low: 173.51,
 184 |             close: 177.02,
 185 |           },
 186 |           {
 187 |             time: "2018-11-19",
 188 |             open: 176.71,
 189 |             high: 178.88,
 190 |             low: 172.3,
 191 |             close: 173.59,
 192 |           },
 193 |           {
 194 |             time: "2018-11-20",
 195 |             open: 169.25,
 196 |             high: 172.0,
 197 |             low: 167.0,
 198 |             close: 169.05,
 199 |           },
 200 |           {
 201 |             time: "2018-11-21",
 202 |             open: 170.0,
 203 |             high: 170.93,
 204 |             low: 169.15,
 205 |             close: 169.3,
 206 |           },
 207 |           {
 208 |             time: "2018-11-23",
 209 |             open: 169.39,
 210 |             high: 170.33,
 211 |             low: 168.47,
 212 |             close: 168.85,
 213 |           },
 214 |           {
 215 |             time: "2018-11-26",
 216 |             open: 170.2,
 217 |             high: 172.39,
 218 |             low: 168.87,
 219 |             close: 169.82,
 220 |           },
 221 |           {
 222 |             time: "2018-11-27",
 223 |             open: 169.11,
 224 |             high: 173.38,
 225 |             low: 168.82,
 226 |             close: 173.22,
 227 |           },
 228 |           {
 229 |             time: "2018-11-28",
 230 |             open: 172.91,
 231 |             high: 177.65,
 232 |             low: 170.62,
 233 |             close: 177.43,
 234 |           },
 235 |           {
 236 |             time: "2018-11-29",
 237 |             open: 176.8,
 238 |             high: 177.27,
 239 |             low: 174.92,
 240 |             close: 175.66,
 241 |           },
 242 |           {
 243 |             time: "2018-11-30",
 244 |             open: 175.75,
 245 |             high: 180.37,
 246 |             low: 175.11,
 247 |             close: 180.32,
 248 |           },
 249 |           {
 250 |             time: "2018-12-03",
 251 |             open: 183.29,
 252 |             high: 183.5,
 253 |             low: 179.35,
 254 |             close: 181.74,
 255 |           },
 256 |           {
 257 |             time: "2018-12-04",
 258 |             open: 181.06,
 259 |             high: 182.23,
 260 |             low: 174.55,
 261 |             close: 175.3,
 262 |           },
 263 |           {
 264 |             time: "2018-12-06",
 265 |             open: 173.5,
 266 |             high: 176.04,
 267 |             low: 170.46,
 268 |             close: 175.96,
 269 |           },
 270 |           {
 271 |             time: "2018-12-07",
 272 |             open: 175.35,
 273 |             high: 178.36,
 274 |             low: 172.24,
 275 |             close: 172.79,
 276 |           },
 277 |           {
 278 |             time: "2018-12-10",
 279 |             open: 173.39,
 280 |             high: 173.99,
 281 |             low: 167.73,
 282 |             close: 171.69,
 283 |           },
 284 |           {
 285 |             time: "2018-12-11",
 286 |             open: 174.3,
 287 |             high: 175.6,
 288 |             low: 171.24,
 289 |             close: 172.21,
 290 |           },
 291 |           {
 292 |             time: "2018-12-12",
 293 |             open: 173.75,
 294 |             high: 176.87,
 295 |             low: 172.81,
 296 |             close: 174.21,
 297 |           },
 298 |           {
 299 |             time: "2018-12-13",
 300 |             open: 174.31,
 301 |             high: 174.91,
 302 |             low: 172.07,
 303 |             close: 173.87,
 304 |           },
 305 |           {
 306 |             time: "2018-12-14",
 307 |             open: 172.98,
 308 |             high: 175.14,
 309 |             low: 171.95,
 310 |             close: 172.29,
 311 |           },
 312 |           {
 313 |             time: "2018-12-17",
 314 |             open: 171.51,
 315 |             high: 171.99,
 316 |             low: 166.93,
 317 |             close: 167.97,
 318 |           },
 319 |           {
 320 |             time: "2018-12-18",
 321 |             open: 168.9,
 322 |             high: 171.95,
 323 |             low: 168.5,
 324 |             close: 170.04,
 325 |           },
 326 |           {
 327 |             time: "2018-12-19",
 328 |             open: 170.92,
 329 |             high: 174.95,
 330 |             low: 166.77,
 331 |             close: 167.56,
 332 |           },
 333 |           {
 334 |             time: "2018-12-20",
 335 |             open: 166.28,
 336 |             high: 167.31,
 337 |             low: 162.23,
 338 |             close: 164.16,
 339 |           },
 340 |           {
 341 |             time: "2018-12-21",
 342 |             open: 162.81,
 343 |             high: 167.96,
 344 |             low: 160.17,
 345 |             close: 160.48,
 346 |           },
 347 |           {
 348 |             time: "2018-12-24",
 349 |             open: 160.16,
 350 |             high: 161.4,
 351 |             low: 158.09,
 352 |             close: 158.14,
 353 |           },
 354 |           {
 355 |             time: "2018-12-26",
 356 |             open: 159.46,
 357 |             high: 168.28,
 358 |             low: 159.44,
 359 |             close: 168.28,
 360 |           },
 361 |           {
 362 |             time: "2018-12-27",
 363 |             open: 166.44,
 364 |             high: 170.46,
 365 |             low: 163.36,
 366 |             close: 170.32,
 367 |           },
 368 |           {
 369 |             time: "2018-12-28",
 370 |             open: 171.22,
 371 |             high: 173.12,
 372 |             low: 168.6,
 373 |             close: 170.22,
 374 |           },
 375 |           {
 376 |             time: "2018-12-31",
 377 |             open: 171.47,
 378 |             high: 173.24,
 379 |             low: 170.65,
 380 |             close: 171.82,
 381 |           },
 382 |           {
 383 |             time: "2019-01-02",
 384 |             open: 169.71,
 385 |             high: 173.18,
 386 |             low: 169.05,
 387 |             close: 172.41,
 388 |           },
 389 |           {
 390 |             time: "2019-01-03",
 391 |             open: 171.84,
 392 |             high: 171.84,
 393 |             low: 168.21,
 394 |             close: 168.61,
 395 |           },
 396 |           {
 397 |             time: "2019-01-04",
 398 |             open: 170.18,
 399 |             high: 174.74,
 400 |             low: 169.52,
 401 |             close: 173.62,
 402 |           },
 403 |           {
 404 |             time: "2019-01-07",
 405 |             open: 173.83,
 406 |             high: 178.18,
 407 |             low: 173.83,
 408 |             close: 177.04,
 409 |           },
 410 |           {
 411 |             time: "2019-01-08",
 412 |             open: 178.57,
 413 |             high: 179.59,
 414 |             low: 175.61,
 415 |             close: 177.89,
 416 |           },
 417 |           {
 418 |             time: "2019-01-09",
 419 |             open: 177.87,
 420 |             high: 181.27,
 421 |             low: 177.1,
 422 |             close: 179.73,
 423 |           },
 424 |           {
 425 |             time: "2019-01-10",
 426 |             open: 178.03,
 427 |             high: 179.24,
 428 |             low: 176.34,
 429 |             close: 179.06,
 430 |           },
 431 |           {
 432 |             time: "2019-01-11",
 433 |             open: 177.93,
 434 |             high: 180.26,
 435 |             low: 177.12,
 436 |             close: 179.41,
 437 |           },
 438 |           {
 439 |             time: "2019-01-14",
 440 |             open: 177.59,
 441 |             high: 179.23,
 442 |             low: 176.9,
 443 |             close: 178.81,
 444 |           },
 445 |           {
 446 |             time: "2019-01-15",
 447 |             open: 176.08,
 448 |             high: 177.82,
 449 |             low: 175.2,
 450 |             close: 176.47,
 451 |           },
 452 |           {
 453 |             time: "2019-01-16",
 454 |             open: 177.09,
 455 |             high: 177.93,
 456 |             low: 175.86,
 457 |             close: 177.04,
 458 |           },
 459 |           {
 460 |             time: "2019-01-17",
 461 |             open: 174.01,
 462 |             high: 175.46,
 463 |             low: 172.0,
 464 |             close: 174.87,
 465 |           },
 466 |           {
 467 |             time: "2019-01-18",
 468 |             open: 176.98,
 469 |             high: 180.04,
 470 |             low: 176.18,
 471 |             close: 179.58,
 472 |           },
 473 |           {
 474 |             time: "2019-01-22",
 475 |             open: 177.49,
 476 |             high: 178.6,
 477 |             low: 175.36,
 478 |             close: 177.11,
 479 |           },
 480 |           {
 481 |             time: "2019-01-23",
 482 |             open: 176.59,
 483 |             high: 178.06,
 484 |             low: 174.53,
 485 |             close: 176.89,
 486 |           },
 487 |           {
 488 |             time: "2019-01-24",
 489 |             open: 177.0,
 490 |             high: 177.53,
 491 |             low: 175.3,
 492 |             close: 177.29,
 493 |           },
 494 |           {
 495 |             time: "2019-01-25",
 496 |             open: 179.78,
 497 |             high: 180.87,
 498 |             low: 178.61,
 499 |             close: 180.4,
 500 |           },
 501 |           {
 502 |             time: "2019-01-28",
 503 |             open: 178.97,
 504 |             high: 179.99,
 505 |             low: 177.41,
 506 |             close: 179.83,
 507 |           },
 508 |           {
 509 |             time: "2019-01-29",
 510 |             open: 178.96,
 511 |             high: 180.15,
 512 |             low: 178.09,
 513 |             close: 179.69,
 514 |           },
 515 |           {
 516 |             time: "2019-01-30",
 517 |             open: 180.47,
 518 |             high: 184.2,
 519 |             low: 179.78,
 520 |             close: 182.18,
 521 |           },
 522 |           {
 523 |             time: "2019-01-31",
 524 |             open: 181.5,
 525 |             high: 184.67,
 526 |             low: 181.06,
 527 |             close: 183.53,
 528 |           },
 529 |           {
 530 |             time: "2019-02-01",
 531 |             open: 184.03,
 532 |             high: 185.15,
 533 |             low: 182.83,
 534 |             close: 184.37,
 535 |           },
 536 |           {
 537 |             time: "2019-02-04",
 538 |             open: 184.3,
 539 |             high: 186.43,
 540 |             low: 183.84,
 541 |             close: 186.43,
 542 |           },
 543 |           {
 544 |             time: "2019-02-05",
 545 |             open: 186.89,
 546 |             high: 186.99,
 547 |             low: 184.69,
 548 |             close: 186.39,
 549 |           },
 550 |           {
 551 |             time: "2019-02-06",
 552 |             open: 186.69,
 553 |             high: 186.69,
 554 |             low: 184.06,
 555 |             close: 184.72,
 556 |           },
 557 |           {
 558 |             time: "2019-02-07",
 559 |             open: 183.74,
 560 |             high: 184.92,
 561 |             low: 182.45,
 562 |             close: 184.07,
 563 |           },
 564 |           {
 565 |             time: "2019-02-08",
 566 |             open: 183.05,
 567 |             high: 184.58,
 568 |             low: 182.72,
 569 |             close: 184.54,
 570 |           },
 571 |           {
 572 |             time: "2019-02-11",
 573 |             open: 185.0,
 574 |             high: 185.42,
 575 |             low: 182.75,
 576 |             close: 182.92,
 577 |           },
 578 |           {
 579 |             time: "2019-02-12",
 580 |             open: 183.84,
 581 |             high: 186.4,
 582 |             low: 183.52,
 583 |             close: 185.52,
 584 |           },
 585 |           {
 586 |             time: "2019-02-13",
 587 |             open: 186.3,
 588 |             high: 188.68,
 589 |             low: 185.92,
 590 |             close: 188.41,
 591 |           },
 592 |           {
 593 |             time: "2019-02-14",
 594 |             open: 187.5,
 595 |             high: 188.93,
 596 |             low: 186.0,
 597 |             close: 187.71,
 598 |           },
 599 |           {
 600 |             time: "2019-02-15",
 601 |             open: 189.87,
 602 |             high: 192.62,
 603 |             low: 189.05,
 604 |             close: 192.39,
 605 |           },
 606 |           {
 607 |             time: "2019-02-19",
 608 |             open: 191.71,
 609 |             high: 193.19,
 610 |             low: 191.28,
 611 |             close: 192.33,
 612 |           },
 613 |           {
 614 |             time: "2019-02-20",
 615 |             open: 192.39,
 616 |             high: 192.4,
 617 |             low: 191.11,
 618 |             close: 191.85,
 619 |           },
 620 |           {
 621 |             time: "2019-02-21",
 622 |             open: 191.85,
 623 |             high: 192.37,
 624 |             low: 190.61,
 625 |             close: 191.82,
 626 |           },
 627 |           {
 628 |             time: "2019-02-22",
 629 |             open: 191.69,
 630 |             high: 192.54,
 631 |             low: 191.62,
 632 |             close: 192.39,
 633 |           },
 634 |           {
 635 |             time: "2019-02-25",
 636 |             open: 192.75,
 637 |             high: 193.42,
 638 |             low: 189.96,
 639 |             close: 189.98,
 640 |           },
 641 |           {
 642 |             time: "2019-02-26",
 643 |             open: 185.59,
 644 |             high: 188.47,
 645 |             low: 182.8,
 646 |             close: 188.3,
 647 |           },
 648 |           {
 649 |             time: "2019-02-27",
 650 |             open: 187.9,
 651 |             high: 188.5,
 652 |             low: 183.21,
 653 |             close: 183.67,
 654 |           },
 655 |           {
 656 |             time: "2019-02-28",
 657 |             open: 183.6,
 658 |             high: 185.19,
 659 |             low: 183.11,
 660 |             close: 185.14,
 661 |           },
 662 |           {
 663 |             time: "2019-03-01",
 664 |             open: 185.82,
 665 |             high: 186.56,
 666 |             low: 182.86,
 667 |             close: 185.17,
 668 |           },
 669 |           {
 670 |             time: "2019-03-04",
 671 |             open: 186.2,
 672 |             high: 186.24,
 673 |             low: 182.1,
 674 |             close: 183.81,
 675 |           },
 676 |           {
 677 |             time: "2019-03-05",
 678 |             open: 184.24,
 679 |             high: 185.12,
 680 |             low: 183.25,
 681 |             close: 184.0,
 682 |           },
 683 |           {
 684 |             time: "2019-03-06",
 685 |             open: 184.53,
 686 |             high: 184.97,
 687 |             low: 183.84,
 688 |             close: 184.45,
 689 |           },
 690 |           {
 691 |             time: "2019-03-07",
 692 |             open: 184.39,
 693 |             high: 184.62,
 694 |             low: 181.58,
 695 |             close: 182.51,
 696 |           },
 697 |           {
 698 |             time: "2019-03-08",
 699 |             open: 181.49,
 700 |             high: 181.91,
 701 |             low: 179.52,
 702 |             close: 181.23,
 703 |           },
 704 |           {
 705 |             time: "2019-03-11",
 706 |             open: 182.0,
 707 |             high: 183.2,
 708 |             low: 181.2,
 709 |             close: 182.44,
 710 |           },
 711 |           {
 712 |             time: "2019-03-12",
 713 |             open: 183.43,
 714 |             high: 184.27,
 715 |             low: 182.33,
 716 |             close: 184.0,
 717 |           },
 718 |           {
 719 |             time: "2019-03-13",
 720 |             open: 183.24,
 721 |             high: 183.78,
 722 |             low: 181.08,
 723 |             close: 181.14,
 724 |           },
 725 |           {
 726 |             time: "2019-03-14",
 727 |             open: 181.28,
 728 |             high: 181.74,
 729 |             low: 180.5,
 730 |             close: 181.61,
 731 |           },
 732 |           {
 733 |             time: "2019-03-15",
 734 |             open: 182.3,
 735 |             high: 182.49,
 736 |             low: 179.57,
 737 |             close: 182.23,
 738 |           },
 739 |           {
 740 |             time: "2019-03-18",
 741 |             open: 182.53,
 742 |             high: 183.48,
 743 |             low: 182.33,
 744 |             close: 183.42,
 745 |           },
 746 |           {
 747 |             time: "2019-03-19",
 748 |             open: 184.19,
 749 |             high: 185.82,
 750 |             low: 183.48,
 751 |             close: 184.13,
 752 |           },
 753 |           {
 754 |             time: "2019-03-20",
 755 |             open: 184.3,
 756 |             high: 187.12,
 757 |             low: 183.43,
 758 |             close: 186.1,
 759 |           },
 760 |           {
 761 |             time: "2019-03-21",
 762 |             open: 185.5,
 763 |             high: 190.0,
 764 |             low: 185.5,
 765 |             close: 189.97,
 766 |           },
 767 |           {
 768 |             time: "2019-03-22",
 769 |             open: 189.31,
 770 |             high: 192.05,
 771 |             low: 188.67,
 772 |             close: 188.75,
 773 |           },
 774 |           {
 775 |             time: "2019-03-25",
 776 |             open: 188.75,
 777 |             high: 191.71,
 778 |             low: 188.51,
 779 |             close: 189.68,
 780 |           },
 781 |           {
 782 |             time: "2019-03-26",
 783 |             open: 190.69,
 784 |             high: 192.19,
 785 |             low: 188.74,
 786 |             close: 189.34,
 787 |           },
 788 |           {
 789 |             time: "2019-03-27",
 790 |             open: 189.65,
 791 |             high: 191.61,
 792 |             low: 188.39,
 793 |             close: 189.25,
 794 |           },
 795 |           {
 796 |             time: "2019-03-28",
 797 |             open: 189.91,
 798 |             high: 191.4,
 799 |             low: 189.16,
 800 |             close: 190.06,
 801 |           },
 802 |           {
 803 |             time: "2019-03-29",
 804 |             open: 190.85,
 805 |             high: 192.04,
 806 |             low: 190.14,
 807 |             close: 191.89,
 808 |           },
 809 |           {
 810 |             time: "2019-04-01",
 811 |             open: 192.99,
 812 |             high: 195.9,
 813 |             low: 192.85,
 814 |             close: 195.64,
 815 |           },
 816 |           {
 817 |             time: "2019-04-02",
 818 |             open: 195.5,
 819 |             high: 195.5,
 820 |             low: 194.01,
 821 |             close: 194.31,
 822 |           },
 823 |           {
 824 |             time: "2019-04-03",
 825 |             open: 194.98,
 826 |             high: 198.78,
 827 |             low: 194.11,
 828 |             close: 198.61,
 829 |           },
 830 |           {
 831 |             time: "2019-04-04",
 832 |             open: 199.0,
 833 |             high: 200.49,
 834 |             low: 198.02,
 835 |             close: 200.45,
 836 |           },
 837 |           {
 838 |             time: "2019-04-05",
 839 |             open: 200.86,
 840 |             high: 203.13,
 841 |             low: 200.61,
 842 |             close: 202.06,
 843 |           },
 844 |           {
 845 |             time: "2019-04-08",
 846 |             open: 201.37,
 847 |             high: 203.79,
 848 |             low: 201.24,
 849 |             close: 203.55,
 850 |           },
 851 |           {
 852 |             time: "2019-04-09",
 853 |             open: 202.26,
 854 |             high: 202.71,
 855 |             low: 200.46,
 856 |             close: 200.9,
 857 |           },
 858 |           {
 859 |             time: "2019-04-10",
 860 |             open: 201.26,
 861 |             high: 201.6,
 862 |             low: 198.02,
 863 |             close: 199.43,
 864 |           },
 865 |           {
 866 |             time: "2019-04-11",
 867 |             open: 199.9,
 868 |             high: 201.5,
 869 |             low: 199.03,
 870 |             close: 201.48,
 871 |           },
 872 |           {
 873 |             time: "2019-04-12",
 874 |             open: 202.13,
 875 |             high: 204.26,
 876 |             low: 202.13,
 877 |             close: 203.85,
 878 |           },
 879 |           {
 880 |             time: "2019-04-15",
 881 |             open: 204.16,
 882 |             high: 205.14,
 883 |             low: 203.4,
 884 |             close: 204.86,
 885 |           },
 886 |           {
 887 |             time: "2019-04-16",
 888 |             open: 205.25,
 889 |             high: 205.99,
 890 |             low: 204.29,
 891 |             close: 204.47,
 892 |           },
 893 |           {
 894 |             time: "2019-04-17",
 895 |             open: 205.34,
 896 |             high: 206.84,
 897 |             low: 205.32,
 898 |             close: 206.55,
 899 |           },
 900 |           {
 901 |             time: "2019-04-18",
 902 |             open: 206.02,
 903 |             high: 207.78,
 904 |             low: 205.1,
 905 |             close: 205.66,
 906 |           },
 907 |           {
 908 |             time: "2019-04-22",
 909 |             open: 204.11,
 910 |             high: 206.25,
 911 |             low: 204.0,
 912 |             close: 204.78,
 913 |           },
 914 |           {
 915 |             time: "2019-04-23",
 916 |             open: 205.14,
 917 |             high: 207.33,
 918 |             low: 203.43,
 919 |             close: 206.05,
 920 |           },
 921 |           {
 922 |             time: "2019-04-24",
 923 |             open: 206.16,
 924 |             high: 208.29,
 925 |             low: 205.54,
 926 |             close: 206.72,
 927 |           },
 928 |           {
 929 |             time: "2019-04-25",
 930 |             open: 206.01,
 931 |             high: 207.72,
 932 |             low: 205.06,
 933 |             close: 206.5,
 934 |           },
 935 |           {
 936 |             time: "2019-04-26",
 937 |             open: 205.88,
 938 |             high: 206.14,
 939 |             low: 203.34,
 940 |             close: 203.61,
 941 |           },
 942 |           {
 943 |             time: "2019-04-29",
 944 |             open: 203.31,
 945 |             high: 203.8,
 946 |             low: 200.34,
 947 |             close: 202.16,
 948 |           },
 949 |           {
 950 |             time: "2019-04-30",
 951 |             open: 201.55,
 952 |             high: 203.75,
 953 |             low: 200.79,
 954 |             close: 203.7,
 955 |           },
 956 |           {
 957 |             time: "2019-05-01",
 958 |             open: 203.2,
 959 |             high: 203.52,
 960 |             low: 198.66,
 961 |             close: 198.8,
 962 |           },
 963 |           {
 964 |             time: "2019-05-02",
 965 |             open: 199.3,
 966 |             high: 201.06,
 967 |             low: 198.8,
 968 |             close: 201.01,
 969 |           },
 970 |           {
 971 |             time: "2019-05-03",
 972 |             open: 202.0,
 973 |             high: 202.31,
 974 |             low: 200.32,
 975 |             close: 200.56,
 976 |           },
 977 |           {
 978 |             time: "2019-05-06",
 979 |             open: 198.74,
 980 |             high: 199.93,
 981 |             low: 198.31,
 982 |             close: 199.63,
 983 |           },
 984 |           {
 985 |             time: "2019-05-07",
 986 |             open: 196.75,
 987 |             high: 197.65,
 988 |             low: 192.96,
 989 |             close: 194.77,
 990 |           },
 991 |           {
 992 |             time: "2019-05-08",
 993 |             open: 194.49,
 994 |             high: 196.61,
 995 |             low: 193.68,
 996 |             close: 195.17,
 997 |           },
 998 |           {
 999 |             time: "2019-05-09",
1000 |             open: 193.31,
1001 |             high: 195.08,
1002 |             low: 191.59,
1003 |             close: 194.58,
1004 |           },
1005 |           {
1006 |             time: "2019-05-10",
1007 |             open: 193.21,
1008 |             high: 195.49,
1009 |             low: 190.01,
1010 |             close: 194.58,
1011 |           },
1012 |           {
1013 |             time: "2019-05-13",
1014 |             open: 191.0,
1015 |             high: 191.66,
1016 |             low: 189.14,
1017 |             close: 190.34,
1018 |           },
1019 |           {
1020 |             time: "2019-05-14",
1021 |             open: 190.5,
1022 |             high: 192.76,
1023 |             low: 190.01,
1024 |             close: 191.62,
1025 |           },
1026 |           {
1027 |             time: "2019-05-15",
1028 |             open: 190.81,
1029 |             high: 192.81,
1030 |             low: 190.27,
1031 |             close: 191.76,
1032 |           },
1033 |           {
1034 |             time: "2019-05-16",
1035 |             open: 192.47,
1036 |             high: 194.96,
1037 |             low: 192.2,
1038 |             close: 192.38,
1039 |           },
1040 |           {
1041 |             time: "2019-05-17",
1042 |             open: 190.86,
1043 |             high: 194.5,
1044 |             low: 190.75,
1045 |             close: 192.58,
1046 |           },
1047 |           {
1048 |             time: "2019-05-20",
1049 |             open: 191.13,
1050 |             high: 192.86,
1051 |             low: 190.61,
1052 |             close: 190.95,
1053 |           },
1054 |           {
1055 |             time: "2019-05-21",
1056 |             open: 187.13,
1057 |             high: 192.52,
1058 |             low: 186.34,
1059 |             close: 191.45,
1060 |           },
1061 |           {
1062 |             time: "2019-05-22",
1063 |             open: 190.49,
1064 |             high: 192.22,
1065 |             low: 188.05,
1066 |             close: 188.91,
1067 |           },
1068 |           {
1069 |             time: "2019-05-23",
1070 |             open: 188.45,
1071 |             high: 192.54,
1072 |             low: 186.27,
1073 |             close: 192.0,
1074 |           },
1075 |           {
1076 |             time: "2019-05-24",
1077 |             open: 192.54,
1078 |             high: 193.86,
1079 |             low: 190.41,
1080 |             close: 193.59,
1081 |           },
1082 |         ];
1083 |       }
1084 | 
1085 |       // Create the Lightweight Chart within the container element
1086 |       const chart = LightweightCharts.createChart(
1087 |         document.getElementById('container'),
1088 |         {
1089 |           layout: {
1090 |             background: { color: "#222" },
1091 |             textColor: "#C3BCDB",
1092 |           },
1093 |           grid: {
1094 |             vertLines: { color: "#444" },
1095 |             horzLines: { color: "#444" },
1096 |           },
1097 |         }
1098 |       );
1099 | 
1100 |       // Setting the border color for the vertical axis
1101 |       chart.priceScale().applyOptions({
1102 |         borderColor: "#71649C",
1103 |       });
1104 | 
1105 |       // Setting the border color for the horizontal axis
1106 |       chart.timeScale().applyOptions({
1107 |         borderColor: "#71649C",
1108 |       });
1109 | 
1110 |       // Adjust the starting bar width (essentially the horizontal zoom)
1111 |       chart.timeScale().applyOptions({
1112 |         barSpacing: 10,
1113 |       });
1114 | 
1115 |       // Changing the font
1116 |       chart.applyOptions({
1117 |         layout: {
1118 |           fontFamily: "'Roboto', sans-serif",
1119 |         },
1120 |       });
1121 | 
1122 |       // Get the current users primary locale
1123 |       const currentLocale = window.navigator.languages[0];
1124 |       // Create a number format using Intl.NumberFormat
1125 |       const myPriceFormatter = Intl.NumberFormat(currentLocale, {
1126 |         style: "currency",
1127 |         currency: "EUR", // Currency for data points
1128 |       }).format;
1129 | 
1130 |       // Apply the custom priceFormatter to the chart
1131 |       chart.applyOptions({
1132 |         localization: {
1133 |           priceFormatter: myPriceFormatter,
1134 |         },
1135 |       });
1136 | 
1137 |       // Customizing the Crosshair
1138 |       chart.applyOptions({
1139 |         crosshair: {
1140 |           // Change mode from default 'magnet' to 'normal'.
1141 |           // Allows the crosshair to move freely without snapping to datapoints
1142 |           mode: LightweightCharts.CrosshairMode.Normal,
1143 | 
1144 |           // Vertical crosshair line (showing Date in Label)
1145 |           vertLine: {
1146 |             width: 8,
1147 |             color: "#C3BCDB44",
1148 |             style: LightweightCharts.LineStyle.Solid,
1149 |             labelBackgroundColor: "#9B7DFF",
1150 |           },
1151 | 
1152 |           // Horizontal crosshair line (showing Price in Label)
1153 |           horzLine: {
1154 |             color: "#9B7DFF",
1155 |             labelBackgroundColor: "#9B7DFF",
1156 |           },
1157 |         },
1158 |       });
1159 | 
1160 |       // Generate sample data to use within a candlestick series
1161 |       const candleStickData = generateCandlestickData().map((datapoint) => {
1162 |         // map function is changing the color for the individual
1163 |         // candlestick points that close above 205
1164 |         if (datapoint.close < 205) return datapoint;
1165 |         // we are adding 'color' and 'wickColor' properties to the datapoint.
1166 |         // Using spread syntax: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#spread_in_object_literals
1167 |         return { ...datapoint, color: "orange", wickColor: "orange" };
1168 |       });
1169 | 
1170 |       // Convert the candlestick data for use with a line series
1171 |       const lineData = candleStickData.map((datapoint) => ({
1172 |         time: datapoint.time,
1173 |         value: (datapoint.close + datapoint.open) / 2,
1174 |       }));
1175 | 
1176 |       // Add an area series to the chart,
1177 |       // Adding this before we add the candlestick chart
1178 |       // so that it will appear beneath the candlesticks
1179 |       const areaSeries = chart.addSeries(LightweightCharts.AreaSeries, {
1180 |         lastValueVisible: false, // hide the last value marker for this series
1181 |         crosshairMarkerVisible: false, // hide the crosshair marker for this series
1182 |         lineColor: "transparent", // hide the line
1183 |         topColor: "rgba(56, 33, 110,0.6)",
1184 |         bottomColor: "rgba(56, 33, 110, 0.1)",
1185 |       });
1186 |       // Set the data for the Area Series
1187 |       areaSeries.setData(lineData);
1188 | 
1189 |       // Create the Main Series (Candlesticks)
1190 |       const mainSeries = chart.addSeries(LightweightCharts.CandlestickSeries);
1191 |       // Set the data for the Main Series
1192 |       mainSeries.setData(candleStickData);
1193 | 
1194 |       // Changing the Candlestick colors
1195 |       mainSeries.applyOptions({
1196 |         wickUpColor: "rgb(54, 116, 217)",
1197 |         upColor: "rgb(54, 116, 217)",
1198 |         wickDownColor: "rgb(225, 50, 85)",
1199 |         downColor: "rgb(225, 50, 85)",
1200 |         borderVisible: false,
1201 |       });
1202 | 
1203 |       // Adjust the options for the priceScale of the mainSeries
1204 |       mainSeries.priceScale().applyOptions({
1205 |         autoScale: false, // disables auto scaling based on visible content
1206 |         scaleMargins: {
1207 |           top: 0.1,
1208 |           bottom: 0.2,
1209 |         },
1210 |       });
1211 | 
1212 |       // Adding a window resize event handler to resize the chart when
1213 |       // the window size changes.
1214 |       // Note: for more advanced examples (when the chart doesn't fill the entire window)
1215 |       // you may need to use ResizeObserver -> https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver
1216 |       window.addEventListener("resize", () => {
1217 |         chart.resize(window.innerWidth, window.innerHeight);
1218 |       });
1219 |     </script>
1220 |   </body>
1221 | </html>
1222 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/assets/step2.html:
--------------------------------------------------------------------------------
   1 | <!DOCTYPE html>
   2 | <html>
   3 |   <head>
   4 |     <meta charset="UTF-8" />
   5 |     <meta
   6 |       name="viewport"
   7 |       content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0"
   8 |     />
   9 |     <title>Lightweight Charts™ Customization Tutorial</title>
  10 |     <!-- Adding the standalone version of Lightweight charts -->
  11 |     <script
  12 |       type="text/javascript"
  13 |       src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"
  14 |     ></script>
  15 |     <style>
  16 |       body {
  17 |         padding: 0;
  18 |         margin: 0;
  19 |         /* Add a background color to match the chart */
  20 |         background-color: #222;
  21 |       }
  22 |     </style>
  23 |   </head>
  24 | 
  25 |   <body>
  26 |     <div
  27 |       id="container"
  28 |       style="position: absolute; width: 100%; height: 100%"
  29 |     ></div>
  30 |     <script type="text/javascript">
  31 |       // Function to generate a sample set of Candlestick datapoints
  32 |       function generateCandlestickData() {
  33 |         return [
  34 |           {
  35 |             time: "2018-10-19",
  36 |             open: 180.34,
  37 |             high: 180.99,
  38 |             low: 178.57,
  39 |             close: 179.85,
  40 |           },
  41 |           {
  42 |             time: "2018-10-22",
  43 |             open: 180.82,
  44 |             high: 181.4,
  45 |             low: 177.56,
  46 |             close: 178.75,
  47 |           },
  48 |           {
  49 |             time: "2018-10-23",
  50 |             open: 175.77,
  51 |             high: 179.49,
  52 |             low: 175.44,
  53 |             close: 178.53,
  54 |           },
  55 |           {
  56 |             time: "2018-10-24",
  57 |             open: 178.58,
  58 |             high: 182.37,
  59 |             low: 176.31,
  60 |             close: 176.97,
  61 |           },
  62 |           {
  63 |             time: "2018-10-25",
  64 |             open: 177.52,
  65 |             high: 180.5,
  66 |             low: 176.83,
  67 |             close: 179.07,
  68 |           },
  69 |           {
  70 |             time: "2018-10-26",
  71 |             open: 176.88,
  72 |             high: 177.34,
  73 |             low: 170.91,
  74 |             close: 172.23,
  75 |           },
  76 |           {
  77 |             time: "2018-10-29",
  78 |             open: 173.74,
  79 |             high: 175.99,
  80 |             low: 170.95,
  81 |             close: 173.2,
  82 |           },
  83 |           {
  84 |             time: "2018-10-30",
  85 |             open: 173.16,
  86 |             high: 176.43,
  87 |             low: 172.64,
  88 |             close: 176.24,
  89 |           },
  90 |           {
  91 |             time: "2018-10-31",
  92 |             open: 177.98,
  93 |             high: 178.85,
  94 |             low: 175.59,
  95 |             close: 175.88,
  96 |           },
  97 |           {
  98 |             time: "2018-11-01",
  99 |             open: 176.84,
 100 |             high: 180.86,
 101 |             low: 175.9,
 102 |             close: 180.46,
 103 |           },
 104 |           {
 105 |             time: "2018-11-02",
 106 |             open: 182.47,
 107 |             high: 183.01,
 108 |             low: 177.39,
 109 |             close: 179.93,
 110 |           },
 111 |           {
 112 |             time: "2018-11-05",
 113 |             open: 181.02,
 114 |             high: 182.41,
 115 |             low: 179.3,
 116 |             close: 182.19,
 117 |           },
 118 |           {
 119 |             time: "2018-11-06",
 120 |             open: 181.93,
 121 |             high: 182.65,
 122 |             low: 180.05,
 123 |             close: 182.01,
 124 |           },
 125 |           {
 126 |             time: "2018-11-07",
 127 |             open: 183.79,
 128 |             high: 187.68,
 129 |             low: 182.06,
 130 |             close: 187.23,
 131 |           },
 132 |           {
 133 |             time: "2018-11-08",
 134 |             open: 187.13,
 135 |             high: 188.69,
 136 |             low: 185.72,
 137 |             close: 188.0,
 138 |           },
 139 |           {
 140 |             time: "2018-11-09",
 141 |             open: 188.32,
 142 |             high: 188.48,
 143 |             low: 184.96,
 144 |             close: 185.99,
 145 |           },
 146 |           {
 147 |             time: "2018-11-12",
 148 |             open: 185.23,
 149 |             high: 186.95,
 150 |             low: 179.02,
 151 |             close: 179.43,
 152 |           },
 153 |           {
 154 |             time: "2018-11-13",
 155 |             open: 177.3,
 156 |             high: 181.62,
 157 |             low: 172.85,
 158 |             close: 179.0,
 159 |           },
 160 |           {
 161 |             time: "2018-11-14",
 162 |             open: 182.61,
 163 |             high: 182.9,
 164 |             low: 179.15,
 165 |             close: 179.9,
 166 |           },
 167 |           {
 168 |             time: "2018-11-15",
 169 |             open: 179.01,
 170 |             high: 179.67,
 171 |             low: 173.61,
 172 |             close: 177.36,
 173 |           },
 174 |           {
 175 |             time: "2018-11-16",
 176 |             open: 173.99,
 177 |             high: 177.6,
 178 |             low: 173.51,
 179 |             close: 177.02,
 180 |           },
 181 |           {
 182 |             time: "2018-11-19",
 183 |             open: 176.71,
 184 |             high: 178.88,
 185 |             low: 172.3,
 186 |             close: 173.59,
 187 |           },
 188 |           {
 189 |             time: "2018-11-20",
 190 |             open: 169.25,
 191 |             high: 172.0,
 192 |             low: 167.0,
 193 |             close: 169.05,
 194 |           },
 195 |           {
 196 |             time: "2018-11-21",
 197 |             open: 170.0,
 198 |             high: 170.93,
 199 |             low: 169.15,
 200 |             close: 169.3,
 201 |           },
 202 |           {
 203 |             time: "2018-11-23",
 204 |             open: 169.39,
 205 |             high: 170.33,
 206 |             low: 168.47,
 207 |             close: 168.85,
 208 |           },
 209 |           {
 210 |             time: "2018-11-26",
 211 |             open: 170.2,
 212 |             high: 172.39,
 213 |             low: 168.87,
 214 |             close: 169.82,
 215 |           },
 216 |           {
 217 |             time: "2018-11-27",
 218 |             open: 169.11,
 219 |             high: 173.38,
 220 |             low: 168.82,
 221 |             close: 173.22,
 222 |           },
 223 |           {
 224 |             time: "2018-11-28",
 225 |             open: 172.91,
 226 |             high: 177.65,
 227 |             low: 170.62,
 228 |             close: 177.43,
 229 |           },
 230 |           {
 231 |             time: "2018-11-29",
 232 |             open: 176.8,
 233 |             high: 177.27,
 234 |             low: 174.92,
 235 |             close: 175.66,
 236 |           },
 237 |           {
 238 |             time: "2018-11-30",
 239 |             open: 175.75,
 240 |             high: 180.37,
 241 |             low: 175.11,
 242 |             close: 180.32,
 243 |           },
 244 |           {
 245 |             time: "2018-12-03",
 246 |             open: 183.29,
 247 |             high: 183.5,
 248 |             low: 179.35,
 249 |             close: 181.74,
 250 |           },
 251 |           {
 252 |             time: "2018-12-04",
 253 |             open: 181.06,
 254 |             high: 182.23,
 255 |             low: 174.55,
 256 |             close: 175.3,
 257 |           },
 258 |           {
 259 |             time: "2018-12-06",
 260 |             open: 173.5,
 261 |             high: 176.04,
 262 |             low: 170.46,
 263 |             close: 175.96,
 264 |           },
 265 |           {
 266 |             time: "2018-12-07",
 267 |             open: 175.35,
 268 |             high: 178.36,
 269 |             low: 172.24,
 270 |             close: 172.79,
 271 |           },
 272 |           {
 273 |             time: "2018-12-10",
 274 |             open: 173.39,
 275 |             high: 173.99,
 276 |             low: 167.73,
 277 |             close: 171.69,
 278 |           },
 279 |           {
 280 |             time: "2018-12-11",
 281 |             open: 174.3,
 282 |             high: 175.6,
 283 |             low: 171.24,
 284 |             close: 172.21,
 285 |           },
 286 |           {
 287 |             time: "2018-12-12",
 288 |             open: 173.75,
 289 |             high: 176.87,
 290 |             low: 172.81,
 291 |             close: 174.21,
 292 |           },
 293 |           {
 294 |             time: "2018-12-13",
 295 |             open: 174.31,
 296 |             high: 174.91,
 297 |             low: 172.07,
 298 |             close: 173.87,
 299 |           },
 300 |           {
 301 |             time: "2018-12-14",
 302 |             open: 172.98,
 303 |             high: 175.14,
 304 |             low: 171.95,
 305 |             close: 172.29,
 306 |           },
 307 |           {
 308 |             time: "2018-12-17",
 309 |             open: 171.51,
 310 |             high: 171.99,
 311 |             low: 166.93,
 312 |             close: 167.97,
 313 |           },
 314 |           {
 315 |             time: "2018-12-18",
 316 |             open: 168.9,
 317 |             high: 171.95,
 318 |             low: 168.5,
 319 |             close: 170.04,
 320 |           },
 321 |           {
 322 |             time: "2018-12-19",
 323 |             open: 170.92,
 324 |             high: 174.95,
 325 |             low: 166.77,
 326 |             close: 167.56,
 327 |           },
 328 |           {
 329 |             time: "2018-12-20",
 330 |             open: 166.28,
 331 |             high: 167.31,
 332 |             low: 162.23,
 333 |             close: 164.16,
 334 |           },
 335 |           {
 336 |             time: "2018-12-21",
 337 |             open: 162.81,
 338 |             high: 167.96,
 339 |             low: 160.17,
 340 |             close: 160.48,
 341 |           },
 342 |           {
 343 |             time: "2018-12-24",
 344 |             open: 160.16,
 345 |             high: 161.4,
 346 |             low: 158.09,
 347 |             close: 158.14,
 348 |           },
 349 |           {
 350 |             time: "2018-12-26",
 351 |             open: 159.46,
 352 |             high: 168.28,
 353 |             low: 159.44,
 354 |             close: 168.28,
 355 |           },
 356 |           {
 357 |             time: "2018-12-27",
 358 |             open: 166.44,
 359 |             high: 170.46,
 360 |             low: 163.36,
 361 |             close: 170.32,
 362 |           },
 363 |           {
 364 |             time: "2018-12-28",
 365 |             open: 171.22,
 366 |             high: 173.12,
 367 |             low: 168.6,
 368 |             close: 170.22,
 369 |           },
 370 |           {
 371 |             time: "2018-12-31",
 372 |             open: 171.47,
 373 |             high: 173.24,
 374 |             low: 170.65,
 375 |             close: 171.82,
 376 |           },
 377 |           {
 378 |             time: "2019-01-02",
 379 |             open: 169.71,
 380 |             high: 173.18,
 381 |             low: 169.05,
 382 |             close: 172.41,
 383 |           },
 384 |           {
 385 |             time: "2019-01-03",
 386 |             open: 171.84,
 387 |             high: 171.84,
 388 |             low: 168.21,
 389 |             close: 168.61,
 390 |           },
 391 |           {
 392 |             time: "2019-01-04",
 393 |             open: 170.18,
 394 |             high: 174.74,
 395 |             low: 169.52,
 396 |             close: 173.62,
 397 |           },
 398 |           {
 399 |             time: "2019-01-07",
 400 |             open: 173.83,
 401 |             high: 178.18,
 402 |             low: 173.83,
 403 |             close: 177.04,
 404 |           },
 405 |           {
 406 |             time: "2019-01-08",
 407 |             open: 178.57,
 408 |             high: 179.59,
 409 |             low: 175.61,
 410 |             close: 177.89,
 411 |           },
 412 |           {
 413 |             time: "2019-01-09",
 414 |             open: 177.87,
 415 |             high: 181.27,
 416 |             low: 177.1,
 417 |             close: 179.73,
 418 |           },
 419 |           {
 420 |             time: "2019-01-10",
 421 |             open: 178.03,
 422 |             high: 179.24,
 423 |             low: 176.34,
 424 |             close: 179.06,
 425 |           },
 426 |           {
 427 |             time: "2019-01-11",
 428 |             open: 177.93,
 429 |             high: 180.26,
 430 |             low: 177.12,
 431 |             close: 179.41,
 432 |           },
 433 |           {
 434 |             time: "2019-01-14",
 435 |             open: 177.59,
 436 |             high: 179.23,
 437 |             low: 176.9,
 438 |             close: 178.81,
 439 |           },
 440 |           {
 441 |             time: "2019-01-15",
 442 |             open: 176.08,
 443 |             high: 177.82,
 444 |             low: 175.2,
 445 |             close: 176.47,
 446 |           },
 447 |           {
 448 |             time: "2019-01-16",
 449 |             open: 177.09,
 450 |             high: 177.93,
 451 |             low: 175.86,
 452 |             close: 177.04,
 453 |           },
 454 |           {
 455 |             time: "2019-01-17",
 456 |             open: 174.01,
 457 |             high: 175.46,
 458 |             low: 172.0,
 459 |             close: 174.87,
 460 |           },
 461 |           {
 462 |             time: "2019-01-18",
 463 |             open: 176.98,
 464 |             high: 180.04,
 465 |             low: 176.18,
 466 |             close: 179.58,
 467 |           },
 468 |           {
 469 |             time: "2019-01-22",
 470 |             open: 177.49,
 471 |             high: 178.6,
 472 |             low: 175.36,
 473 |             close: 177.11,
 474 |           },
 475 |           {
 476 |             time: "2019-01-23",
 477 |             open: 176.59,
 478 |             high: 178.06,
 479 |             low: 174.53,
 480 |             close: 176.89,
 481 |           },
 482 |           {
 483 |             time: "2019-01-24",
 484 |             open: 177.0,
 485 |             high: 177.53,
 486 |             low: 175.3,
 487 |             close: 177.29,
 488 |           },
 489 |           {
 490 |             time: "2019-01-25",
 491 |             open: 179.78,
 492 |             high: 180.87,
 493 |             low: 178.61,
 494 |             close: 180.4,
 495 |           },
 496 |           {
 497 |             time: "2019-01-28",
 498 |             open: 178.97,
 499 |             high: 179.99,
 500 |             low: 177.41,
 501 |             close: 179.83,
 502 |           },
 503 |           {
 504 |             time: "2019-01-29",
 505 |             open: 178.96,
 506 |             high: 180.15,
 507 |             low: 178.09,
 508 |             close: 179.69,
 509 |           },
 510 |           {
 511 |             time: "2019-01-30",
 512 |             open: 180.47,
 513 |             high: 184.2,
 514 |             low: 179.78,
 515 |             close: 182.18,
 516 |           },
 517 |           {
 518 |             time: "2019-01-31",
 519 |             open: 181.5,
 520 |             high: 184.67,
 521 |             low: 181.06,
 522 |             close: 183.53,
 523 |           },
 524 |           {
 525 |             time: "2019-02-01",
 526 |             open: 184.03,
 527 |             high: 185.15,
 528 |             low: 182.83,
 529 |             close: 184.37,
 530 |           },
 531 |           {
 532 |             time: "2019-02-04",
 533 |             open: 184.3,
 534 |             high: 186.43,
 535 |             low: 183.84,
 536 |             close: 186.43,
 537 |           },
 538 |           {
 539 |             time: "2019-02-05",
 540 |             open: 186.89,
 541 |             high: 186.99,
 542 |             low: 184.69,
 543 |             close: 186.39,
 544 |           },
 545 |           {
 546 |             time: "2019-02-06",
 547 |             open: 186.69,
 548 |             high: 186.69,
 549 |             low: 184.06,
 550 |             close: 184.72,
 551 |           },
 552 |           {
 553 |             time: "2019-02-07",
 554 |             open: 183.74,
 555 |             high: 184.92,
 556 |             low: 182.45,
 557 |             close: 184.07,
 558 |           },
 559 |           {
 560 |             time: "2019-02-08",
 561 |             open: 183.05,
 562 |             high: 184.58,
 563 |             low: 182.72,
 564 |             close: 184.54,
 565 |           },
 566 |           {
 567 |             time: "2019-02-11",
 568 |             open: 185.0,
 569 |             high: 185.42,
 570 |             low: 182.75,
 571 |             close: 182.92,
 572 |           },
 573 |           {
 574 |             time: "2019-02-12",
 575 |             open: 183.84,
 576 |             high: 186.4,
 577 |             low: 183.52,
 578 |             close: 185.52,
 579 |           },
 580 |           {
 581 |             time: "2019-02-13",
 582 |             open: 186.3,
 583 |             high: 188.68,
 584 |             low: 185.92,
 585 |             close: 188.41,
 586 |           },
 587 |           {
 588 |             time: "2019-02-14",
 589 |             open: 187.5,
 590 |             high: 188.93,
 591 |             low: 186.0,
 592 |             close: 187.71,
 593 |           },
 594 |           {
 595 |             time: "2019-02-15",
 596 |             open: 189.87,
 597 |             high: 192.62,
 598 |             low: 189.05,
 599 |             close: 192.39,
 600 |           },
 601 |           {
 602 |             time: "2019-02-19",
 603 |             open: 191.71,
 604 |             high: 193.19,
 605 |             low: 191.28,
 606 |             close: 192.33,
 607 |           },
 608 |           {
 609 |             time: "2019-02-20",
 610 |             open: 192.39,
 611 |             high: 192.4,
 612 |             low: 191.11,
 613 |             close: 191.85,
 614 |           },
 615 |           {
 616 |             time: "2019-02-21",
 617 |             open: 191.85,
 618 |             high: 192.37,
 619 |             low: 190.61,
 620 |             close: 191.82,
 621 |           },
 622 |           {
 623 |             time: "2019-02-22",
 624 |             open: 191.69,
 625 |             high: 192.54,
 626 |             low: 191.62,
 627 |             close: 192.39,
 628 |           },
 629 |           {
 630 |             time: "2019-02-25",
 631 |             open: 192.75,
 632 |             high: 193.42,
 633 |             low: 189.96,
 634 |             close: 189.98,
 635 |           },
 636 |           {
 637 |             time: "2019-02-26",
 638 |             open: 185.59,
 639 |             high: 188.47,
 640 |             low: 182.8,
 641 |             close: 188.3,
 642 |           },
 643 |           {
 644 |             time: "2019-02-27",
 645 |             open: 187.9,
 646 |             high: 188.5,
 647 |             low: 183.21,
 648 |             close: 183.67,
 649 |           },
 650 |           {
 651 |             time: "2019-02-28",
 652 |             open: 183.6,
 653 |             high: 185.19,
 654 |             low: 183.11,
 655 |             close: 185.14,
 656 |           },
 657 |           {
 658 |             time: "2019-03-01",
 659 |             open: 185.82,
 660 |             high: 186.56,
 661 |             low: 182.86,
 662 |             close: 185.17,
 663 |           },
 664 |           {
 665 |             time: "2019-03-04",
 666 |             open: 186.2,
 667 |             high: 186.24,
 668 |             low: 182.1,
 669 |             close: 183.81,
 670 |           },
 671 |           {
 672 |             time: "2019-03-05",
 673 |             open: 184.24,
 674 |             high: 185.12,
 675 |             low: 183.25,
 676 |             close: 184.0,
 677 |           },
 678 |           {
 679 |             time: "2019-03-06",
 680 |             open: 184.53,
 681 |             high: 184.97,
 682 |             low: 183.84,
 683 |             close: 184.45,
 684 |           },
 685 |           {
 686 |             time: "2019-03-07",
 687 |             open: 184.39,
 688 |             high: 184.62,
 689 |             low: 181.58,
 690 |             close: 182.51,
 691 |           },
 692 |           {
 693 |             time: "2019-03-08",
 694 |             open: 181.49,
 695 |             high: 181.91,
 696 |             low: 179.52,
 697 |             close: 181.23,
 698 |           },
 699 |           {
 700 |             time: "2019-03-11",
 701 |             open: 182.0,
 702 |             high: 183.2,
 703 |             low: 181.2,
 704 |             close: 182.44,
 705 |           },
 706 |           {
 707 |             time: "2019-03-12",
 708 |             open: 183.43,
 709 |             high: 184.27,
 710 |             low: 182.33,
 711 |             close: 184.0,
 712 |           },
 713 |           {
 714 |             time: "2019-03-13",
 715 |             open: 183.24,
 716 |             high: 183.78,
 717 |             low: 181.08,
 718 |             close: 181.14,
 719 |           },
 720 |           {
 721 |             time: "2019-03-14",
 722 |             open: 181.28,
 723 |             high: 181.74,
 724 |             low: 180.5,
 725 |             close: 181.61,
 726 |           },
 727 |           {
 728 |             time: "2019-03-15",
 729 |             open: 182.3,
 730 |             high: 182.49,
 731 |             low: 179.57,
 732 |             close: 182.23,
 733 |           },
 734 |           {
 735 |             time: "2019-03-18",
 736 |             open: 182.53,
 737 |             high: 183.48,
 738 |             low: 182.33,
 739 |             close: 183.42,
 740 |           },
 741 |           {
 742 |             time: "2019-03-19",
 743 |             open: 184.19,
 744 |             high: 185.82,
 745 |             low: 183.48,
 746 |             close: 184.13,
 747 |           },
 748 |           {
 749 |             time: "2019-03-20",
 750 |             open: 184.3,
 751 |             high: 187.12,
 752 |             low: 183.43,
 753 |             close: 186.1,
 754 |           },
 755 |           {
 756 |             time: "2019-03-21",
 757 |             open: 185.5,
 758 |             high: 190.0,
 759 |             low: 185.5,
 760 |             close: 189.97,
 761 |           },
 762 |           {
 763 |             time: "2019-03-22",
 764 |             open: 189.31,
 765 |             high: 192.05,
 766 |             low: 188.67,
 767 |             close: 188.75,
 768 |           },
 769 |           {
 770 |             time: "2019-03-25",
 771 |             open: 188.75,
 772 |             high: 191.71,
 773 |             low: 188.51,
 774 |             close: 189.68,
 775 |           },
 776 |           {
 777 |             time: "2019-03-26",
 778 |             open: 190.69,
 779 |             high: 192.19,
 780 |             low: 188.74,
 781 |             close: 189.34,
 782 |           },
 783 |           {
 784 |             time: "2019-03-27",
 785 |             open: 189.65,
 786 |             high: 191.61,
 787 |             low: 188.39,
 788 |             close: 189.25,
 789 |           },
 790 |           {
 791 |             time: "2019-03-28",
 792 |             open: 189.91,
 793 |             high: 191.4,
 794 |             low: 189.16,
 795 |             close: 190.06,
 796 |           },
 797 |           {
 798 |             time: "2019-03-29",
 799 |             open: 190.85,
 800 |             high: 192.04,
 801 |             low: 190.14,
 802 |             close: 191.89,
 803 |           },
 804 |           {
 805 |             time: "2019-04-01",
 806 |             open: 192.99,
 807 |             high: 195.9,
 808 |             low: 192.85,
 809 |             close: 195.64,
 810 |           },
 811 |           {
 812 |             time: "2019-04-02",
 813 |             open: 195.5,
 814 |             high: 195.5,
 815 |             low: 194.01,
 816 |             close: 194.31,
 817 |           },
 818 |           {
 819 |             time: "2019-04-03",
 820 |             open: 194.98,
 821 |             high: 198.78,
 822 |             low: 194.11,
 823 |             close: 198.61,
 824 |           },
 825 |           {
 826 |             time: "2019-04-04",
 827 |             open: 199.0,
 828 |             high: 200.49,
 829 |             low: 198.02,
 830 |             close: 200.45,
 831 |           },
 832 |           {
 833 |             time: "2019-04-05",
 834 |             open: 200.86,
 835 |             high: 203.13,
 836 |             low: 200.61,
 837 |             close: 202.06,
 838 |           },
 839 |           {
 840 |             time: "2019-04-08",
 841 |             open: 201.37,
 842 |             high: 203.79,
 843 |             low: 201.24,
 844 |             close: 203.55,
 845 |           },
 846 |           {
 847 |             time: "2019-04-09",
 848 |             open: 202.26,
 849 |             high: 202.71,
 850 |             low: 200.46,
 851 |             close: 200.9,
 852 |           },
 853 |           {
 854 |             time: "2019-04-10",
 855 |             open: 201.26,
 856 |             high: 201.6,
 857 |             low: 198.02,
 858 |             close: 199.43,
 859 |           },
 860 |           {
 861 |             time: "2019-04-11",
 862 |             open: 199.9,
 863 |             high: 201.5,
 864 |             low: 199.03,
 865 |             close: 201.48,
 866 |           },
 867 |           {
 868 |             time: "2019-04-12",
 869 |             open: 202.13,
 870 |             high: 204.26,
 871 |             low: 202.13,
 872 |             close: 203.85,
 873 |           },
 874 |           {
 875 |             time: "2019-04-15",
 876 |             open: 204.16,
 877 |             high: 205.14,
 878 |             low: 203.4,
 879 |             close: 204.86,
 880 |           },
 881 |           {
 882 |             time: "2019-04-16",
 883 |             open: 205.25,
 884 |             high: 205.99,
 885 |             low: 204.29,
 886 |             close: 204.47,
 887 |           },
 888 |           {
 889 |             time: "2019-04-17",
 890 |             open: 205.34,
 891 |             high: 206.84,
 892 |             low: 205.32,
 893 |             close: 206.55,
 894 |           },
 895 |           {
 896 |             time: "2019-04-18",
 897 |             open: 206.02,
 898 |             high: 207.78,
 899 |             low: 205.1,
 900 |             close: 205.66,
 901 |           },
 902 |           {
 903 |             time: "2019-04-22",
 904 |             open: 204.11,
 905 |             high: 206.25,
 906 |             low: 204.0,
 907 |             close: 204.78,
 908 |           },
 909 |           {
 910 |             time: "2019-04-23",
 911 |             open: 205.14,
 912 |             high: 207.33,
 913 |             low: 203.43,
 914 |             close: 206.05,
 915 |           },
 916 |           {
 917 |             time: "2019-04-24",
 918 |             open: 206.16,
 919 |             high: 208.29,
 920 |             low: 205.54,
 921 |             close: 206.72,
 922 |           },
 923 |           {
 924 |             time: "2019-04-25",
 925 |             open: 206.01,
 926 |             high: 207.72,
 927 |             low: 205.06,
 928 |             close: 206.5,
 929 |           },
 930 |           {
 931 |             time: "2019-04-26",
 932 |             open: 205.88,
 933 |             high: 206.14,
 934 |             low: 203.34,
 935 |             close: 203.61,
 936 |           },
 937 |           {
 938 |             time: "2019-04-29",
 939 |             open: 203.31,
 940 |             high: 203.8,
 941 |             low: 200.34,
 942 |             close: 202.16,
 943 |           },
 944 |           {
 945 |             time: "2019-04-30",
 946 |             open: 201.55,
 947 |             high: 203.75,
 948 |             low: 200.79,
 949 |             close: 203.7,
 950 |           },
 951 |           {
 952 |             time: "2019-05-01",
 953 |             open: 203.2,
 954 |             high: 203.52,
 955 |             low: 198.66,
 956 |             close: 198.8,
 957 |           },
 958 |           {
 959 |             time: "2019-05-02",
 960 |             open: 199.3,
 961 |             high: 201.06,
 962 |             low: 198.8,
 963 |             close: 201.01,
 964 |           },
 965 |           {
 966 |             time: "2019-05-03",
 967 |             open: 202.0,
 968 |             high: 202.31,
 969 |             low: 200.32,
 970 |             close: 200.56,
 971 |           },
 972 |           {
 973 |             time: "2019-05-06",
 974 |             open: 198.74,
 975 |             high: 199.93,
 976 |             low: 198.31,
 977 |             close: 199.63,
 978 |           },
 979 |           {
 980 |             time: "2019-05-07",
 981 |             open: 196.75,
 982 |             high: 197.65,
 983 |             low: 192.96,
 984 |             close: 194.77,
 985 |           },
 986 |           {
 987 |             time: "2019-05-08",
 988 |             open: 194.49,
 989 |             high: 196.61,
 990 |             low: 193.68,
 991 |             close: 195.17,
 992 |           },
 993 |           {
 994 |             time: "2019-05-09",
 995 |             open: 193.31,
 996 |             high: 195.08,
 997 |             low: 191.59,
 998 |             close: 194.58,
 999 |           },
1000 |           {
1001 |             time: "2019-05-10",
1002 |             open: 193.21,
1003 |             high: 195.49,
1004 |             low: 190.01,
1005 |             close: 194.58,
1006 |           },
1007 |           {
1008 |             time: "2019-05-13",
1009 |             open: 191.0,
1010 |             high: 191.66,
1011 |             low: 189.14,
1012 |             close: 190.34,
1013 |           },
1014 |           {
1015 |             time: "2019-05-14",
1016 |             open: 190.5,
1017 |             high: 192.76,
1018 |             low: 190.01,
1019 |             close: 191.62,
1020 |           },
1021 |           {
1022 |             time: "2019-05-15",
1023 |             open: 190.81,
1024 |             high: 192.81,
1025 |             low: 190.27,
1026 |             close: 191.76,
1027 |           },
1028 |           {
1029 |             time: "2019-05-16",
1030 |             open: 192.47,
1031 |             high: 194.96,
1032 |             low: 192.2,
1033 |             close: 192.38,
1034 |           },
1035 |           {
1036 |             time: "2019-05-17",
1037 |             open: 190.86,
1038 |             high: 194.5,
1039 |             low: 190.75,
1040 |             close: 192.58,
1041 |           },
1042 |           {
1043 |             time: "2019-05-20",
1044 |             open: 191.13,
1045 |             high: 192.86,
1046 |             low: 190.61,
1047 |             close: 190.95,
1048 |           },
1049 |           {
1050 |             time: "2019-05-21",
1051 |             open: 187.13,
1052 |             high: 192.52,
1053 |             low: 186.34,
1054 |             close: 191.45,
1055 |           },
1056 |           {
1057 |             time: "2019-05-22",
1058 |             open: 190.49,
1059 |             high: 192.22,
1060 |             low: 188.05,
1061 |             close: 188.91,
1062 |           },
1063 |           {
1064 |             time: "2019-05-23",
1065 |             open: 188.45,
1066 |             high: 192.54,
1067 |             low: 186.27,
1068 |             close: 192.0,
1069 |           },
1070 |           {
1071 |             time: "2019-05-24",
1072 |             open: 192.54,
1073 |             high: 193.86,
1074 |             low: 190.41,
1075 |             close: 193.59,
1076 |           },
1077 |         ];
1078 |       }
1079 | 
1080 |       // Create the Lightweight Chart within the container element
1081 |       const chart = LightweightCharts.createChart(
1082 |         document.getElementById('container'),
1083 |         {
1084 |           layout: {
1085 |             background: { color: "#222" },
1086 |             textColor: "#C3BCDB",
1087 |           },
1088 |           grid: {
1089 |             vertLines: { color: "#444" },
1090 |             horzLines: { color: "#444" },
1091 |           },
1092 |         }
1093 |       );
1094 | 
1095 |       // Setting the border color for the vertical axis
1096 |       chart.priceScale().applyOptions({
1097 |         borderColor: "#71649C",
1098 |       });
1099 | 
1100 |       // Setting the border color for the horizontal axis
1101 |       chart.timeScale().applyOptions({
1102 |         borderColor: "#71649C",
1103 |       });
1104 | 
1105 |       // Generate sample data to use within a candlestick series
1106 |       const candleStickData = generateCandlestickData();
1107 | 
1108 |       // Create the Main Series (Candlesticks)
1109 |       const mainSeries = chart.addSeries(LightweightCharts.CandlestickSeries);
1110 |       // Set the data for the Main Series
1111 |       mainSeries.setData(candleStickData);
1112 | 
1113 |       // Adding a window resize event handler to resize the chart when
1114 |       // the window size changes.
1115 |       // Note: for more advanced examples (when the chart doesn't fill the entire window)
1116 |       // you may need to use ResizeObserver -> https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver
1117 |       window.addEventListener("resize", () => {
1118 |         chart.resize(window.innerWidth, window.innerHeight);
1119 |       });
1120 |     </script>
1121 |   </body>
1122 | </html>
1123 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/assets/step3.html:
--------------------------------------------------------------------------------
   1 | <!DOCTYPE html>
   2 | <html>
   3 |   <head>
   4 |     <meta charset="UTF-8" />
   5 |     <meta
   6 |       name="viewport"
   7 |       content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0"
   8 |     />
   9 |     <title>Lightweight Charts™ Customization Tutorial</title>
  10 |     <!-- Adding the standalone version of Lightweight charts -->
  11 |     <script
  12 |       type="text/javascript"
  13 |       src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"
  14 |     ></script>
  15 |     <style>
  16 |       body {
  17 |         padding: 0;
  18 |         margin: 0;
  19 |         /* Add a background color to match the chart */
  20 |         background-color: #222;
  21 |       }
  22 |     </style>
  23 |   </head>
  24 | 
  25 |   <body>
  26 |     <div
  27 |       id="container"
  28 |       style="position: absolute; width: 100%; height: 100%"
  29 |     ></div>
  30 |     <script type="text/javascript">
  31 |       // Function to generate a sample set of Candlestick datapoints
  32 |       function generateCandlestickData() {
  33 |         return [
  34 |           {
  35 |             time: "2018-10-19",
  36 |             open: 180.34,
  37 |             high: 180.99,
  38 |             low: 178.57,
  39 |             close: 179.85,
  40 |           },
  41 |           {
  42 |             time: "2018-10-22",
  43 |             open: 180.82,
  44 |             high: 181.4,
  45 |             low: 177.56,
  46 |             close: 178.75,
  47 |           },
  48 |           {
  49 |             time: "2018-10-23",
  50 |             open: 175.77,
  51 |             high: 179.49,
  52 |             low: 175.44,
  53 |             close: 178.53,
  54 |           },
  55 |           {
  56 |             time: "2018-10-24",
  57 |             open: 178.58,
  58 |             high: 182.37,
  59 |             low: 176.31,
  60 |             close: 176.97,
  61 |           },
  62 |           {
  63 |             time: "2018-10-25",
  64 |             open: 177.52,
  65 |             high: 180.5,
  66 |             low: 176.83,
  67 |             close: 179.07,
  68 |           },
  69 |           {
  70 |             time: "2018-10-26",
  71 |             open: 176.88,
  72 |             high: 177.34,
  73 |             low: 170.91,
  74 |             close: 172.23,
  75 |           },
  76 |           {
  77 |             time: "2018-10-29",
  78 |             open: 173.74,
  79 |             high: 175.99,
  80 |             low: 170.95,
  81 |             close: 173.2,
  82 |           },
  83 |           {
  84 |             time: "2018-10-30",
  85 |             open: 173.16,
  86 |             high: 176.43,
  87 |             low: 172.64,
  88 |             close: 176.24,
  89 |           },
  90 |           {
  91 |             time: "2018-10-31",
  92 |             open: 177.98,
  93 |             high: 178.85,
  94 |             low: 175.59,
  95 |             close: 175.88,
  96 |           },
  97 |           {
  98 |             time: "2018-11-01",
  99 |             open: 176.84,
 100 |             high: 180.86,
 101 |             low: 175.9,
 102 |             close: 180.46,
 103 |           },
 104 |           {
 105 |             time: "2018-11-02",
 106 |             open: 182.47,
 107 |             high: 183.01,
 108 |             low: 177.39,
 109 |             close: 179.93,
 110 |           },
 111 |           {
 112 |             time: "2018-11-05",
 113 |             open: 181.02,
 114 |             high: 182.41,
 115 |             low: 179.3,
 116 |             close: 182.19,
 117 |           },
 118 |           {
 119 |             time: "2018-11-06",
 120 |             open: 181.93,
 121 |             high: 182.65,
 122 |             low: 180.05,
 123 |             close: 182.01,
 124 |           },
 125 |           {
 126 |             time: "2018-11-07",
 127 |             open: 183.79,
 128 |             high: 187.68,
 129 |             low: 182.06,
 130 |             close: 187.23,
 131 |           },
 132 |           {
 133 |             time: "2018-11-08",
 134 |             open: 187.13,
 135 |             high: 188.69,
 136 |             low: 185.72,
 137 |             close: 188.0,
 138 |           },
 139 |           {
 140 |             time: "2018-11-09",
 141 |             open: 188.32,
 142 |             high: 188.48,
 143 |             low: 184.96,
 144 |             close: 185.99,
 145 |           },
 146 |           {
 147 |             time: "2018-11-12",
 148 |             open: 185.23,
 149 |             high: 186.95,
 150 |             low: 179.02,
 151 |             close: 179.43,
 152 |           },
 153 |           {
 154 |             time: "2018-11-13",
 155 |             open: 177.3,
 156 |             high: 181.62,
 157 |             low: 172.85,
 158 |             close: 179.0,
 159 |           },
 160 |           {
 161 |             time: "2018-11-14",
 162 |             open: 182.61,
 163 |             high: 182.9,
 164 |             low: 179.15,
 165 |             close: 179.9,
 166 |           },
 167 |           {
 168 |             time: "2018-11-15",
 169 |             open: 179.01,
 170 |             high: 179.67,
 171 |             low: 173.61,
 172 |             close: 177.36,
 173 |           },
 174 |           {
 175 |             time: "2018-11-16",
 176 |             open: 173.99,
 177 |             high: 177.6,
 178 |             low: 173.51,
 179 |             close: 177.02,
 180 |           },
 181 |           {
 182 |             time: "2018-11-19",
 183 |             open: 176.71,
 184 |             high: 178.88,
 185 |             low: 172.3,
 186 |             close: 173.59,
 187 |           },
 188 |           {
 189 |             time: "2018-11-20",
 190 |             open: 169.25,
 191 |             high: 172.0,
 192 |             low: 167.0,
 193 |             close: 169.05,
 194 |           },
 195 |           {
 196 |             time: "2018-11-21",
 197 |             open: 170.0,
 198 |             high: 170.93,
 199 |             low: 169.15,
 200 |             close: 169.3,
 201 |           },
 202 |           {
 203 |             time: "2018-11-23",
 204 |             open: 169.39,
 205 |             high: 170.33,
 206 |             low: 168.47,
 207 |             close: 168.85,
 208 |           },
 209 |           {
 210 |             time: "2018-11-26",
 211 |             open: 170.2,
 212 |             high: 172.39,
 213 |             low: 168.87,
 214 |             close: 169.82,
 215 |           },
 216 |           {
 217 |             time: "2018-11-27",
 218 |             open: 169.11,
 219 |             high: 173.38,
 220 |             low: 168.82,
 221 |             close: 173.22,
 222 |           },
 223 |           {
 224 |             time: "2018-11-28",
 225 |             open: 172.91,
 226 |             high: 177.65,
 227 |             low: 170.62,
 228 |             close: 177.43,
 229 |           },
 230 |           {
 231 |             time: "2018-11-29",
 232 |             open: 176.8,
 233 |             high: 177.27,
 234 |             low: 174.92,
 235 |             close: 175.66,
 236 |           },
 237 |           {
 238 |             time: "2018-11-30",
 239 |             open: 175.75,
 240 |             high: 180.37,
 241 |             low: 175.11,
 242 |             close: 180.32,
 243 |           },
 244 |           {
 245 |             time: "2018-12-03",
 246 |             open: 183.29,
 247 |             high: 183.5,
 248 |             low: 179.35,
 249 |             close: 181.74,
 250 |           },
 251 |           {
 252 |             time: "2018-12-04",
 253 |             open: 181.06,
 254 |             high: 182.23,
 255 |             low: 174.55,
 256 |             close: 175.3,
 257 |           },
 258 |           {
 259 |             time: "2018-12-06",
 260 |             open: 173.5,
 261 |             high: 176.04,
 262 |             low: 170.46,
 263 |             close: 175.96,
 264 |           },
 265 |           {
 266 |             time: "2018-12-07",
 267 |             open: 175.35,
 268 |             high: 178.36,
 269 |             low: 172.24,
 270 |             close: 172.79,
 271 |           },
 272 |           {
 273 |             time: "2018-12-10",
 274 |             open: 173.39,
 275 |             high: 173.99,
 276 |             low: 167.73,
 277 |             close: 171.69,
 278 |           },
 279 |           {
 280 |             time: "2018-12-11",
 281 |             open: 174.3,
 282 |             high: 175.6,
 283 |             low: 171.24,
 284 |             close: 172.21,
 285 |           },
 286 |           {
 287 |             time: "2018-12-12",
 288 |             open: 173.75,
 289 |             high: 176.87,
 290 |             low: 172.81,
 291 |             close: 174.21,
 292 |           },
 293 |           {
 294 |             time: "2018-12-13",
 295 |             open: 174.31,
 296 |             high: 174.91,
 297 |             low: 172.07,
 298 |             close: 173.87,
 299 |           },
 300 |           {
 301 |             time: "2018-12-14",
 302 |             open: 172.98,
 303 |             high: 175.14,
 304 |             low: 171.95,
 305 |             close: 172.29,
 306 |           },
 307 |           {
 308 |             time: "2018-12-17",
 309 |             open: 171.51,
 310 |             high: 171.99,
 311 |             low: 166.93,
 312 |             close: 167.97,
 313 |           },
 314 |           {
 315 |             time: "2018-12-18",
 316 |             open: 168.9,
 317 |             high: 171.95,
 318 |             low: 168.5,
 319 |             close: 170.04,
 320 |           },
 321 |           {
 322 |             time: "2018-12-19",
 323 |             open: 170.92,
 324 |             high: 174.95,
 325 |             low: 166.77,
 326 |             close: 167.56,
 327 |           },
 328 |           {
 329 |             time: "2018-12-20",
 330 |             open: 166.28,
 331 |             high: 167.31,
 332 |             low: 162.23,
 333 |             close: 164.16,
 334 |           },
 335 |           {
 336 |             time: "2018-12-21",
 337 |             open: 162.81,
 338 |             high: 167.96,
 339 |             low: 160.17,
 340 |             close: 160.48,
 341 |           },
 342 |           {
 343 |             time: "2018-12-24",
 344 |             open: 160.16,
 345 |             high: 161.4,
 346 |             low: 158.09,
 347 |             close: 158.14,
 348 |           },
 349 |           {
 350 |             time: "2018-12-26",
 351 |             open: 159.46,
 352 |             high: 168.28,
 353 |             low: 159.44,
 354 |             close: 168.28,
 355 |           },
 356 |           {
 357 |             time: "2018-12-27",
 358 |             open: 166.44,
 359 |             high: 170.46,
 360 |             low: 163.36,
 361 |             close: 170.32,
 362 |           },
 363 |           {
 364 |             time: "2018-12-28",
 365 |             open: 171.22,
 366 |             high: 173.12,
 367 |             low: 168.6,
 368 |             close: 170.22,
 369 |           },
 370 |           {
 371 |             time: "2018-12-31",
 372 |             open: 171.47,
 373 |             high: 173.24,
 374 |             low: 170.65,
 375 |             close: 171.82,
 376 |           },
 377 |           {
 378 |             time: "2019-01-02",
 379 |             open: 169.71,
 380 |             high: 173.18,
 381 |             low: 169.05,
 382 |             close: 172.41,
 383 |           },
 384 |           {
 385 |             time: "2019-01-03",
 386 |             open: 171.84,
 387 |             high: 171.84,
 388 |             low: 168.21,
 389 |             close: 168.61,
 390 |           },
 391 |           {
 392 |             time: "2019-01-04",
 393 |             open: 170.18,
 394 |             high: 174.74,
 395 |             low: 169.52,
 396 |             close: 173.62,
 397 |           },
 398 |           {
 399 |             time: "2019-01-07",
 400 |             open: 173.83,
 401 |             high: 178.18,
 402 |             low: 173.83,
 403 |             close: 177.04,
 404 |           },
 405 |           {
 406 |             time: "2019-01-08",
 407 |             open: 178.57,
 408 |             high: 179.59,
 409 |             low: 175.61,
 410 |             close: 177.89,
 411 |           },
 412 |           {
 413 |             time: "2019-01-09",
 414 |             open: 177.87,
 415 |             high: 181.27,
 416 |             low: 177.1,
 417 |             close: 179.73,
 418 |           },
 419 |           {
 420 |             time: "2019-01-10",
 421 |             open: 178.03,
 422 |             high: 179.24,
 423 |             low: 176.34,
 424 |             close: 179.06,
 425 |           },
 426 |           {
 427 |             time: "2019-01-11",
 428 |             open: 177.93,
 429 |             high: 180.26,
 430 |             low: 177.12,
 431 |             close: 179.41,
 432 |           },
 433 |           {
 434 |             time: "2019-01-14",
 435 |             open: 177.59,
 436 |             high: 179.23,
 437 |             low: 176.9,
 438 |             close: 178.81,
 439 |           },
 440 |           {
 441 |             time: "2019-01-15",
 442 |             open: 176.08,
 443 |             high: 177.82,
 444 |             low: 175.2,
 445 |             close: 176.47,
 446 |           },
 447 |           {
 448 |             time: "2019-01-16",
 449 |             open: 177.09,
 450 |             high: 177.93,
 451 |             low: 175.86,
 452 |             close: 177.04,
 453 |           },
 454 |           {
 455 |             time: "2019-01-17",
 456 |             open: 174.01,
 457 |             high: 175.46,
 458 |             low: 172.0,
 459 |             close: 174.87,
 460 |           },
 461 |           {
 462 |             time: "2019-01-18",
 463 |             open: 176.98,
 464 |             high: 180.04,
 465 |             low: 176.18,
 466 |             close: 179.58,
 467 |           },
 468 |           {
 469 |             time: "2019-01-22",
 470 |             open: 177.49,
 471 |             high: 178.6,
 472 |             low: 175.36,
 473 |             close: 177.11,
 474 |           },
 475 |           {
 476 |             time: "2019-01-23",
 477 |             open: 176.59,
 478 |             high: 178.06,
 479 |             low: 174.53,
 480 |             close: 176.89,
 481 |           },
 482 |           {
 483 |             time: "2019-01-24",
 484 |             open: 177.0,
 485 |             high: 177.53,
 486 |             low: 175.3,
 487 |             close: 177.29,
 488 |           },
 489 |           {
 490 |             time: "2019-01-25",
 491 |             open: 179.78,
 492 |             high: 180.87,
 493 |             low: 178.61,
 494 |             close: 180.4,
 495 |           },
 496 |           {
 497 |             time: "2019-01-28",
 498 |             open: 178.97,
 499 |             high: 179.99,
 500 |             low: 177.41,
 501 |             close: 179.83,
 502 |           },
 503 |           {
 504 |             time: "2019-01-29",
 505 |             open: 178.96,
 506 |             high: 180.15,
 507 |             low: 178.09,
 508 |             close: 179.69,
 509 |           },
 510 |           {
 511 |             time: "2019-01-30",
 512 |             open: 180.47,
 513 |             high: 184.2,
 514 |             low: 179.78,
 515 |             close: 182.18,
 516 |           },
 517 |           {
 518 |             time: "2019-01-31",
 519 |             open: 181.5,
 520 |             high: 184.67,
 521 |             low: 181.06,
 522 |             close: 183.53,
 523 |           },
 524 |           {
 525 |             time: "2019-02-01",
 526 |             open: 184.03,
 527 |             high: 185.15,
 528 |             low: 182.83,
 529 |             close: 184.37,
 530 |           },
 531 |           {
 532 |             time: "2019-02-04",
 533 |             open: 184.3,
 534 |             high: 186.43,
 535 |             low: 183.84,
 536 |             close: 186.43,
 537 |           },
 538 |           {
 539 |             time: "2019-02-05",
 540 |             open: 186.89,
 541 |             high: 186.99,
 542 |             low: 184.69,
 543 |             close: 186.39,
 544 |           },
 545 |           {
 546 |             time: "2019-02-06",
 547 |             open: 186.69,
 548 |             high: 186.69,
 549 |             low: 184.06,
 550 |             close: 184.72,
 551 |           },
 552 |           {
 553 |             time: "2019-02-07",
 554 |             open: 183.74,
 555 |             high: 184.92,
 556 |             low: 182.45,
 557 |             close: 184.07,
 558 |           },
 559 |           {
 560 |             time: "2019-02-08",
 561 |             open: 183.05,
 562 |             high: 184.58,
 563 |             low: 182.72,
 564 |             close: 184.54,
 565 |           },
 566 |           {
 567 |             time: "2019-02-11",
 568 |             open: 185.0,
 569 |             high: 185.42,
 570 |             low: 182.75,
 571 |             close: 182.92,
 572 |           },
 573 |           {
 574 |             time: "2019-02-12",
 575 |             open: 183.84,
 576 |             high: 186.4,
 577 |             low: 183.52,
 578 |             close: 185.52,
 579 |           },
 580 |           {
 581 |             time: "2019-02-13",
 582 |             open: 186.3,
 583 |             high: 188.68,
 584 |             low: 185.92,
 585 |             close: 188.41,
 586 |           },
 587 |           {
 588 |             time: "2019-02-14",
 589 |             open: 187.5,
 590 |             high: 188.93,
 591 |             low: 186.0,
 592 |             close: 187.71,
 593 |           },
 594 |           {
 595 |             time: "2019-02-15",
 596 |             open: 189.87,
 597 |             high: 192.62,
 598 |             low: 189.05,
 599 |             close: 192.39,
 600 |           },
 601 |           {
 602 |             time: "2019-02-19",
 603 |             open: 191.71,
 604 |             high: 193.19,
 605 |             low: 191.28,
 606 |             close: 192.33,
 607 |           },
 608 |           {
 609 |             time: "2019-02-20",
 610 |             open: 192.39,
 611 |             high: 192.4,
 612 |             low: 191.11,
 613 |             close: 191.85,
 614 |           },
 615 |           {
 616 |             time: "2019-02-21",
 617 |             open: 191.85,
 618 |             high: 192.37,
 619 |             low: 190.61,
 620 |             close: 191.82,
 621 |           },
 622 |           {
 623 |             time: "2019-02-22",
 624 |             open: 191.69,
 625 |             high: 192.54,
 626 |             low: 191.62,
 627 |             close: 192.39,
 628 |           },
 629 |           {
 630 |             time: "2019-02-25",
 631 |             open: 192.75,
 632 |             high: 193.42,
 633 |             low: 189.96,
 634 |             close: 189.98,
 635 |           },
 636 |           {
 637 |             time: "2019-02-26",
 638 |             open: 185.59,
 639 |             high: 188.47,
 640 |             low: 182.8,
 641 |             close: 188.3,
 642 |           },
 643 |           {
 644 |             time: "2019-02-27",
 645 |             open: 187.9,
 646 |             high: 188.5,
 647 |             low: 183.21,
 648 |             close: 183.67,
 649 |           },
 650 |           {
 651 |             time: "2019-02-28",
 652 |             open: 183.6,
 653 |             high: 185.19,
 654 |             low: 183.11,
 655 |             close: 185.14,
 656 |           },
 657 |           {
 658 |             time: "2019-03-01",
 659 |             open: 185.82,
 660 |             high: 186.56,
 661 |             low: 182.86,
 662 |             close: 185.17,
 663 |           },
 664 |           {
 665 |             time: "2019-03-04",
 666 |             open: 186.2,
 667 |             high: 186.24,
 668 |             low: 182.1,
 669 |             close: 183.81,
 670 |           },
 671 |           {
 672 |             time: "2019-03-05",
 673 |             open: 184.24,
 674 |             high: 185.12,
 675 |             low: 183.25,
 676 |             close: 184.0,
 677 |           },
 678 |           {
 679 |             time: "2019-03-06",
 680 |             open: 184.53,
 681 |             high: 184.97,
 682 |             low: 183.84,
 683 |             close: 184.45,
 684 |           },
 685 |           {
 686 |             time: "2019-03-07",
 687 |             open: 184.39,
 688 |             high: 184.62,
 689 |             low: 181.58,
 690 |             close: 182.51,
 691 |           },
 692 |           {
 693 |             time: "2019-03-08",
 694 |             open: 181.49,
 695 |             high: 181.91,
 696 |             low: 179.52,
 697 |             close: 181.23,
 698 |           },
 699 |           {
 700 |             time: "2019-03-11",
 701 |             open: 182.0,
 702 |             high: 183.2,
 703 |             low: 181.2,
 704 |             close: 182.44,
 705 |           },
 706 |           {
 707 |             time: "2019-03-12",
 708 |             open: 183.43,
 709 |             high: 184.27,
 710 |             low: 182.33,
 711 |             close: 184.0,
 712 |           },
 713 |           {
 714 |             time: "2019-03-13",
 715 |             open: 183.24,
 716 |             high: 183.78,
 717 |             low: 181.08,
 718 |             close: 181.14,
 719 |           },
 720 |           {
 721 |             time: "2019-03-14",
 722 |             open: 181.28,
 723 |             high: 181.74,
 724 |             low: 180.5,
 725 |             close: 181.61,
 726 |           },
 727 |           {
 728 |             time: "2019-03-15",
 729 |             open: 182.3,
 730 |             high: 182.49,
 731 |             low: 179.57,
 732 |             close: 182.23,
 733 |           },
 734 |           {
 735 |             time: "2019-03-18",
 736 |             open: 182.53,
 737 |             high: 183.48,
 738 |             low: 182.33,
 739 |             close: 183.42,
 740 |           },
 741 |           {
 742 |             time: "2019-03-19",
 743 |             open: 184.19,
 744 |             high: 185.82,
 745 |             low: 183.48,
 746 |             close: 184.13,
 747 |           },
 748 |           {
 749 |             time: "2019-03-20",
 750 |             open: 184.3,
 751 |             high: 187.12,
 752 |             low: 183.43,
 753 |             close: 186.1,
 754 |           },
 755 |           {
 756 |             time: "2019-03-21",
 757 |             open: 185.5,
 758 |             high: 190.0,
 759 |             low: 185.5,
 760 |             close: 189.97,
 761 |           },
 762 |           {
 763 |             time: "2019-03-22",
 764 |             open: 189.31,
 765 |             high: 192.05,
 766 |             low: 188.67,
 767 |             close: 188.75,
 768 |           },
 769 |           {
 770 |             time: "2019-03-25",
 771 |             open: 188.75,
 772 |             high: 191.71,
 773 |             low: 188.51,
 774 |             close: 189.68,
 775 |           },
 776 |           {
 777 |             time: "2019-03-26",
 778 |             open: 190.69,
 779 |             high: 192.19,
 780 |             low: 188.74,
 781 |             close: 189.34,
 782 |           },
 783 |           {
 784 |             time: "2019-03-27",
 785 |             open: 189.65,
 786 |             high: 191.61,
 787 |             low: 188.39,
 788 |             close: 189.25,
 789 |           },
 790 |           {
 791 |             time: "2019-03-28",
 792 |             open: 189.91,
 793 |             high: 191.4,
 794 |             low: 189.16,
 795 |             close: 190.06,
 796 |           },
 797 |           {
 798 |             time: "2019-03-29",
 799 |             open: 190.85,
 800 |             high: 192.04,
 801 |             low: 190.14,
 802 |             close: 191.89,
 803 |           },
 804 |           {
 805 |             time: "2019-04-01",
 806 |             open: 192.99,
 807 |             high: 195.9,
 808 |             low: 192.85,
 809 |             close: 195.64,
 810 |           },
 811 |           {
 812 |             time: "2019-04-02",
 813 |             open: 195.5,
 814 |             high: 195.5,
 815 |             low: 194.01,
 816 |             close: 194.31,
 817 |           },
 818 |           {
 819 |             time: "2019-04-03",
 820 |             open: 194.98,
 821 |             high: 198.78,
 822 |             low: 194.11,
 823 |             close: 198.61,
 824 |           },
 825 |           {
 826 |             time: "2019-04-04",
 827 |             open: 199.0,
 828 |             high: 200.49,
 829 |             low: 198.02,
 830 |             close: 200.45,
 831 |           },
 832 |           {
 833 |             time: "2019-04-05",
 834 |             open: 200.86,
 835 |             high: 203.13,
 836 |             low: 200.61,
 837 |             close: 202.06,
 838 |           },
 839 |           {
 840 |             time: "2019-04-08",
 841 |             open: 201.37,
 842 |             high: 203.79,
 843 |             low: 201.24,
 844 |             close: 203.55,
 845 |           },
 846 |           {
 847 |             time: "2019-04-09",
 848 |             open: 202.26,
 849 |             high: 202.71,
 850 |             low: 200.46,
 851 |             close: 200.9,
 852 |           },
 853 |           {
 854 |             time: "2019-04-10",
 855 |             open: 201.26,
 856 |             high: 201.6,
 857 |             low: 198.02,
 858 |             close: 199.43,
 859 |           },
 860 |           {
 861 |             time: "2019-04-11",
 862 |             open: 199.9,
 863 |             high: 201.5,
 864 |             low: 199.03,
 865 |             close: 201.48,
 866 |           },
 867 |           {
 868 |             time: "2019-04-12",
 869 |             open: 202.13,
 870 |             high: 204.26,
 871 |             low: 202.13,
 872 |             close: 203.85,
 873 |           },
 874 |           {
 875 |             time: "2019-04-15",
 876 |             open: 204.16,
 877 |             high: 205.14,
 878 |             low: 203.4,
 879 |             close: 204.86,
 880 |           },
 881 |           {
 882 |             time: "2019-04-16",
 883 |             open: 205.25,
 884 |             high: 205.99,
 885 |             low: 204.29,
 886 |             close: 204.47,
 887 |           },
 888 |           {
 889 |             time: "2019-04-17",
 890 |             open: 205.34,
 891 |             high: 206.84,
 892 |             low: 205.32,
 893 |             close: 206.55,
 894 |           },
 895 |           {
 896 |             time: "2019-04-18",
 897 |             open: 206.02,
 898 |             high: 207.78,
 899 |             low: 205.1,
 900 |             close: 205.66,
 901 |           },
 902 |           {
 903 |             time: "2019-04-22",
 904 |             open: 204.11,
 905 |             high: 206.25,
 906 |             low: 204.0,
 907 |             close: 204.78,
 908 |           },
 909 |           {
 910 |             time: "2019-04-23",
 911 |             open: 205.14,
 912 |             high: 207.33,
 913 |             low: 203.43,
 914 |             close: 206.05,
 915 |           },
 916 |           {
 917 |             time: "2019-04-24",
 918 |             open: 206.16,
 919 |             high: 208.29,
 920 |             low: 205.54,
 921 |             close: 206.72,
 922 |           },
 923 |           {
 924 |             time: "2019-04-25",
 925 |             open: 206.01,
 926 |             high: 207.72,
 927 |             low: 205.06,
 928 |             close: 206.5,
 929 |           },
 930 |           {
 931 |             time: "2019-04-26",
 932 |             open: 205.88,
 933 |             high: 206.14,
 934 |             low: 203.34,
 935 |             close: 203.61,
 936 |           },
 937 |           {
 938 |             time: "2019-04-29",
 939 |             open: 203.31,
 940 |             high: 203.8,
 941 |             low: 200.34,
 942 |             close: 202.16,
 943 |           },
 944 |           {
 945 |             time: "2019-04-30",
 946 |             open: 201.55,
 947 |             high: 203.75,
 948 |             low: 200.79,
 949 |             close: 203.7,
 950 |           },
 951 |           {
 952 |             time: "2019-05-01",
 953 |             open: 203.2,
 954 |             high: 203.52,
 955 |             low: 198.66,
 956 |             close: 198.8,
 957 |           },
 958 |           {
 959 |             time: "2019-05-02",
 960 |             open: 199.3,
 961 |             high: 201.06,
 962 |             low: 198.8,
 963 |             close: 201.01,
 964 |           },
 965 |           {
 966 |             time: "2019-05-03",
 967 |             open: 202.0,
 968 |             high: 202.31,
 969 |             low: 200.32,
 970 |             close: 200.56,
 971 |           },
 972 |           {
 973 |             time: "2019-05-06",
 974 |             open: 198.74,
 975 |             high: 199.93,
 976 |             low: 198.31,
 977 |             close: 199.63,
 978 |           },
 979 |           {
 980 |             time: "2019-05-07",
 981 |             open: 196.75,
 982 |             high: 197.65,
 983 |             low: 192.96,
 984 |             close: 194.77,
 985 |           },
 986 |           {
 987 |             time: "2019-05-08",
 988 |             open: 194.49,
 989 |             high: 196.61,
 990 |             low: 193.68,
 991 |             close: 195.17,
 992 |           },
 993 |           {
 994 |             time: "2019-05-09",
 995 |             open: 193.31,
 996 |             high: 195.08,
 997 |             low: 191.59,
 998 |             close: 194.58,
 999 |           },
1000 |           {
1001 |             time: "2019-05-10",
1002 |             open: 193.21,
1003 |             high: 195.49,
1004 |             low: 190.01,
1005 |             close: 194.58,
1006 |           },
1007 |           {
1008 |             time: "2019-05-13",
1009 |             open: 191.0,
1010 |             high: 191.66,
1011 |             low: 189.14,
1012 |             close: 190.34,
1013 |           },
1014 |           {
1015 |             time: "2019-05-14",
1016 |             open: 190.5,
1017 |             high: 192.76,
1018 |             low: 190.01,
1019 |             close: 191.62,
1020 |           },
1021 |           {
1022 |             time: "2019-05-15",
1023 |             open: 190.81,
1024 |             high: 192.81,
1025 |             low: 190.27,
1026 |             close: 191.76,
1027 |           },
1028 |           {
1029 |             time: "2019-05-16",
1030 |             open: 192.47,
1031 |             high: 194.96,
1032 |             low: 192.2,
1033 |             close: 192.38,
1034 |           },
1035 |           {
1036 |             time: "2019-05-17",
1037 |             open: 190.86,
1038 |             high: 194.5,
1039 |             low: 190.75,
1040 |             close: 192.58,
1041 |           },
1042 |           {
1043 |             time: "2019-05-20",
1044 |             open: 191.13,
1045 |             high: 192.86,
1046 |             low: 190.61,
1047 |             close: 190.95,
1048 |           },
1049 |           {
1050 |             time: "2019-05-21",
1051 |             open: 187.13,
1052 |             high: 192.52,
1053 |             low: 186.34,
1054 |             close: 191.45,
1055 |           },
1056 |           {
1057 |             time: "2019-05-22",
1058 |             open: 190.49,
1059 |             high: 192.22,
1060 |             low: 188.05,
1061 |             close: 188.91,
1062 |           },
1063 |           {
1064 |             time: "2019-05-23",
1065 |             open: 188.45,
1066 |             high: 192.54,
1067 |             low: 186.27,
1068 |             close: 192.0,
1069 |           },
1070 |           {
1071 |             time: "2019-05-24",
1072 |             open: 192.54,
1073 |             high: 193.86,
1074 |             low: 190.41,
1075 |             close: 193.59,
1076 |           },
1077 |         ];
1078 |       }
1079 | 
1080 |       // Create the Lightweight Chart within the container element
1081 |       const chart = LightweightCharts.createChart(
1082 |         document.getElementById('container'),
1083 |         {
1084 |           layout: {
1085 |             background: { color: "#222" },
1086 |             textColor: "#DDD",
1087 |           },
1088 |           grid: {
1089 |             vertLines: { color: "#444" },
1090 |             horzLines: { color: "#444" },
1091 |           },
1092 |         }
1093 |       );
1094 | 
1095 |       // Setting the border color for the vertical axis
1096 |       chart.priceScale().applyOptions({
1097 |         borderColor: "#71649C",
1098 |       });
1099 | 
1100 |       // Setting the border color for the horizontal axis
1101 |       chart.timeScale().applyOptions({
1102 |         borderColor: "#71649C",
1103 |       });
1104 | 
1105 |       // Generate sample data to use within a candlestick series
1106 |       const candleStickData = generateCandlestickData();
1107 | 
1108 |       // Create the Main Series (Candlesticks)
1109 |       const mainSeries = chart.addSeries(LightweightCharts.CandlestickSeries);
1110 |       // Set the data for the Main Series
1111 |       mainSeries.setData(candleStickData);
1112 | 
1113 |       // Changing the Candlestick colors
1114 |       mainSeries.applyOptions({
1115 |         wickUpColor: "rgb(54, 116, 217)",
1116 |         upColor: "rgb(54, 116, 217)",
1117 |         wickDownColor: "rgb(225, 50, 85)",
1118 |         downColor: "rgb(225, 50, 85)",
1119 |         borderVisible: false,
1120 |       });
1121 | 
1122 |       // Adding a window resize event handler to resize the chart when
1123 |       // the window size changes.
1124 |       // Note: for more advanced examples (when the chart doesn't fill the entire window)
1125 |       // you may need to use ResizeObserver -> https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver
1126 |       window.addEventListener("resize", () => {
1127 |         chart.resize(window.innerWidth, window.innerHeight);
1128 |       });
1129 |     </script>
1130 |   </body>
1131 | </html>
1132 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/assets/step4.html:
--------------------------------------------------------------------------------
   1 | <!DOCTYPE html>
   2 | <html>
   3 |   <head>
   4 |     <meta charset="UTF-8" />
   5 |     <meta
   6 |       name="viewport"
   7 |       content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0"
   8 |     />
   9 |     <title>Lightweight Charts™ Customization Tutorial</title>
  10 |     <!-- Adding the standalone version of Lightweight charts -->
  11 |     <script
  12 |       type="text/javascript"
  13 |       src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"
  14 |     ></script>
  15 |     <style>
  16 |       body {
  17 |         padding: 0;
  18 |         margin: 0;
  19 |         /* Add a background color to match the chart */
  20 |         background-color: #222;
  21 |       }
  22 |     </style>
  23 |   </head>
  24 | 
  25 |   <body>
  26 |     <div
  27 |       id="container"
  28 |       style="position: absolute; width: 100%; height: 100%"
  29 |     ></div>
  30 |     <script type="text/javascript">
  31 |       // Function to generate a sample set of Candlestick datapoints
  32 |       function generateCandlestickData() {
  33 |         return [
  34 |           {
  35 |             time: "2018-10-19",
  36 |             open: 180.34,
  37 |             high: 180.99,
  38 |             low: 178.57,
  39 |             close: 179.85,
  40 |           },
  41 |           {
  42 |             time: "2018-10-22",
  43 |             open: 180.82,
  44 |             high: 181.4,
  45 |             low: 177.56,
  46 |             close: 178.75,
  47 |           },
  48 |           {
  49 |             time: "2018-10-23",
  50 |             open: 175.77,
  51 |             high: 179.49,
  52 |             low: 175.44,
  53 |             close: 178.53,
  54 |           },
  55 |           {
  56 |             time: "2018-10-24",
  57 |             open: 178.58,
  58 |             high: 182.37,
  59 |             low: 176.31,
  60 |             close: 176.97,
  61 |           },
  62 |           {
  63 |             time: "2018-10-25",
  64 |             open: 177.52,
  65 |             high: 180.5,
  66 |             low: 176.83,
  67 |             close: 179.07,
  68 |           },
  69 |           {
  70 |             time: "2018-10-26",
  71 |             open: 176.88,
  72 |             high: 177.34,
  73 |             low: 170.91,
  74 |             close: 172.23,
  75 |           },
  76 |           {
  77 |             time: "2018-10-29",
  78 |             open: 173.74,
  79 |             high: 175.99,
  80 |             low: 170.95,
  81 |             close: 173.2,
  82 |           },
  83 |           {
  84 |             time: "2018-10-30",
  85 |             open: 173.16,
  86 |             high: 176.43,
  87 |             low: 172.64,
  88 |             close: 176.24,
  89 |           },
  90 |           {
  91 |             time: "2018-10-31",
  92 |             open: 177.98,
  93 |             high: 178.85,
  94 |             low: 175.59,
  95 |             close: 175.88,
  96 |           },
  97 |           {
  98 |             time: "2018-11-01",
  99 |             open: 176.84,
 100 |             high: 180.86,
 101 |             low: 175.9,
 102 |             close: 180.46,
 103 |           },
 104 |           {
 105 |             time: "2018-11-02",
 106 |             open: 182.47,
 107 |             high: 183.01,
 108 |             low: 177.39,
 109 |             close: 179.93,
 110 |           },
 111 |           {
 112 |             time: "2018-11-05",
 113 |             open: 181.02,
 114 |             high: 182.41,
 115 |             low: 179.3,
 116 |             close: 182.19,
 117 |           },
 118 |           {
 119 |             time: "2018-11-06",
 120 |             open: 181.93,
 121 |             high: 182.65,
 122 |             low: 180.05,
 123 |             close: 182.01,
 124 |           },
 125 |           {
 126 |             time: "2018-11-07",
 127 |             open: 183.79,
 128 |             high: 187.68,
 129 |             low: 182.06,
 130 |             close: 187.23,
 131 |           },
 132 |           {
 133 |             time: "2018-11-08",
 134 |             open: 187.13,
 135 |             high: 188.69,
 136 |             low: 185.72,
 137 |             close: 188.0,
 138 |           },
 139 |           {
 140 |             time: "2018-11-09",
 141 |             open: 188.32,
 142 |             high: 188.48,
 143 |             low: 184.96,
 144 |             close: 185.99,
 145 |           },
 146 |           {
 147 |             time: "2018-11-12",
 148 |             open: 185.23,
 149 |             high: 186.95,
 150 |             low: 179.02,
 151 |             close: 179.43,
 152 |           },
 153 |           {
 154 |             time: "2018-11-13",
 155 |             open: 177.3,
 156 |             high: 181.62,
 157 |             low: 172.85,
 158 |             close: 179.0,
 159 |           },
 160 |           {
 161 |             time: "2018-11-14",
 162 |             open: 182.61,
 163 |             high: 182.9,
 164 |             low: 179.15,
 165 |             close: 179.9,
 166 |           },
 167 |           {
 168 |             time: "2018-11-15",
 169 |             open: 179.01,
 170 |             high: 179.67,
 171 |             low: 173.61,
 172 |             close: 177.36,
 173 |           },
 174 |           {
 175 |             time: "2018-11-16",
 176 |             open: 173.99,
 177 |             high: 177.6,
 178 |             low: 173.51,
 179 |             close: 177.02,
 180 |           },
 181 |           {
 182 |             time: "2018-11-19",
 183 |             open: 176.71,
 184 |             high: 178.88,
 185 |             low: 172.3,
 186 |             close: 173.59,
 187 |           },
 188 |           {
 189 |             time: "2018-11-20",
 190 |             open: 169.25,
 191 |             high: 172.0,
 192 |             low: 167.0,
 193 |             close: 169.05,
 194 |           },
 195 |           {
 196 |             time: "2018-11-21",
 197 |             open: 170.0,
 198 |             high: 170.93,
 199 |             low: 169.15,
 200 |             close: 169.3,
 201 |           },
 202 |           {
 203 |             time: "2018-11-23",
 204 |             open: 169.39,
 205 |             high: 170.33,
 206 |             low: 168.47,
 207 |             close: 168.85,
 208 |           },
 209 |           {
 210 |             time: "2018-11-26",
 211 |             open: 170.2,
 212 |             high: 172.39,
 213 |             low: 168.87,
 214 |             close: 169.82,
 215 |           },
 216 |           {
 217 |             time: "2018-11-27",
 218 |             open: 169.11,
 219 |             high: 173.38,
 220 |             low: 168.82,
 221 |             close: 173.22,
 222 |           },
 223 |           {
 224 |             time: "2018-11-28",
 225 |             open: 172.91,
 226 |             high: 177.65,
 227 |             low: 170.62,
 228 |             close: 177.43,
 229 |           },
 230 |           {
 231 |             time: "2018-11-29",
 232 |             open: 176.8,
 233 |             high: 177.27,
 234 |             low: 174.92,
 235 |             close: 175.66,
 236 |           },
 237 |           {
 238 |             time: "2018-11-30",
 239 |             open: 175.75,
 240 |             high: 180.37,
 241 |             low: 175.11,
 242 |             close: 180.32,
 243 |           },
 244 |           {
 245 |             time: "2018-12-03",
 246 |             open: 183.29,
 247 |             high: 183.5,
 248 |             low: 179.35,
 249 |             close: 181.74,
 250 |           },
 251 |           {
 252 |             time: "2018-12-04",
 253 |             open: 181.06,
 254 |             high: 182.23,
 255 |             low: 174.55,
 256 |             close: 175.3,
 257 |           },
 258 |           {
 259 |             time: "2018-12-06",
 260 |             open: 173.5,
 261 |             high: 176.04,
 262 |             low: 170.46,
 263 |             close: 175.96,
 264 |           },
 265 |           {
 266 |             time: "2018-12-07",
 267 |             open: 175.35,
 268 |             high: 178.36,
 269 |             low: 172.24,
 270 |             close: 172.79,
 271 |           },
 272 |           {
 273 |             time: "2018-12-10",
 274 |             open: 173.39,
 275 |             high: 173.99,
 276 |             low: 167.73,
 277 |             close: 171.69,
 278 |           },
 279 |           {
 280 |             time: "2018-12-11",
 281 |             open: 174.3,
 282 |             high: 175.6,
 283 |             low: 171.24,
 284 |             close: 172.21,
 285 |           },
 286 |           {
 287 |             time: "2018-12-12",
 288 |             open: 173.75,
 289 |             high: 176.87,
 290 |             low: 172.81,
 291 |             close: 174.21,
 292 |           },
 293 |           {
 294 |             time: "2018-12-13",
 295 |             open: 174.31,
 296 |             high: 174.91,
 297 |             low: 172.07,
 298 |             close: 173.87,
 299 |           },
 300 |           {
 301 |             time: "2018-12-14",
 302 |             open: 172.98,
 303 |             high: 175.14,
 304 |             low: 171.95,
 305 |             close: 172.29,
 306 |           },
 307 |           {
 308 |             time: "2018-12-17",
 309 |             open: 171.51,
 310 |             high: 171.99,
 311 |             low: 166.93,
 312 |             close: 167.97,
 313 |           },
 314 |           {
 315 |             time: "2018-12-18",
 316 |             open: 168.9,
 317 |             high: 171.95,
 318 |             low: 168.5,
 319 |             close: 170.04,
 320 |           },
 321 |           {
 322 |             time: "2018-12-19",
 323 |             open: 170.92,
 324 |             high: 174.95,
 325 |             low: 166.77,
 326 |             close: 167.56,
 327 |           },
 328 |           {
 329 |             time: "2018-12-20",
 330 |             open: 166.28,
 331 |             high: 167.31,
 332 |             low: 162.23,
 333 |             close: 164.16,
 334 |           },
 335 |           {
 336 |             time: "2018-12-21",
 337 |             open: 162.81,
 338 |             high: 167.96,
 339 |             low: 160.17,
 340 |             close: 160.48,
 341 |           },
 342 |           {
 343 |             time: "2018-12-24",
 344 |             open: 160.16,
 345 |             high: 161.4,
 346 |             low: 158.09,
 347 |             close: 158.14,
 348 |           },
 349 |           {
 350 |             time: "2018-12-26",
 351 |             open: 159.46,
 352 |             high: 168.28,
 353 |             low: 159.44,
 354 |             close: 168.28,
 355 |           },
 356 |           {
 357 |             time: "2018-12-27",
 358 |             open: 166.44,
 359 |             high: 170.46,
 360 |             low: 163.36,
 361 |             close: 170.32,
 362 |           },
 363 |           {
 364 |             time: "2018-12-28",
 365 |             open: 171.22,
 366 |             high: 173.12,
 367 |             low: 168.6,
 368 |             close: 170.22,
 369 |           },
 370 |           {
 371 |             time: "2018-12-31",
 372 |             open: 171.47,
 373 |             high: 173.24,
 374 |             low: 170.65,
 375 |             close: 171.82,
 376 |           },
 377 |           {
 378 |             time: "2019-01-02",
 379 |             open: 169.71,
 380 |             high: 173.18,
 381 |             low: 169.05,
 382 |             close: 172.41,
 383 |           },
 384 |           {
 385 |             time: "2019-01-03",
 386 |             open: 171.84,
 387 |             high: 171.84,
 388 |             low: 168.21,
 389 |             close: 168.61,
 390 |           },
 391 |           {
 392 |             time: "2019-01-04",
 393 |             open: 170.18,
 394 |             high: 174.74,
 395 |             low: 169.52,
 396 |             close: 173.62,
 397 |           },
 398 |           {
 399 |             time: "2019-01-07",
 400 |             open: 173.83,
 401 |             high: 178.18,
 402 |             low: 173.83,
 403 |             close: 177.04,
 404 |           },
 405 |           {
 406 |             time: "2019-01-08",
 407 |             open: 178.57,
 408 |             high: 179.59,
 409 |             low: 175.61,
 410 |             close: 177.89,
 411 |           },
 412 |           {
 413 |             time: "2019-01-09",
 414 |             open: 177.87,
 415 |             high: 181.27,
 416 |             low: 177.1,
 417 |             close: 179.73,
 418 |           },
 419 |           {
 420 |             time: "2019-01-10",
 421 |             open: 178.03,
 422 |             high: 179.24,
 423 |             low: 176.34,
 424 |             close: 179.06,
 425 |           },
 426 |           {
 427 |             time: "2019-01-11",
 428 |             open: 177.93,
 429 |             high: 180.26,
 430 |             low: 177.12,
 431 |             close: 179.41,
 432 |           },
 433 |           {
 434 |             time: "2019-01-14",
 435 |             open: 177.59,
 436 |             high: 179.23,
 437 |             low: 176.9,
 438 |             close: 178.81,
 439 |           },
 440 |           {
 441 |             time: "2019-01-15",
 442 |             open: 176.08,
 443 |             high: 177.82,
 444 |             low: 175.2,
 445 |             close: 176.47,
 446 |           },
 447 |           {
 448 |             time: "2019-01-16",
 449 |             open: 177.09,
 450 |             high: 177.93,
 451 |             low: 175.86,
 452 |             close: 177.04,
 453 |           },
 454 |           {
 455 |             time: "2019-01-17",
 456 |             open: 174.01,
 457 |             high: 175.46,
 458 |             low: 172.0,
 459 |             close: 174.87,
 460 |           },
 461 |           {
 462 |             time: "2019-01-18",
 463 |             open: 176.98,
 464 |             high: 180.04,
 465 |             low: 176.18,
 466 |             close: 179.58,
 467 |           },
 468 |           {
 469 |             time: "2019-01-22",
 470 |             open: 177.49,
 471 |             high: 178.6,
 472 |             low: 175.36,
 473 |             close: 177.11,
 474 |           },
 475 |           {
 476 |             time: "2019-01-23",
 477 |             open: 176.59,
 478 |             high: 178.06,
 479 |             low: 174.53,
 480 |             close: 176.89,
 481 |           },
 482 |           {
 483 |             time: "2019-01-24",
 484 |             open: 177.0,
 485 |             high: 177.53,
 486 |             low: 175.3,
 487 |             close: 177.29,
 488 |           },
 489 |           {
 490 |             time: "2019-01-25",
 491 |             open: 179.78,
 492 |             high: 180.87,
 493 |             low: 178.61,
 494 |             close: 180.4,
 495 |           },
 496 |           {
 497 |             time: "2019-01-28",
 498 |             open: 178.97,
 499 |             high: 179.99,
 500 |             low: 177.41,
 501 |             close: 179.83,
 502 |           },
 503 |           {
 504 |             time: "2019-01-29",
 505 |             open: 178.96,
 506 |             high: 180.15,
 507 |             low: 178.09,
 508 |             close: 179.69,
 509 |           },
 510 |           {
 511 |             time: "2019-01-30",
 512 |             open: 180.47,
 513 |             high: 184.2,
 514 |             low: 179.78,
 515 |             close: 182.18,
 516 |           },
 517 |           {
 518 |             time: "2019-01-31",
 519 |             open: 181.5,
 520 |             high: 184.67,
 521 |             low: 181.06,
 522 |             close: 183.53,
 523 |           },
 524 |           {
 525 |             time: "2019-02-01",
 526 |             open: 184.03,
 527 |             high: 185.15,
 528 |             low: 182.83,
 529 |             close: 184.37,
 530 |           },
 531 |           {
 532 |             time: "2019-02-04",
 533 |             open: 184.3,
 534 |             high: 186.43,
 535 |             low: 183.84,
 536 |             close: 186.43,
 537 |           },
 538 |           {
 539 |             time: "2019-02-05",
 540 |             open: 186.89,
 541 |             high: 186.99,
 542 |             low: 184.69,
 543 |             close: 186.39,
 544 |           },
 545 |           {
 546 |             time: "2019-02-06",
 547 |             open: 186.69,
 548 |             high: 186.69,
 549 |             low: 184.06,
 550 |             close: 184.72,
 551 |           },
 552 |           {
 553 |             time: "2019-02-07",
 554 |             open: 183.74,
 555 |             high: 184.92,
 556 |             low: 182.45,
 557 |             close: 184.07,
 558 |           },
 559 |           {
 560 |             time: "2019-02-08",
 561 |             open: 183.05,
 562 |             high: 184.58,
 563 |             low: 182.72,
 564 |             close: 184.54,
 565 |           },
 566 |           {
 567 |             time: "2019-02-11",
 568 |             open: 185.0,
 569 |             high: 185.42,
 570 |             low: 182.75,
 571 |             close: 182.92,
 572 |           },
 573 |           {
 574 |             time: "2019-02-12",
 575 |             open: 183.84,
 576 |             high: 186.4,
 577 |             low: 183.52,
 578 |             close: 185.52,
 579 |           },
 580 |           {
 581 |             time: "2019-02-13",
 582 |             open: 186.3,
 583 |             high: 188.68,
 584 |             low: 185.92,
 585 |             close: 188.41,
 586 |           },
 587 |           {
 588 |             time: "2019-02-14",
 589 |             open: 187.5,
 590 |             high: 188.93,
 591 |             low: 186.0,
 592 |             close: 187.71,
 593 |           },
 594 |           {
 595 |             time: "2019-02-15",
 596 |             open: 189.87,
 597 |             high: 192.62,
 598 |             low: 189.05,
 599 |             close: 192.39,
 600 |           },
 601 |           {
 602 |             time: "2019-02-19",
 603 |             open: 191.71,
 604 |             high: 193.19,
 605 |             low: 191.28,
 606 |             close: 192.33,
 607 |           },
 608 |           {
 609 |             time: "2019-02-20",
 610 |             open: 192.39,
 611 |             high: 192.4,
 612 |             low: 191.11,
 613 |             close: 191.85,
 614 |           },
 615 |           {
 616 |             time: "2019-02-21",
 617 |             open: 191.85,
 618 |             high: 192.37,
 619 |             low: 190.61,
 620 |             close: 191.82,
 621 |           },
 622 |           {
 623 |             time: "2019-02-22",
 624 |             open: 191.69,
 625 |             high: 192.54,
 626 |             low: 191.62,
 627 |             close: 192.39,
 628 |           },
 629 |           {
 630 |             time: "2019-02-25",
 631 |             open: 192.75,
 632 |             high: 193.42,
 633 |             low: 189.96,
 634 |             close: 189.98,
 635 |           },
 636 |           {
 637 |             time: "2019-02-26",
 638 |             open: 185.59,
 639 |             high: 188.47,
 640 |             low: 182.8,
 641 |             close: 188.3,
 642 |           },
 643 |           {
 644 |             time: "2019-02-27",
 645 |             open: 187.9,
 646 |             high: 188.5,
 647 |             low: 183.21,
 648 |             close: 183.67,
 649 |           },
 650 |           {
 651 |             time: "2019-02-28",
 652 |             open: 183.6,
 653 |             high: 185.19,
 654 |             low: 183.11,
 655 |             close: 185.14,
 656 |           },
 657 |           {
 658 |             time: "2019-03-01",
 659 |             open: 185.82,
 660 |             high: 186.56,
 661 |             low: 182.86,
 662 |             close: 185.17,
 663 |           },
 664 |           {
 665 |             time: "2019-03-04",
 666 |             open: 186.2,
 667 |             high: 186.24,
 668 |             low: 182.1,
 669 |             close: 183.81,
 670 |           },
 671 |           {
 672 |             time: "2019-03-05",
 673 |             open: 184.24,
 674 |             high: 185.12,
 675 |             low: 183.25,
 676 |             close: 184.0,
 677 |           },
 678 |           {
 679 |             time: "2019-03-06",
 680 |             open: 184.53,
 681 |             high: 184.97,
 682 |             low: 183.84,
 683 |             close: 184.45,
 684 |           },
 685 |           {
 686 |             time: "2019-03-07",
 687 |             open: 184.39,
 688 |             high: 184.62,
 689 |             low: 181.58,
 690 |             close: 182.51,
 691 |           },
 692 |           {
 693 |             time: "2019-03-08",
 694 |             open: 181.49,
 695 |             high: 181.91,
 696 |             low: 179.52,
 697 |             close: 181.23,
 698 |           },
 699 |           {
 700 |             time: "2019-03-11",
 701 |             open: 182.0,
 702 |             high: 183.2,
 703 |             low: 181.2,
 704 |             close: 182.44,
 705 |           },
 706 |           {
 707 |             time: "2019-03-12",
 708 |             open: 183.43,
 709 |             high: 184.27,
 710 |             low: 182.33,
 711 |             close: 184.0,
 712 |           },
 713 |           {
 714 |             time: "2019-03-13",
 715 |             open: 183.24,
 716 |             high: 183.78,
 717 |             low: 181.08,
 718 |             close: 181.14,
 719 |           },
 720 |           {
 721 |             time: "2019-03-14",
 722 |             open: 181.28,
 723 |             high: 181.74,
 724 |             low: 180.5,
 725 |             close: 181.61,
 726 |           },
 727 |           {
 728 |             time: "2019-03-15",
 729 |             open: 182.3,
 730 |             high: 182.49,
 731 |             low: 179.57,
 732 |             close: 182.23,
 733 |           },
 734 |           {
 735 |             time: "2019-03-18",
 736 |             open: 182.53,
 737 |             high: 183.48,
 738 |             low: 182.33,
 739 |             close: 183.42,
 740 |           },
 741 |           {
 742 |             time: "2019-03-19",
 743 |             open: 184.19,
 744 |             high: 185.82,
 745 |             low: 183.48,
 746 |             close: 184.13,
 747 |           },
 748 |           {
 749 |             time: "2019-03-20",
 750 |             open: 184.3,
 751 |             high: 187.12,
 752 |             low: 183.43,
 753 |             close: 186.1,
 754 |           },
 755 |           {
 756 |             time: "2019-03-21",
 757 |             open: 185.5,
 758 |             high: 190.0,
 759 |             low: 185.5,
 760 |             close: 189.97,
 761 |           },
 762 |           {
 763 |             time: "2019-03-22",
 764 |             open: 189.31,
 765 |             high: 192.05,
 766 |             low: 188.67,
 767 |             close: 188.75,
 768 |           },
 769 |           {
 770 |             time: "2019-03-25",
 771 |             open: 188.75,
 772 |             high: 191.71,
 773 |             low: 188.51,
 774 |             close: 189.68,
 775 |           },
 776 |           {
 777 |             time: "2019-03-26",
 778 |             open: 190.69,
 779 |             high: 192.19,
 780 |             low: 188.74,
 781 |             close: 189.34,
 782 |           },
 783 |           {
 784 |             time: "2019-03-27",
 785 |             open: 189.65,
 786 |             high: 191.61,
 787 |             low: 188.39,
 788 |             close: 189.25,
 789 |           },
 790 |           {
 791 |             time: "2019-03-28",
 792 |             open: 189.91,
 793 |             high: 191.4,
 794 |             low: 189.16,
 795 |             close: 190.06,
 796 |           },
 797 |           {
 798 |             time: "2019-03-29",
 799 |             open: 190.85,
 800 |             high: 192.04,
 801 |             low: 190.14,
 802 |             close: 191.89,
 803 |           },
 804 |           {
 805 |             time: "2019-04-01",
 806 |             open: 192.99,
 807 |             high: 195.9,
 808 |             low: 192.85,
 809 |             close: 195.64,
 810 |           },
 811 |           {
 812 |             time: "2019-04-02",
 813 |             open: 195.5,
 814 |             high: 195.5,
 815 |             low: 194.01,
 816 |             close: 194.31,
 817 |           },
 818 |           {
 819 |             time: "2019-04-03",
 820 |             open: 194.98,
 821 |             high: 198.78,
 822 |             low: 194.11,
 823 |             close: 198.61,
 824 |           },
 825 |           {
 826 |             time: "2019-04-04",
 827 |             open: 199.0,
 828 |             high: 200.49,
 829 |             low: 198.02,
 830 |             close: 200.45,
 831 |           },
 832 |           {
 833 |             time: "2019-04-05",
 834 |             open: 200.86,
 835 |             high: 203.13,
 836 |             low: 200.61,
 837 |             close: 202.06,
 838 |           },
 839 |           {
 840 |             time: "2019-04-08",
 841 |             open: 201.37,
 842 |             high: 203.79,
 843 |             low: 201.24,
 844 |             close: 203.55,
 845 |           },
 846 |           {
 847 |             time: "2019-04-09",
 848 |             open: 202.26,
 849 |             high: 202.71,
 850 |             low: 200.46,
 851 |             close: 200.9,
 852 |           },
 853 |           {
 854 |             time: "2019-04-10",
 855 |             open: 201.26,
 856 |             high: 201.6,
 857 |             low: 198.02,
 858 |             close: 199.43,
 859 |           },
 860 |           {
 861 |             time: "2019-04-11",
 862 |             open: 199.9,
 863 |             high: 201.5,
 864 |             low: 199.03,
 865 |             close: 201.48,
 866 |           },
 867 |           {
 868 |             time: "2019-04-12",
 869 |             open: 202.13,
 870 |             high: 204.26,
 871 |             low: 202.13,
 872 |             close: 203.85,
 873 |           },
 874 |           {
 875 |             time: "2019-04-15",
 876 |             open: 204.16,
 877 |             high: 205.14,
 878 |             low: 203.4,
 879 |             close: 204.86,
 880 |           },
 881 |           {
 882 |             time: "2019-04-16",
 883 |             open: 205.25,
 884 |             high: 205.99,
 885 |             low: 204.29,
 886 |             close: 204.47,
 887 |           },
 888 |           {
 889 |             time: "2019-04-17",
 890 |             open: 205.34,
 891 |             high: 206.84,
 892 |             low: 205.32,
 893 |             close: 206.55,
 894 |           },
 895 |           {
 896 |             time: "2019-04-18",
 897 |             open: 206.02,
 898 |             high: 207.78,
 899 |             low: 205.1,
 900 |             close: 205.66,
 901 |           },
 902 |           {
 903 |             time: "2019-04-22",
 904 |             open: 204.11,
 905 |             high: 206.25,
 906 |             low: 204.0,
 907 |             close: 204.78,
 908 |           },
 909 |           {
 910 |             time: "2019-04-23",
 911 |             open: 205.14,
 912 |             high: 207.33,
 913 |             low: 203.43,
 914 |             close: 206.05,
 915 |           },
 916 |           {
 917 |             time: "2019-04-24",
 918 |             open: 206.16,
 919 |             high: 208.29,
 920 |             low: 205.54,
 921 |             close: 206.72,
 922 |           },
 923 |           {
 924 |             time: "2019-04-25",
 925 |             open: 206.01,
 926 |             high: 207.72,
 927 |             low: 205.06,
 928 |             close: 206.5,
 929 |           },
 930 |           {
 931 |             time: "2019-04-26",
 932 |             open: 205.88,
 933 |             high: 206.14,
 934 |             low: 203.34,
 935 |             close: 203.61,
 936 |           },
 937 |           {
 938 |             time: "2019-04-29",
 939 |             open: 203.31,
 940 |             high: 203.8,
 941 |             low: 200.34,
 942 |             close: 202.16,
 943 |           },
 944 |           {
 945 |             time: "2019-04-30",
 946 |             open: 201.55,
 947 |             high: 203.75,
 948 |             low: 200.79,
 949 |             close: 203.7,
 950 |           },
 951 |           {
 952 |             time: "2019-05-01",
 953 |             open: 203.2,
 954 |             high: 203.52,
 955 |             low: 198.66,
 956 |             close: 198.8,
 957 |           },
 958 |           {
 959 |             time: "2019-05-02",
 960 |             open: 199.3,
 961 |             high: 201.06,
 962 |             low: 198.8,
 963 |             close: 201.01,
 964 |           },
 965 |           {
 966 |             time: "2019-05-03",
 967 |             open: 202.0,
 968 |             high: 202.31,
 969 |             low: 200.32,
 970 |             close: 200.56,
 971 |           },
 972 |           {
 973 |             time: "2019-05-06",
 974 |             open: 198.74,
 975 |             high: 199.93,
 976 |             low: 198.31,
 977 |             close: 199.63,
 978 |           },
 979 |           {
 980 |             time: "2019-05-07",
 981 |             open: 196.75,
 982 |             high: 197.65,
 983 |             low: 192.96,
 984 |             close: 194.77,
 985 |           },
 986 |           {
 987 |             time: "2019-05-08",
 988 |             open: 194.49,
 989 |             high: 196.61,
 990 |             low: 193.68,
 991 |             close: 195.17,
 992 |           },
 993 |           {
 994 |             time: "2019-05-09",
 995 |             open: 193.31,
 996 |             high: 195.08,
 997 |             low: 191.59,
 998 |             close: 194.58,
 999 |           },
1000 |           {
1001 |             time: "2019-05-10",
1002 |             open: 193.21,
1003 |             high: 195.49,
1004 |             low: 190.01,
1005 |             close: 194.58,
1006 |           },
1007 |           {
1008 |             time: "2019-05-13",
1009 |             open: 191.0,
1010 |             high: 191.66,
1011 |             low: 189.14,
1012 |             close: 190.34,
1013 |           },
1014 |           {
1015 |             time: "2019-05-14",
1016 |             open: 190.5,
1017 |             high: 192.76,
1018 |             low: 190.01,
1019 |             close: 191.62,
1020 |           },
1021 |           {
1022 |             time: "2019-05-15",
1023 |             open: 190.81,
1024 |             high: 192.81,
1025 |             low: 190.27,
1026 |             close: 191.76,
1027 |           },
1028 |           {
1029 |             time: "2019-05-16",
1030 |             open: 192.47,
1031 |             high: 194.96,
1032 |             low: 192.2,
1033 |             close: 192.38,
1034 |           },
1035 |           {
1036 |             time: "2019-05-17",
1037 |             open: 190.86,
1038 |             high: 194.5,
1039 |             low: 190.75,
1040 |             close: 192.58,
1041 |           },
1042 |           {
1043 |             time: "2019-05-20",
1044 |             open: 191.13,
1045 |             high: 192.86,
1046 |             low: 190.61,
1047 |             close: 190.95,
1048 |           },
1049 |           {
1050 |             time: "2019-05-21",
1051 |             open: 187.13,
1052 |             high: 192.52,
1053 |             low: 186.34,
1054 |             close: 191.45,
1055 |           },
1056 |           {
1057 |             time: "2019-05-22",
1058 |             open: 190.49,
1059 |             high: 192.22,
1060 |             low: 188.05,
1061 |             close: 188.91,
1062 |           },
1063 |           {
1064 |             time: "2019-05-23",
1065 |             open: 188.45,
1066 |             high: 192.54,
1067 |             low: 186.27,
1068 |             close: 192.0,
1069 |           },
1070 |           {
1071 |             time: "2019-05-24",
1072 |             open: 192.54,
1073 |             high: 193.86,
1074 |             low: 190.41,
1075 |             close: 193.59,
1076 |           },
1077 |         ];
1078 |       }
1079 | 
1080 |       // Create the Lightweight Chart within the container element
1081 |       const chart = LightweightCharts.createChart(
1082 |         document.getElementById('container'),
1083 |         {
1084 |           layout: {
1085 |             background: { color: "#222" },
1086 |             textColor: "#C3BCDB",
1087 |           },
1088 |           grid: {
1089 |             vertLines: { color: "#444" },
1090 |             horzLines: { color: "#444" },
1091 |           },
1092 |         }
1093 |       );
1094 | 
1095 |       // Setting the border color for the vertical axis
1096 |       chart.priceScale().applyOptions({
1097 |         borderColor: "#71649C",
1098 |       });
1099 | 
1100 |       // Setting the border color for the horizontal axis
1101 |       chart.timeScale().applyOptions({
1102 |         borderColor: "#71649C",
1103 |       });
1104 | 
1105 |       // Get the current users primary locale
1106 |       const currentLocale = window.navigator.languages[0];
1107 |       // Create a number format using Intl.NumberFormat
1108 |       const myPriceFormatter = Intl.NumberFormat(currentLocale, {
1109 |             style: "currency",
1110 |             currency: "EUR", // Currency for data points
1111 |           }).format;
1112 | 
1113 |       // Apply the custom priceFormatter to the chart
1114 |       chart.applyOptions({
1115 |         localization: {
1116 |           priceFormatter: myPriceFormatter,
1117 |         },
1118 |       });
1119 | 
1120 |       // Generate sample data to use within a candlestick series
1121 |       const candleStickData = generateCandlestickData();
1122 | 
1123 |       // Create the Main Series (Candlesticks)
1124 |       const mainSeries = chart.addSeries(LightweightCharts.CandlestickSeries);
1125 |       // Set the data for the Main Series
1126 |       mainSeries.setData(candleStickData);
1127 | 
1128 |       // Changing the Candlestick colors
1129 |       mainSeries.applyOptions({
1130 |         wickUpColor: "rgb(54, 116, 217)",
1131 |         upColor: "rgb(54, 116, 217)",
1132 |         wickDownColor: "rgb(225, 50, 85)",
1133 |         downColor: "rgb(225, 50, 85)",
1134 |         borderVisible: false,
1135 |       });
1136 | 
1137 |       // Adding a window resize event handler to resize the chart when
1138 |       // the window size changes.
1139 |       // Note: for more advanced examples (when the chart doesn't fill the entire window)
1140 |       // you may need to use ResizeObserver -> https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver
1141 |       window.addEventListener("resize", () => {
1142 |         chart.resize(window.innerWidth, window.innerHeight);
1143 |       });
1144 |     </script>
1145 |   </body>
1146 | </html>
1147 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/assets/step5.html:
--------------------------------------------------------------------------------
   1 | <!DOCTYPE html>
   2 | <html>
   3 |   <head>
   4 |     <meta charset="UTF-8" />
   5 |     <meta
   6 |       name="viewport"
   7 |       content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0"
   8 |     />
   9 |     <title>Lightweight Charts™ Customization Tutorial</title>
  10 |     <!-- Adding the standalone version of Lightweight charts -->
  11 |     <script
  12 |       type="text/javascript"
  13 |       src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"
  14 |     ></script>
  15 |     <style>
  16 |       body {
  17 |         padding: 0;
  18 |         margin: 0;
  19 |         /* Add a background color to match the chart */
  20 |         background-color: #222;
  21 |       }
  22 |     </style>
  23 |   </head>
  24 | 
  25 |   <body>
  26 |     <div
  27 |       id="container"
  28 |       style="position: absolute; width: 100%; height: 100%"
  29 |     ></div>
  30 |     <script type="text/javascript">
  31 |       // Function to generate a sample set of Candlestick datapoints
  32 |       function generateCandlestickData() {
  33 |         return [
  34 |           {
  35 |             time: "2018-10-19",
  36 |             open: 180.34,
  37 |             high: 180.99,
  38 |             low: 178.57,
  39 |             close: 179.85,
  40 |           },
  41 |           {
  42 |             time: "2018-10-22",
  43 |             open: 180.82,
  44 |             high: 181.4,
  45 |             low: 177.56,
  46 |             close: 178.75,
  47 |           },
  48 |           {
  49 |             time: "2018-10-23",
  50 |             open: 175.77,
  51 |             high: 179.49,
  52 |             low: 175.44,
  53 |             close: 178.53,
  54 |           },
  55 |           {
  56 |             time: "2018-10-24",
  57 |             open: 178.58,
  58 |             high: 182.37,
  59 |             low: 176.31,
  60 |             close: 176.97,
  61 |           },
  62 |           {
  63 |             time: "2018-10-25",
  64 |             open: 177.52,
  65 |             high: 180.5,
  66 |             low: 176.83,
  67 |             close: 179.07,
  68 |           },
  69 |           {
  70 |             time: "2018-10-26",
  71 |             open: 176.88,
  72 |             high: 177.34,
  73 |             low: 170.91,
  74 |             close: 172.23,
  75 |           },
  76 |           {
  77 |             time: "2018-10-29",
  78 |             open: 173.74,
  79 |             high: 175.99,
  80 |             low: 170.95,
  81 |             close: 173.2,
  82 |           },
  83 |           {
  84 |             time: "2018-10-30",
  85 |             open: 173.16,
  86 |             high: 176.43,
  87 |             low: 172.64,
  88 |             close: 176.24,
  89 |           },
  90 |           {
  91 |             time: "2018-10-31",
  92 |             open: 177.98,
  93 |             high: 178.85,
  94 |             low: 175.59,
  95 |             close: 175.88,
  96 |           },
  97 |           {
  98 |             time: "2018-11-01",
  99 |             open: 176.84,
 100 |             high: 180.86,
 101 |             low: 175.9,
 102 |             close: 180.46,
 103 |           },
 104 |           {
 105 |             time: "2018-11-02",
 106 |             open: 182.47,
 107 |             high: 183.01,
 108 |             low: 177.39,
 109 |             close: 179.93,
 110 |           },
 111 |           {
 112 |             time: "2018-11-05",
 113 |             open: 181.02,
 114 |             high: 182.41,
 115 |             low: 179.3,
 116 |             close: 182.19,
 117 |           },
 118 |           {
 119 |             time: "2018-11-06",
 120 |             open: 181.93,
 121 |             high: 182.65,
 122 |             low: 180.05,
 123 |             close: 182.01,
 124 |           },
 125 |           {
 126 |             time: "2018-11-07",
 127 |             open: 183.79,
 128 |             high: 187.68,
 129 |             low: 182.06,
 130 |             close: 187.23,
 131 |           },
 132 |           {
 133 |             time: "2018-11-08",
 134 |             open: 187.13,
 135 |             high: 188.69,
 136 |             low: 185.72,
 137 |             close: 188.0,
 138 |           },
 139 |           {
 140 |             time: "2018-11-09",
 141 |             open: 188.32,
 142 |             high: 188.48,
 143 |             low: 184.96,
 144 |             close: 185.99,
 145 |           },
 146 |           {
 147 |             time: "2018-11-12",
 148 |             open: 185.23,
 149 |             high: 186.95,
 150 |             low: 179.02,
 151 |             close: 179.43,
 152 |           },
 153 |           {
 154 |             time: "2018-11-13",
 155 |             open: 177.3,
 156 |             high: 181.62,
 157 |             low: 172.85,
 158 |             close: 179.0,
 159 |           },
 160 |           {
 161 |             time: "2018-11-14",
 162 |             open: 182.61,
 163 |             high: 182.9,
 164 |             low: 179.15,
 165 |             close: 179.9,
 166 |           },
 167 |           {
 168 |             time: "2018-11-15",
 169 |             open: 179.01,
 170 |             high: 179.67,
 171 |             low: 173.61,
 172 |             close: 177.36,
 173 |           },
 174 |           {
 175 |             time: "2018-11-16",
 176 |             open: 173.99,
 177 |             high: 177.6,
 178 |             low: 173.51,
 179 |             close: 177.02,
 180 |           },
 181 |           {
 182 |             time: "2018-11-19",
 183 |             open: 176.71,
 184 |             high: 178.88,
 185 |             low: 172.3,
 186 |             close: 173.59,
 187 |           },
 188 |           {
 189 |             time: "2018-11-20",
 190 |             open: 169.25,
 191 |             high: 172.0,
 192 |             low: 167.0,
 193 |             close: 169.05,
 194 |           },
 195 |           {
 196 |             time: "2018-11-21",
 197 |             open: 170.0,
 198 |             high: 170.93,
 199 |             low: 169.15,
 200 |             close: 169.3,
 201 |           },
 202 |           {
 203 |             time: "2018-11-23",
 204 |             open: 169.39,
 205 |             high: 170.33,
 206 |             low: 168.47,
 207 |             close: 168.85,
 208 |           },
 209 |           {
 210 |             time: "2018-11-26",
 211 |             open: 170.2,
 212 |             high: 172.39,
 213 |             low: 168.87,
 214 |             close: 169.82,
 215 |           },
 216 |           {
 217 |             time: "2018-11-27",
 218 |             open: 169.11,
 219 |             high: 173.38,
 220 |             low: 168.82,
 221 |             close: 173.22,
 222 |           },
 223 |           {
 224 |             time: "2018-11-28",
 225 |             open: 172.91,
 226 |             high: 177.65,
 227 |             low: 170.62,
 228 |             close: 177.43,
 229 |           },
 230 |           {
 231 |             time: "2018-11-29",
 232 |             open: 176.8,
 233 |             high: 177.27,
 234 |             low: 174.92,
 235 |             close: 175.66,
 236 |           },
 237 |           {
 238 |             time: "2018-11-30",
 239 |             open: 175.75,
 240 |             high: 180.37,
 241 |             low: 175.11,
 242 |             close: 180.32,
 243 |           },
 244 |           {
 245 |             time: "2018-12-03",
 246 |             open: 183.29,
 247 |             high: 183.5,
 248 |             low: 179.35,
 249 |             close: 181.74,
 250 |           },
 251 |           {
 252 |             time: "2018-12-04",
 253 |             open: 181.06,
 254 |             high: 182.23,
 255 |             low: 174.55,
 256 |             close: 175.3,
 257 |           },
 258 |           {
 259 |             time: "2018-12-06",
 260 |             open: 173.5,
 261 |             high: 176.04,
 262 |             low: 170.46,
 263 |             close: 175.96,
 264 |           },
 265 |           {
 266 |             time: "2018-12-07",
 267 |             open: 175.35,
 268 |             high: 178.36,
 269 |             low: 172.24,
 270 |             close: 172.79,
 271 |           },
 272 |           {
 273 |             time: "2018-12-10",
 274 |             open: 173.39,
 275 |             high: 173.99,
 276 |             low: 167.73,
 277 |             close: 171.69,
 278 |           },
 279 |           {
 280 |             time: "2018-12-11",
 281 |             open: 174.3,
 282 |             high: 175.6,
 283 |             low: 171.24,
 284 |             close: 172.21,
 285 |           },
 286 |           {
 287 |             time: "2018-12-12",
 288 |             open: 173.75,
 289 |             high: 176.87,
 290 |             low: 172.81,
 291 |             close: 174.21,
 292 |           },
 293 |           {
 294 |             time: "2018-12-13",
 295 |             open: 174.31,
 296 |             high: 174.91,
 297 |             low: 172.07,
 298 |             close: 173.87,
 299 |           },
 300 |           {
 301 |             time: "2018-12-14",
 302 |             open: 172.98,
 303 |             high: 175.14,
 304 |             low: 171.95,
 305 |             close: 172.29,
 306 |           },
 307 |           {
 308 |             time: "2018-12-17",
 309 |             open: 171.51,
 310 |             high: 171.99,
 311 |             low: 166.93,
 312 |             close: 167.97,
 313 |           },
 314 |           {
 315 |             time: "2018-12-18",
 316 |             open: 168.9,
 317 |             high: 171.95,
 318 |             low: 168.5,
 319 |             close: 170.04,
 320 |           },
 321 |           {
 322 |             time: "2018-12-19",
 323 |             open: 170.92,
 324 |             high: 174.95,
 325 |             low: 166.77,
 326 |             close: 167.56,
 327 |           },
 328 |           {
 329 |             time: "2018-12-20",
 330 |             open: 166.28,
 331 |             high: 167.31,
 332 |             low: 162.23,
 333 |             close: 164.16,
 334 |           },
 335 |           {
 336 |             time: "2018-12-21",
 337 |             open: 162.81,
 338 |             high: 167.96,
 339 |             low: 160.17,
 340 |             close: 160.48,
 341 |           },
 342 |           {
 343 |             time: "2018-12-24",
 344 |             open: 160.16,
 345 |             high: 161.4,
 346 |             low: 158.09,
 347 |             close: 158.14,
 348 |           },
 349 |           {
 350 |             time: "2018-12-26",
 351 |             open: 159.46,
 352 |             high: 168.28,
 353 |             low: 159.44,
 354 |             close: 168.28,
 355 |           },
 356 |           {
 357 |             time: "2018-12-27",
 358 |             open: 166.44,
 359 |             high: 170.46,
 360 |             low: 163.36,
 361 |             close: 170.32,
 362 |           },
 363 |           {
 364 |             time: "2018-12-28",
 365 |             open: 171.22,
 366 |             high: 173.12,
 367 |             low: 168.6,
 368 |             close: 170.22,
 369 |           },
 370 |           {
 371 |             time: "2018-12-31",
 372 |             open: 171.47,
 373 |             high: 173.24,
 374 |             low: 170.65,
 375 |             close: 171.82,
 376 |           },
 377 |           {
 378 |             time: "2019-01-02",
 379 |             open: 169.71,
 380 |             high: 173.18,
 381 |             low: 169.05,
 382 |             close: 172.41,
 383 |           },
 384 |           {
 385 |             time: "2019-01-03",
 386 |             open: 171.84,
 387 |             high: 171.84,
 388 |             low: 168.21,
 389 |             close: 168.61,
 390 |           },
 391 |           {
 392 |             time: "2019-01-04",
 393 |             open: 170.18,
 394 |             high: 174.74,
 395 |             low: 169.52,
 396 |             close: 173.62,
 397 |           },
 398 |           {
 399 |             time: "2019-01-07",
 400 |             open: 173.83,
 401 |             high: 178.18,
 402 |             low: 173.83,
 403 |             close: 177.04,
 404 |           },
 405 |           {
 406 |             time: "2019-01-08",
 407 |             open: 178.57,
 408 |             high: 179.59,
 409 |             low: 175.61,
 410 |             close: 177.89,
 411 |           },
 412 |           {
 413 |             time: "2019-01-09",
 414 |             open: 177.87,
 415 |             high: 181.27,
 416 |             low: 177.1,
 417 |             close: 179.73,
 418 |           },
 419 |           {
 420 |             time: "2019-01-10",
 421 |             open: 178.03,
 422 |             high: 179.24,
 423 |             low: 176.34,
 424 |             close: 179.06,
 425 |           },
 426 |           {
 427 |             time: "2019-01-11",
 428 |             open: 177.93,
 429 |             high: 180.26,
 430 |             low: 177.12,
 431 |             close: 179.41,
 432 |           },
 433 |           {
 434 |             time: "2019-01-14",
 435 |             open: 177.59,
 436 |             high: 179.23,
 437 |             low: 176.9,
 438 |             close: 178.81,
 439 |           },
 440 |           {
 441 |             time: "2019-01-15",
 442 |             open: 176.08,
 443 |             high: 177.82,
 444 |             low: 175.2,
 445 |             close: 176.47,
 446 |           },
 447 |           {
 448 |             time: "2019-01-16",
 449 |             open: 177.09,
 450 |             high: 177.93,
 451 |             low: 175.86,
 452 |             close: 177.04,
 453 |           },
 454 |           {
 455 |             time: "2019-01-17",
 456 |             open: 174.01,
 457 |             high: 175.46,
 458 |             low: 172.0,
 459 |             close: 174.87,
 460 |           },
 461 |           {
 462 |             time: "2019-01-18",
 463 |             open: 176.98,
 464 |             high: 180.04,
 465 |             low: 176.18,
 466 |             close: 179.58,
 467 |           },
 468 |           {
 469 |             time: "2019-01-22",
 470 |             open: 177.49,
 471 |             high: 178.6,
 472 |             low: 175.36,
 473 |             close: 177.11,
 474 |           },
 475 |           {
 476 |             time: "2019-01-23",
 477 |             open: 176.59,
 478 |             high: 178.06,
 479 |             low: 174.53,
 480 |             close: 176.89,
 481 |           },
 482 |           {
 483 |             time: "2019-01-24",
 484 |             open: 177.0,
 485 |             high: 177.53,
 486 |             low: 175.3,
 487 |             close: 177.29,
 488 |           },
 489 |           {
 490 |             time: "2019-01-25",
 491 |             open: 179.78,
 492 |             high: 180.87,
 493 |             low: 178.61,
 494 |             close: 180.4,
 495 |           },
 496 |           {
 497 |             time: "2019-01-28",
 498 |             open: 178.97,
 499 |             high: 179.99,
 500 |             low: 177.41,
 501 |             close: 179.83,
 502 |           },
 503 |           {
 504 |             time: "2019-01-29",
 505 |             open: 178.96,
 506 |             high: 180.15,
 507 |             low: 178.09,
 508 |             close: 179.69,
 509 |           },
 510 |           {
 511 |             time: "2019-01-30",
 512 |             open: 180.47,
 513 |             high: 184.2,
 514 |             low: 179.78,
 515 |             close: 182.18,
 516 |           },
 517 |           {
 518 |             time: "2019-01-31",
 519 |             open: 181.5,
 520 |             high: 184.67,
 521 |             low: 181.06,
 522 |             close: 183.53,
 523 |           },
 524 |           {
 525 |             time: "2019-02-01",
 526 |             open: 184.03,
 527 |             high: 185.15,
 528 |             low: 182.83,
 529 |             close: 184.37,
 530 |           },
 531 |           {
 532 |             time: "2019-02-04",
 533 |             open: 184.3,
 534 |             high: 186.43,
 535 |             low: 183.84,
 536 |             close: 186.43,
 537 |           },
 538 |           {
 539 |             time: "2019-02-05",
 540 |             open: 186.89,
 541 |             high: 186.99,
 542 |             low: 184.69,
 543 |             close: 186.39,
 544 |           },
 545 |           {
 546 |             time: "2019-02-06",
 547 |             open: 186.69,
 548 |             high: 186.69,
 549 |             low: 184.06,
 550 |             close: 184.72,
 551 |           },
 552 |           {
 553 |             time: "2019-02-07",
 554 |             open: 183.74,
 555 |             high: 184.92,
 556 |             low: 182.45,
 557 |             close: 184.07,
 558 |           },
 559 |           {
 560 |             time: "2019-02-08",
 561 |             open: 183.05,
 562 |             high: 184.58,
 563 |             low: 182.72,
 564 |             close: 184.54,
 565 |           },
 566 |           {
 567 |             time: "2019-02-11",
 568 |             open: 185.0,
 569 |             high: 185.42,
 570 |             low: 182.75,
 571 |             close: 182.92,
 572 |           },
 573 |           {
 574 |             time: "2019-02-12",
 575 |             open: 183.84,
 576 |             high: 186.4,
 577 |             low: 183.52,
 578 |             close: 185.52,
 579 |           },
 580 |           {
 581 |             time: "2019-02-13",
 582 |             open: 186.3,
 583 |             high: 188.68,
 584 |             low: 185.92,
 585 |             close: 188.41,
 586 |           },
 587 |           {
 588 |             time: "2019-02-14",
 589 |             open: 187.5,
 590 |             high: 188.93,
 591 |             low: 186.0,
 592 |             close: 187.71,
 593 |           },
 594 |           {
 595 |             time: "2019-02-15",
 596 |             open: 189.87,
 597 |             high: 192.62,
 598 |             low: 189.05,
 599 |             close: 192.39,
 600 |           },
 601 |           {
 602 |             time: "2019-02-19",
 603 |             open: 191.71,
 604 |             high: 193.19,
 605 |             low: 191.28,
 606 |             close: 192.33,
 607 |           },
 608 |           {
 609 |             time: "2019-02-20",
 610 |             open: 192.39,
 611 |             high: 192.4,
 612 |             low: 191.11,
 613 |             close: 191.85,
 614 |           },
 615 |           {
 616 |             time: "2019-02-21",
 617 |             open: 191.85,
 618 |             high: 192.37,
 619 |             low: 190.61,
 620 |             close: 191.82,
 621 |           },
 622 |           {
 623 |             time: "2019-02-22",
 624 |             open: 191.69,
 625 |             high: 192.54,
 626 |             low: 191.62,
 627 |             close: 192.39,
 628 |           },
 629 |           {
 630 |             time: "2019-02-25",
 631 |             open: 192.75,
 632 |             high: 193.42,
 633 |             low: 189.96,
 634 |             close: 189.98,
 635 |           },
 636 |           {
 637 |             time: "2019-02-26",
 638 |             open: 185.59,
 639 |             high: 188.47,
 640 |             low: 182.8,
 641 |             close: 188.3,
 642 |           },
 643 |           {
 644 |             time: "2019-02-27",
 645 |             open: 187.9,
 646 |             high: 188.5,
 647 |             low: 183.21,
 648 |             close: 183.67,
 649 |           },
 650 |           {
 651 |             time: "2019-02-28",
 652 |             open: 183.6,
 653 |             high: 185.19,
 654 |             low: 183.11,
 655 |             close: 185.14,
 656 |           },
 657 |           {
 658 |             time: "2019-03-01",
 659 |             open: 185.82,
 660 |             high: 186.56,
 661 |             low: 182.86,
 662 |             close: 185.17,
 663 |           },
 664 |           {
 665 |             time: "2019-03-04",
 666 |             open: 186.2,
 667 |             high: 186.24,
 668 |             low: 182.1,
 669 |             close: 183.81,
 670 |           },
 671 |           {
 672 |             time: "2019-03-05",
 673 |             open: 184.24,
 674 |             high: 185.12,
 675 |             low: 183.25,
 676 |             close: 184.0,
 677 |           },
 678 |           {
 679 |             time: "2019-03-06",
 680 |             open: 184.53,
 681 |             high: 184.97,
 682 |             low: 183.84,
 683 |             close: 184.45,
 684 |           },
 685 |           {
 686 |             time: "2019-03-07",
 687 |             open: 184.39,
 688 |             high: 184.62,
 689 |             low: 181.58,
 690 |             close: 182.51,
 691 |           },
 692 |           {
 693 |             time: "2019-03-08",
 694 |             open: 181.49,
 695 |             high: 181.91,
 696 |             low: 179.52,
 697 |             close: 181.23,
 698 |           },
 699 |           {
 700 |             time: "2019-03-11",
 701 |             open: 182.0,
 702 |             high: 183.2,
 703 |             low: 181.2,
 704 |             close: 182.44,
 705 |           },
 706 |           {
 707 |             time: "2019-03-12",
 708 |             open: 183.43,
 709 |             high: 184.27,
 710 |             low: 182.33,
 711 |             close: 184.0,
 712 |           },
 713 |           {
 714 |             time: "2019-03-13",
 715 |             open: 183.24,
 716 |             high: 183.78,
 717 |             low: 181.08,
 718 |             close: 181.14,
 719 |           },
 720 |           {
 721 |             time: "2019-03-14",
 722 |             open: 181.28,
 723 |             high: 181.74,
 724 |             low: 180.5,
 725 |             close: 181.61,
 726 |           },
 727 |           {
 728 |             time: "2019-03-15",
 729 |             open: 182.3,
 730 |             high: 182.49,
 731 |             low: 179.57,
 732 |             close: 182.23,
 733 |           },
 734 |           {
 735 |             time: "2019-03-18",
 736 |             open: 182.53,
 737 |             high: 183.48,
 738 |             low: 182.33,
 739 |             close: 183.42,
 740 |           },
 741 |           {
 742 |             time: "2019-03-19",
 743 |             open: 184.19,
 744 |             high: 185.82,
 745 |             low: 183.48,
 746 |             close: 184.13,
 747 |           },
 748 |           {
 749 |             time: "2019-03-20",
 750 |             open: 184.3,
 751 |             high: 187.12,
 752 |             low: 183.43,
 753 |             close: 186.1,
 754 |           },
 755 |           {
 756 |             time: "2019-03-21",
 757 |             open: 185.5,
 758 |             high: 190.0,
 759 |             low: 185.5,
 760 |             close: 189.97,
 761 |           },
 762 |           {
 763 |             time: "2019-03-22",
 764 |             open: 189.31,
 765 |             high: 192.05,
 766 |             low: 188.67,
 767 |             close: 188.75,
 768 |           },
 769 |           {
 770 |             time: "2019-03-25",
 771 |             open: 188.75,
 772 |             high: 191.71,
 773 |             low: 188.51,
 774 |             close: 189.68,
 775 |           },
 776 |           {
 777 |             time: "2019-03-26",
 778 |             open: 190.69,
 779 |             high: 192.19,
 780 |             low: 188.74,
 781 |             close: 189.34,
 782 |           },
 783 |           {
 784 |             time: "2019-03-27",
 785 |             open: 189.65,
 786 |             high: 191.61,
 787 |             low: 188.39,
 788 |             close: 189.25,
 789 |           },
 790 |           {
 791 |             time: "2019-03-28",
 792 |             open: 189.91,
 793 |             high: 191.4,
 794 |             low: 189.16,
 795 |             close: 190.06,
 796 |           },
 797 |           {
 798 |             time: "2019-03-29",
 799 |             open: 190.85,
 800 |             high: 192.04,
 801 |             low: 190.14,
 802 |             close: 191.89,
 803 |           },
 804 |           {
 805 |             time: "2019-04-01",
 806 |             open: 192.99,
 807 |             high: 195.9,
 808 |             low: 192.85,
 809 |             close: 195.64,
 810 |           },
 811 |           {
 812 |             time: "2019-04-02",
 813 |             open: 195.5,
 814 |             high: 195.5,
 815 |             low: 194.01,
 816 |             close: 194.31,
 817 |           },
 818 |           {
 819 |             time: "2019-04-03",
 820 |             open: 194.98,
 821 |             high: 198.78,
 822 |             low: 194.11,
 823 |             close: 198.61,
 824 |           },
 825 |           {
 826 |             time: "2019-04-04",
 827 |             open: 199.0,
 828 |             high: 200.49,
 829 |             low: 198.02,
 830 |             close: 200.45,
 831 |           },
 832 |           {
 833 |             time: "2019-04-05",
 834 |             open: 200.86,
 835 |             high: 203.13,
 836 |             low: 200.61,
 837 |             close: 202.06,
 838 |           },
 839 |           {
 840 |             time: "2019-04-08",
 841 |             open: 201.37,
 842 |             high: 203.79,
 843 |             low: 201.24,
 844 |             close: 203.55,
 845 |           },
 846 |           {
 847 |             time: "2019-04-09",
 848 |             open: 202.26,
 849 |             high: 202.71,
 850 |             low: 200.46,
 851 |             close: 200.9,
 852 |           },
 853 |           {
 854 |             time: "2019-04-10",
 855 |             open: 201.26,
 856 |             high: 201.6,
 857 |             low: 198.02,
 858 |             close: 199.43,
 859 |           },
 860 |           {
 861 |             time: "2019-04-11",
 862 |             open: 199.9,
 863 |             high: 201.5,
 864 |             low: 199.03,
 865 |             close: 201.48,
 866 |           },
 867 |           {
 868 |             time: "2019-04-12",
 869 |             open: 202.13,
 870 |             high: 204.26,
 871 |             low: 202.13,
 872 |             close: 203.85,
 873 |           },
 874 |           {
 875 |             time: "2019-04-15",
 876 |             open: 204.16,
 877 |             high: 205.14,
 878 |             low: 203.4,
 879 |             close: 204.86,
 880 |           },
 881 |           {
 882 |             time: "2019-04-16",
 883 |             open: 205.25,
 884 |             high: 205.99,
 885 |             low: 204.29,
 886 |             close: 204.47,
 887 |           },
 888 |           {
 889 |             time: "2019-04-17",
 890 |             open: 205.34,
 891 |             high: 206.84,
 892 |             low: 205.32,
 893 |             close: 206.55,
 894 |           },
 895 |           {
 896 |             time: "2019-04-18",
 897 |             open: 206.02,
 898 |             high: 207.78,
 899 |             low: 205.1,
 900 |             close: 205.66,
 901 |           },
 902 |           {
 903 |             time: "2019-04-22",
 904 |             open: 204.11,
 905 |             high: 206.25,
 906 |             low: 204.0,
 907 |             close: 204.78,
 908 |           },
 909 |           {
 910 |             time: "2019-04-23",
 911 |             open: 205.14,
 912 |             high: 207.33,
 913 |             low: 203.43,
 914 |             close: 206.05,
 915 |           },
 916 |           {
 917 |             time: "2019-04-24",
 918 |             open: 206.16,
 919 |             high: 208.29,
 920 |             low: 205.54,
 921 |             close: 206.72,
 922 |           },
 923 |           {
 924 |             time: "2019-04-25",
 925 |             open: 206.01,
 926 |             high: 207.72,
 927 |             low: 205.06,
 928 |             close: 206.5,
 929 |           },
 930 |           {
 931 |             time: "2019-04-26",
 932 |             open: 205.88,
 933 |             high: 206.14,
 934 |             low: 203.34,
 935 |             close: 203.61,
 936 |           },
 937 |           {
 938 |             time: "2019-04-29",
 939 |             open: 203.31,
 940 |             high: 203.8,
 941 |             low: 200.34,
 942 |             close: 202.16,
 943 |           },
 944 |           {
 945 |             time: "2019-04-30",
 946 |             open: 201.55,
 947 |             high: 203.75,
 948 |             low: 200.79,
 949 |             close: 203.7,
 950 |           },
 951 |           {
 952 |             time: "2019-05-01",
 953 |             open: 203.2,
 954 |             high: 203.52,
 955 |             low: 198.66,
 956 |             close: 198.8,
 957 |           },
 958 |           {
 959 |             time: "2019-05-02",
 960 |             open: 199.3,
 961 |             high: 201.06,
 962 |             low: 198.8,
 963 |             close: 201.01,
 964 |           },
 965 |           {
 966 |             time: "2019-05-03",
 967 |             open: 202.0,
 968 |             high: 202.31,
 969 |             low: 200.32,
 970 |             close: 200.56,
 971 |           },
 972 |           {
 973 |             time: "2019-05-06",
 974 |             open: 198.74,
 975 |             high: 199.93,
 976 |             low: 198.31,
 977 |             close: 199.63,
 978 |           },
 979 |           {
 980 |             time: "2019-05-07",
 981 |             open: 196.75,
 982 |             high: 197.65,
 983 |             low: 192.96,
 984 |             close: 194.77,
 985 |           },
 986 |           {
 987 |             time: "2019-05-08",
 988 |             open: 194.49,
 989 |             high: 196.61,
 990 |             low: 193.68,
 991 |             close: 195.17,
 992 |           },
 993 |           {
 994 |             time: "2019-05-09",
 995 |             open: 193.31,
 996 |             high: 195.08,
 997 |             low: 191.59,
 998 |             close: 194.58,
 999 |           },
1000 |           {
1001 |             time: "2019-05-10",
1002 |             open: 193.21,
1003 |             high: 195.49,
1004 |             low: 190.01,
1005 |             close: 194.58,
1006 |           },
1007 |           {
1008 |             time: "2019-05-13",
1009 |             open: 191.0,
1010 |             high: 191.66,
1011 |             low: 189.14,
1012 |             close: 190.34,
1013 |           },
1014 |           {
1015 |             time: "2019-05-14",
1016 |             open: 190.5,
1017 |             high: 192.76,
1018 |             low: 190.01,
1019 |             close: 191.62,
1020 |           },
1021 |           {
1022 |             time: "2019-05-15",
1023 |             open: 190.81,
1024 |             high: 192.81,
1025 |             low: 190.27,
1026 |             close: 191.76,
1027 |           },
1028 |           {
1029 |             time: "2019-05-16",
1030 |             open: 192.47,
1031 |             high: 194.96,
1032 |             low: 192.2,
1033 |             close: 192.38,
1034 |           },
1035 |           {
1036 |             time: "2019-05-17",
1037 |             open: 190.86,
1038 |             high: 194.5,
1039 |             low: 190.75,
1040 |             close: 192.58,
1041 |           },
1042 |           {
1043 |             time: "2019-05-20",
1044 |             open: 191.13,
1045 |             high: 192.86,
1046 |             low: 190.61,
1047 |             close: 190.95,
1048 |           },
1049 |           {
1050 |             time: "2019-05-21",
1051 |             open: 187.13,
1052 |             high: 192.52,
1053 |             low: 186.34,
1054 |             close: 191.45,
1055 |           },
1056 |           {
1057 |             time: "2019-05-22",
1058 |             open: 190.49,
1059 |             high: 192.22,
1060 |             low: 188.05,
1061 |             close: 188.91,
1062 |           },
1063 |           {
1064 |             time: "2019-05-23",
1065 |             open: 188.45,
1066 |             high: 192.54,
1067 |             low: 186.27,
1068 |             close: 192.0,
1069 |           },
1070 |           {
1071 |             time: "2019-05-24",
1072 |             open: 192.54,
1073 |             high: 193.86,
1074 |             low: 190.41,
1075 |             close: 193.59,
1076 |           },
1077 |         ];
1078 |       }
1079 | 
1080 |       // Create the Lightweight Chart within the container element
1081 |       const chart = LightweightCharts.createChart(
1082 |         document.getElementById('container'),
1083 |         {
1084 |           layout: {
1085 |             background: { color: "#222" },
1086 |             textColor: "#C3BCDB",
1087 |           },
1088 |           grid: {
1089 |             vertLines: { color: "#444" },
1090 |             horzLines: { color: "#444" },
1091 |           },
1092 |         }
1093 |       );
1094 | 
1095 |       // Setting the border color for the vertical axis
1096 |       chart.priceScale().applyOptions({
1097 |         borderColor: "#71649C",
1098 |       });
1099 | 
1100 |       // Setting the border color for the horizontal axis
1101 |       chart.timeScale().applyOptions({
1102 |         borderColor: "#71649C",
1103 |       });
1104 | 
1105 |       // Get the current users primary locale
1106 |       const currentLocale = window.navigator.languages[0];
1107 |       // Create a number format using Intl.NumberFormat
1108 |       const myPriceFormatter = Intl.NumberFormat(currentLocale, {
1109 |             style: "currency",
1110 |             currency: "EUR", // Currency for data points
1111 |           }).format;
1112 | 
1113 |       // Apply the custom priceFormatter to the chart
1114 |       chart.applyOptions({
1115 |         localization: {
1116 |           priceFormatter: myPriceFormatter,
1117 |         },
1118 |       });
1119 | 
1120 |       // Generate sample data to use within a candlestick series
1121 |       const candleStickData = generateCandlestickData();
1122 | 
1123 |       // Create the Main Series (Candlesticks)
1124 |       const mainSeries = chart.addSeries(LightweightCharts.CandlestickSeries);
1125 |       // Set the data for the Main Series
1126 |       mainSeries.setData(candleStickData);
1127 | 
1128 |       // Changing the Candlestick colors
1129 |       mainSeries.applyOptions({
1130 |         wickUpColor: "rgb(54, 116, 217)",
1131 |         upColor: "rgb(54, 116, 217)",
1132 |         wickDownColor: "rgb(225, 50, 85)",
1133 |         downColor: "rgb(225, 50, 85)",
1134 |         borderVisible: false,
1135 |       });
1136 | 
1137 |       // Adjust the options for the priceScale of the mainSeries
1138 |       mainSeries.priceScale().applyOptions({
1139 |         autoScale: false, // disables auto scaling based on visible content
1140 |         scaleMargins: {
1141 |           top: 0.1,
1142 |           bottom: 0.2,
1143 |         },
1144 |       });
1145 | 
1146 |       // Adding a window resize event handler to resize the chart when
1147 |       // the window size changes.
1148 |       // Note: for more advanced examples (when the chart doesn't fill the entire window)
1149 |       // you may need to use ResizeObserver -> https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver
1150 |       window.addEventListener("resize", () => {
1151 |         chart.resize(window.innerWidth, window.innerHeight);
1152 |       });
1153 |     </script>
1154 |   </body>
1155 | </html>
1156 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/assets/step6.html:
--------------------------------------------------------------------------------
   1 | <!DOCTYPE html>
   2 | <html>
   3 |   <head>
   4 |     <meta charset="UTF-8" />
   5 |     <meta
   6 |       name="viewport"
   7 |       content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0"
   8 |     />
   9 |     <title>Lightweight Charts™ Customization Tutorial</title>
  10 |     <!-- Adding the standalone version of Lightweight charts -->
  11 |     <script
  12 |       type="text/javascript"
  13 |       src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"
  14 |     ></script>
  15 |     <style>
  16 |       body {
  17 |         padding: 0;
  18 |         margin: 0;
  19 |         /* Add a background color to match the chart */
  20 |         background-color: #222;
  21 |       }
  22 |     </style>
  23 |   </head>
  24 | 
  25 |   <body>
  26 |     <div
  27 |       id="container"
  28 |       style="position: absolute; width: 100%; height: 100%"
  29 |     ></div>
  30 |     <script type="text/javascript">
  31 |       // Function to generate a sample set of Candlestick datapoints
  32 |       function generateCandlestickData() {
  33 |         return [
  34 |           {
  35 |             time: "2018-10-19",
  36 |             open: 180.34,
  37 |             high: 180.99,
  38 |             low: 178.57,
  39 |             close: 179.85,
  40 |           },
  41 |           {
  42 |             time: "2018-10-22",
  43 |             open: 180.82,
  44 |             high: 181.4,
  45 |             low: 177.56,
  46 |             close: 178.75,
  47 |           },
  48 |           {
  49 |             time: "2018-10-23",
  50 |             open: 175.77,
  51 |             high: 179.49,
  52 |             low: 175.44,
  53 |             close: 178.53,
  54 |           },
  55 |           {
  56 |             time: "2018-10-24",
  57 |             open: 178.58,
  58 |             high: 182.37,
  59 |             low: 176.31,
  60 |             close: 176.97,
  61 |           },
  62 |           {
  63 |             time: "2018-10-25",
  64 |             open: 177.52,
  65 |             high: 180.5,
  66 |             low: 176.83,
  67 |             close: 179.07,
  68 |           },
  69 |           {
  70 |             time: "2018-10-26",
  71 |             open: 176.88,
  72 |             high: 177.34,
  73 |             low: 170.91,
  74 |             close: 172.23,
  75 |           },
  76 |           {
  77 |             time: "2018-10-29",
  78 |             open: 173.74,
  79 |             high: 175.99,
  80 |             low: 170.95,
  81 |             close: 173.2,
  82 |           },
  83 |           {
  84 |             time: "2018-10-30",
  85 |             open: 173.16,
  86 |             high: 176.43,
  87 |             low: 172.64,
  88 |             close: 176.24,
  89 |           },
  90 |           {
  91 |             time: "2018-10-31",
  92 |             open: 177.98,
  93 |             high: 178.85,
  94 |             low: 175.59,
  95 |             close: 175.88,
  96 |           },
  97 |           {
  98 |             time: "2018-11-01",
  99 |             open: 176.84,
 100 |             high: 180.86,
 101 |             low: 175.9,
 102 |             close: 180.46,
 103 |           },
 104 |           {
 105 |             time: "2018-11-02",
 106 |             open: 182.47,
 107 |             high: 183.01,
 108 |             low: 177.39,
 109 |             close: 179.93,
 110 |           },
 111 |           {
 112 |             time: "2018-11-05",
 113 |             open: 181.02,
 114 |             high: 182.41,
 115 |             low: 179.3,
 116 |             close: 182.19,
 117 |           },
 118 |           {
 119 |             time: "2018-11-06",
 120 |             open: 181.93,
 121 |             high: 182.65,
 122 |             low: 180.05,
 123 |             close: 182.01,
 124 |           },
 125 |           {
 126 |             time: "2018-11-07",
 127 |             open: 183.79,
 128 |             high: 187.68,
 129 |             low: 182.06,
 130 |             close: 187.23,
 131 |           },
 132 |           {
 133 |             time: "2018-11-08",
 134 |             open: 187.13,
 135 |             high: 188.69,
 136 |             low: 185.72,
 137 |             close: 188.0,
 138 |           },
 139 |           {
 140 |             time: "2018-11-09",
 141 |             open: 188.32,
 142 |             high: 188.48,
 143 |             low: 184.96,
 144 |             close: 185.99,
 145 |           },
 146 |           {
 147 |             time: "2018-11-12",
 148 |             open: 185.23,
 149 |             high: 186.95,
 150 |             low: 179.02,
 151 |             close: 179.43,
 152 |           },
 153 |           {
 154 |             time: "2018-11-13",
 155 |             open: 177.3,
 156 |             high: 181.62,
 157 |             low: 172.85,
 158 |             close: 179.0,
 159 |           },
 160 |           {
 161 |             time: "2018-11-14",
 162 |             open: 182.61,
 163 |             high: 182.9,
 164 |             low: 179.15,
 165 |             close: 179.9,
 166 |           },
 167 |           {
 168 |             time: "2018-11-15",
 169 |             open: 179.01,
 170 |             high: 179.67,
 171 |             low: 173.61,
 172 |             close: 177.36,
 173 |           },
 174 |           {
 175 |             time: "2018-11-16",
 176 |             open: 173.99,
 177 |             high: 177.6,
 178 |             low: 173.51,
 179 |             close: 177.02,
 180 |           },
 181 |           {
 182 |             time: "2018-11-19",
 183 |             open: 176.71,
 184 |             high: 178.88,
 185 |             low: 172.3,
 186 |             close: 173.59,
 187 |           },
 188 |           {
 189 |             time: "2018-11-20",
 190 |             open: 169.25,
 191 |             high: 172.0,
 192 |             low: 167.0,
 193 |             close: 169.05,
 194 |           },
 195 |           {
 196 |             time: "2018-11-21",
 197 |             open: 170.0,
 198 |             high: 170.93,
 199 |             low: 169.15,
 200 |             close: 169.3,
 201 |           },
 202 |           {
 203 |             time: "2018-11-23",
 204 |             open: 169.39,
 205 |             high: 170.33,
 206 |             low: 168.47,
 207 |             close: 168.85,
 208 |           },
 209 |           {
 210 |             time: "2018-11-26",
 211 |             open: 170.2,
 212 |             high: 172.39,
 213 |             low: 168.87,
 214 |             close: 169.82,
 215 |           },
 216 |           {
 217 |             time: "2018-11-27",
 218 |             open: 169.11,
 219 |             high: 173.38,
 220 |             low: 168.82,
 221 |             close: 173.22,
 222 |           },
 223 |           {
 224 |             time: "2018-11-28",
 225 |             open: 172.91,
 226 |             high: 177.65,
 227 |             low: 170.62,
 228 |             close: 177.43,
 229 |           },
 230 |           {
 231 |             time: "2018-11-29",
 232 |             open: 176.8,
 233 |             high: 177.27,
 234 |             low: 174.92,
 235 |             close: 175.66,
 236 |           },
 237 |           {
 238 |             time: "2018-11-30",
 239 |             open: 175.75,
 240 |             high: 180.37,
 241 |             low: 175.11,
 242 |             close: 180.32,
 243 |           },
 244 |           {
 245 |             time: "2018-12-03",
 246 |             open: 183.29,
 247 |             high: 183.5,
 248 |             low: 179.35,
 249 |             close: 181.74,
 250 |           },
 251 |           {
 252 |             time: "2018-12-04",
 253 |             open: 181.06,
 254 |             high: 182.23,
 255 |             low: 174.55,
 256 |             close: 175.3,
 257 |           },
 258 |           {
 259 |             time: "2018-12-06",
 260 |             open: 173.5,
 261 |             high: 176.04,
 262 |             low: 170.46,
 263 |             close: 175.96,
 264 |           },
 265 |           {
 266 |             time: "2018-12-07",
 267 |             open: 175.35,
 268 |             high: 178.36,
 269 |             low: 172.24,
 270 |             close: 172.79,
 271 |           },
 272 |           {
 273 |             time: "2018-12-10",
 274 |             open: 173.39,
 275 |             high: 173.99,
 276 |             low: 167.73,
 277 |             close: 171.69,
 278 |           },
 279 |           {
 280 |             time: "2018-12-11",
 281 |             open: 174.3,
 282 |             high: 175.6,
 283 |             low: 171.24,
 284 |             close: 172.21,
 285 |           },
 286 |           {
 287 |             time: "2018-12-12",
 288 |             open: 173.75,
 289 |             high: 176.87,
 290 |             low: 172.81,
 291 |             close: 174.21,
 292 |           },
 293 |           {
 294 |             time: "2018-12-13",
 295 |             open: 174.31,
 296 |             high: 174.91,
 297 |             low: 172.07,
 298 |             close: 173.87,
 299 |           },
 300 |           {
 301 |             time: "2018-12-14",
 302 |             open: 172.98,
 303 |             high: 175.14,
 304 |             low: 171.95,
 305 |             close: 172.29,
 306 |           },
 307 |           {
 308 |             time: "2018-12-17",
 309 |             open: 171.51,
 310 |             high: 171.99,
 311 |             low: 166.93,
 312 |             close: 167.97,
 313 |           },
 314 |           {
 315 |             time: "2018-12-18",
 316 |             open: 168.9,
 317 |             high: 171.95,
 318 |             low: 168.5,
 319 |             close: 170.04,
 320 |           },
 321 |           {
 322 |             time: "2018-12-19",
 323 |             open: 170.92,
 324 |             high: 174.95,
 325 |             low: 166.77,
 326 |             close: 167.56,
 327 |           },
 328 |           {
 329 |             time: "2018-12-20",
 330 |             open: 166.28,
 331 |             high: 167.31,
 332 |             low: 162.23,
 333 |             close: 164.16,
 334 |           },
 335 |           {
 336 |             time: "2018-12-21",
 337 |             open: 162.81,
 338 |             high: 167.96,
 339 |             low: 160.17,
 340 |             close: 160.48,
 341 |           },
 342 |           {
 343 |             time: "2018-12-24",
 344 |             open: 160.16,
 345 |             high: 161.4,
 346 |             low: 158.09,
 347 |             close: 158.14,
 348 |           },
 349 |           {
 350 |             time: "2018-12-26",
 351 |             open: 159.46,
 352 |             high: 168.28,
 353 |             low: 159.44,
 354 |             close: 168.28,
 355 |           },
 356 |           {
 357 |             time: "2018-12-27",
 358 |             open: 166.44,
 359 |             high: 170.46,
 360 |             low: 163.36,
 361 |             close: 170.32,
 362 |           },
 363 |           {
 364 |             time: "2018-12-28",
 365 |             open: 171.22,
 366 |             high: 173.12,
 367 |             low: 168.6,
 368 |             close: 170.22,
 369 |           },
 370 |           {
 371 |             time: "2018-12-31",
 372 |             open: 171.47,
 373 |             high: 173.24,
 374 |             low: 170.65,
 375 |             close: 171.82,
 376 |           },
 377 |           {
 378 |             time: "2019-01-02",
 379 |             open: 169.71,
 380 |             high: 173.18,
 381 |             low: 169.05,
 382 |             close: 172.41,
 383 |           },
 384 |           {
 385 |             time: "2019-01-03",
 386 |             open: 171.84,
 387 |             high: 171.84,
 388 |             low: 168.21,
 389 |             close: 168.61,
 390 |           },
 391 |           {
 392 |             time: "2019-01-04",
 393 |             open: 170.18,
 394 |             high: 174.74,
 395 |             low: 169.52,
 396 |             close: 173.62,
 397 |           },
 398 |           {
 399 |             time: "2019-01-07",
 400 |             open: 173.83,
 401 |             high: 178.18,
 402 |             low: 173.83,
 403 |             close: 177.04,
 404 |           },
 405 |           {
 406 |             time: "2019-01-08",
 407 |             open: 178.57,
 408 |             high: 179.59,
 409 |             low: 175.61,
 410 |             close: 177.89,
 411 |           },
 412 |           {
 413 |             time: "2019-01-09",
 414 |             open: 177.87,
 415 |             high: 181.27,
 416 |             low: 177.1,
 417 |             close: 179.73,
 418 |           },
 419 |           {
 420 |             time: "2019-01-10",
 421 |             open: 178.03,
 422 |             high: 179.24,
 423 |             low: 176.34,
 424 |             close: 179.06,
 425 |           },
 426 |           {
 427 |             time: "2019-01-11",
 428 |             open: 177.93,
 429 |             high: 180.26,
 430 |             low: 177.12,
 431 |             close: 179.41,
 432 |           },
 433 |           {
 434 |             time: "2019-01-14",
 435 |             open: 177.59,
 436 |             high: 179.23,
 437 |             low: 176.9,
 438 |             close: 178.81,
 439 |           },
 440 |           {
 441 |             time: "2019-01-15",
 442 |             open: 176.08,
 443 |             high: 177.82,
 444 |             low: 175.2,
 445 |             close: 176.47,
 446 |           },
 447 |           {
 448 |             time: "2019-01-16",
 449 |             open: 177.09,
 450 |             high: 177.93,
 451 |             low: 175.86,
 452 |             close: 177.04,
 453 |           },
 454 |           {
 455 |             time: "2019-01-17",
 456 |             open: 174.01,
 457 |             high: 175.46,
 458 |             low: 172.0,
 459 |             close: 174.87,
 460 |           },
 461 |           {
 462 |             time: "2019-01-18",
 463 |             open: 176.98,
 464 |             high: 180.04,
 465 |             low: 176.18,
 466 |             close: 179.58,
 467 |           },
 468 |           {
 469 |             time: "2019-01-22",
 470 |             open: 177.49,
 471 |             high: 178.6,
 472 |             low: 175.36,
 473 |             close: 177.11,
 474 |           },
 475 |           {
 476 |             time: "2019-01-23",
 477 |             open: 176.59,
 478 |             high: 178.06,
 479 |             low: 174.53,
 480 |             close: 176.89,
 481 |           },
 482 |           {
 483 |             time: "2019-01-24",
 484 |             open: 177.0,
 485 |             high: 177.53,
 486 |             low: 175.3,
 487 |             close: 177.29,
 488 |           },
 489 |           {
 490 |             time: "2019-01-25",
 491 |             open: 179.78,
 492 |             high: 180.87,
 493 |             low: 178.61,
 494 |             close: 180.4,
 495 |           },
 496 |           {
 497 |             time: "2019-01-28",
 498 |             open: 178.97,
 499 |             high: 179.99,
 500 |             low: 177.41,
 501 |             close: 179.83,
 502 |           },
 503 |           {
 504 |             time: "2019-01-29",
 505 |             open: 178.96,
 506 |             high: 180.15,
 507 |             low: 178.09,
 508 |             close: 179.69,
 509 |           },
 510 |           {
 511 |             time: "2019-01-30",
 512 |             open: 180.47,
 513 |             high: 184.2,
 514 |             low: 179.78,
 515 |             close: 182.18,
 516 |           },
 517 |           {
 518 |             time: "2019-01-31",
 519 |             open: 181.5,
 520 |             high: 184.67,
 521 |             low: 181.06,
 522 |             close: 183.53,
 523 |           },
 524 |           {
 525 |             time: "2019-02-01",
 526 |             open: 184.03,
 527 |             high: 185.15,
 528 |             low: 182.83,
 529 |             close: 184.37,
 530 |           },
 531 |           {
 532 |             time: "2019-02-04",
 533 |             open: 184.3,
 534 |             high: 186.43,
 535 |             low: 183.84,
 536 |             close: 186.43,
 537 |           },
 538 |           {
 539 |             time: "2019-02-05",
 540 |             open: 186.89,
 541 |             high: 186.99,
 542 |             low: 184.69,
 543 |             close: 186.39,
 544 |           },
 545 |           {
 546 |             time: "2019-02-06",
 547 |             open: 186.69,
 548 |             high: 186.69,
 549 |             low: 184.06,
 550 |             close: 184.72,
 551 |           },
 552 |           {
 553 |             time: "2019-02-07",
 554 |             open: 183.74,
 555 |             high: 184.92,
 556 |             low: 182.45,
 557 |             close: 184.07,
 558 |           },
 559 |           {
 560 |             time: "2019-02-08",
 561 |             open: 183.05,
 562 |             high: 184.58,
 563 |             low: 182.72,
 564 |             close: 184.54,
 565 |           },
 566 |           {
 567 |             time: "2019-02-11",
 568 |             open: 185.0,
 569 |             high: 185.42,
 570 |             low: 182.75,
 571 |             close: 182.92,
 572 |           },
 573 |           {
 574 |             time: "2019-02-12",
 575 |             open: 183.84,
 576 |             high: 186.4,
 577 |             low: 183.52,
 578 |             close: 185.52,
 579 |           },
 580 |           {
 581 |             time: "2019-02-13",
 582 |             open: 186.3,
 583 |             high: 188.68,
 584 |             low: 185.92,
 585 |             close: 188.41,
 586 |           },
 587 |           {
 588 |             time: "2019-02-14",
 589 |             open: 187.5,
 590 |             high: 188.93,
 591 |             low: 186.0,
 592 |             close: 187.71,
 593 |           },
 594 |           {
 595 |             time: "2019-02-15",
 596 |             open: 189.87,
 597 |             high: 192.62,
 598 |             low: 189.05,
 599 |             close: 192.39,
 600 |           },
 601 |           {
 602 |             time: "2019-02-19",
 603 |             open: 191.71,
 604 |             high: 193.19,
 605 |             low: 191.28,
 606 |             close: 192.33,
 607 |           },
 608 |           {
 609 |             time: "2019-02-20",
 610 |             open: 192.39,
 611 |             high: 192.4,
 612 |             low: 191.11,
 613 |             close: 191.85,
 614 |           },
 615 |           {
 616 |             time: "2019-02-21",
 617 |             open: 191.85,
 618 |             high: 192.37,
 619 |             low: 190.61,
 620 |             close: 191.82,
 621 |           },
 622 |           {
 623 |             time: "2019-02-22",
 624 |             open: 191.69,
 625 |             high: 192.54,
 626 |             low: 191.62,
 627 |             close: 192.39,
 628 |           },
 629 |           {
 630 |             time: "2019-02-25",
 631 |             open: 192.75,
 632 |             high: 193.42,
 633 |             low: 189.96,
 634 |             close: 189.98,
 635 |           },
 636 |           {
 637 |             time: "2019-02-26",
 638 |             open: 185.59,
 639 |             high: 188.47,
 640 |             low: 182.8,
 641 |             close: 188.3,
 642 |           },
 643 |           {
 644 |             time: "2019-02-27",
 645 |             open: 187.9,
 646 |             high: 188.5,
 647 |             low: 183.21,
 648 |             close: 183.67,
 649 |           },
 650 |           {
 651 |             time: "2019-02-28",
 652 |             open: 183.6,
 653 |             high: 185.19,
 654 |             low: 183.11,
 655 |             close: 185.14,
 656 |           },
 657 |           {
 658 |             time: "2019-03-01",
 659 |             open: 185.82,
 660 |             high: 186.56,
 661 |             low: 182.86,
 662 |             close: 185.17,
 663 |           },
 664 |           {
 665 |             time: "2019-03-04",
 666 |             open: 186.2,
 667 |             high: 186.24,
 668 |             low: 182.1,
 669 |             close: 183.81,
 670 |           },
 671 |           {
 672 |             time: "2019-03-05",
 673 |             open: 184.24,
 674 |             high: 185.12,
 675 |             low: 183.25,
 676 |             close: 184.0,
 677 |           },
 678 |           {
 679 |             time: "2019-03-06",
 680 |             open: 184.53,
 681 |             high: 184.97,
 682 |             low: 183.84,
 683 |             close: 184.45,
 684 |           },
 685 |           {
 686 |             time: "2019-03-07",
 687 |             open: 184.39,
 688 |             high: 184.62,
 689 |             low: 181.58,
 690 |             close: 182.51,
 691 |           },
 692 |           {
 693 |             time: "2019-03-08",
 694 |             open: 181.49,
 695 |             high: 181.91,
 696 |             low: 179.52,
 697 |             close: 181.23,
 698 |           },
 699 |           {
 700 |             time: "2019-03-11",
 701 |             open: 182.0,
 702 |             high: 183.2,
 703 |             low: 181.2,
 704 |             close: 182.44,
 705 |           },
 706 |           {
 707 |             time: "2019-03-12",
 708 |             open: 183.43,
 709 |             high: 184.27,
 710 |             low: 182.33,
 711 |             close: 184.0,
 712 |           },
 713 |           {
 714 |             time: "2019-03-13",
 715 |             open: 183.24,
 716 |             high: 183.78,
 717 |             low: 181.08,
 718 |             close: 181.14,
 719 |           },
 720 |           {
 721 |             time: "2019-03-14",
 722 |             open: 181.28,
 723 |             high: 181.74,
 724 |             low: 180.5,
 725 |             close: 181.61,
 726 |           },
 727 |           {
 728 |             time: "2019-03-15",
 729 |             open: 182.3,
 730 |             high: 182.49,
 731 |             low: 179.57,
 732 |             close: 182.23,
 733 |           },
 734 |           {
 735 |             time: "2019-03-18",
 736 |             open: 182.53,
 737 |             high: 183.48,
 738 |             low: 182.33,
 739 |             close: 183.42,
 740 |           },
 741 |           {
 742 |             time: "2019-03-19",
 743 |             open: 184.19,
 744 |             high: 185.82,
 745 |             low: 183.48,
 746 |             close: 184.13,
 747 |           },
 748 |           {
 749 |             time: "2019-03-20",
 750 |             open: 184.3,
 751 |             high: 187.12,
 752 |             low: 183.43,
 753 |             close: 186.1,
 754 |           },
 755 |           {
 756 |             time: "2019-03-21",
 757 |             open: 185.5,
 758 |             high: 190.0,
 759 |             low: 185.5,
 760 |             close: 189.97,
 761 |           },
 762 |           {
 763 |             time: "2019-03-22",
 764 |             open: 189.31,
 765 |             high: 192.05,
 766 |             low: 188.67,
 767 |             close: 188.75,
 768 |           },
 769 |           {
 770 |             time: "2019-03-25",
 771 |             open: 188.75,
 772 |             high: 191.71,
 773 |             low: 188.51,
 774 |             close: 189.68,
 775 |           },
 776 |           {
 777 |             time: "2019-03-26",
 778 |             open: 190.69,
 779 |             high: 192.19,
 780 |             low: 188.74,
 781 |             close: 189.34,
 782 |           },
 783 |           {
 784 |             time: "2019-03-27",
 785 |             open: 189.65,
 786 |             high: 191.61,
 787 |             low: 188.39,
 788 |             close: 189.25,
 789 |           },
 790 |           {
 791 |             time: "2019-03-28",
 792 |             open: 189.91,
 793 |             high: 191.4,
 794 |             low: 189.16,
 795 |             close: 190.06,
 796 |           },
 797 |           {
 798 |             time: "2019-03-29",
 799 |             open: 190.85,
 800 |             high: 192.04,
 801 |             low: 190.14,
 802 |             close: 191.89,
 803 |           },
 804 |           {
 805 |             time: "2019-04-01",
 806 |             open: 192.99,
 807 |             high: 195.9,
 808 |             low: 192.85,
 809 |             close: 195.64,
 810 |           },
 811 |           {
 812 |             time: "2019-04-02",
 813 |             open: 195.5,
 814 |             high: 195.5,
 815 |             low: 194.01,
 816 |             close: 194.31,
 817 |           },
 818 |           {
 819 |             time: "2019-04-03",
 820 |             open: 194.98,
 821 |             high: 198.78,
 822 |             low: 194.11,
 823 |             close: 198.61,
 824 |           },
 825 |           {
 826 |             time: "2019-04-04",
 827 |             open: 199.0,
 828 |             high: 200.49,
 829 |             low: 198.02,
 830 |             close: 200.45,
 831 |           },
 832 |           {
 833 |             time: "2019-04-05",
 834 |             open: 200.86,
 835 |             high: 203.13,
 836 |             low: 200.61,
 837 |             close: 202.06,
 838 |           },
 839 |           {
 840 |             time: "2019-04-08",
 841 |             open: 201.37,
 842 |             high: 203.79,
 843 |             low: 201.24,
 844 |             close: 203.55,
 845 |           },
 846 |           {
 847 |             time: "2019-04-09",
 848 |             open: 202.26,
 849 |             high: 202.71,
 850 |             low: 200.46,
 851 |             close: 200.9,
 852 |           },
 853 |           {
 854 |             time: "2019-04-10",
 855 |             open: 201.26,
 856 |             high: 201.6,
 857 |             low: 198.02,
 858 |             close: 199.43,
 859 |           },
 860 |           {
 861 |             time: "2019-04-11",
 862 |             open: 199.9,
 863 |             high: 201.5,
 864 |             low: 199.03,
 865 |             close: 201.48,
 866 |           },
 867 |           {
 868 |             time: "2019-04-12",
 869 |             open: 202.13,
 870 |             high: 204.26,
 871 |             low: 202.13,
 872 |             close: 203.85,
 873 |           },
 874 |           {
 875 |             time: "2019-04-15",
 876 |             open: 204.16,
 877 |             high: 205.14,
 878 |             low: 203.4,
 879 |             close: 204.86,
 880 |           },
 881 |           {
 882 |             time: "2019-04-16",
 883 |             open: 205.25,
 884 |             high: 205.99,
 885 |             low: 204.29,
 886 |             close: 204.47,
 887 |           },
 888 |           {
 889 |             time: "2019-04-17",
 890 |             open: 205.34,
 891 |             high: 206.84,
 892 |             low: 205.32,
 893 |             close: 206.55,
 894 |           },
 895 |           {
 896 |             time: "2019-04-18",
 897 |             open: 206.02,
 898 |             high: 207.78,
 899 |             low: 205.1,
 900 |             close: 205.66,
 901 |           },
 902 |           {
 903 |             time: "2019-04-22",
 904 |             open: 204.11,
 905 |             high: 206.25,
 906 |             low: 204.0,
 907 |             close: 204.78,
 908 |           },
 909 |           {
 910 |             time: "2019-04-23",
 911 |             open: 205.14,
 912 |             high: 207.33,
 913 |             low: 203.43,
 914 |             close: 206.05,
 915 |           },
 916 |           {
 917 |             time: "2019-04-24",
 918 |             open: 206.16,
 919 |             high: 208.29,
 920 |             low: 205.54,
 921 |             close: 206.72,
 922 |           },
 923 |           {
 924 |             time: "2019-04-25",
 925 |             open: 206.01,
 926 |             high: 207.72,
 927 |             low: 205.06,
 928 |             close: 206.5,
 929 |           },
 930 |           {
 931 |             time: "2019-04-26",
 932 |             open: 205.88,
 933 |             high: 206.14,
 934 |             low: 203.34,
 935 |             close: 203.61,
 936 |           },
 937 |           {
 938 |             time: "2019-04-29",
 939 |             open: 203.31,
 940 |             high: 203.8,
 941 |             low: 200.34,
 942 |             close: 202.16,
 943 |           },
 944 |           {
 945 |             time: "2019-04-30",
 946 |             open: 201.55,
 947 |             high: 203.75,
 948 |             low: 200.79,
 949 |             close: 203.7,
 950 |           },
 951 |           {
 952 |             time: "2019-05-01",
 953 |             open: 203.2,
 954 |             high: 203.52,
 955 |             low: 198.66,
 956 |             close: 198.8,
 957 |           },
 958 |           {
 959 |             time: "2019-05-02",
 960 |             open: 199.3,
 961 |             high: 201.06,
 962 |             low: 198.8,
 963 |             close: 201.01,
 964 |           },
 965 |           {
 966 |             time: "2019-05-03",
 967 |             open: 202.0,
 968 |             high: 202.31,
 969 |             low: 200.32,
 970 |             close: 200.56,
 971 |           },
 972 |           {
 973 |             time: "2019-05-06",
 974 |             open: 198.74,
 975 |             high: 199.93,
 976 |             low: 198.31,
 977 |             close: 199.63,
 978 |           },
 979 |           {
 980 |             time: "2019-05-07",
 981 |             open: 196.75,
 982 |             high: 197.65,
 983 |             low: 192.96,
 984 |             close: 194.77,
 985 |           },
 986 |           {
 987 |             time: "2019-05-08",
 988 |             open: 194.49,
 989 |             high: 196.61,
 990 |             low: 193.68,
 991 |             close: 195.17,
 992 |           },
 993 |           {
 994 |             time: "2019-05-09",
 995 |             open: 193.31,
 996 |             high: 195.08,
 997 |             low: 191.59,
 998 |             close: 194.58,
 999 |           },
1000 |           {
1001 |             time: "2019-05-10",
1002 |             open: 193.21,
1003 |             high: 195.49,
1004 |             low: 190.01,
1005 |             close: 194.58,
1006 |           },
1007 |           {
1008 |             time: "2019-05-13",
1009 |             open: 191.0,
1010 |             high: 191.66,
1011 |             low: 189.14,
1012 |             close: 190.34,
1013 |           },
1014 |           {
1015 |             time: "2019-05-14",
1016 |             open: 190.5,
1017 |             high: 192.76,
1018 |             low: 190.01,
1019 |             close: 191.62,
1020 |           },
1021 |           {
1022 |             time: "2019-05-15",
1023 |             open: 190.81,
1024 |             high: 192.81,
1025 |             low: 190.27,
1026 |             close: 191.76,
1027 |           },
1028 |           {
1029 |             time: "2019-05-16",
1030 |             open: 192.47,
1031 |             high: 194.96,
1032 |             low: 192.2,
1033 |             close: 192.38,
1034 |           },
1035 |           {
1036 |             time: "2019-05-17",
1037 |             open: 190.86,
1038 |             high: 194.5,
1039 |             low: 190.75,
1040 |             close: 192.58,
1041 |           },
1042 |           {
1043 |             time: "2019-05-20",
1044 |             open: 191.13,
1045 |             high: 192.86,
1046 |             low: 190.61,
1047 |             close: 190.95,
1048 |           },
1049 |           {
1050 |             time: "2019-05-21",
1051 |             open: 187.13,
1052 |             high: 192.52,
1053 |             low: 186.34,
1054 |             close: 191.45,
1055 |           },
1056 |           {
1057 |             time: "2019-05-22",
1058 |             open: 190.49,
1059 |             high: 192.22,
1060 |             low: 188.05,
1061 |             close: 188.91,
1062 |           },
1063 |           {
1064 |             time: "2019-05-23",
1065 |             open: 188.45,
1066 |             high: 192.54,
1067 |             low: 186.27,
1068 |             close: 192.0,
1069 |           },
1070 |           {
1071 |             time: "2019-05-24",
1072 |             open: 192.54,
1073 |             high: 193.86,
1074 |             low: 190.41,
1075 |             close: 193.59,
1076 |           },
1077 |         ];
1078 |       }
1079 | 
1080 |       // Create the Lightweight Chart within the container element
1081 |       const chart = LightweightCharts.createChart(
1082 |         document.getElementById('container'),
1083 |         {
1084 |           layout: {
1085 |             background: { color: "#222" },
1086 |             textColor: "#C3BCDB",
1087 |           },
1088 |           grid: {
1089 |             vertLines: { color: "#444" },
1090 |             horzLines: { color: "#444" },
1091 |           },
1092 |         }
1093 |       );
1094 | 
1095 |       // Setting the border color for the vertical axis
1096 |       chart.priceScale().applyOptions({
1097 |         borderColor: "#71649C",
1098 |       });
1099 | 
1100 |       // Setting the border color for the horizontal axis
1101 |       chart.timeScale().applyOptions({
1102 |         borderColor: "#71649C",
1103 |       });
1104 | 
1105 |       // Adjust the starting bar width (essentially the horizontal zoom)
1106 |       chart.timeScale().applyOptions({
1107 |         barSpacing: 10,
1108 |       });
1109 | 
1110 |       // Get the current users primary locale
1111 |       const currentLocale = window.navigator.languages[0];
1112 |       // Create a number format using Intl.NumberFormat
1113 |       const myPriceFormatter = Intl.NumberFormat(currentLocale, {
1114 |         style: "currency",
1115 |         currency: "EUR", // Currency for data points
1116 |       }).format;
1117 | 
1118 |       // Apply the custom priceFormatter to the chart
1119 |       chart.applyOptions({
1120 |         localization: {
1121 |           priceFormatter: myPriceFormatter,
1122 |         },
1123 |       });
1124 | 
1125 |       // Generate sample data to use within a candlestick series
1126 |       const candleStickData = generateCandlestickData();
1127 | 
1128 |       // Create the Main Series (Candlesticks)
1129 |       const mainSeries = chart.addSeries(LightweightCharts.CandlestickSeries);
1130 |       // Set the data for the Main Series
1131 |       mainSeries.setData(candleStickData);
1132 | 
1133 |       // Changing the Candlestick colors
1134 |       mainSeries.applyOptions({
1135 |         wickUpColor: "rgb(54, 116, 217)",
1136 |         upColor: "rgb(54, 116, 217)",
1137 |         wickDownColor: "rgb(225, 50, 85)",
1138 |         downColor: "rgb(225, 50, 85)",
1139 |         borderVisible: false,
1140 |       });
1141 | 
1142 |       // Adjust the options for the priceScale of the mainSeries
1143 |       mainSeries.priceScale().applyOptions({
1144 |         autoScale: false, // disables auto scaling based on visible content
1145 |         scaleMargins: {
1146 |           top: 0.1,
1147 |           bottom: 0.2,
1148 |         },
1149 |       });
1150 | 
1151 |       // Adding a window resize event handler to resize the chart when
1152 |       // the window size changes.
1153 |       // Note: for more advanced examples (when the chart doesn't fill the entire window)
1154 |       // you may need to use ResizeObserver -> https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver
1155 |       window.addEventListener("resize", () => {
1156 |         chart.resize(window.innerWidth, window.innerHeight);
1157 |       });
1158 |     </script>
1159 |   </body>
1160 | </html>
1161 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/assets/step7.html:
--------------------------------------------------------------------------------
   1 | <!DOCTYPE html>
   2 | <html>
   3 |   <head>
   4 |     <meta charset="UTF-8" />
   5 |     <meta
   6 |       name="viewport"
   7 |       content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0"
   8 |     />
   9 |     <title>Lightweight Charts™ Customization Tutorial</title>
  10 |     <!-- Adding the standalone version of Lightweight charts -->
  11 |     <script
  12 |       type="text/javascript"
  13 |       src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"
  14 |     ></script>
  15 |     <style>
  16 |       body {
  17 |         padding: 0;
  18 |         margin: 0;
  19 |         /* Add a background color to match the chart */
  20 |         background-color: #222;
  21 |       }
  22 |     </style>
  23 |   </head>
  24 | 
  25 |   <body>
  26 |     <div
  27 |       id="container"
  28 |       style="position: absolute; width: 100%; height: 100%"
  29 |     ></div>
  30 |     <script type="text/javascript">
  31 |       // Function to generate a sample set of Candlestick datapoints
  32 |       function generateCandlestickData() {
  33 |         return [
  34 |           {
  35 |             time: "2018-10-19",
  36 |             open: 180.34,
  37 |             high: 180.99,
  38 |             low: 178.57,
  39 |             close: 179.85,
  40 |           },
  41 |           {
  42 |             time: "2018-10-22",
  43 |             open: 180.82,
  44 |             high: 181.4,
  45 |             low: 177.56,
  46 |             close: 178.75,
  47 |           },
  48 |           {
  49 |             time: "2018-10-23",
  50 |             open: 175.77,
  51 |             high: 179.49,
  52 |             low: 175.44,
  53 |             close: 178.53,
  54 |           },
  55 |           {
  56 |             time: "2018-10-24",
  57 |             open: 178.58,
  58 |             high: 182.37,
  59 |             low: 176.31,
  60 |             close: 176.97,
  61 |           },
  62 |           {
  63 |             time: "2018-10-25",
  64 |             open: 177.52,
  65 |             high: 180.5,
  66 |             low: 176.83,
  67 |             close: 179.07,
  68 |           },
  69 |           {
  70 |             time: "2018-10-26",
  71 |             open: 176.88,
  72 |             high: 177.34,
  73 |             low: 170.91,
  74 |             close: 172.23,
  75 |           },
  76 |           {
  77 |             time: "2018-10-29",
  78 |             open: 173.74,
  79 |             high: 175.99,
  80 |             low: 170.95,
  81 |             close: 173.2,
  82 |           },
  83 |           {
  84 |             time: "2018-10-30",
  85 |             open: 173.16,
  86 |             high: 176.43,
  87 |             low: 172.64,
  88 |             close: 176.24,
  89 |           },
  90 |           {
  91 |             time: "2018-10-31",
  92 |             open: 177.98,
  93 |             high: 178.85,
  94 |             low: 175.59,
  95 |             close: 175.88,
  96 |           },
  97 |           {
  98 |             time: "2018-11-01",
  99 |             open: 176.84,
 100 |             high: 180.86,
 101 |             low: 175.9,
 102 |             close: 180.46,
 103 |           },
 104 |           {
 105 |             time: "2018-11-02",
 106 |             open: 182.47,
 107 |             high: 183.01,
 108 |             low: 177.39,
 109 |             close: 179.93,
 110 |           },
 111 |           {
 112 |             time: "2018-11-05",
 113 |             open: 181.02,
 114 |             high: 182.41,
 115 |             low: 179.3,
 116 |             close: 182.19,
 117 |           },
 118 |           {
 119 |             time: "2018-11-06",
 120 |             open: 181.93,
 121 |             high: 182.65,
 122 |             low: 180.05,
 123 |             close: 182.01,
 124 |           },
 125 |           {
 126 |             time: "2018-11-07",
 127 |             open: 183.79,
 128 |             high: 187.68,
 129 |             low: 182.06,
 130 |             close: 187.23,
 131 |           },
 132 |           {
 133 |             time: "2018-11-08",
 134 |             open: 187.13,
 135 |             high: 188.69,
 136 |             low: 185.72,
 137 |             close: 188.0,
 138 |           },
 139 |           {
 140 |             time: "2018-11-09",
 141 |             open: 188.32,
 142 |             high: 188.48,
 143 |             low: 184.96,
 144 |             close: 185.99,
 145 |           },
 146 |           {
 147 |             time: "2018-11-12",
 148 |             open: 185.23,
 149 |             high: 186.95,
 150 |             low: 179.02,
 151 |             close: 179.43,
 152 |           },
 153 |           {
 154 |             time: "2018-11-13",
 155 |             open: 177.3,
 156 |             high: 181.62,
 157 |             low: 172.85,
 158 |             close: 179.0,
 159 |           },
 160 |           {
 161 |             time: "2018-11-14",
 162 |             open: 182.61,
 163 |             high: 182.9,
 164 |             low: 179.15,
 165 |             close: 179.9,
 166 |           },
 167 |           {
 168 |             time: "2018-11-15",
 169 |             open: 179.01,
 170 |             high: 179.67,
 171 |             low: 173.61,
 172 |             close: 177.36,
 173 |           },
 174 |           {
 175 |             time: "2018-11-16",
 176 |             open: 173.99,
 177 |             high: 177.6,
 178 |             low: 173.51,
 179 |             close: 177.02,
 180 |           },
 181 |           {
 182 |             time: "2018-11-19",
 183 |             open: 176.71,
 184 |             high: 178.88,
 185 |             low: 172.3,
 186 |             close: 173.59,
 187 |           },
 188 |           {
 189 |             time: "2018-11-20",
 190 |             open: 169.25,
 191 |             high: 172.0,
 192 |             low: 167.0,
 193 |             close: 169.05,
 194 |           },
 195 |           {
 196 |             time: "2018-11-21",
 197 |             open: 170.0,
 198 |             high: 170.93,
 199 |             low: 169.15,
 200 |             close: 169.3,
 201 |           },
 202 |           {
 203 |             time: "2018-11-23",
 204 |             open: 169.39,
 205 |             high: 170.33,
 206 |             low: 168.47,
 207 |             close: 168.85,
 208 |           },
 209 |           {
 210 |             time: "2018-11-26",
 211 |             open: 170.2,
 212 |             high: 172.39,
 213 |             low: 168.87,
 214 |             close: 169.82,
 215 |           },
 216 |           {
 217 |             time: "2018-11-27",
 218 |             open: 169.11,
 219 |             high: 173.38,
 220 |             low: 168.82,
 221 |             close: 173.22,
 222 |           },
 223 |           {
 224 |             time: "2018-11-28",
 225 |             open: 172.91,
 226 |             high: 177.65,
 227 |             low: 170.62,
 228 |             close: 177.43,
 229 |           },
 230 |           {
 231 |             time: "2018-11-29",
 232 |             open: 176.8,
 233 |             high: 177.27,
 234 |             low: 174.92,
 235 |             close: 175.66,
 236 |           },
 237 |           {
 238 |             time: "2018-11-30",
 239 |             open: 175.75,
 240 |             high: 180.37,
 241 |             low: 175.11,
 242 |             close: 180.32,
 243 |           },
 244 |           {
 245 |             time: "2018-12-03",
 246 |             open: 183.29,
 247 |             high: 183.5,
 248 |             low: 179.35,
 249 |             close: 181.74,
 250 |           },
 251 |           {
 252 |             time: "2018-12-04",
 253 |             open: 181.06,
 254 |             high: 182.23,
 255 |             low: 174.55,
 256 |             close: 175.3,
 257 |           },
 258 |           {
 259 |             time: "2018-12-06",
 260 |             open: 173.5,
 261 |             high: 176.04,
 262 |             low: 170.46,
 263 |             close: 175.96,
 264 |           },
 265 |           {
 266 |             time: "2018-12-07",
 267 |             open: 175.35,
 268 |             high: 178.36,
 269 |             low: 172.24,
 270 |             close: 172.79,
 271 |           },
 272 |           {
 273 |             time: "2018-12-10",
 274 |             open: 173.39,
 275 |             high: 173.99,
 276 |             low: 167.73,
 277 |             close: 171.69,
 278 |           },
 279 |           {
 280 |             time: "2018-12-11",
 281 |             open: 174.3,
 282 |             high: 175.6,
 283 |             low: 171.24,
 284 |             close: 172.21,
 285 |           },
 286 |           {
 287 |             time: "2018-12-12",
 288 |             open: 173.75,
 289 |             high: 176.87,
 290 |             low: 172.81,
 291 |             close: 174.21,
 292 |           },
 293 |           {
 294 |             time: "2018-12-13",
 295 |             open: 174.31,
 296 |             high: 174.91,
 297 |             low: 172.07,
 298 |             close: 173.87,
 299 |           },
 300 |           {
 301 |             time: "2018-12-14",
 302 |             open: 172.98,
 303 |             high: 175.14,
 304 |             low: 171.95,
 305 |             close: 172.29,
 306 |           },
 307 |           {
 308 |             time: "2018-12-17",
 309 |             open: 171.51,
 310 |             high: 171.99,
 311 |             low: 166.93,
 312 |             close: 167.97,
 313 |           },
 314 |           {
 315 |             time: "2018-12-18",
 316 |             open: 168.9,
 317 |             high: 171.95,
 318 |             low: 168.5,
 319 |             close: 170.04,
 320 |           },
 321 |           {
 322 |             time: "2018-12-19",
 323 |             open: 170.92,
 324 |             high: 174.95,
 325 |             low: 166.77,
 326 |             close: 167.56,
 327 |           },
 328 |           {
 329 |             time: "2018-12-20",
 330 |             open: 166.28,
 331 |             high: 167.31,
 332 |             low: 162.23,
 333 |             close: 164.16,
 334 |           },
 335 |           {
 336 |             time: "2018-12-21",
 337 |             open: 162.81,
 338 |             high: 167.96,
 339 |             low: 160.17,
 340 |             close: 160.48,
 341 |           },
 342 |           {
 343 |             time: "2018-12-24",
 344 |             open: 160.16,
 345 |             high: 161.4,
 346 |             low: 158.09,
 347 |             close: 158.14,
 348 |           },
 349 |           {
 350 |             time: "2018-12-26",
 351 |             open: 159.46,
 352 |             high: 168.28,
 353 |             low: 159.44,
 354 |             close: 168.28,
 355 |           },
 356 |           {
 357 |             time: "2018-12-27",
 358 |             open: 166.44,
 359 |             high: 170.46,
 360 |             low: 163.36,
 361 |             close: 170.32,
 362 |           },
 363 |           {
 364 |             time: "2018-12-28",
 365 |             open: 171.22,
 366 |             high: 173.12,
 367 |             low: 168.6,
 368 |             close: 170.22,
 369 |           },
 370 |           {
 371 |             time: "2018-12-31",
 372 |             open: 171.47,
 373 |             high: 173.24,
 374 |             low: 170.65,
 375 |             close: 171.82,
 376 |           },
 377 |           {
 378 |             time: "2019-01-02",
 379 |             open: 169.71,
 380 |             high: 173.18,
 381 |             low: 169.05,
 382 |             close: 172.41,
 383 |           },
 384 |           {
 385 |             time: "2019-01-03",
 386 |             open: 171.84,
 387 |             high: 171.84,
 388 |             low: 168.21,
 389 |             close: 168.61,
 390 |           },
 391 |           {
 392 |             time: "2019-01-04",
 393 |             open: 170.18,
 394 |             high: 174.74,
 395 |             low: 169.52,
 396 |             close: 173.62,
 397 |           },
 398 |           {
 399 |             time: "2019-01-07",
 400 |             open: 173.83,
 401 |             high: 178.18,
 402 |             low: 173.83,
 403 |             close: 177.04,
 404 |           },
 405 |           {
 406 |             time: "2019-01-08",
 407 |             open: 178.57,
 408 |             high: 179.59,
 409 |             low: 175.61,
 410 |             close: 177.89,
 411 |           },
 412 |           {
 413 |             time: "2019-01-09",
 414 |             open: 177.87,
 415 |             high: 181.27,
 416 |             low: 177.1,
 417 |             close: 179.73,
 418 |           },
 419 |           {
 420 |             time: "2019-01-10",
 421 |             open: 178.03,
 422 |             high: 179.24,
 423 |             low: 176.34,
 424 |             close: 179.06,
 425 |           },
 426 |           {
 427 |             time: "2019-01-11",
 428 |             open: 177.93,
 429 |             high: 180.26,
 430 |             low: 177.12,
 431 |             close: 179.41,
 432 |           },
 433 |           {
 434 |             time: "2019-01-14",
 435 |             open: 177.59,
 436 |             high: 179.23,
 437 |             low: 176.9,
 438 |             close: 178.81,
 439 |           },
 440 |           {
 441 |             time: "2019-01-15",
 442 |             open: 176.08,
 443 |             high: 177.82,
 444 |             low: 175.2,
 445 |             close: 176.47,
 446 |           },
 447 |           {
 448 |             time: "2019-01-16",
 449 |             open: 177.09,
 450 |             high: 177.93,
 451 |             low: 175.86,
 452 |             close: 177.04,
 453 |           },
 454 |           {
 455 |             time: "2019-01-17",
 456 |             open: 174.01,
 457 |             high: 175.46,
 458 |             low: 172.0,
 459 |             close: 174.87,
 460 |           },
 461 |           {
 462 |             time: "2019-01-18",
 463 |             open: 176.98,
 464 |             high: 180.04,
 465 |             low: 176.18,
 466 |             close: 179.58,
 467 |           },
 468 |           {
 469 |             time: "2019-01-22",
 470 |             open: 177.49,
 471 |             high: 178.6,
 472 |             low: 175.36,
 473 |             close: 177.11,
 474 |           },
 475 |           {
 476 |             time: "2019-01-23",
 477 |             open: 176.59,
 478 |             high: 178.06,
 479 |             low: 174.53,
 480 |             close: 176.89,
 481 |           },
 482 |           {
 483 |             time: "2019-01-24",
 484 |             open: 177.0,
 485 |             high: 177.53,
 486 |             low: 175.3,
 487 |             close: 177.29,
 488 |           },
 489 |           {
 490 |             time: "2019-01-25",
 491 |             open: 179.78,
 492 |             high: 180.87,
 493 |             low: 178.61,
 494 |             close: 180.4,
 495 |           },
 496 |           {
 497 |             time: "2019-01-28",
 498 |             open: 178.97,
 499 |             high: 179.99,
 500 |             low: 177.41,
 501 |             close: 179.83,
 502 |           },
 503 |           {
 504 |             time: "2019-01-29",
 505 |             open: 178.96,
 506 |             high: 180.15,
 507 |             low: 178.09,
 508 |             close: 179.69,
 509 |           },
 510 |           {
 511 |             time: "2019-01-30",
 512 |             open: 180.47,
 513 |             high: 184.2,
 514 |             low: 179.78,
 515 |             close: 182.18,
 516 |           },
 517 |           {
 518 |             time: "2019-01-31",
 519 |             open: 181.5,
 520 |             high: 184.67,
 521 |             low: 181.06,
 522 |             close: 183.53,
 523 |           },
 524 |           {
 525 |             time: "2019-02-01",
 526 |             open: 184.03,
 527 |             high: 185.15,
 528 |             low: 182.83,
 529 |             close: 184.37,
 530 |           },
 531 |           {
 532 |             time: "2019-02-04",
 533 |             open: 184.3,
 534 |             high: 186.43,
 535 |             low: 183.84,
 536 |             close: 186.43,
 537 |           },
 538 |           {
 539 |             time: "2019-02-05",
 540 |             open: 186.89,
 541 |             high: 186.99,
 542 |             low: 184.69,
 543 |             close: 186.39,
 544 |           },
 545 |           {
 546 |             time: "2019-02-06",
 547 |             open: 186.69,
 548 |             high: 186.69,
 549 |             low: 184.06,
 550 |             close: 184.72,
 551 |           },
 552 |           {
 553 |             time: "2019-02-07",
 554 |             open: 183.74,
 555 |             high: 184.92,
 556 |             low: 182.45,
 557 |             close: 184.07,
 558 |           },
 559 |           {
 560 |             time: "2019-02-08",
 561 |             open: 183.05,
 562 |             high: 184.58,
 563 |             low: 182.72,
 564 |             close: 184.54,
 565 |           },
 566 |           {
 567 |             time: "2019-02-11",
 568 |             open: 185.0,
 569 |             high: 185.42,
 570 |             low: 182.75,
 571 |             close: 182.92,
 572 |           },
 573 |           {
 574 |             time: "2019-02-12",
 575 |             open: 183.84,
 576 |             high: 186.4,
 577 |             low: 183.52,
 578 |             close: 185.52,
 579 |           },
 580 |           {
 581 |             time: "2019-02-13",
 582 |             open: 186.3,
 583 |             high: 188.68,
 584 |             low: 185.92,
 585 |             close: 188.41,
 586 |           },
 587 |           {
 588 |             time: "2019-02-14",
 589 |             open: 187.5,
 590 |             high: 188.93,
 591 |             low: 186.0,
 592 |             close: 187.71,
 593 |           },
 594 |           {
 595 |             time: "2019-02-15",
 596 |             open: 189.87,
 597 |             high: 192.62,
 598 |             low: 189.05,
 599 |             close: 192.39,
 600 |           },
 601 |           {
 602 |             time: "2019-02-19",
 603 |             open: 191.71,
 604 |             high: 193.19,
 605 |             low: 191.28,
 606 |             close: 192.33,
 607 |           },
 608 |           {
 609 |             time: "2019-02-20",
 610 |             open: 192.39,
 611 |             high: 192.4,
 612 |             low: 191.11,
 613 |             close: 191.85,
 614 |           },
 615 |           {
 616 |             time: "2019-02-21",
 617 |             open: 191.85,
 618 |             high: 192.37,
 619 |             low: 190.61,
 620 |             close: 191.82,
 621 |           },
 622 |           {
 623 |             time: "2019-02-22",
 624 |             open: 191.69,
 625 |             high: 192.54,
 626 |             low: 191.62,
 627 |             close: 192.39,
 628 |           },
 629 |           {
 630 |             time: "2019-02-25",
 631 |             open: 192.75,
 632 |             high: 193.42,
 633 |             low: 189.96,
 634 |             close: 189.98,
 635 |           },
 636 |           {
 637 |             time: "2019-02-26",
 638 |             open: 185.59,
 639 |             high: 188.47,
 640 |             low: 182.8,
 641 |             close: 188.3,
 642 |           },
 643 |           {
 644 |             time: "2019-02-27",
 645 |             open: 187.9,
 646 |             high: 188.5,
 647 |             low: 183.21,
 648 |             close: 183.67,
 649 |           },
 650 |           {
 651 |             time: "2019-02-28",
 652 |             open: 183.6,
 653 |             high: 185.19,
 654 |             low: 183.11,
 655 |             close: 185.14,
 656 |           },
 657 |           {
 658 |             time: "2019-03-01",
 659 |             open: 185.82,
 660 |             high: 186.56,
 661 |             low: 182.86,
 662 |             close: 185.17,
 663 |           },
 664 |           {
 665 |             time: "2019-03-04",
 666 |             open: 186.2,
 667 |             high: 186.24,
 668 |             low: 182.1,
 669 |             close: 183.81,
 670 |           },
 671 |           {
 672 |             time: "2019-03-05",
 673 |             open: 184.24,
 674 |             high: 185.12,
 675 |             low: 183.25,
 676 |             close: 184.0,
 677 |           },
 678 |           {
 679 |             time: "2019-03-06",
 680 |             open: 184.53,
 681 |             high: 184.97,
 682 |             low: 183.84,
 683 |             close: 184.45,
 684 |           },
 685 |           {
 686 |             time: "2019-03-07",
 687 |             open: 184.39,
 688 |             high: 184.62,
 689 |             low: 181.58,
 690 |             close: 182.51,
 691 |           },
 692 |           {
 693 |             time: "2019-03-08",
 694 |             open: 181.49,
 695 |             high: 181.91,
 696 |             low: 179.52,
 697 |             close: 181.23,
 698 |           },
 699 |           {
 700 |             time: "2019-03-11",
 701 |             open: 182.0,
 702 |             high: 183.2,
 703 |             low: 181.2,
 704 |             close: 182.44,
 705 |           },
 706 |           {
 707 |             time: "2019-03-12",
 708 |             open: 183.43,
 709 |             high: 184.27,
 710 |             low: 182.33,
 711 |             close: 184.0,
 712 |           },
 713 |           {
 714 |             time: "2019-03-13",
 715 |             open: 183.24,
 716 |             high: 183.78,
 717 |             low: 181.08,
 718 |             close: 181.14,
 719 |           },
 720 |           {
 721 |             time: "2019-03-14",
 722 |             open: 181.28,
 723 |             high: 181.74,
 724 |             low: 180.5,
 725 |             close: 181.61,
 726 |           },
 727 |           {
 728 |             time: "2019-03-15",
 729 |             open: 182.3,
 730 |             high: 182.49,
 731 |             low: 179.57,
 732 |             close: 182.23,
 733 |           },
 734 |           {
 735 |             time: "2019-03-18",
 736 |             open: 182.53,
 737 |             high: 183.48,
 738 |             low: 182.33,
 739 |             close: 183.42,
 740 |           },
 741 |           {
 742 |             time: "2019-03-19",
 743 |             open: 184.19,
 744 |             high: 185.82,
 745 |             low: 183.48,
 746 |             close: 184.13,
 747 |           },
 748 |           {
 749 |             time: "2019-03-20",
 750 |             open: 184.3,
 751 |             high: 187.12,
 752 |             low: 183.43,
 753 |             close: 186.1,
 754 |           },
 755 |           {
 756 |             time: "2019-03-21",
 757 |             open: 185.5,
 758 |             high: 190.0,
 759 |             low: 185.5,
 760 |             close: 189.97,
 761 |           },
 762 |           {
 763 |             time: "2019-03-22",
 764 |             open: 189.31,
 765 |             high: 192.05,
 766 |             low: 188.67,
 767 |             close: 188.75,
 768 |           },
 769 |           {
 770 |             time: "2019-03-25",
 771 |             open: 188.75,
 772 |             high: 191.71,
 773 |             low: 188.51,
 774 |             close: 189.68,
 775 |           },
 776 |           {
 777 |             time: "2019-03-26",
 778 |             open: 190.69,
 779 |             high: 192.19,
 780 |             low: 188.74,
 781 |             close: 189.34,
 782 |           },
 783 |           {
 784 |             time: "2019-03-27",
 785 |             open: 189.65,
 786 |             high: 191.61,
 787 |             low: 188.39,
 788 |             close: 189.25,
 789 |           },
 790 |           {
 791 |             time: "2019-03-28",
 792 |             open: 189.91,
 793 |             high: 191.4,
 794 |             low: 189.16,
 795 |             close: 190.06,
 796 |           },
 797 |           {
 798 |             time: "2019-03-29",
 799 |             open: 190.85,
 800 |             high: 192.04,
 801 |             low: 190.14,
 802 |             close: 191.89,
 803 |           },
 804 |           {
 805 |             time: "2019-04-01",
 806 |             open: 192.99,
 807 |             high: 195.9,
 808 |             low: 192.85,
 809 |             close: 195.64,
 810 |           },
 811 |           {
 812 |             time: "2019-04-02",
 813 |             open: 195.5,
 814 |             high: 195.5,
 815 |             low: 194.01,
 816 |             close: 194.31,
 817 |           },
 818 |           {
 819 |             time: "2019-04-03",
 820 |             open: 194.98,
 821 |             high: 198.78,
 822 |             low: 194.11,
 823 |             close: 198.61,
 824 |           },
 825 |           {
 826 |             time: "2019-04-04",
 827 |             open: 199.0,
 828 |             high: 200.49,
 829 |             low: 198.02,
 830 |             close: 200.45,
 831 |           },
 832 |           {
 833 |             time: "2019-04-05",
 834 |             open: 200.86,
 835 |             high: 203.13,
 836 |             low: 200.61,
 837 |             close: 202.06,
 838 |           },
 839 |           {
 840 |             time: "2019-04-08",
 841 |             open: 201.37,
 842 |             high: 203.79,
 843 |             low: 201.24,
 844 |             close: 203.55,
 845 |           },
 846 |           {
 847 |             time: "2019-04-09",
 848 |             open: 202.26,
 849 |             high: 202.71,
 850 |             low: 200.46,
 851 |             close: 200.9,
 852 |           },
 853 |           {
 854 |             time: "2019-04-10",
 855 |             open: 201.26,
 856 |             high: 201.6,
 857 |             low: 198.02,
 858 |             close: 199.43,
 859 |           },
 860 |           {
 861 |             time: "2019-04-11",
 862 |             open: 199.9,
 863 |             high: 201.5,
 864 |             low: 199.03,
 865 |             close: 201.48,
 866 |           },
 867 |           {
 868 |             time: "2019-04-12",
 869 |             open: 202.13,
 870 |             high: 204.26,
 871 |             low: 202.13,
 872 |             close: 203.85,
 873 |           },
 874 |           {
 875 |             time: "2019-04-15",
 876 |             open: 204.16,
 877 |             high: 205.14,
 878 |             low: 203.4,
 879 |             close: 204.86,
 880 |           },
 881 |           {
 882 |             time: "2019-04-16",
 883 |             open: 205.25,
 884 |             high: 205.99,
 885 |             low: 204.29,
 886 |             close: 204.47,
 887 |           },
 888 |           {
 889 |             time: "2019-04-17",
 890 |             open: 205.34,
 891 |             high: 206.84,
 892 |             low: 205.32,
 893 |             close: 206.55,
 894 |           },
 895 |           {
 896 |             time: "2019-04-18",
 897 |             open: 206.02,
 898 |             high: 207.78,
 899 |             low: 205.1,
 900 |             close: 205.66,
 901 |           },
 902 |           {
 903 |             time: "2019-04-22",
 904 |             open: 204.11,
 905 |             high: 206.25,
 906 |             low: 204.0,
 907 |             close: 204.78,
 908 |           },
 909 |           {
 910 |             time: "2019-04-23",
 911 |             open: 205.14,
 912 |             high: 207.33,
 913 |             low: 203.43,
 914 |             close: 206.05,
 915 |           },
 916 |           {
 917 |             time: "2019-04-24",
 918 |             open: 206.16,
 919 |             high: 208.29,
 920 |             low: 205.54,
 921 |             close: 206.72,
 922 |           },
 923 |           {
 924 |             time: "2019-04-25",
 925 |             open: 206.01,
 926 |             high: 207.72,
 927 |             low: 205.06,
 928 |             close: 206.5,
 929 |           },
 930 |           {
 931 |             time: "2019-04-26",
 932 |             open: 205.88,
 933 |             high: 206.14,
 934 |             low: 203.34,
 935 |             close: 203.61,
 936 |           },
 937 |           {
 938 |             time: "2019-04-29",
 939 |             open: 203.31,
 940 |             high: 203.8,
 941 |             low: 200.34,
 942 |             close: 202.16,
 943 |           },
 944 |           {
 945 |             time: "2019-04-30",
 946 |             open: 201.55,
 947 |             high: 203.75,
 948 |             low: 200.79,
 949 |             close: 203.7,
 950 |           },
 951 |           {
 952 |             time: "2019-05-01",
 953 |             open: 203.2,
 954 |             high: 203.52,
 955 |             low: 198.66,
 956 |             close: 198.8,
 957 |           },
 958 |           {
 959 |             time: "2019-05-02",
 960 |             open: 199.3,
 961 |             high: 201.06,
 962 |             low: 198.8,
 963 |             close: 201.01,
 964 |           },
 965 |           {
 966 |             time: "2019-05-03",
 967 |             open: 202.0,
 968 |             high: 202.31,
 969 |             low: 200.32,
 970 |             close: 200.56,
 971 |           },
 972 |           {
 973 |             time: "2019-05-06",
 974 |             open: 198.74,
 975 |             high: 199.93,
 976 |             low: 198.31,
 977 |             close: 199.63,
 978 |           },
 979 |           {
 980 |             time: "2019-05-07",
 981 |             open: 196.75,
 982 |             high: 197.65,
 983 |             low: 192.96,
 984 |             close: 194.77,
 985 |           },
 986 |           {
 987 |             time: "2019-05-08",
 988 |             open: 194.49,
 989 |             high: 196.61,
 990 |             low: 193.68,
 991 |             close: 195.17,
 992 |           },
 993 |           {
 994 |             time: "2019-05-09",
 995 |             open: 193.31,
 996 |             high: 195.08,
 997 |             low: 191.59,
 998 |             close: 194.58,
 999 |           },
1000 |           {
1001 |             time: "2019-05-10",
1002 |             open: 193.21,
1003 |             high: 195.49,
1004 |             low: 190.01,
1005 |             close: 194.58,
1006 |           },
1007 |           {
1008 |             time: "2019-05-13",
1009 |             open: 191.0,
1010 |             high: 191.66,
1011 |             low: 189.14,
1012 |             close: 190.34,
1013 |           },
1014 |           {
1015 |             time: "2019-05-14",
1016 |             open: 190.5,
1017 |             high: 192.76,
1018 |             low: 190.01,
1019 |             close: 191.62,
1020 |           },
1021 |           {
1022 |             time: "2019-05-15",
1023 |             open: 190.81,
1024 |             high: 192.81,
1025 |             low: 190.27,
1026 |             close: 191.76,
1027 |           },
1028 |           {
1029 |             time: "2019-05-16",
1030 |             open: 192.47,
1031 |             high: 194.96,
1032 |             low: 192.2,
1033 |             close: 192.38,
1034 |           },
1035 |           {
1036 |             time: "2019-05-17",
1037 |             open: 190.86,
1038 |             high: 194.5,
1039 |             low: 190.75,
1040 |             close: 192.58,
1041 |           },
1042 |           {
1043 |             time: "2019-05-20",
1044 |             open: 191.13,
1045 |             high: 192.86,
1046 |             low: 190.61,
1047 |             close: 190.95,
1048 |           },
1049 |           {
1050 |             time: "2019-05-21",
1051 |             open: 187.13,
1052 |             high: 192.52,
1053 |             low: 186.34,
1054 |             close: 191.45,
1055 |           },
1056 |           {
1057 |             time: "2019-05-22",
1058 |             open: 190.49,
1059 |             high: 192.22,
1060 |             low: 188.05,
1061 |             close: 188.91,
1062 |           },
1063 |           {
1064 |             time: "2019-05-23",
1065 |             open: 188.45,
1066 |             high: 192.54,
1067 |             low: 186.27,
1068 |             close: 192.0,
1069 |           },
1070 |           {
1071 |             time: "2019-05-24",
1072 |             open: 192.54,
1073 |             high: 193.86,
1074 |             low: 190.41,
1075 |             close: 193.59,
1076 |           },
1077 |         ];
1078 |       }
1079 | 
1080 |       // Create the Lightweight Chart within the container element
1081 |       const chart = LightweightCharts.createChart(
1082 |         document.getElementById('container'),
1083 |         {
1084 |           layout: {
1085 |             background: { color: "#222" },
1086 |             textColor: "#C3BCDB",
1087 |           },
1088 |           grid: {
1089 |             vertLines: { color: "#444" },
1090 |             horzLines: { color: "#444" },
1091 |           },
1092 |         }
1093 |       );
1094 | 
1095 |       // Setting the border color for the vertical axis
1096 |       chart.priceScale().applyOptions({
1097 |         borderColor: "#71649C",
1098 |       });
1099 | 
1100 |       // Setting the border color for the horizontal axis
1101 |       chart.timeScale().applyOptions({
1102 |         borderColor: "#71649C",
1103 |       });
1104 | 
1105 |       // Adjust the starting bar width (essentially the horizontal zoom)
1106 |       chart.timeScale().applyOptions({
1107 |         barSpacing: 10,
1108 |       });
1109 | 
1110 |       // Get the current users primary locale
1111 |       const currentLocale = window.navigator.languages[0];
1112 |       // Create a number format using Intl.NumberFormat
1113 |       const myPriceFormatter = Intl.NumberFormat(currentLocale, {
1114 |         style: "currency",
1115 |         currency: "EUR", // Currency for data points
1116 |       }).format;
1117 | 
1118 |       // Apply the custom priceFormatter to the chart
1119 |       chart.applyOptions({
1120 |         localization: {
1121 |           priceFormatter: myPriceFormatter,
1122 |         },
1123 |       });
1124 | 
1125 |       // Customizing the Crosshair
1126 |       chart.applyOptions({
1127 |         crosshair: {
1128 |           // Change mode from default 'magnet' to 'normal'.
1129 |           // Allows the crosshair to move freely without snapping to datapoints
1130 |           mode: LightweightCharts.CrosshairMode.Normal,
1131 | 
1132 |           // Vertical crosshair line (showing Date in Label)
1133 |           vertLine: {
1134 |             width: 8,
1135 |             color: "#C3BCDB44",
1136 |             style: LightweightCharts.LineStyle.Solid,
1137 |             labelBackgroundColor: "#9B7DFF",
1138 |           },
1139 | 
1140 |           // Horizontal crosshair line (showing Price in Label)
1141 |           horzLine: {
1142 |             color: "#9B7DFF",
1143 |             labelBackgroundColor: "#9B7DFF",
1144 |           },
1145 |         },
1146 |       });
1147 | 
1148 |       // Generate sample data to use within a candlestick series
1149 |       const candleStickData = generateCandlestickData();
1150 | 
1151 |       // Create the Main Series (Candlesticks)
1152 |       const mainSeries = chart.addSeries(LightweightCharts.CandlestickSeries);
1153 |       // Set the data for the Main Series
1154 |       mainSeries.setData(candleStickData);
1155 | 
1156 |       // Changing the Candlestick colors
1157 |       mainSeries.applyOptions({
1158 |         wickUpColor: "rgb(54, 116, 217)",
1159 |         upColor: "rgb(54, 116, 217)",
1160 |         wickDownColor: "rgb(225, 50, 85)",
1161 |         downColor: "rgb(225, 50, 85)",
1162 |         borderVisible: false,
1163 |       });
1164 | 
1165 |       // Adjust the options for the priceScale of the mainSeries
1166 |       mainSeries.priceScale().applyOptions({
1167 |         autoScale: false, // disables auto scaling based on visible content
1168 |         scaleMargins: {
1169 |           top: 0.1,
1170 |           bottom: 0.2,
1171 |         },
1172 |       });
1173 | 
1174 |       // Adding a window resize event handler to resize the chart when
1175 |       // the window size changes.
1176 |       // Note: for more advanced examples (when the chart doesn't fill the entire window)
1177 |       // you may need to use ResizeObserver -> https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver
1178 |       window.addEventListener("resize", () => {
1179 |         chart.resize(window.innerWidth, window.innerHeight);
1180 |       });
1181 |     </script>
1182 |   </body>
1183 | </html>
1184 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/assets/step8.html:
--------------------------------------------------------------------------------
   1 | <!DOCTYPE html>
   2 | <html>
   3 |   <head>
   4 |     <meta charset="UTF-8" />
   5 |     <meta
   6 |       name="viewport"
   7 |       content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0"
   8 |     />
   9 |     <title>Lightweight Charts™ Customization Tutorial</title>
  10 |     <!-- Adding the standalone version of Lightweight charts -->
  11 |     <script
  12 |       type="text/javascript"
  13 |       src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"
  14 |     ></script>
  15 |     <style>
  16 |       body {
  17 |         padding: 0;
  18 |         margin: 0;
  19 |         /* Add a background color to match the chart */
  20 |         background-color: #222;
  21 |       }
  22 |     </style>
  23 |   </head>
  24 | 
  25 |   <body>
  26 |     <div
  27 |       id="container"
  28 |       style="position: absolute; width: 100%; height: 100%"
  29 |     ></div>
  30 |     <script type="text/javascript">
  31 |       // Function to generate a sample set of Candlestick datapoints
  32 |       function generateCandlestickData() {
  33 |         return [
  34 |           {
  35 |             time: "2018-10-19",
  36 |             open: 180.34,
  37 |             high: 180.99,
  38 |             low: 178.57,
  39 |             close: 179.85,
  40 |           },
  41 |           {
  42 |             time: "2018-10-22",
  43 |             open: 180.82,
  44 |             high: 181.4,
  45 |             low: 177.56,
  46 |             close: 178.75,
  47 |           },
  48 |           {
  49 |             time: "2018-10-23",
  50 |             open: 175.77,
  51 |             high: 179.49,
  52 |             low: 175.44,
  53 |             close: 178.53,
  54 |           },
  55 |           {
  56 |             time: "2018-10-24",
  57 |             open: 178.58,
  58 |             high: 182.37,
  59 |             low: 176.31,
  60 |             close: 176.97,
  61 |           },
  62 |           {
  63 |             time: "2018-10-25",
  64 |             open: 177.52,
  65 |             high: 180.5,
  66 |             low: 176.83,
  67 |             close: 179.07,
  68 |           },
  69 |           {
  70 |             time: "2018-10-26",
  71 |             open: 176.88,
  72 |             high: 177.34,
  73 |             low: 170.91,
  74 |             close: 172.23,
  75 |           },
  76 |           {
  77 |             time: "2018-10-29",
  78 |             open: 173.74,
  79 |             high: 175.99,
  80 |             low: 170.95,
  81 |             close: 173.2,
  82 |           },
  83 |           {
  84 |             time: "2018-10-30",
  85 |             open: 173.16,
  86 |             high: 176.43,
  87 |             low: 172.64,
  88 |             close: 176.24,
  89 |           },
  90 |           {
  91 |             time: "2018-10-31",
  92 |             open: 177.98,
  93 |             high: 178.85,
  94 |             low: 175.59,
  95 |             close: 175.88,
  96 |           },
  97 |           {
  98 |             time: "2018-11-01",
  99 |             open: 176.84,
 100 |             high: 180.86,
 101 |             low: 175.9,
 102 |             close: 180.46,
 103 |           },
 104 |           {
 105 |             time: "2018-11-02",
 106 |             open: 182.47,
 107 |             high: 183.01,
 108 |             low: 177.39,
 109 |             close: 179.93,
 110 |           },
 111 |           {
 112 |             time: "2018-11-05",
 113 |             open: 181.02,
 114 |             high: 182.41,
 115 |             low: 179.3,
 116 |             close: 182.19,
 117 |           },
 118 |           {
 119 |             time: "2018-11-06",
 120 |             open: 181.93,
 121 |             high: 182.65,
 122 |             low: 180.05,
 123 |             close: 182.01,
 124 |           },
 125 |           {
 126 |             time: "2018-11-07",
 127 |             open: 183.79,
 128 |             high: 187.68,
 129 |             low: 182.06,
 130 |             close: 187.23,
 131 |           },
 132 |           {
 133 |             time: "2018-11-08",
 134 |             open: 187.13,
 135 |             high: 188.69,
 136 |             low: 185.72,
 137 |             close: 188.0,
 138 |           },
 139 |           {
 140 |             time: "2018-11-09",
 141 |             open: 188.32,
 142 |             high: 188.48,
 143 |             low: 184.96,
 144 |             close: 185.99,
 145 |           },
 146 |           {
 147 |             time: "2018-11-12",
 148 |             open: 185.23,
 149 |             high: 186.95,
 150 |             low: 179.02,
 151 |             close: 179.43,
 152 |           },
 153 |           {
 154 |             time: "2018-11-13",
 155 |             open: 177.3,
 156 |             high: 181.62,
 157 |             low: 172.85,
 158 |             close: 179.0,
 159 |           },
 160 |           {
 161 |             time: "2018-11-14",
 162 |             open: 182.61,
 163 |             high: 182.9,
 164 |             low: 179.15,
 165 |             close: 179.9,
 166 |           },
 167 |           {
 168 |             time: "2018-11-15",
 169 |             open: 179.01,
 170 |             high: 179.67,
 171 |             low: 173.61,
 172 |             close: 177.36,
 173 |           },
 174 |           {
 175 |             time: "2018-11-16",
 176 |             open: 173.99,
 177 |             high: 177.6,
 178 |             low: 173.51,
 179 |             close: 177.02,
 180 |           },
 181 |           {
 182 |             time: "2018-11-19",
 183 |             open: 176.71,
 184 |             high: 178.88,
 185 |             low: 172.3,
 186 |             close: 173.59,
 187 |           },
 188 |           {
 189 |             time: "2018-11-20",
 190 |             open: 169.25,
 191 |             high: 172.0,
 192 |             low: 167.0,
 193 |             close: 169.05,
 194 |           },
 195 |           {
 196 |             time: "2018-11-21",
 197 |             open: 170.0,
 198 |             high: 170.93,
 199 |             low: 169.15,
 200 |             close: 169.3,
 201 |           },
 202 |           {
 203 |             time: "2018-11-23",
 204 |             open: 169.39,
 205 |             high: 170.33,
 206 |             low: 168.47,
 207 |             close: 168.85,
 208 |           },
 209 |           {
 210 |             time: "2018-11-26",
 211 |             open: 170.2,
 212 |             high: 172.39,
 213 |             low: 168.87,
 214 |             close: 169.82,
 215 |           },
 216 |           {
 217 |             time: "2018-11-27",
 218 |             open: 169.11,
 219 |             high: 173.38,
 220 |             low: 168.82,
 221 |             close: 173.22,
 222 |           },
 223 |           {
 224 |             time: "2018-11-28",
 225 |             open: 172.91,
 226 |             high: 177.65,
 227 |             low: 170.62,
 228 |             close: 177.43,
 229 |           },
 230 |           {
 231 |             time: "2018-11-29",
 232 |             open: 176.8,
 233 |             high: 177.27,
 234 |             low: 174.92,
 235 |             close: 175.66,
 236 |           },
 237 |           {
 238 |             time: "2018-11-30",
 239 |             open: 175.75,
 240 |             high: 180.37,
 241 |             low: 175.11,
 242 |             close: 180.32,
 243 |           },
 244 |           {
 245 |             time: "2018-12-03",
 246 |             open: 183.29,
 247 |             high: 183.5,
 248 |             low: 179.35,
 249 |             close: 181.74,
 250 |           },
 251 |           {
 252 |             time: "2018-12-04",
 253 |             open: 181.06,
 254 |             high: 182.23,
 255 |             low: 174.55,
 256 |             close: 175.3,
 257 |           },
 258 |           {
 259 |             time: "2018-12-06",
 260 |             open: 173.5,
 261 |             high: 176.04,
 262 |             low: 170.46,
 263 |             close: 175.96,
 264 |           },
 265 |           {
 266 |             time: "2018-12-07",
 267 |             open: 175.35,
 268 |             high: 178.36,
 269 |             low: 172.24,
 270 |             close: 172.79,
 271 |           },
 272 |           {
 273 |             time: "2018-12-10",
 274 |             open: 173.39,
 275 |             high: 173.99,
 276 |             low: 167.73,
 277 |             close: 171.69,
 278 |           },
 279 |           {
 280 |             time: "2018-12-11",
 281 |             open: 174.3,
 282 |             high: 175.6,
 283 |             low: 171.24,
 284 |             close: 172.21,
 285 |           },
 286 |           {
 287 |             time: "2018-12-12",
 288 |             open: 173.75,
 289 |             high: 176.87,
 290 |             low: 172.81,
 291 |             close: 174.21,
 292 |           },
 293 |           {
 294 |             time: "2018-12-13",
 295 |             open: 174.31,
 296 |             high: 174.91,
 297 |             low: 172.07,
 298 |             close: 173.87,
 299 |           },
 300 |           {
 301 |             time: "2018-12-14",
 302 |             open: 172.98,
 303 |             high: 175.14,
 304 |             low: 171.95,
 305 |             close: 172.29,
 306 |           },
 307 |           {
 308 |             time: "2018-12-17",
 309 |             open: 171.51,
 310 |             high: 171.99,
 311 |             low: 166.93,
 312 |             close: 167.97,
 313 |           },
 314 |           {
 315 |             time: "2018-12-18",
 316 |             open: 168.9,
 317 |             high: 171.95,
 318 |             low: 168.5,
 319 |             close: 170.04,
 320 |           },
 321 |           {
 322 |             time: "2018-12-19",
 323 |             open: 170.92,
 324 |             high: 174.95,
 325 |             low: 166.77,
 326 |             close: 167.56,
 327 |           },
 328 |           {
 329 |             time: "2018-12-20",
 330 |             open: 166.28,
 331 |             high: 167.31,
 332 |             low: 162.23,
 333 |             close: 164.16,
 334 |           },
 335 |           {
 336 |             time: "2018-12-21",
 337 |             open: 162.81,
 338 |             high: 167.96,
 339 |             low: 160.17,
 340 |             close: 160.48,
 341 |           },
 342 |           {
 343 |             time: "2018-12-24",
 344 |             open: 160.16,
 345 |             high: 161.4,
 346 |             low: 158.09,
 347 |             close: 158.14,
 348 |           },
 349 |           {
 350 |             time: "2018-12-26",
 351 |             open: 159.46,
 352 |             high: 168.28,
 353 |             low: 159.44,
 354 |             close: 168.28,
 355 |           },
 356 |           {
 357 |             time: "2018-12-27",
 358 |             open: 166.44,
 359 |             high: 170.46,
 360 |             low: 163.36,
 361 |             close: 170.32,
 362 |           },
 363 |           {
 364 |             time: "2018-12-28",
 365 |             open: 171.22,
 366 |             high: 173.12,
 367 |             low: 168.6,
 368 |             close: 170.22,
 369 |           },
 370 |           {
 371 |             time: "2018-12-31",
 372 |             open: 171.47,
 373 |             high: 173.24,
 374 |             low: 170.65,
 375 |             close: 171.82,
 376 |           },
 377 |           {
 378 |             time: "2019-01-02",
 379 |             open: 169.71,
 380 |             high: 173.18,
 381 |             low: 169.05,
 382 |             close: 172.41,
 383 |           },
 384 |           {
 385 |             time: "2019-01-03",
 386 |             open: 171.84,
 387 |             high: 171.84,
 388 |             low: 168.21,
 389 |             close: 168.61,
 390 |           },
 391 |           {
 392 |             time: "2019-01-04",
 393 |             open: 170.18,
 394 |             high: 174.74,
 395 |             low: 169.52,
 396 |             close: 173.62,
 397 |           },
 398 |           {
 399 |             time: "2019-01-07",
 400 |             open: 173.83,
 401 |             high: 178.18,
 402 |             low: 173.83,
 403 |             close: 177.04,
 404 |           },
 405 |           {
 406 |             time: "2019-01-08",
 407 |             open: 178.57,
 408 |             high: 179.59,
 409 |             low: 175.61,
 410 |             close: 177.89,
 411 |           },
 412 |           {
 413 |             time: "2019-01-09",
 414 |             open: 177.87,
 415 |             high: 181.27,
 416 |             low: 177.1,
 417 |             close: 179.73,
 418 |           },
 419 |           {
 420 |             time: "2019-01-10",
 421 |             open: 178.03,
 422 |             high: 179.24,
 423 |             low: 176.34,
 424 |             close: 179.06,
 425 |           },
 426 |           {
 427 |             time: "2019-01-11",
 428 |             open: 177.93,
 429 |             high: 180.26,
 430 |             low: 177.12,
 431 |             close: 179.41,
 432 |           },
 433 |           {
 434 |             time: "2019-01-14",
 435 |             open: 177.59,
 436 |             high: 179.23,
 437 |             low: 176.9,
 438 |             close: 178.81,
 439 |           },
 440 |           {
 441 |             time: "2019-01-15",
 442 |             open: 176.08,
 443 |             high: 177.82,
 444 |             low: 175.2,
 445 |             close: 176.47,
 446 |           },
 447 |           {
 448 |             time: "2019-01-16",
 449 |             open: 177.09,
 450 |             high: 177.93,
 451 |             low: 175.86,
 452 |             close: 177.04,
 453 |           },
 454 |           {
 455 |             time: "2019-01-17",
 456 |             open: 174.01,
 457 |             high: 175.46,
 458 |             low: 172.0,
 459 |             close: 174.87,
 460 |           },
 461 |           {
 462 |             time: "2019-01-18",
 463 |             open: 176.98,
 464 |             high: 180.04,
 465 |             low: 176.18,
 466 |             close: 179.58,
 467 |           },
 468 |           {
 469 |             time: "2019-01-22",
 470 |             open: 177.49,
 471 |             high: 178.6,
 472 |             low: 175.36,
 473 |             close: 177.11,
 474 |           },
 475 |           {
 476 |             time: "2019-01-23",
 477 |             open: 176.59,
 478 |             high: 178.06,
 479 |             low: 174.53,
 480 |             close: 176.89,
 481 |           },
 482 |           {
 483 |             time: "2019-01-24",
 484 |             open: 177.0,
 485 |             high: 177.53,
 486 |             low: 175.3,
 487 |             close: 177.29,
 488 |           },
 489 |           {
 490 |             time: "2019-01-25",
 491 |             open: 179.78,
 492 |             high: 180.87,
 493 |             low: 178.61,
 494 |             close: 180.4,
 495 |           },
 496 |           {
 497 |             time: "2019-01-28",
 498 |             open: 178.97,
 499 |             high: 179.99,
 500 |             low: 177.41,
 501 |             close: 179.83,
 502 |           },
 503 |           {
 504 |             time: "2019-01-29",
 505 |             open: 178.96,
 506 |             high: 180.15,
 507 |             low: 178.09,
 508 |             close: 179.69,
 509 |           },
 510 |           {
 511 |             time: "2019-01-30",
 512 |             open: 180.47,
 513 |             high: 184.2,
 514 |             low: 179.78,
 515 |             close: 182.18,
 516 |           },
 517 |           {
 518 |             time: "2019-01-31",
 519 |             open: 181.5,
 520 |             high: 184.67,
 521 |             low: 181.06,
 522 |             close: 183.53,
 523 |           },
 524 |           {
 525 |             time: "2019-02-01",
 526 |             open: 184.03,
 527 |             high: 185.15,
 528 |             low: 182.83,
 529 |             close: 184.37,
 530 |           },
 531 |           {
 532 |             time: "2019-02-04",
 533 |             open: 184.3,
 534 |             high: 186.43,
 535 |             low: 183.84,
 536 |             close: 186.43,
 537 |           },
 538 |           {
 539 |             time: "2019-02-05",
 540 |             open: 186.89,
 541 |             high: 186.99,
 542 |             low: 184.69,
 543 |             close: 186.39,
 544 |           },
 545 |           {
 546 |             time: "2019-02-06",
 547 |             open: 186.69,
 548 |             high: 186.69,
 549 |             low: 184.06,
 550 |             close: 184.72,
 551 |           },
 552 |           {
 553 |             time: "2019-02-07",
 554 |             open: 183.74,
 555 |             high: 184.92,
 556 |             low: 182.45,
 557 |             close: 184.07,
 558 |           },
 559 |           {
 560 |             time: "2019-02-08",
 561 |             open: 183.05,
 562 |             high: 184.58,
 563 |             low: 182.72,
 564 |             close: 184.54,
 565 |           },
 566 |           {
 567 |             time: "2019-02-11",
 568 |             open: 185.0,
 569 |             high: 185.42,
 570 |             low: 182.75,
 571 |             close: 182.92,
 572 |           },
 573 |           {
 574 |             time: "2019-02-12",
 575 |             open: 183.84,
 576 |             high: 186.4,
 577 |             low: 183.52,
 578 |             close: 185.52,
 579 |           },
 580 |           {
 581 |             time: "2019-02-13",
 582 |             open: 186.3,
 583 |             high: 188.68,
 584 |             low: 185.92,
 585 |             close: 188.41,
 586 |           },
 587 |           {
 588 |             time: "2019-02-14",
 589 |             open: 187.5,
 590 |             high: 188.93,
 591 |             low: 186.0,
 592 |             close: 187.71,
 593 |           },
 594 |           {
 595 |             time: "2019-02-15",
 596 |             open: 189.87,
 597 |             high: 192.62,
 598 |             low: 189.05,
 599 |             close: 192.39,
 600 |           },
 601 |           {
 602 |             time: "2019-02-19",
 603 |             open: 191.71,
 604 |             high: 193.19,
 605 |             low: 191.28,
 606 |             close: 192.33,
 607 |           },
 608 |           {
 609 |             time: "2019-02-20",
 610 |             open: 192.39,
 611 |             high: 192.4,
 612 |             low: 191.11,
 613 |             close: 191.85,
 614 |           },
 615 |           {
 616 |             time: "2019-02-21",
 617 |             open: 191.85,
 618 |             high: 192.37,
 619 |             low: 190.61,
 620 |             close: 191.82,
 621 |           },
 622 |           {
 623 |             time: "2019-02-22",
 624 |             open: 191.69,
 625 |             high: 192.54,
 626 |             low: 191.62,
 627 |             close: 192.39,
 628 |           },
 629 |           {
 630 |             time: "2019-02-25",
 631 |             open: 192.75,
 632 |             high: 193.42,
 633 |             low: 189.96,
 634 |             close: 189.98,
 635 |           },
 636 |           {
 637 |             time: "2019-02-26",
 638 |             open: 185.59,
 639 |             high: 188.47,
 640 |             low: 182.8,
 641 |             close: 188.3,
 642 |           },
 643 |           {
 644 |             time: "2019-02-27",
 645 |             open: 187.9,
 646 |             high: 188.5,
 647 |             low: 183.21,
 648 |             close: 183.67,
 649 |           },
 650 |           {
 651 |             time: "2019-02-28",
 652 |             open: 183.6,
 653 |             high: 185.19,
 654 |             low: 183.11,
 655 |             close: 185.14,
 656 |           },
 657 |           {
 658 |             time: "2019-03-01",
 659 |             open: 185.82,
 660 |             high: 186.56,
 661 |             low: 182.86,
 662 |             close: 185.17,
 663 |           },
 664 |           {
 665 |             time: "2019-03-04",
 666 |             open: 186.2,
 667 |             high: 186.24,
 668 |             low: 182.1,
 669 |             close: 183.81,
 670 |           },
 671 |           {
 672 |             time: "2019-03-05",
 673 |             open: 184.24,
 674 |             high: 185.12,
 675 |             low: 183.25,
 676 |             close: 184.0,
 677 |           },
 678 |           {
 679 |             time: "2019-03-06",
 680 |             open: 184.53,
 681 |             high: 184.97,
 682 |             low: 183.84,
 683 |             close: 184.45,
 684 |           },
 685 |           {
 686 |             time: "2019-03-07",
 687 |             open: 184.39,
 688 |             high: 184.62,
 689 |             low: 181.58,
 690 |             close: 182.51,
 691 |           },
 692 |           {
 693 |             time: "2019-03-08",
 694 |             open: 181.49,
 695 |             high: 181.91,
 696 |             low: 179.52,
 697 |             close: 181.23,
 698 |           },
 699 |           {
 700 |             time: "2019-03-11",
 701 |             open: 182.0,
 702 |             high: 183.2,
 703 |             low: 181.2,
 704 |             close: 182.44,
 705 |           },
 706 |           {
 707 |             time: "2019-03-12",
 708 |             open: 183.43,
 709 |             high: 184.27,
 710 |             low: 182.33,
 711 |             close: 184.0,
 712 |           },
 713 |           {
 714 |             time: "2019-03-13",
 715 |             open: 183.24,
 716 |             high: 183.78,
 717 |             low: 181.08,
 718 |             close: 181.14,
 719 |           },
 720 |           {
 721 |             time: "2019-03-14",
 722 |             open: 181.28,
 723 |             high: 181.74,
 724 |             low: 180.5,
 725 |             close: 181.61,
 726 |           },
 727 |           {
 728 |             time: "2019-03-15",
 729 |             open: 182.3,
 730 |             high: 182.49,
 731 |             low: 179.57,
 732 |             close: 182.23,
 733 |           },
 734 |           {
 735 |             time: "2019-03-18",
 736 |             open: 182.53,
 737 |             high: 183.48,
 738 |             low: 182.33,
 739 |             close: 183.42,
 740 |           },
 741 |           {
 742 |             time: "2019-03-19",
 743 |             open: 184.19,
 744 |             high: 185.82,
 745 |             low: 183.48,
 746 |             close: 184.13,
 747 |           },
 748 |           {
 749 |             time: "2019-03-20",
 750 |             open: 184.3,
 751 |             high: 187.12,
 752 |             low: 183.43,
 753 |             close: 186.1,
 754 |           },
 755 |           {
 756 |             time: "2019-03-21",
 757 |             open: 185.5,
 758 |             high: 190.0,
 759 |             low: 185.5,
 760 |             close: 189.97,
 761 |           },
 762 |           {
 763 |             time: "2019-03-22",
 764 |             open: 189.31,
 765 |             high: 192.05,
 766 |             low: 188.67,
 767 |             close: 188.75,
 768 |           },
 769 |           {
 770 |             time: "2019-03-25",
 771 |             open: 188.75,
 772 |             high: 191.71,
 773 |             low: 188.51,
 774 |             close: 189.68,
 775 |           },
 776 |           {
 777 |             time: "2019-03-26",
 778 |             open: 190.69,
 779 |             high: 192.19,
 780 |             low: 188.74,
 781 |             close: 189.34,
 782 |           },
 783 |           {
 784 |             time: "2019-03-27",
 785 |             open: 189.65,
 786 |             high: 191.61,
 787 |             low: 188.39,
 788 |             close: 189.25,
 789 |           },
 790 |           {
 791 |             time: "2019-03-28",
 792 |             open: 189.91,
 793 |             high: 191.4,
 794 |             low: 189.16,
 795 |             close: 190.06,
 796 |           },
 797 |           {
 798 |             time: "2019-03-29",
 799 |             open: 190.85,
 800 |             high: 192.04,
 801 |             low: 190.14,
 802 |             close: 191.89,
 803 |           },
 804 |           {
 805 |             time: "2019-04-01",
 806 |             open: 192.99,
 807 |             high: 195.9,
 808 |             low: 192.85,
 809 |             close: 195.64,
 810 |           },
 811 |           {
 812 |             time: "2019-04-02",
 813 |             open: 195.5,
 814 |             high: 195.5,
 815 |             low: 194.01,
 816 |             close: 194.31,
 817 |           },
 818 |           {
 819 |             time: "2019-04-03",
 820 |             open: 194.98,
 821 |             high: 198.78,
 822 |             low: 194.11,
 823 |             close: 198.61,
 824 |           },
 825 |           {
 826 |             time: "2019-04-04",
 827 |             open: 199.0,
 828 |             high: 200.49,
 829 |             low: 198.02,
 830 |             close: 200.45,
 831 |           },
 832 |           {
 833 |             time: "2019-04-05",
 834 |             open: 200.86,
 835 |             high: 203.13,
 836 |             low: 200.61,
 837 |             close: 202.06,
 838 |           },
 839 |           {
 840 |             time: "2019-04-08",
 841 |             open: 201.37,
 842 |             high: 203.79,
 843 |             low: 201.24,
 844 |             close: 203.55,
 845 |           },
 846 |           {
 847 |             time: "2019-04-09",
 848 |             open: 202.26,
 849 |             high: 202.71,
 850 |             low: 200.46,
 851 |             close: 200.9,
 852 |           },
 853 |           {
 854 |             time: "2019-04-10",
 855 |             open: 201.26,
 856 |             high: 201.6,
 857 |             low: 198.02,
 858 |             close: 199.43,
 859 |           },
 860 |           {
 861 |             time: "2019-04-11",
 862 |             open: 199.9,
 863 |             high: 201.5,
 864 |             low: 199.03,
 865 |             close: 201.48,
 866 |           },
 867 |           {
 868 |             time: "2019-04-12",
 869 |             open: 202.13,
 870 |             high: 204.26,
 871 |             low: 202.13,
 872 |             close: 203.85,
 873 |           },
 874 |           {
 875 |             time: "2019-04-15",
 876 |             open: 204.16,
 877 |             high: 205.14,
 878 |             low: 203.4,
 879 |             close: 204.86,
 880 |           },
 881 |           {
 882 |             time: "2019-04-16",
 883 |             open: 205.25,
 884 |             high: 205.99,
 885 |             low: 204.29,
 886 |             close: 204.47,
 887 |           },
 888 |           {
 889 |             time: "2019-04-17",
 890 |             open: 205.34,
 891 |             high: 206.84,
 892 |             low: 205.32,
 893 |             close: 206.55,
 894 |           },
 895 |           {
 896 |             time: "2019-04-18",
 897 |             open: 206.02,
 898 |             high: 207.78,
 899 |             low: 205.1,
 900 |             close: 205.66,
 901 |           },
 902 |           {
 903 |             time: "2019-04-22",
 904 |             open: 204.11,
 905 |             high: 206.25,
 906 |             low: 204.0,
 907 |             close: 204.78,
 908 |           },
 909 |           {
 910 |             time: "2019-04-23",
 911 |             open: 205.14,
 912 |             high: 207.33,
 913 |             low: 203.43,
 914 |             close: 206.05,
 915 |           },
 916 |           {
 917 |             time: "2019-04-24",
 918 |             open: 206.16,
 919 |             high: 208.29,
 920 |             low: 205.54,
 921 |             close: 206.72,
 922 |           },
 923 |           {
 924 |             time: "2019-04-25",
 925 |             open: 206.01,
 926 |             high: 207.72,
 927 |             low: 205.06,
 928 |             close: 206.5,
 929 |           },
 930 |           {
 931 |             time: "2019-04-26",
 932 |             open: 205.88,
 933 |             high: 206.14,
 934 |             low: 203.34,
 935 |             close: 203.61,
 936 |           },
 937 |           {
 938 |             time: "2019-04-29",
 939 |             open: 203.31,
 940 |             high: 203.8,
 941 |             low: 200.34,
 942 |             close: 202.16,
 943 |           },
 944 |           {
 945 |             time: "2019-04-30",
 946 |             open: 201.55,
 947 |             high: 203.75,
 948 |             low: 200.79,
 949 |             close: 203.7,
 950 |           },
 951 |           {
 952 |             time: "2019-05-01",
 953 |             open: 203.2,
 954 |             high: 203.52,
 955 |             low: 198.66,
 956 |             close: 198.8,
 957 |           },
 958 |           {
 959 |             time: "2019-05-02",
 960 |             open: 199.3,
 961 |             high: 201.06,
 962 |             low: 198.8,
 963 |             close: 201.01,
 964 |           },
 965 |           {
 966 |             time: "2019-05-03",
 967 |             open: 202.0,
 968 |             high: 202.31,
 969 |             low: 200.32,
 970 |             close: 200.56,
 971 |           },
 972 |           {
 973 |             time: "2019-05-06",
 974 |             open: 198.74,
 975 |             high: 199.93,
 976 |             low: 198.31,
 977 |             close: 199.63,
 978 |           },
 979 |           {
 980 |             time: "2019-05-07",
 981 |             open: 196.75,
 982 |             high: 197.65,
 983 |             low: 192.96,
 984 |             close: 194.77,
 985 |           },
 986 |           {
 987 |             time: "2019-05-08",
 988 |             open: 194.49,
 989 |             high: 196.61,
 990 |             low: 193.68,
 991 |             close: 195.17,
 992 |           },
 993 |           {
 994 |             time: "2019-05-09",
 995 |             open: 193.31,
 996 |             high: 195.08,
 997 |             low: 191.59,
 998 |             close: 194.58,
 999 |           },
1000 |           {
1001 |             time: "2019-05-10",
1002 |             open: 193.21,
1003 |             high: 195.49,
1004 |             low: 190.01,
1005 |             close: 194.58,
1006 |           },
1007 |           {
1008 |             time: "2019-05-13",
1009 |             open: 191.0,
1010 |             high: 191.66,
1011 |             low: 189.14,
1012 |             close: 190.34,
1013 |           },
1014 |           {
1015 |             time: "2019-05-14",
1016 |             open: 190.5,
1017 |             high: 192.76,
1018 |             low: 190.01,
1019 |             close: 191.62,
1020 |           },
1021 |           {
1022 |             time: "2019-05-15",
1023 |             open: 190.81,
1024 |             high: 192.81,
1025 |             low: 190.27,
1026 |             close: 191.76,
1027 |           },
1028 |           {
1029 |             time: "2019-05-16",
1030 |             open: 192.47,
1031 |             high: 194.96,
1032 |             low: 192.2,
1033 |             close: 192.38,
1034 |           },
1035 |           {
1036 |             time: "2019-05-17",
1037 |             open: 190.86,
1038 |             high: 194.5,
1039 |             low: 190.75,
1040 |             close: 192.58,
1041 |           },
1042 |           {
1043 |             time: "2019-05-20",
1044 |             open: 191.13,
1045 |             high: 192.86,
1046 |             low: 190.61,
1047 |             close: 190.95,
1048 |           },
1049 |           {
1050 |             time: "2019-05-21",
1051 |             open: 187.13,
1052 |             high: 192.52,
1053 |             low: 186.34,
1054 |             close: 191.45,
1055 |           },
1056 |           {
1057 |             time: "2019-05-22",
1058 |             open: 190.49,
1059 |             high: 192.22,
1060 |             low: 188.05,
1061 |             close: 188.91,
1062 |           },
1063 |           {
1064 |             time: "2019-05-23",
1065 |             open: 188.45,
1066 |             high: 192.54,
1067 |             low: 186.27,
1068 |             close: 192.0,
1069 |           },
1070 |           {
1071 |             time: "2019-05-24",
1072 |             open: 192.54,
1073 |             high: 193.86,
1074 |             low: 190.41,
1075 |             close: 193.59,
1076 |           },
1077 |         ];
1078 |       }
1079 | 
1080 |       // Create the Lightweight Chart within the container element
1081 |       const chart = LightweightCharts.createChart(
1082 |         document.getElementById('container'),
1083 |         {
1084 |           layout: {
1085 |             background: { color: "#222" },
1086 |             textColor: "#C3BCDB",
1087 |           },
1088 |           grid: {
1089 |             vertLines: { color: "#444" },
1090 |             horzLines: { color: "#444" },
1091 |           },
1092 |         }
1093 |       );
1094 | 
1095 |       // Setting the border color for the vertical axis
1096 |       chart.priceScale().applyOptions({
1097 |         borderColor: "#71649C",
1098 |       });
1099 | 
1100 |       // Setting the border color for the horizontal axis
1101 |       chart.timeScale().applyOptions({
1102 |         borderColor: "#71649C",
1103 |       });
1104 | 
1105 |       // Adjust the starting bar width (essentially the horizontal zoom)
1106 |       chart.timeScale().applyOptions({
1107 |         barSpacing: 10,
1108 |       });
1109 | 
1110 |       // Get the current users primary locale
1111 |       const currentLocale = window.navigator.languages[0];
1112 |       // Create a number format using Intl.NumberFormat
1113 |       const myPriceFormatter = Intl.NumberFormat(currentLocale, {
1114 |         style: "currency",
1115 |         currency: "EUR", // Currency for data points
1116 |       }).format;
1117 | 
1118 |       // Apply the custom priceFormatter to the chart
1119 |       chart.applyOptions({
1120 |         localization: {
1121 |           priceFormatter: myPriceFormatter,
1122 |         },
1123 |       });
1124 | 
1125 |       // Customizing the Crosshair
1126 |       chart.applyOptions({
1127 |         crosshair: {
1128 |           // Change mode from default 'magnet' to 'normal'.
1129 |           // Allows the crosshair to move freely without snapping to datapoints
1130 |           mode: LightweightCharts.CrosshairMode.Normal,
1131 | 
1132 |           // Vertical crosshair line (showing Date in Label)
1133 |           vertLine: {
1134 |             width: 8,
1135 |             color: "#C3BCDB44",
1136 |             style: LightweightCharts.LineStyle.Solid,
1137 |             labelBackgroundColor: "#9B7DFF",
1138 |           },
1139 | 
1140 |           // Horizontal crosshair line (showing Price in Label)
1141 |           horzLine: {
1142 |             color: "#9B7DFF",
1143 |             labelBackgroundColor: "#9B7DFF",
1144 |           },
1145 |         },
1146 |       });
1147 | 
1148 |       // Generate sample data to use within a candlestick series
1149 |       const candleStickData = generateCandlestickData();
1150 | 
1151 |       // Convert the candlestick data for use with a line series
1152 |       const lineData = candleStickData.map((datapoint) => ({
1153 |         time: datapoint.time,
1154 |         value: (datapoint.close + datapoint.open) / 2,
1155 |       }));
1156 | 
1157 |       // Add an area series to the chart,
1158 |       // Adding this before we add the candlestick chart
1159 |       // so that it will appear beneath the candlesticks
1160 |       const areaSeries = chart.addSeries(LightweightCharts.AreaSeries, {
1161 |         lastValueVisible: false, // hide the last value marker for this series
1162 |         crosshairMarkerVisible: false, // hide the crosshair marker for this series
1163 |         lineColor: "transparent", // hide the line
1164 |         topColor: "rgba(56, 33, 110,0.6)",
1165 |         bottomColor: "rgba(56, 33, 110, 0.1)",
1166 |       });
1167 |       // Set the data for the Area Series
1168 |       areaSeries.setData(lineData);
1169 | 
1170 |       // Create the Main Series (Candlesticks)
1171 |       const mainSeries = chart.addSeries(LightweightCharts.CandlestickSeries);
1172 |       // Set the data for the Main Series
1173 |       mainSeries.setData(candleStickData);
1174 | 
1175 |       // Changing the Candlestick colors
1176 |       mainSeries.applyOptions({
1177 |         wickUpColor: "rgb(54, 116, 217)",
1178 |         upColor: "rgb(54, 116, 217)",
1179 |         wickDownColor: "rgb(225, 50, 85)",
1180 |         downColor: "rgb(225, 50, 85)",
1181 |         borderVisible: false,
1182 |       });
1183 | 
1184 |       // Adjust the options for the priceScale of the mainSeries
1185 |       mainSeries.priceScale().applyOptions({
1186 |         autoScale: false, // disables auto scaling based on visible content
1187 |         scaleMargins: {
1188 |           top: 0.1,
1189 |           bottom: 0.2,
1190 |         },
1191 |       });
1192 | 
1193 |       // Adding a window resize event handler to resize the chart when
1194 |       // the window size changes.
1195 |       // Note: for more advanced examples (when the chart doesn't fill the entire window)
1196 |       // you may need to use ResizeObserver -> https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver
1197 |       window.addEventListener("resize", () => {
1198 |         chart.resize(window.innerWidth, window.innerHeight);
1199 |       });
1200 |     </script>
1201 |   </body>
1202 | </html>
1203 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/assets/step9.html:
--------------------------------------------------------------------------------
   1 | <!DOCTYPE html>
   2 | <html>
   3 |   <head>
   4 |     <meta charset="UTF-8" />
   5 |     <meta
   6 |       name="viewport"
   7 |       content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0"
   8 |     />
   9 |     <title>Lightweight Charts™ Customization Tutorial</title>
  10 |     <!-- Adding the standalone version of Lightweight charts -->
  11 |     <script
  12 |       type="text/javascript"
  13 |       src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"
  14 |     ></script>
  15 |     <style>
  16 |       body {
  17 |         padding: 0;
  18 |         margin: 0;
  19 |         /* Add a background color to match the chart */
  20 |         background-color: #222;
  21 |       }
  22 |     </style>
  23 |   </head>
  24 | 
  25 |   <body>
  26 |     <div
  27 |       id="container"
  28 |       style="position: absolute; width: 100%; height: 100%"
  29 |     ></div>
  30 |     <script type="text/javascript">
  31 |       // Function to generate a sample set of Candlestick datapoints
  32 |       function generateCandlestickData() {
  33 |         return [
  34 |           {
  35 |             time: "2018-10-19",
  36 |             open: 180.34,
  37 |             high: 180.99,
  38 |             low: 178.57,
  39 |             close: 179.85,
  40 |           },
  41 |           {
  42 |             time: "2018-10-22",
  43 |             open: 180.82,
  44 |             high: 181.4,
  45 |             low: 177.56,
  46 |             close: 178.75,
  47 |           },
  48 |           {
  49 |             time: "2018-10-23",
  50 |             open: 175.77,
  51 |             high: 179.49,
  52 |             low: 175.44,
  53 |             close: 178.53,
  54 |           },
  55 |           {
  56 |             time: "2018-10-24",
  57 |             open: 178.58,
  58 |             high: 182.37,
  59 |             low: 176.31,
  60 |             close: 176.97,
  61 |           },
  62 |           {
  63 |             time: "2018-10-25",
  64 |             open: 177.52,
  65 |             high: 180.5,
  66 |             low: 176.83,
  67 |             close: 179.07,
  68 |           },
  69 |           {
  70 |             time: "2018-10-26",
  71 |             open: 176.88,
  72 |             high: 177.34,
  73 |             low: 170.91,
  74 |             close: 172.23,
  75 |           },
  76 |           {
  77 |             time: "2018-10-29",
  78 |             open: 173.74,
  79 |             high: 175.99,
  80 |             low: 170.95,
  81 |             close: 173.2,
  82 |           },
  83 |           {
  84 |             time: "2018-10-30",
  85 |             open: 173.16,
  86 |             high: 176.43,
  87 |             low: 172.64,
  88 |             close: 176.24,
  89 |           },
  90 |           {
  91 |             time: "2018-10-31",
  92 |             open: 177.98,
  93 |             high: 178.85,
  94 |             low: 175.59,
  95 |             close: 175.88,
  96 |           },
  97 |           {
  98 |             time: "2018-11-01",
  99 |             open: 176.84,
 100 |             high: 180.86,
 101 |             low: 175.9,
 102 |             close: 180.46,
 103 |           },
 104 |           {
 105 |             time: "2018-11-02",
 106 |             open: 182.47,
 107 |             high: 183.01,
 108 |             low: 177.39,
 109 |             close: 179.93,
 110 |           },
 111 |           {
 112 |             time: "2018-11-05",
 113 |             open: 181.02,
 114 |             high: 182.41,
 115 |             low: 179.3,
 116 |             close: 182.19,
 117 |           },
 118 |           {
 119 |             time: "2018-11-06",
 120 |             open: 181.93,
 121 |             high: 182.65,
 122 |             low: 180.05,
 123 |             close: 182.01,
 124 |           },
 125 |           {
 126 |             time: "2018-11-07",
 127 |             open: 183.79,
 128 |             high: 187.68,
 129 |             low: 182.06,
 130 |             close: 187.23,
 131 |           },
 132 |           {
 133 |             time: "2018-11-08",
 134 |             open: 187.13,
 135 |             high: 188.69,
 136 |             low: 185.72,
 137 |             close: 188.0,
 138 |           },
 139 |           {
 140 |             time: "2018-11-09",
 141 |             open: 188.32,
 142 |             high: 188.48,
 143 |             low: 184.96,
 144 |             close: 185.99,
 145 |           },
 146 |           {
 147 |             time: "2018-11-12",
 148 |             open: 185.23,
 149 |             high: 186.95,
 150 |             low: 179.02,
 151 |             close: 179.43,
 152 |           },
 153 |           {
 154 |             time: "2018-11-13",
 155 |             open: 177.3,
 156 |             high: 181.62,
 157 |             low: 172.85,
 158 |             close: 179.0,
 159 |           },
 160 |           {
 161 |             time: "2018-11-14",
 162 |             open: 182.61,
 163 |             high: 182.9,
 164 |             low: 179.15,
 165 |             close: 179.9,
 166 |           },
 167 |           {
 168 |             time: "2018-11-15",
 169 |             open: 179.01,
 170 |             high: 179.67,
 171 |             low: 173.61,
 172 |             close: 177.36,
 173 |           },
 174 |           {
 175 |             time: "2018-11-16",
 176 |             open: 173.99,
 177 |             high: 177.6,
 178 |             low: 173.51,
 179 |             close: 177.02,
 180 |           },
 181 |           {
 182 |             time: "2018-11-19",
 183 |             open: 176.71,
 184 |             high: 178.88,
 185 |             low: 172.3,
 186 |             close: 173.59,
 187 |           },
 188 |           {
 189 |             time: "2018-11-20",
 190 |             open: 169.25,
 191 |             high: 172.0,
 192 |             low: 167.0,
 193 |             close: 169.05,
 194 |           },
 195 |           {
 196 |             time: "2018-11-21",
 197 |             open: 170.0,
 198 |             high: 170.93,
 199 |             low: 169.15,
 200 |             close: 169.3,
 201 |           },
 202 |           {
 203 |             time: "2018-11-23",
 204 |             open: 169.39,
 205 |             high: 170.33,
 206 |             low: 168.47,
 207 |             close: 168.85,
 208 |           },
 209 |           {
 210 |             time: "2018-11-26",
 211 |             open: 170.2,
 212 |             high: 172.39,
 213 |             low: 168.87,
 214 |             close: 169.82,
 215 |           },
 216 |           {
 217 |             time: "2018-11-27",
 218 |             open: 169.11,
 219 |             high: 173.38,
 220 |             low: 168.82,
 221 |             close: 173.22,
 222 |           },
 223 |           {
 224 |             time: "2018-11-28",
 225 |             open: 172.91,
 226 |             high: 177.65,
 227 |             low: 170.62,
 228 |             close: 177.43,
 229 |           },
 230 |           {
 231 |             time: "2018-11-29",
 232 |             open: 176.8,
 233 |             high: 177.27,
 234 |             low: 174.92,
 235 |             close: 175.66,
 236 |           },
 237 |           {
 238 |             time: "2018-11-30",
 239 |             open: 175.75,
 240 |             high: 180.37,
 241 |             low: 175.11,
 242 |             close: 180.32,
 243 |           },
 244 |           {
 245 |             time: "2018-12-03",
 246 |             open: 183.29,
 247 |             high: 183.5,
 248 |             low: 179.35,
 249 |             close: 181.74,
 250 |           },
 251 |           {
 252 |             time: "2018-12-04",
 253 |             open: 181.06,
 254 |             high: 182.23,
 255 |             low: 174.55,
 256 |             close: 175.3,
 257 |           },
 258 |           {
 259 |             time: "2018-12-06",
 260 |             open: 173.5,
 261 |             high: 176.04,
 262 |             low: 170.46,
 263 |             close: 175.96,
 264 |           },
 265 |           {
 266 |             time: "2018-12-07",
 267 |             open: 175.35,
 268 |             high: 178.36,
 269 |             low: 172.24,
 270 |             close: 172.79,
 271 |           },
 272 |           {
 273 |             time: "2018-12-10",
 274 |             open: 173.39,
 275 |             high: 173.99,
 276 |             low: 167.73,
 277 |             close: 171.69,
 278 |           },
 279 |           {
 280 |             time: "2018-12-11",
 281 |             open: 174.3,
 282 |             high: 175.6,
 283 |             low: 171.24,
 284 |             close: 172.21,
 285 |           },
 286 |           {
 287 |             time: "2018-12-12",
 288 |             open: 173.75,
 289 |             high: 176.87,
 290 |             low: 172.81,
 291 |             close: 174.21,
 292 |           },
 293 |           {
 294 |             time: "2018-12-13",
 295 |             open: 174.31,
 296 |             high: 174.91,
 297 |             low: 172.07,
 298 |             close: 173.87,
 299 |           },
 300 |           {
 301 |             time: "2018-12-14",
 302 |             open: 172.98,
 303 |             high: 175.14,
 304 |             low: 171.95,
 305 |             close: 172.29,
 306 |           },
 307 |           {
 308 |             time: "2018-12-17",
 309 |             open: 171.51,
 310 |             high: 171.99,
 311 |             low: 166.93,
 312 |             close: 167.97,
 313 |           },
 314 |           {
 315 |             time: "2018-12-18",
 316 |             open: 168.9,
 317 |             high: 171.95,
 318 |             low: 168.5,
 319 |             close: 170.04,
 320 |           },
 321 |           {
 322 |             time: "2018-12-19",
 323 |             open: 170.92,
 324 |             high: 174.95,
 325 |             low: 166.77,
 326 |             close: 167.56,
 327 |           },
 328 |           {
 329 |             time: "2018-12-20",
 330 |             open: 166.28,
 331 |             high: 167.31,
 332 |             low: 162.23,
 333 |             close: 164.16,
 334 |           },
 335 |           {
 336 |             time: "2018-12-21",
 337 |             open: 162.81,
 338 |             high: 167.96,
 339 |             low: 160.17,
 340 |             close: 160.48,
 341 |           },
 342 |           {
 343 |             time: "2018-12-24",
 344 |             open: 160.16,
 345 |             high: 161.4,
 346 |             low: 158.09,
 347 |             close: 158.14,
 348 |           },
 349 |           {
 350 |             time: "2018-12-26",
 351 |             open: 159.46,
 352 |             high: 168.28,
 353 |             low: 159.44,
 354 |             close: 168.28,
 355 |           },
 356 |           {
 357 |             time: "2018-12-27",
 358 |             open: 166.44,
 359 |             high: 170.46,
 360 |             low: 163.36,
 361 |             close: 170.32,
 362 |           },
 363 |           {
 364 |             time: "2018-12-28",
 365 |             open: 171.22,
 366 |             high: 173.12,
 367 |             low: 168.6,
 368 |             close: 170.22,
 369 |           },
 370 |           {
 371 |             time: "2018-12-31",
 372 |             open: 171.47,
 373 |             high: 173.24,
 374 |             low: 170.65,
 375 |             close: 171.82,
 376 |           },
 377 |           {
 378 |             time: "2019-01-02",
 379 |             open: 169.71,
 380 |             high: 173.18,
 381 |             low: 169.05,
 382 |             close: 172.41,
 383 |           },
 384 |           {
 385 |             time: "2019-01-03",
 386 |             open: 171.84,
 387 |             high: 171.84,
 388 |             low: 168.21,
 389 |             close: 168.61,
 390 |           },
 391 |           {
 392 |             time: "2019-01-04",
 393 |             open: 170.18,
 394 |             high: 174.74,
 395 |             low: 169.52,
 396 |             close: 173.62,
 397 |           },
 398 |           {
 399 |             time: "2019-01-07",
 400 |             open: 173.83,
 401 |             high: 178.18,
 402 |             low: 173.83,
 403 |             close: 177.04,
 404 |           },
 405 |           {
 406 |             time: "2019-01-08",
 407 |             open: 178.57,
 408 |             high: 179.59,
 409 |             low: 175.61,
 410 |             close: 177.89,
 411 |           },
 412 |           {
 413 |             time: "2019-01-09",
 414 |             open: 177.87,
 415 |             high: 181.27,
 416 |             low: 177.1,
 417 |             close: 179.73,
 418 |           },
 419 |           {
 420 |             time: "2019-01-10",
 421 |             open: 178.03,
 422 |             high: 179.24,
 423 |             low: 176.34,
 424 |             close: 179.06,
 425 |           },
 426 |           {
 427 |             time: "2019-01-11",
 428 |             open: 177.93,
 429 |             high: 180.26,
 430 |             low: 177.12,
 431 |             close: 179.41,
 432 |           },
 433 |           {
 434 |             time: "2019-01-14",
 435 |             open: 177.59,
 436 |             high: 179.23,
 437 |             low: 176.9,
 438 |             close: 178.81,
 439 |           },
 440 |           {
 441 |             time: "2019-01-15",
 442 |             open: 176.08,
 443 |             high: 177.82,
 444 |             low: 175.2,
 445 |             close: 176.47,
 446 |           },
 447 |           {
 448 |             time: "2019-01-16",
 449 |             open: 177.09,
 450 |             high: 177.93,
 451 |             low: 175.86,
 452 |             close: 177.04,
 453 |           },
 454 |           {
 455 |             time: "2019-01-17",
 456 |             open: 174.01,
 457 |             high: 175.46,
 458 |             low: 172.0,
 459 |             close: 174.87,
 460 |           },
 461 |           {
 462 |             time: "2019-01-18",
 463 |             open: 176.98,
 464 |             high: 180.04,
 465 |             low: 176.18,
 466 |             close: 179.58,
 467 |           },
 468 |           {
 469 |             time: "2019-01-22",
 470 |             open: 177.49,
 471 |             high: 178.6,
 472 |             low: 175.36,
 473 |             close: 177.11,
 474 |           },
 475 |           {
 476 |             time: "2019-01-23",
 477 |             open: 176.59,
 478 |             high: 178.06,
 479 |             low: 174.53,
 480 |             close: 176.89,
 481 |           },
 482 |           {
 483 |             time: "2019-01-24",
 484 |             open: 177.0,
 485 |             high: 177.53,
 486 |             low: 175.3,
 487 |             close: 177.29,
 488 |           },
 489 |           {
 490 |             time: "2019-01-25",
 491 |             open: 179.78,
 492 |             high: 180.87,
 493 |             low: 178.61,
 494 |             close: 180.4,
 495 |           },
 496 |           {
 497 |             time: "2019-01-28",
 498 |             open: 178.97,
 499 |             high: 179.99,
 500 |             low: 177.41,
 501 |             close: 179.83,
 502 |           },
 503 |           {
 504 |             time: "2019-01-29",
 505 |             open: 178.96,
 506 |             high: 180.15,
 507 |             low: 178.09,
 508 |             close: 179.69,
 509 |           },
 510 |           {
 511 |             time: "2019-01-30",
 512 |             open: 180.47,
 513 |             high: 184.2,
 514 |             low: 179.78,
 515 |             close: 182.18,
 516 |           },
 517 |           {
 518 |             time: "2019-01-31",
 519 |             open: 181.5,
 520 |             high: 184.67,
 521 |             low: 181.06,
 522 |             close: 183.53,
 523 |           },
 524 |           {
 525 |             time: "2019-02-01",
 526 |             open: 184.03,
 527 |             high: 185.15,
 528 |             low: 182.83,
 529 |             close: 184.37,
 530 |           },
 531 |           {
 532 |             time: "2019-02-04",
 533 |             open: 184.3,
 534 |             high: 186.43,
 535 |             low: 183.84,
 536 |             close: 186.43,
 537 |           },
 538 |           {
 539 |             time: "2019-02-05",
 540 |             open: 186.89,
 541 |             high: 186.99,
 542 |             low: 184.69,
 543 |             close: 186.39,
 544 |           },
 545 |           {
 546 |             time: "2019-02-06",
 547 |             open: 186.69,
 548 |             high: 186.69,
 549 |             low: 184.06,
 550 |             close: 184.72,
 551 |           },
 552 |           {
 553 |             time: "2019-02-07",
 554 |             open: 183.74,
 555 |             high: 184.92,
 556 |             low: 182.45,
 557 |             close: 184.07,
 558 |           },
 559 |           {
 560 |             time: "2019-02-08",
 561 |             open: 183.05,
 562 |             high: 184.58,
 563 |             low: 182.72,
 564 |             close: 184.54,
 565 |           },
 566 |           {
 567 |             time: "2019-02-11",
 568 |             open: 185.0,
 569 |             high: 185.42,
 570 |             low: 182.75,
 571 |             close: 182.92,
 572 |           },
 573 |           {
 574 |             time: "2019-02-12",
 575 |             open: 183.84,
 576 |             high: 186.4,
 577 |             low: 183.52,
 578 |             close: 185.52,
 579 |           },
 580 |           {
 581 |             time: "2019-02-13",
 582 |             open: 186.3,
 583 |             high: 188.68,
 584 |             low: 185.92,
 585 |             close: 188.41,
 586 |           },
 587 |           {
 588 |             time: "2019-02-14",
 589 |             open: 187.5,
 590 |             high: 188.93,
 591 |             low: 186.0,
 592 |             close: 187.71,
 593 |           },
 594 |           {
 595 |             time: "2019-02-15",
 596 |             open: 189.87,
 597 |             high: 192.62,
 598 |             low: 189.05,
 599 |             close: 192.39,
 600 |           },
 601 |           {
 602 |             time: "2019-02-19",
 603 |             open: 191.71,
 604 |             high: 193.19,
 605 |             low: 191.28,
 606 |             close: 192.33,
 607 |           },
 608 |           {
 609 |             time: "2019-02-20",
 610 |             open: 192.39,
 611 |             high: 192.4,
 612 |             low: 191.11,
 613 |             close: 191.85,
 614 |           },
 615 |           {
 616 |             time: "2019-02-21",
 617 |             open: 191.85,
 618 |             high: 192.37,
 619 |             low: 190.61,
 620 |             close: 191.82,
 621 |           },
 622 |           {
 623 |             time: "2019-02-22",
 624 |             open: 191.69,
 625 |             high: 192.54,
 626 |             low: 191.62,
 627 |             close: 192.39,
 628 |           },
 629 |           {
 630 |             time: "2019-02-25",
 631 |             open: 192.75,
 632 |             high: 193.42,
 633 |             low: 189.96,
 634 |             close: 189.98,
 635 |           },
 636 |           {
 637 |             time: "2019-02-26",
 638 |             open: 185.59,
 639 |             high: 188.47,
 640 |             low: 182.8,
 641 |             close: 188.3,
 642 |           },
 643 |           {
 644 |             time: "2019-02-27",
 645 |             open: 187.9,
 646 |             high: 188.5,
 647 |             low: 183.21,
 648 |             close: 183.67,
 649 |           },
 650 |           {
 651 |             time: "2019-02-28",
 652 |             open: 183.6,
 653 |             high: 185.19,
 654 |             low: 183.11,
 655 |             close: 185.14,
 656 |           },
 657 |           {
 658 |             time: "2019-03-01",
 659 |             open: 185.82,
 660 |             high: 186.56,
 661 |             low: 182.86,
 662 |             close: 185.17,
 663 |           },
 664 |           {
 665 |             time: "2019-03-04",
 666 |             open: 186.2,
 667 |             high: 186.24,
 668 |             low: 182.1,
 669 |             close: 183.81,
 670 |           },
 671 |           {
 672 |             time: "2019-03-05",
 673 |             open: 184.24,
 674 |             high: 185.12,
 675 |             low: 183.25,
 676 |             close: 184.0,
 677 |           },
 678 |           {
 679 |             time: "2019-03-06",
 680 |             open: 184.53,
 681 |             high: 184.97,
 682 |             low: 183.84,
 683 |             close: 184.45,
 684 |           },
 685 |           {
 686 |             time: "2019-03-07",
 687 |             open: 184.39,
 688 |             high: 184.62,
 689 |             low: 181.58,
 690 |             close: 182.51,
 691 |           },
 692 |           {
 693 |             time: "2019-03-08",
 694 |             open: 181.49,
 695 |             high: 181.91,
 696 |             low: 179.52,
 697 |             close: 181.23,
 698 |           },
 699 |           {
 700 |             time: "2019-03-11",
 701 |             open: 182.0,
 702 |             high: 183.2,
 703 |             low: 181.2,
 704 |             close: 182.44,
 705 |           },
 706 |           {
 707 |             time: "2019-03-12",
 708 |             open: 183.43,
 709 |             high: 184.27,
 710 |             low: 182.33,
 711 |             close: 184.0,
 712 |           },
 713 |           {
 714 |             time: "2019-03-13",
 715 |             open: 183.24,
 716 |             high: 183.78,
 717 |             low: 181.08,
 718 |             close: 181.14,
 719 |           },
 720 |           {
 721 |             time: "2019-03-14",
 722 |             open: 181.28,
 723 |             high: 181.74,
 724 |             low: 180.5,
 725 |             close: 181.61,
 726 |           },
 727 |           {
 728 |             time: "2019-03-15",
 729 |             open: 182.3,
 730 |             high: 182.49,
 731 |             low: 179.57,
 732 |             close: 182.23,
 733 |           },
 734 |           {
 735 |             time: "2019-03-18",
 736 |             open: 182.53,
 737 |             high: 183.48,
 738 |             low: 182.33,
 739 |             close: 183.42,
 740 |           },
 741 |           {
 742 |             time: "2019-03-19",
 743 |             open: 184.19,
 744 |             high: 185.82,
 745 |             low: 183.48,
 746 |             close: 184.13,
 747 |           },
 748 |           {
 749 |             time: "2019-03-20",
 750 |             open: 184.3,
 751 |             high: 187.12,
 752 |             low: 183.43,
 753 |             close: 186.1,
 754 |           },
 755 |           {
 756 |             time: "2019-03-21",
 757 |             open: 185.5,
 758 |             high: 190.0,
 759 |             low: 185.5,
 760 |             close: 189.97,
 761 |           },
 762 |           {
 763 |             time: "2019-03-22",
 764 |             open: 189.31,
 765 |             high: 192.05,
 766 |             low: 188.67,
 767 |             close: 188.75,
 768 |           },
 769 |           {
 770 |             time: "2019-03-25",
 771 |             open: 188.75,
 772 |             high: 191.71,
 773 |             low: 188.51,
 774 |             close: 189.68,
 775 |           },
 776 |           {
 777 |             time: "2019-03-26",
 778 |             open: 190.69,
 779 |             high: 192.19,
 780 |             low: 188.74,
 781 |             close: 189.34,
 782 |           },
 783 |           {
 784 |             time: "2019-03-27",
 785 |             open: 189.65,
 786 |             high: 191.61,
 787 |             low: 188.39,
 788 |             close: 189.25,
 789 |           },
 790 |           {
 791 |             time: "2019-03-28",
 792 |             open: 189.91,
 793 |             high: 191.4,
 794 |             low: 189.16,
 795 |             close: 190.06,
 796 |           },
 797 |           {
 798 |             time: "2019-03-29",
 799 |             open: 190.85,
 800 |             high: 192.04,
 801 |             low: 190.14,
 802 |             close: 191.89,
 803 |           },
 804 |           {
 805 |             time: "2019-04-01",
 806 |             open: 192.99,
 807 |             high: 195.9,
 808 |             low: 192.85,
 809 |             close: 195.64,
 810 |           },
 811 |           {
 812 |             time: "2019-04-02",
 813 |             open: 195.5,
 814 |             high: 195.5,
 815 |             low: 194.01,
 816 |             close: 194.31,
 817 |           },
 818 |           {
 819 |             time: "2019-04-03",
 820 |             open: 194.98,
 821 |             high: 198.78,
 822 |             low: 194.11,
 823 |             close: 198.61,
 824 |           },
 825 |           {
 826 |             time: "2019-04-04",
 827 |             open: 199.0,
 828 |             high: 200.49,
 829 |             low: 198.02,
 830 |             close: 200.45,
 831 |           },
 832 |           {
 833 |             time: "2019-04-05",
 834 |             open: 200.86,
 835 |             high: 203.13,
 836 |             low: 200.61,
 837 |             close: 202.06,
 838 |           },
 839 |           {
 840 |             time: "2019-04-08",
 841 |             open: 201.37,
 842 |             high: 203.79,
 843 |             low: 201.24,
 844 |             close: 203.55,
 845 |           },
 846 |           {
 847 |             time: "2019-04-09",
 848 |             open: 202.26,
 849 |             high: 202.71,
 850 |             low: 200.46,
 851 |             close: 200.9,
 852 |           },
 853 |           {
 854 |             time: "2019-04-10",
 855 |             open: 201.26,
 856 |             high: 201.6,
 857 |             low: 198.02,
 858 |             close: 199.43,
 859 |           },
 860 |           {
 861 |             time: "2019-04-11",
 862 |             open: 199.9,
 863 |             high: 201.5,
 864 |             low: 199.03,
 865 |             close: 201.48,
 866 |           },
 867 |           {
 868 |             time: "2019-04-12",
 869 |             open: 202.13,
 870 |             high: 204.26,
 871 |             low: 202.13,
 872 |             close: 203.85,
 873 |           },
 874 |           {
 875 |             time: "2019-04-15",
 876 |             open: 204.16,
 877 |             high: 205.14,
 878 |             low: 203.4,
 879 |             close: 204.86,
 880 |           },
 881 |           {
 882 |             time: "2019-04-16",
 883 |             open: 205.25,
 884 |             high: 205.99,
 885 |             low: 204.29,
 886 |             close: 204.47,
 887 |           },
 888 |           {
 889 |             time: "2019-04-17",
 890 |             open: 205.34,
 891 |             high: 206.84,
 892 |             low: 205.32,
 893 |             close: 206.55,
 894 |           },
 895 |           {
 896 |             time: "2019-04-18",
 897 |             open: 206.02,
 898 |             high: 207.78,
 899 |             low: 205.1,
 900 |             close: 205.66,
 901 |           },
 902 |           {
 903 |             time: "2019-04-22",
 904 |             open: 204.11,
 905 |             high: 206.25,
 906 |             low: 204.0,
 907 |             close: 204.78,
 908 |           },
 909 |           {
 910 |             time: "2019-04-23",
 911 |             open: 205.14,
 912 |             high: 207.33,
 913 |             low: 203.43,
 914 |             close: 206.05,
 915 |           },
 916 |           {
 917 |             time: "2019-04-24",
 918 |             open: 206.16,
 919 |             high: 208.29,
 920 |             low: 205.54,
 921 |             close: 206.72,
 922 |           },
 923 |           {
 924 |             time: "2019-04-25",
 925 |             open: 206.01,
 926 |             high: 207.72,
 927 |             low: 205.06,
 928 |             close: 206.5,
 929 |           },
 930 |           {
 931 |             time: "2019-04-26",
 932 |             open: 205.88,
 933 |             high: 206.14,
 934 |             low: 203.34,
 935 |             close: 203.61,
 936 |           },
 937 |           {
 938 |             time: "2019-04-29",
 939 |             open: 203.31,
 940 |             high: 203.8,
 941 |             low: 200.34,
 942 |             close: 202.16,
 943 |           },
 944 |           {
 945 |             time: "2019-04-30",
 946 |             open: 201.55,
 947 |             high: 203.75,
 948 |             low: 200.79,
 949 |             close: 203.7,
 950 |           },
 951 |           {
 952 |             time: "2019-05-01",
 953 |             open: 203.2,
 954 |             high: 203.52,
 955 |             low: 198.66,
 956 |             close: 198.8,
 957 |           },
 958 |           {
 959 |             time: "2019-05-02",
 960 |             open: 199.3,
 961 |             high: 201.06,
 962 |             low: 198.8,
 963 |             close: 201.01,
 964 |           },
 965 |           {
 966 |             time: "2019-05-03",
 967 |             open: 202.0,
 968 |             high: 202.31,
 969 |             low: 200.32,
 970 |             close: 200.56,
 971 |           },
 972 |           {
 973 |             time: "2019-05-06",
 974 |             open: 198.74,
 975 |             high: 199.93,
 976 |             low: 198.31,
 977 |             close: 199.63,
 978 |           },
 979 |           {
 980 |             time: "2019-05-07",
 981 |             open: 196.75,
 982 |             high: 197.65,
 983 |             low: 192.96,
 984 |             close: 194.77,
 985 |           },
 986 |           {
 987 |             time: "2019-05-08",
 988 |             open: 194.49,
 989 |             high: 196.61,
 990 |             low: 193.68,
 991 |             close: 195.17,
 992 |           },
 993 |           {
 994 |             time: "2019-05-09",
 995 |             open: 193.31,
 996 |             high: 195.08,
 997 |             low: 191.59,
 998 |             close: 194.58,
 999 |           },
1000 |           {
1001 |             time: "2019-05-10",
1002 |             open: 193.21,
1003 |             high: 195.49,
1004 |             low: 190.01,
1005 |             close: 194.58,
1006 |           },
1007 |           {
1008 |             time: "2019-05-13",
1009 |             open: 191.0,
1010 |             high: 191.66,
1011 |             low: 189.14,
1012 |             close: 190.34,
1013 |           },
1014 |           {
1015 |             time: "2019-05-14",
1016 |             open: 190.5,
1017 |             high: 192.76,
1018 |             low: 190.01,
1019 |             close: 191.62,
1020 |           },
1021 |           {
1022 |             time: "2019-05-15",
1023 |             open: 190.81,
1024 |             high: 192.81,
1025 |             low: 190.27,
1026 |             close: 191.76,
1027 |           },
1028 |           {
1029 |             time: "2019-05-16",
1030 |             open: 192.47,
1031 |             high: 194.96,
1032 |             low: 192.2,
1033 |             close: 192.38,
1034 |           },
1035 |           {
1036 |             time: "2019-05-17",
1037 |             open: 190.86,
1038 |             high: 194.5,
1039 |             low: 190.75,
1040 |             close: 192.58,
1041 |           },
1042 |           {
1043 |             time: "2019-05-20",
1044 |             open: 191.13,
1045 |             high: 192.86,
1046 |             low: 190.61,
1047 |             close: 190.95,
1048 |           },
1049 |           {
1050 |             time: "2019-05-21",
1051 |             open: 187.13,
1052 |             high: 192.52,
1053 |             low: 186.34,
1054 |             close: 191.45,
1055 |           },
1056 |           {
1057 |             time: "2019-05-22",
1058 |             open: 190.49,
1059 |             high: 192.22,
1060 |             low: 188.05,
1061 |             close: 188.91,
1062 |           },
1063 |           {
1064 |             time: "2019-05-23",
1065 |             open: 188.45,
1066 |             high: 192.54,
1067 |             low: 186.27,
1068 |             close: 192.0,
1069 |           },
1070 |           {
1071 |             time: "2019-05-24",
1072 |             open: 192.54,
1073 |             high: 193.86,
1074 |             low: 190.41,
1075 |             close: 193.59,
1076 |           },
1077 |         ];
1078 |       }
1079 | 
1080 |       // Create the Lightweight Chart within the container element
1081 |       const chart = LightweightCharts.createChart(
1082 |         document.getElementById('container'),
1083 |         {
1084 |           layout: {
1085 |             background: { color: "#222" },
1086 |             textColor: "#C3BCDB",
1087 |           },
1088 |           grid: {
1089 |             vertLines: { color: "#444" },
1090 |             horzLines: { color: "#444" },
1091 |           },
1092 |         }
1093 |       );
1094 | 
1095 |       // Setting the border color for the vertical axis
1096 |       chart.priceScale().applyOptions({
1097 |         borderColor: "#71649C",
1098 |       });
1099 | 
1100 |       // Setting the border color for the horizontal axis
1101 |       chart.timeScale().applyOptions({
1102 |         borderColor: "#71649C",
1103 |       });
1104 | 
1105 |       // Adjust the starting bar width (essentially the horizontal zoom)
1106 |       chart.timeScale().applyOptions({
1107 |         barSpacing: 10,
1108 |       });
1109 | 
1110 |       // Get the current users primary locale
1111 |       const currentLocale = window.navigator.languages[0];
1112 |       // Create a number format using Intl.NumberFormat
1113 |       const myPriceFormatter = Intl.NumberFormat(currentLocale, {
1114 |         style: "currency",
1115 |         currency: "EUR", // Currency for data points
1116 |       }).format;
1117 | 
1118 |       // Apply the custom priceFormatter to the chart
1119 |       chart.applyOptions({
1120 |         localization: {
1121 |           priceFormatter: myPriceFormatter,
1122 |         },
1123 |       });
1124 | 
1125 |       // Customizing the Crosshair
1126 |       chart.applyOptions({
1127 |         crosshair: {
1128 |           // Change mode from default 'magnet' to 'normal'.
1129 |           // Allows the crosshair to move freely without snapping to datapoints
1130 |           mode: LightweightCharts.CrosshairMode.Normal,
1131 | 
1132 |           // Vertical crosshair line (showing Date in Label)
1133 |           vertLine: {
1134 |             width: 8,
1135 |             color: "#C3BCDB44",
1136 |             style: LightweightCharts.LineStyle.Solid,
1137 |             labelBackgroundColor: "#9B7DFF",
1138 |           },
1139 | 
1140 |           // Horizontal crosshair line (showing Price in Label)
1141 |           horzLine: {
1142 |             color: "#9B7DFF",
1143 |             labelBackgroundColor: "#9B7DFF",
1144 |           },
1145 |         },
1146 |       });
1147 | 
1148 |       // Generate sample data to use within a candlestick series
1149 |       const candleStickData = generateCandlestickData().map((datapoint) => {
1150 |         // map function is changing the color for the individual
1151 |         // candlestick points that close above 205
1152 |         if (datapoint.close < 205) return datapoint;
1153 |         // we are adding 'color' and 'wickColor' properties to the datapoint.
1154 |         // Using spread syntax: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#spread_in_object_literals
1155 |         return { ...datapoint, color: "orange", wickColor: "orange" };
1156 |       });
1157 | 
1158 |       // Convert the candlestick data for use with a line series
1159 |       const lineData = candleStickData.map((datapoint) => ({
1160 |         time: datapoint.time,
1161 |         value: (datapoint.close + datapoint.open) / 2,
1162 |       }));
1163 | 
1164 |       // Add an area series to the chart,
1165 |       // Adding this before we add the candlestick chart
1166 |       // so that it will appear beneath the candlesticks
1167 |       const areaSeries = chart.addSeries(LightweightCharts.AreaSeries, {
1168 |         lastValueVisible: false, // hide the last value marker for this series
1169 |         crosshairMarkerVisible: false, // hide the crosshair marker for this series
1170 |         lineColor: "transparent", // hide the line
1171 |         topColor: "rgba(56, 33, 110,0.6)",
1172 |         bottomColor: "rgba(56, 33, 110, 0.1)",
1173 |       });
1174 |       // Set the data for the Area Series
1175 |       areaSeries.setData(lineData);
1176 | 
1177 |       // Create the Main Series (Candlesticks)
1178 |       const mainSeries = chart.addSeries(LightweightCharts.CandlestickSeries);
1179 |       // Set the data for the Main Series
1180 |       mainSeries.setData(candleStickData);
1181 | 
1182 |       // Changing the Candlestick colors
1183 |       mainSeries.applyOptions({
1184 |         wickUpColor: "rgb(54, 116, 217)",
1185 |         upColor: "rgb(54, 116, 217)",
1186 |         wickDownColor: "rgb(225, 50, 85)",
1187 |         downColor: "rgb(225, 50, 85)",
1188 |         borderVisible: false,
1189 |       });
1190 | 
1191 |       // Adjust the options for the priceScale of the mainSeries
1192 |       mainSeries.priceScale().applyOptions({
1193 |         autoScale: false, // disables auto scaling based on visible content
1194 |         scaleMargins: {
1195 |           top: 0.1,
1196 |           bottom: 0.2,
1197 |         },
1198 |       });
1199 | 
1200 |       // Adding a window resize event handler to resize the chart when
1201 |       // the window size changes.
1202 |       // Note: for more advanced examples (when the chart doesn't fill the entire window)
1203 |       // you may need to use ResizeObserver -> https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver
1204 |       window.addEventListener("resize", () => {
1205 |         chart.resize(window.innerWidth, window.innerHeight);
1206 |       });
1207 |     </script>
1208 |   </body>
1209 | </html>
1210 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/chart-colors.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_position: 2
  3 | title: Chart colors
  4 | pagination_title: Chart colors
  5 | sidebar_label: Chart colors
  6 | description: In this section, we will be customizing the appearance of the chart 'backdrop'.
  7 | keywords:
  8 |   - customization
  9 |   - appearance
 10 |   - styling
 11 | pagination_prev: customization/creating-a-chart
 12 | pagination_next: customization/series
 13 | ---
 14 | 
 15 | import IterativeGuideWarning from './_iterative-guide-warning-partial.mdx';
 16 | 
 17 | <IterativeGuideWarning/>
 18 | 
 19 | In this section, we will be customizing the appearance of the chart 'backdrop'. We will be adjusting the colors to better suit a dark theme.
 20 | 
 21 | ## Setting the background color of the HTML body
 22 | 
 23 | Before we get started customizing the colors of the chart, we will first change the background color of the entire HTML page to our desired color of `#222`. If we decide to have the chart not fill the entire space of the page (the optional step further below) then this step will ensure that the chart's background matches the background of the page.
 24 | 
 25 | :::tip
 26 | 
 27 | It is also possible to set the chart background color to `transparent`, which may be useful in certain circumstances.
 28 | 
 29 | :::
 30 | 
 31 | We can set the page background by adding the following code which the `<style>` tag near the top of the HTML code.
 32 | 
 33 | ```html
 34 | <style>
 35 |     body {
 36 |         padding: 0;
 37 |         margin: 0;
 38 |         /* highlight-start */
 39 |         /* Add a background color to match the chart */
 40 |         background-color: #222;
 41 |         /* highlight-end */
 42 |     }
 43 | </style>
 44 | ```
 45 | 
 46 | ## Applying options
 47 | 
 48 | One final explanation before we dive into customizing the chart. There are generally two ways to specify options for an API instance (such as IChartApi, ISeriesApi, IPriceScale, etc...) within Lightweight Charts™. The first is to specify the options at the time of creation, and the second is to specify the options at any other time by using the `applyOptions` method. Which approach to use is primarily up to you, however, you can only use the `applyOptions` approach if you are changing the options at a later stage after the instance has been created.
 49 | 
 50 | This tutorial will make use of both approaches to provide cleaner and easier-to-follow code.
 51 | 
 52 | The options object passed into either method doesn't need to be a complete object containing all the options, but rather only the options you need to change. During the creation of an instance, the default options will be used and your options will be applied over those. When using `applyOptions`, the specified options will be merged over the current options for that instance.
 53 | 
 54 | **The following code block isn't part of the tutorial but is included just to highlight the two approaches.**
 55 | 
 56 | import ApplyOptionsTabs from './_apply-options-tabs-partial.mdx';
 57 | 
 58 | <ApplyOptionsTabs/>
 59 | 
 60 | ## Adjusting the background and text colors for the chart
 61 | 
 62 | We can adjust the chart's background color and text color by specifying our desired colors within the options for [IChartApi](/docs/api/interfaces/IChartApi). A full list of the available options for the chart instance can be viewed here: [ChartOptionsBase](/docs/api/interfaces/ChartOptionsBase).
 63 | 
 64 | We are going to add the options during the creation of the chart (as the second argument to the `createChart` method) as follows:
 65 | 
 66 | ```js
 67 | const chart = LightweightCharts.createChart(
 68 |     document.getElementById('container'),
 69 |     {
 70 |         layout: {
 71 |             background: { color: '#222' },
 72 |             textColor: '#DDD',
 73 |         },
 74 |         grid: {
 75 |             vertLines: { color: '#444' },
 76 |             horzLines: { color: '#444' },
 77 |         },
 78 |     }
 79 | );
 80 | ```
 81 | 
 82 | We also set the color for the gridlines at the same time.
 83 | 
 84 | ## (Optional) Setting a desired height and width for the chart
 85 | 
 86 | By default, if you don't specify a `height` and `width` within the options for the chart then the chart will fill the available space within it's HTML element.
 87 | 
 88 | If you would like to set specific dimensions for the chart then you can do so like this:
 89 | 
 90 | ```js
 91 | const chart = LightweightCharts.createChart(
 92 |     document.getElementById('container'),
 93 |     {
 94 |         height: 400,
 95 |         width: 600,
 96 |     }
 97 | );
 98 | ```
 99 | 
100 | ## Adjusting the border colors for the axes
101 | 
102 | We can set the border colors for the price and time scales by using the `applyOptions` method on the [IPriceScale](/docs/api/interfaces/IPriceScaleApi) and [ITimeScale](/docs/api/interfaces/ITimeScaleApi) instances. We can get references to these instances by using the `priceScale()` and `timeScale()` methods on a chart instance.
103 | 
104 | You can add the following code beneath the `createChart` method call.
105 | 
106 | ```js
107 | // Setting the border color for the vertical axis
108 | chart.priceScale().applyOptions({
109 |     borderColor: '#71649C',
110 | });
111 | 
112 | // Setting the border color for the horizontal axis
113 | chart.timeScale().applyOptions({
114 |     borderColor: '#71649C',
115 | });
116 | ```
117 | 
118 | At a later stage, we will customise these scales further.
119 | 
120 | ## Result
121 | 
122 | At this point we should have a chart like this:
123 | 
124 | <iframe
125 |     className="standalone-iframe"
126 |     src={require('!!file-loader!./assets/step2.html').default}
127 | ></iframe>
128 | <a href={require('!!file-loader!./assets/step2.html').default} target="\_blank">
129 |     View in a new window
130 | </a>
131 | 
132 | ## Next steps
133 | 
134 | In the next step, we will change the colors for the candlestick series.
135 | 
136 | ## Download
137 | 
138 | You can download the HTML file for example at this stage <a href={require('!!file-loader!./assets/step2.html').default} download="customization-tutorial-step2.html" target="\_blank">here</a> in case you've encountered a problem or would like to start the next step from this point.
139 | 
140 | ## Complete code
141 | 
142 | import CodeBlock from '@theme/CodeBlock';
143 | import code from '!!raw-loader!./assets/step2.html';
144 | import InstantDetails from '@site/src/components/InstantDetails'
145 | 
146 | <InstantDetails>
147 | <summary>
148 | Click here to reveal the complete code for the example at this stage of the guide.
149 | </summary>
150 | <CodeBlock className="language-html">{code}</CodeBlock>
151 | </InstantDetails>
152 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/conclusion.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 11
 3 | title: Conclusion
 4 | pagination_title: Conclusion
 5 | sidebar_label: Conclusion
 6 | description: Conclusion to the customization tutorial
 7 | keywords:
 8 |   - customization
 9 |   - appearance
10 |   - styling
11 | pagination_prev: customization/finishing-touches
12 | pagination_next: null
13 | ---
14 | 
15 | Thank you for taking the time to complete this tutorial, and we hope that you've learnt how to customise your charts to meet your needs and more importantly where to find the available options in the documentation and how to apply them to your chart.
16 | 
17 | We look forward to seeing what you create.
18 | 
19 | We welcome any and all feedback on this tutorial and library in general. You can reach us via the following channels:
20 | 
21 | - [GitHub Discussions](https://github.com/tradingview/lightweight-charts/discussions)
22 | 
23 | and if you've spotted any errors or bugs then please post an issue on our [GitHub page](https://github.com/tradingview/lightweight-charts/issues).
24 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/creating-a-chart.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_position: 1
  3 | title: First steps
  4 | pagination_title: First steps
  5 | sidebar_label: First steps
  6 | description: In this section, we will be creating a simple chart.
  7 | keywords:
  8 |   - customization
  9 |   - appearance
 10 |   - styling
 11 | pagination_prev: customization/intro
 12 | pagination_next: customization/chart-colors
 13 | ---
 14 | 
 15 | :::tip
 16 | 
 17 | If you haven't already, please read the [Introduction](intro). At the bottom of that page, you will find a starting file containing everything you need to get up and running with this tutorial (including some sample data to display on the chart).
 18 | 
 19 | :::
 20 | 
 21 | Our first task will be to create a chart and get it visible on the page. A more detailed explanation of these steps is available [here](/docs).
 22 | 
 23 | ## Adding the Lightweight Charts™ script
 24 | 
 25 | For this example, we will be loading the Lightweight Charts™ library using the standalone version hosted on a CDN server. This approach allows us to just include the script tag within our HTML file and not be concerned about spinning up a web server to host our files, and thus open the HTML file directly on our computer.
 26 | 
 27 | We can add the script tag to the HTML page by including the following code within the `<head>` element of the page. In this case, we will insert the code between the `<title>` and `<style>` elements.
 28 | 
 29 | ```html
 30 | <title>Lightweight Charts Customization Tutorial</title>
 31 | <!-- highlight-start -->
 32 | <!-- Adding the standalone version of Lightweight charts -->
 33 | <script
 34 |     type="text/javascript"
 35 |     src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"
 36 | ></script>
 37 | <!-- highlight-end -->
 38 | <style>
 39 | ```
 40 | 
 41 | The standalone script will add the library as a global variable named `LightweightCharts` once it has been downloaded and executed by the browser.
 42 | 
 43 | ## Creating the chart
 44 | 
 45 | We can create the chart instance by calling the [`createChart`](/docs/api/functions/createChart) method on the `LightweightCharts` global variable, and providing an HTML div element as the first parameter to the method. The `createChart` method can take a second parameter for options which will be explored and used later in the guide.
 46 | 
 47 | We will add the following code to our main script tag which already contains the code to generate the sample data. The sample file contains a `// your code here` comment as a reference of where to insert the code.
 48 | 
 49 | ```js
 50 | // Create the Lightweight Chart within the container element
 51 | const chart = LightweightCharts.createChart(
 52 |     document.getElementById('container')
 53 | );
 54 | ```
 55 | 
 56 | The `createChart` method returns an [IChartApi](/docs/api/interfaces/IChartApi) instance which will be our main point of contact for interacting with the API.
 57 | 
 58 | ## Creating some sample data
 59 | 
 60 | We can create some sample data for the chart by calling the provided `generateCandlestickData` function and we will assign it to a variable named `candleStickData`, as follows:
 61 | 
 62 | ```js
 63 | // Create the Lightweight Chart within the container element
 64 | const chart = LightweightCharts.createChart(
 65 |     document.getElementById('container')
 66 | );
 67 | 
 68 | // highlight-start
 69 | // Generate sample data to use within a candlestick series
 70 | const candleStickData = generateCandlestickData();
 71 | // highlight-end
 72 | ```
 73 | 
 74 | ## Adding a candlestick series
 75 | 
 76 | We can now add a [candlestick series](/docs/series-types#candlestick) to our chart by using the `addCandlestickSeries` method on the `chart` variable (which is an [IChartApi](/docs/api/interfaces/IChartApi) instance). This will return a series instance which we will assign to a variable named `mainSeries`.
 77 | 
 78 | `mainSeries` will be an instance of [`ISeriesApi`](/docs/api/interfaces/ISeriesApi) which will provide the API for interacting with the series and it's options.
 79 | 
 80 | ```js
 81 | // Generate sample data to use within a candlestick series
 82 | const candleStickData = generateCandlestickData();
 83 | 
 84 | // highlight-start
 85 | // Create the Main Series (Candlesticks)
 86 | const mainSeries = chart.addSeries(LightweightCharts.CandlestickSeries);
 87 | // Set the data for the Main Series
 88 | mainSeries.setData(candleStickData);
 89 | // highlight-end
 90 | ```
 91 | 
 92 | ## Automatically resizing the chart when the window is resized (Optional)
 93 | 
 94 | This is an optional step which will enable automatically resizing the chart whenever
 95 | the browser window is resized.
 96 | 
 97 | :::caution
 98 | 
 99 | This code snippet will only work correctly if you want the chart to completely fill the window / iframe.
100 | 
101 | :::
102 | 
103 | Adding the following code snippet to the end of the script tag to enable automatic resizing.
104 | 
105 | ```js
106 | // Adding a window resize event handler to resize the chart when
107 | // the window size changes.
108 | // Note: for more advanced examples (when the chart doesn't fill the entire window)
109 | // you may need to use ResizeObserver -> https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver
110 | window.addEventListener('resize', () => {
111 |     chart.resize(window.innerWidth, window.innerHeight);
112 | });
113 | ```
114 | 
115 | ## Result
116 | 
117 | At this point we should have a chart like this:
118 | 
119 | <iframe
120 |     className="standalone-iframe"
121 |     src={require('!!file-loader!./assets/step1.html').default}
122 | ></iframe>
123 | <a href={require('!!file-loader!./assets/step1.html').default} target="\_blank">
124 |     View in a new window
125 | </a>
126 | 
127 | ## Next steps
128 | 
129 | 🎉 Congrats! We now have a basic, yet beautiful, candlestick chart rendering on our page.
130 | 
131 | The rest of the tutorial will focus on how to customise this chart to further match our desired visual style and functionality. The next step will be to adjust the chart colors to better suit a dark theme.
132 | 
133 | ## Download
134 | 
135 | You can download the HTML file for example at this stage <a href={require('!!file-loader!./assets/step1.html').default} download="customization-tutorial-step1.html" target="\_blank">here</a> in case you've encountered a problem or would like to start the next step from this point.
136 | 
137 | ## Complete code
138 | 
139 | import CodeBlock from '@theme/CodeBlock';
140 | import code from '!!raw-loader!./assets/step1.html';
141 | import InstantDetails from '@site/src/components/InstantDetails'
142 | 
143 | <InstantDetails>
144 | <summary>
145 | Click here to reveal the complete code for the example at this stage of the guide.
146 | </summary>
147 | <CodeBlock className="language-html">{code}</CodeBlock>
148 | </InstantDetails>
149 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/crosshair.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 7
 3 | title: Crosshair
 4 | pagination_title: Crosshair
 5 | sidebar_label: Crosshair
 6 | description: In this section, we will be customizing the appearance of the crosshair and it's functionality.
 7 | keywords:
 8 |   - customization
 9 |   - appearance
10 |   - styling
11 | pagination_prev: customization/time-scale
12 | pagination_next: customization/second-series
13 | ---
14 | 
15 | import IterativeGuideWarning from './_iterative-guide-warning-partial.mdx';
16 | 
17 | <IterativeGuideWarning/>
18 | 
19 | In this section, we will be customizing the appearance of the crosshair and it's functionality.
20 | 
21 | The crosshair can be customized within the options of the [IChartApi](/docs/api/interfaces/IChartApi) instance. You can view the full set of crosshair options available here: [CrosshairOptions](/docs/api/interfaces/CrosshairOptions).
22 | 
23 | ## Crosshair mode
24 | 
25 | One of the options is `mode` which can be set to the default `magnet` or `normal` ([CrosshairMode](/docs/api/enumerations/CrosshairMode)). Magnet mode snaps the crosshair to data points on the chart such that it is easy to read the exact values on the labels shown on the two scales. However, in some circumstances, it may be more desirable to have a 'free' moving crosshair which can be enabled by setting the value to `normal`. The normal mode will always draw the crosshair at the exact point of the mouse cursor.
26 | 
27 | ## Styling the crosshair
28 | 
29 | The crosshair consists of two lines (vertical and horizontal) which can be individually adjusted with the options set on the `vertLine` and `horzLine` properties respectively. The available options for each crosshair line can be viewed here: [CrosshairLineOptions](/docs/api/interfaces/CrosshairLineOptions).
30 | 
31 | For this example, we will be adjusting the width and line style for the vertical line such that it appears like a spotlight, and adjusting the `color` and `labelBackgroundColor` for both lines so that they better match our color scheme.
32 | 
33 | You can add the following code anywhere below the creation of the `chart` reference. (directly after we set the price formatter and before we add the candlestick series will do nicely so that our chart options are kept together in the code)
34 | 
35 | ```js
36 | // Customizing the Crosshair
37 | chart.applyOptions({
38 |     crosshair: {
39 |         // Change mode from default 'magnet' to 'normal'.
40 |         // Allows the crosshair to move freely without snapping to datapoints
41 |         mode: LightweightCharts.CrosshairMode.Normal,
42 | 
43 |         // Vertical crosshair line (showing Date in Label)
44 |         vertLine: {
45 |             width: 8,
46 |             color: '#C3BCDB44',
47 |             style: LightweightCharts.LineStyle.Solid,
48 |             labelBackgroundColor: '#9B7DFF',
49 |         },
50 | 
51 |         // Horizontal crosshair line (showing Price in Label)
52 |         horzLine: {
53 |             color: '#9B7DFF',
54 |             labelBackgroundColor: '#9B7DFF',
55 |         },
56 |     },
57 | });
58 | ```
59 | 
60 | ## Result
61 | 
62 | At this point we should have a chart like this:
63 | 
64 | <iframe
65 |     className="standalone-iframe"
66 |     src={require('!!file-loader!./assets/step7.html').default}
67 | ></iframe>
68 | <a href={require('!!file-loader!./assets/step7.html').default} target="\_blank">
69 |     View in a new window
70 | </a>
71 | 
72 | ## Next steps
73 | 
74 | In the next step, we will be adding a second series to the chart such that we can add a subtle gradient effect below the candlestick series.
75 | 
76 | ## Download
77 | 
78 | You can download the HTML file for example at this stage <a href={require('!!file-loader!./assets/step7.html').default} download="customization-tutorial-step7.html" target="\_blank">here</a> in case you've encountered a problem or would like to start the next step from this point.
79 | 
80 | ## Complete code
81 | 
82 | import CodeBlock from '@theme/CodeBlock';
83 | import code from '!!raw-loader!./assets/step7.html';
84 | import InstantDetails from '@site/src/components/InstantDetails'
85 | 
86 | <InstantDetails>
87 | <summary>
88 | Click here to reveal the complete code for the example at this stage of the guide.
89 | </summary>
90 | <CodeBlock className="language-html">{code}</CodeBlock>
91 | </InstantDetails>
92 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/data-points.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 9
 3 | title: Data points
 4 | pagination_title: Data points
 5 | sidebar_label: Data points
 6 | description: In this section, we will modify the candlestick data such that we can individually set the color for each candlestick.
 7 | keywords:
 8 |   - customization
 9 |   - appearance
10 |   - styling
11 | pagination_prev: customization/second-series
12 | pagination_next: customization/finishing-touches
13 | ---
14 | 
15 | import IterativeGuideWarning from './_iterative-guide-warning-partial.mdx';
16 | 
17 | <IterativeGuideWarning/>
18 | 
19 | In this section, we will modify the candlestick data such that we can individually set the color for each candlestick.
20 | 
21 | If we take a look at the interface for the candlestick data here: [CandlestickData](/docs/api/interfaces/CandlestickData), we can see a few properties related to color: `color`, `borderColor`, and `wickColor`. Lightweight Charts™ allows the data points to override the colors specified for series as a whole. In other words, if a datapoint has one of these properties set then it will use that color for that data point instead of the colors used for the rest of the series. We can use this feature to highlight a few key data points in a different color.
22 | 
23 | We are going to change the color of all data points which have a `close` value over `205` to orange. We will use the map higher-order function to go through each data point and either leave it alone if it is below `205` or otherwise add the `color` and `wickColor` properties (set to 'orange'). We don't need to set the `borderColor` because we disabled that in an earlier step.
24 | 
25 | We are going to **replace** the following line of code:
26 | 
27 | ```js
28 | const candleStickData = generateCandlestickData();
29 | ```
30 | 
31 | with this block of code:
32 | 
33 | ```js
34 | // Generate sample data to use within a candlestick series
35 | const candleStickData = generateCandlestickData().map(datapoint => {
36 |     // map function is changing the color for the individual
37 |     // candlestick points that close above 205
38 |     if (datapoint.close < 205) { return datapoint; }
39 |     // we are adding 'color' and 'wickColor' properties to the datapoint.
40 |     // Using spread syntax: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#spread_in_object_literals
41 |     return { ...datapoint, color: 'orange', wickColor: 'orange' };
42 | });
43 | ```
44 | 
45 | ## Result
46 | 
47 | At this point we should have a chart like this (with a few candlesticks in orange):
48 | 
49 | <iframe
50 |     className="standalone-iframe"
51 |     src={require('!!file-loader!./assets/step9.html').default}
52 | ></iframe>
53 | <a href={require('!!file-loader!./assets/step9.html').default} target="\_blank">
54 |     View in a new window
55 | </a>
56 | 
57 | ## Next steps
58 | 
59 | In the next step, we will add a few finishing touches to the chart.
60 | 
61 | ## Download
62 | 
63 | You can download the HTML file for example at this stage <a href={require('!!file-loader!./assets/step9.html').default} download="customization-tutorial-step9.html" target="\_blank">here</a> in case you've encountered a problem or would like to start the next step from this point.
64 | 
65 | ## Complete code
66 | 
67 | import CodeBlock from '@theme/CodeBlock';
68 | import code from '!!raw-loader!./assets/step9.html';
69 | import InstantDetails from '@site/src/components/InstantDetails'
70 | 
71 | <InstantDetails>
72 | <summary>
73 | Click here to reveal the complete code for the example at this stage of the guide.
74 | </summary>
75 | <CodeBlock className="language-html">{code}</CodeBlock>
76 | </InstantDetails>
77 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/finishing-touches.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 10
 3 | title: Finishing touches
 4 | pagination_title: Finishing touches
 5 | sidebar_label: Finishing touches
 6 | description: In this section we are going to add a few finishing touches to the chart which are entirely optional.
 7 | keywords:
 8 |   - customization
 9 |   - appearance
10 |   - styling
11 | pagination_prev: customization/data-points
12 | pagination_next: customization/conclusion
13 | ---
14 | 
15 | import IterativeGuideWarning from './_iterative-guide-warning-partial.mdx';
16 | 
17 | <IterativeGuideWarning/>
18 | 
19 | In this section we are going to add a few finishing touches to the chart which are entirely optional.
20 | 
21 | ## Changing the font
22 | 
23 | It is possible to specify a custom font to use within the Lightweight Charts™. As an example we are going to load the `Roboto` font from [Google Fonts](https://fonts.google.com/) by adding the following tags within the `<head>` element on the page (for example, just below the `<title>` element).
24 | 
25 | ```html
26 | <title>Lightweight Charts Customization Tutorial</title>
27 | <!-- Adding Google Font -->
28 | <link rel="preconnect" href="https://fonts.googleapis.com" />
29 | <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
30 | <link
31 |     href="https://fonts.googleapis.com/css2?family=Roboto&display=swap"
32 |     rel="stylesheet"
33 | />
34 | ```
35 | 
36 | We can then tell Lightweight Charts™ to use that specific font by setting the `fontFamily` property within the `layout` property of the chart options as follows:
37 | 
38 | ```js
39 | // Changing the font
40 | chart.applyOptions({
41 |     layout: {
42 |         fontFamily: "'Roboto', sans-serif",
43 |     },
44 | });
45 | ```
46 | 
47 | ## Result
48 | 
49 | 🎉 Congrats! At this point you should have the final chart which looks like this:
50 | 
51 | <iframe
52 |     className="standalone-iframe"
53 |     src={require('!!file-loader!./assets/step10.html').default}
54 | ></iframe>
55 | <a href={require('!!file-loader!./assets/step10.html').default} target="\_blank">
56 |     View in a new window
57 | </a>
58 | 
59 | ## Download
60 | 
61 | You can download the HTML file for example at this stage <a href={require('!!file-loader!./assets/step10.html').default} download="customization-tutorial-step10.html" target="\_blank">here</a> in case you've encountered a problem or would like to start the next step from this point.
62 | 
63 | ## Complete code
64 | 
65 | import CodeBlock from '@theme/CodeBlock';
66 | import code from '!!raw-loader!./assets/step10.html';
67 | import InstantDetails from '@site/src/components/InstantDetails'
68 | 
69 | <InstantDetails>
70 | <summary>
71 | Click here to reveal the complete code for the example at this stage of the guide.
72 | </summary>
73 | <CodeBlock className="language-html">{code}</CodeBlock>
74 | </InstantDetails>
75 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/intro.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 0
 3 | sidebar_label: Introduction
 4 | pagination_title: Introduction
 5 | title: Customizing the Chart
 6 | description: This tutorial provides an introduction to customizing Lightweight Chart's appearance and functionality.
 7 | keywords:
 8 |   - customization
 9 |   - appearance
10 |   - styling
11 | pagination_prev: null
12 | pagination_next: customization/creating-a-chart
13 | ---
14 | 
15 | # Customization - Introduction
16 | 
17 | This tutorial provides an introduction to customizing Lightweight Charts™ appearance and functionality. It is not meant as an exhaustive tutorial but rather as a guided tour on how and where to apply options within the API to adjust specific parts of the chart. Along the way, we will provide links to the API documentation which outline the full set of options available for each part of the chart. It is highly recommended that you explore these API links to discover the wide range of possible customization and feature flags contained within Lightweight Charts™.
18 | 
19 | ## What we will be building
20 | 
21 | Before we get started, let us have a look at what we will be building in this tutorial.
22 | 
23 | {/*
24 |   note: iframe won't display correctly when using `docusaurus serve`,
25 |   however it works correctly when hosted. https://github.com/facebook/docusaurus/issues/7991
26 | */}
27 | 
28 | <iframe
29 |     className="standalone-iframe"
30 |     src={require('!!file-loader!./assets/step10.html').default}
31 | ></iframe>
32 | <a href={require('!!file-loader!./assets/step10.html').default} target="\_blank">
33 |     View in a new window
34 | </a>
35 | 
36 | ## Topics to be covered
37 | 
38 | The following topics will be covered within the tutorial:
39 | 
40 | - Styling the main chart
41 | - Styling a series
42 | - Setting a custom price formatter
43 | - Adjusting the Price Scale
44 | - Adjusting the Time Scale
45 | - Customising the Crosshair
46 | - Adding a second series
47 | - Customising the appearance of a few data points
48 | - Setting a different font
49 | 
50 | ## Prerequisite knowledge
51 | 
52 | The tutorial requires basic knowledge of:
53 | 
54 | - Javascript
55 | - HTML
56 | - CSS
57 | 
58 | :::tip
59 | 
60 | The tutorial will assume that you've already read the [Getting Started](/docs) section even though we may repeat a few aspects from that guide.
61 | 
62 | :::
63 | 
64 | ## Terminology
65 | 
66 | - **Data Series (aka data/dataset):** A collection of data points representing a specific metric over time.
67 | - **Series Type:** A series type specifies how to draw the data on the chart. For example, a line series type will plot the data series on the chart as a series of the data points connected by straight line segments. Available series types: [Series types | Lightweight Charts](/docs/series-types)
68 | - **Series:** A combination of a specified series type and a data series.
69 | - **Price Scale:** Price Scale (or price axis) is a vertical scale that mostly maps prices to coordinates and vice versa.
70 | - **Time Scale:** Time scale (or time axis) is a horizontal scale at the bottom of the chart that displays the time of bars.
71 | - **Crosshair:** Thin vertical and horizontal lines centered on a data point in the chart.
72 | 
73 | ## How to set up the example so you can follow along
74 | 
75 | This guide makes use of a single HTML file which you can download to your computer and run in the browser without the need for any build steps or web servers. The only thing required is an active internet connection such that the Lightweight Charts™ library can be downloaded from the CDN.
76 | 
77 | Provided below is the 'starting point' file for the guide which is a simple HTML page scaffolded out with a single div element (`#container`) and a JS function to generate the sample data set. **At this point, you won't see anything on the page until we add the chart in the next step.**
78 | 
79 | You can either:
80 | 
81 | - <a href={require('!!file-loader!./assets/start.html').default} download="customization-tutorial-start.html" target="\_blank">Download the file</a> and then edit and run the example on your computer,
82 | - or [open this JSFiddle](https://jsfiddle.net/TradingView/5h76xeqk/) and then edit and run the example within the browser.
83 | 
84 | {/* replace JSFiddle link above with one created using TradingView account */}
85 | 
86 | :::tip
87 | 
88 | At the end of each section will be a link to download the example at that stage of the guide, and a full code block.
89 | 
90 | :::
91 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/price-format.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 4
 3 | title: Price format
 4 | pagination_title: Price format
 5 | sidebar_label: Price format
 6 | description: In this section, we will be replacing the default price formatter function with our implementation.
 7 | keywords:
 8 |   - customization
 9 |   - appearance
10 |   - styling
11 | pagination_prev: customization/series
12 | pagination_next: customization/price-scale
13 | ---
14 | 
15 | import IterativeGuideWarning from './_iterative-guide-warning-partial.mdx';
16 | 
17 | <IterativeGuideWarning/>
18 | 
19 | In this section, we will be replacing the default price formatter function with our implementation. Currently, the prices on the chart are been shown with two decimal places and without a currency symbol. Let's implement a formatter which will format the number correctly based on their current locale and present it as the Euro currency.
20 | 
21 | ## Price Formatter functions
22 | 
23 | To provide a price formatter, we need to create a function which accepts a `number` as the input and returns a `string` as the output. A simple price formatter which takes a number and returns the number (as a string) formatted with two decimal points would look as follows:
24 | 
25 | ```js
26 | const myPriceFormatter = p => p.toFixed(2);
27 | ```
28 | 
29 | We can make use of the built-in functionality provided by the browser to build a more versatile price formatter by using the [Intl.NumberFormat API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat).
30 | 
31 | ```js
32 | // Get the current users primary locale
33 | const currentLocale = window.navigator.languages[0];
34 | // Create a number format using Intl.NumberFormat
35 | const myPriceFormatter = Intl.NumberFormat(currentLocale, {
36 |     style: 'currency',
37 |     currency: 'EUR', // Currency for data points
38 | }).format;
39 | ```
40 | 
41 | First, we are grabbing the primary locale for the current user which will pass into the `Intl.NumberFormat` constructor. The constructor takes a second argument for options where we can specify the `style` and `currency` properties. The instance created contains a `format` method which we can then pass into Lightweight Charts™ as shown below).
42 | 
43 | ## Setting the price formatter
44 | 
45 | We can set the default price formatter to be used throughout the chart by passing our own custom price formatter function into the `priceformatter` property of the `localization` property ([LocalizationOptions](/docs/api/interfaces/LocalizationOptions)) within the chart options.
46 | 
47 | ```js
48 | // Apply the custom priceFormatter to the chart
49 | chart.applyOptions({
50 |     localization: {
51 |         priceFormatter: myPriceFormatter,
52 |     },
53 | });
54 | ```
55 | 
56 | Price values displayed on the vertical price scale will now be displayed as Euros.
57 | 
58 | Price formatters can also be applied to each series individually by adjusting the [priceformat](/docs/api/interfaces/SeriesOptionsCommon#priceformat) property of the series options.
59 | 
60 | ## Built-in price formatting
61 | 
62 | Lightweight Charts™ includes a few options to adjust the built-in price formatting which can be see here: [PriceFormatBuiltIn](/docs/api/interfaces/PriceFormatBuiltIn).
63 | 
64 | ## Result
65 | 
66 | At this point we should have a chart like this:
67 | 
68 | <iframe
69 |     className="standalone-iframe"
70 |     src={require('!!file-loader!./assets/step4.html').default}
71 | ></iframe>
72 | <a href={require('!!file-loader!./assets/step4.html').default} target="\_blank">
73 |     View in a new window
74 | </a>
75 | 
76 | ## Next steps
77 | 
78 | In the next step, we will be making some adjustments to the functionality of the vertical price scale.
79 | 
80 | ## Download
81 | 
82 | You can download the HTML file for example at this stage <a href={require('!!file-loader!./assets/step4.html').default} download="customization-tutorial-step4.html" target="\_blank">here</a> in case you've encountered a problem or would like to start the next step from this point.
83 | 
84 | ## Complete code
85 | 
86 | import CodeBlock from '@theme/CodeBlock';
87 | import code from '!!raw-loader!./assets/step4.html';
88 | import InstantDetails from '@site/src/components/InstantDetails'
89 | 
90 | <InstantDetails>
91 | <summary>
92 | Click here to reveal the complete code for the example at this stage of the guide.
93 | </summary>
94 | <CodeBlock className="language-html">{code}</CodeBlock>
95 | </InstantDetails>
96 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/price-scale.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 5
 3 | title: Price scale
 4 | pagination_title: Price scale
 5 | sidebar_label: Price scale
 6 | description: In this section, we are going to adjust the functionality of the vertical price scale.
 7 | keywords:
 8 |   - customization
 9 |   - appearance
10 |   - styling
11 | pagination_prev: customization/price-format
12 | pagination_next: customization/time-scale
13 | ---
14 | 
15 | import IterativeGuideWarning from './_iterative-guide-warning-partial.mdx';
16 | 
17 | <IterativeGuideWarning/>
18 | 
19 | In this section, we are going to adjust the functionality of the vertical price scale. Currently, the price scale will auto-scale to fit the visible data on the chart. You can observe this behaviour by scrolling the chart to the right such that some of the data points are no longer visible. We will disable this feature such that the price scale can only be manually adjusted by the user (by clicking and dragging on the scale).
20 | 
21 | :::tip
22 | 
23 | A chart can have more than one price scale and their options can be individually adjusted, however in this example we only have one price scale.
24 | 
25 | :::
26 | 
27 | ## Adjusting settings for the price scale
28 | 
29 | We can get the current [IPriceScaleApi](/docs/api/interfaces/IPriceScaleApi) instance for the chart by evoking the `priceScale()` method on the candlestick series reference.
30 | 
31 | Once again, we can use the `applyOptions()` method on this API instance to adjust it's options. You can add the following code to the example at any point after the `mainSeries` reference has been created, so let us place it at the end of the script. The options available are shown here: [PriceScaleOptions](/docs/api/interfaces/PriceScaleOptions).
32 | 
33 | ```js
34 | // Adjust the options for the priceScale of the mainSeries
35 | mainSeries.priceScale().applyOptions({
36 |     autoScale: false, // disables auto scaling based on visible content
37 |     scaleMargins: {
38 |         top: 0.1,
39 |         bottom: 0.2,
40 |     },
41 | });
42 | ```
43 | 
44 | As discussed above we are disabling the `autoScale` feature on this price scale. We are additionally adjusting the `scaleMargins` which are used when the chart is first rendered to determine the 'zoom' and position of the scale. The scale margins set the proportion of the chart to be empty above and below the data points currently visible.
45 | 
46 | ## Result
47 | 
48 | At this point, we should have a chart like the one presented below. Play around with scrolling the data left and right to see the change of behaviour versus the previous step.
49 | 
50 | ### Before
51 | 
52 | <iframe
53 |     className="standalone-iframe"
54 |     src={require('!!file-loader!./assets/step4.html').default}
55 | ></iframe>
56 | 
57 | ### After
58 | 
59 | <iframe
60 |     className="standalone-iframe"
61 |     src={require('!!file-loader!./assets/step5.html').default}
62 | ></iframe>
63 | <a href={require('!!file-loader!./assets/step5.html').default} target="\_blank">
64 |     View in a new window
65 | </a>
66 | 
67 | ## Next steps
68 | 
69 | In the next step, we will be adjusting the settings on the horizontal time scale.
70 | 
71 | ## Download
72 | 
73 | You can download the HTML file for example at this stage <a href={require('!!file-loader!./assets/step5.html').default} download="customization-tutorial-step5.html" target="\_blank">here</a> in case you've encountered a problem or would like to start the next step from this point.
74 | 
75 | ## Complete code
76 | 
77 | import CodeBlock from '@theme/CodeBlock';
78 | import code from '!!raw-loader!./assets/step5.html';
79 | import InstantDetails from '@site/src/components/InstantDetails'
80 | 
81 | <InstantDetails>
82 | <summary>
83 | Click here to reveal the complete code for the example at this stage of the guide.
84 | </summary>
85 | <CodeBlock className="language-html">{code}</CodeBlock>
86 | </InstantDetails>
87 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/second-series.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_position: 8
  3 | title: Adding a second series
  4 | pagination_title: Adding a second series
  5 | sidebar_label: Adding a second series
  6 | description: In this section, we will be adding an area series to the chart with a subtle vertical gradient.
  7 | keywords:
  8 |   - customization
  9 |   - appearance
 10 |   - styling
 11 | pagination_prev: customization/crosshair
 12 | pagination_next: customization/data-points
 13 | ---
 14 | 
 15 | import IterativeGuideWarning from './_iterative-guide-warning-partial.mdx';
 16 | 
 17 | <IterativeGuideWarning/>
 18 | 
 19 | In this section, we will be adding an [area series](/docs/series-types#area) to the chart with a subtle vertical gradient. It's purpose is solely for aesthetic reasons (only to make the chart more visually appealing). However, it will teach us a few key points about the differences between different series types and the visual stacking order.
 20 | 
 21 | ## Preparing the data for the area series
 22 | 
 23 | The data structure required for the area series isn't the same as for the candlestick series. The area series is expecting each data point to have the following properties: `time` and `value`. Whereas the candlestick data points don't have a `value` property but rather the following properties: `open`, `close`, `high`, `low`, and `time`.
 24 | 
 25 | We can create a copy of the candlestick data and transform it in a single step by using a `map` higher-order function ([more info](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)). We will set the `value` for the area series as the midpoint between the `open` and `close` values of the candlestick data points.
 26 | 
 27 | ```js
 28 | // Generate sample data to use within a candlestick series
 29 | const candleStickData = generateCandlestickData();
 30 | 
 31 | // highlight-start
 32 | // Convert the candlestick data for use with a line series
 33 | const lineData = candleStickData.map(datapoint => ({
 34 |     time: datapoint.time,
 35 |     value: (datapoint.close + datapoint.open) / 2,
 36 | }));
 37 | // highlight-end
 38 | ```
 39 | 
 40 | ## Adding the area series and setting it's options
 41 | 
 42 | We can add the area series as we did with the candlestick series by calling the `addSeries(AreaSeries)` method on the chart instance. We will pass the options for the series as the second argument to `addSeries()` method instead of separately calling `applyOptions()` at a later stage.
 43 | 
 44 | :::caution
 45 | 
 46 | Make sure to add this code **before** the `addSeries(CandlestickSeries)` call already in the code because we want it to appear below the candlesticks (as explained in the next section).
 47 | 
 48 | :::
 49 | 
 50 | ```js
 51 | // Convert the candlestick data for use with a line series
 52 | const lineData = candleStickData.map(datapoint => ({
 53 |     time: datapoint.time,
 54 |     value: (datapoint.close + datapoint.open) / 2,
 55 | }));
 56 | 
 57 | // highlight-start
 58 | // Add an area series to the chart,
 59 | // Adding this before we add the candlestick chart
 60 | // so that it will appear beneath the candlesticks
 61 | const areaSeries = chart.addSeries(AreaSeries, {
 62 |     lastValueVisible: false, // hide the last value marker for this series
 63 |     crosshairMarkerVisible: false, // hide the crosshair marker for this series
 64 |     lineColor: 'transparent', // hide the line
 65 |     topColor: 'rgba(56, 33, 110,0.6)',
 66 |     bottomColor: 'rgba(56, 33, 110, 0.1)',
 67 | });
 68 | // Set the data for the Area Series
 69 | areaSeries.setData(lineData);
 70 | // highlight-end
 71 | 
 72 | // Create the Main Series (Candlesticks)
 73 | const mainSeries = chart.addSeries(CandlestickSeries);
 74 | ```
 75 | 
 76 | ## Visual stacking order of series
 77 | 
 78 | When adding multiple series to a single chart, it is important to take note of the order in which they are added because that will determine the visual stacking order (when they overlap). The first series added will appear at the bottom of the stack and each series added will be placed on top of the stack. Thus in the current example, we want the area series to appear below the candlestick series so we will make sure to first add the area series and then the candlestick series.
 79 | 
 80 | ## Result
 81 | 
 82 | At this point we should have a chart like this:
 83 | 
 84 | <iframe
 85 |     className="standalone-iframe"
 86 |     src={require('!!file-loader!./assets/step8.html').default}
 87 | ></iframe>
 88 | <a href={require('!!file-loader!./assets/step8.html').default} target="\_blank">
 89 |     View in a new window
 90 | </a>
 91 | 
 92 | ## Next steps
 93 | 
 94 | In the next step, we will look at how to adjust the colour of individual candlesticks on our chart.
 95 | 
 96 | ## Download
 97 | 
 98 | You can download the HTML file for example at this stage <a href={require('!!file-loader!./assets/step8.html').default} download="customization-tutorial-step8.html" target="\_blank">here</a> in case you've encountered a problem or would like to start the next step from this point.
 99 | 
100 | ## Complete code
101 | 
102 | import CodeBlock from '@theme/CodeBlock';
103 | import code from '!!raw-loader!./assets/step8.html';
104 | import InstantDetails from '@site/src/components/InstantDetails'
105 | 
106 | <InstantDetails>
107 | <summary>
108 | Click here to reveal the complete code for the example at this stage of the guide.
109 | </summary>
110 | <CodeBlock className="language-html">{code}</CodeBlock>
111 | </InstantDetails>
112 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/series.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 3
 3 | title: Series colors
 4 | pagination_title: Series colors
 5 | sidebar_label: Series colors
 6 | description: In this section, we will be customizing the visual styling of the candlestick series.
 7 | keywords:
 8 |   - customization
 9 |   - appearance
10 |   - styling
11 | pagination_prev: customization/chart-colors
12 | pagination_next: customization/price-format
13 | ---
14 | 
15 | import IterativeGuideWarning from './_iterative-guide-warning-partial.mdx';
16 | 
17 | <IterativeGuideWarning/>
18 | 
19 | In this section, we will be customizing the visual styling of the candlestick series.
20 | 
21 | We can add our custom options to the series by using the `applyOptions` method on the ISeriesApi instance for the candlestick series. In other words, we can call the `applyOptions` method on the `mainSeries` variable (which was returned when we evoked `addSeries(CandlestickSeries)` earlier).
22 | 
23 | The available options for the candlestick series is a combination of the following interfaces: [CandlestickStyleOptions](/docs/api/interfaces/CandlestickStyleOptions) and [SeriesOptionsCommon](/docs/api/interfaces/SeriesOptionsCommon).
24 | 
25 | ## Setting custom colors for the candlestick series
26 | 
27 | We are going to set the colors such that upward candles will be a light blue and downward candles will be a vibrant red. The color for the body of the candle is determined by the `upColor` and `downColor` properties, whilst the wick colors are determined by `wickUpColor` and `wickDownColor`. We will additionally disable the border on the candlestick for this example.
28 | 
29 | We can apply these options at any point in the code after we have created the candlestick series, and in this case, we will place the code below the `setData()` call (but it would still work if was placed before).
30 | 
31 | ```js
32 | mainSeries.setData(candleStickData);
33 | 
34 | // highlight-start
35 | // Changing the Candlestick colors
36 | mainSeries.applyOptions({
37 |     wickUpColor: 'rgb(54, 116, 217)',
38 |     upColor: 'rgb(54, 116, 217)',
39 |     wickDownColor: 'rgb(225, 50, 85)',
40 |     downColor: 'rgb(225, 50, 85)',
41 |     borderVisible: false,
42 | });
43 | // highlight-end
44 | ```
45 | 
46 | ## Result
47 | 
48 | At this point we should have a chart like this:
49 | 
50 | <iframe
51 |     className="standalone-iframe"
52 |     src={require('!!file-loader!./assets/step3.html').default}
53 | ></iframe>
54 | <a href={require('!!file-loader!./assets/step3.html').default} target="\_blank">
55 |     View in a new window
56 | </a>
57 | 
58 | ## Next steps
59 | 
60 | In the next step, we will set a price formatter so we can customize the formatting of numbers on the chart.
61 | 
62 | ## Download
63 | 
64 | You can download the HTML file for example at this stage <a href={require('!!file-loader!./assets/step3.html').default} download="customization-tutorial-step3.html" target="\_blank">here</a> in case you've encountered a problem or would like to start the next step from this point.
65 | 
66 | ## Complete code
67 | 
68 | import CodeBlock from '@theme/CodeBlock';
69 | import code from '!!raw-loader!./assets/step3.html';
70 | import InstantDetails from '@site/src/components/InstantDetails'
71 | 
72 | <InstantDetails>
73 | <summary>
74 | Click here to reveal the complete code for the example at this stage of the guide.
75 | </summary>
76 | <CodeBlock className="language-html">{code}</CodeBlock>
77 | </InstantDetails>
78 | 


--------------------------------------------------------------------------------
/website/tutorials/customization/time-scale.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 6
 3 | title: Time scale
 4 | pagination_title: Time scale
 5 | sidebar_label: Time scale
 6 | description: In the previous step, we adjusted the vertical price scale, now let us adjust the horizontal time scale.
 7 | keywords:
 8 |   - customization
 9 |   - appearance
10 |   - styling
11 | pagination_prev: customization/price-scale
12 | pagination_next: customization/crosshair
13 | ---
14 | 
15 | import IterativeGuideWarning from './_iterative-guide-warning-partial.mdx';
16 | 
17 | <IterativeGuideWarning/>
18 | 
19 | In the previous step, we adjusted the vertical price scale, now let us adjust the horizontal time scale. We previously adjusted the border color of this scale and now we are going to adjust the starting 'zoom' level.
20 | 
21 | We will be adjusting the [`barSpacing`](/docs/api/interfaces/TimeScaleOptions#barspacing) option on the time scale which is used when the chart is first rendered to determine the horizontal 'zoom' level. The property sets 'The space between bars in pixels.', where a larger number will result in wider bars and fewer bars visible on the chart. The default value is `6` and we will be increasing it to `10` which will effectively 'zoom in' for the time scale.
22 | 
23 | ## Adjusting settings for the time scale
24 | 
25 | We can get the [ITimeScaleApi](/docs/api/interfaces/ITimeScaleApi) instance for the chart by evoking the `timeScale()` method on the chart reference.
26 | 
27 | Just as with the previous step, we can use the `applyOptions()` method on this API instance to adjust it's options. You can add the following code to the example at any point after the `chart` reference has been created, but we will place it directly below where we set the border color for the time scale. The options available are shown here: [TimeScaleOptions](/docs/api/interfaces/TimeScaleOptions).
28 | 
29 | ```js
30 | // Setting the border color for the horizontal axis
31 | chart.timeScale().applyOptions({
32 |     borderColor: '#71649C',
33 | });
34 | 
35 | // highlight-start
36 | // Adjust the starting bar width (essentially the horizontal zoom)
37 | chart.timeScale().applyOptions({
38 |     barSpacing: 10,
39 | });
40 | // highlight-end
41 | ```
42 | 
43 | The `applyOptions()` calls on the time scale were purposely split into two to show that it is possible to apply the options individually if that leads to cleaner code to read. It is also possible to apply both options in a single step as shown below:
44 | 
45 | ```js
46 | // Example of applying both properties in a single call
47 | chart.timeScale().applyOptions({
48 |     borderColor: '#71649C',
49 |     barSpacing: 10,
50 | });
51 | ```
52 | 
53 | ## Auto fitting all the content
54 | 
55 | It is possible to auto fit all the content into the visable area of the chart by calling the [`fitContent()`](/docs/api/interfaces/ITimeScaleApi#fitcontent) method on the time scale instance, for example: `chart.timeScale().fitContent();`
56 | 
57 | ## Result
58 | 
59 | At this point we should have a chart like this (noting the wider candlestick bars):
60 | 
61 | <iframe
62 |     className="standalone-iframe"
63 |     src={require('!!file-loader!./assets/step6.html').default}
64 | ></iframe>
65 | <a href={require('!!file-loader!./assets/step6.html').default} target="\_blank">
66 |     View in a new window
67 | </a>
68 | 
69 | ## Next steps
70 | 
71 | In the next step, we will be adjusting the visual style and behaviour of the crosshair.
72 | 
73 | ## Download
74 | 
75 | You can download the HTML file for example at this stage <a href={require('!!file-loader!./assets/step6.html').default} download="customization-tutorial-step6.html" target="\_blank">here</a> in case you've encountered a problem or would like to start the next step from this point.
76 | 
77 | ## Complete code
78 | 
79 | import CodeBlock from '@theme/CodeBlock';
80 | import code from '!!raw-loader!./assets/step6.html';
81 | import InstantDetails from '@site/src/components/InstantDetails'
82 | 
83 | <InstantDetails>
84 | <summary>
85 | Click here to reveal the complete code for the example at this stage of the guide.
86 | </summary>
87 | <CodeBlock className="language-html">{code}</CodeBlock>
88 | </InstantDetails>
89 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/.eslintrc.js:
--------------------------------------------------------------------------------
 1 | module.exports = {
 2 | 	globals: {
 3 | 		document: false,
 4 | 		createChart: false,
 5 | 		createYieldCurveChart: false,
 6 | 		createUpDownMarkers: false,
 7 | 		LineSeries: false,
 8 | 		AreaSeries: false,
 9 | 		BarSeries: false,
10 | 		BaselineSeries: false,
11 | 		CandlestickSeries: false,
12 | 		HistogramSeries: false,
13 | 	},
14 | };
15 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/compare-multiple-series.js:
--------------------------------------------------------------------------------
 1 | // remove-start
 2 | // Lightweight Charts™ Example: Compare multiple series
 3 | // https://tradingview.github.io/lightweight-charts/tutorials/how_to/compare-multiple-series
 4 | 
 5 | // remove-end
 6 | // hide-start
 7 | let randomFactor = 25 + Math.random() * 25;
 8 | const samplePoint = i =>
 9 | 	i *
10 | 		(0.5 +
11 | 			Math.sin(i / 10) * 0.2 +
12 | 			Math.sin(i / 20) * 0.4 +
13 | 			Math.sin(i / randomFactor) * 0.8 +
14 | 			Math.sin(i / 500) * 0.5) +
15 | 	200;
16 | 
17 | function generateLineData(numberOfPoints = 500) {
18 | 	randomFactor = 25 + Math.random() * 25;
19 | 	const res = [];
20 | 	const date = new Date(Date.UTC(2018, 0, 1, 12, 0, 0, 0));
21 | 	for (let i = 0; i < numberOfPoints; ++i) {
22 | 		const time = (date.getTime() / 1000);
23 | 		const value = samplePoint(i);
24 | 		res.push({
25 | 			time,
26 | 			value,
27 | 		});
28 | 
29 | 		date.setUTCDate(date.getUTCDate() + 1);
30 | 	}
31 | 
32 | 	return res;
33 | }
34 | // hide-end
35 | const chartOptions = {
36 | 	layout: {
37 | 		textColor: CHART_TEXT_COLOR,
38 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
39 | 	},
40 | };
41 | // remove-line
42 | /** @type {import('lightweight-charts').IChartApi} */
43 | const chart = createChart(document.getElementById('container'), chartOptions);
44 | 
45 | const lineSeriesOne = chart.addSeries(LineSeries, { color: LINE_LINE_COLOR });
46 | 
47 | const lineSeriesTwo = chart.addSeries(LineSeries, { color: LINE_LINE2_COLOR });
48 | 
49 | const lineSeriesThree = chart.addSeries(LineSeries, { color: LINE_LINE3_COLOR });
50 | 
51 | const lineSeriesOneData = generateLineData();
52 | const lineSeriesTwoData = generateLineData();
53 | const lineSeriesThreeData = generateLineData();
54 | 
55 | lineSeriesOne.setData(lineSeriesOneData);
56 | lineSeriesTwo.setData(lineSeriesTwoData);
57 | lineSeriesThree.setData(lineSeriesThreeData);
58 | 
59 | chart.timeScale().fitContent();
60 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/compare-multiple-series.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Compare multiple series
 3 | sidebar_label: Compare multiple series
 4 | description:
 5 |   An example of how to compare multiple series on a single price scale
 6 | pagination_prev: null
 7 | pagination_next: null
 8 | keywords:
 9 |   - compare
10 |   - series
11 | ---
12 | 
13 | This Multi-Series Comparison Example illustrates how an assortment of data
14 | series can be integrated into a single chart for comparisons. Simply use the
15 | charting API `addSeries` to create multiple series.
16 | 
17 | If you would like an unique price scales for each individual series,
18 | particularly when dealing with data series with divergent value ranges, then
19 | take a look at the [Two Price Scales Example](../how_to/two-price-scales.mdx).
20 | 
21 | import UsageGuidePartial from '../_usage-guide-partial.mdx';
22 | import CodeBlock from '@theme/CodeBlock';
23 | import code from '!!raw-loader!./compare-multiple-series.js';
24 | 
25 | <CodeBlock
26 |   replaceThemeConstants
27 |   chart
28 |   className="language-js"
29 |   hideableCode
30 |   chartOnTop
31 |   codeUsage={<UsageGuidePartial />}
32 | >
33 | 	{code}
34 | </CodeBlock>
35 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/custom-font-family.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Compare mfont family
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/demos/custom-font-family
  4 | 
  5 | // remove-end
  6 | // hide-start
  7 | const chartOptions = {
  8 | 	layout: {
  9 | 		textColor: CHART_TEXT_COLOR,
 10 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
 11 | 	},
 12 | 	height: 200,
 13 | };
 14 | // hide-end
 15 | const container = document.getElementById('container');
 16 | // remove-line
 17 | /** @type {import('lightweight-charts').IChartApi} */
 18 | const chart = createChart(container, chartOptions);
 19 | 
 20 | // remove-start
 21 | // Only needed within demo page
 22 | // eslint-disable-next-line no-undef
 23 | window.addEventListener('resize', () => {
 24 | 	chart.applyOptions({ height: 200 });
 25 | });
 26 | // remove-end
 27 | 
 28 | function setFontFamily(fontFamily) {
 29 | 	// highlight-start
 30 | 	chart.applyOptions({
 31 | 		layout: {
 32 | 			fontFamily: fontFamily,
 33 | 		},
 34 | 	});
 35 | 	// highlight-end
 36 | }
 37 | 
 38 | const candlestickSeries = chart.addSeries(CandlestickSeries, {
 39 | 	upColor: BAR_UP_COLOR,
 40 | 	downColor: BAR_DOWN_COLOR,
 41 | 	borderVisible: false,
 42 | 	wickUpColor: BAR_UP_COLOR,
 43 | 	wickDownColor: BAR_DOWN_COLOR,
 44 | });
 45 | 
 46 | candlestickSeries.setData([
 47 | 	{
 48 | 		close: 108.9974612905403,
 49 | 		high: 121.20998259466148,
 50 | 		low: 96.65376292551082,
 51 | 		open: 104.5614412226746,
 52 | 		time: { year: 2018, month: 9, day: 22 },
 53 | 	},
 54 | 	// hide-start
 55 | 	{
 56 | 		close: 110.46815600023501,
 57 | 		high: 111.3650273696516,
 58 | 		low: 82.65543461471314,
 59 | 		open: 110.16538466099634,
 60 | 		time: { year: 2018, month: 9, day: 23 },
 61 | 	},
 62 | 	{
 63 | 		close: 90.62131977740425,
 64 | 		high: 109.19838270252615,
 65 | 		low: 82.30106956144076,
 66 | 		open: 105.03104735287424,
 67 | 		time: { year: 2018, month: 9, day: 24 },
 68 | 	},
 69 | 	{
 70 | 		close: 96.80120024431532,
 71 | 		high: 101.92074283374939,
 72 | 		low: 89.25819769856513,
 73 | 		open: 89.25819769856513,
 74 | 		time: { year: 2018, month: 9, day: 25 },
 75 | 	},
 76 | 	{
 77 | 		close: 94.87113928076117,
 78 | 		high: 104.12503365679314,
 79 | 		low: 85.42405005240111,
 80 | 		open: 104.12503365679314,
 81 | 		time: { year: 2018, month: 9, day: 26 },
 82 | 	},
 83 | 	{
 84 | 		close: 100.76494087674855,
 85 | 		high: 102.60508417239113,
 86 | 		low: 80.76268547064865,
 87 | 		open: 92.93299948659636,
 88 | 		time: { year: 2018, month: 9, day: 27 },
 89 | 	},
 90 | 	{
 91 | 		close: 101.45855928883597,
 92 | 		high: 110.26727325817173,
 93 | 		low: 91.10348900896837,
 94 | 		open: 93.4362185148034,
 95 | 		time: { year: 2018, month: 9, day: 28 },
 96 | 	},
 97 | 	{
 98 | 		close: 91.68871815146144,
 99 | 		high: 103.73263644407702,
100 | 		low: 73.5329263610334,
101 | 		open: 92.96467883926464,
102 | 		time: { year: 2018, month: 9, day: 29 },
103 | 	},
104 | 	{
105 | 		close: 89.39633140354033,
106 | 		high: 101.06569518834237,
107 | 		low: 81.71149885084162,
108 | 		open: 83.08248758612376,
109 | 		time: { year: 2018, month: 9, day: 30 },
110 | 	},
111 | 	{
112 | 		close: 93.09498513675378,
113 | 		high: 93.09498513675378,
114 | 		low: 76.81138276012628,
115 | 		open: 91.97280452613565,
116 | 		time: { year: 2018, month: 10, day: 1 },
117 | 	},
118 | 	{
119 | 		close: 89.26733004009083,
120 | 		high: 89.26733004009083,
121 | 		low: 76.27851645958225,
122 | 		open: 85.83860311023625,
123 | 		time: { year: 2018, month: 10, day: 2 },
124 | 	},
125 | 	{
126 | 		close: 89.66035763006947,
127 | 		high: 89.66035763006947,
128 | 		low: 67.63677527399729,
129 | 		open: 77.79584976144585,
130 | 		time: { year: 2018, month: 10, day: 3 },
131 | 	},
132 | 	{
133 | 		close: 89.59687813884807,
134 | 		high: 97.05916949817754,
135 | 		low: 72.9823390058379,
136 | 		open: 77.37388423995716,
137 | 		time: { year: 2018, month: 10, day: 4 },
138 | 	},
139 | 	{
140 | 		close: 83.6425403120788,
141 | 		high: 91.72593377862522,
142 | 		low: 65.27208271740422,
143 | 		open: 85.92711686401718,
144 | 		time: { year: 2018, month: 10, day: 5 },
145 | 	},
146 | 	{
147 | 		close: 82.99053929200655,
148 | 		high: 93.4482645370556,
149 | 		low: 65.98920655616067,
150 | 		open: 71.8940788814462,
151 | 		time: { year: 2018, month: 10, day: 6 },
152 | 	},
153 | 	{
154 | 		close: 73.09595957510754,
155 | 		high: 86.65935598412881,
156 | 		low: 62.710852488609326,
157 | 		open: 80.78945254092527,
158 | 		time: { year: 2018, month: 10, day: 7 },
159 | 	},
160 | 	{
161 | 		close: 80.12127692112905,
162 | 		high: 87.49034842093855,
163 | 		low: 60.09987438133361,
164 | 		open: 70.2408873110499,
165 | 		time: { year: 2018, month: 10, day: 8 },
166 | 	},
167 | 	{
168 | 		close: 77.60439116240829,
169 | 		high: 83.20908153481327,
170 | 		low: 68.56836128158209,
171 | 		open: 75.83440719565763,
172 | 		time: { year: 2018, month: 10, day: 9 },
173 | 	},
174 | 	{
175 | 		close: 73.8952889203428,
176 | 		high: 81.89987377779327,
177 | 		low: 57.8891283348631,
178 | 		open: 66.51904017615065,
179 | 		time: { year: 2018, month: 10, day: 10 },
180 | 	},
181 | 	{
182 | 		close: 75.08452506029613,
183 | 		high: 75.08452506029613,
184 | 		low: 59.208194031968155,
185 | 		open: 72.14475369395771,
186 | 		time: { year: 2018, month: 10, day: 11 },
187 | 	},
188 | 	{
189 | 		close: 73.08898607472305,
190 | 		high: 73.08898607472305,
191 | 		low: 63.05632280826725,
192 | 		open: 66.93050765469924,
193 | 		time: { year: 2018, month: 10, day: 12 },
194 | 	},
195 | 	{
196 | 		close: 58.993371469509704,
197 | 		high: 73.08872095153116,
198 | 		low: 53.52204433018574,
199 | 		open: 66.12840939191403,
200 | 		time: { year: 2018, month: 10, day: 13 },
201 | 	},
202 | 	{
203 | 		close: 57.150755012485,
204 | 		high: 74.57414896810235,
205 | 		low: 52.6552427480398,
206 | 		open: 68.50876667562338,
207 | 		time: { year: 2018, month: 10, day: 14 },
208 | 	},
209 | 	{
210 | 		close: 58.03147289822832,
211 | 		high: 69.62445357159157,
212 | 		low: 53.8260018823565,
213 | 		open: 61.62298899368165,
214 | 		time: { year: 2018, month: 10, day: 15 },
215 | 	},
216 | 	{
217 | 		close: 60.6852855399041,
218 | 		high: 69.02095441024431,
219 | 		low: 54.00939224622043,
220 | 		open: 64.81901552322648,
221 | 		time: { year: 2018, month: 10, day: 16 },
222 | 	},
223 | 	{
224 | 		close: 57.508820449565285,
225 | 		high: 63.82926565242872,
226 | 		low: 54.07370975509682,
227 | 		open: 54.07370975509682,
228 | 		time: { year: 2018, month: 10, day: 17 },
229 | 	},
230 | 	{
231 | 		close: 51.60796818909221,
232 | 		high: 64.88712939579875,
233 | 		low: 51.60796818909221,
234 | 		open: 53.489226476218434,
235 | 		time: { year: 2018, month: 10, day: 18 },
236 | 	},
237 | 	{
238 | 		close: 55.139520748382864,
239 | 		high: 59.161320710177925,
240 | 		low: 52.228139922762765,
241 | 		open: 52.228139922762765,
242 | 		time: { year: 2018, month: 10, day: 19 },
243 | 	},
244 | 	{
245 | 		close: 47.47868992247237,
246 | 		high: 58.0836625917653,
247 | 		low: 46.43213518526832,
248 | 		open: 47.59258635788406,
249 | 		time: { year: 2018, month: 10, day: 20 },
250 | 	},
251 | 	{
252 | 		close: 47.22596723150508,
253 | 		high: 51.55468175560989,
254 | 		low: 45.22654435521185,
255 | 		open: 47.452459556200054,
256 | 		time: { year: 2018, month: 10, day: 21 },
257 | 	},
258 | 	{
259 | 		close: 53.39724151191295,
260 | 		high: 58.256006746786035,
261 | 		low: 46.40105667413804,
262 | 		open: 53.41548527476272,
263 | 		time: { year: 2018, month: 10, day: 22 },
264 | 	},
265 | 	{
266 | 		close: 45.015877277800854,
267 | 		high: 51.2955426978105,
268 | 		low: 40.26534748806228,
269 | 		open: 43.90158660063875,
270 | 		time: { year: 2018, month: 10, day: 23 },
271 | 	},
272 | 	{
273 | 		close: 49.307312373439665,
274 | 		high: 49.93643636637581,
275 | 		low: 43.20705757075934,
276 | 		open: 45.672934511555795,
277 | 		time: { year: 2018, month: 10, day: 24 },
278 | 	},
279 | 	{
280 | 		close: 45.15418019295631,
281 | 		high: 48.59676744409583,
282 | 		low: 37.628047445918504,
283 | 		open: 40.33862825788268,
284 | 		time: { year: 2018, month: 10, day: 25 },
285 | 	},
286 | 	{
287 | 		close: 43.2972018283068,
288 | 		high: 43.2972018283068,
289 | 		low: 36.335943004352245,
290 | 		open: 42.605991542720965,
291 | 		time: { year: 2018, month: 10, day: 26 },
292 | 	},
293 | 	{
294 | 		close: 39.1153643552137,
295 | 		high: 44.311406627923844,
296 | 		low: 35.31457011784855,
297 | 		open: 42.00000202357808,
298 | 		time: { year: 2018, month: 10, day: 27 },
299 | 	},
300 | 	{
301 | 		close: 36.06960076896885,
302 | 		high: 42.89041111567749,
303 | 		low: 33.58326637182405,
304 | 		open: 37.40942817102858,
305 | 		time: { year: 2018, month: 10, day: 28 },
306 | 	},
307 | 	{
308 | 		close: 35.8981036950969,
309 | 		high: 42.19793419602979,
310 | 		low: 33.62190962880232,
311 | 		open: 36.87246325249825,
312 | 		time: { year: 2018, month: 10, day: 29 },
313 | 	},
314 | 	{
315 | 		close: 31.378205119641457,
316 | 		high: 37.33501102832602,
317 | 		low: 31.30137162225214,
318 | 		open: 35.651275660713694,
319 | 		time: { year: 2018, month: 10, day: 30 },
320 | 	},
321 | 	{
322 | 		close: 33.574536057730576,
323 | 		high: 37.30152570719593,
324 | 		low: 27.369689193426243,
325 | 		open: 34.330180925654936,
326 | 		time: { year: 2018, month: 10, day: 31 },
327 | 	},
328 | 	{
329 | 		close: 28.91735096504839,
330 | 		high: 32.62196350117741,
331 | 		low: 27.072564759401843,
332 | 		open: 29.398552328599372,
333 | 		time: { year: 2018, month: 11, day: 1 },
334 | 	},
335 | 	{
336 | 		close: 28.44143154172122,
337 | 		high: 31.042019861166594,
338 | 		low: 23.383320830495375,
339 | 		open: 27.275885037308072,
340 | 		time: { year: 2018, month: 11, day: 2 },
341 | 	},
342 | 	{
343 | 		close: 25.92162714418916,
344 | 		high: 30.57604443170622,
345 | 		low: 25.418671641150752,
346 | 		open: 26.775196275924657,
347 | 		time: { year: 2018, month: 11, day: 3 },
348 | 	},
349 | 	{
350 | 		close: 26.376994016637433,
351 | 		high: 28.198647836523744,
352 | 		low: 21.492969733673334,
353 | 		open: 26.27980943059139,
354 | 		time: { year: 2018, month: 11, day: 4 },
355 | 	},
356 | 	{
357 | 		close: 28.60834088674494,
358 | 		high: 28.60834088674494,
359 | 		low: 21.89002840571941,
360 | 		open: 25.376464895884993,
361 | 		time: { year: 2018, month: 11, day: 5 },
362 | 	},
363 | 	{
364 | 		close: 31.103861067101136,
365 | 		high: 31.103861067101136,
366 | 		low: 24.39227668420513,
367 | 		open: 28.994785427089838,
368 | 		time: { year: 2018, month: 11, day: 6 },
369 | 	},
370 | 	{
371 | 		close: 28.6308138310307,
372 | 		high: 35.430817482769164,
373 | 		low: 24.069515410358232,
374 | 		open: 27.109407394069084,
375 | 		time: { year: 2018, month: 11, day: 7 },
376 | 	},
377 | 	{
378 | 		close: 29.468889521733466,
379 | 		high: 37.54082586961352,
380 | 		low: 27.90833873315644,
381 | 		open: 33.16901271715577,
382 | 		time: { year: 2018, month: 11, day: 8 },
383 | 	},
384 | 	{
385 | 		close: 35.887823124204296,
386 | 		high: 39.21804237580939,
387 | 		low: 30.951078044055627,
388 | 		open: 30.951078044055627,
389 | 		time: { year: 2018, month: 11, day: 9 },
390 | 	},
391 | 	{
392 | 		close: 34.361137347097575,
393 | 		high: 35.27083445807796,
394 | 		low: 27.825889562160082,
395 | 		open: 34.86040182980157,
396 | 		time: { year: 2018, month: 11, day: 10 },
397 | 	},
398 | 	{
399 | 		close: 36.61336645243868,
400 | 		high: 40.31460537175622,
401 | 		low: 33.96383400053921,
402 | 		open: 39.70037560142739,
403 | 		time: { year: 2018, month: 11, day: 11 },
404 | 	},
405 | 	{
406 | 		close: 41.321693986803055,
407 | 		high: 44.45481986667003,
408 | 		low: 35.67563772228475,
409 | 		open: 38.67059795413642,
410 | 		time: { year: 2018, month: 11, day: 12 },
411 | 	},
412 | 	{
413 | 		close: 40.15038854039306,
414 | 		high: 41.50912000191902,
415 | 		low: 32.610637769394444,
416 | 		open: 41.50912000191902,
417 | 		time: { year: 2018, month: 11, day: 13 },
418 | 	},
419 | 	{
420 | 		close: 44.092601065208015,
421 | 		high: 44.092601065208015,
422 | 		low: 37.778306506100726,
423 | 		open: 38.99045898154136,
424 | 		time: { year: 2018, month: 11, day: 14 },
425 | 	},
426 | 	{
427 | 		close: 41.42426637839382,
428 | 		high: 44.72189614841937,
429 | 		low: 41.42426637839382,
430 | 		open: 44.72189614841937,
431 | 		time: { year: 2018, month: 11, day: 15 },
432 | 	},
433 | 	{
434 | 		close: 41.19513795258408,
435 | 		high: 49.08084695291049,
436 | 		low: 36.24282165100056,
437 | 		open: 44.909248500660254,
438 | 		time: { year: 2018, month: 11, day: 16 },
439 | 	},
440 | 	{
441 | 		close: 44.24935708161703,
442 | 		high: 53.028535501565486,
443 | 		low: 40.32056743060158,
444 | 		open: 46.198546801109984,
445 | 		time: { year: 2018, month: 11, day: 17 },
446 | 	},
447 | 	{
448 | 		close: 43.18555863372182,
449 | 		high: 52.34250206788521,
450 | 		low: 43.18555863372182,
451 | 		open: 49.58135271619679,
452 | 		time: { year: 2018, month: 11, day: 18 },
453 | 	},
454 | 	{
455 | 		close: 50.8568887039091,
456 | 		high: 52.60441957102357,
457 | 		low: 39.917719271944364,
458 | 		open: 48.197532365645806,
459 | 		time: { year: 2018, month: 11, day: 19 },
460 | 	},
461 | 	{
462 | 		close: 48.79128595974164,
463 | 		high: 52.45087789296739,
464 | 		low: 46.80633073487828,
465 | 		open: 52.45087789296739,
466 | 		time: { year: 2018, month: 11, day: 20 },
467 | 	},
468 | 	{
469 | 		close: 46.97300046781947,
470 | 		high: 55.80689868049132,
471 | 		low: 46.97300046781947,
472 | 		open: 55.80689868049132,
473 | 		time: { year: 2018, month: 11, day: 21 },
474 | 	},
475 | 	{
476 | 		close: 55.58129861112469,
477 | 		high: 55.58129861112469,
478 | 		low: 49.087279242343996,
479 | 		open: 53.16719476594961,
480 | 		time: { year: 2018, month: 11, day: 22 },
481 | 	},
482 | 	{
483 | 		close: 50.058979311730226,
484 | 		high: 62.55333249171461,
485 | 		low: 50.058979311730226,
486 | 		open: 52.628489607588826,
487 | 		time: { year: 2018, month: 11, day: 23 },
488 | 	},
489 | 	{
490 | 		close: 51.193155229085995,
491 | 		high: 59.08949991997865,
492 | 		low: 51.193155229085995,
493 | 		open: 55.352594157474755,
494 | 		time: { year: 2018, month: 11, day: 24 },
495 | 	},
496 | 	{
497 | 		close: 60.099338327208436,
498 | 		high: 66.93510126958154,
499 | 		low: 55.27299867222781,
500 | 		open: 61.05897620044226,
501 | 		time: { year: 2018, month: 11, day: 25 },
502 | 	},
503 | 	{
504 | 		close: 58.3802630890727,
505 | 		high: 71.50922937699602,
506 | 		low: 50.95210438359451,
507 | 		open: 62.4679688326532,
508 | 		time: { year: 2018, month: 11, day: 26 },
509 | 	},
510 | 	{
511 | 		close: 57.875350873413225,
512 | 		high: 65.59903214448208,
513 | 		low: 57.875350873413225,
514 | 		open: 62.747405667247016,
515 | 		time: { year: 2018, month: 11, day: 27 },
516 | 	},
517 | 	{
518 | 		close: 61.231150731698605,
519 | 		high: 66.3829902228434,
520 | 		low: 61.231150731698605,
521 | 		open: 65.01028486919516,
522 | 		time: { year: 2018, month: 11, day: 28 },
523 | 	},
524 | 	{
525 | 		close: 64.9698540874806,
526 | 		high: 77.09783903299783,
527 | 		low: 58.455031795628194,
528 | 		open: 58.455031795628194,
529 | 		time: { year: 2018, month: 11, day: 29 },
530 | 	},
531 | 	{
532 | 		close: 72.40978471883417,
533 | 		high: 72.40978471883417,
534 | 		low: 53.05804901549206,
535 | 		open: 65.907298021202,
536 | 		time: { year: 2018, month: 11, day: 30 },
537 | 	},
538 | 	{
539 | 		close: 74.60745731538934,
540 | 		high: 78.33742117000789,
541 | 		low: 54.42067144918077,
542 | 		open: 73.20930147914103,
543 | 		time: { year: 2018, month: 12, day: 1 },
544 | 	},
545 | 	{
546 | 		close: 64.10866184869924,
547 | 		high: 76.14506447001202,
548 | 		low: 61.5224432669736,
549 | 		open: 69.33984127682314,
550 | 		time: { year: 2018, month: 12, day: 2 },
551 | 	},
552 | 	{
553 | 		close: 65.92038759928786,
554 | 		high: 76.98479070362022,
555 | 		low: 65.92038759928786,
556 | 		open: 69.32298264631615,
557 | 		time: { year: 2018, month: 12, day: 3 },
558 | 	},
559 | 	{
560 | 		close: 68.23682161095334,
561 | 		high: 77.6723729460968,
562 | 		low: 68.23682161095334,
563 | 		open: 74.39471534484744,
564 | 		time: { year: 2018, month: 12, day: 4 },
565 | 	},
566 | 	{
567 | 		close: 67.45035792565862,
568 | 		high: 83.53728553118547,
569 | 		low: 67.45035792565862,
570 | 		open: 74.79418570077237,
571 | 		time: { year: 2018, month: 12, day: 5 },
572 | 	},
573 | 	{
574 | 		close: 79.26722967320323,
575 | 		high: 79.26722967320323,
576 | 		low: 68.40654829383521,
577 | 		open: 68.40654829383521,
578 | 		time: { year: 2018, month: 12, day: 6 },
579 | 	},
580 | 	{
581 | 		close: 74.95305464030587,
582 | 		high: 81.65884414224071,
583 | 		low: 64.08761481290135,
584 | 		open: 81.65884414224071,
585 | 		time: { year: 2018, month: 12, day: 7 },
586 | 	},
587 | 	{
588 | 		close: 86.30802154315482,
589 | 		high: 91.21953112925642,
590 | 		low: 65.46112304993535,
591 | 		open: 77.82514647663533,
592 | 		time: { year: 2018, month: 12, day: 8 },
593 | 	},
594 | 	{
595 | 		close: 82.67218208289492,
596 | 		high: 92.45833377442081,
597 | 		low: 76.80728739647081,
598 | 		open: 87.18916937056241,
599 | 		time: { year: 2018, month: 12, day: 9 },
600 | 	},
601 | 	{
602 | 		close: 73.86125805398967,
603 | 		high: 83.68952750914036,
604 | 		low: 73.86125805398967,
605 | 		open: 75.76119064173785,
606 | 		time: { year: 2018, month: 12, day: 10 },
607 | 	},
608 | 	{
609 | 		close: 79.00109311074502,
610 | 		high: 88.74271558831151,
611 | 		low: 69.00900811612337,
612 | 		open: 88.74271558831151,
613 | 		time: { year: 2018, month: 12, day: 11 },
614 | 	},
615 | 	{
616 | 		close: 80.98779620162513,
617 | 		high: 97.07429720104427,
618 | 		low: 73.76970378608283,
619 | 		open: 88.57288529720472,
620 | 		time: { year: 2018, month: 12, day: 12 },
621 | 	},
622 | 	{
623 | 		close: 87.83619759370346,
624 | 		high: 91.29759438607132,
625 | 		low: 74.00740214639268,
626 | 		open: 87.51853658661781,
627 | 		time: { year: 2018, month: 12, day: 13 },
628 | 	},
629 | 	{
630 | 		close: 87.50134898892377,
631 | 		high: 102.95635188637507,
632 | 		low: 81.0513723219724,
633 | 		open: 94.74009794290814,
634 | 		time: { year: 2018, month: 12, day: 14 },
635 | 	},
636 | 	{
637 | 		close: 92.40159548029843,
638 | 		high: 103.24363067710844,
639 | 		low: 75.44605394394573,
640 | 		open: 95.99903495559444,
641 | 		time: { year: 2018, month: 12, day: 15 },
642 | 	},
643 | 	{
644 | 		close: 87.43619322092951,
645 | 		high: 99.39349139000474,
646 | 		low: 80.24624983473528,
647 | 		open: 99.39349139000474,
648 | 		time: { year: 2018, month: 12, day: 16 },
649 | 	},
650 | 	{
651 | 		close: 84.42724177432086,
652 | 		high: 95.57485075893881,
653 | 		low: 84.42724177432086,
654 | 		open: 90.71070399095831,
655 | 		time: { year: 2018, month: 12, day: 17 },
656 | 	},
657 | 	{
658 | 		close: 96.04408990868804,
659 | 		high: 101.02158248010466,
660 | 		low: 94.38544669520195,
661 | 		open: 101.02158248010466,
662 | 		time: { year: 2018, month: 12, day: 18 },
663 | 	},
664 | 	{
665 | 		close: 97.2120815653703,
666 | 		high: 103.35830035963959,
667 | 		low: 78.72594316029567,
668 | 		open: 86.98009038330306,
669 | 		time: { year: 2018, month: 12, day: 19 },
670 | 	},
671 | 	{
672 | 		close: 105.23366706522204,
673 | 		high: 106.56174456393981,
674 | 		low: 94.6658899187065,
675 | 		open: 106.56174456393981,
676 | 		time: { year: 2018, month: 12, day: 20 },
677 | 	},
678 | 	{
679 | 		close: 89.53750874231946,
680 | 		high: 112.27917367188074,
681 | 		low: 87.13586952228918,
682 | 		open: 96.0857985693989,
683 | 		time: { year: 2018, month: 12, day: 21 },
684 | 	},
685 | 	{
686 | 		close: 88.55787263435407,
687 | 		high: 112.62138454627025,
688 | 		low: 80.42783344898223,
689 | 		open: 88.34340019789849,
690 | 		time: { year: 2018, month: 12, day: 22 },
691 | 	},
692 | 	{
693 | 		close: 86.00639650371167,
694 | 		high: 110.94532193307279,
695 | 		low: 74.78703575498496,
696 | 		open: 92.4275741143068,
697 | 		time: { year: 2018, month: 12, day: 23 },
698 | 	},
699 | 	{
700 | 		close: 90.45119640254379,
701 | 		high: 92.51500970997435,
702 | 		low: 82.69475430846728,
703 | 		open: 86.21662699549296,
704 | 		time: { year: 2018, month: 12, day: 24 },
705 | 	},
706 | 	{
707 | 		close: 93.38124264891343,
708 | 		high: 93.38124264891343,
709 | 		low: 84.5674956907938,
710 | 		open: 87.54923273867136,
711 | 		time: { year: 2018, month: 12, day: 25 },
712 | 	},
713 | 	{
714 | 		close: 87.88725775527871,
715 | 		high: 90.14253631595105,
716 | 		low: 77.28638555494503,
717 | 		open: 83.93199044032968,
718 | 		time: { year: 2018, month: 12, day: 26 },
719 | 	},
720 | 	{
721 | 		close: 71.77940077333062,
722 | 		high: 89.25710176370582,
723 | 		low: 67.74278646676306,
724 | 		open: 78.5346198695072,
725 | 		time: { year: 2018, month: 12, day: 27 },
726 | 	},
727 | 	{
728 | 		close: 72.08757207606054,
729 | 		high: 79.36518615067514,
730 | 		low: 69.18787486704672,
731 | 		open: 69.18787486704672,
732 | 		time: { year: 2018, month: 12, day: 28 },
733 | 	},
734 | 	{
735 | 		close: 73.87977927793119,
736 | 		high: 77.62891475860795,
737 | 		low: 70.42293039125319,
738 | 		open: 70.42293039125319,
739 | 		time: { year: 2018, month: 12, day: 29 },
740 | 	},
741 | 	{
742 | 		close: 74.86330345366132,
743 | 		high: 75.88473282167168,
744 | 		low: 62.89549355427313,
745 | 		open: 74.86554252962132,
746 | 		time: { year: 2018, month: 12, day: 30 },
747 | 	},
748 | 	{
749 | 		close: 71.00787215611817,
750 | 		high: 71.00787215611817,
751 | 		low: 57.29681995441558,
752 | 		open: 60.04464694823929,
753 | 		time: { year: 2018, month: 12, day: 31 },
754 | 	},
755 | 	// hide-end
756 | ]);
757 | 
758 | chart.timeScale().fitContent();
759 | // hide-start
760 | const styles = `
761 |     .buttons-container {
762 |         display: flex;
763 |         flex-direction: row;
764 |         gap: 8px;
765 |     }
766 |     .buttons-container button {
767 |         all: initial;
768 |         font-family: -apple-system, BlinkMacSystemFont, 'Trebuchet MS', Roboto, Ubuntu,
769 |             sans-serif;
770 |         font-size: 16px;
771 |         font-style: normal;
772 |         font-weight: 510;
773 |         line-height: 24px; /* 150% */
774 |         letter-spacing: -0.32px;
775 |         padding: 8px 24px;
776 |         color: rgba(19, 23, 34, 1);
777 |         background-color: rgba(240, 243, 250, 1);
778 |         border-radius: 8px;
779 |         cursor: pointer;
780 |     }
781 | 
782 |     .buttons-container button:hover {
783 |         background-color: rgba(224, 227, 235, 1);
784 |     }
785 | 
786 |     .buttons-container button:active {
787 |         background-color: rgba(209, 212, 220, 1);
788 |     }
789 | `;
790 | 
791 | const stylesElement = document.createElement('style');
792 | stylesElement.innerHTML = styles;
793 | container.appendChild(stylesElement);
794 | 
795 | const buttonsContainer = document.createElement('div');
796 | buttonsContainer.classList.add('buttons-container');
797 | // hide-end
798 | const fontOptions = ['Courier New', 'Arial', 'Times New Roman'];
799 | fontOptions.forEach(font => {
800 | 	const button = document.createElement('button');
801 | 	button.innerText = font;
802 | 	button.addEventListener('click', () => setFontFamily(font));
803 | 	buttonsContainer.appendChild(button);
804 | });
805 | 
806 | container.appendChild(buttonsContainer);
807 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/custom-font-family.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Custom font family
 3 | sidebar_label: Custom font
 4 | description: An example of how to configure a custom font family for the chart
 5 | pagination_prev: null
 6 | pagination_next: null
 7 | keywords:
 8 |   - font
 9 |   - typeface
10 | ---
11 | 
12 | In this example, Lightweight Charts™ showcases its high customizability,
13 | specifically with respect to adjusting font families. The primary tool for
14 | implementing this shift in font is the `chart.applyOptions()` method.
15 | 
16 | This method is called within the `setFontFamily(fontFamily)` function, accepting
17 | an object that modifies the `layout` section of the chart options. The object
18 | changes the `fontFamily` property to the passed argument, allowing quick and
19 | responsive alterations to the chart's font style.
20 | 
21 | The flexibility in adjusting text characteristics enables the fine-tuning of the
22 | chart's visual elements for better readability or to match specific styles,
23 | attesting to the adaptability of Lightweight Charts™.
24 | 
25 | A more detailed tutorial on customizing the appearance of the chart can be found
26 | [here](../customization/intro.mdx).
27 | 
28 | ### API Reference
29 | 
30 | - [LayoutOptions.fontFamily](/docs/api/interfaces/LayoutOptions#fontfamily)
31 | 
32 | import UsageGuidePartial from '../_usage-guide-partial.mdx';
33 | import CodeBlock from '@theme/CodeBlock';
34 | import code from '!!raw-loader!./custom-font-family.js';
35 | 
36 | <CodeBlock
37 | 	replaceThemeConstants
38 | 	chart
39 | 	className="language-js"
40 | 	hideableCode
41 | 	chartOnTop
42 | 	codeUsage={<UsageGuidePartial />}
43 | >
44 | 	{code}
45 | </CodeBlock>
46 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/custom-locale.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Custom locale
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/demos/custom-locale
  4 | 
  5 | // remove-end
  6 | // hide-start
  7 | const chartOptions = {
  8 | 	layout: {
  9 | 		textColor: CHART_TEXT_COLOR,
 10 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
 11 | 	},
 12 | 	height: 200,
 13 | };
 14 | // hide-end
 15 | const container = document.getElementById('container');
 16 | // remove-line
 17 | /** @type {import('lightweight-charts').IChartApi} */
 18 | const chart = createChart(container, chartOptions);
 19 | 
 20 | // remove-start
 21 | // Only needed within demo page
 22 | // eslint-disable-next-line no-undef
 23 | window.addEventListener('resize', () => {
 24 | 	chart.applyOptions({ height: 200 });
 25 | });
 26 | // remove-end
 27 | 
 28 | function setLocale(locale) {
 29 | 	// highlight-start
 30 | 	chart.applyOptions({
 31 | 		localization: {
 32 | 			locale: locale,
 33 | 			dateFormat: 'ja-JP' === locale ? 'yyyy-MM-dd' : "dd MMM 'yy",
 34 | 		},
 35 | 	});
 36 | 	// highlight-end
 37 | }
 38 | 
 39 | const candlestickSeries = chart.addSeries(CandlestickSeries, {
 40 | 	upColor: BAR_UP_COLOR,
 41 | 	downColor: BAR_DOWN_COLOR,
 42 | 	borderVisible: false,
 43 | 	wickUpColor: BAR_UP_COLOR,
 44 | 	wickDownColor: BAR_DOWN_COLOR,
 45 | });
 46 | 
 47 | candlestickSeries.setData([
 48 | 	{
 49 | 		close: 108.9974612905403,
 50 | 		high: 121.20998259466148,
 51 | 		low: 96.65376292551082,
 52 | 		open: 104.5614412226746,
 53 | 		time: { year: 2018, month: 9, day: 22 },
 54 | 	},
 55 | 	// hide-start
 56 | 	{
 57 | 		close: 110.46815600023501,
 58 | 		high: 111.3650273696516,
 59 | 		low: 82.65543461471314,
 60 | 		open: 110.16538466099634,
 61 | 		time: { year: 2018, month: 9, day: 23 },
 62 | 	},
 63 | 	{
 64 | 		close: 90.62131977740425,
 65 | 		high: 109.19838270252615,
 66 | 		low: 82.30106956144076,
 67 | 		open: 105.03104735287424,
 68 | 		time: { year: 2018, month: 9, day: 24 },
 69 | 	},
 70 | 	{
 71 | 		close: 96.80120024431532,
 72 | 		high: 101.92074283374939,
 73 | 		low: 89.25819769856513,
 74 | 		open: 89.25819769856513,
 75 | 		time: { year: 2018, month: 9, day: 25 },
 76 | 	},
 77 | 	{
 78 | 		close: 94.87113928076117,
 79 | 		high: 104.12503365679314,
 80 | 		low: 85.42405005240111,
 81 | 		open: 104.12503365679314,
 82 | 		time: { year: 2018, month: 9, day: 26 },
 83 | 	},
 84 | 	{
 85 | 		close: 100.76494087674855,
 86 | 		high: 102.60508417239113,
 87 | 		low: 80.76268547064865,
 88 | 		open: 92.93299948659636,
 89 | 		time: { year: 2018, month: 9, day: 27 },
 90 | 	},
 91 | 	{
 92 | 		close: 101.45855928883597,
 93 | 		high: 110.26727325817173,
 94 | 		low: 91.10348900896837,
 95 | 		open: 93.4362185148034,
 96 | 		time: { year: 2018, month: 9, day: 28 },
 97 | 	},
 98 | 	{
 99 | 		close: 91.68871815146144,
100 | 		high: 103.73263644407702,
101 | 		low: 73.5329263610334,
102 | 		open: 92.96467883926464,
103 | 		time: { year: 2018, month: 9, day: 29 },
104 | 	},
105 | 	{
106 | 		close: 89.39633140354033,
107 | 		high: 101.06569518834237,
108 | 		low: 81.71149885084162,
109 | 		open: 83.08248758612376,
110 | 		time: { year: 2018, month: 9, day: 30 },
111 | 	},
112 | 	{
113 | 		close: 93.09498513675378,
114 | 		high: 93.09498513675378,
115 | 		low: 76.81138276012628,
116 | 		open: 91.97280452613565,
117 | 		time: { year: 2018, month: 10, day: 1 },
118 | 	},
119 | 	{
120 | 		close: 89.26733004009083,
121 | 		high: 89.26733004009083,
122 | 		low: 76.27851645958225,
123 | 		open: 85.83860311023625,
124 | 		time: { year: 2018, month: 10, day: 2 },
125 | 	},
126 | 	{
127 | 		close: 89.66035763006947,
128 | 		high: 89.66035763006947,
129 | 		low: 67.63677527399729,
130 | 		open: 77.79584976144585,
131 | 		time: { year: 2018, month: 10, day: 3 },
132 | 	},
133 | 	{
134 | 		close: 89.59687813884807,
135 | 		high: 97.05916949817754,
136 | 		low: 72.9823390058379,
137 | 		open: 77.37388423995716,
138 | 		time: { year: 2018, month: 10, day: 4 },
139 | 	},
140 | 	{
141 | 		close: 83.6425403120788,
142 | 		high: 91.72593377862522,
143 | 		low: 65.27208271740422,
144 | 		open: 85.92711686401718,
145 | 		time: { year: 2018, month: 10, day: 5 },
146 | 	},
147 | 	{
148 | 		close: 82.99053929200655,
149 | 		high: 93.4482645370556,
150 | 		low: 65.98920655616067,
151 | 		open: 71.8940788814462,
152 | 		time: { year: 2018, month: 10, day: 6 },
153 | 	},
154 | 	{
155 | 		close: 73.09595957510754,
156 | 		high: 86.65935598412881,
157 | 		low: 62.710852488609326,
158 | 		open: 80.78945254092527,
159 | 		time: { year: 2018, month: 10, day: 7 },
160 | 	},
161 | 	{
162 | 		close: 80.12127692112905,
163 | 		high: 87.49034842093855,
164 | 		low: 60.09987438133361,
165 | 		open: 70.2408873110499,
166 | 		time: { year: 2018, month: 10, day: 8 },
167 | 	},
168 | 	{
169 | 		close: 77.60439116240829,
170 | 		high: 83.20908153481327,
171 | 		low: 68.56836128158209,
172 | 		open: 75.83440719565763,
173 | 		time: { year: 2018, month: 10, day: 9 },
174 | 	},
175 | 	{
176 | 		close: 73.8952889203428,
177 | 		high: 81.89987377779327,
178 | 		low: 57.8891283348631,
179 | 		open: 66.51904017615065,
180 | 		time: { year: 2018, month: 10, day: 10 },
181 | 	},
182 | 	{
183 | 		close: 75.08452506029613,
184 | 		high: 75.08452506029613,
185 | 		low: 59.208194031968155,
186 | 		open: 72.14475369395771,
187 | 		time: { year: 2018, month: 10, day: 11 },
188 | 	},
189 | 	{
190 | 		close: 73.08898607472305,
191 | 		high: 73.08898607472305,
192 | 		low: 63.05632280826725,
193 | 		open: 66.93050765469924,
194 | 		time: { year: 2018, month: 10, day: 12 },
195 | 	},
196 | 	{
197 | 		close: 58.993371469509704,
198 | 		high: 73.08872095153116,
199 | 		low: 53.52204433018574,
200 | 		open: 66.12840939191403,
201 | 		time: { year: 2018, month: 10, day: 13 },
202 | 	},
203 | 	{
204 | 		close: 57.150755012485,
205 | 		high: 74.57414896810235,
206 | 		low: 52.6552427480398,
207 | 		open: 68.50876667562338,
208 | 		time: { year: 2018, month: 10, day: 14 },
209 | 	},
210 | 	{
211 | 		close: 58.03147289822832,
212 | 		high: 69.62445357159157,
213 | 		low: 53.8260018823565,
214 | 		open: 61.62298899368165,
215 | 		time: { year: 2018, month: 10, day: 15 },
216 | 	},
217 | 	{
218 | 		close: 60.6852855399041,
219 | 		high: 69.02095441024431,
220 | 		low: 54.00939224622043,
221 | 		open: 64.81901552322648,
222 | 		time: { year: 2018, month: 10, day: 16 },
223 | 	},
224 | 	{
225 | 		close: 57.508820449565285,
226 | 		high: 63.82926565242872,
227 | 		low: 54.07370975509682,
228 | 		open: 54.07370975509682,
229 | 		time: { year: 2018, month: 10, day: 17 },
230 | 	},
231 | 	{
232 | 		close: 51.60796818909221,
233 | 		high: 64.88712939579875,
234 | 		low: 51.60796818909221,
235 | 		open: 53.489226476218434,
236 | 		time: { year: 2018, month: 10, day: 18 },
237 | 	},
238 | 	{
239 | 		close: 55.139520748382864,
240 | 		high: 59.161320710177925,
241 | 		low: 52.228139922762765,
242 | 		open: 52.228139922762765,
243 | 		time: { year: 2018, month: 10, day: 19 },
244 | 	},
245 | 	{
246 | 		close: 47.47868992247237,
247 | 		high: 58.0836625917653,
248 | 		low: 46.43213518526832,
249 | 		open: 47.59258635788406,
250 | 		time: { year: 2018, month: 10, day: 20 },
251 | 	},
252 | 	{
253 | 		close: 47.22596723150508,
254 | 		high: 51.55468175560989,
255 | 		low: 45.22654435521185,
256 | 		open: 47.452459556200054,
257 | 		time: { year: 2018, month: 10, day: 21 },
258 | 	},
259 | 	{
260 | 		close: 53.39724151191295,
261 | 		high: 58.256006746786035,
262 | 		low: 46.40105667413804,
263 | 		open: 53.41548527476272,
264 | 		time: { year: 2018, month: 10, day: 22 },
265 | 	},
266 | 	{
267 | 		close: 45.015877277800854,
268 | 		high: 51.2955426978105,
269 | 		low: 40.26534748806228,
270 | 		open: 43.90158660063875,
271 | 		time: { year: 2018, month: 10, day: 23 },
272 | 	},
273 | 	{
274 | 		close: 49.307312373439665,
275 | 		high: 49.93643636637581,
276 | 		low: 43.20705757075934,
277 | 		open: 45.672934511555795,
278 | 		time: { year: 2018, month: 10, day: 24 },
279 | 	},
280 | 	{
281 | 		close: 45.15418019295631,
282 | 		high: 48.59676744409583,
283 | 		low: 37.628047445918504,
284 | 		open: 40.33862825788268,
285 | 		time: { year: 2018, month: 10, day: 25 },
286 | 	},
287 | 	{
288 | 		close: 43.2972018283068,
289 | 		high: 43.2972018283068,
290 | 		low: 36.335943004352245,
291 | 		open: 42.605991542720965,
292 | 		time: { year: 2018, month: 10, day: 26 },
293 | 	},
294 | 	{
295 | 		close: 39.1153643552137,
296 | 		high: 44.311406627923844,
297 | 		low: 35.31457011784855,
298 | 		open: 42.00000202357808,
299 | 		time: { year: 2018, month: 10, day: 27 },
300 | 	},
301 | 	{
302 | 		close: 36.06960076896885,
303 | 		high: 42.89041111567749,
304 | 		low: 33.58326637182405,
305 | 		open: 37.40942817102858,
306 | 		time: { year: 2018, month: 10, day: 28 },
307 | 	},
308 | 	{
309 | 		close: 35.8981036950969,
310 | 		high: 42.19793419602979,
311 | 		low: 33.62190962880232,
312 | 		open: 36.87246325249825,
313 | 		time: { year: 2018, month: 10, day: 29 },
314 | 	},
315 | 	{
316 | 		close: 31.378205119641457,
317 | 		high: 37.33501102832602,
318 | 		low: 31.30137162225214,
319 | 		open: 35.651275660713694,
320 | 		time: { year: 2018, month: 10, day: 30 },
321 | 	},
322 | 	{
323 | 		close: 33.574536057730576,
324 | 		high: 37.30152570719593,
325 | 		low: 27.369689193426243,
326 | 		open: 34.330180925654936,
327 | 		time: { year: 2018, month: 10, day: 31 },
328 | 	},
329 | 	{
330 | 		close: 28.91735096504839,
331 | 		high: 32.62196350117741,
332 | 		low: 27.072564759401843,
333 | 		open: 29.398552328599372,
334 | 		time: { year: 2018, month: 11, day: 1 },
335 | 	},
336 | 	{
337 | 		close: 28.44143154172122,
338 | 		high: 31.042019861166594,
339 | 		low: 23.383320830495375,
340 | 		open: 27.275885037308072,
341 | 		time: { year: 2018, month: 11, day: 2 },
342 | 	},
343 | 	{
344 | 		close: 25.92162714418916,
345 | 		high: 30.57604443170622,
346 | 		low: 25.418671641150752,
347 | 		open: 26.775196275924657,
348 | 		time: { year: 2018, month: 11, day: 3 },
349 | 	},
350 | 	{
351 | 		close: 26.376994016637433,
352 | 		high: 28.198647836523744,
353 | 		low: 21.492969733673334,
354 | 		open: 26.27980943059139,
355 | 		time: { year: 2018, month: 11, day: 4 },
356 | 	},
357 | 	{
358 | 		close: 28.60834088674494,
359 | 		high: 28.60834088674494,
360 | 		low: 21.89002840571941,
361 | 		open: 25.376464895884993,
362 | 		time: { year: 2018, month: 11, day: 5 },
363 | 	},
364 | 	{
365 | 		close: 31.103861067101136,
366 | 		high: 31.103861067101136,
367 | 		low: 24.39227668420513,
368 | 		open: 28.994785427089838,
369 | 		time: { year: 2018, month: 11, day: 6 },
370 | 	},
371 | 	{
372 | 		close: 28.6308138310307,
373 | 		high: 35.430817482769164,
374 | 		low: 24.069515410358232,
375 | 		open: 27.109407394069084,
376 | 		time: { year: 2018, month: 11, day: 7 },
377 | 	},
378 | 	{
379 | 		close: 29.468889521733466,
380 | 		high: 37.54082586961352,
381 | 		low: 27.90833873315644,
382 | 		open: 33.16901271715577,
383 | 		time: { year: 2018, month: 11, day: 8 },
384 | 	},
385 | 	{
386 | 		close: 35.887823124204296,
387 | 		high: 39.21804237580939,
388 | 		low: 30.951078044055627,
389 | 		open: 30.951078044055627,
390 | 		time: { year: 2018, month: 11, day: 9 },
391 | 	},
392 | 	{
393 | 		close: 34.361137347097575,
394 | 		high: 35.27083445807796,
395 | 		low: 27.825889562160082,
396 | 		open: 34.86040182980157,
397 | 		time: { year: 2018, month: 11, day: 10 },
398 | 	},
399 | 	{
400 | 		close: 36.61336645243868,
401 | 		high: 40.31460537175622,
402 | 		low: 33.96383400053921,
403 | 		open: 39.70037560142739,
404 | 		time: { year: 2018, month: 11, day: 11 },
405 | 	},
406 | 	{
407 | 		close: 41.321693986803055,
408 | 		high: 44.45481986667003,
409 | 		low: 35.67563772228475,
410 | 		open: 38.67059795413642,
411 | 		time: { year: 2018, month: 11, day: 12 },
412 | 	},
413 | 	{
414 | 		close: 40.15038854039306,
415 | 		high: 41.50912000191902,
416 | 		low: 32.610637769394444,
417 | 		open: 41.50912000191902,
418 | 		time: { year: 2018, month: 11, day: 13 },
419 | 	},
420 | 	{
421 | 		close: 44.092601065208015,
422 | 		high: 44.092601065208015,
423 | 		low: 37.778306506100726,
424 | 		open: 38.99045898154136,
425 | 		time: { year: 2018, month: 11, day: 14 },
426 | 	},
427 | 	{
428 | 		close: 41.42426637839382,
429 | 		high: 44.72189614841937,
430 | 		low: 41.42426637839382,
431 | 		open: 44.72189614841937,
432 | 		time: { year: 2018, month: 11, day: 15 },
433 | 	},
434 | 	{
435 | 		close: 41.19513795258408,
436 | 		high: 49.08084695291049,
437 | 		low: 36.24282165100056,
438 | 		open: 44.909248500660254,
439 | 		time: { year: 2018, month: 11, day: 16 },
440 | 	},
441 | 	{
442 | 		close: 44.24935708161703,
443 | 		high: 53.028535501565486,
444 | 		low: 40.32056743060158,
445 | 		open: 46.198546801109984,
446 | 		time: { year: 2018, month: 11, day: 17 },
447 | 	},
448 | 	{
449 | 		close: 43.18555863372182,
450 | 		high: 52.34250206788521,
451 | 		low: 43.18555863372182,
452 | 		open: 49.58135271619679,
453 | 		time: { year: 2018, month: 11, day: 18 },
454 | 	},
455 | 	{
456 | 		close: 50.8568887039091,
457 | 		high: 52.60441957102357,
458 | 		low: 39.917719271944364,
459 | 		open: 48.197532365645806,
460 | 		time: { year: 2018, month: 11, day: 19 },
461 | 	},
462 | 	{
463 | 		close: 48.79128595974164,
464 | 		high: 52.45087789296739,
465 | 		low: 46.80633073487828,
466 | 		open: 52.45087789296739,
467 | 		time: { year: 2018, month: 11, day: 20 },
468 | 	},
469 | 	{
470 | 		close: 46.97300046781947,
471 | 		high: 55.80689868049132,
472 | 		low: 46.97300046781947,
473 | 		open: 55.80689868049132,
474 | 		time: { year: 2018, month: 11, day: 21 },
475 | 	},
476 | 	{
477 | 		close: 55.58129861112469,
478 | 		high: 55.58129861112469,
479 | 		low: 49.087279242343996,
480 | 		open: 53.16719476594961,
481 | 		time: { year: 2018, month: 11, day: 22 },
482 | 	},
483 | 	{
484 | 		close: 50.058979311730226,
485 | 		high: 62.55333249171461,
486 | 		low: 50.058979311730226,
487 | 		open: 52.628489607588826,
488 | 		time: { year: 2018, month: 11, day: 23 },
489 | 	},
490 | 	{
491 | 		close: 51.193155229085995,
492 | 		high: 59.08949991997865,
493 | 		low: 51.193155229085995,
494 | 		open: 55.352594157474755,
495 | 		time: { year: 2018, month: 11, day: 24 },
496 | 	},
497 | 	{
498 | 		close: 60.099338327208436,
499 | 		high: 66.93510126958154,
500 | 		low: 55.27299867222781,
501 | 		open: 61.05897620044226,
502 | 		time: { year: 2018, month: 11, day: 25 },
503 | 	},
504 | 	{
505 | 		close: 58.3802630890727,
506 | 		high: 71.50922937699602,
507 | 		low: 50.95210438359451,
508 | 		open: 62.4679688326532,
509 | 		time: { year: 2018, month: 11, day: 26 },
510 | 	},
511 | 	{
512 | 		close: 57.875350873413225,
513 | 		high: 65.59903214448208,
514 | 		low: 57.875350873413225,
515 | 		open: 62.747405667247016,
516 | 		time: { year: 2018, month: 11, day: 27 },
517 | 	},
518 | 	{
519 | 		close: 61.231150731698605,
520 | 		high: 66.3829902228434,
521 | 		low: 61.231150731698605,
522 | 		open: 65.01028486919516,
523 | 		time: { year: 2018, month: 11, day: 28 },
524 | 	},
525 | 	{
526 | 		close: 64.9698540874806,
527 | 		high: 77.09783903299783,
528 | 		low: 58.455031795628194,
529 | 		open: 58.455031795628194,
530 | 		time: { year: 2018, month: 11, day: 29 },
531 | 	},
532 | 	{
533 | 		close: 72.40978471883417,
534 | 		high: 72.40978471883417,
535 | 		low: 53.05804901549206,
536 | 		open: 65.907298021202,
537 | 		time: { year: 2018, month: 11, day: 30 },
538 | 	},
539 | 	{
540 | 		close: 74.60745731538934,
541 | 		high: 78.33742117000789,
542 | 		low: 54.42067144918077,
543 | 		open: 73.20930147914103,
544 | 		time: { year: 2018, month: 12, day: 1 },
545 | 	},
546 | 	{
547 | 		close: 64.10866184869924,
548 | 		high: 76.14506447001202,
549 | 		low: 61.5224432669736,
550 | 		open: 69.33984127682314,
551 | 		time: { year: 2018, month: 12, day: 2 },
552 | 	},
553 | 	{
554 | 		close: 65.92038759928786,
555 | 		high: 76.98479070362022,
556 | 		low: 65.92038759928786,
557 | 		open: 69.32298264631615,
558 | 		time: { year: 2018, month: 12, day: 3 },
559 | 	},
560 | 	{
561 | 		close: 68.23682161095334,
562 | 		high: 77.6723729460968,
563 | 		low: 68.23682161095334,
564 | 		open: 74.39471534484744,
565 | 		time: { year: 2018, month: 12, day: 4 },
566 | 	},
567 | 	{
568 | 		close: 67.45035792565862,
569 | 		high: 83.53728553118547,
570 | 		low: 67.45035792565862,
571 | 		open: 74.79418570077237,
572 | 		time: { year: 2018, month: 12, day: 5 },
573 | 	},
574 | 	{
575 | 		close: 79.26722967320323,
576 | 		high: 79.26722967320323,
577 | 		low: 68.40654829383521,
578 | 		open: 68.40654829383521,
579 | 		time: { year: 2018, month: 12, day: 6 },
580 | 	},
581 | 	{
582 | 		close: 74.95305464030587,
583 | 		high: 81.65884414224071,
584 | 		low: 64.08761481290135,
585 | 		open: 81.65884414224071,
586 | 		time: { year: 2018, month: 12, day: 7 },
587 | 	},
588 | 	{
589 | 		close: 86.30802154315482,
590 | 		high: 91.21953112925642,
591 | 		low: 65.46112304993535,
592 | 		open: 77.82514647663533,
593 | 		time: { year: 2018, month: 12, day: 8 },
594 | 	},
595 | 	{
596 | 		close: 82.67218208289492,
597 | 		high: 92.45833377442081,
598 | 		low: 76.80728739647081,
599 | 		open: 87.18916937056241,
600 | 		time: { year: 2018, month: 12, day: 9 },
601 | 	},
602 | 	{
603 | 		close: 73.86125805398967,
604 | 		high: 83.68952750914036,
605 | 		low: 73.86125805398967,
606 | 		open: 75.76119064173785,
607 | 		time: { year: 2018, month: 12, day: 10 },
608 | 	},
609 | 	{
610 | 		close: 79.00109311074502,
611 | 		high: 88.74271558831151,
612 | 		low: 69.00900811612337,
613 | 		open: 88.74271558831151,
614 | 		time: { year: 2018, month: 12, day: 11 },
615 | 	},
616 | 	{
617 | 		close: 80.98779620162513,
618 | 		high: 97.07429720104427,
619 | 		low: 73.76970378608283,
620 | 		open: 88.57288529720472,
621 | 		time: { year: 2018, month: 12, day: 12 },
622 | 	},
623 | 	{
624 | 		close: 87.83619759370346,
625 | 		high: 91.29759438607132,
626 | 		low: 74.00740214639268,
627 | 		open: 87.51853658661781,
628 | 		time: { year: 2018, month: 12, day: 13 },
629 | 	},
630 | 	{
631 | 		close: 87.50134898892377,
632 | 		high: 102.95635188637507,
633 | 		low: 81.0513723219724,
634 | 		open: 94.74009794290814,
635 | 		time: { year: 2018, month: 12, day: 14 },
636 | 	},
637 | 	{
638 | 		close: 92.40159548029843,
639 | 		high: 103.24363067710844,
640 | 		low: 75.44605394394573,
641 | 		open: 95.99903495559444,
642 | 		time: { year: 2018, month: 12, day: 15 },
643 | 	},
644 | 	{
645 | 		close: 87.43619322092951,
646 | 		high: 99.39349139000474,
647 | 		low: 80.24624983473528,
648 | 		open: 99.39349139000474,
649 | 		time: { year: 2018, month: 12, day: 16 },
650 | 	},
651 | 	{
652 | 		close: 84.42724177432086,
653 | 		high: 95.57485075893881,
654 | 		low: 84.42724177432086,
655 | 		open: 90.71070399095831,
656 | 		time: { year: 2018, month: 12, day: 17 },
657 | 	},
658 | 	{
659 | 		close: 96.04408990868804,
660 | 		high: 101.02158248010466,
661 | 		low: 94.38544669520195,
662 | 		open: 101.02158248010466,
663 | 		time: { year: 2018, month: 12, day: 18 },
664 | 	},
665 | 	{
666 | 		close: 97.2120815653703,
667 | 		high: 103.35830035963959,
668 | 		low: 78.72594316029567,
669 | 		open: 86.98009038330306,
670 | 		time: { year: 2018, month: 12, day: 19 },
671 | 	},
672 | 	{
673 | 		close: 105.23366706522204,
674 | 		high: 106.56174456393981,
675 | 		low: 94.6658899187065,
676 | 		open: 106.56174456393981,
677 | 		time: { year: 2018, month: 12, day: 20 },
678 | 	},
679 | 	{
680 | 		close: 89.53750874231946,
681 | 		high: 112.27917367188074,
682 | 		low: 87.13586952228918,
683 | 		open: 96.0857985693989,
684 | 		time: { year: 2018, month: 12, day: 21 },
685 | 	},
686 | 	{
687 | 		close: 88.55787263435407,
688 | 		high: 112.62138454627025,
689 | 		low: 80.42783344898223,
690 | 		open: 88.34340019789849,
691 | 		time: { year: 2018, month: 12, day: 22 },
692 | 	},
693 | 	{
694 | 		close: 86.00639650371167,
695 | 		high: 110.94532193307279,
696 | 		low: 74.78703575498496,
697 | 		open: 92.4275741143068,
698 | 		time: { year: 2018, month: 12, day: 23 },
699 | 	},
700 | 	{
701 | 		close: 90.45119640254379,
702 | 		high: 92.51500970997435,
703 | 		low: 82.69475430846728,
704 | 		open: 86.21662699549296,
705 | 		time: { year: 2018, month: 12, day: 24 },
706 | 	},
707 | 	{
708 | 		close: 93.38124264891343,
709 | 		high: 93.38124264891343,
710 | 		low: 84.5674956907938,
711 | 		open: 87.54923273867136,
712 | 		time: { year: 2018, month: 12, day: 25 },
713 | 	},
714 | 	{
715 | 		close: 87.88725775527871,
716 | 		high: 90.14253631595105,
717 | 		low: 77.28638555494503,
718 | 		open: 83.93199044032968,
719 | 		time: { year: 2018, month: 12, day: 26 },
720 | 	},
721 | 	{
722 | 		close: 71.77940077333062,
723 | 		high: 89.25710176370582,
724 | 		low: 67.74278646676306,
725 | 		open: 78.5346198695072,
726 | 		time: { year: 2018, month: 12, day: 27 },
727 | 	},
728 | 	{
729 | 		close: 72.08757207606054,
730 | 		high: 79.36518615067514,
731 | 		low: 69.18787486704672,
732 | 		open: 69.18787486704672,
733 | 		time: { year: 2018, month: 12, day: 28 },
734 | 	},
735 | 	{
736 | 		close: 73.87977927793119,
737 | 		high: 77.62891475860795,
738 | 		low: 70.42293039125319,
739 | 		open: 70.42293039125319,
740 | 		time: { year: 2018, month: 12, day: 29 },
741 | 	},
742 | 	{
743 | 		close: 74.86330345366132,
744 | 		high: 75.88473282167168,
745 | 		low: 62.89549355427313,
746 | 		open: 74.86554252962132,
747 | 		time: { year: 2018, month: 12, day: 30 },
748 | 	},
749 | 	{
750 | 		close: 71.00787215611817,
751 | 		high: 71.00787215611817,
752 | 		low: 57.29681995441558,
753 | 		open: 60.04464694823929,
754 | 		time: { year: 2018, month: 12, day: 31 },
755 | 	},
756 | 	// hide-end
757 | ]);
758 | 
759 | chart.timeScale().fitContent();
760 | // hide-start
761 | const styles = `
762 |     .buttons-container {
763 |         display: flex;
764 |         flex-direction: row;
765 |         gap: 8px;
766 |     }
767 |     .buttons-container button {
768 |         all: initial;
769 |         font-family: -apple-system, BlinkMacSystemFont, 'Trebuchet MS', Roboto, Ubuntu,
770 |             sans-serif;
771 |         font-size: 16px;
772 |         font-style: normal;
773 |         font-weight: 510;
774 |         line-height: 24px; /* 150% */
775 |         letter-spacing: -0.32px;
776 |         padding: 8px 24px;
777 |         color: rgba(19, 23, 34, 1);
778 |         background-color: rgba(240, 243, 250, 1);
779 |         border-radius: 8px;
780 |         cursor: pointer;
781 |     }
782 | 
783 |     .buttons-container button:hover {
784 |         background-color: rgba(224, 227, 235, 1);
785 |     }
786 | 
787 |     .buttons-container button:active {
788 |         background-color: rgba(209, 212, 220, 1);
789 |     }
790 | `;
791 | 
792 | const stylesElement = document.createElement('style');
793 | stylesElement.innerHTML = styles;
794 | container.appendChild(stylesElement);
795 | 
796 | const buttonsContainer = document.createElement('div');
797 | buttonsContainer.classList.add('buttons-container');
798 | // hide-end
799 | const localeOptions = ['es-ES', 'en-US', 'ja-JP'];
800 | localeOptions.forEach(locale => {
801 | 	const button = document.createElement('button');
802 | 	button.innerText = locale;
803 | 	button.addEventListener('click', () => setLocale(locale));
804 | 	buttonsContainer.appendChild(button);
805 | });
806 | 
807 | container.appendChild(buttonsContainer);
808 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/custom-locale.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Custom locale
 3 | sidebar_label: Custom locale
 4 | description: An example of how to set a custom locale for the chart
 5 | pagination_prev: null
 6 | pagination_next: null
 7 | keywords:
 8 |   - locale
 9 |   - language
10 |   - international
11 |   - internationalization
12 |   - i18n
13 | ---
14 | 
15 | In this example, the Lightweight Charts™ library allows for a change in the
16 | locale of the chart rendering, enabling customization to best suit the end-user.
17 | An initial chart is displayed in the default locale.
18 | 
19 | The function `setLocale(locale)` is defined to change the locale of the chart
20 | using `chart.applyOptions` method. It adjusts the `localization` property of the
21 | chart options, specifically the `locale` and `dateFormat` options. The
22 | `dateFormat` varies depending on the set locale to mirror customary date formats
23 | in respective regions.
24 | 
25 | A selection of buttons are created, each representing a distinct locale (like
26 | 'es-ES', 'en-US', 'ja-JP'). On clicking any of these buttons, its respective
27 | locale is applied to the chart by invoking `setLocale(locale)`. This dynamically
28 | adjusts the date formatting for the chart data, demonstrating the flexibility of
29 | the Lightweight Charts™ in catering to an international audience.
30 | 
31 | ### API Reference
32 | 
33 | - [ChartOptions.localization](/docs/api/interfaces/ChartOptionsBase#localization)
34 | 
35 | import UsageGuidePartial from '../_usage-guide-partial.mdx';
36 | import CodeBlock from '@theme/CodeBlock';
37 | import code from '!!raw-loader!./custom-locale.js';
38 | 
39 | <CodeBlock
40 | 	replaceThemeConstants
41 | 	chart
42 | 	className="language-js"
43 | 	hideableCode
44 | 	chartOnTop
45 | 	codeUsage={<UsageGuidePartial />}
46 | >
47 | 	{code}
48 | </CodeBlock>
49 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/infinite-history.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Infinite history
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/demos/infinite-history
  4 | 
  5 | // remove-end
  6 | 
  7 | // hide-start
  8 | let randomFactor = 25 + Math.random() * 25;
  9 | const samplePoint = i =>
 10 | 	i *
 11 | 		(0.5 +
 12 | 			Math.sin(i / 10) * 0.2 +
 13 | 			Math.sin(i / 20) * 0.4 +
 14 | 			Math.sin(i / randomFactor) * 0.8 +
 15 | 			Math.sin(i / 500) * 0.5) +
 16 | 	200;
 17 | 
 18 | function generateLineData(numberOfPoints = 500, endDate) {
 19 | 	randomFactor = 25 + Math.random() * 25;
 20 | 	const res = [];
 21 | 	const date = endDate || new Date(Date.UTC(2018, 0, 1, 12, 0, 0, 0));
 22 | 	date.setUTCDate(date.getUTCDate() - numberOfPoints - 1);
 23 | 	for (let i = 0; i < numberOfPoints; ++i) {
 24 | 		const time = date.getTime() / 1000;
 25 | 		const value = samplePoint(i);
 26 | 		res.push({
 27 | 			time,
 28 | 			value,
 29 | 		});
 30 | 
 31 | 		date.setUTCDate(date.getUTCDate() + 1);
 32 | 	}
 33 | 
 34 | 	return res;
 35 | }
 36 | 
 37 | function randomNumber(min, max) {
 38 | 	return Math.random() * (max - min) + min;
 39 | }
 40 | 
 41 | function randomBar(lastClose) {
 42 | 	const open = +randomNumber(lastClose * 0.95, lastClose * 1.05).toFixed(2);
 43 | 	const close = +randomNumber(open * 0.95, open * 1.05).toFixed(2);
 44 | 	const high = +randomNumber(
 45 | 		Math.max(open, close),
 46 | 		Math.max(open, close) * 1.1
 47 | 	).toFixed(2);
 48 | 	const low = +randomNumber(
 49 | 		Math.min(open, close) * 0.9,
 50 | 		Math.min(open, close)
 51 | 	).toFixed(2);
 52 | 	return {
 53 | 		open,
 54 | 		high,
 55 | 		low,
 56 | 		close,
 57 | 	};
 58 | }
 59 | 
 60 | function generateCandleData(numberOfPoints = 250, endDate) {
 61 | 	const lineData = generateLineData(numberOfPoints, endDate);
 62 | 	let lastClose = lineData[0].value;
 63 | 	return lineData.map(d => {
 64 | 		const candle = randomBar(lastClose);
 65 | 		lastClose = candle.close;
 66 | 		return {
 67 | 			time: d.time,
 68 | 			low: candle.low,
 69 | 			high: candle.high,
 70 | 			open: candle.open,
 71 | 			close: candle.close,
 72 | 		};
 73 | 	});
 74 | }
 75 | 
 76 | class Datafeed {
 77 | 	constructor() {
 78 | 		this._earliestDate = new Date(Date.UTC(2018, 0, 1, 12, 0, 0, 0));
 79 | 		this._data = [];
 80 | 	}
 81 | 
 82 | 	getBars(numberOfExtraBars) {
 83 | 		const historicalData = generateCandleData(
 84 | 			numberOfExtraBars,
 85 | 			this._earliestDate
 86 | 		);
 87 | 		this._data = [...historicalData, ...this._data];
 88 | 		this._earliestDate = new Date(historicalData[0].time * 1000);
 89 | 		return this._data;
 90 | 	}
 91 | }
 92 | 
 93 | const chartOptions = {
 94 | 	layout: {
 95 | 		textColor: CHART_TEXT_COLOR,
 96 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
 97 | 	},
 98 | };
 99 | // hide-end
100 | const container = document.getElementById('container');
101 | // remove-line
102 | /** @type {import('lightweight-charts').IChartApi} */
103 | const chart = createChart(container, chartOptions);
104 | 
105 | const series = chart.addSeries(CandlestickSeries, {
106 | 	upColor: BAR_UP_COLOR,
107 | 	downColor: BAR_DOWN_COLOR,
108 | 	borderVisible: false,
109 | 	wickUpColor: BAR_UP_COLOR,
110 | 	wickDownColor: BAR_DOWN_COLOR,
111 | });
112 | 
113 | const datafeed = new Datafeed();
114 | 
115 | series.setData(datafeed.getBars(200));
116 | 
117 | chart.timeScale().subscribeVisibleLogicalRangeChange(logicalRange => {
118 | 	if (logicalRange.from < 10) {
119 | 		// load more data
120 | 		const numberBarsToLoad = 50 - logicalRange.from;
121 | 		const data = datafeed.getBars(numberBarsToLoad);
122 | 		setTimeout(() => {
123 | 			series.setData(data);
124 | 		}, 250); // add a loading delay
125 | 	}
126 | });
127 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/infinite-history.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Infinite history
 3 | sidebar_label: Infinite history
 4 | description: An example of how to load historical data on demand
 5 | pagination_prev: null
 6 | pagination_next: null
 7 | keywords:
 8 |   - history
 9 | ---
10 | 
11 | This sample showcases the capability of Lightweight Charts™ to manage and display
12 | an ever-expanding dataset, resembling a live feed that loads older data when the
13 | user scrolls back in time. The example depicts a chart that initially loads a
14 | limited amount of data, but later fetches additional data as required.
15 | 
16 | Key to this functionality is the
17 | [`subscribeVisibleLogicalRangeChange`](/docs/api/interfaces/ITimeScaleApi#subscribevisiblelogicalrangechange)
18 | method. This function is triggered when the visible data range changes, in this
19 | case, when the user scrolls beyond the initially loaded data.
20 | 
21 | By checking if the amount of unseen data on the left of the screen falls below a
22 | certain threshold (in this example, 10 units), it's determined whether
23 | additional data needs to be loaded. New data is appended through a simulated
24 | delay using `setTimeout`.
25 | 
26 | This kind of infinite history functionality is typical of financial charts which
27 | frequently handle large and continuously expanding datasets.
28 | 
29 | import UsageGuidePartial from '../_usage-guide-partial.mdx';
30 | import CodeBlock from '@theme/CodeBlock';
31 | import code from '!!raw-loader!./infinite-history.js';
32 | 
33 | <CodeBlock
34 | 	replaceThemeConstants
35 | 	chart
36 | 	className="language-js"
37 | 	hideableCode
38 | 	chartOnTop
39 | 	codeUsage={<UsageGuidePartial />}
40 | >
41 | 	{code}
42 | </CodeBlock>
43 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/moving-average.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Moving average indicator
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/demos/moving-average
  4 | 
  5 | // remove-end
  6 | 
  7 | // hide-start
  8 | let randomFactor = 25 + Math.random() * 25;
  9 | const samplePoint = i =>
 10 | 	i *
 11 | 		(0.5 +
 12 | 			Math.sin(i / 10) * 0.2 +
 13 | 			Math.sin(i / 20) * 0.4 +
 14 | 			Math.sin(i / randomFactor) * 0.8 +
 15 | 			Math.sin(i / 500) * 0.5) +
 16 | 	200;
 17 | 
 18 | function generateLineData(numberOfPoints = 500, endDate) {
 19 | 	randomFactor = 25 + Math.random() * 25;
 20 | 	const res = [];
 21 | 	const date = endDate || new Date(Date.UTC(2018, 0, 1, 12, 0, 0, 0));
 22 | 	date.setUTCDate(date.getUTCDate() - numberOfPoints - 1);
 23 | 	for (let i = 0; i < numberOfPoints; ++i) {
 24 | 		const time = date.getTime() / 1000;
 25 | 		const value = samplePoint(i);
 26 | 		res.push({
 27 | 			time,
 28 | 			value,
 29 | 		});
 30 | 
 31 | 		date.setUTCDate(date.getUTCDate() + 1);
 32 | 	}
 33 | 
 34 | 	return res;
 35 | }
 36 | 
 37 | function randomNumber(min, max) {
 38 | 	return Math.random() * (max - min) + min;
 39 | }
 40 | 
 41 | function randomBar(lastClose) {
 42 | 	const open = +randomNumber(lastClose * 0.95, lastClose * 1.05).toFixed(2);
 43 | 	const close = +randomNumber(open * 0.95, open * 1.05).toFixed(2);
 44 | 	const high = +randomNumber(
 45 | 		Math.max(open, close),
 46 | 		Math.max(open, close) * 1.1
 47 | 	).toFixed(2);
 48 | 	const low = +randomNumber(
 49 | 		Math.min(open, close) * 0.9,
 50 | 		Math.min(open, close)
 51 | 	).toFixed(2);
 52 | 	return {
 53 | 		open,
 54 | 		high,
 55 | 		low,
 56 | 		close,
 57 | 	};
 58 | }
 59 | 
 60 | function generateCandleData(numberOfPoints = 250, endDate) {
 61 | 	const lineData = generateLineData(numberOfPoints, endDate);
 62 | 	let lastClose = lineData[0].value;
 63 | 	return lineData.map(d => {
 64 | 		const candle = randomBar(lastClose);
 65 | 		lastClose = candle.close;
 66 | 		return {
 67 | 			time: d.time,
 68 | 			low: candle.low,
 69 | 			high: candle.high,
 70 | 			open: candle.open,
 71 | 			close: candle.close,
 72 | 		};
 73 | 	});
 74 | }
 75 | 
 76 | const chartOptions = {
 77 | 	layout: {
 78 | 		textColor: CHART_TEXT_COLOR,
 79 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
 80 | 	},
 81 | };
 82 | // hide-end
 83 | // remove-line
 84 | /** @type {import('lightweight-charts').IChartApi} */
 85 | const chart = createChart(document.getElementById('container'), chartOptions);
 86 | 
 87 | const barData = generateCandleData(500);
 88 | 
 89 | function calculateMovingAverageSeriesData(candleData, maLength) {
 90 | 	const maData = [];
 91 | 
 92 | 	for (let i = 0; i < candleData.length; i++) {
 93 | 		if (i < maLength) {
 94 | 			// Provide whitespace data points until the MA can be calculated
 95 | 			maData.push({ time: candleData[i].time });
 96 | 		} else {
 97 | 			// Calculate the moving average, slow but simple way
 98 | 			let sum = 0;
 99 | 			for (let j = 0; j < maLength; j++) {
100 | 				sum += candleData[i - j].close;
101 | 			}
102 | 			const maValue = sum / maLength;
103 | 			maData.push({ time: candleData[i].time, value: maValue });
104 | 		}
105 | 	}
106 | 
107 | 	return maData;
108 | }
109 | 
110 | const maData = calculateMovingAverageSeriesData(barData, 20);
111 | 
112 | const maSeries = chart.addSeries(LineSeries, { color: LINE_LINE_COLOR, lineWidth: 1 });
113 | maSeries.setData(maData);
114 | 
115 | const candlestickSeries = chart.addSeries(CandlestickSeries, {
116 | 	upColor: BAR_UP_COLOR,
117 | 	downColor: BAR_DOWN_COLOR,
118 | 	borderVisible: false,
119 | 	wickUpColor: BAR_UP_COLOR,
120 | 	wickDownColor: BAR_DOWN_COLOR,
121 | });
122 | candlestickSeries.setData(barData);
123 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/moving-average.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Moving average indicator
 3 | sidebar_label: Moving average
 4 | description: An example of how to add a moving average indicator line
 5 | pagination_prev: null
 6 | pagination_next: null
 7 | keywords:
 8 |   - moving average
 9 |   - indicator
10 | ---
11 | 
12 | This example demonstrates the implementation of a moving average (MA) indicator
13 | using Lightweight Charts™. It effectively shows how to overlay a line series
14 | representing the moving average on a candlestick series.
15 | 
16 | Initial rendering involves the creation of a candlestick series using randomly
17 | generated data. The `calculateMovingAverageSeriesData` function subsequently
18 | computes the 20-period MA data from the candlestick data. For each point, if
19 | less than 20 data points precede it, the function creates a whitespace data
20 | point. If 20 or more data points precede it, it calculates the MA for that
21 | period.
22 | 
23 | The MA data set forms a line series, which is placed underneath the candlestick
24 | series (by creating the line series first). As a result, users can view the
25 | underlying price data (via the candlestick series) in conjunction with the
26 | moving average trend line which provides valuable analytical insight.
27 | 
28 | import UsageGuidePartial from '../_usage-guide-partial.mdx';
29 | import CodeBlock from '@theme/CodeBlock';
30 | import code from '!!raw-loader!./moving-average.js';
31 | 
32 | <CodeBlock
33 | 	replaceThemeConstants
34 | 	chart
35 | 	className="language-js"
36 | 	hideableCode
37 | 	chartOnTop
38 | 	codeUsage={<UsageGuidePartial />}
39 | >
40 | 	{code}
41 | </CodeBlock>
42 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/range-switcher.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Range switcher
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/demos/range-switcher
  4 | 
  5 | // remove-end
  6 | 
  7 | const dayData = [
  8 | 	{ time: '2018-10-19', value: 26.19 },
  9 | 	// hide-start
 10 | 	{ time: '2018-10-22', value: 25.87 },
 11 | 	{ time: '2018-10-23', value: 25.83 },
 12 | 	{ time: '2018-10-24', value: 25.78 },
 13 | 	{ time: '2018-10-25', value: 25.82 },
 14 | 	{ time: '2018-10-26', value: 25.81 },
 15 | 	{ time: '2018-10-29', value: 25.82 },
 16 | 	{ time: '2018-10-30', value: 25.71 },
 17 | 	{ time: '2018-10-31', value: 25.82 },
 18 | 	{ time: '2018-11-01', value: 25.72 },
 19 | 	{ time: '2018-11-02', value: 25.74 },
 20 | 	{ time: '2018-11-05', value: 25.81 },
 21 | 	{ time: '2018-11-06', value: 25.75 },
 22 | 	{ time: '2018-11-07', value: 25.73 },
 23 | 	{ time: '2018-11-08', value: 25.75 },
 24 | 	{ time: '2018-11-09', value: 25.75 },
 25 | 	{ time: '2018-11-12', value: 25.76 },
 26 | 	{ time: '2018-11-13', value: 25.8 },
 27 | 	{ time: '2018-11-14', value: 25.77 },
 28 | 	{ time: '2018-11-15', value: 25.75 },
 29 | 	{ time: '2018-11-16', value: 25.75 },
 30 | 	{ time: '2018-11-19', value: 25.75 },
 31 | 	{ time: '2018-11-20', value: 25.72 },
 32 | 	{ time: '2018-11-21', value: 25.78 },
 33 | 	{ time: '2018-11-23', value: 25.72 },
 34 | 	{ time: '2018-11-26', value: 25.78 },
 35 | 	{ time: '2018-11-27', value: 25.85 },
 36 | 	{ time: '2018-11-28', value: 25.85 },
 37 | 	{ time: '2018-11-29', value: 25.55 },
 38 | 	{ time: '2018-11-30', value: 25.41 },
 39 | 	{ time: '2018-12-03', value: 25.41 },
 40 | 	{ time: '2018-12-04', value: 25.42 },
 41 | 	{ time: '2018-12-06', value: 25.33 },
 42 | 	{ time: '2018-12-07', value: 25.39 },
 43 | 	{ time: '2018-12-10', value: 25.32 },
 44 | 	{ time: '2018-12-11', value: 25.48 },
 45 | 	{ time: '2018-12-12', value: 25.39 },
 46 | 	{ time: '2018-12-13', value: 25.45 },
 47 | 	{ time: '2018-12-14', value: 25.52 },
 48 | 	{ time: '2018-12-17', value: 25.38 },
 49 | 	{ time: '2018-12-18', value: 25.36 },
 50 | 	{ time: '2018-12-19', value: 25.65 },
 51 | 	{ time: '2018-12-20', value: 25.7 },
 52 | 	{ time: '2018-12-21', value: 25.66 },
 53 | 	{ time: '2018-12-24', value: 25.66 },
 54 | 	{ time: '2018-12-26', value: 25.65 },
 55 | 	{ time: '2018-12-27', value: 25.66 },
 56 | 	{ time: '2018-12-28', value: 25.68 },
 57 | 	{ time: '2018-12-31', value: 25.77 },
 58 | 	{ time: '2019-01-02', value: 25.72 },
 59 | 	{ time: '2019-01-03', value: 25.69 },
 60 | 	{ time: '2019-01-04', value: 25.71 },
 61 | 	{ time: '2019-01-07', value: 25.72 },
 62 | 	{ time: '2019-01-08', value: 25.72 },
 63 | 	{ time: '2019-01-09', value: 25.66 },
 64 | 	{ time: '2019-01-10', value: 25.85 },
 65 | 	{ time: '2019-01-11', value: 25.92 },
 66 | 	{ time: '2019-01-14', value: 25.94 },
 67 | 	{ time: '2019-01-15', value: 25.95 },
 68 | 	{ time: '2019-01-16', value: 26.0 },
 69 | 	{ time: '2019-01-17', value: 25.99 },
 70 | 	{ time: '2019-01-18', value: 25.6 },
 71 | 	{ time: '2019-01-22', value: 25.81 },
 72 | 	{ time: '2019-01-23', value: 25.7 },
 73 | 	{ time: '2019-01-24', value: 25.74 },
 74 | 	{ time: '2019-01-25', value: 25.8 },
 75 | 	{ time: '2019-01-28', value: 25.83 },
 76 | 	{ time: '2019-01-29', value: 25.7 },
 77 | 	{ time: '2019-01-30', value: 25.78 },
 78 | 	{ time: '2019-01-31', value: 25.35 },
 79 | 	{ time: '2019-02-01', value: 25.6 },
 80 | 	{ time: '2019-02-04', value: 25.65 },
 81 | 	{ time: '2019-02-05', value: 25.73 },
 82 | 	{ time: '2019-02-06', value: 25.71 },
 83 | 	{ time: '2019-02-07', value: 25.71 },
 84 | 	{ time: '2019-02-08', value: 25.72 },
 85 | 	{ time: '2019-02-11', value: 25.76 },
 86 | 	{ time: '2019-02-12', value: 25.84 },
 87 | 	{ time: '2019-02-13', value: 25.85 },
 88 | 	{ time: '2019-02-14', value: 25.87 },
 89 | 	{ time: '2019-02-15', value: 25.89 },
 90 | 	{ time: '2019-02-19', value: 25.9 },
 91 | 	{ time: '2019-02-20', value: 25.92 },
 92 | 	{ time: '2019-02-21', value: 25.96 },
 93 | 	{ time: '2019-02-22', value: 26.0 },
 94 | 	{ time: '2019-02-25', value: 25.93 },
 95 | 	{ time: '2019-02-26', value: 25.92 },
 96 | 	{ time: '2019-02-27', value: 25.67 },
 97 | 	{ time: '2019-02-28', value: 25.79 },
 98 | 	{ time: '2019-03-01', value: 25.86 },
 99 | 	{ time: '2019-03-04', value: 25.94 },
100 | 	{ time: '2019-03-05', value: 26.02 },
101 | 	{ time: '2019-03-06', value: 25.95 },
102 | 	{ time: '2019-03-07', value: 25.89 },
103 | 	{ time: '2019-03-08', value: 25.94 },
104 | 	{ time: '2019-03-11', value: 25.91 },
105 | 	{ time: '2019-03-12', value: 25.92 },
106 | 	{ time: '2019-03-13', value: 26.0 },
107 | 	{ time: '2019-03-14', value: 26.05 },
108 | 	{ time: '2019-03-15', value: 26.11 },
109 | 	{ time: '2019-03-18', value: 26.1 },
110 | 	{ time: '2019-03-19', value: 25.98 },
111 | 	{ time: '2019-03-20', value: 26.11 },
112 | 	{ time: '2019-03-21', value: 26.12 },
113 | 	{ time: '2019-03-22', value: 25.88 },
114 | 	{ time: '2019-03-25', value: 25.85 },
115 | 	{ time: '2019-03-26', value: 25.72 },
116 | 	{ time: '2019-03-27', value: 25.73 },
117 | 	{ time: '2019-03-28', value: 25.8 },
118 | 	{ time: '2019-03-29', value: 25.77 },
119 | 	{ time: '2019-04-01', value: 26.06 },
120 | 	{ time: '2019-04-02', value: 25.93 },
121 | 	{ time: '2019-04-03', value: 25.95 },
122 | 	{ time: '2019-04-04', value: 26.06 },
123 | 	{ time: '2019-04-05', value: 26.16 },
124 | 	{ time: '2019-04-08', value: 26.12 },
125 | 	{ time: '2019-04-09', value: 26.07 },
126 | 	{ time: '2019-04-10', value: 26.13 },
127 | 	{ time: '2019-04-11', value: 26.04 },
128 | 	{ time: '2019-04-12', value: 26.04 },
129 | 	{ time: '2019-04-15', value: 26.05 },
130 | 	{ time: '2019-04-16', value: 26.01 },
131 | 	{ time: '2019-04-17', value: 26.09 },
132 | 	{ time: '2019-04-18', value: 26.0 },
133 | 	{ time: '2019-04-22', value: 26.0 },
134 | 	{ time: '2019-04-23', value: 26.06 },
135 | 	{ time: '2019-04-24', value: 26.0 },
136 | 	{ time: '2019-04-25', value: 25.81 },
137 | 	{ time: '2019-04-26', value: 25.88 },
138 | 	{ time: '2019-04-29', value: 25.91 },
139 | 	{ time: '2019-04-30', value: 25.9 },
140 | 	{ time: '2019-05-01', value: 26.02 },
141 | 	{ time: '2019-05-02', value: 25.97 },
142 | 	{ time: '2019-05-03', value: 26.02 },
143 | 	{ time: '2019-05-06', value: 26.03 },
144 | 	{ time: '2019-05-07', value: 26.04 },
145 | 	{ time: '2019-05-08', value: 26.05 },
146 | 	{ time: '2019-05-09', value: 26.05 },
147 | 	{ time: '2019-05-10', value: 26.08 },
148 | 	{ time: '2019-05-13', value: 26.05 },
149 | 	{ time: '2019-05-14', value: 26.01 },
150 | 	{ time: '2019-05-15', value: 26.03 },
151 | 	{ time: '2019-05-16', value: 26.14 },
152 | 	{ time: '2019-05-17', value: 26.09 },
153 | 	{ time: '2019-05-20', value: 26.01 },
154 | 	{ time: '2019-05-21', value: 26.12 },
155 | 	{ time: '2019-05-22', value: 26.15 },
156 | 	{ time: '2019-05-23', value: 26.18 },
157 | 	{ time: '2019-05-24', value: 26.16 },
158 | 	{ time: '2019-05-28', value: 26.23 },
159 | 	// hide-end
160 | ];
161 | 
162 | const weekData = [
163 | 	{ time: '2016-07-18', value: 26.1 },
164 | 	// hide-start
165 | 	{ time: '2016-07-25', value: 26.19 },
166 | 	{ time: '2016-08-01', value: 26.24 },
167 | 	{ time: '2016-08-08', value: 26.22 },
168 | 	{ time: '2016-08-15', value: 25.98 },
169 | 	{ time: '2016-08-22', value: 25.85 },
170 | 	{ time: '2016-08-29', value: 25.98 },
171 | 	{ time: '2016-09-05', value: 25.71 },
172 | 	{ time: '2016-09-12', value: 25.84 },
173 | 	{ time: '2016-09-19', value: 25.89 },
174 | 	{ time: '2016-09-26', value: 25.65 },
175 | 	{ time: '2016-10-03', value: 25.69 },
176 | 	{ time: '2016-10-10', value: 25.67 },
177 | 	{ time: '2016-10-17', value: 26.11 },
178 | 	{ time: '2016-10-24', value: 25.8 },
179 | 	{ time: '2016-10-31', value: 25.7 },
180 | 	{ time: '2016-11-07', value: 25.4 },
181 | 	{ time: '2016-11-14', value: 25.32 },
182 | 	{ time: '2016-11-21', value: 25.48 },
183 | 	{ time: '2016-11-28', value: 25.08 },
184 | 	{ time: '2016-12-05', value: 25.06 },
185 | 	{ time: '2016-12-12', value: 25.11 },
186 | 	{ time: '2016-12-19', value: 25.34 },
187 | 	{ time: '2016-12-26', value: 25.2 },
188 | 	{ time: '2017-01-02', value: 25.33 },
189 | 	{ time: '2017-01-09', value: 25.56 },
190 | 	{ time: '2017-01-16', value: 25.32 },
191 | 	{ time: '2017-01-23', value: 25.71 },
192 | 	{ time: '2017-01-30', value: 25.85 },
193 | 	{ time: '2017-02-06', value: 25.77 },
194 | 	{ time: '2017-02-13', value: 25.94 },
195 | 	{ time: '2017-02-20', value: 25.67 },
196 | 	{ time: '2017-02-27', value: 25.6 },
197 | 	{ time: '2017-03-06', value: 25.54 },
198 | 	{ time: '2017-03-13', value: 25.84 },
199 | 	{ time: '2017-03-20', value: 25.96 },
200 | 	{ time: '2017-03-27', value: 25.9 },
201 | 	{ time: '2017-04-03', value: 25.97 },
202 | 	{ time: '2017-04-10', value: 26.0 },
203 | 	{ time: '2017-04-17', value: 26.13 },
204 | 	{ time: '2017-04-24', value: 26.02 },
205 | 	{ time: '2017-05-01', value: 26.3 },
206 | 	{ time: '2017-05-08', value: 26.27 },
207 | 	{ time: '2017-05-15', value: 26.24 },
208 | 	{ time: '2017-05-22', value: 26.02 },
209 | 	{ time: '2017-05-29', value: 26.2 },
210 | 	{ time: '2017-06-05', value: 26.12 },
211 | 	{ time: '2017-06-12', value: 26.2 },
212 | 	{ time: '2017-06-19', value: 26.46 },
213 | 	{ time: '2017-06-26', value: 26.39 },
214 | 	{ time: '2017-07-03', value: 26.52 },
215 | 	{ time: '2017-07-10', value: 26.57 },
216 | 	{ time: '2017-07-17', value: 26.65 },
217 | 	{ time: '2017-07-24', value: 26.45 },
218 | 	{ time: '2017-07-31', value: 26.37 },
219 | 	{ time: '2017-08-07', value: 26.13 },
220 | 	{ time: '2017-08-14', value: 26.21 },
221 | 	{ time: '2017-08-21', value: 26.31 },
222 | 	{ time: '2017-08-28', value: 26.33 },
223 | 	{ time: '2017-09-04', value: 26.38 },
224 | 	{ time: '2017-09-11', value: 26.38 },
225 | 	{ time: '2017-09-18', value: 26.5 },
226 | 	{ time: '2017-09-25', value: 26.39 },
227 | 	{ time: '2017-10-02', value: 25.95 },
228 | 	{ time: '2017-10-09', value: 26.15 },
229 | 	{ time: '2017-10-16', value: 26.43 },
230 | 	{ time: '2017-10-23', value: 26.22 },
231 | 	{ time: '2017-10-30', value: 26.14 },
232 | 	{ time: '2017-11-06', value: 26.08 },
233 | 	{ time: '2017-11-13', value: 26.27 },
234 | 	{ time: '2017-11-20', value: 26.3 },
235 | 	{ time: '2017-11-27', value: 25.92 },
236 | 	{ time: '2017-12-04', value: 26.1 },
237 | 	{ time: '2017-12-11', value: 25.88 },
238 | 	{ time: '2017-12-18', value: 25.82 },
239 | 	{ time: '2017-12-25', value: 25.82 },
240 | 	{ time: '2018-01-01', value: 25.81 },
241 | 	{ time: '2018-01-08', value: 25.95 },
242 | 	{ time: '2018-01-15', value: 26.03 },
243 | 	{ time: '2018-01-22', value: 26.04 },
244 | 	{ time: '2018-01-29', value: 25.96 },
245 | 	{ time: '2018-02-05', value: 25.99 },
246 | 	{ time: '2018-02-12', value: 26.0 },
247 | 	{ time: '2018-02-19', value: 26.06 },
248 | 	{ time: '2018-02-26', value: 25.77 },
249 | 	{ time: '2018-03-05', value: 25.81 },
250 | 	{ time: '2018-03-12', value: 25.88 },
251 | 	{ time: '2018-03-19', value: 25.72 },
252 | 	{ time: '2018-03-26', value: 25.75 },
253 | 	{ time: '2018-04-02', value: 25.7 },
254 | 	{ time: '2018-04-09', value: 25.73 },
255 | 	{ time: '2018-04-16', value: 25.74 },
256 | 	{ time: '2018-04-23', value: 25.69 },
257 | 	{ time: '2018-04-30', value: 25.76 },
258 | 	{ time: '2018-05-07', value: 25.89 },
259 | 	{ time: '2018-05-14', value: 25.89 },
260 | 	{ time: '2018-05-21', value: 26.0 },
261 | 	{ time: '2018-05-28', value: 25.79 },
262 | 	{ time: '2018-06-04', value: 26.11 },
263 | 	{ time: '2018-06-11', value: 26.43 },
264 | 	{ time: '2018-06-18', value: 26.3 },
265 | 	{ time: '2018-06-25', value: 26.58 },
266 | 	{ time: '2018-07-02', value: 26.33 },
267 | 	{ time: '2018-07-09', value: 26.33 },
268 | 	{ time: '2018-07-16', value: 26.32 },
269 | 	{ time: '2018-07-23', value: 26.2 },
270 | 	{ time: '2018-07-30', value: 26.03 },
271 | 	{ time: '2018-08-06', value: 26.15 },
272 | 	{ time: '2018-08-13', value: 26.17 },
273 | 	{ time: '2018-08-20', value: 26.28 },
274 | 	{ time: '2018-08-27', value: 25.86 },
275 | 	{ time: '2018-09-03', value: 25.69 },
276 | 	{ time: '2018-09-10', value: 25.69 },
277 | 	{ time: '2018-09-17', value: 25.64 },
278 | 	{ time: '2018-09-24', value: 25.67 },
279 | 	{ time: '2018-10-01', value: 25.55 },
280 | 	{ time: '2018-10-08', value: 25.59 },
281 | 	{ time: '2018-10-15', value: 26.19 },
282 | 	{ time: '2018-10-22', value: 25.81 },
283 | 	{ time: '2018-10-29', value: 25.74 },
284 | 	{ time: '2018-11-05', value: 25.75 },
285 | 	{ time: '2018-11-12', value: 25.75 },
286 | 	{ time: '2018-11-19', value: 25.72 },
287 | 	{ time: '2018-11-26', value: 25.41 },
288 | 	{ time: '2018-12-03', value: 25.39 },
289 | 	{ time: '2018-12-10', value: 25.52 },
290 | 	{ time: '2018-12-17', value: 25.66 },
291 | 	{ time: '2018-12-24', value: 25.68 },
292 | 	{ time: '2018-12-31', value: 25.71 },
293 | 	{ time: '2019-01-07', value: 25.92 },
294 | 	{ time: '2019-01-14', value: 25.6 },
295 | 	{ time: '2019-01-21', value: 25.8 },
296 | 	{ time: '2019-01-28', value: 25.6 },
297 | 	{ time: '2019-02-04', value: 25.72 },
298 | 	{ time: '2019-02-11', value: 25.89 },
299 | 	{ time: '2019-02-18', value: 26.0 },
300 | 	{ time: '2019-02-25', value: 25.86 },
301 | 	{ time: '2019-03-04', value: 25.94 },
302 | 	{ time: '2019-03-11', value: 26.11 },
303 | 	{ time: '2019-03-18', value: 25.88 },
304 | 	{ time: '2019-03-25', value: 25.77 },
305 | 	{ time: '2019-04-01', value: 26.16 },
306 | 	{ time: '2019-04-08', value: 26.04 },
307 | 	{ time: '2019-04-15', value: 26.0 },
308 | 	{ time: '2019-04-22', value: 25.88 },
309 | 	{ time: '2019-04-29', value: 26.02 },
310 | 	{ time: '2019-05-06', value: 26.08 },
311 | 	{ time: '2019-05-13', value: 26.09 },
312 | 	{ time: '2019-05-20', value: 26.16 },
313 | 	{ time: '2019-05-27', value: 26.23 },
314 | 	// hide-end
315 | ];
316 | 
317 | const monthData = [
318 | 	{ time: '2006-12-01', value: 25.4 },
319 | 	// hide-start
320 | 	{ time: '2007-01-01', value: 25.5 },
321 | 	{ time: '2007-02-01', value: 25.11 },
322 | 	{ time: '2007-03-01', value: 25.24 },
323 | 	{ time: '2007-04-02', value: 25.34 },
324 | 	{ time: '2007-05-01', value: 24.82 },
325 | 	{ time: '2007-06-01', value: 23.85 },
326 | 	{ time: '2007-07-02', value: 23.24 },
327 | 	{ time: '2007-08-01', value: 23.05 },
328 | 	{ time: '2007-09-03', value: 22.26 },
329 | 	{ time: '2007-10-01', value: 22.52 },
330 | 	{ time: '2007-11-01', value: 20.84 },
331 | 	{ time: '2007-12-03', value: 20.37 },
332 | 	{ time: '2008-01-01', value: 23.9 },
333 | 	{ time: '2008-02-01', value: 22.58 },
334 | 	{ time: '2008-03-03', value: 21.74 },
335 | 	{ time: '2008-04-01', value: 22.5 },
336 | 	{ time: '2008-05-01', value: 22.38 },
337 | 	{ time: '2008-06-02', value: 20.58 },
338 | 	{ time: '2008-07-01', value: 20.6 },
339 | 	{ time: '2008-08-01', value: 20.82 },
340 | 	{ time: '2008-09-01', value: 17.5 },
341 | 	{ time: '2008-10-01', value: 17.7 },
342 | 	{ time: '2008-11-03', value: 15.52 },
343 | 	{ time: '2008-12-01', value: 18.58 },
344 | 	{ time: '2009-01-01', value: 15.4 },
345 | 	{ time: '2009-02-02', value: 11.68 },
346 | 	{ time: '2009-03-02', value: 14.89 },
347 | 	{ time: '2009-04-01', value: 16.24 },
348 | 	{ time: '2009-05-01', value: 18.33 },
349 | 	{ time: '2009-06-01', value: 18.08 },
350 | 	{ time: '2009-07-01', value: 20.07 },
351 | 	{ time: '2009-08-03', value: 20.35 },
352 | 	{ time: '2009-09-01', value: 21.53 },
353 | 	{ time: '2009-10-01', value: 21.48 },
354 | 	{ time: '2009-11-02', value: 20.28 },
355 | 	{ time: '2009-12-01', value: 21.39 },
356 | 	{ time: '2010-01-01', value: 22.0 },
357 | 	{ time: '2010-02-01', value: 22.31 },
358 | 	{ time: '2010-03-01', value: 22.82 },
359 | 	{ time: '2010-04-01', value: 22.58 },
360 | 	{ time: '2010-05-03', value: 21.02 },
361 | 	{ time: '2010-06-01', value: 21.45 },
362 | 	{ time: '2010-07-01', value: 22.42 },
363 | 	{ time: '2010-08-02', value: 23.61 },
364 | 	{ time: '2010-09-01', value: 24.4 },
365 | 	{ time: '2010-10-01', value: 24.46 },
366 | 	{ time: '2010-11-01', value: 23.64 },
367 | 	{ time: '2010-12-01', value: 22.9 },
368 | 	{ time: '2011-01-03', value: 23.73 },
369 | 	{ time: '2011-02-01', value: 23.52 },
370 | 	{ time: '2011-03-01', value: 24.15 },
371 | 	{ time: '2011-04-01', value: 24.37 },
372 | 	{ time: '2011-05-02', value: 24.4 },
373 | 	{ time: '2011-06-01', value: 24.45 },
374 | 	{ time: '2011-07-01', value: 24.24 },
375 | 	{ time: '2011-08-01', value: 24.0 },
376 | 	{ time: '2011-09-01', value: 22.77 },
377 | 	{ time: '2011-10-03', value: 24.21 },
378 | 	{ time: '2011-11-01', value: 23.4 },
379 | 	{ time: '2011-12-01', value: 23.9 },
380 | 	{ time: '2012-01-02', value: 24.84 },
381 | 	{ time: '2012-02-01', value: 25.04 },
382 | 	{ time: '2012-03-01', value: 24.9 },
383 | 	{ time: '2012-04-02', value: 25.06 },
384 | 	{ time: '2012-05-01', value: 24.63 },
385 | 	{ time: '2012-06-01', value: 25.07 },
386 | 	{ time: '2012-07-02', value: 25.3 },
387 | 	{ time: '2012-08-01', value: 25.08 },
388 | 	{ time: '2012-09-03', value: 25.27 },
389 | 	{ time: '2012-10-01', value: 25.39 },
390 | 	{ time: '2012-11-01', value: 25.06 },
391 | 	{ time: '2012-12-03', value: 25.03 },
392 | 	{ time: '2013-01-01', value: 25.26 },
393 | 	{ time: '2013-02-01', value: 25.2 },
394 | 	{ time: '2013-03-01', value: 25.3 },
395 | 	{ time: '2013-04-01', value: 25.38 },
396 | 	{ time: '2013-05-01', value: 25.22 },
397 | 	{ time: '2013-06-03', value: 24.88 },
398 | 	{ time: '2013-07-01', value: 24.98 },
399 | 	{ time: '2013-08-01', value: 24.6 },
400 | 	{ time: '2013-09-02', value: 24.65 },
401 | 	{ time: '2013-10-01', value: 24.62 },
402 | 	{ time: '2013-11-01', value: 24.65 },
403 | 	{ time: '2013-12-02', value: 24.7 },
404 | 	{ time: '2014-01-01', value: 24.98 },
405 | 	{ time: '2014-02-03', value: 24.95 },
406 | 	{ time: '2014-03-03', value: 25.45 },
407 | 	{ time: '2014-04-01', value: 25.4 },
408 | 	{ time: '2014-05-01', value: 25.51 },
409 | 	{ time: '2014-06-02', value: 25.34 },
410 | 	{ time: '2014-07-01', value: 25.3 },
411 | 	{ time: '2014-08-01', value: 25.36 },
412 | 	{ time: '2014-09-01', value: 25.16 },
413 | 	{ time: '2014-10-01', value: 25.53 },
414 | 	{ time: '2014-11-03', value: 25.4 },
415 | 	{ time: '2014-12-01', value: 25.7 },
416 | 	{ time: '2015-01-01', value: 25.95 },
417 | 	{ time: '2015-02-02', value: 25.81 },
418 | 	{ time: '2015-03-02', value: 25.63 },
419 | 	{ time: '2015-04-01', value: 25.39 },
420 | 	{ time: '2015-05-01', value: 25.62 },
421 | 	{ time: '2015-06-01', value: 25.23 },
422 | 	{ time: '2015-07-01', value: 25.47 },
423 | 	{ time: '2015-08-03', value: 25.18 },
424 | 	{ time: '2015-09-01', value: 25.3 },
425 | 	{ time: '2015-10-01', value: 25.68 },
426 | 	{ time: '2015-11-02', value: 25.63 },
427 | 	{ time: '2015-12-01', value: 25.57 },
428 | 	{ time: '2016-01-01', value: 25.55 },
429 | 	{ time: '2016-02-01', value: 25.05 },
430 | 	{ time: '2016-03-01', value: 25.61 },
431 | 	{ time: '2016-04-01', value: 25.91 },
432 | 	{ time: '2016-05-02', value: 25.84 },
433 | 	{ time: '2016-06-01', value: 25.94 },
434 | 	{ time: '2016-07-01', value: 26.19 },
435 | 	{ time: '2016-08-01', value: 26.06 },
436 | 	{ time: '2016-09-01', value: 25.65 },
437 | 	{ time: '2016-10-03', value: 25.8 },
438 | 	{ time: '2016-11-01', value: 25.06 },
439 | 	{ time: '2016-12-01', value: 25.2 },
440 | 	{ time: '2017-01-02', value: 25.7 },
441 | 	{ time: '2017-02-01', value: 25.78 },
442 | 	{ time: '2017-03-01', value: 25.9 },
443 | 	{ time: '2017-04-03', value: 26.02 },
444 | 	{ time: '2017-05-01', value: 26.02 },
445 | 	{ time: '2017-06-01', value: 26.39 },
446 | 	{ time: '2017-07-03', value: 26.3 },
447 | 	{ time: '2017-08-01', value: 26.14 },
448 | 	{ time: '2017-09-01', value: 26.39 },
449 | 	{ time: '2017-10-02', value: 26.12 },
450 | 	{ time: '2017-11-01', value: 25.81 },
451 | 	{ time: '2017-12-01', value: 25.82 },
452 | 	{ time: '2018-01-01', value: 26.06 },
453 | 	{ time: '2018-02-01', value: 25.78 },
454 | 	{ time: '2018-03-01', value: 25.75 },
455 | 	{ time: '2018-04-02', value: 25.72 },
456 | 	{ time: '2018-05-01', value: 25.75 },
457 | 	{ time: '2018-06-01', value: 26.58 },
458 | 	{ time: '2018-07-02', value: 26.14 },
459 | 	{ time: '2018-08-01', value: 25.86 },
460 | 	{ time: '2018-09-03', value: 25.67 },
461 | 	{ time: '2018-10-01', value: 25.82 },
462 | 	{ time: '2018-11-01', value: 25.41 },
463 | 	{ time: '2018-12-03', value: 25.77 },
464 | 	{ time: '2019-01-01', value: 25.35 },
465 | 	{ time: '2019-02-01', value: 25.79 },
466 | 	{ time: '2019-03-01', value: 25.77 },
467 | 	{ time: '2019-04-01', value: 25.9 },
468 | 	{ time: '2019-05-01', value: 26.23 },
469 | 	// hide-end
470 | ];
471 | 
472 | const yearData = [
473 | 	{ time: '2006-01-02', value: 24.89 },
474 | 	// hide-start
475 | 	{ time: '2007-01-01', value: 25.5 },
476 | 	{ time: '2008-01-01', value: 23.9 },
477 | 	{ time: '2009-01-01', value: 15.4 },
478 | 	{ time: '2010-01-01', value: 22.0 },
479 | 	{ time: '2011-01-03', value: 23.73 },
480 | 	{ time: '2012-01-02', value: 24.84 },
481 | 	{ time: '2013-01-01', value: 25.26 },
482 | 	{ time: '2014-01-01', value: 24.98 },
483 | 	{ time: '2015-01-01', value: 25.95 },
484 | 	{ time: '2016-01-01', value: 25.55 },
485 | 	{ time: '2017-01-02', value: 25.7 },
486 | 	{ time: '2018-01-01', value: 26.06 },
487 | 	{ time: '2019-01-01', value: 26.23 },
488 | 	// hide-end
489 | ];
490 | 
491 | const seriesesData = new Map([
492 | 	['1D', dayData],
493 | 	['1W', weekData],
494 | 	['1M', monthData],
495 | 	['1Y', yearData],
496 | ]);
497 | 
498 | // hide-start
499 | const chartOptions = {
500 | 	layout: {
501 | 		textColor: CHART_TEXT_COLOR,
502 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
503 | 	},
504 | 	height: 200,
505 | };
506 | // hide-end
507 | const container = document.getElementById('container');
508 | // remove-line
509 | /** @type {import('lightweight-charts').IChartApi} */
510 | const chart = createChart(container, chartOptions);
511 | 
512 | // remove-start
513 | // Only needed within demo page
514 | // eslint-disable-next-line no-undef
515 | window.addEventListener('resize', () => {
516 | 	chart.applyOptions({ height: 200 });
517 | });
518 | // remove-end
519 | 
520 | const intervalColors = {
521 | 	'1D': LINE_LINE_COLOR,
522 | 	'1W': LINE_LINE2_COLOR,
523 | 	'1M': LINE_LINE3_COLOR,
524 | 	'1Y': LINE_LINE4_COLOR,
525 | };
526 | 
527 | const lineSeries = chart.addSeries(LineSeries, { color: intervalColors['1D'] });
528 | 
529 | function setChartInterval(interval) {
530 | 	lineSeries.setData(seriesesData.get(interval));
531 | 	lineSeries.applyOptions({
532 | 		color: intervalColors[interval],
533 | 	});
534 | 	chart.timeScale().fitContent();
535 | }
536 | 
537 | setChartInterval('1D');
538 | 
539 | // hide-start
540 | const styles = `
541 |     .buttons-container {
542 |         display: flex;
543 |         flex-direction: row;
544 |         gap: 8px;
545 |     }
546 |     .buttons-container button {
547 |         all: initial;
548 |         font-family: -apple-system, BlinkMacSystemFont, 'Trebuchet MS', Roboto, Ubuntu,
549 |             sans-serif;
550 |         font-size: 16px;
551 |         font-style: normal;
552 |         font-weight: 510;
553 |         line-height: 24px; /* 150% */
554 |         letter-spacing: -0.32px;
555 |         padding: 8px 24px;
556 |         color: rgba(19, 23, 34, 1);
557 |         background-color: rgba(240, 243, 250, 1);
558 |         border-radius: 8px;
559 |         cursor: pointer;
560 |     }
561 | 
562 |     .buttons-container button:hover {
563 |         background-color: rgba(224, 227, 235, 1);
564 |     }
565 | 
566 |     .buttons-container button:active {
567 |         background-color: rgba(209, 212, 220, 1);
568 |     }
569 | `;
570 | 
571 | const stylesElement = document.createElement('style');
572 | stylesElement.innerHTML = styles;
573 | container.appendChild(stylesElement);
574 | 
575 | const buttonsContainer = document.createElement('div');
576 | buttonsContainer.classList.add('buttons-container');
577 | // hide-end
578 | const intervals = ['1D', '1W', '1M', '1Y'];
579 | intervals.forEach(interval => {
580 | 	const button = document.createElement('button');
581 | 	button.innerText = interval;
582 | 	button.addEventListener('click', () => setChartInterval(interval));
583 | 	buttonsContainer.appendChild(button);
584 | });
585 | 
586 | container.appendChild(buttonsContainer);
587 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/range-switcher.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Range switcher
 3 | sidebar_label: Range switcher
 4 | description: An example of how to switch range (resolution) of the chart
 5 | pagination_prev: null
 6 | pagination_next: null
 7 | keywords:
 8 |   - range
 9 |   - resolution
10 | ---
11 | 
12 | This example illustrates the creation of a range switcher in Lightweight Charts™
13 | that allows for changing the data set displayed based on a selected time range
14 | or interval. Different data sets representing ranges such as daily ('1D'),
15 | weekly ('1W'), monthly ('1M'), and yearly ('1Y') are prepared.
16 | 
17 | The chart begins with daily data displayed by default. Then, buttons
18 | corresponding to each predefined interval are created. When a user clicks one of
19 | these buttons, the `setChartInterval` function is called with the chosen
20 | interval, swapping the currently displayed data series with the one
21 | corresponding to the chosen interval. Consequently, the viewers can quickly
22 | switch between different timeframes, providing flexible analysis of the data
23 | trends.
24 | 
25 | import UsageGuidePartial from '../_usage-guide-partial.mdx';
26 | import CodeBlock from '@theme/CodeBlock';
27 | import code from '!!raw-loader!./range-switcher.js';
28 | 
29 | <CodeBlock
30 | 	replaceThemeConstants
31 | 	chart
32 | 	className="language-js"
33 | 	hideableCode
34 | 	chartOnTop
35 | 	codeUsage={<UsageGuidePartial />}
36 | >
37 | 	{code}
38 | </CodeBlock>
39 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/realtime-updates.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Realtime updates
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/demos/realtime-updates
  4 | 
  5 | // remove-end
  6 | 
  7 | // hide-start
  8 | let randomFactor = 25 + Math.random() * 25;
  9 | const samplePoint = i =>
 10 | 	i *
 11 | 		(0.5 +
 12 | 			Math.sin(i / 1) * 0.2 +
 13 | 			Math.sin(i / 2) * 0.4 +
 14 | 			Math.sin(i / randomFactor) * 0.8 +
 15 | 			Math.sin(i / 50) * 0.5) +
 16 | 	200 +
 17 | 	i * 2;
 18 | 
 19 | function generateData(
 20 | 	numberOfCandles = 500,
 21 | 	updatesPerCandle = 5,
 22 | 	startAt = 100
 23 | ) {
 24 | 	const createCandle = (val, time) => ({
 25 | 		time,
 26 | 		open: val,
 27 | 		high: val,
 28 | 		low: val,
 29 | 		close: val,
 30 | 	});
 31 | 
 32 | 	const updateCandle = (candle, val) => ({
 33 | 		time: candle.time,
 34 | 		close: val,
 35 | 		open: candle.open,
 36 | 		low: Math.min(candle.low, val),
 37 | 		high: Math.max(candle.high, val),
 38 | 	});
 39 | 
 40 | 	randomFactor = 25 + Math.random() * 25;
 41 | 	const date = new Date(Date.UTC(2018, 0, 1, 12, 0, 0, 0));
 42 | 	const numberOfPoints = numberOfCandles * updatesPerCandle;
 43 | 	const initialData = [];
 44 | 	const realtimeUpdates = [];
 45 | 	let lastCandle;
 46 | 	let previousValue = samplePoint(-1);
 47 | 	for (let i = 0; i < numberOfPoints; ++i) {
 48 | 		if (i % updatesPerCandle === 0) {
 49 | 			date.setUTCDate(date.getUTCDate() + 1);
 50 | 		}
 51 | 		const time = date.getTime() / 1000;
 52 | 		let value = samplePoint(i);
 53 | 		const diff = (value - previousValue) * Math.random();
 54 | 		value = previousValue + diff;
 55 | 		previousValue = value;
 56 | 		if (i % updatesPerCandle === 0) {
 57 | 			const candle = createCandle(value, time);
 58 | 			lastCandle = candle;
 59 | 			if (i >= startAt) {
 60 | 				realtimeUpdates.push(candle);
 61 | 			}
 62 | 		} else {
 63 | 			const newCandle = updateCandle(lastCandle, value);
 64 | 			lastCandle = newCandle;
 65 | 			if (i >= startAt) {
 66 | 				realtimeUpdates.push(newCandle);
 67 | 			} else if ((i + 1) % updatesPerCandle === 0) {
 68 | 				initialData.push(newCandle);
 69 | 			}
 70 | 		}
 71 | 	}
 72 | 
 73 | 	return {
 74 | 		initialData,
 75 | 		realtimeUpdates,
 76 | 	};
 77 | }
 78 | 
 79 | const chartOptions = {
 80 | 	layout: {
 81 | 		textColor: CHART_TEXT_COLOR,
 82 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
 83 | 	},
 84 | 	height: 200,
 85 | };
 86 | // hide-end
 87 | const container = document.getElementById('container');
 88 | // remove-line
 89 | /** @type {import('lightweight-charts').IChartApi} */
 90 | const chart = createChart(container, chartOptions);
 91 | 
 92 | // remove-start
 93 | // Only needed within demo page
 94 | // eslint-disable-next-line no-undef
 95 | window.addEventListener('resize', () => {
 96 | 	chart.applyOptions({ height: 200 });
 97 | });
 98 | // remove-end
 99 | 
100 | const series = chart.addSeries(CandlestickSeries, {
101 | 	upColor: BAR_UP_COLOR,
102 | 	downColor: BAR_DOWN_COLOR,
103 | 	borderVisible: false,
104 | 	wickUpColor: BAR_UP_COLOR,
105 | 	wickDownColor: BAR_DOWN_COLOR,
106 | });
107 | 
108 | const data = generateData(2500, 20, 1000);
109 | 
110 | series.setData(data.initialData);
111 | chart.timeScale().fitContent();
112 | chart.timeScale().scrollToPosition(5);
113 | 
114 | // simulate real-time data
115 | function* getNextRealtimeUpdate(realtimeData) {
116 | 	for (const dataPoint of realtimeData) {
117 | 		yield dataPoint;
118 | 	}
119 | 	return null;
120 | }
121 | const streamingDataProvider = getNextRealtimeUpdate(data.realtimeUpdates);
122 | 
123 | const intervalID = setInterval(() => {
124 | 	const update = streamingDataProvider.next();
125 | 	if (update.done) {
126 | 		clearInterval(intervalID);
127 | 		return;
128 | 	}
129 | 	series.update(update.value);
130 | }, 100);
131 | 
132 | // hide-start
133 | const styles = `
134 |     .buttons-container {
135 |         display: flex;
136 |         flex-direction: row;
137 |         gap: 8px;
138 |     }
139 |     .buttons-container button {
140 |         all: initial;
141 |         font-family: -apple-system, BlinkMacSystemFont, 'Trebuchet MS', Roboto, Ubuntu,
142 |             sans-serif;
143 |         font-size: 16px;
144 |         font-style: normal;
145 |         font-weight: 510;
146 |         line-height: 24px; /* 150% */
147 |         letter-spacing: -0.32px;
148 |         padding: 8px 24px;
149 |         color: rgba(19, 23, 34, 1);
150 |         background-color: rgba(240, 243, 250, 1);
151 |         border-radius: 8px;
152 |         cursor: pointer;
153 |     }
154 | 
155 |     .buttons-container button:hover {
156 |         background-color: rgba(224, 227, 235, 1);
157 |     }
158 | 
159 |     .buttons-container button:active {
160 |         background-color: rgba(209, 212, 220, 1);
161 |     }
162 | `;
163 | 
164 | const stylesElement = document.createElement('style');
165 | stylesElement.innerHTML = styles;
166 | container.appendChild(stylesElement);
167 | 
168 | const buttonsContainer = document.createElement('div');
169 | buttonsContainer.classList.add('buttons-container');
170 | // hide-end
171 | const button = document.createElement('button');
172 | button.innerText = 'Go to realtime';
173 | button.addEventListener('click', () => chart.timeScale().scrollToRealTime());
174 | buttonsContainer.appendChild(button);
175 | 
176 | container.appendChild(buttonsContainer);
177 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/realtime-updates.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Realtime updates
 3 | sidebar_label: Realtime updates
 4 | description: An example of how to handle realtime updates
 5 | pagination_prev: null
 6 | pagination_next: null
 7 | keywords:
 8 |   - realtime updates
 9 | ---
10 | 
11 | This sample demonstrates how to mimic real-time updates on a candlestick chart
12 | with Lightweight Charts™. The chart initially populates with some historical
13 | data. By using `setInterval` function, the chart then begins to receive
14 | simulated real-time updates with the usage of `series.update(...)`.
15 | 
16 | Each real-time update represents a new data point or modifies the latest point,
17 | providing the illusion of a live, updating chart. If you scroll the chart and
18 | wish to return to the latest data points then you can use the "Go to realtime"
19 | button provided which calls the
20 | [`scrollToRealtime`](/docs/api/interfaces/ITimeScaleApi#scrolltorealtime) method
21 | on the timescale.
22 | 
23 | import UsageGuidePartial from '../_usage-guide-partial.mdx';
24 | import CodeBlock from '@theme/CodeBlock';
25 | import code from '!!raw-loader!./realtime-updates.js';
26 | 
27 | <CodeBlock
28 | 	replaceThemeConstants
29 | 	chart
30 | 	className="language-js"
31 | 	hideableCode
32 | 	chartOnTop
33 | 	codeUsage={<UsageGuidePartial />}
34 | >
35 | 	{code}
36 | </CodeBlock>
37 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/whitespace.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Whitespace data
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/demos/whitespace
  4 | 
  5 | // remove-end
  6 | // hide-start
  7 | const chartOptions = {
  8 | 	layout: {
  9 | 		textColor: CHART_TEXT_COLOR,
 10 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
 11 | 	},
 12 | };
 13 | // hide-end
 14 | const container = document.getElementById('container');
 15 | // remove-line
 16 | /** @type {import('lightweight-charts').IChartApi} */
 17 | const chart = createChart(container, chartOptions);
 18 | 
 19 | const candlestickSeries = chart.addSeries(CandlestickSeries, {
 20 | 	upColor: BAR_UP_COLOR,
 21 | 	downColor: BAR_DOWN_COLOR,
 22 | 	borderVisible: false,
 23 | 	wickUpColor: BAR_UP_COLOR,
 24 | 	wickDownColor: BAR_DOWN_COLOR,
 25 | });
 26 | 
 27 | candlestickSeries.setData([
 28 | 	{
 29 | 		close: 108.9974612905403,
 30 | 		high: 121.20998259466148,
 31 | 		low: 96.65376292551082,
 32 | 		open: 104.5614412226746,
 33 | 		time: { year: 2018, month: 9, day: 22 },
 34 | 	},
 35 | 	{
 36 | 		close: 110.46815600023501,
 37 | 		high: 111.3650273696516,
 38 | 		low: 82.65543461471314,
 39 | 		open: 110.16538466099634,
 40 | 		time: { year: 2018, month: 9, day: 23 },
 41 | 	},
 42 | 	// highlight-start
 43 | 	{
 44 | 		// Whitespace data, only time is provided
 45 | 		time: { year: 2018, month: 9, day: 24 },
 46 | 	},
 47 | 	// highlight-end
 48 | 	{
 49 | 		close: 96.80120024431532,
 50 | 		high: 101.92074283374939,
 51 | 		low: 89.25819769856513,
 52 | 		open: 89.25819769856513,
 53 | 		time: { year: 2018, month: 9, day: 25 },
 54 | 	},
 55 | 	// hide-start
 56 | 	{
 57 | 		close: 94.87113928076117,
 58 | 		high: 104.12503365679314,
 59 | 		low: 85.42405005240111,
 60 | 		open: 104.12503365679314,
 61 | 		time: { year: 2018, month: 9, day: 26 },
 62 | 	},
 63 | 	{
 64 | 		close: 100.76494087674855,
 65 | 		high: 102.60508417239113,
 66 | 		low: 80.76268547064865,
 67 | 		open: 92.93299948659636,
 68 | 		time: { year: 2018, month: 9, day: 27 },
 69 | 	},
 70 | 	{
 71 | 		close: 101.45855928883597,
 72 | 		high: 110.26727325817173,
 73 | 		low: 91.10348900896837,
 74 | 		open: 93.4362185148034,
 75 | 		time: { year: 2018, month: 9, day: 28 },
 76 | 	},
 77 | 	{
 78 | 		close: 91.68871815146144,
 79 | 		high: 103.73263644407702,
 80 | 		low: 73.5329263610334,
 81 | 		open: 92.96467883926464,
 82 | 		time: { year: 2018, month: 9, day: 29 },
 83 | 	},
 84 | 	{
 85 | 		time: { year: 2018, month: 9, day: 30 },
 86 | 	},
 87 | 	{
 88 | 		time: { year: 2018, month: 10, day: 1 },
 89 | 	},
 90 | 	{
 91 | 		close: 89.26733004009083,
 92 | 		high: 89.26733004009083,
 93 | 		low: 76.27851645958225,
 94 | 		open: 85.83860311023625,
 95 | 		time: { year: 2018, month: 10, day: 2 },
 96 | 	},
 97 | 	{
 98 | 		close: 89.66035763006947,
 99 | 		high: 89.66035763006947,
100 | 		low: 67.63677527399729,
101 | 		open: 77.79584976144585,
102 | 		time: { year: 2018, month: 10, day: 3 },
103 | 	},
104 | 	{
105 | 		close: 89.59687813884807,
106 | 		high: 97.05916949817754,
107 | 		low: 72.9823390058379,
108 | 		open: 77.37388423995716,
109 | 		time: { year: 2018, month: 10, day: 4 },
110 | 	},
111 | 	{
112 | 		close: 83.6425403120788,
113 | 		high: 91.72593377862522,
114 | 		low: 65.27208271740422,
115 | 		open: 85.92711686401718,
116 | 		time: { year: 2018, month: 10, day: 5 },
117 | 	},
118 | 	{
119 | 		close: 82.99053929200655,
120 | 		high: 93.4482645370556,
121 | 		low: 65.98920655616067,
122 | 		open: 71.8940788814462,
123 | 		time: { year: 2018, month: 10, day: 6 },
124 | 	},
125 | 	{
126 | 		time: { year: 2018, month: 10, day: 7 },
127 | 	},
128 | 	{
129 | 		time: { year: 2018, month: 10, day: 8 },
130 | 	},
131 | 	{
132 | 		close: 77.60439116240829,
133 | 		high: 83.20908153481327,
134 | 		low: 68.56836128158209,
135 | 		open: 75.83440719565763,
136 | 		time: { year: 2018, month: 10, day: 9 },
137 | 	},
138 | 	{
139 | 		close: 73.8952889203428,
140 | 		high: 81.89987377779327,
141 | 		low: 57.8891283348631,
142 | 		open: 66.51904017615065,
143 | 		time: { year: 2018, month: 10, day: 10 },
144 | 	},
145 | 	{
146 | 		close: 75.08452506029613,
147 | 		high: 75.08452506029613,
148 | 		low: 59.208194031968155,
149 | 		open: 72.14475369395771,
150 | 		time: { year: 2018, month: 10, day: 11 },
151 | 	},
152 | 	{
153 | 		close: 73.08898607472305,
154 | 		high: 73.08898607472305,
155 | 		low: 63.05632280826725,
156 | 		open: 66.93050765469924,
157 | 		time: { year: 2018, month: 10, day: 12 },
158 | 	},
159 | 	{
160 | 		close: 58.993371469509704,
161 | 		high: 73.08872095153116,
162 | 		low: 53.52204433018574,
163 | 		open: 66.12840939191403,
164 | 		time: { year: 2018, month: 10, day: 13 },
165 | 	},
166 | 	{
167 | 		time: { year: 2018, month: 10, day: 14 },
168 | 	},
169 | 	{
170 | 		time: { year: 2018, month: 10, day: 15 },
171 | 	},
172 | 	{
173 | 		close: 60.6852855399041,
174 | 		high: 69.02095441024431,
175 | 		low: 54.00939224622043,
176 | 		open: 64.81901552322648,
177 | 		time: { year: 2018, month: 10, day: 16 },
178 | 	},
179 | 	{
180 | 		close: 57.508820449565285,
181 | 		high: 63.82926565242872,
182 | 		low: 54.07370975509682,
183 | 		open: 54.07370975509682,
184 | 		time: { year: 2018, month: 10, day: 17 },
185 | 	},
186 | 	{
187 | 		close: 51.60796818909221,
188 | 		high: 64.88712939579875,
189 | 		low: 51.60796818909221,
190 | 		open: 53.489226476218434,
191 | 		time: { year: 2018, month: 10, day: 18 },
192 | 	},
193 | 	{
194 | 		close: 55.139520748382864,
195 | 		high: 59.161320710177925,
196 | 		low: 52.228139922762765,
197 | 		open: 52.228139922762765,
198 | 		time: { year: 2018, month: 10, day: 19 },
199 | 	},
200 | 	{
201 | 		close: 47.47868992247237,
202 | 		high: 58.0836625917653,
203 | 		low: 46.43213518526832,
204 | 		open: 47.59258635788406,
205 | 		time: { year: 2018, month: 10, day: 20 },
206 | 	},
207 | 	{
208 | 		time: { year: 2018, month: 10, day: 21 },
209 | 	},
210 | 	{
211 | 		time: { year: 2018, month: 10, day: 22 },
212 | 	},
213 | 	{
214 | 		close: 45.015877277800854,
215 | 		high: 51.2955426978105,
216 | 		low: 40.26534748806228,
217 | 		open: 43.90158660063875,
218 | 		time: { year: 2018, month: 10, day: 23 },
219 | 	},
220 | 	{
221 | 		close: 49.307312373439665,
222 | 		high: 49.93643636637581,
223 | 		low: 43.20705757075934,
224 | 		open: 45.672934511555795,
225 | 		time: { year: 2018, month: 10, day: 24 },
226 | 	},
227 | 	{
228 | 		close: 45.15418019295631,
229 | 		high: 48.59676744409583,
230 | 		low: 37.628047445918504,
231 | 		open: 40.33862825788268,
232 | 		time: { year: 2018, month: 10, day: 25 },
233 | 	},
234 | 	{
235 | 		close: 43.2972018283068,
236 | 		high: 43.2972018283068,
237 | 		low: 36.335943004352245,
238 | 		open: 42.605991542720965,
239 | 		time: { year: 2018, month: 10, day: 26 },
240 | 	},
241 | 	{
242 | 		close: 39.1153643552137,
243 | 		high: 44.311406627923844,
244 | 		low: 35.31457011784855,
245 | 		open: 42.00000202357808,
246 | 		time: { year: 2018, month: 10, day: 27 },
247 | 	},
248 | 	{
249 | 		time: { year: 2018, month: 10, day: 28 },
250 | 	},
251 | 	{
252 | 		time: { year: 2018, month: 10, day: 29 },
253 | 	},
254 | 	{
255 | 		close: 31.378205119641457,
256 | 		high: 37.33501102832602,
257 | 		low: 31.30137162225214,
258 | 		open: 35.651275660713694,
259 | 		time: { year: 2018, month: 10, day: 30 },
260 | 	},
261 | 	{
262 | 		close: 33.574536057730576,
263 | 		high: 37.30152570719593,
264 | 		low: 27.369689193426243,
265 | 		open: 34.330180925654936,
266 | 		time: { year: 2018, month: 10, day: 31 },
267 | 	},
268 | 	{
269 | 		close: 28.91735096504839,
270 | 		high: 32.62196350117741,
271 | 		low: 27.072564759401843,
272 | 		open: 29.398552328599372,
273 | 		time: { year: 2018, month: 11, day: 1 },
274 | 	},
275 | 	{
276 | 		close: 28.44143154172122,
277 | 		high: 31.042019861166594,
278 | 		low: 23.383320830495375,
279 | 		open: 27.275885037308072,
280 | 		time: { year: 2018, month: 11, day: 2 },
281 | 	},
282 | 	{
283 | 		close: 25.92162714418916,
284 | 		high: 30.57604443170622,
285 | 		low: 25.418671641150752,
286 | 		open: 26.775196275924657,
287 | 		time: { year: 2018, month: 11, day: 3 },
288 | 	},
289 | 	{
290 | 		time: { year: 2018, month: 11, day: 4 },
291 | 	},
292 | 	{
293 | 		time: { year: 2018, month: 11, day: 5 },
294 | 	},
295 | 	{
296 | 		close: 31.103861067101136,
297 | 		high: 31.103861067101136,
298 | 		low: 24.39227668420513,
299 | 		open: 28.994785427089838,
300 | 		time: { year: 2018, month: 11, day: 6 },
301 | 	},
302 | 	{
303 | 		close: 28.6308138310307,
304 | 		high: 35.430817482769164,
305 | 		low: 24.069515410358232,
306 | 		open: 27.109407394069084,
307 | 		time: { year: 2018, month: 11, day: 7 },
308 | 	},
309 | 	{
310 | 		close: 29.468889521733466,
311 | 		high: 37.54082586961352,
312 | 		low: 27.90833873315644,
313 | 		open: 33.16901271715577,
314 | 		time: { year: 2018, month: 11, day: 8 },
315 | 	},
316 | 	{
317 | 		close: 35.887823124204296,
318 | 		high: 39.21804237580939,
319 | 		low: 30.951078044055627,
320 | 		open: 30.951078044055627,
321 | 		time: { year: 2018, month: 11, day: 9 },
322 | 	},
323 | 	{
324 | 		close: 34.361137347097575,
325 | 		high: 35.27083445807796,
326 | 		low: 27.825889562160082,
327 | 		open: 34.86040182980157,
328 | 		time: { year: 2018, month: 11, day: 10 },
329 | 	},
330 | 	{
331 | 		time: { year: 2018, month: 11, day: 11 },
332 | 	},
333 | 	{
334 | 		time: { year: 2018, month: 11, day: 12 },
335 | 	},
336 | 	{
337 | 		close: 40.15038854039306,
338 | 		high: 41.50912000191902,
339 | 		low: 32.610637769394444,
340 | 		open: 41.50912000191902,
341 | 		time: { year: 2018, month: 11, day: 13 },
342 | 	},
343 | 	{
344 | 		close: 44.092601065208015,
345 | 		high: 44.092601065208015,
346 | 		low: 37.778306506100726,
347 | 		open: 38.99045898154136,
348 | 		time: { year: 2018, month: 11, day: 14 },
349 | 	},
350 | 	{
351 | 		close: 41.42426637839382,
352 | 		high: 44.72189614841937,
353 | 		low: 41.42426637839382,
354 | 		open: 44.72189614841937,
355 | 		time: { year: 2018, month: 11, day: 15 },
356 | 	},
357 | 	{
358 | 		close: 41.19513795258408,
359 | 		high: 49.08084695291049,
360 | 		low: 36.24282165100056,
361 | 		open: 44.909248500660254,
362 | 		time: { year: 2018, month: 11, day: 16 },
363 | 	},
364 | 	{
365 | 		close: 44.24935708161703,
366 | 		high: 53.028535501565486,
367 | 		low: 40.32056743060158,
368 | 		open: 46.198546801109984,
369 | 		time: { year: 2018, month: 11, day: 17 },
370 | 	},
371 | 	{
372 | 		time: { year: 2018, month: 11, day: 18 },
373 | 	},
374 | 	{
375 | 		time: { year: 2018, month: 11, day: 19 },
376 | 	},
377 | 	{
378 | 		close: 48.79128595974164,
379 | 		high: 52.45087789296739,
380 | 		low: 46.80633073487828,
381 | 		open: 52.45087789296739,
382 | 		time: { year: 2018, month: 11, day: 20 },
383 | 	},
384 | 	{
385 | 		close: 46.97300046781947,
386 | 		high: 55.80689868049132,
387 | 		low: 46.97300046781947,
388 | 		open: 55.80689868049132,
389 | 		time: { year: 2018, month: 11, day: 21 },
390 | 	},
391 | 	{
392 | 		close: 55.58129861112469,
393 | 		high: 55.58129861112469,
394 | 		low: 49.087279242343996,
395 | 		open: 53.16719476594961,
396 | 		time: { year: 2018, month: 11, day: 22 },
397 | 	},
398 | 	{
399 | 		close: 50.058979311730226,
400 | 		high: 62.55333249171461,
401 | 		low: 50.058979311730226,
402 | 		open: 52.628489607588826,
403 | 		time: { year: 2018, month: 11, day: 23 },
404 | 	},
405 | 	{
406 | 		close: 51.193155229085995,
407 | 		high: 59.08949991997865,
408 | 		low: 51.193155229085995,
409 | 		open: 55.352594157474755,
410 | 		time: { year: 2018, month: 11, day: 24 },
411 | 	},
412 | 	{
413 | 		time: { year: 2018, month: 11, day: 25 },
414 | 	},
415 | 	{
416 | 		time: { year: 2018, month: 11, day: 26 },
417 | 	},
418 | 	{
419 | 		close: 57.875350873413225,
420 | 		high: 65.59903214448208,
421 | 		low: 57.875350873413225,
422 | 		open: 62.747405667247016,
423 | 		time: { year: 2018, month: 11, day: 27 },
424 | 	},
425 | 	{
426 | 		close: 61.231150731698605,
427 | 		high: 66.3829902228434,
428 | 		low: 61.231150731698605,
429 | 		open: 65.01028486919516,
430 | 		time: { year: 2018, month: 11, day: 28 },
431 | 	},
432 | 	{
433 | 		close: 64.9698540874806,
434 | 		high: 77.09783903299783,
435 | 		low: 58.455031795628194,
436 | 		open: 58.455031795628194,
437 | 		time: { year: 2018, month: 11, day: 29 },
438 | 	},
439 | 	{
440 | 		close: 72.40978471883417,
441 | 		high: 72.40978471883417,
442 | 		low: 53.05804901549206,
443 | 		open: 65.907298021202,
444 | 		time: { year: 2018, month: 11, day: 30 },
445 | 	},
446 | 	{
447 | 		close: 74.60745731538934,
448 | 		high: 78.33742117000789,
449 | 		low: 54.42067144918077,
450 | 		open: 73.20930147914103,
451 | 		time: { year: 2018, month: 12, day: 1 },
452 | 	},
453 | 	{
454 | 		time: { year: 2018, month: 12, day: 2 },
455 | 	},
456 | 	{
457 | 		time: { year: 2018, month: 12, day: 3 },
458 | 	},
459 | 	{
460 | 		close: 68.23682161095334,
461 | 		high: 77.6723729460968,
462 | 		low: 68.23682161095334,
463 | 		open: 74.39471534484744,
464 | 		time: { year: 2018, month: 12, day: 4 },
465 | 	},
466 | 	{
467 | 		close: 67.45035792565862,
468 | 		high: 83.53728553118547,
469 | 		low: 67.45035792565862,
470 | 		open: 74.79418570077237,
471 | 		time: { year: 2018, month: 12, day: 5 },
472 | 	},
473 | 	{
474 | 		close: 79.26722967320323,
475 | 		high: 79.26722967320323,
476 | 		low: 68.40654829383521,
477 | 		open: 68.40654829383521,
478 | 		time: { year: 2018, month: 12, day: 6 },
479 | 	},
480 | 	{
481 | 		close: 74.95305464030587,
482 | 		high: 81.65884414224071,
483 | 		low: 64.08761481290135,
484 | 		open: 81.65884414224071,
485 | 		time: { year: 2018, month: 12, day: 7 },
486 | 	},
487 | 	{
488 | 		close: 86.30802154315482,
489 | 		high: 91.21953112925642,
490 | 		low: 65.46112304993535,
491 | 		open: 77.82514647663533,
492 | 		time: { year: 2018, month: 12, day: 8 },
493 | 	},
494 | 	{
495 | 		time: { year: 2018, month: 12, day: 9 },
496 | 	},
497 | 	{
498 | 		time: { year: 2018, month: 12, day: 10 },
499 | 	},
500 | 	{
501 | 		close: 79.00109311074502,
502 | 		high: 88.74271558831151,
503 | 		low: 69.00900811612337,
504 | 		open: 88.74271558831151,
505 | 		time: { year: 2018, month: 12, day: 11 },
506 | 	},
507 | 	{
508 | 		close: 80.98779620162513,
509 | 		high: 97.07429720104427,
510 | 		low: 73.76970378608283,
511 | 		open: 88.57288529720472,
512 | 		time: { year: 2018, month: 12, day: 12 },
513 | 	},
514 | 	{
515 | 		close: 87.83619759370346,
516 | 		high: 91.29759438607132,
517 | 		low: 74.00740214639268,
518 | 		open: 87.51853658661781,
519 | 		time: { year: 2018, month: 12, day: 13 },
520 | 	},
521 | 	{
522 | 		close: 87.50134898892377,
523 | 		high: 102.95635188637507,
524 | 		low: 81.0513723219724,
525 | 		open: 94.74009794290814,
526 | 		time: { year: 2018, month: 12, day: 14 },
527 | 	},
528 | 	{
529 | 		close: 92.40159548029843,
530 | 		high: 103.24363067710844,
531 | 		low: 75.44605394394573,
532 | 		open: 95.99903495559444,
533 | 		time: { year: 2018, month: 12, day: 15 },
534 | 	},
535 | 	{
536 | 		time: { year: 2018, month: 12, day: 16 },
537 | 	},
538 | 	{
539 | 		time: { year: 2018, month: 12, day: 17 },
540 | 	},
541 | 	{
542 | 		close: 96.04408990868804,
543 | 		high: 101.02158248010466,
544 | 		low: 94.38544669520195,
545 | 		open: 101.02158248010466,
546 | 		time: { year: 2018, month: 12, day: 18 },
547 | 	},
548 | 	{
549 | 		close: 97.2120815653703,
550 | 		high: 103.35830035963959,
551 | 		low: 78.72594316029567,
552 | 		open: 86.98009038330306,
553 | 		time: { year: 2018, month: 12, day: 19 },
554 | 	},
555 | 	{
556 | 		close: 105.23366706522204,
557 | 		high: 106.56174456393981,
558 | 		low: 94.6658899187065,
559 | 		open: 106.56174456393981,
560 | 		time: { year: 2018, month: 12, day: 20 },
561 | 	},
562 | 	{
563 | 		close: 89.53750874231946,
564 | 		high: 112.27917367188074,
565 | 		low: 87.13586952228918,
566 | 		open: 96.0857985693989,
567 | 		time: { year: 2018, month: 12, day: 21 },
568 | 	},
569 | 	{
570 | 		close: 88.55787263435407,
571 | 		high: 112.62138454627025,
572 | 		low: 80.42783344898223,
573 | 		open: 88.34340019789849,
574 | 		time: { year: 2018, month: 12, day: 22 },
575 | 	},
576 | 	{
577 | 		time: { year: 2018, month: 12, day: 23 },
578 | 	},
579 | 	{
580 | 		time: { year: 2018, month: 12, day: 24 },
581 | 	},
582 | 	{
583 | 		close: 93.38124264891343,
584 | 		high: 93.38124264891343,
585 | 		low: 84.5674956907938,
586 | 		open: 87.54923273867136,
587 | 		time: { year: 2018, month: 12, day: 25 },
588 | 	},
589 | 	{
590 | 		close: 87.88725775527871,
591 | 		high: 90.14253631595105,
592 | 		low: 77.28638555494503,
593 | 		open: 83.93199044032968,
594 | 		time: { year: 2018, month: 12, day: 26 },
595 | 	},
596 | 	{
597 | 		close: 71.77940077333062,
598 | 		high: 89.25710176370582,
599 | 		low: 67.74278646676306,
600 | 		open: 78.5346198695072,
601 | 		time: { year: 2018, month: 12, day: 27 },
602 | 	},
603 | 	{
604 | 		close: 72.08757207606054,
605 | 		high: 79.36518615067514,
606 | 		low: 69.18787486704672,
607 | 		open: 69.18787486704672,
608 | 		time: { year: 2018, month: 12, day: 28 },
609 | 	},
610 | 	{
611 | 		close: 73.87977927793119,
612 | 		high: 77.62891475860795,
613 | 		low: 70.42293039125319,
614 | 		open: 70.42293039125319,
615 | 		time: { year: 2018, month: 12, day: 29 },
616 | 	},
617 | 	{
618 | 		time: { year: 2018, month: 12, day: 30 },
619 | 	},
620 | 	{
621 | 		close: 71.00787215611817,
622 | 		high: 71.00787215611817,
623 | 		low: 57.29681995441558,
624 | 		open: 60.04464694823929,
625 | 		time: { year: 2018, month: 12, day: 31 },
626 | 	},
627 | 	// hide-end
628 | ]);
629 | 
630 | chart.timeScale().fitContent();
631 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/whitespace.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Whitespace data
 3 | sidebar_label: Whitespace data
 4 | description: An example of how to provide whitespace data
 5 | pagination_prev: null
 6 | pagination_next: null
 7 | keywords:
 8 |   - whitespace data
 9 | ---
10 | 
11 | This sample demonstrates the usage of "whitespace data" in Lightweight Charts™.
12 | Rather than a complete set of pricing information, these data points only
13 | provide a timestamp. This generates a gap or "whitespace" on the chart,
14 | signifying periods without trading. An example in the code is `{time: { year:
15 | 2018, month: 9, day: 24 }}`, which results in a visual break in the candlestick
16 | series.
17 | 
18 | ### API Reference
19 | 
20 | - [WhitespaceData](/docs/api/interfaces/WhitespaceData)
21 | 
22 | import UsageGuidePartial from '../_usage-guide-partial.mdx';
23 | import CodeBlock from '@theme/CodeBlock';
24 | import code from '!!raw-loader!./whitespace.js';
25 | 
26 | <CodeBlock
27 | 	replaceThemeConstants
28 | 	chart
29 | 	className="language-js"
30 | 	hideableCode
31 | 	chartOnTop
32 | 	codeUsage={<UsageGuidePartial />}
33 | >
34 | 	{code}
35 | </CodeBlock>
36 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/yield-curve-with-update-markers.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Yield Curve Chart with Update Markers
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/demos/yield-curve-with-update-markers
  4 | 
  5 | // remove-end
  6 | 
  7 | // hide-start
  8 | const curve1 = [
  9 | 	{ time: 1, value: 5.378 },
 10 | 	{ time: 2, value: 5.372 },
 11 | 	{ time: 3, value: 5.271 },
 12 | 	{ time: 6, value: 5.094 },
 13 | 	{ time: 12, value: 4.739 },
 14 | 	{ time: 24, value: 4.237 },
 15 | 	{ time: 36, value: 4.036 },
 16 | 	{ time: 60, value: 3.887 },
 17 | 	{ time: 84, value: 3.921 },
 18 | 	{ time: 120, value: 4.007 },
 19 | 	{ time: 240, value: 4.366 },
 20 | 	{ time: 360, value: 4.29 },
 21 | ];
 22 | const curve2 = [
 23 | 	{ time: 1, value: 5.381 },
 24 | 	{ time: 2, value: 5.393 },
 25 | 	{ time: 3, value: 5.425 },
 26 | 	{ time: 6, value: 5.494 },
 27 | 	{ time: 12, value: 5.377 },
 28 | 	{ time: 24, value: 4.883 },
 29 | 	{ time: 36, value: 4.554 },
 30 | 	{ time: 60, value: 4.241 },
 31 | 	{ time: 84, value: 4.172 },
 32 | 	{ time: 120, value: 4.084 },
 33 | 	{ time: 240, value: 4.365 },
 34 | 	{ time: 360, value: 4.176 },
 35 | ];
 36 | // hide-end
 37 | 
 38 | const chartOptions = {
 39 | 	autoSize: true,
 40 | 	layout: {
 41 | 		textColor: CHART_TEXT_COLOR,
 42 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
 43 | 	},
 44 | 	yieldCurve: {
 45 | 		baseResolution: 12,
 46 | 		minimumTimeRange: 10,
 47 | 		startTimeRange: 3,
 48 | 	},
 49 | 	handleScroll: false,
 50 | 	handleScale: false,
 51 | 	grid: {
 52 | 		vertLines: {
 53 | 			visible: false,
 54 | 		},
 55 | 		horzLines: {
 56 | 			visible: false,
 57 | 		},
 58 | 	},
 59 | 	timeScale: {
 60 | 		minBarSpacing: 3,
 61 | 	},
 62 | };
 63 | 
 64 | const container = document.getElementById('container');
 65 | const chart = createYieldCurveChart(container, chartOptions);
 66 | 
 67 | const series1 = chart.addSeries(LineSeries, {
 68 | 	lineType: 2,
 69 | 	color: '#26c6da',
 70 | 	pointMarkersVisible: true,
 71 | 	lineWidth: 2,
 72 | });
 73 | const priceChangeMarkers = createUpDownMarkers(series1);
 74 | priceChangeMarkers.setData(curve1);
 75 | 
 76 | const series2 = chart.addSeries(LineSeries, {
 77 | 	lineType: 2,
 78 | 	color: 'rgb(164, 89, 209)',
 79 | 	pointMarkersVisible: true,
 80 | 	lineWidth: 1,
 81 | });
 82 | series2.setData(curve2);
 83 | 
 84 | chart.timeScale().fitContent();
 85 | 
 86 | chart.timeScale().subscribeSizeChange(() => {
 87 | 	chart.timeScale().fitContent();
 88 | });
 89 | 
 90 | setInterval(() => {
 91 | 	curve1
 92 | 		.filter(() => Math.random() < 0.1)
 93 | 		.forEach(data => {
 94 | 			const shift = (Math.random() > 0.5 ? -1 : 1) * Math.random() * 0.01 * data.value;
 95 | 			priceChangeMarkers.update(
 96 | 				{
 97 | 					...data,
 98 | 					value: data.value + shift,
 99 | 				},
100 | 				true
101 | 			);
102 | 		});
103 | }, 5000);
104 | 


--------------------------------------------------------------------------------
/website/tutorials/demos/yield-curve-with-update-markers.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Yield Curve Chart with Update Markers
 3 | sidebar_label: Yield Curve with Updates
 4 | description:
 5 |   An example of a yield curve chart with real-time updates using markers
 6 | pagination_prev: null
 7 | pagination_next: null
 8 | keywords:
 9 |   - yield curve
10 |   - realtime updates
11 |   - markers
12 |   - plugins
13 | ---
14 | 
15 | This sample demonstrates how to create a yield curve chart with real-time
16 | updates using Lightweight Charts™. The chart displays two
17 | [yield curves](/docs/next/chart-types#yield-curve-chart) and utilizes the
18 | [UpDownMarkersPrimitive](/docs/next/api/functions/createUpDownMarkers) plugin
19 | to show price change markers for updates.
20 | 
21 | The chart is initialized with historical yield curve data for two series. By
22 | using the `setInterval` function, we simulate real-time updates to the first
23 | curve. These updates are applied using the `update` method provided by the
24 | UpDownMarkersPrimitive, which automatically handles the creation and display of
25 | markers for price changes.
26 | 
27 | Key features of this demo:
28 | 
29 | 1. Yield curve chart configuration with custom time range settings.
30 | 2. Two line series representing different yield curves.
31 | 3. Usage of the UpDownMarkersPrimitive plugin for displaying update markers.
32 | 4. Simulated real-time updates to demonstrate dynamic data handling.
33 | 
34 | The UpDownMarkersPrimitive is attached to the first series when created using
35 | `priceChangeMarkers = createUpDownMarkers(series1)`. We then use
36 | `priceChangeMarkers.setData(curve1)` to initialize the data and
37 | `priceChangeMarkers.update(...)` for subsequent updates. This approach allows
38 | the primitive to manage both the series data and the markers, providing a
39 | seamless way to visualize price changes.
40 | 
41 | import UsageGuidePartial from '../_usage-guide-partial.mdx';
42 | import CodeBlock from '@theme/CodeBlock';
43 | import code from '!!raw-loader!./yield-curve-with-update-markers.js';
44 | 
45 | <CodeBlock
46 | 	replaceThemeConstants
47 | 	chart
48 | 	className="language-js"
49 | 	hideableCode
50 | 	chartOnTop
51 | 	codeUsage={<UsageGuidePartial />}
52 | >
53 | 	{code}
54 | </CodeBlock>
55 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/.eslintrc.js:
--------------------------------------------------------------------------------
 1 | module.exports = {
 2 | 	globals: {
 3 | 		document: false,
 4 | 		createChart: false,
 5 | 		createChartEx: false,
 6 | 		createTextWatermark: false,
 7 | 		createImageWatermark: false,
 8 | 		createSeriesMarkers: false,
 9 | 		LineSeries: false,
10 | 		AreaSeries: false,
11 | 		BarSeries: false,
12 | 		BaselineSeries: false,
13 | 		CandlestickSeries: false,
14 | 		HistogramSeries: false,
15 | 	},
16 | };
17 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/_usage-guide-partial.mdx:
--------------------------------------------------------------------------------
 1 | <details>
 2 | <summary>How to use the code sample</summary>
 3 | 
 4 | <strong>Before you use the code sample below, you should do the following::</strong>
 5 | -  Import `createChart`. Refer to [Getting Started](/docs#creating-a-chart) for more information.
 6 | -  Add an HTML div element with the `id` of the `container`.
 7 | 
 8 | Here is an example skeleton setup: [Code Sandbox](https://codesandbox.io/s/lightweight-charts-skeleton-n67pm6).
 9 | You can paste the provided code below the `// REPLACE EVERYTHING BELOW HERE` comment.
10 | 
11 | :::tip
12 | 
13 | Some code may be hidden to improve readability. Toggle the checkbox above the code block to reveal all the code.
14 | 
15 | :::
16 | </details>
17 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/horizontal-price-scale.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Horizontal Price Scale
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/how_to/horizontal-price-scale
  4 | 
  5 | // remove-end
  6 | function markWithGreaterWeight(a, b) {
  7 | 	return a.weight > b.weight ? a : b;
  8 | }
  9 | 
 10 | // remove-line
 11 | /** @type {import('lightweight-charts').IHorzScaleBehavior} */
 12 | class HorzScaleBehaviorPrice {
 13 | 	constructor() {
 14 | 		this._options = {};
 15 | 	}
 16 | 
 17 | 	options() {
 18 | 		return this._options;
 19 | 	}
 20 | 
 21 | 	setOptions(options) {
 22 | 		this._options = options;
 23 | 	}
 24 | 
 25 | 	preprocessData(data) {}
 26 | 
 27 | 	updateFormatter(options) {
 28 | 		if (!this._options) {
 29 | 			return;
 30 | 		}
 31 | 		this._options.localization = options;
 32 | 	}
 33 | 
 34 | 	createConverterToInternalObj(data) {
 35 | 		return price => price;
 36 | 	}
 37 | 
 38 | 	key(internalItem) {
 39 | 		return internalItem;
 40 | 	}
 41 | 
 42 | 	cacheKey(internalItem) {
 43 | 		return internalItem;
 44 | 	}
 45 | 
 46 | 	convertHorzItemToInternal(item) {
 47 | 		return item;
 48 | 	}
 49 | 
 50 | 	formatHorzItem(item) {
 51 | 		return item.toFixed(this._precision());
 52 | 	}
 53 | 
 54 | 	formatTickmark(item, localizationOptions) {
 55 | 		return item.time.toFixed(this._precision());
 56 | 	}
 57 | 
 58 | 	maxTickMarkWeight(marks) {
 59 | 		return marks.reduce(markWithGreaterWeight, marks[0]).weight;
 60 | 	}
 61 | 
 62 | 	fillWeightsForPoints(sortedTimePoints, startIndex) {
 63 | 		const priceWeight = price => {
 64 | 			if (price === Math.ceil(price / 100) * 100) {
 65 | 				return 8;
 66 | 			}
 67 | 			if (price === Math.ceil(price / 50) * 50) {
 68 | 				return 7;
 69 | 			}
 70 | 			if (price === Math.ceil(price / 25) * 25) {
 71 | 				return 6;
 72 | 			}
 73 | 			if (price === Math.ceil(price / 10) * 10) {
 74 | 				return 5;
 75 | 			}
 76 | 			if (price === Math.ceil(price / 5) * 5) {
 77 | 				return 4;
 78 | 			}
 79 | 			if (price === Math.ceil(price)) {
 80 | 				return 3;
 81 | 			}
 82 | 			if (price * 2 === Math.ceil(price * 2)) {
 83 | 				return 1;
 84 | 			}
 85 | 			return 0;
 86 | 		};
 87 | 		for (let index = startIndex; index < sortedTimePoints.length; ++index) {
 88 | 			sortedTimePoints[index].timeWeight = priceWeight(
 89 | 				sortedTimePoints[index].time
 90 | 			);
 91 | 		}
 92 | 	}
 93 | 
 94 | 	_precision() {
 95 | 		return this._options.localization.precision;
 96 | 	}
 97 | }
 98 | 
 99 | const horzItemBehavior = new HorzScaleBehaviorPrice();
100 | 
101 | const chartOptions = {
102 | 	layout: {
103 | 		textColor: CHART_TEXT_COLOR,
104 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
105 | 	},
106 | 	localization: {
107 | 		precision: 2, // custom option
108 | 	},
109 | };
110 | 
111 | // remove-line
112 | /** @type {import('lightweight-charts').IChartApi} */
113 | const chart = createChartEx(
114 | 	document.getElementById('container'),
115 | 	horzItemBehavior,
116 | 	chartOptions
117 | );
118 | 
119 | const lineSeries = chart.addSeries(LineSeries, { color: LINE_LINE_COLOR });
120 | 
121 | const data = [];
122 | for (let i = 0; i < 5000; i++) {
123 | 	data.push({
124 | 		time: i * 0.25,
125 | 		value: Math.sin(i / 100) + i / 500,
126 | 	});
127 | }
128 | 
129 | lineSeries.setData(data);
130 | 
131 | chart.timeScale().fitContent();
132 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/horizontal-price-scale.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | title: Custom horizontal scale
  3 | sidebar_label: Custom horizontal scale
  4 | description:
  5 |   Customizing horizontal scale behavior with IHorzScaleBehavior interface.
  6 | pagination_prev: null
  7 | pagination_next: null
  8 | keywords:
  9 |   - price
 10 |   - scale
 11 |   - horizontal
 12 |   - options
 13 | ---
 14 | 
 15 | The `IHorzScaleBehavior` interface allows you to customize the behavior of the
 16 | horizontal scale. By default, this scale uses [time](/docs/api/type-aliases/Time) values, but
 17 | you can override it to use any other type of horizontal scale items, such as
 18 | price values. The most typical use case is the creation of Options charts.
 19 | 
 20 | This guide will explain the
 21 | [`IHorzScaleBehavior`](/docs/api/interfaces/IHorzScaleBehavior) interface and
 22 | how to implement it to create a horizontal scale using price values with
 23 | customizable precision.
 24 | 
 25 | ## Understanding the IHorzScaleBehavior interface
 26 | 
 27 | The `IHorzScaleBehavior` interface consists of several methods that you need to
 28 | implement to customize the horizontal scale behavior. Here's a breakdown of each
 29 | method and its purpose:
 30 | 
 31 | ### options
 32 | 
 33 | ```
 34 | public options(): ChartOptionsImpl<HorzScaleItem>
 35 | ```
 36 | 
 37 | This method returns the chart's current configuration options. These options
 38 | include various settings that control the appearance and behavior of the chart.
 39 | Implement this method to return the current options of your horizontal scale
 40 | behavior.
 41 | 
 42 | ### setOptions
 43 | 
 44 | ```
 45 | public setOptions(options: ChartOptionsImpl<HorzScaleItem>): void
 46 | ```
 47 | 
 48 | This method allows you to set or update the chart's configuration options. The
 49 | provided `options` parameter will contain the settings you want to apply. Use
 50 | this method to update the options when necessary.
 51 | 
 52 | ### preprocessData
 53 | 
 54 | ```
 55 | public preprocessData(data: DataItem<HorzScaleItem> | DataItem<HorzScaleItem>[]): void
 56 | ```
 57 | 
 58 | This method processes the series data before it is used by the chart. It
 59 | receives an array of data items or a single data item. You can implement this
 60 | method to preprocess or modify data as needed before it is rendered.
 61 | 
 62 | ### updateFormatter
 63 | 
 64 | ```
 65 | public updateFormatter(options: LocalizationOptions<HorzScaleItem>): void
 66 | ```
 67 | 
 68 | This method updates the formatter used for displaying the horizontal scale items
 69 | based on localization options. Implement this to set custom formatting settings,
 70 | such as locale-specific date or number formats.
 71 | 
 72 | ### createConverterToInternalObj
 73 | 
 74 | ```
 75 | public createConverterToInternalObj(data: SeriesDataItemTypeMap<HorzScaleItem>[SeriesType][]): HorzScaleItemConverterToInternalObj<HorzScaleItem>
 76 | ```
 77 | 
 78 | This method creates and returns a function that converts series data items into
 79 | internal horizontal scale items. Implementing this method is essential for
 80 | transforming your custom data into the format required by the chart's internal
 81 | mechanisms.
 82 | 
 83 | ### key
 84 | 
 85 | ```
 86 | public key(internalItem: InternalHorzScaleItem | HorzScaleItem): InternalHorzScaleItemKey
 87 | ```
 88 | 
 89 | This method returns a unique key for a given horizontal scale item. It's used
 90 | internally by the chart to identify and manage items uniquely. Implement this
 91 | method to provide a unique identifier for each item.
 92 | 
 93 | ### cacheKey
 94 | 
 95 | ```
 96 | public cacheKey(internalItem: InternalHorzScaleItem): number
 97 | ```
 98 | 
 99 | This method returns a cache key for a given internal horizontal scale item. This
100 | key helps the chart to cache and retrieve items efficiently. Implement this
101 | method to return a numeric key for caching purposes.
102 | 
103 | ### convertHorzItemToInternal
104 | 
105 | ```
106 | public convertHorzItemToInternal(item: HorzScaleItem): InternalHorzScaleItem
107 | ```
108 | 
109 | This method converts a horizontal scale item into an internal item that the
110 | chart can use. Implementing this method ensures that your custom data type is
111 | correctly transformed for internal use.
112 | 
113 | ### formatHorzItem
114 | 
115 | ```
116 | public formatHorzItem(item: InternalHorzScaleItem): string
117 | ```
118 | 
119 | This method formats a horizontal scale item into a display string. The returned
120 | string will be used for displaying the item on the chart. Implement this method
121 | to format your items in the desired way (e.g., with a specific number of decimal
122 | places).
123 | 
124 | ### formatTickmark
125 | 
126 | ```
127 | public formatTickmark(item: TickMark, localizationOptions: LocalizationOptions<HorzScaleItem>): string
128 | ```
129 | 
130 | This method formats a horizontal scale tick mark into a display string. The tick
131 | mark represents significant points on the horizontal scale. Implement this
132 | method to customize how tick marks are displayed.
133 | 
134 | ### maxTickMarkWeight
135 | 
136 | ```
137 | public maxTickMarkWeight(marks: TimeMark[]): TickMarkWeightValue
138 | ```
139 | 
140 | This method determines the maximum weight for a set of tick marks, which
141 | influences their display prominence. Implement this method to specify the weight
142 | of the most significant tick mark.
143 | 
144 | ### fillWeightsForPoints
145 | 
146 | ```
147 | public fillWeightsForPoints(sortedTimePoints: readonly Mutable<TimeScalePoint>[], startIndex: number): void
148 | ```
149 | 
150 | This method assigns weights to the sorted time points. These weights influence
151 | the tick marks' visual prominence. Implement this method to provide a weighting
152 | system for your horizontal scale items.
153 | 
154 | ## Example
155 | 
156 | Below is an example implementation of a custom horizontal scale behavior using
157 | price values. This example also includes customizable precision for formatting
158 | price values.
159 | 
160 | ### Implement price-based horizontal scale
161 | 
162 | 1. **Define the custom localization options interface**
163 | 
164 | Extend the [`LocalizationOptions`](/docs/api/interfaces/LocalizationOptions)
165 | interface to include a `precision` property.
166 | 
167 | ```ts
168 | export interface CustomLocalizationOptions
169 |     extends LocalizationOptions<HorzScalePriceItem> {
170 |     precision: number;
171 | }
172 | ```
173 | 
174 | 2. **Define the type alias**
175 | 
176 | Define a type alias for the horizontal scale item representing price values.
177 | 
178 | ```ts
179 | export type HorzScalePriceItem = number;
180 | ```
181 | 
182 | 3. **Implement the custom horizontal scale behavior class**
183 | 
184 | The `HorzScaleBehaviorPrice` class implements the `IHorzScaleBehavior`
185 | interface, with additional logic to handle the precision provided in the custom
186 | localization options.
187 | 
188 | ```ts
189 | function markWithGreaterWeight(a: TimeMark, b: TimeMark): TimeMark {
190 |     return a.weight > b.weight ? a : b;
191 | }
192 | 
193 | export class HorzScaleBehaviorPrice implements IHorzScaleBehavior<HorzScalePriceItem> {
194 |     private _options!: ChartOptionsImpl<HorzScalePriceItem>;
195 | 
196 |     public options(): ChartOptionsImpl<HorzScalePriceItem> {
197 |         return this._options;
198 |     }
199 | 
200 |     public setOptions(options: ChartOptionsImpl<HorzScalePriceItem>): void {
201 |         this._options = options;
202 |     }
203 | 
204 |     public preprocessData(
205 |         data: DataItem<HorzScalePriceItem> | DataItem<HorzScalePriceItem>[]
206 |     ): void {
207 |         // un-needed in this example because we do not require any additional
208 |         // data processing for this scale.
209 |         // The method is still required to be implemented in the class.
210 |     }
211 | 
212 |     public updateFormatter(options: CustomLocalizationOptions): void {
213 |         if (!this._options) {
214 |             return;
215 |         }
216 |         this._options.localization = options;
217 |     }
218 | 
219 |     public createConverterToInternalObj(
220 |         data: SeriesDataItemTypeMap<HorzScalePriceItem>[SeriesType][]
221 |     ): HorzScaleItemConverterToInternalObj<HorzScalePriceItem> {
222 |         return (price: number) => price as unknown as InternalHorzScaleItem;
223 |     }
224 | 
225 |     public key(
226 |         internalItem: InternalHorzScaleItem | HorzScalePriceItem
227 |     ): InternalHorzScaleItemKey {
228 |         return internalItem as InternalHorzScaleItemKey;
229 |     }
230 | 
231 |     public cacheKey(internalItem: InternalHorzScaleItem): number {
232 |         return internalItem as unknown as number;
233 |     }
234 | 
235 |     public convertHorzItemToInternal(
236 |         item: HorzScalePriceItem
237 |     ): InternalHorzScaleItem {
238 |         return item as unknown as InternalHorzScaleItem;
239 |     }
240 | 
241 |     public formatHorzItem(item: InternalHorzScaleItem): string {
242 |         return (item as unknown as number).toFixed(this._precision());
243 |     }
244 | 
245 |     public formatTickmark(
246 |         item: TickMark,
247 |         localizationOptions: LocalizationOptions<HorzScalePriceItem>
248 |     ): string {
249 |         return (item.time as unknown as number).toFixed(this._precision());
250 |     }
251 | 
252 |     public maxTickMarkWeight(marks: TimeMark[]): TickMarkWeightValue {
253 |         return marks.reduce(markWithGreaterWeight, marks[0]).weight;
254 |     }
255 | 
256 |     public fillWeightsForPoints(
257 |         sortedTimePoints: readonly Mutable<TimeScalePoint>[],
258 |         startIndex: number
259 |     ): void {
260 |         const priceWeight = (price: number) => {
261 |             if (price === Math.ceil(price / 100) * 100) {
262 |                 return 8;
263 |             }
264 |             if (price === Math.ceil(price / 50) * 50) {
265 |                 return 7;
266 |             }
267 |             if (price === Math.ceil(price / 25) * 25) {
268 |                 return 6;
269 |             }
270 |             if (price === Math.ceil(price / 10) * 10) {
271 |                 return 5;
272 |             }
273 |             if (price === Math.ceil(price / 5) * 5) {
274 |                 return 4;
275 |             }
276 |             if (price === Math.ceil(price)) {
277 |                 return 3;
278 |             }
279 |             if (price * 2 === Math.ceil(price * 2)) {
280 |                 return 1;
281 |             }
282 |             return 0;
283 |         };
284 |         for (let index = startIndex; index < sortedTimePoints.length; ++index) {
285 |             sortedTimePoints[index].timeWeight = priceWeight(
286 |                 sortedTimePoints[index].time as unknown as number
287 |             );
288 |         }
289 |     }
290 | 
291 |     private _precision(): number {
292 |         return (this._options.localization as CustomLocalizationOptions).precision;
293 |     }
294 | }
295 | ```
296 | 
297 | This class provides additional precision control through localization options,
298 | allowing formatted price values to use a specific number of decimal places.
299 | 
300 | ### Customize horizontal scale behavior
301 | 
302 | To use the custom horizontal scale behavior, instantiate the
303 | `HorzScaleBehaviorPrice` class and pass it to
304 | [`createChartEx`](/docs/api/functions/createChartEx).
305 | 
306 | You can pass the custom option for `precision` within the `localization`
307 | property of the chart options.
308 | 
309 | ```js
310 | const horzItemBehavior = new HorzScaleBehaviorPrice();
311 | const chart = LightweightCharts.createChartEx(container, horzItemBehavior, {
312 |     localization: {
313 |         precision: 2, // custom option
314 |     },
315 | });
316 | const s1 = chart.addSeries(LightweightCharts.LineSeries);
317 | const data = [];
318 | for (let i = 0; i < 5000; i++) {
319 |     data.push({
320 |         time: i * 0.25,
321 |         value: Math.sin(i / 100),
322 |     });
323 | }
324 | s1.setData(data);
325 | ```
326 | 
327 | ### Conclusion
328 | 
329 | The `IHorzScaleBehavior` interface provides a powerful way to customize the
330 | horizontal scale behavior in Lightweight Charts™. By implementing this
331 | interface, you can define how the horizontal scale should interpret and display
332 | custom data types, such as price values. The provided example demonstrates how
333 | to implement a horizontal scale with customizable precision, allowing for
334 | tailored display formats to fit your specific requirements.
335 | 
336 | ### Full example
337 | 
338 | import UsageGuidePartial from '../_usage-guide-partial.mdx';
339 | import CodeBlock from '@theme/CodeBlock';
340 | import code from '!!raw-loader!./horizontal-price-scale.js';
341 | 
342 | <CodeBlock
343 |     replaceThemeConstants
344 |     chart
345 |     className="language-js"
346 |     chartOnTop
347 |     codeUsage={<UsageGuidePartial />}
348 | >
349 |     {code}
350 | </CodeBlock>
351 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/inverted-price-scale.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Inverted Price Scale
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/how_to/inverted-price-scale
  4 | 
  5 | // remove-end
  6 | const chartOptions = {
  7 | 	layout: {
  8 | 		textColor: CHART_TEXT_COLOR,
  9 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
 10 | 	},
 11 | };
 12 | // remove-line
 13 | /** @type {import('lightweight-charts').IChartApi} */
 14 | const chart = createChart(document.getElementById('container'), chartOptions);
 15 | 
 16 | chart.applyOptions({
 17 | 	rightPriceScale: {
 18 | 		scaleMargins: {
 19 | 			top: 0.1,
 20 | 			bottom: 0.1,
 21 | 		},
 22 | 		// highlight-start
 23 | 		invertScale: true,
 24 | 		// highlight-end
 25 | 	},
 26 | });
 27 | 
 28 | const lineSeries = chart.addSeries(LineSeries, { color: LINE_LINE_COLOR });
 29 | 
 30 | const data = [
 31 | 	{ time: '2016-07-18', value: 661.47 },
 32 | 	// hide-start
 33 | 	{ time: '2016-07-25', value: 623.83 },
 34 | 	{ time: '2016-08-01', value: 592.47 },
 35 | 	{ time: '2016-08-08', value: 568.76 },
 36 | 	{ time: '2016-08-15', value: 577.55 },
 37 | 	{ time: '2016-08-22', value: 573.20 },
 38 | 	{ time: '2016-08-29', value: 603.72 },
 39 | 	{ time: '2016-09-05', value: 606.32 },
 40 | 	{ time: '2016-09-12', value: 608.00 },
 41 | 	{ time: '2016-09-19', value: 598.98 },
 42 | 	{ time: '2016-09-26', value: 608.60 },
 43 | 	{ time: '2016-10-03', value: 613.06 },
 44 | 	{ time: '2016-10-10', value: 638.97 },
 45 | 	{ time: '2016-10-17', value: 648.74 },
 46 | 	{ time: '2016-10-24', value: 697.23 },
 47 | 	{ time: '2016-10-31', value: 709.93 },
 48 | 	{ time: '2016-11-07', value: 700.38 },
 49 | 	{ time: '2016-11-14', value: 727.09 },
 50 | 	{ time: '2016-11-21', value: 727.32 },
 51 | 	{ time: '2016-11-28', value: 762.00 },
 52 | 	{ time: '2016-12-05', value: 768.97 },
 53 | 	{ time: '2016-12-12', value: 788.67 },
 54 | 	{ time: '2016-12-19', value: 890.67 },
 55 | 	{ time: '2016-12-26', value: 997.75 },
 56 | 	{ time: '2017-01-02', value: 909.75 },
 57 | 	{ time: '2017-01-09', value: 821.86 },
 58 | 	{ time: '2017-01-16', value: 923.76 },
 59 | 	{ time: '2017-01-23', value: 912.01 },
 60 | 	{ time: '2017-01-30', value: 1011.07 },
 61 | 	{ time: '2017-02-06', value: 1000.73 },
 62 | 	{ time: '2017-02-13', value: 1051.80 },
 63 | 	{ time: '2017-02-20', value: 1179.05 },
 64 | 	{ time: '2017-02-27', value: 1273.00 },
 65 | 	{ time: '2017-03-06', value: 1226.62 },
 66 | 	{ time: '2017-03-13', value: 1017.97 },
 67 | 	{ time: '2017-03-20', value: 960.00 },
 68 | 	{ time: '2017-03-27', value: 1078.01 },
 69 | 	{ time: '2017-04-03', value: 1206.20 },
 70 | 	{ time: '2017-04-10', value: 1162.31 },
 71 | 	{ time: '2017-04-17', value: 1241.99 },
 72 | 	{ time: '2017-04-24', value: 1350.21 },
 73 | 	{ time: '2017-05-01', value: 1554.01 },
 74 | 	{ time: '2017-05-08', value: 1784.00 },
 75 | 	{ time: '2017-05-15', value: 2017.55 },
 76 | 	{ time: '2017-05-22', value: 2178.81 },
 77 | 	{ time: '2017-05-29', value: 2530.27 },
 78 | 	{ time: '2017-06-05', value: 2954.22 },
 79 | 	{ time: '2017-06-12', value: 2516.98 },
 80 | 	{ time: '2017-06-19', value: 2502.03 },
 81 | 	{ time: '2017-06-26', value: 2504.37 },
 82 | 	{ time: '2017-07-03', value: 2502.28 },
 83 | 	{ time: '2017-07-10', value: 1917.63 },
 84 | 	{ time: '2017-07-17', value: 2749.02 },
 85 | 	{ time: '2017-07-24', value: 2742.37 },
 86 | 	{ time: '2017-07-31', value: 3222.75 },
 87 | 	{ time: '2017-08-07', value: 4053.87 },
 88 | 	{ time: '2017-08-14', value: 4058.68 },
 89 | 	{ time: '2017-08-21', value: 4337.68 },
 90 | 	{ time: '2017-08-28', value: 4606.26 },
 91 | 	{ time: '2017-09-04', value: 4226.22 },
 92 | 	{ time: '2017-09-11', value: 3662.99 },
 93 | 	{ time: '2017-09-18', value: 3664.22 },
 94 | 	{ time: '2017-09-25', value: 4377.22 },
 95 | 	{ time: '2017-10-02', value: 4597.98 },
 96 | 	{ time: '2017-10-09', value: 5679.70 },
 97 | 	{ time: '2017-10-16', value: 5969.00 },
 98 | 	{ time: '2017-10-23', value: 6137.37 },
 99 | 	{ time: '2017-10-30', value: 7372.72 },
100 | 	{ time: '2017-11-06', value: 5870.37 },
101 | 	{ time: '2017-11-13', value: 8016.58 },
102 | 	{ time: '2017-11-20', value: 9271.06 },
103 | 	{ time: '2017-11-27', value: 11250.00 },
104 | 	{ time: '2017-12-04', value: 14691.00 },
105 | 	{ time: '2017-12-11', value: 18953.00 },
106 | 	{ time: '2017-12-18', value: 14157.87 },
107 | 	{ time: '2017-12-25', value: 13880.00 },
108 | 	{ time: '2018-01-01', value: 16124.02 },
109 | 	{ time: '2018-01-08', value: 13647.99 },
110 | 	{ time: '2018-01-15', value: 11558.87 },
111 | 	{ time: '2018-01-22', value: 11685.58 },
112 | 	{ time: '2018-01-29', value: 8191.00 },
113 | 	{ time: '2018-02-05', value: 8067.00 },
114 | 	{ time: '2018-02-12', value: 10421.06 },
115 | 	{ time: '2018-02-19', value: 9590.04 },
116 | 	{ time: '2018-02-26', value: 11463.27 },
117 | 	{ time: '2018-03-05', value: 9535.04 },
118 | 	{ time: '2018-03-12', value: 8188.24 },
119 | 	{ time: '2018-03-19', value: 8453.90 },
120 | 	{ time: '2018-03-26', value: 6813.52 },
121 | 	{ time: '2018-04-02', value: 7027.26 },
122 | 	{ time: '2018-04-09', value: 8354.22 },
123 | 	{ time: '2018-04-16', value: 8789.96 },
124 | 	{ time: '2018-04-23', value: 9393.99 },
125 | 	{ time: '2018-04-30', value: 9623.54 },
126 | 	{ time: '2018-05-07', value: 8696.58 },
127 | 	{ time: '2018-05-14', value: 8518.48 },
128 | 	{ time: '2018-05-21', value: 7347.39 },
129 | 	{ time: '2018-05-28', value: 7703.67 },
130 | 	{ time: '2018-06-04', value: 6781.17 },
131 | 	{ time: '2018-06-11', value: 6453.41 },
132 | 	{ time: '2018-06-18', value: 6153.40 },
133 | 	{ time: '2018-06-25', value: 6349.99 },
134 | 	{ time: '2018-07-02', value: 6706.60 },
135 | 	{ time: '2018-07-09', value: 6349.30 },
136 | 	{ time: '2018-07-16', value: 7396.60 },
137 | 	{ time: '2018-07-23', value: 8216.74 },
138 | 	{ time: '2018-07-30', value: 7032.61 },
139 | 	{ time: '2018-08-06', value: 6310.82 },
140 | 	{ time: '2018-08-13', value: 6481.99 },
141 | 	{ time: '2018-08-20', value: 6700.46 },
142 | 	{ time: '2018-08-27', value: 7290.31 },
143 | 	{ time: '2018-09-03', value: 6236.04 },
144 | 	{ time: '2018-09-10', value: 6499.98 },
145 | 	{ time: '2018-09-17', value: 6702.22 },
146 | 	{ time: '2018-09-24', value: 6597.81 },
147 | 	{ time: '2018-10-01', value: 6577.63 },
148 | 	{ time: '2018-10-08', value: 6183.00 },
149 | 	{ time: '2018-10-15', value: 6413.38 },
150 | 	{ time: '2018-10-22', value: 6405.57 },
151 | 	{ time: '2018-10-29', value: 6421.76 },
152 | 	{ time: '2018-11-05', value: 6357.54 },
153 | 	{ time: '2018-11-12', value: 5559.26 },
154 | 	{ time: '2018-11-19', value: 3938.89 },
155 | 	{ time: '2018-11-26', value: 4102.05 },
156 | 	{ time: '2018-12-03', value: 3529.75 },
157 | 	{ time: '2018-12-10', value: 3193.78 },
158 | 	{ time: '2018-12-17', value: 3943.83 },
159 | 	{ time: '2018-12-24', value: 3835.79 },
160 | 	{ time: '2018-12-31', value: 4040.71 },
161 | 	{ time: '2019-01-07', value: 3515.95 },
162 | 	{ time: '2019-01-14', value: 3536.72 },
163 | 	{ time: '2019-01-21', value: 3533.23 },
164 | 	{ time: '2019-01-28', value: 3414.82 },
165 | 	{ time: '2019-02-04', value: 3650.37 },
166 | 	{ time: '2019-02-11', value: 3625.60 },
167 | 	{ time: '2019-02-18', value: 3730.68 },
168 | 	{ time: '2019-02-25', value: 3789.52 },
169 | 	{ time: '2019-03-04', value: 3897.92 },
170 | 	{ time: '2019-03-11', value: 3965.50 },
171 | 	{ time: '2019-03-18', value: 3969.99 },
172 | 	{ time: '2019-03-25', value: 4096.08 },
173 | 	{ time: '2019-04-01', value: 5190.85 },
174 | 	{ time: '2019-04-08', value: 5162.72 },
175 | 	{ time: '2019-04-15', value: 5295.65 },
176 | 	{ time: '2019-04-22', value: 5160.98 },
177 | 	{ time: '2019-04-29', value: 5709.32 },
178 | 	{ time: '2019-05-06', value: 6974.35 },
179 | 	{ time: '2019-05-13', value: 8200.00 },
180 | 	{ time: '2019-05-20', value: 8733.26 },
181 | 	{ time: '2019-05-27', value: 8702.43 },
182 | 	// hide-end
183 | ];
184 | 
185 | lineSeries.setData(data);
186 | 
187 | chart.timeScale().fitContent();
188 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/inverted-price-scale.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Inverted Price Scale
 3 | sidebar_label: Inverted Price Scale
 4 | description: How to invert a price scale.
 5 | pagination_prev: null
 6 | pagination_next: null
 7 | keywords:
 8 |   - price scale
 9 |   - Inverted
10 |   - example
11 | ---
12 | 
13 | This example shows how to invert a price scale. Usually, the price scale will
14 | map the range of numbers from small to large along the vertical axis from bottom
15 | to top. Inverting the price scale will change this such that the values map from
16 | top to bottom.
17 | 
18 | ## How to
19 | 
20 | Set the [`invertScale`](/docs/api/interfaces/PriceScaleOptions#invertscale) property
21 | on the [priceScale options](/docs/api/interfaces/PriceScaleOptions) to `true`.
22 | 
23 | ```js
24 | chart.applyOptions({
25 |     rightPriceScale: {
26 |         invertScale: true,
27 |     },
28 | });
29 | 
30 | // or (for a specific price scale)
31 | const priceScale = chart.priceScale();
32 | priceScale.applyOptions({
33 |     invertScale: true,
34 | });
35 | ```
36 | 
37 | You can see a full [working example](#full-example) below.
38 | 
39 | ## Resources
40 | - [invertScale](/docs/api/interfaces/PriceScaleOptions#invertscale)
41 | - [Price Scales](/docs/price-scale) - General introduction to Price Scales.
42 | 
43 | ## Full example
44 | 
45 | import UsageGuidePartial from "../_usage-guide-partial.mdx";
46 | import CodeBlock from "@theme/CodeBlock";
47 | import code from "!!raw-loader!./inverted-price-scale.js";
48 | 
49 | <CodeBlock replaceThemeConstants chart className="language-js" hideableCode chartOnTop codeUsage={<UsageGuidePartial />}>
50 | 	{code}
51 | </CodeBlock>
52 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/legend-3line.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Legend 3 Lines
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/how_to/legends
  4 | 
  5 | // remove-end
  6 | const chartOptions = {
  7 | 	layout: {
  8 | 		textColor: CHART_TEXT_COLOR,
  9 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
 10 | 	},
 11 | };
 12 | // remove-line
 13 | /** @type {import('lightweight-charts').IChartApi} */
 14 | const chart = createChart(document.getElementById('container'), chartOptions);
 15 | 
 16 | chart.applyOptions({
 17 | 	rightPriceScale: {
 18 | 		scaleMargins: {
 19 | 			top: 0.4, // leave some space for the legend
 20 | 			bottom: 0.15,
 21 | 		},
 22 | 	},
 23 | 	crosshair: {
 24 | 		// hide the horizontal crosshair line
 25 | 		horzLine: {
 26 | 			visible: false,
 27 | 			labelVisible: false,
 28 | 		},
 29 | 	},
 30 | 	// hide the grid lines
 31 | 	grid: {
 32 | 		vertLines: {
 33 | 			visible: false,
 34 | 		},
 35 | 		horzLines: {
 36 | 			visible: false,
 37 | 		},
 38 | 	},
 39 | });
 40 | 
 41 | const areaSeries = chart.addSeries(AreaSeries, {
 42 | 	topColor: AREA_TOP_COLOR,
 43 | 	bottomColor: AREA_BOTTOM_COLOR,
 44 | 	lineColor: LINE_LINE_COLOR,
 45 | 	lineWidth: 2,
 46 | 	crossHairMarkerVisible: false,
 47 | });
 48 | 
 49 | const data = [
 50 | 	{ time: '2018-10-19', value: 26.19 },
 51 | 	// hide-start
 52 | 	{ time: '2018-10-22', value: 25.87 },
 53 | 	{ time: '2018-10-23', value: 25.83 },
 54 | 	{ time: '2018-10-24', value: 25.78 },
 55 | 	{ time: '2018-10-25', value: 25.82 },
 56 | 	{ time: '2018-10-26', value: 25.81 },
 57 | 	{ time: '2018-10-29', value: 25.82 },
 58 | 	{ time: '2018-10-30', value: 25.71 },
 59 | 	{ time: '2018-10-31', value: 25.82 },
 60 | 	{ time: '2018-11-01', value: 25.72 },
 61 | 	{ time: '2018-11-02', value: 25.74 },
 62 | 	{ time: '2018-11-05', value: 25.81 },
 63 | 	{ time: '2018-11-06', value: 25.75 },
 64 | 	{ time: '2018-11-07', value: 25.73 },
 65 | 	{ time: '2018-11-08', value: 25.75 },
 66 | 	{ time: '2018-11-09', value: 25.75 },
 67 | 	{ time: '2018-11-12', value: 25.76 },
 68 | 	{ time: '2018-11-13', value: 25.8 },
 69 | 	{ time: '2018-11-14', value: 25.77 },
 70 | 	{ time: '2018-11-15', value: 25.75 },
 71 | 	{ time: '2018-11-16', value: 25.75 },
 72 | 	{ time: '2018-11-19', value: 25.75 },
 73 | 	{ time: '2018-11-20', value: 25.72 },
 74 | 	{ time: '2018-11-21', value: 25.78 },
 75 | 	{ time: '2018-11-23', value: 25.72 },
 76 | 	{ time: '2018-11-26', value: 25.78 },
 77 | 	{ time: '2018-11-27', value: 25.85 },
 78 | 	{ time: '2018-11-28', value: 25.85 },
 79 | 	{ time: '2018-11-29', value: 25.55 },
 80 | 	{ time: '2018-11-30', value: 25.41 },
 81 | 	{ time: '2018-12-03', value: 25.41 },
 82 | 	{ time: '2018-12-04', value: 25.42 },
 83 | 	{ time: '2018-12-06', value: 25.33 },
 84 | 	{ time: '2018-12-07', value: 25.39 },
 85 | 	{ time: '2018-12-10', value: 25.32 },
 86 | 	{ time: '2018-12-11', value: 25.48 },
 87 | 	{ time: '2018-12-12', value: 25.39 },
 88 | 	{ time: '2018-12-13', value: 25.45 },
 89 | 	{ time: '2018-12-14', value: 25.52 },
 90 | 	{ time: '2018-12-17', value: 25.38 },
 91 | 	{ time: '2018-12-18', value: 25.36 },
 92 | 	{ time: '2018-12-19', value: 25.65 },
 93 | 	{ time: '2018-12-20', value: 25.7 },
 94 | 	{ time: '2018-12-21', value: 25.66 },
 95 | 	{ time: '2018-12-24', value: 25.66 },
 96 | 	{ time: '2018-12-26', value: 25.65 },
 97 | 	{ time: '2018-12-27', value: 25.66 },
 98 | 	{ time: '2018-12-28', value: 25.68 },
 99 | 	{ time: '2018-12-31', value: 25.77 },
100 | 	{ time: '2019-01-02', value: 25.72 },
101 | 	{ time: '2019-01-03', value: 25.69 },
102 | 	{ time: '2019-01-04', value: 25.71 },
103 | 	{ time: '2019-01-07', value: 25.72 },
104 | 	{ time: '2019-01-08', value: 25.72 },
105 | 	{ time: '2019-01-09', value: 25.66 },
106 | 	{ time: '2019-01-10', value: 25.85 },
107 | 	{ time: '2019-01-11', value: 25.92 },
108 | 	{ time: '2019-01-14', value: 25.94 },
109 | 	{ time: '2019-01-15', value: 25.95 },
110 | 	{ time: '2019-01-16', value: 26.0 },
111 | 	{ time: '2019-01-17', value: 25.99 },
112 | 	{ time: '2019-01-18', value: 25.6 },
113 | 	{ time: '2019-01-22', value: 25.81 },
114 | 	{ time: '2019-01-23', value: 25.7 },
115 | 	{ time: '2019-01-24', value: 25.74 },
116 | 	{ time: '2019-01-25', value: 25.8 },
117 | 	{ time: '2019-01-28', value: 25.83 },
118 | 	{ time: '2019-01-29', value: 25.7 },
119 | 	{ time: '2019-01-30', value: 25.78 },
120 | 	{ time: '2019-01-31', value: 25.35 },
121 | 	{ time: '2019-02-01', value: 25.6 },
122 | 	{ time: '2019-02-04', value: 25.65 },
123 | 	{ time: '2019-02-05', value: 25.73 },
124 | 	{ time: '2019-02-06', value: 25.71 },
125 | 	{ time: '2019-02-07', value: 25.71 },
126 | 	{ time: '2019-02-08', value: 25.72 },
127 | 	{ time: '2019-02-11', value: 25.76 },
128 | 	{ time: '2019-02-12', value: 25.84 },
129 | 	{ time: '2019-02-13', value: 25.85 },
130 | 	{ time: '2019-02-14', value: 25.87 },
131 | 	{ time: '2019-02-15', value: 25.89 },
132 | 	{ time: '2019-02-19', value: 25.9 },
133 | 	{ time: '2019-02-20', value: 25.92 },
134 | 	{ time: '2019-02-21', value: 25.96 },
135 | 	{ time: '2019-02-22', value: 26.0 },
136 | 	{ time: '2019-02-25', value: 25.93 },
137 | 	{ time: '2019-02-26', value: 25.92 },
138 | 	{ time: '2019-02-27', value: 25.67 },
139 | 	{ time: '2019-02-28', value: 25.79 },
140 | 	{ time: '2019-03-01', value: 25.86 },
141 | 	{ time: '2019-03-04', value: 25.94 },
142 | 	{ time: '2019-03-05', value: 26.02 },
143 | 	{ time: '2019-03-06', value: 25.95 },
144 | 	{ time: '2019-03-07', value: 25.89 },
145 | 	{ time: '2019-03-08', value: 25.94 },
146 | 	{ time: '2019-03-11', value: 25.91 },
147 | 	{ time: '2019-03-12', value: 25.92 },
148 | 	{ time: '2019-03-13', value: 26.0 },
149 | 	{ time: '2019-03-14', value: 26.05 },
150 | 	{ time: '2019-03-15', value: 26.11 },
151 | 	{ time: '2019-03-18', value: 26.1 },
152 | 	{ time: '2019-03-19', value: 25.98 },
153 | 	{ time: '2019-03-20', value: 26.11 },
154 | 	{ time: '2019-03-21', value: 26.12 },
155 | 	{ time: '2019-03-22', value: 25.88 },
156 | 	{ time: '2019-03-25', value: 25.85 },
157 | 	{ time: '2019-03-26', value: 25.72 },
158 | 	{ time: '2019-03-27', value: 25.73 },
159 | 	{ time: '2019-03-28', value: 25.8 },
160 | 	{ time: '2019-03-29', value: 25.77 },
161 | 	{ time: '2019-04-01', value: 26.06 },
162 | 	{ time: '2019-04-02', value: 25.93 },
163 | 	{ time: '2019-04-03', value: 25.95 },
164 | 	{ time: '2019-04-04', value: 26.06 },
165 | 	{ time: '2019-04-05', value: 26.16 },
166 | 	{ time: '2019-04-08', value: 26.12 },
167 | 	{ time: '2019-04-09', value: 26.07 },
168 | 	{ time: '2019-04-10', value: 26.13 },
169 | 	{ time: '2019-04-11', value: 26.04 },
170 | 	{ time: '2019-04-12', value: 26.04 },
171 | 	{ time: '2019-04-15', value: 26.05 },
172 | 	{ time: '2019-04-16', value: 26.01 },
173 | 	{ time: '2019-04-17', value: 26.09 },
174 | 	{ time: '2019-04-18', value: 26.0 },
175 | 	{ time: '2019-04-22', value: 26.0 },
176 | 	{ time: '2019-04-23', value: 26.06 },
177 | 	{ time: '2019-04-24', value: 26.0 },
178 | 	{ time: '2019-04-25', value: 25.81 },
179 | 	{ time: '2019-04-26', value: 25.88 },
180 | 	{ time: '2019-04-29', value: 25.91 },
181 | 	{ time: '2019-04-30', value: 25.9 },
182 | 	{ time: '2019-05-01', value: 26.02 },
183 | 	{ time: '2019-05-02', value: 25.97 },
184 | 	{ time: '2019-05-03', value: 26.02 },
185 | 	{ time: '2019-05-06', value: 26.03 },
186 | 	{ time: '2019-05-07', value: 26.04 },
187 | 	{ time: '2019-05-08', value: 26.05 },
188 | 	{ time: '2019-05-09', value: 26.05 },
189 | 	{ time: '2019-05-10', value: 26.08 },
190 | 	{ time: '2019-05-13', value: 26.05 },
191 | 	{ time: '2019-05-14', value: 26.01 },
192 | 	{ time: '2019-05-15', value: 26.03 },
193 | 	{ time: '2019-05-16', value: 26.14 },
194 | 	{ time: '2019-05-17', value: 26.09 },
195 | 	{ time: '2019-05-20', value: 26.01 },
196 | 	{ time: '2019-05-21', value: 26.12 },
197 | 	{ time: '2019-05-22', value: 26.15 },
198 | 	{ time: '2019-05-23', value: 26.18 },
199 | 	{ time: '2019-05-24', value: 26.16 },
200 | 	{ time: '2019-05-28', value: 26.23 },
201 | 	// hide-end
202 | ];
203 | 
204 | areaSeries.setData(data);
205 | 
206 | const symbolName = 'AEROSPACE';
207 | 
208 | const container = document.getElementById('container');
209 | 
210 | const legend = document.createElement('div');
211 | legend.style = `position: absolute; left: 12px; top: 12px; z-index: 1; font-size: 14px; font-family: sans-serif; line-height: 18px; font-weight: 300;`;
212 | legend.style.color = CHART_TEXT_COLOR;
213 | container.appendChild(legend);
214 | 
215 | const getLastBar = series => {
216 | 	const lastIndex = series.dataByIndex(Number.MAX_SAFE_INTEGER, -1);
217 | 	return series.dataByIndex(lastIndex);
218 | };
219 | const formatPrice = price => (Math.round(price * 100) / 100).toFixed(2);
220 | const setTooltipHtml = (name, date, price) => {
221 | 	legend.innerHTML = `<div style="font-size: 24px; margin: 4px 0px;">${name}</div><div style="font-size: 22px; margin: 4px 0px;">${price}</div><div>${date}</div>`;
222 | };
223 | 
224 | const updateLegend = param => {
225 | 	const validCrosshairPoint = !(
226 | 		param === undefined || param.time === undefined || param.point.x < 0 || param.point.y < 0
227 | 	);
228 | 	const bar = validCrosshairPoint ? param.seriesData.get(areaSeries) : getLastBar(areaSeries);
229 | 	// time is in the same format that you supplied to the setData method,
230 | 	// which in this case is YYYY-MM-DD
231 | 	const time = bar.time;
232 | 	const price = bar.value !== undefined ? bar.value : bar.close;
233 | 	const formattedPrice = formatPrice(price);
234 | 	setTooltipHtml(symbolName, time, formattedPrice);
235 | };
236 | 
237 | chart.subscribeCrosshairMove(updateLegend);
238 | 
239 | updateLegend(undefined);
240 | 
241 | chart.timeScale().fitContent();
242 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/legend.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Legend
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/how_to/legends
  4 | 
  5 | // remove-end
  6 | const chartOptions = {
  7 | 	layout: {
  8 | 		textColor: CHART_TEXT_COLOR,
  9 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
 10 | 	},
 11 | };
 12 | // remove-line
 13 | /** @type {import('lightweight-charts').IChartApi} */
 14 | const chart = createChart(document.getElementById('container'), chartOptions);
 15 | 
 16 | chart.applyOptions({
 17 | 	rightPriceScale: {
 18 | 		scaleMargins: {
 19 | 			top: 0.3, // leave some space for the legend
 20 | 			bottom: 0.25,
 21 | 		},
 22 | 	},
 23 | 	crosshair: {
 24 | 		// hide the horizontal crosshair line
 25 | 		horzLine: {
 26 | 			visible: false,
 27 | 			labelVisible: false,
 28 | 		},
 29 | 	},
 30 | 	// hide the grid lines
 31 | 	grid: {
 32 | 		vertLines: {
 33 | 			visible: false,
 34 | 		},
 35 | 		horzLines: {
 36 | 			visible: false,
 37 | 		},
 38 | 	},
 39 | });
 40 | 
 41 | const areaSeries = chart.addSeries(AreaSeries, {
 42 | 	topColor: AREA_TOP_COLOR,
 43 | 	bottomColor: AREA_BOTTOM_COLOR,
 44 | 	lineColor: LINE_LINE_COLOR,
 45 | 	lineWidth: 2,
 46 | 	crossHairMarkerVisible: false,
 47 | });
 48 | 
 49 | areaSeries.setData([
 50 | 	{ time: '2018-10-19', value: 26.19 },
 51 | 	// hide-start
 52 | 	{ time: '2018-10-22', value: 25.87 },
 53 | 	{ time: '2018-10-23', value: 25.83 },
 54 | 	{ time: '2018-10-24', value: 25.78 },
 55 | 	{ time: '2018-10-25', value: 25.82 },
 56 | 	{ time: '2018-10-26', value: 25.81 },
 57 | 	{ time: '2018-10-29', value: 25.82 },
 58 | 	{ time: '2018-10-30', value: 25.71 },
 59 | 	{ time: '2018-10-31', value: 25.82 },
 60 | 	{ time: '2018-11-01', value: 25.72 },
 61 | 	{ time: '2018-11-02', value: 25.74 },
 62 | 	{ time: '2018-11-05', value: 25.81 },
 63 | 	{ time: '2018-11-06', value: 25.75 },
 64 | 	{ time: '2018-11-07', value: 25.73 },
 65 | 	{ time: '2018-11-08', value: 25.75 },
 66 | 	{ time: '2018-11-09', value: 25.75 },
 67 | 	{ time: '2018-11-12', value: 25.76 },
 68 | 	{ time: '2018-11-13', value: 25.8 },
 69 | 	{ time: '2018-11-14', value: 25.77 },
 70 | 	{ time: '2018-11-15', value: 25.75 },
 71 | 	{ time: '2018-11-16', value: 25.75 },
 72 | 	{ time: '2018-11-19', value: 25.75 },
 73 | 	{ time: '2018-11-20', value: 25.72 },
 74 | 	{ time: '2018-11-21', value: 25.78 },
 75 | 	{ time: '2018-11-23', value: 25.72 },
 76 | 	{ time: '2018-11-26', value: 25.78 },
 77 | 	{ time: '2018-11-27', value: 25.85 },
 78 | 	{ time: '2018-11-28', value: 25.85 },
 79 | 	{ time: '2018-11-29', value: 25.55 },
 80 | 	{ time: '2018-11-30', value: 25.41 },
 81 | 	{ time: '2018-12-03', value: 25.41 },
 82 | 	{ time: '2018-12-04', value: 25.42 },
 83 | 	{ time: '2018-12-06', value: 25.33 },
 84 | 	{ time: '2018-12-07', value: 25.39 },
 85 | 	{ time: '2018-12-10', value: 25.32 },
 86 | 	{ time: '2018-12-11', value: 25.48 },
 87 | 	{ time: '2018-12-12', value: 25.39 },
 88 | 	{ time: '2018-12-13', value: 25.45 },
 89 | 	{ time: '2018-12-14', value: 25.52 },
 90 | 	{ time: '2018-12-17', value: 25.38 },
 91 | 	{ time: '2018-12-18', value: 25.36 },
 92 | 	{ time: '2018-12-19', value: 25.65 },
 93 | 	{ time: '2018-12-20', value: 25.7 },
 94 | 	{ time: '2018-12-21', value: 25.66 },
 95 | 	{ time: '2018-12-24', value: 25.66 },
 96 | 	{ time: '2018-12-26', value: 25.65 },
 97 | 	{ time: '2018-12-27', value: 25.66 },
 98 | 	{ time: '2018-12-28', value: 25.68 },
 99 | 	{ time: '2018-12-31', value: 25.77 },
100 | 	{ time: '2019-01-02', value: 25.72 },
101 | 	{ time: '2019-01-03', value: 25.69 },
102 | 	{ time: '2019-01-04', value: 25.71 },
103 | 	{ time: '2019-01-07', value: 25.72 },
104 | 	{ time: '2019-01-08', value: 25.72 },
105 | 	{ time: '2019-01-09', value: 25.66 },
106 | 	{ time: '2019-01-10', value: 25.85 },
107 | 	{ time: '2019-01-11', value: 25.92 },
108 | 	{ time: '2019-01-14', value: 25.94 },
109 | 	{ time: '2019-01-15', value: 25.95 },
110 | 	{ time: '2019-01-16', value: 26.0 },
111 | 	{ time: '2019-01-17', value: 25.99 },
112 | 	{ time: '2019-01-18', value: 25.6 },
113 | 	{ time: '2019-01-22', value: 25.81 },
114 | 	{ time: '2019-01-23', value: 25.7 },
115 | 	{ time: '2019-01-24', value: 25.74 },
116 | 	{ time: '2019-01-25', value: 25.8 },
117 | 	{ time: '2019-01-28', value: 25.83 },
118 | 	{ time: '2019-01-29', value: 25.7 },
119 | 	{ time: '2019-01-30', value: 25.78 },
120 | 	{ time: '2019-01-31', value: 25.35 },
121 | 	{ time: '2019-02-01', value: 25.6 },
122 | 	{ time: '2019-02-04', value: 25.65 },
123 | 	{ time: '2019-02-05', value: 25.73 },
124 | 	{ time: '2019-02-06', value: 25.71 },
125 | 	{ time: '2019-02-07', value: 25.71 },
126 | 	{ time: '2019-02-08', value: 25.72 },
127 | 	{ time: '2019-02-11', value: 25.76 },
128 | 	{ time: '2019-02-12', value: 25.84 },
129 | 	{ time: '2019-02-13', value: 25.85 },
130 | 	{ time: '2019-02-14', value: 25.87 },
131 | 	{ time: '2019-02-15', value: 25.89 },
132 | 	{ time: '2019-02-19', value: 25.9 },
133 | 	{ time: '2019-02-20', value: 25.92 },
134 | 	{ time: '2019-02-21', value: 25.96 },
135 | 	{ time: '2019-02-22', value: 26.0 },
136 | 	{ time: '2019-02-25', value: 25.93 },
137 | 	{ time: '2019-02-26', value: 25.92 },
138 | 	{ time: '2019-02-27', value: 25.67 },
139 | 	{ time: '2019-02-28', value: 25.79 },
140 | 	{ time: '2019-03-01', value: 25.86 },
141 | 	{ time: '2019-03-04', value: 25.94 },
142 | 	{ time: '2019-03-05', value: 26.02 },
143 | 	{ time: '2019-03-06', value: 25.95 },
144 | 	{ time: '2019-03-07', value: 25.89 },
145 | 	{ time: '2019-03-08', value: 25.94 },
146 | 	{ time: '2019-03-11', value: 25.91 },
147 | 	{ time: '2019-03-12', value: 25.92 },
148 | 	{ time: '2019-03-13', value: 26.0 },
149 | 	{ time: '2019-03-14', value: 26.05 },
150 | 	{ time: '2019-03-15', value: 26.11 },
151 | 	{ time: '2019-03-18', value: 26.1 },
152 | 	{ time: '2019-03-19', value: 25.98 },
153 | 	{ time: '2019-03-20', value: 26.11 },
154 | 	{ time: '2019-03-21', value: 26.12 },
155 | 	{ time: '2019-03-22', value: 25.88 },
156 | 	{ time: '2019-03-25', value: 25.85 },
157 | 	{ time: '2019-03-26', value: 25.72 },
158 | 	{ time: '2019-03-27', value: 25.73 },
159 | 	{ time: '2019-03-28', value: 25.8 },
160 | 	{ time: '2019-03-29', value: 25.77 },
161 | 	{ time: '2019-04-01', value: 26.06 },
162 | 	{ time: '2019-04-02', value: 25.93 },
163 | 	{ time: '2019-04-03', value: 25.95 },
164 | 	{ time: '2019-04-04', value: 26.06 },
165 | 	{ time: '2019-04-05', value: 26.16 },
166 | 	{ time: '2019-04-08', value: 26.12 },
167 | 	{ time: '2019-04-09', value: 26.07 },
168 | 	{ time: '2019-04-10', value: 26.13 },
169 | 	{ time: '2019-04-11', value: 26.04 },
170 | 	{ time: '2019-04-12', value: 26.04 },
171 | 	{ time: '2019-04-15', value: 26.05 },
172 | 	{ time: '2019-04-16', value: 26.01 },
173 | 	{ time: '2019-04-17', value: 26.09 },
174 | 	{ time: '2019-04-18', value: 26.0 },
175 | 	{ time: '2019-04-22', value: 26.0 },
176 | 	{ time: '2019-04-23', value: 26.06 },
177 | 	{ time: '2019-04-24', value: 26.0 },
178 | 	{ time: '2019-04-25', value: 25.81 },
179 | 	{ time: '2019-04-26', value: 25.88 },
180 | 	{ time: '2019-04-29', value: 25.91 },
181 | 	{ time: '2019-04-30', value: 25.9 },
182 | 	{ time: '2019-05-01', value: 26.02 },
183 | 	{ time: '2019-05-02', value: 25.97 },
184 | 	{ time: '2019-05-03', value: 26.02 },
185 | 	{ time: '2019-05-06', value: 26.03 },
186 | 	{ time: '2019-05-07', value: 26.04 },
187 | 	{ time: '2019-05-08', value: 26.05 },
188 | 	{ time: '2019-05-09', value: 26.05 },
189 | 	{ time: '2019-05-10', value: 26.08 },
190 | 	{ time: '2019-05-13', value: 26.05 },
191 | 	{ time: '2019-05-14', value: 26.01 },
192 | 	{ time: '2019-05-15', value: 26.03 },
193 | 	{ time: '2019-05-16', value: 26.14 },
194 | 	{ time: '2019-05-17', value: 26.09 },
195 | 	{ time: '2019-05-20', value: 26.01 },
196 | 	{ time: '2019-05-21', value: 26.12 },
197 | 	{ time: '2019-05-22', value: 26.15 },
198 | 	{ time: '2019-05-23', value: 26.18 },
199 | 	{ time: '2019-05-24', value: 26.16 },
200 | 	{ time: '2019-05-28', value: 26.23 },
201 | 	// hide-end
202 | ]);
203 | 
204 | const symbolName = 'ETC USD 7D VWAP';
205 | 
206 | const container = document.getElementById('container');
207 | 
208 | const legend = document.createElement('div');
209 | legend.style = `position: absolute; left: 12px; top: 12px; z-index: 1; font-size: 14px; font-family: sans-serif; line-height: 18px; font-weight: 300;`;
210 | container.appendChild(legend);
211 | 
212 | const firstRow = document.createElement('div');
213 | firstRow.innerHTML = symbolName;
214 | firstRow.style.color = CHART_TEXT_COLOR;
215 | legend.appendChild(firstRow);
216 | 
217 | chart.subscribeCrosshairMove(param => {
218 | 	let priceFormatted = '';
219 | 	if (param.time) {
220 | 		const data = param.seriesData.get(areaSeries);
221 | 		const price = data.value !== undefined ? data.value : data.close;
222 | 		priceFormatted = price.toFixed(2);
223 | 	}
224 | 	firstRow.innerHTML = `${symbolName} <strong>${priceFormatted}</strong>`;
225 | });
226 | 
227 | chart.timeScale().fitContent();
228 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/legends.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Legends
 3 | sidebar_label: Legends
 4 | description: Examples on how to add a legend to your chart.
 5 | pagination_prev: null
 6 | pagination_next: null
 7 | keywords:
 8 |   - example
 9 |   - legend
10 | ---
11 | 
12 | import VersionWarningAdmonition from "@site/src/components/VersionWarningAdmonition";
13 | 
14 | {/*
15 |   Show warning when not on the latest published version
16 |   Tutorials section isn't versioned yet, hence the need for the warning message
17 |   THESE TUTORIALS NEED TO BE UPDATED FOR VERSION 4
18 | */}
19 | 
20 | <VersionWarningAdmonition
21 | 	notCurrent="This example is for the latest published version of Lightweight Charts."
22 | 	type="caution"
23 | 	displayVersionMessage
24 | />
25 | 
26 | Lightweight Charts™ doesn't include a built-in legend feature, however it is something which can be added
27 | to your chart by following the examples presented below.
28 | 
29 | ## How to
30 | 
31 | In order to add a legend to the chart we need to create and position an `html` into the desired position above
32 | the chart. We can then subscribe to the crosshairMove events ([subscribeCrosshairMove](/docs/api/interfaces/IChartApi#subscribecrosshairmove)) provided by the [`IChartApi`](/docs/api/interfaces/IChartApi) instance, and manually
33 | update the content within our `html` legend element.
34 | 
35 | ```js
36 | chart.subscribeCrosshairMove(param => {
37 |     let priceFormatted = '';
38 |     if (param.time) {
39 |         const dataPoint = param.seriesData.get(areaSeries);
40 |         const price = data.value !== undefined ? data.value : data.close;
41 |         priceFormatted = price.toFixed(2);
42 |     }
43 |     // legend is a html element which has already been created
44 |     legend.innerHTML = `${symbolName} <strong>${priceFormatted}</strong>`;
45 | });
46 | ```
47 | 
48 | The process of creating the legend html element and positioning can be seen within the examples below.
49 | Essentially, we create a new div element within the container div (holding the chart) and then position
50 | and style it using `css`.
51 | 
52 | You can see full [working examples](#examples) below.
53 | 
54 | ## Resources
55 | 
56 | - [subscribeCrosshairMove](/docs/api/interfaces/IChartApi#subscribecrosshairmove)
57 | - [MouseEventParams Interface](/docs/api/interfaces/MouseEventParams)
58 | - [MouseEventhandler](/docs/api/type-aliases/MouseEventHandler)
59 | 
60 | Below are a few external resources related to creating and styling html elements:
61 | 
62 | - [createElement](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)
63 | - [innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML)
64 | - [style property](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style)
65 | 
66 | ## Examples
67 | 
68 | import UsageGuidePartial from "../_usage-guide-partial.mdx";
69 | 
70 | <UsageGuidePartial />
71 | 
72 | import CodeBlock from "@theme/CodeBlock";
73 | 
74 | ### Simple Legend Example
75 | 
76 | import codeLegend from "!!raw-loader!./legend.js";
77 | 
78 | <CodeBlock replaceThemeConstants chart className="language-js" hideableCode chartOnTop>
79 | 	{codeLegend}
80 | </CodeBlock>
81 | 
82 | ### 3 Line Legend Example
83 | 
84 | import code3Line from "!!raw-loader!./legend-3line.js";
85 | 
86 | <CodeBlock replaceThemeConstants chart className="language-js" hideableCode chartOnTop>
87 | 	{code3Line}
88 | </CodeBlock>
89 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/no-time-scale.js:
--------------------------------------------------------------------------------
 1 | // remove-start
 2 | // Lightweight Charts™ Example: No Time Scale
 3 | // https://tradingview.github.io/lightweight-charts/tutorials/how_to/example
 4 | 
 5 | // remove-end
 6 | const chartOptions = {
 7 | 	layout: {
 8 | 		textColor: CHART_TEXT_COLOR,
 9 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
10 | 	},
11 | };
12 | // remove-line
13 | /** @type {import('lightweight-charts').IChartApi} */
14 | const chart = createChart(document.getElementById('container'), chartOptions);
15 | 
16 | // highlight-start
17 | chart.applyOptions({
18 | 	timeScale: {
19 | 		visible: false,
20 | 	},
21 | });
22 | // highlight-end
23 | 
24 | const lineSeries = chart.addSeries(LineSeries, { color: LINE_LINE_COLOR });
25 | 
26 | const data = [
27 | 	{ value: 0, time: 1642425322 },
28 | 	// hide-start
29 | 	{ value: 8, time: 1642511722 },
30 | 	{ value: 10, time: 1642598122 },
31 | 	{ value: 20, time: 1642684522 },
32 | 	{ value: 3, time: 1642770922 },
33 | 	{ value: 43, time: 1642857322 },
34 | 	{ value: 41, time: 1642943722 },
35 | 	{ value: 43, time: 1643030122 },
36 | 	{ value: 56, time: 1643116522 },
37 | 	{ value: 46, time: 1643202922 },
38 | 	// hide-end
39 | ];
40 | 
41 | lineSeries.setData(data);
42 | 
43 | chart.timeScale().fitContent();
44 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/panes.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Price and Volume
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/how_to/price-and-volume
  4 | 
  5 | // remove-end
  6 | const chartOptions = {
  7 | 	layout: {
  8 | 		textColor: CHART_TEXT_COLOR,
  9 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
 10 | 		// highlight-start
 11 | 		panes: {
 12 | 			separatorColor: '#f22c3d',
 13 | 			separatorHoverColor: 'rgba(255, 0, 0, 0.1)',
 14 | 			// setting this to false will disable the resize of the panes by the user
 15 | 			enableResize: false,
 16 | 		},
 17 | 		// highlight-end
 18 | 	},
 19 | };
 20 | // remove-line
 21 | /** @type {import('lightweight-charts').IChartApi} */
 22 | const chart = createChart(document.getElementById('container'), chartOptions);
 23 | 
 24 | const areaSeries = chart.addSeries(AreaSeries, {
 25 | 	topColor: AREA_TOP_COLOR,
 26 | 	bottomColor: AREA_BOTTOM_COLOR,
 27 | 	lineColor: LINE_LINE_COLOR,
 28 | 	lineWidth: 2,
 29 | });
 30 | 
 31 | const candlestickSeries = chart.addSeries(CandlestickSeries, {
 32 | 	upColor: '#26a69a', downColor: '#ef5350', borderVisible: false,
 33 | 	wickUpColor: '#26a69a', wickDownColor: '#ef5350',
 34 | 	// we are setting pane index 1 for this series
 35 | }, 1);
 36 | 
 37 | areaSeries.setData([
 38 | 	{ time: '2018-10-19', value: 52.89 },
 39 | 	// hide-start
 40 | 	{ time: '2018-10-22', value: 55.22 },
 41 | 	{ time: '2018-10-23', value: 57.21 },
 42 | 	{ time: '2018-10-24', value: 57.42 },
 43 | 	{ time: '2018-10-25', value: 56.43 },
 44 | 	{ time: '2018-10-26', value: 55.51 },
 45 | 	{ time: '2018-10-29', value: 56.48 },
 46 | 	{ time: '2018-10-30', value: 58.18 },
 47 | 	{ time: '2018-10-31', value: 57.09 },
 48 | 	{ time: '2018-11-01', value: 56.05 },
 49 | 	{ time: '2018-11-02', value: 56.63 },
 50 | 	{ time: '2018-11-05', value: 57.21 },
 51 | 	{ time: '2018-11-06', value: 57.21 },
 52 | 	{ time: '2018-11-07', value: 57.65 },
 53 | 	{ time: '2018-11-08', value: 58.27 },
 54 | 	{ time: '2018-11-09', value: 58.46 },
 55 | 	{ time: '2018-11-12', value: 58.72 },
 56 | 	{ time: '2018-11-13', value: 58.66 },
 57 | 	{ time: '2018-11-14', value: 58.94 },
 58 | 	{ time: '2018-11-15', value: 59.08 },
 59 | 	{ time: '2018-11-16', value: 60.21 },
 60 | 	{ time: '2018-11-19', value: 60.62 },
 61 | 	{ time: '2018-11-20', value: 59.46 },
 62 | 	{ time: '2018-11-21', value: 59.16 },
 63 | 	{ time: '2018-11-23', value: 58.64 },
 64 | 	{ time: '2018-11-26', value: 59.17 },
 65 | 	{ time: '2018-11-27', value: 60.65 },
 66 | 	{ time: '2018-11-28', value: 60.06 },
 67 | 	{ time: '2018-11-29', value: 59.45 },
 68 | 	{ time: '2018-11-30', value: 60.30 },
 69 | 	{ time: '2018-12-03', value: 58.16 },
 70 | 	{ time: '2018-12-04', value: 58.09 },
 71 | 	{ time: '2018-12-06', value: 58.08 },
 72 | 	{ time: '2018-12-07', value: 57.68 },
 73 | 	{ time: '2018-12-10', value: 58.27 },
 74 | 	{ time: '2018-12-11', value: 58.85 },
 75 | 	{ time: '2018-12-12', value: 57.25 },
 76 | 	{ time: '2018-12-13', value: 57.09 },
 77 | 	{ time: '2018-12-14', value: 57.08 },
 78 | 	{ time: '2018-12-17', value: 55.95 },
 79 | 	{ time: '2018-12-18', value: 55.65 },
 80 | 	{ time: '2018-12-19', value: 55.86 },
 81 | 	{ time: '2018-12-20', value: 55.07 },
 82 | 	{ time: '2018-12-21', value: 54.92 },
 83 | 	{ time: '2018-12-24', value: 53.05 },
 84 | 	// hide-end
 85 | ]);
 86 | 
 87 | // setting the data for the volume series.
 88 | // note: we are defining each bars color as part of the data
 89 | candlestickSeries.setData([
 90 | 	{ time: '2018-10-19', open: 75.16, high: 82.84, low: 36.16, close: 45.72 },
 91 | 	// hide-start
 92 | 	{ time: '2018-10-22', open: 72.16, high: 80.32, low: 32.18, close: 42.12 },
 93 | 	{ time: '2018-10-23', open: 45.12, high: 53.90, low: 45.12, close: 48.09 },
 94 | 	{ time: '2018-10-24', open: 60.71, high: 60.71, low: 53.39, close: 59.29 },
 95 | 	{ time: '2018-10-25', open: 68.26, high: 68.26, low: 59.04, close: 60.50 },
 96 | 	{ time: '2018-10-26', open: 67.71, high: 105.85, low: 66.67, close: 91.04 },
 97 | 	{ time: '2018-10-29', open: 91.04, high: 121.40, low: 82.70, close: 111.40 },
 98 | 	{ time: '2018-10-30', open: 111.51, high: 142.83, low: 103.34, close: 131.25 },
 99 | 	{ time: '2018-10-31', open: 131.33, high: 151.17, low: 77.68, close: 96.43 },
100 | 	{ time: '2018-11-01', open: 106.33, high: 110.20, low: 90.39, close: 98.10 },
101 | 	{ time: '2018-11-02', open: 109.87, high: 114.69, low: 85.66, close: 111.26 },
102 | 	{ time: '2018-11-05', open: 56.02, high: 56.02, low: 56.02, close: 56.02 },
103 | 	{ time: '2018-11-06', open: 106.33, high: 110.20, low: 90.39, close: 98.10 },
104 | 	{ time: '2018-11-07', open: 109.87, high: 114.69, low: 85.66, close: 111.26 },
105 | 	{ time: '2018-11-09', open: 58.46, high: 53.90, low: 32.18, close: 42.12 },
106 | 	{ time: '2018-11-12', open: 45.12, high: 60.71, low: 45.12, close: 48.09 },
107 | 	{ time: '2018-11-13', open: 60.71, high: 68.26, low: 53.39, close: 59.29 },
108 | 	{ time: '2018-11-14', open: 68.26, high: 105.85, low: 59.04, close: 60.50 },
109 | 	{ time: '2018-11-15', open: 67.71, high: 121.40, low: 66.67, close: 91.04 },
110 | 	{ time: '2018-11-16', open: 91.04, high: 142.83, low: 82.70, close: 111.40 },
111 | 	{ time: '2018-11-19', open: 111.51, high: 151.17, low: 103.34, close: 131.25 },
112 | 	{ time: '2018-11-20', open: 131.33, high: 110.20, low: 77.68, close: 96.43 },
113 | 	{ time: '2018-11-21', open: 106.33, high: 114.69, low: 90.39, close: 98.10 },
114 | 	{ time: '2018-11-23', open: 109.87, high: 56.02, low: 85.66, close: 111.26 },
115 | 	{ time: '2018-11-26', open: 59.17, high: 58.46, low: 56.02, close: 56.02 },
116 | 	{ time: '2018-11-27', open: 60.65, high: 58.46, low: 90.39, close: 98.10 },
117 | 	{ time: '2018-11-28', open: 60.06, high: 58.46, low: 85.66, close: 111.26 },
118 | 	{ time: '2018-11-29', open: 59.45, high: 58.46, low: 58.46, close: 58.46 },
119 | 	{ time: '2018-11-30', open: 60.30, high: 58.46, low: 58.46, close: 58.46 },
120 | 	{ time: '2018-12-03', open: 72.16, high: 80.32, low: 32.18, close: 42.12 },
121 | 	{ time: '2018-12-04', open: 45.12, high: 53.90, low: 45.12, close: 48.09 },
122 | 	{ time: '2018-12-06', open: 60.71, high: 60.71, low: 53.39, close: 59.29 },
123 | 	{ time: '2018-12-07', open: 68.26, high: 68.26, low: 59.04, close: 60.50 },
124 | 	{ time: '2018-12-10', open: 67.71, high: 105.85, low: 66.67, close: 91.04 },
125 | 	{ time: '2018-12-11', open: 91.04, high: 121.40, low: 82.70, close: 111.40 },
126 | 	{ time: '2018-12-12', open: 111.51, high: 142.83, low: 103.34, close: 131.25 },
127 | 	{ time: '2018-12-13', open: 131.33, high: 151.17, low: 77.68, close: 96.43 },
128 | 	{ time: '2018-12-14', open: 106.33, high: 110.20, low: 90.39, close: 98.10 },
129 | 	{ time: '2018-12-17', open: 109.87, high: 114.69, low: 85.66, close: 111.26 },
130 | 	{ time: '2018-12-18', open: 56.02, high: 56.02, low: 56.02, close: 56.02 },
131 | 	{ time: '2018-12-19', open: 106.33, high: 110.20, low: 90.39, close: 98.10 },
132 | 	{ time: '2018-12-20', open: 109.87, high: 114.69, low: 85.66, close: 111.26 },
133 | 	{ time: '2018-12-21', open: 58.46, high: 53.90, low: 32.18, close: 42.12 },
134 | 	{ time: '2018-12-24', open: 45.12, high: 60.71, low: 45.12, close: 48.09 },
135 | 	// hide-end
136 | ]);
137 | // highlight-start
138 | const candlesPane = chart.panes()[1];
139 | candlesPane.moveTo(0);
140 | candlesPane.setHeight(150);
141 | // highlight-end
142 | chart.timeScale().fitContent();
143 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/panes.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Panes
 3 | sidebar_label: Panes
 4 | description: An example of how to manipulate panes in Lightweight Charts.
 5 | pagination_prev: null
 6 | pagination_next: null
 7 | keywords:
 8 |   - example
 9 | ---
10 | 
11 | Lightweight Charts™ allows you to create multiple [panes](/docs/next/panes) in a single chart.
12 | 
13 | Using multiple panes in a charting library can be incredibly useful for a variety of analytical and visualization scenarios,
14 | especially when dealing with complex datasets or requiring detailed comparative analysis across different data dimensions.
15 | 
16 | This example shows how to use panes in Lightweight Charts™. We will create a chart with two panes: the first one will display a stock's price over time and the second one will contain trading volume. The price and volume will be represented with candles and an area, respectively.
17 | 
18 | You can see a full [working example](#full-example) below.
19 | 
20 | ## How to add a pane
21 | 
22 | To introduce an additional pane into a chart, specify `paneIndex` during series creation.
23 | 
24 | Alternatively, you can invoke the [`moveToPane`](/docs/next/api/interfaces/ISeriesApi#movetopane) method on the series instance. Note that if the pane with specified index doesn't exist, it will be created.
25 | 
26 | ```js
27 | const volumeSeries = chart.addSeries(
28 |     HistogramSeries,
29 |     {
30 |         priceFormat: {
31 |             type: 'volume',
32 |         },
33 |     },
34 |     1 // Pane index
35 | );
36 | // Moving the series to a different pane
37 | volumeSeries.moveToPane(2);
38 | ```
39 | 
40 | If a series is moved out of a pane and no other series remain, the pane will be automatically removed.
41 | 
42 | ### Customizations
43 | 
44 | Lightweight Charts™ provides options to customize the panes. You can adjust the pane separator color by specifying the `separatorColor` property in the
45 | [`layout.panes`](/docs/next/api/interfaces/LayoutPanesOptions) chart options, and use `separatorHoverColor` to change the separator color on hover.
46 | 
47 | ```js
48 | chart.applyOptions({
49 |     layout: {
50 |         panes: {
51 |             separatorColor: '#ff0000',
52 |             separatorHoverColor: '#00ff00',
53 |             enableResize: false,
54 |         },
55 |     },
56 | });
57 | ```
58 | 
59 | Lightweight Charts™ includes  [`PaneApi`](/docs/next/api/interfaces/IPaneApi) that allows you to control each pane. The API has methods to get information on the pane such as `getHeight()`, `paneIndex()`, and `getSeries()`. It also contains methods to adjust the pane parameters, for example `setHeight(height)` and `moveTo(paneIndex)`.
60 | 
61 | To get a `PaneApi` instance for each pane, you need to call the `panes` method on the `ChartApi` instance.
62 | Let's say we want to set the height of the second pane to 300px and move it to the first position.
63 | 
64 | ```js
65 | const secondPane = chart.panes()[1];
66 | secondPane.setHeight(300);
67 | secondPane.moveTo(0);
68 | ```
69 | 
70 | Note that the minimum pane height is 30px. Any values lower than 30px will be ignored.
71 | 
72 | To remove the pane, you can call the `removePane(paneIndex)` method on the `ChartApi` instance.
73 | 
74 | ```js
75 | chart.removePane(1);
76 | ```
77 | 
78 | Note that removing a pane also removes any series contained within it.
79 | 
80 | ## Full Example
81 | 
82 | import UsageGuidePartial from "./_usage-guide-partial.mdx";
83 | 
84 | <UsageGuidePartial />
85 | 
86 | import CodeBlock from "@theme/CodeBlock";
87 | import code from "!!raw-loader!./panes.js";
88 | 
89 | <CodeBlock replaceThemeConstants chart className="language-js" hideableCode>
90 | 	{code}
91 | </CodeBlock>
92 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/price-and-volume.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Price and Volume
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/how_to/price-and-volume
  4 | 
  5 | // remove-end
  6 | const chartOptions = {
  7 | 	layout: {
  8 | 		textColor: CHART_TEXT_COLOR,
  9 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
 10 | 	},
 11 | 	rightPriceScale: {
 12 | 		borderVisible: false,
 13 | 	},
 14 | };
 15 | // remove-line
 16 | /** @type {import('lightweight-charts').IChartApi} */
 17 | const chart = createChart(document.getElementById('container'), chartOptions);
 18 | 
 19 | const areaSeries = chart.addSeries(AreaSeries, {
 20 | 	topColor: AREA_TOP_COLOR,
 21 | 	bottomColor: AREA_BOTTOM_COLOR,
 22 | 	lineColor: LINE_LINE_COLOR,
 23 | 	lineWidth: 2,
 24 | });
 25 | areaSeries.priceScale().applyOptions({
 26 | 	// highlight-start
 27 | 	scaleMargins: {
 28 | 		// positioning the price scale for the area series
 29 | 		top: 0.1,
 30 | 		bottom: 0.4,
 31 | 	},
 32 | 	// highlight-end
 33 | });
 34 | 
 35 | const volumeSeries = chart.addSeries(HistogramSeries, {
 36 | 	color: BAR_UP_COLOR,
 37 | 	// highlight-start
 38 | 	priceFormat: {
 39 | 		type: 'volume',
 40 | 	},
 41 | 	priceScaleId: '', // set as an overlay by setting a blank priceScaleId
 42 | 	// set the positioning of the volume series
 43 | 	scaleMargins: {
 44 | 		top: 0.7, // highest point of the series will be 70% away from the top
 45 | 		bottom: 0,
 46 | 	},
 47 | });
 48 | volumeSeries.priceScale().applyOptions({
 49 | 	scaleMargins: {
 50 | 		top: 0.7, // highest point of the series will be 70% away from the top
 51 | 		bottom: 0,
 52 | 	},
 53 | });
 54 | // highlight-end
 55 | 
 56 | areaSeries.setData([
 57 | 	{ time: '2018-10-19', value: 54.90 },
 58 | 	// hide-start
 59 | 	{ time: '2018-10-22', value: 54.98 },
 60 | 	{ time: '2018-10-23', value: 57.21 },
 61 | 	{ time: '2018-10-24', value: 57.42 },
 62 | 	{ time: '2018-10-25', value: 56.43 },
 63 | 	{ time: '2018-10-26', value: 55.51 },
 64 | 	{ time: '2018-10-29', value: 56.48 },
 65 | 	{ time: '2018-10-30', value: 58.18 },
 66 | 	{ time: '2018-10-31', value: 57.09 },
 67 | 	{ time: '2018-11-01', value: 56.05 },
 68 | 	{ time: '2018-11-02', value: 56.63 },
 69 | 	{ time: '2018-11-05', value: 57.21 },
 70 | 	{ time: '2018-11-06', value: 57.21 },
 71 | 	{ time: '2018-11-07', value: 57.65 },
 72 | 	{ time: '2018-11-08', value: 58.27 },
 73 | 	{ time: '2018-11-09', value: 58.46 },
 74 | 	{ time: '2018-11-12', value: 58.72 },
 75 | 	{ time: '2018-11-13', value: 58.66 },
 76 | 	{ time: '2018-11-14', value: 58.94 },
 77 | 	{ time: '2018-11-15', value: 59.08 },
 78 | 	{ time: '2018-11-16', value: 60.21 },
 79 | 	{ time: '2018-11-19', value: 60.62 },
 80 | 	{ time: '2018-11-20', value: 59.46 },
 81 | 	{ time: '2018-11-21', value: 59.16 },
 82 | 	{ time: '2018-11-23', value: 58.64 },
 83 | 	{ time: '2018-11-26', value: 59.17 },
 84 | 	{ time: '2018-11-27', value: 60.65 },
 85 | 	{ time: '2018-11-28', value: 60.06 },
 86 | 	{ time: '2018-11-29', value: 59.45 },
 87 | 	{ time: '2018-11-30', value: 60.30 },
 88 | 	{ time: '2018-12-03', value: 58.16 },
 89 | 	{ time: '2018-12-04', value: 58.09 },
 90 | 	{ time: '2018-12-06', value: 58.08 },
 91 | 	{ time: '2018-12-07', value: 57.68 },
 92 | 	{ time: '2018-12-10', value: 58.27 },
 93 | 	{ time: '2018-12-11', value: 58.85 },
 94 | 	{ time: '2018-12-12', value: 57.25 },
 95 | 	{ time: '2018-12-13', value: 57.09 },
 96 | 	{ time: '2018-12-14', value: 57.08 },
 97 | 	{ time: '2018-12-17', value: 55.95 },
 98 | 	{ time: '2018-12-18', value: 55.65 },
 99 | 	{ time: '2018-12-19', value: 55.86 },
100 | 	{ time: '2018-12-20', value: 55.07 },
101 | 	{ time: '2018-12-21', value: 54.92 },
102 | 	{ time: '2018-12-24', value: 53.05 },
103 | 	{ time: '2018-12-26', value: 54.44 },
104 | 	{ time: '2018-12-27', value: 55.15 },
105 | 	{ time: '2018-12-28', value: 55.27 },
106 | 	{ time: '2018-12-31', value: 56.22 },
107 | 	{ time: '2019-01-02', value: 56.02 },
108 | 	{ time: '2019-01-03', value: 56.22 },
109 | 	{ time: '2019-01-04', value: 56.36 },
110 | 	{ time: '2019-01-07', value: 56.72 },
111 | 	{ time: '2019-01-08', value: 58.38 },
112 | 	{ time: '2019-01-09', value: 57.05 },
113 | 	{ time: '2019-01-10', value: 57.60 },
114 | 	{ time: '2019-01-11', value: 58.02 },
115 | 	{ time: '2019-01-14', value: 58.03 },
116 | 	{ time: '2019-01-15', value: 58.10 },
117 | 	{ time: '2019-01-16', value: 57.08 },
118 | 	{ time: '2019-01-17', value: 56.83 },
119 | 	{ time: '2019-01-18', value: 57.09 },
120 | 	{ time: '2019-01-22', value: 56.99 },
121 | 	{ time: '2019-01-23', value: 57.76 },
122 | 	{ time: '2019-01-24', value: 57.07 },
123 | 	{ time: '2019-01-25', value: 56.40 },
124 | 	{ time: '2019-01-28', value: 55.07 },
125 | 	{ time: '2019-01-29', value: 53.28 },
126 | 	{ time: '2019-01-30', value: 54.00 },
127 | 	{ time: '2019-01-31', value: 55.06 },
128 | 	{ time: '2019-02-01', value: 54.55 },
129 | 	{ time: '2019-02-04', value: 54.04 },
130 | 	{ time: '2019-02-05', value: 54.14 },
131 | 	{ time: '2019-02-06', value: 53.79 },
132 | 	{ time: '2019-02-07', value: 53.57 },
133 | 	{ time: '2019-02-08', value: 53.95 },
134 | 	{ time: '2019-02-11', value: 54.05 },
135 | 	{ time: '2019-02-12', value: 54.42 },
136 | 	{ time: '2019-02-13', value: 54.48 },
137 | 	{ time: '2019-02-14', value: 54.03 },
138 | 	{ time: '2019-02-15', value: 55.16 },
139 | 	{ time: '2019-02-19', value: 55.44 },
140 | 	{ time: '2019-02-20', value: 55.76 },
141 | 	{ time: '2019-02-21', value: 56.15 },
142 | 	{ time: '2019-02-22', value: 56.92 },
143 | 	{ time: '2019-02-25', value: 56.78 },
144 | 	{ time: '2019-02-26', value: 56.64 },
145 | 	{ time: '2019-02-27', value: 56.72 },
146 | 	{ time: '2019-02-28', value: 56.92 },
147 | 	{ time: '2019-03-01', value: 56.96 },
148 | 	{ time: '2019-03-04', value: 56.24 },
149 | 	{ time: '2019-03-05', value: 56.08 },
150 | 	{ time: '2019-03-06', value: 55.68 },
151 | 	{ time: '2019-03-07', value: 56.30 },
152 | 	{ time: '2019-03-08', value: 56.53 },
153 | 	{ time: '2019-03-11', value: 57.58 },
154 | 	{ time: '2019-03-12', value: 57.43 },
155 | 	{ time: '2019-03-13', value: 57.66 },
156 | 	{ time: '2019-03-14', value: 57.95 },
157 | 	{ time: '2019-03-15', value: 58.39 },
158 | 	{ time: '2019-03-18', value: 58.07 },
159 | 	{ time: '2019-03-19', value: 57.50 },
160 | 	{ time: '2019-03-20', value: 57.67 },
161 | 	{ time: '2019-03-21', value: 58.29 },
162 | 	{ time: '2019-03-22', value: 59.76 },
163 | 	{ time: '2019-03-25', value: 60.08 },
164 | 	{ time: '2019-03-26', value: 60.63 },
165 | 	{ time: '2019-03-27', value: 60.88 },
166 | 	{ time: '2019-03-28', value: 59.08 },
167 | 	{ time: '2019-03-29', value: 59.13 },
168 | 	{ time: '2019-04-01', value: 59.09 },
169 | 	{ time: '2019-04-02', value: 58.53 },
170 | 	{ time: '2019-04-03', value: 58.87 },
171 | 	{ time: '2019-04-04', value: 58.99 },
172 | 	{ time: '2019-04-05', value: 59.09 },
173 | 	{ time: '2019-04-08', value: 59.13 },
174 | 	{ time: '2019-04-09', value: 58.40 },
175 | 	{ time: '2019-04-10', value: 58.61 },
176 | 	{ time: '2019-04-11', value: 58.56 },
177 | 	{ time: '2019-04-12', value: 58.74 },
178 | 	{ time: '2019-04-15', value: 58.71 },
179 | 	{ time: '2019-04-16', value: 58.79 },
180 | 	{ time: '2019-04-17', value: 57.78 },
181 | 	{ time: '2019-04-18', value: 58.04 },
182 | 	{ time: '2019-04-22', value: 58.37 },
183 | 	{ time: '2019-04-23', value: 57.15 },
184 | 	{ time: '2019-04-24', value: 57.08 },
185 | 	{ time: '2019-04-25', value: 55.85 },
186 | 	{ time: '2019-04-26', value: 56.58 },
187 | 	{ time: '2019-04-29', value: 56.84 },
188 | 	{ time: '2019-04-30', value: 57.19 },
189 | 	{ time: '2019-05-01', value: 56.52 },
190 | 	{ time: '2019-05-02', value: 56.99 },
191 | 	{ time: '2019-05-03', value: 57.24 },
192 | 	{ time: '2019-05-06', value: 56.91 },
193 | 	{ time: '2019-05-07', value: 56.63 },
194 | 	{ time: '2019-05-08', value: 56.38 },
195 | 	{ time: '2019-05-09', value: 56.48 },
196 | 	{ time: '2019-05-10', value: 56.91 },
197 | 	{ time: '2019-05-13', value: 56.75 },
198 | 	{ time: '2019-05-14', value: 56.55 },
199 | 	{ time: '2019-05-15', value: 56.81 },
200 | 	{ time: '2019-05-16', value: 57.38 },
201 | 	{ time: '2019-05-17', value: 58.09 },
202 | 	{ time: '2019-05-20', value: 59.01 },
203 | 	{ time: '2019-05-21', value: 59.50 },
204 | 	{ time: '2019-05-22', value: 59.25 },
205 | 	{ time: '2019-05-23', value: 58.87 },
206 | 	{ time: '2019-05-24', value: 59.32 },
207 | 	{ time: '2019-05-28', value: 59.57 },
208 | 	// hide-end
209 | ]);
210 | 
211 | // setting the data for the volume series.
212 | // note: we are defining each bars color as part of the data
213 | volumeSeries.setData([
214 | 	{ time: '2018-10-19', value: 19103293.00, color: BAR_UP_COLOR },
215 | 	// hide-start
216 | 	{ time: '2018-10-22', value: 21737523.00, color: BAR_UP_COLOR },
217 | 	{ time: '2018-10-23', value: 29328713.00, color: BAR_UP_COLOR },
218 | 	{ time: '2018-10-24', value: 37435638.00, color: BAR_UP_COLOR },
219 | 	{ time: '2018-10-25', value: 25269995.00, color: BAR_DOWN_COLOR },
220 | 	{ time: '2018-10-26', value: 24973311.00, color: BAR_DOWN_COLOR },
221 | 	{ time: '2018-10-29', value: 22103692.00, color: BAR_UP_COLOR },
222 | 	{ time: '2018-10-30', value: 25231199.00, color: BAR_UP_COLOR },
223 | 	{ time: '2018-10-31', value: 24214427.00, color: BAR_DOWN_COLOR },
224 | 	{ time: '2018-11-01', value: 22533201.00, color: BAR_DOWN_COLOR },
225 | 	{ time: '2018-11-02', value: 14734412.00, color: BAR_UP_COLOR },
226 | 	{ time: '2018-11-05', value: 12733842.00, color: BAR_UP_COLOR },
227 | 	{ time: '2018-11-06', value: 12371207.00, color: BAR_UP_COLOR },
228 | 	{ time: '2018-11-07', value: 14891287.00, color: BAR_UP_COLOR },
229 | 	{ time: '2018-11-08', value: 12482392.00, color: BAR_UP_COLOR },
230 | 	{ time: '2018-11-09', value: 17365762.00, color: BAR_UP_COLOR },
231 | 	{ time: '2018-11-12', value: 13236769.00, color: BAR_UP_COLOR },
232 | 	{ time: '2018-11-13', value: 13047907.00, color: BAR_DOWN_COLOR },
233 | 	{ time: '2018-11-14', value: 18288710.00, color: BAR_UP_COLOR },
234 | 	{ time: '2018-11-15', value: 17147123.00, color: BAR_UP_COLOR },
235 | 	{ time: '2018-11-16', value: 19470986.00, color: BAR_UP_COLOR },
236 | 	{ time: '2018-11-19', value: 18405731.00, color: BAR_UP_COLOR },
237 | 	{ time: '2018-11-20', value: 22028957.00, color: BAR_DOWN_COLOR },
238 | 	{ time: '2018-11-21', value: 18482233.00, color: BAR_DOWN_COLOR },
239 | 	{ time: '2018-11-23', value: 7009050.00, color: BAR_DOWN_COLOR },
240 | 	{ time: '2018-11-26', value: 12308876.00, color: BAR_UP_COLOR },
241 | 	{ time: '2018-11-27', value: 14118867.00, color: BAR_UP_COLOR },
242 | 	{ time: '2018-11-28', value: 18662989.00, color: BAR_DOWN_COLOR },
243 | 	{ time: '2018-11-29', value: 14763658.00, color: BAR_DOWN_COLOR },
244 | 	{ time: '2018-11-30', value: 31142818.00, color: BAR_UP_COLOR },
245 | 	{ time: '2018-12-03', value: 27795428.00, color: BAR_DOWN_COLOR },
246 | 	{ time: '2018-12-04', value: 21727411.00, color: BAR_DOWN_COLOR },
247 | 	{ time: '2018-12-06', value: 26880429.00, color: BAR_DOWN_COLOR },
248 | 	{ time: '2018-12-07', value: 16948126.00, color: BAR_DOWN_COLOR },
249 | 	{ time: '2018-12-10', value: 16603356.00, color: BAR_UP_COLOR },
250 | 	{ time: '2018-12-11', value: 14991438.00, color: BAR_UP_COLOR },
251 | 	{ time: '2018-12-12', value: 18892182.00, color: BAR_DOWN_COLOR },
252 | 	{ time: '2018-12-13', value: 15454706.00, color: BAR_DOWN_COLOR },
253 | 	{ time: '2018-12-14', value: 13960870.00, color: BAR_DOWN_COLOR },
254 | 	{ time: '2018-12-17', value: 18902523.00, color: BAR_DOWN_COLOR },
255 | 	{ time: '2018-12-18', value: 18895777.00, color: BAR_DOWN_COLOR },
256 | 	{ time: '2018-12-19', value: 20968473.00, color: BAR_UP_COLOR },
257 | 	{ time: '2018-12-20', value: 26897008.00, color: BAR_DOWN_COLOR },
258 | 	{ time: '2018-12-21', value: 55413082.00, color: BAR_DOWN_COLOR },
259 | 	{ time: '2018-12-24', value: 15077207.00, color: BAR_DOWN_COLOR },
260 | 	{ time: '2018-12-26', value: 17970539.00, color: BAR_UP_COLOR },
261 | 	{ time: '2018-12-27', value: 17530977.00, color: BAR_UP_COLOR },
262 | 	{ time: '2018-12-28', value: 14771641.00, color: BAR_UP_COLOR },
263 | 	{ time: '2018-12-31', value: 15331758.00, color: BAR_UP_COLOR },
264 | 	{ time: '2019-01-02', value: 13969691.00, color: BAR_DOWN_COLOR },
265 | 	{ time: '2019-01-03', value: 19245411.00, color: BAR_UP_COLOR },
266 | 	{ time: '2019-01-04', value: 17035848.00, color: BAR_UP_COLOR },
267 | 	{ time: '2019-01-07', value: 16348982.00, color: BAR_UP_COLOR },
268 | 	{ time: '2019-01-08', value: 21425008.00, color: BAR_UP_COLOR },
269 | 	{ time: '2019-01-09', value: 18136000.00, color: BAR_DOWN_COLOR },
270 | 	{ time: '2019-01-10', value: 14259910.00, color: BAR_UP_COLOR },
271 | 	{ time: '2019-01-11', value: 15801548.00, color: BAR_UP_COLOR },
272 | 	{ time: '2019-01-14', value: 11342293.00, color: BAR_UP_COLOR },
273 | 	{ time: '2019-01-15', value: 10074386.00, color: BAR_UP_COLOR },
274 | 	{ time: '2019-01-16', value: 13411691.00, color: BAR_DOWN_COLOR },
275 | 	{ time: '2019-01-17', value: 15223854.00, color: BAR_DOWN_COLOR },
276 | 	{ time: '2019-01-18', value: 16802516.00, color: BAR_UP_COLOR },
277 | 	{ time: '2019-01-22', value: 18284771.00, color: BAR_DOWN_COLOR },
278 | 	{ time: '2019-01-23', value: 15109007.00, color: BAR_UP_COLOR },
279 | 	{ time: '2019-01-24', value: 12494109.00, color: BAR_DOWN_COLOR },
280 | 	{ time: '2019-01-25', value: 17806822.00, color: BAR_DOWN_COLOR },
281 | 	{ time: '2019-01-28', value: 25955718.00, color: BAR_DOWN_COLOR },
282 | 	{ time: '2019-01-29', value: 33789235.00, color: BAR_DOWN_COLOR },
283 | 	{ time: '2019-01-30', value: 27260036.00, color: BAR_UP_COLOR },
284 | 	{ time: '2019-01-31', value: 28585447.00, color: BAR_UP_COLOR },
285 | 	{ time: '2019-02-01', value: 13778392.00, color: BAR_DOWN_COLOR },
286 | 	{ time: '2019-02-04', value: 15818901.00, color: BAR_DOWN_COLOR },
287 | 	{ time: '2019-02-05', value: 14124794.00, color: BAR_UP_COLOR },
288 | 	{ time: '2019-02-06', value: 11391442.00, color: BAR_DOWN_COLOR },
289 | 	{ time: '2019-02-07', value: 12436168.00, color: BAR_DOWN_COLOR },
290 | 	{ time: '2019-02-08', value: 12011657.00, color: BAR_UP_COLOR },
291 | 	{ time: '2019-02-11', value: 9802798.00, color: BAR_UP_COLOR },
292 | 	{ time: '2019-02-12', value: 11227550.00, color: BAR_UP_COLOR },
293 | 	{ time: '2019-02-13', value: 11884803.00, color: BAR_UP_COLOR },
294 | 	{ time: '2019-02-14', value: 11190094.00, color: BAR_DOWN_COLOR },
295 | 	{ time: '2019-02-15', value: 15719416.00, color: BAR_UP_COLOR },
296 | 	{ time: '2019-02-19', value: 12272877.00, color: BAR_UP_COLOR },
297 | 	{ time: '2019-02-20', value: 11379006.00, color: BAR_UP_COLOR },
298 | 	{ time: '2019-02-21', value: 14680547.00, color: BAR_UP_COLOR },
299 | 	{ time: '2019-02-22', value: 12534431.00, color: BAR_UP_COLOR },
300 | 	{ time: '2019-02-25', value: 15051182.00, color: BAR_DOWN_COLOR },
301 | 	{ time: '2019-02-26', value: 12005571.00, color: BAR_DOWN_COLOR },
302 | 	{ time: '2019-02-27', value: 8962776.00, color: BAR_UP_COLOR },
303 | 	{ time: '2019-02-28', value: 15742971.00, color: BAR_UP_COLOR },
304 | 	{ time: '2019-03-01', value: 10942737.00, color: BAR_UP_COLOR },
305 | 	{ time: '2019-03-04', value: 13674737.00, color: BAR_DOWN_COLOR },
306 | 	{ time: '2019-03-05', value: 15749545.00, color: BAR_DOWN_COLOR },
307 | 	{ time: '2019-03-06', value: 13935530.00, color: BAR_DOWN_COLOR },
308 | 	{ time: '2019-03-07', value: 12644171.00, color: BAR_UP_COLOR },
309 | 	{ time: '2019-03-08', value: 10646710.00, color: BAR_UP_COLOR },
310 | 	{ time: '2019-03-11', value: 13627431.00, color: BAR_UP_COLOR },
311 | 	{ time: '2019-03-12', value: 12812980.00, color: BAR_DOWN_COLOR },
312 | 	{ time: '2019-03-13', value: 14168350.00, color: BAR_UP_COLOR },
313 | 	{ time: '2019-03-14', value: 12148349.00, color: BAR_UP_COLOR },
314 | 	{ time: '2019-03-15', value: 23715337.00, color: BAR_UP_COLOR },
315 | 	{ time: '2019-03-18', value: 12168133.00, color: BAR_DOWN_COLOR },
316 | 	{ time: '2019-03-19', value: 13462686.00, color: BAR_DOWN_COLOR },
317 | 	{ time: '2019-03-20', value: 11903104.00, color: BAR_UP_COLOR },
318 | 	{ time: '2019-03-21', value: 10920129.00, color: BAR_UP_COLOR },
319 | 	{ time: '2019-03-22', value: 25125385.00, color: BAR_UP_COLOR },
320 | 	{ time: '2019-03-25', value: 15463411.00, color: BAR_UP_COLOR },
321 | 	{ time: '2019-03-26', value: 12316901.00, color: BAR_UP_COLOR },
322 | 	{ time: '2019-03-27', value: 13290298.00, color: BAR_UP_COLOR },
323 | 	{ time: '2019-03-28', value: 20547060.00, color: BAR_DOWN_COLOR },
324 | 	{ time: '2019-03-29', value: 17283871.00, color: BAR_UP_COLOR },
325 | 	{ time: '2019-04-01', value: 16331140.00, color: BAR_DOWN_COLOR },
326 | 	{ time: '2019-04-02', value: 11408146.00, color: BAR_DOWN_COLOR },
327 | 	{ time: '2019-04-03', value: 15491724.00, color: BAR_UP_COLOR },
328 | 	{ time: '2019-04-04', value: 8776028.00, color: BAR_UP_COLOR },
329 | 	{ time: '2019-04-05', value: 11497780.00, color: BAR_UP_COLOR },
330 | 	{ time: '2019-04-08', value: 11680538.00, color: BAR_UP_COLOR },
331 | 	{ time: '2019-04-09', value: 10414416.00, color: BAR_DOWN_COLOR },
332 | 	{ time: '2019-04-10', value: 8782061.00, color: BAR_UP_COLOR },
333 | 	{ time: '2019-04-11', value: 9219930.00, color: BAR_DOWN_COLOR },
334 | 	{ time: '2019-04-12', value: 10847504.00, color: BAR_UP_COLOR },
335 | 	{ time: '2019-04-15', value: 7741472.00, color: BAR_DOWN_COLOR },
336 | 	{ time: '2019-04-16', value: 10239261.00, color: BAR_UP_COLOR },
337 | 	{ time: '2019-04-17', value: 15498037.00, color: BAR_DOWN_COLOR },
338 | 	{ time: '2019-04-18', value: 13189013.00, color: BAR_UP_COLOR },
339 | 	{ time: '2019-04-22', value: 11950365.00, color: BAR_UP_COLOR },
340 | 	{ time: '2019-04-23', value: 23488682.00, color: BAR_DOWN_COLOR },
341 | 	{ time: '2019-04-24', value: 13227084.00, color: BAR_DOWN_COLOR },
342 | 	{ time: '2019-04-25', value: 17425466.00, color: BAR_DOWN_COLOR },
343 | 	{ time: '2019-04-26', value: 16329727.00, color: BAR_UP_COLOR },
344 | 	{ time: '2019-04-29', value: 13984965.00, color: BAR_UP_COLOR },
345 | 	{ time: '2019-04-30', value: 15469002.00, color: BAR_UP_COLOR },
346 | 	{ time: '2019-05-01', value: 11627436.00, color: BAR_DOWN_COLOR },
347 | 	{ time: '2019-05-02', value: 14435436.00, color: BAR_UP_COLOR },
348 | 	{ time: '2019-05-03', value: 9388228.00, color: BAR_UP_COLOR },
349 | 	{ time: '2019-05-06', value: 10066145.00, color: BAR_DOWN_COLOR },
350 | 	{ time: '2019-05-07', value: 12963827.00, color: BAR_DOWN_COLOR },
351 | 	{ time: '2019-05-08', value: 12086743.00, color: BAR_DOWN_COLOR },
352 | 	{ time: '2019-05-09', value: 14835326.00, color: BAR_UP_COLOR },
353 | 	{ time: '2019-05-10', value: 10707335.00, color: BAR_UP_COLOR },
354 | 	{ time: '2019-05-13', value: 13759350.00, color: BAR_DOWN_COLOR },
355 | 	{ time: '2019-05-14', value: 12776175.00, color: BAR_DOWN_COLOR },
356 | 	{ time: '2019-05-15', value: 10806379.00, color: BAR_UP_COLOR },
357 | 	{ time: '2019-05-16', value: 11695064.00, color: BAR_UP_COLOR },
358 | 	{ time: '2019-05-17', value: 14436662.00, color: BAR_UP_COLOR },
359 | 	{ time: '2019-05-20', value: 20910590.00, color: BAR_UP_COLOR },
360 | 	{ time: '2019-05-21', value: 14016315.00, color: BAR_UP_COLOR },
361 | 	{ time: '2019-05-22', value: 11487448.00, color: BAR_DOWN_COLOR },
362 | 	{ time: '2019-05-23', value: 11707083.00, color: BAR_DOWN_COLOR },
363 | 	{ time: '2019-05-24', value: 8755506.00, color: BAR_UP_COLOR },
364 | 	{ time: '2019-05-28', value: 3097125.00, color: BAR_UP_COLOR },
365 | 	// hide-end
366 | ]);
367 | 
368 | chart.timeScale().fitContent();
369 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/price-and-volume.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | title: Price and volume on a single chart
  3 | sidebar_label: Price and Volume
  4 | description: An example of how to include both price and volume series on a single chart.
  5 | pagination_prev: null
  6 | pagination_next: null
  7 | keywords:
  8 |   - example
  9 | ---
 10 | 
 11 | import VersionWarningAdmonition from "@site/src/components/VersionWarningAdmonition";
 12 | 
 13 | {/*
 14 |   Show warning when not on the latest published version
 15 |   Tutorials section isn't versioned yet, hence the need for the warning message
 16 |   THESE TUTORIALS NEED TO BE UPDATED FOR VERSION 4
 17 | */}
 18 | 
 19 | <VersionWarningAdmonition
 20 | 	notCurrent="This example is for the latest published version of Lightweight Charts."
 21 | 	type="caution"
 22 | 	displayVersionMessage
 23 | />
 24 | 
 25 | This example shows how to include a volume study on your chart.
 26 | 
 27 | ## How to add a volume histogram
 28 | 
 29 | An additional series can be added to a chart as an 'overlay' by setting the series'
 30 | [`priceScaleId`](/docs/api/interfaces/SeriesOptionsCommon#pricescaleid) to `''`.
 31 | An overlay doesn't make use of either the left or right price scale, and it's positioning
 32 | is controlled by setting the [`scaleMargins`](/docs/api/interfaces/PriceScaleOptions#scalemargins)
 33 | property on the price scale options associated with the series.
 34 | 
 35 | ```js
 36 | const volumeSeries = chart.addSeries(HistogramSeries, {
 37 |     priceFormat: {
 38 |         type: 'volume',
 39 |     },
 40 |     priceScaleId: '', // set as an overlay by setting a blank priceScaleId
 41 | });
 42 | volumeSeries.priceScale().applyOptions({
 43 |     // set the positioning of the volume series
 44 |     scaleMargins: {
 45 |         top: 0.7, // highest point of the series will be 70% away from the top
 46 |         bottom: 0,
 47 |     },
 48 | });
 49 | ```
 50 | 
 51 | We are using the [Histogram](/docs/series-types#histogram) series type to draw the volume bars.
 52 | We can set the `priceFormat` option to `'volume'` to have the values display correctly within
 53 | the crosshair line label.
 54 | 
 55 | We adjust the position of the overlay series to the bottom 30% of the chart by
 56 | setting the [`scaleMargins`](/docs/api/interfaces/PriceScaleOptions#scalemargins) properties as follows:
 57 | 
 58 | ```js
 59 | volumeSeries.priceScale().applyOptions({
 60 |     scaleMargins: {
 61 |         top: 0.7, // highest point of the series will be 70% away from the top
 62 |         bottom: 0, // lowest point will be at the very bottom.
 63 |     },
 64 | });
 65 | ```
 66 | 
 67 | Similarly, we can set the position of the main series using the same approach. By setting
 68 | the `bottom` margin value to `0.4` we can ensure that the two series don't overlap each other.
 69 | 
 70 | ```js
 71 | mainSeries.priceScale().applyOptions({
 72 |     scaleMargins: {
 73 |         top: 0.1, // highest point of the series will be 10% away from the top
 74 |         bottom: 0.4, // lowest point will be 40% away from the bottom
 75 |     },
 76 | });
 77 | ```
 78 | 
 79 | We can control the color of the histogram bars by directly specifying color inside
 80 | the data set.
 81 | 
 82 | ```js
 83 | histogramSeries.setData([
 84 |     { time: '2018-10-19', value: 19103293.0, color: 'green' },
 85 |     { time: '2018-10-20', value: 20345000.0, color: 'red' },
 86 | ]);
 87 | ```
 88 | 
 89 | You can see a full [working example](#full-example) below.
 90 | 
 91 | ## Resources
 92 | 
 93 | - [OverlayPriceScale Options](/docs/api/type-aliases/OverlayPriceScaleOptions)
 94 | - [Histogram Series Type](/docs/series-types#histogram)
 95 | - [PriceFormat Types](/docs/api/interfaces/PriceFormatBuiltIn#type)
 96 | - [Scale Margins](/docs/api/interfaces/PriceScaleOptions#scalemargins)
 97 | 
 98 | ## Full example
 99 | 
100 | import UsageGuidePartial from "../_usage-guide-partial.mdx";
101 | import CodeBlock from "@theme/CodeBlock";
102 | import code from "!!raw-loader!./price-and-volume.js";
103 | 
104 | <CodeBlock replaceThemeConstants chart className="language-js" hideableCode chartOnTop codeUsage={<UsageGuidePartial />}>
105 | 	{code}
106 | </CodeBlock>
107 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/price-line.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Price Lines
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/how_to/price-line
  4 | 
  5 | // remove-end
  6 | const chartOptions = {
  7 | 	layout: {
  8 | 		textColor: CHART_TEXT_COLOR,
  9 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
 10 | 	},
 11 | };
 12 | // remove-line
 13 | /** @type {import('lightweight-charts').IChartApi} */
 14 | const chart = createChart(document.getElementById('container'), chartOptions);
 15 | 
 16 | const series = chart.addSeries(LineSeries, {
 17 | 	color: LINE_LINE_COLOR,
 18 | 	lineWidth: 2,
 19 | 	// highlight-start
 20 | 	// disabling built-in price lines
 21 | 	lastValueVisible: false,
 22 | 	priceLineVisible: false,
 23 | 	// highlight-end
 24 | });
 25 | 
 26 | const data = [
 27 | 	{ time: { year: 2018, month: 1, day: 1 }, value: 27.58405298746434 },
 28 | 	// hide-start
 29 | 	{ time: { year: 2018, month: 1, day: 2 }, value: 31.74088841431117 },
 30 | 	{ time: { year: 2018, month: 1, day: 3 }, value: 35.892978753808926 },
 31 | 	{ time: { year: 2018, month: 1, day: 4 }, value: 39.63642029045179 },
 32 | 	{ time: { year: 2018, month: 1, day: 5 }, value: 40.79167357702531 },
 33 | 	{ time: { year: 2018, month: 1, day: 6 }, value: 47.691740220947764 },
 34 | 	{ time: { year: 2018, month: 1, day: 7 }, value: 49.377161099825415 },
 35 | 	{ time: { year: 2018, month: 1, day: 8 }, value: 52.47379203136591 },
 36 | 	{ time: { year: 2018, month: 1, day: 9 }, value: 50.40209743179448 },
 37 | 	{ time: { year: 2018, month: 1, day: 10 }, value: 61.47316837848548 },
 38 | 	{ time: { year: 2018, month: 1, day: 11 }, value: 58.22831552141069 },
 39 | 	{ time: { year: 2018, month: 1, day: 12 }, value: 59.36868132891698 },
 40 | 	{ time: { year: 2018, month: 1, day: 13 }, value: 62.10845687168416 },
 41 | 	{ time: { year: 2018, month: 1, day: 14 }, value: 51.259701958506724 },
 42 | 	{ time: { year: 2018, month: 1, day: 15 }, value: 56.247578870411644 },
 43 | 	{ time: { year: 2018, month: 1, day: 16 }, value: 55.483307642385164 },
 44 | 	{ time: { year: 2018, month: 1, day: 17 }, value: 55.85295564734231 },
 45 | 	{ time: { year: 2018, month: 1, day: 18 }, value: 48.3138216778343 },
 46 | 	{ time: { year: 2018, month: 1, day: 19 }, value: 53.071901176203866 },
 47 | 	{ time: { year: 2018, month: 1, day: 20 }, value: 50.873781097281885 },
 48 | 	{ time: { year: 2018, month: 1, day: 21 }, value: 49.7840315054249 },
 49 | 	{ time: { year: 2018, month: 1, day: 22 }, value: 52.34956807336156 },
 50 | 	{ time: { year: 2018, month: 1, day: 23 }, value: 53.79112543285674 },
 51 | 	{ time: { year: 2018, month: 1, day: 24 }, value: 53.984887985424805 },
 52 | 	{ time: { year: 2018, month: 1, day: 25 }, value: 58.56902893497121 },
 53 | 	{ time: { year: 2018, month: 1, day: 26 }, value: 54.76191372282466 },
 54 | 	{ time: { year: 2018, month: 1, day: 27 }, value: 63.38042554684846 },
 55 | 	{ time: { year: 2018, month: 1, day: 28 }, value: 55.452618512103065 },
 56 | 	{ time: { year: 2018, month: 1, day: 29 }, value: 65.60820758942769 },
 57 | 	{ time: { year: 2018, month: 1, day: 30 }, value: 56.82795136583009 },
 58 | 	{ time: { year: 2018, month: 1, day: 31 }, value: 70.3148022984224 },
 59 | 	{ time: { year: 2018, month: 2, day: 1 }, value: 65.86230944167264 },
 60 | 	{ time: { year: 2018, month: 2, day: 2 }, value: 72.05467846676524 },
 61 | 	{ time: { year: 2018, month: 2, day: 3 }, value: 72.99238887850564 },
 62 | 	{ time: { year: 2018, month: 2, day: 4 }, value: 67.03373730222785 },
 63 | 	{ time: { year: 2018, month: 2, day: 5 }, value: 69.97670934736414 },
 64 | 	{ time: { year: 2018, month: 2, day: 6 }, value: 73.08910595492105 },
 65 | 	{ time: { year: 2018, month: 2, day: 7 }, value: 81.43976528732057 },
 66 | 	{ time: { year: 2018, month: 2, day: 8 }, value: 73.62230936920984 },
 67 | 	{ time: { year: 2018, month: 2, day: 9 }, value: 82.15522801870938 },
 68 | 	{ time: { year: 2018, month: 2, day: 10 }, value: 77.99384538574678 },
 69 | 	{ time: { year: 2018, month: 2, day: 11 }, value: 85.62489628897463 },
 70 | 	{ time: { year: 2018, month: 2, day: 12 }, value: 86.93090666568217 },
 71 | 	{ time: { year: 2018, month: 2, day: 13 }, value: 75.99689788850394 },
 72 | 	{ time: { year: 2018, month: 2, day: 14 }, value: 88.46418548355727 },
 73 | 	{ time: { year: 2018, month: 2, day: 15 }, value: 86.20760396539865 },
 74 | 	{ time: { year: 2018, month: 2, day: 16 }, value: 81.88757639758437 },
 75 | 	{ time: { year: 2018, month: 2, day: 17 }, value: 79.58151786389108 },
 76 | 	{ time: { year: 2018, month: 2, day: 18 }, value: 80.96845249711073 },
 77 | 	{ time: { year: 2018, month: 2, day: 19 }, value: 73.54901807055447 },
 78 | 	{ time: { year: 2018, month: 2, day: 20 }, value: 75.65626118347262 },
 79 | 	{ time: { year: 2018, month: 2, day: 21 }, value: 78.41307347680399 },
 80 | 	{ time: { year: 2018, month: 2, day: 22 }, value: 74.60352602043042 },
 81 | 	{ time: { year: 2018, month: 2, day: 23 }, value: 72.28241570381236 },
 82 | 	{ time: { year: 2018, month: 2, day: 24 }, value: 72.24427397962566 },
 83 | 	{ time: { year: 2018, month: 2, day: 25 }, value: 64.80996965592134 },
 84 | 	{ time: { year: 2018, month: 2, day: 26 }, value: 67.37511361319652 },
 85 | 	{ time: { year: 2018, month: 2, day: 27 }, value: 65.5449131917524 },
 86 | 	{ time: { year: 2018, month: 2, day: 28 }, value: 65.4802711362433 },
 87 | 	{ time: { year: 2018, month: 3, day: 1 }, value: 62.207767815581086 },
 88 | 	{ time: { year: 2018, month: 3, day: 2 }, value: 59.78884720470812 },
 89 | 	{ time: { year: 2018, month: 3, day: 3 }, value: 67.51846586137782 },
 90 | 	{ time: { year: 2018, month: 3, day: 4 }, value: 68.752834400291 },
 91 | 	{ time: { year: 2018, month: 3, day: 5 }, value: 66.63416073573323 },
 92 | 	{ time: { year: 2018, month: 3, day: 6 }, value: 65.58601621691751 },
 93 | 	{ time: { year: 2018, month: 3, day: 7 }, value: 57.33498792621458 },
 94 | 	{ time: { year: 2018, month: 3, day: 8 }, value: 56.93436946311955 },
 95 | 	{ time: { year: 2018, month: 3, day: 9 }, value: 58.31144672902557 },
 96 | 	{ time: { year: 2018, month: 3, day: 10 }, value: 59.96407207657268 },
 97 | 	{ time: { year: 2018, month: 3, day: 11 }, value: 55.7861486424976 },
 98 | 	{ time: { year: 2018, month: 3, day: 12 }, value: 52.91803500214551 },
 99 | 	{ time: { year: 2018, month: 3, day: 13 }, value: 54.491591573038306 },
100 | 	{ time: { year: 2018, month: 3, day: 14 }, value: 51.924409342593385 },
101 | 	{ time: { year: 2018, month: 3, day: 15 }, value: 41.90263950118436 },
102 | 	{ time: { year: 2018, month: 3, day: 16 }, value: 40.514436076485694 },
103 | 	{ time: { year: 2018, month: 3, day: 17 }, value: 41.065887666854486 },
104 | 	{ time: { year: 2018, month: 3, day: 18 }, value: 40.44445534031683 },
105 | 	{ time: { year: 2018, month: 3, day: 19 }, value: 42.13922977216152 },
106 | 	{ time: { year: 2018, month: 3, day: 20 }, value: 42.317162952084495 },
107 | 	{ time: { year: 2018, month: 3, day: 21 }, value: 39.02881877743751 },
108 | 	{ time: { year: 2018, month: 3, day: 22 }, value: 39.81917993955704 },
109 | 	{ time: { year: 2018, month: 3, day: 23 }, value: 36.753197056053374 },
110 | 	{ time: { year: 2018, month: 3, day: 24 }, value: 37.02203306330588 },
111 | 	{ time: { year: 2018, month: 3, day: 25 }, value: 36.36014042161194 },
112 | 	{ time: { year: 2018, month: 3, day: 26 }, value: 33.56275879100148 },
113 | 	{ time: { year: 2018, month: 3, day: 27 }, value: 34.39112540787079 },
114 | 	{ time: { year: 2018, month: 3, day: 28 }, value: 30.57170225544929 },
115 | 	{ time: { year: 2018, month: 3, day: 29 }, value: 33.56826040802756 },
116 | 	{ time: { year: 2018, month: 3, day: 30 }, value: 32.89895543218274 },
117 | 	{ time: { year: 2018, month: 3, day: 31 }, value: 31.015658561825738 },
118 | 	{ time: { year: 2018, month: 4, day: 1 }, value: 33.189179815787455 },
119 | 	{ time: { year: 2018, month: 4, day: 2 }, value: 29.530756945582162 },
120 | 	{ time: { year: 2018, month: 4, day: 3 }, value: 29.250978140719916 },
121 | 	{ time: { year: 2018, month: 4, day: 4 }, value: 27.89635178919736 },
122 | 	{ time: { year: 2018, month: 4, day: 5 }, value: 26.995427160624686 },
123 | 	{ time: { year: 2018, month: 4, day: 6 }, value: 25.89631885043023 },
124 | 	{ time: { year: 2018, month: 4, day: 7 }, value: 28.71812492475548 },
125 | 	{ time: { year: 2018, month: 4, day: 8 }, value: 23.56476085365468 },
126 | 	{ time: { year: 2018, month: 4, day: 9 }, value: 23.8550787876547 },
127 | 	{ time: { year: 2018, month: 4, day: 10 }, value: 23.27046572075657 },
128 | 	{ time: { year: 2018, month: 4, day: 11 }, value: 25.73099630369951 },
129 | 	{ time: { year: 2018, month: 4, day: 12 }, value: 23.398760738394646 },
130 | 	{ time: { year: 2018, month: 4, day: 13 }, value: 22.97970501784193 },
131 | 	{ time: { year: 2018, month: 4, day: 14 }, value: 22.145587244500526 },
132 | 	{ time: { year: 2018, month: 4, day: 15 }, value: 20.622578956226192 },
133 | 	{ time: { year: 2018, month: 4, day: 16 }, value: 21.99297423796017 },
134 | 	{ time: { year: 2018, month: 4, day: 17 }, value: 20.756081302371527 },
135 | 	{ time: { year: 2018, month: 4, day: 18 }, value: 18.1983338834302 },
136 | 	{ time: { year: 2018, month: 4, day: 19 }, value: 16.419404563645198 },
137 | 	{ time: { year: 2018, month: 4, day: 20 }, value: 18.38192363882247 },
138 | 	{ time: { year: 2018, month: 4, day: 21 }, value: 17.41452255210322 },
139 | 	{ time: { year: 2018, month: 4, day: 22 }, value: 17.39866711593896 },
140 | 	{ time: { year: 2018, month: 4, day: 23 }, value: 14.859371316920733 },
141 | 	{ time: { year: 2018, month: 4, day: 24 }, value: 14.49488592297959 },
142 | 	{ time: { year: 2018, month: 4, day: 25 }, value: 14.183858665721397 },
143 | 	{ time: { year: 2018, month: 4, day: 26 }, value: 12.754187935636056 },
144 | 	{ time: { year: 2018, month: 4, day: 27 }, value: 14.467536059608742 },
145 | 	{ time: { year: 2018, month: 4, day: 28 }, value: 14.72962730689032 },
146 | 	{ time: { year: 2018, month: 4, day: 29 }, value: 16.591675981296518 },
147 | 	{ time: { year: 2018, month: 4, day: 30 }, value: 17.560385679284135 },
148 | 	{ time: { year: 2018, month: 5, day: 1 }, value: 22.386250317504064 },
149 | 	{ time: { year: 2018, month: 5, day: 2 }, value: 23.697029442697385 },
150 | 	{ time: { year: 2018, month: 5, day: 3 }, value: 23.453148128592442 },
151 | 	{ time: { year: 2018, month: 5, day: 4 }, value: 23.164700105036882 },
152 | 	{ time: { year: 2018, month: 5, day: 5 }, value: 23.919034678006323 },
153 | 	{ time: { year: 2018, month: 5, day: 6 }, value: 25.18353870528509 },
154 | 	{ time: { year: 2018, month: 5, day: 7 }, value: 26.982824465076394 },
155 | 	{ time: { year: 2018, month: 5, day: 8 }, value: 29.122512185000712 },
156 | 	{ time: { year: 2018, month: 5, day: 9 }, value: 29.60160406576696 },
157 | 	{ time: { year: 2018, month: 5, day: 10 }, value: 30.845749384528016 },
158 | 	{ time: { year: 2018, month: 5, day: 11 }, value: 33.03296938636202 },
159 | 	{ time: { year: 2018, month: 5, day: 12 }, value: 33.784707082446104 },
160 | 	{ time: { year: 2018, month: 5, day: 13 }, value: 36.08545410406137 },
161 | 	{ time: { year: 2018, month: 5, day: 14 }, value: 36.80597815439238 },
162 | 	{ time: { year: 2018, month: 5, day: 15 }, value: 34.56062188644443 },
163 | 	{ time: { year: 2018, month: 5, day: 16 }, value: 36.52666657165473 },
164 | 	{ time: { year: 2018, month: 5, day: 17 }, value: 34.76705735297833 },
165 | 	{ time: { year: 2018, month: 5, day: 18 }, value: 39.01598033743525 },
166 | 	{ time: { year: 2018, month: 5, day: 19 }, value: 37.60979560604685 },
167 | 	{ time: { year: 2018, month: 5, day: 20 }, value: 42.403895121650436 },
168 | 	{ time: { year: 2018, month: 5, day: 21 }, value: 45.55998014298455 },
169 | 	{ time: { year: 2018, month: 5, day: 22 }, value: 39.76704752577289 },
170 | 	{ time: { year: 2018, month: 5, day: 23 }, value: 41.83196178430985 },
171 | 	{ time: { year: 2018, month: 5, day: 24 }, value: 46.99399105885453 },
172 | 	{ time: { year: 2018, month: 5, day: 25 }, value: 48.553566318637984 },
173 | 	{ time: { year: 2018, month: 5, day: 26 }, value: 48.918166891087594 },
174 | 	{ time: { year: 2018, month: 5, day: 27 }, value: 42.95391588314584 },
175 | 	{ time: { year: 2018, month: 5, day: 28 }, value: 51.267649950057546 },
176 | 	{ time: { year: 2018, month: 5, day: 29 }, value: 44.86104374986037 },
177 | 	{ time: { year: 2018, month: 5, day: 30 }, value: 46.7183564731453 },
178 | 	{ time: { year: 2018, month: 5, day: 31 }, value: 52.753001379260766 },
179 | 	{ time: { year: 2018, month: 6, day: 1 }, value: 56.04835638442964 },
180 | 	{ time: { year: 2018, month: 6, day: 2 }, value: 54.82119793390652 },
181 | 	{ time: { year: 2018, month: 6, day: 3 }, value: 57.718938021257685 },
182 | 	{ time: { year: 2018, month: 6, day: 4 }, value: 53.9914459224653 },
183 | 	{ time: { year: 2018, month: 6, day: 5 }, value: 59.33050624063286 },
184 | 	{ time: { year: 2018, month: 6, day: 6 }, value: 50.79074268713266 },
185 | 	{ time: { year: 2018, month: 6, day: 7 }, value: 53.15657316197036 },
186 | 	{ time: { year: 2018, month: 6, day: 8 }, value: 59.43675134021954 },
187 | 	{ time: { year: 2018, month: 6, day: 9 }, value: 63.28437595760727 },
188 | 	{ time: { year: 2018, month: 6, day: 10 }, value: 58.07099287435428 },
189 | 	{ time: { year: 2018, month: 6, day: 11 }, value: 56.68728978119396 },
190 | 	{ time: { year: 2018, month: 6, day: 12 }, value: 57.05079700873323 },
191 | 	{ time: { year: 2018, month: 6, day: 13 }, value: 65.65087785161663 },
192 | 	{ time: { year: 2018, month: 6, day: 14 }, value: 59.20877581396441 },
193 | 	{ time: { year: 2018, month: 6, day: 15 }, value: 64.30200099280857 },
194 | 	{ time: { year: 2018, month: 6, day: 16 }, value: 68.60774992100288 },
195 | 	{ time: { year: 2018, month: 6, day: 17 }, value: 67.16628680993453 },
196 | 	{ time: { year: 2018, month: 6, day: 18 }, value: 62.89644591741811 },
197 | 	{ time: { year: 2018, month: 6, day: 19 }, value: 61.42888198118138 },
198 | 	{ time: { year: 2018, month: 6, day: 20 }, value: 64.89813095653885 },
199 | 	{ time: { year: 2018, month: 6, day: 21 }, value: 72.72701573552945 },
200 | 	{ time: { year: 2018, month: 6, day: 22 }, value: 67.85006296129148 },
201 | 	{ time: { year: 2018, month: 6, day: 23 }, value: 74.8567814889 },
202 | 	{ time: { year: 2018, month: 6, day: 24 }, value: 66.24228046316296 },
203 | 	{ time: { year: 2018, month: 6, day: 25 }, value: 68.09192660329269 },
204 | 	{ time: { year: 2018, month: 6, day: 26 }, value: 75.30075953672075 },
205 | 	{ time: { year: 2018, month: 6, day: 27 }, value: 68.7478054620306 },
206 | 	{ time: { year: 2018, month: 6, day: 28 }, value: 76.2285023801364 },
207 | 	{ time: { year: 2018, month: 6, day: 29 }, value: 82.945167109736 },
208 | 	{ time: { year: 2018, month: 6, day: 30 }, value: 76.91811779365663 },
209 | 	{ time: { year: 2018, month: 7, day: 1 }, value: 73.4904875247808 },
210 | 	{ time: { year: 2018, month: 7, day: 2 }, value: 78.37882382739707 },
211 | 	{ time: { year: 2018, month: 7, day: 3 }, value: 77.00224598364632 },
212 | 	{ time: { year: 2018, month: 7, day: 4 }, value: 74.96345662377028 },
213 | 	{ time: { year: 2018, month: 7, day: 5 }, value: 85.54303380001907 },
214 | 	{ time: { year: 2018, month: 7, day: 6 }, value: 74.23916926437794 },
215 | 	{ time: { year: 2018, month: 7, day: 7 }, value: 86.38109732705232 },
216 | 	{ time: { year: 2018, month: 7, day: 8 }, value: 88.36203657839357 },
217 | 	{ time: { year: 2018, month: 7, day: 9 }, value: 81.63303116061893 },
218 | 	{ time: { year: 2018, month: 7, day: 10 }, value: 78.05188105610182 },
219 | 	{ time: { year: 2018, month: 7, day: 11 }, value: 93.73294498110195 },
220 | 	{ time: { year: 2018, month: 7, day: 12 }, value: 86.3226018109303 },
221 | 	{ time: { year: 2018, month: 7, day: 13 }, value: 83.18571530136985 },
222 | 	{ time: { year: 2018, month: 7, day: 14 }, value: 92.45097319531271 },
223 | 	{ time: { year: 2018, month: 7, day: 15 }, value: 82.61971871486392 },
224 | 	{ time: { year: 2018, month: 7, day: 16 }, value: 84.39935112744469 },
225 | 	{ time: { year: 2018, month: 7, day: 17 }, value: 86.84420907417798 },
226 | 	{ time: { year: 2018, month: 7, day: 18 }, value: 81.50766784637338 },
227 | 	{ time: { year: 2018, month: 7, day: 19 }, value: 88.74841709228694 },
228 | 	{ time: { year: 2018, month: 7, day: 20 }, value: 85.84190975050336 },
229 | 	{ time: { year: 2018, month: 7, day: 21 }, value: 86.9594938103096 },
230 | 	{ time: { year: 2018, month: 7, day: 22 }, value: 83.72572564120199 },
231 | 	{ time: { year: 2018, month: 7, day: 23 }, value: 83.42754326770913 },
232 | 	{ time: { year: 2018, month: 7, day: 24 }, value: 80.40755818165856 },
233 | 	{ time: { year: 2018, month: 7, day: 25 }, value: 81.40515523172276 },
234 | 	{ time: { year: 2018, month: 7, day: 26 }, value: 88.6671912474792 },
235 | 	{ time: { year: 2018, month: 7, day: 27 }, value: 83.98197434091429 },
236 | 	{ time: { year: 2018, month: 7, day: 28 }, value: 79.93747419607003 },
237 | 	{ time: { year: 2018, month: 7, day: 29 }, value: 88.74666581089701 },
238 | 	{ time: { year: 2018, month: 7, day: 30 }, value: 88.4887222568271 },
239 | 	{ time: { year: 2018, month: 7, day: 31 }, value: 91.70282162754224 },
240 | 	{ time: { year: 2018, month: 8, day: 1 }, value: 81.82327312829118 },
241 | 	{ time: { year: 2018, month: 8, day: 2 }, value: 89.56625546634567 },
242 | 	{ time: { year: 2018, month: 8, day: 3 }, value: 83.60742160062637 },
243 | 	{ time: { year: 2018, month: 8, day: 4 }, value: 92.16271144958857 },
244 | 	{ time: { year: 2018, month: 8, day: 5 }, value: 92.93451790057534 },
245 | 	{ time: { year: 2018, month: 8, day: 6 }, value: 97.10629615852636 },
246 | 	{ time: { year: 2018, month: 8, day: 7 }, value: 93.18989484413193 },
247 | 	{ time: { year: 2018, month: 8, day: 8 }, value: 99.52744238602173 },
248 | 	{ time: { year: 2018, month: 8, day: 9 }, value: 90.84973685659028 },
249 | 	{ time: { year: 2018, month: 8, day: 10 }, value: 98.37517814040118 },
250 | 	{ time: { year: 2018, month: 8, day: 11 }, value: 90.13525425607658 },
251 | 	{ time: { year: 2018, month: 8, day: 12 }, value: 95.55125798221395 },
252 | 	{ time: { year: 2018, month: 8, day: 13 }, value: 82.77346455876308 },
253 | 	{ time: { year: 2018, month: 8, day: 14 }, value: 83.24854499361042 },
254 | 	{ time: { year: 2018, month: 8, day: 15 }, value: 95.41999231944423 },
255 | 	{ time: { year: 2018, month: 8, day: 16 }, value: 93.80228527345439 },
256 | 	{ time: { year: 2018, month: 8, day: 17 }, value: 95.6453232668047 },
257 | 	{ time: { year: 2018, month: 8, day: 18 }, value: 85.15427147925779 },
258 | 	{ time: { year: 2018, month: 8, day: 19 }, value: 84.96447951638784 },
259 | 	{ time: { year: 2018, month: 8, day: 20 }, value: 95.92739640648459 },
260 | 	{ time: { year: 2018, month: 8, day: 21 }, value: 96.44143870862634 },
261 | 	{ time: { year: 2018, month: 8, day: 22 }, value: 101.23323393804354 },
262 | 	{ time: { year: 2018, month: 8, day: 23 }, value: 92.12092707164649 },
263 | 	{ time: { year: 2018, month: 8, day: 24 }, value: 101.74117610271144 },
264 | 	{ time: { year: 2018, month: 8, day: 25 }, value: 96.38311956379351 },
265 | 	{ time: { year: 2018, month: 8, day: 26 }, value: 98.18485692799554 },
266 | 	{ time: { year: 2018, month: 8, day: 27 }, value: 102.60080903938159 },
267 | 	{ time: { year: 2018, month: 8, day: 28 }, value: 97.48394132428021 },
268 | 	{ time: { year: 2018, month: 8, day: 29 }, value: 101.41501247525068 },
269 | 	{ time: { year: 2018, month: 8, day: 30 }, value: 94.9501205245301 },
270 | 	{ time: { year: 2018, month: 8, day: 31 }, value: 89.11429564465982 },
271 | 	{ time: { year: 2018, month: 9, day: 1 }, value: 104.1842141132897 },
272 | 	{ time: { year: 2018, month: 9, day: 2 }, value: 97.36185743859737 },
273 | 	{ time: { year: 2018, month: 9, day: 3 }, value: 97.34376526297034 },
274 | 	{ time: { year: 2018, month: 9, day: 4 }, value: 103.73609636859413 },
275 | 	{ time: { year: 2018, month: 9, day: 5 }, value: 86.89420264148593 },
276 | 	{ time: { year: 2018, month: 9, day: 6 }, value: 90.99445484839778 },
277 | 	{ time: { year: 2018, month: 9, day: 7 }, value: 92.0197876339847 },
278 | 	{ time: { year: 2018, month: 9, day: 8 }, value: 87.35412911434453 },
279 | 	{ time: { year: 2018, month: 9, day: 9 }, value: 97.40224787139312 },
280 | 	{ time: { year: 2018, month: 9, day: 10 }, value: 98.14732375673768 },
281 | 	{ time: { year: 2018, month: 9, day: 11 }, value: 101.5147062059064 },
282 | 	{ time: { year: 2018, month: 9, day: 12 }, value: 93.11950437404803 },
283 | 	{ time: { year: 2018, month: 9, day: 13 }, value: 98.41765784798642 },
284 | 	{ time: { year: 2018, month: 9, day: 14 }, value: 89.08499357950659 },
285 | 	{ time: { year: 2018, month: 9, day: 15 }, value: 96.29213559344964 },
286 | 	{ time: { year: 2018, month: 9, day: 16 }, value: 103.57528341068684 },
287 | 	{ time: { year: 2018, month: 9, day: 17 }, value: 98.94258099235431 },
288 | 	{ time: { year: 2018, month: 9, day: 18 }, value: 92.43383394007822 },
289 | 	{ time: { year: 2018, month: 9, day: 19 }, value: 105.39681697822706 },
290 | 	{ time: { year: 2018, month: 9, day: 20 }, value: 100.52663985092036 },
291 | 	{ time: { year: 2018, month: 9, day: 21 }, value: 98.84754340440189 },
292 | 	{ time: { year: 2018, month: 9, day: 22 }, value: 93.78502517034752 },
293 | 	{ time: { year: 2018, month: 9, day: 23 }, value: 95.51435402626828 },
294 | 	{ time: { year: 2018, month: 9, day: 24 }, value: 91.94633821567461 },
295 | 	{ time: { year: 2018, month: 9, day: 25 }, value: 98.18484857755837 },
296 | 	{ time: { year: 2018, month: 9, day: 26 }, value: 102.51694320185617 },
297 | 	{ time: { year: 2018, month: 9, day: 27 }, value: 97.40549024974396 },
298 | 	{ time: { year: 2018, month: 9, day: 28 }, value: 103.49718807374374 },
299 | 	{ time: { year: 2018, month: 9, day: 29 }, value: 108.24441490057781 },
300 | 	{ time: { year: 2018, month: 9, day: 30 }, value: 103.24675412744978 },
301 | 	{ time: { year: 2018, month: 10, day: 1 }, value: 97.05089568637521 },
302 | 	{ time: { year: 2018, month: 10, day: 2 }, value: 91.85875309835458 },
303 | 	{ time: { year: 2018, month: 10, day: 3 }, value: 72.24590653541385 },
304 | 	{ time: { year: 2018, month: 10, day: 4 }, value: 70.73707674373722 },
305 | 	{ time: { year: 2018, month: 10, day: 5 }, value: 61.2106378263602 },
306 | 	{ time: { year: 2018, month: 10, day: 6 }, value: 62.35889407826063 },
307 | 	{ time: { year: 2018, month: 10, day: 7 }, value: 56.311930696659 },
308 | 	{ time: { year: 2018, month: 10, day: 8 }, value: 51.462743547904374 },
309 | 	{ time: { year: 2018, month: 10, day: 9 }, value: 47.99928302521288 },
310 | 	{ time: { year: 2018, month: 10, day: 10 }, value: 42.735011616511976 },
311 | 	{ time: { year: 2018, month: 10, day: 11 }, value: 35.82291867003256 },
312 | 	{ time: { year: 2018, month: 10, day: 12 }, value: 28.706141122035454 },
313 | 	{ time: { year: 2018, month: 10, day: 13 }, value: 24.289344698634036 },
314 | 	{ time: { year: 2018, month: 10, day: 14 }, value: 22.56513000253429 },
315 | 	{ time: { year: 2018, month: 10, day: 15 }, value: 18.862530899060324 },
316 | 	{ time: { year: 2018, month: 10, day: 16 }, value: 18.164416367748263 },
317 | 	{ time: { year: 2018, month: 10, day: 17 }, value: 16.25993836760582 },
318 | 	{ time: { year: 2018, month: 10, day: 18 }, value: 15.849033589978859 },
319 | 	{ time: { year: 2018, month: 10, day: 19 }, value: 12.581184324950792 },
320 | 	{ time: { year: 2018, month: 10, day: 20 }, value: 12.46960767886934 },
321 | 	{ time: { year: 2018, month: 10, day: 21 }, value: 13.203284995561251 },
322 | 	{ time: { year: 2018, month: 10, day: 22 }, value: 12.751819244602629 },
323 | 	{ time: { year: 2018, month: 10, day: 23 }, value: 13.815126496529205 },
324 | 	{ time: { year: 2018, month: 10, day: 24 }, value: 14.44156419046133 },
325 | 	{ time: { year: 2018, month: 10, day: 25 }, value: 12.030505290672643 },
326 | 	{ time: { year: 2018, month: 10, day: 26 }, value: 13.426535837756518 },
327 | 	{ time: { year: 2018, month: 10, day: 27 }, value: 13.141003741491893 },
328 | 	{ time: { year: 2018, month: 10, day: 28 }, value: 12.216411608284261 },
329 | 	{ time: { year: 2018, month: 10, day: 29 }, value: 12.437867813477077 },
330 | 	{ time: { year: 2018, month: 10, day: 30 }, value: 12.228521667932771 },
331 | 	{ time: { year: 2018, month: 10, day: 31 }, value: 13.587126038913974 },
332 | 	{ time: { year: 2018, month: 11, day: 1 }, value: 12.016792589137491 },
333 | 	{ time: { year: 2018, month: 11, day: 2 }, value: 13.01948020515645 },
334 | 	{ time: { year: 2018, month: 11, day: 3 }, value: 12.70475528902004 },
335 | 	{ time: { year: 2018, month: 11, day: 4 }, value: 13.018454073452016 },
336 | 	{ time: { year: 2018, month: 11, day: 5 }, value: 12.505487262036313 },
337 | 	{ time: { year: 2018, month: 11, day: 6 }, value: 13.467522897553604 },
338 | 	{ time: { year: 2018, month: 11, day: 7 }, value: 13.748796553616549 },
339 | 	{ time: { year: 2018, month: 11, day: 8 }, value: 11.974873751121669 },
340 | 	{ time: { year: 2018, month: 11, day: 9 }, value: 11.8316362912944 },
341 | 	{ time: { year: 2018, month: 11, day: 10 }, value: 13.864291857325023 },
342 | 	{ time: { year: 2018, month: 11, day: 11 }, value: 12.071675684436165 },
343 | 	{ time: { year: 2018, month: 11, day: 12 }, value: 12.314581956701367 },
344 | 	{ time: { year: 2018, month: 11, day: 13 }, value: 13.223445358310986 },
345 | 	{ time: { year: 2018, month: 11, day: 14 }, value: 12.346191421746546 },
346 | 	{ time: { year: 2018, month: 11, day: 15 }, value: 12.0232072259563 },
347 | 	{ time: { year: 2018, month: 11, day: 16 }, value: 13.367039701380252 },
348 | 	{ time: { year: 2018, month: 11, day: 17 }, value: 12.232635114201212 },
349 | 	{ time: { year: 2018, month: 11, day: 18 }, value: 13.348220671014012 },
350 | 	{ time: { year: 2018, month: 11, day: 19 }, value: 13.508314659502604 },
351 | 	{ time: { year: 2018, month: 11, day: 20 }, value: 12.630893498655155 },
352 | 	{ time: { year: 2018, month: 11, day: 21 }, value: 12.632952849963768 },
353 | 	{ time: { year: 2018, month: 11, day: 22 }, value: 11.645073051089117 },
354 | 	{ time: { year: 2018, month: 11, day: 23 }, value: 13.845637677048611 },
355 | 	{ time: { year: 2018, month: 11, day: 24 }, value: 12.567519871595463 },
356 | 	{ time: { year: 2018, month: 11, day: 25 }, value: 13.927270152127294 },
357 | 	{ time: { year: 2018, month: 11, day: 26 }, value: 12.179362670863737 },
358 | 	{ time: { year: 2018, month: 11, day: 27 }, value: 12.471835488646303 },
359 | 	{ time: { year: 2018, month: 11, day: 28 }, value: 11.71761488042106 },
360 | 	{ time: { year: 2018, month: 11, day: 29 }, value: 12.181312973409113 },
361 | 	{ time: { year: 2018, month: 11, day: 30 }, value: 12.662272671374286 },
362 | 	{ time: { year: 2018, month: 12, day: 1 }, value: 13.859774226603497 },
363 | 	{ time: { year: 2018, month: 12, day: 2 }, value: 11.643237368800426 },
364 | 	{ time: { year: 2018, month: 12, day: 3 }, value: 11.646083130428282 },
365 | 	{ time: { year: 2018, month: 12, day: 4 }, value: 13.3486102643562 },
366 | 	{ time: { year: 2018, month: 12, day: 5 }, value: 13.421817450001853 },
367 | 	{ time: { year: 2018, month: 12, day: 6 }, value: 13.734844672048157 },
368 | 	{ time: { year: 2018, month: 12, day: 7 }, value: 11.808371821628475 },
369 | 	{ time: { year: 2018, month: 12, day: 8 }, value: 13.906976670383472 },
370 | 	{ time: { year: 2018, month: 12, day: 9 }, value: 13.161627469585584 },
371 | 	{ time: { year: 2018, month: 12, day: 10 }, value: 13.642368164712535 },
372 | 	{ time: { year: 2018, month: 12, day: 11 }, value: 12.755167209621261 },
373 | 	{ time: { year: 2018, month: 12, day: 12 }, value: 12.13947468588139 },
374 | 	{ time: { year: 2018, month: 12, day: 13 }, value: 13.68979129854326 },
375 | 	{ time: { year: 2018, month: 12, day: 14 }, value: 11.812050924695251 },
376 | 	{ time: { year: 2018, month: 12, day: 15 }, value: 11.71992287051065 },
377 | 	{ time: { year: 2018, month: 12, day: 16 }, value: 13.003823991463284 },
378 | 	{ time: { year: 2018, month: 12, day: 17 }, value: 13.124946877570311 },
379 | 	{ time: { year: 2018, month: 12, day: 18 }, value: 11.844736927132542 },
380 | 	{ time: { year: 2018, month: 12, day: 19 }, value: 11.770961792864846 },
381 | 	{ time: { year: 2018, month: 12, day: 20 }, value: 10.926179837275598 },
382 | 	{ time: { year: 2018, month: 12, day: 21 }, value: 11.155771630851676 },
383 | 	{ time: { year: 2018, month: 12, day: 22 }, value: 11.63008791780728 },
384 | 	{ time: { year: 2018, month: 12, day: 23 }, value: 10.216268005840389 },
385 | 	{ time: { year: 2018, month: 12, day: 24 }, value: 13.611694182717626 },
386 | 	{ time: { year: 2018, month: 12, day: 25 }, value: 17.47706580052263 },
387 | 	{ time: { year: 2018, month: 12, day: 26 }, value: 20.900697260373697 },
388 | 	{ time: { year: 2018, month: 12, day: 27 }, value: 20.44940301651778 },
389 | 	{ time: { year: 2018, month: 12, day: 28 }, value: 23.47128311932538 },
390 | 	{ time: { year: 2018, month: 12, day: 29 }, value: 28.63506505828928 },
391 | 	{ time: { year: 2018, month: 12, day: 30 }, value: 29.567577074788517 },
392 | 	// hide-end
393 | ];
394 | series.setData(data);
395 | 
396 | let minimumPrice = data[0].value;
397 | let maximumPrice = minimumPrice;
398 | for (let i = 1; i < data.length; i++) {
399 | 	const price = data[i].value;
400 | 	if (price > maximumPrice) {
401 | 		maximumPrice = price;
402 | 	}
403 | 	if (price < minimumPrice) {
404 | 		minimumPrice = price;
405 | 	}
406 | }
407 | const avgPrice = (maximumPrice + minimumPrice) / 2;
408 | 
409 | // highlight-start
410 | const lineWidth = 2;
411 | const minPriceLine = {
412 | 	price: minimumPrice,
413 | 	color: BAR_DOWN_COLOR,
414 | 	lineWidth: lineWidth,
415 | 	lineStyle: 2, // LineStyle.Dashed
416 | 	axisLabelVisible: true,
417 | 	title: 'min price',
418 | };
419 | const avgPriceLine = {
420 | 	price: avgPrice,
421 | 	color: CHART_TEXT_COLOR,
422 | 	lineWidth: lineWidth,
423 | 	lineStyle: 1, // LineStyle.Dotted
424 | 	axisLabelVisible: true,
425 | 	title: 'ave price',
426 | };
427 | const maxPriceLine = {
428 | 	price: maximumPrice,
429 | 	color: BAR_UP_COLOR,
430 | 	lineWidth: lineWidth,
431 | 	lineStyle: 2, // LineStyle.Dashed
432 | 	axisLabelVisible: true,
433 | 	title: 'max price',
434 | };
435 | 
436 | series.createPriceLine(minPriceLine);
437 | series.createPriceLine(avgPriceLine);
438 | series.createPriceLine(maxPriceLine);
439 | // highlight-end
440 | 
441 | chart.timeScale().fitContent();
442 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/price-line.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Add Price Line
 3 | sidebar_label: Price Lines
 4 | description: An example of how to add price lines to a chart.
 5 | pagination_prev: null
 6 | pagination_next: null
 7 | keywords:
 8 |   - price line
 9 | ---
10 | 
11 | A price line is a horizontal line drawn across the width of the chart at a specific price value.
12 | This example shows how to add price lines to your chart.
13 | 
14 | ## Short answer
15 | 
16 | A price line can be added to a chart by using the
17 | [`createPriceLine`](/docs/api/interfaces/ISeriesApi#createpriceline) method on an existing series
18 | ([ISeriesApi](/docs/api/interfaces/ISeriesApi)) instance.
19 | 
20 | ```js
21 | const myPriceLine = {
22 |     price: 1234,
23 |     color: '#3179F5',
24 |     lineWidth: 2,
25 |     lineStyle: 2, // LineStyle.Dashed
26 |     axisLabelVisible: true,
27 |     title: 'my label',
28 | };
29 | 
30 | series.createPriceLine(myPriceLine);
31 | ```
32 | 
33 | You can see a full [working example](#full-example) below.
34 | 
35 | ## Tips
36 | 
37 | You may wish to disable the default price line drawn by Lightweight Charts™
38 | for the last value in the series (and it's label). You can do this by adjusting the
39 | series options as follows:
40 | 
41 | ```js
42 | series.applyOptions({
43 |     lastValueVisible: false,
44 |     priceLineVisible: false,
45 | });
46 | ```
47 | 
48 | ## Resources
49 | 
50 | You can view the related APIs here:
51 | - [createPriceLine](/docs/api/interfaces/ISeriesApi#createpriceline) - Method to create a new Price Line.
52 | - [PriceLineOptions](/docs/api/interfaces/PriceLineOptions) - Price Line options.
53 | - [LineStyle](/docs/api/enumerations/LineStyle) - Available line styles.
54 | 
55 | ## Full example
56 | 
57 | import UsageGuidePartial from "../_usage-guide-partial.mdx";
58 | import CodeBlock from "@theme/CodeBlock";
59 | import code from "!!raw-loader!./price-line.js";
60 | 
61 | <CodeBlock replaceThemeConstants chart className="language-js" hideableCode chartOnTop codeUsage={<UsageGuidePartial />}>
62 | 	{code}
63 | </CodeBlock>
64 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/series-markers.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Series Markers
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/how_to/series-markers
  4 | 
  5 | // remove-end
  6 | const chartOptions = {
  7 | 	layout: {
  8 | 		textColor: CHART_TEXT_COLOR,
  9 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
 10 | 	},
 11 | };
 12 | // remove-line
 13 | /** @type {import('lightweight-charts').IChartApi} */
 14 | const chart = createChart(document.getElementById('container'), chartOptions);
 15 | 
 16 | const series = chart.addSeries(CandlestickSeries, {
 17 | 	upColor: BAR_UP_COLOR, downColor: BAR_DOWN_COLOR, borderVisible: false,
 18 | 	wickUpColor: BAR_UP_COLOR, wickDownColor: BAR_DOWN_COLOR,
 19 | });
 20 | 
 21 | const data = [
 22 | 	{
 23 | 		time: { year: 2018, month: 9, day: 22 },
 24 | 		open: 29.630237296336794,
 25 | 		high: 35.36950035097501,
 26 | 		low: 26.21522501353531,
 27 | 		close: 30.734997177569916,
 28 | 	},
 29 | 	// hide-start
 30 | 	{
 31 | 		time: { year: 2018, month: 9, day: 23 },
 32 | 		open: 32.267626500691215,
 33 | 		high: 34.452661663723774,
 34 | 		low: 26.096868360824704,
 35 | 		close: 29.573918833457004,
 36 | 	},
 37 | 	{
 38 | 		time: { year: 2018, month: 9, day: 24 },
 39 | 		open: 27.33996760497746,
 40 | 		high: 35.8060364835531,
 41 | 		low: 27.33996760497746,
 42 | 		close: 33.06283432964511,
 43 | 	},
 44 | 	{
 45 | 		time: { year: 2018, month: 9, day: 25 },
 46 | 		open: 31.1654368745013,
 47 | 		high: 31.97284477478497,
 48 | 		low: 26.766743287285593,
 49 | 		close: 27.364979322283386,
 50 | 	},
 51 | 	{
 52 | 		time: { year: 2018, month: 9, day: 26 },
 53 | 		open: 29.5901452337888,
 54 | 		high: 32.147919593347474,
 55 | 		low: 27.53289219709677,
 56 | 		close: 29.202912415085272,
 57 | 	},
 58 | 	{
 59 | 		time: { year: 2018, month: 9, day: 27 },
 60 | 		open: 27.561741523265923,
 61 | 		high: 35.11649043301526,
 62 | 		low: 25.20035866163233,
 63 | 		close: 31.14520649627546,
 64 | 	},
 65 | 	{
 66 | 		time: { year: 2018, month: 9, day: 28 },
 67 | 		open: 31.925975006823798,
 68 | 		high: 31.925975006823798,
 69 | 		low: 28.998500720406675,
 70 | 		close: 29.87723790403876,
 71 | 	},
 72 | 	{
 73 | 		time: { year: 2018, month: 9, day: 29 },
 74 | 		open: 30.826956088992475,
 75 | 		high: 34.79463130873015,
 76 | 		low: 25.291546123273097,
 77 | 		close: 28.994812708315987,
 78 | 	},
 79 | 	{
 80 | 		time: { year: 2018, month: 9, day: 30 },
 81 | 		open: 31.202920145287838,
 82 | 		high: 33.19178819590413,
 83 | 		low: 23.94419012923956,
 84 | 		close: 31.47253745770869,
 85 | 	},
 86 | 	{
 87 | 		time: { year: 2018, month: 10, day: 1 },
 88 | 		open: 26.927794164758666,
 89 | 		high: 34.6744456778885,
 90 | 		low: 26.927794164758666,
 91 | 		close: 31.091122539737423,
 92 | 	},
 93 | 	{
 94 | 		time: { year: 2018, month: 10, day: 2 },
 95 | 		open: 26.452041173938298,
 96 | 		high: 34.527917622572154,
 97 | 		low: 26.452041173938298,
 98 | 		close: 27.65703395829094,
 99 | 	},
100 | 	{
101 | 		time: { year: 2018, month: 10, day: 3 },
102 | 		open: 27.74629982387605,
103 | 		high: 29.300441707649835,
104 | 		low: 23.761300216231263,
105 | 		close: 29.182874625005628,
106 | 	},
107 | 	{
108 | 		time: { year: 2018, month: 10, day: 4 },
109 | 		open: 30.41599722290526,
110 | 		high: 31.942643078777103,
111 | 		low: 27.09925359459428,
112 | 		close: 30.918477883682872,
113 | 	},
114 | 	{
115 | 		time: { year: 2018, month: 10, day: 5 },
116 | 		open: 25.76549797105683,
117 | 		high: 33.4650523853759,
118 | 		low: 25.76549797105683,
119 | 		close: 28.15984801386293,
120 | 	},
121 | 	{
122 | 		time: { year: 2018, month: 10, day: 6 },
123 | 		open: 27.543404135965382,
124 | 		high: 30.7227783000902,
125 | 		low: 25.749951838020884,
126 | 		close: 29.150903848724184,
127 | 	},
128 | 	{
129 | 		time: { year: 2018, month: 10, day: 7 },
130 | 		open: 29.34759861812077,
131 | 		high: 31.08503530472835,
132 | 		low: 23.395022079647823,
133 | 		close: 25.00923131079722,
134 | 	},
135 | 	{
136 | 		time: { year: 2018, month: 10, day: 8 },
137 | 		open: 27.00266154335036,
138 | 		high: 29.51599687178633,
139 | 		low: 23.46749249241176,
140 | 		close: 28.702932483799707,
141 | 	},
142 | 	{
143 | 		time: { year: 2018, month: 10, day: 9 },
144 | 		open: 25.569958099853594,
145 | 		high: 27.669071502065417,
146 | 		low: 25.569958099853594,
147 | 		close: 25.626920473922613,
148 | 	},
149 | 	{
150 | 		time: { year: 2018, month: 10, day: 10 },
151 | 		open: 24.886919828178304,
152 | 		high: 27.167620185117006,
153 | 		low: 23.71595991386752,
154 | 		close: 23.71595991386752,
155 | 	},
156 | 	{
157 | 		time: { year: 2018, month: 10, day: 11 },
158 | 		open: 26.14124249813686,
159 | 		high: 29.5638477987916,
160 | 		low: 20.82341105699825,
161 | 		close: 25.563138238511257,
162 | 	},
163 | 	{
164 | 		time: { year: 2018, month: 10, day: 12 },
165 | 		open: 22.26412127509447,
166 | 		high: 27.637685003390743,
167 | 		low: 20.838507431464958,
168 | 		close: 22.450517792778047,
169 | 	},
170 | 	{
171 | 		time: { year: 2018, month: 10, day: 13 },
172 | 		open: 25.75099239090953,
173 | 		high: 28.12000626118839,
174 | 		low: 21.929748303510852,
175 | 		close: 22.63015682488669,
176 | 	},
177 | 	{
178 | 		time: { year: 2018, month: 10, day: 14 },
179 | 		open: 25.428132591291497,
180 | 		high: 25.999229490809693,
181 | 		low: 22.266121337091555,
182 | 		close: 23.51047528528147,
183 | 	},
184 | 	{
185 | 		time: { year: 2018, month: 10, day: 15 },
186 | 		open: 25.07416967939059,
187 | 		high: 25.50535192500713,
188 | 		low: 21.96666570325133,
189 | 		close: 21.96666570325133,
190 | 	},
191 | 	{
192 | 		time: { year: 2018, month: 10, day: 16 },
193 | 		open: 24.957206161449307,
194 | 		high: 26.679727314857256,
195 | 		low: 20.196753994637245,
196 | 		close: 21.523347810451863,
197 | 	},
198 | 	{
199 | 		time: { year: 2018, month: 10, day: 17 },
200 | 		open: 23.705184745772733,
201 | 		high: 26.754094837621004,
202 | 		low: 18.724184302695104,
203 | 		close: 20.160857555541725,
204 | 	},
205 | 	{
206 | 		time: { year: 2018, month: 10, day: 18 },
207 | 		open: 21.95610851644136,
208 | 		high: 22.914889536420105,
209 | 		low: 19.567733140100472,
210 | 		close: 22.914889536420105,
211 | 	},
212 | 	{
213 | 		time: { year: 2018, month: 10, day: 19 },
214 | 		open: 23.216357873687972,
215 | 		high: 25.44815512734246,
216 | 		low: 19.54787451276509,
217 | 		close: 20.76851802225937,
218 | 	},
219 | 	{
220 | 		time: { year: 2018, month: 10, day: 20 },
221 | 		open: 19.6289025950405,
222 | 		high: 24.290702755740412,
223 | 		low: 19.041541929894358,
224 | 		close: 22.48608548162324,
225 | 	},
226 | 	{
227 | 		time: { year: 2018, month: 10, day: 21 },
228 | 		open: 23.599000037544915,
229 | 		high: 26.839019853462844,
230 | 		low: 20.884129956680898,
231 | 		close: 22.01878871761756,
232 | 	},
233 | 	{
234 | 		time: { year: 2018, month: 10, day: 22 },
235 | 		open: 24.618502768742008,
236 | 		high: 28.00099352255492,
237 | 		low: 23.061935629399088,
238 | 		close: 23.061935629399088,
239 | 	},
240 | 	{
241 | 		time: { year: 2018, month: 10, day: 23 },
242 | 		open: 23.840701995876866,
243 | 		high: 28.494382608429564,
244 | 		low: 23.840701995876866,
245 | 		close: 25.321841131665526,
246 | 	},
247 | 	{
248 | 		time: { year: 2018, month: 10, day: 24 },
249 | 		open: 27.764925733189372,
250 | 		high: 31.05550601484776,
251 | 		low: 22.810929726970702,
252 | 		close: 30.02406259204889,
253 | 	},
254 | 	{
255 | 		time: { year: 2018, month: 10, day: 25 },
256 | 		open: 29.703149280184604,
257 | 		high: 34.0185175501095,
258 | 		low: 26.82967654698301,
259 | 		close: 32.06834171351323,
260 | 	},
261 | 	{
262 | 		time: { year: 2018, month: 10, day: 26 },
263 | 		open: 29.0251492427822,
264 | 		high: 36.89478162439007,
265 | 		low: 28.3502671011196,
266 | 		close: 32.822663125409356,
267 | 	},
268 | 	{
269 | 		time: { year: 2018, month: 10, day: 27 },
270 | 		open: 35.040777462643284,
271 | 		high: 35.12524316379231,
272 | 		low: 26.805156020579663,
273 | 		close: 34.23626219571325,
274 | 	},
275 | 	{
276 | 		time: { year: 2018, month: 10, day: 28 },
277 | 		open: 31.21349419519032,
278 | 		high: 35.73068910379853,
279 | 		low: 31.064101813812698,
280 | 		close: 34.75020857236565,
281 | 	},
282 | 	{
283 | 		time: { year: 2018, month: 10, day: 29 },
284 | 		open: 32.34914826794689,
285 | 		high: 42.381605482695505,
286 | 		low: 30.176750284055878,
287 | 		close: 39.24138147444552,
288 | 	},
289 | 	{
290 | 		time: { year: 2018, month: 10, day: 30 },
291 | 		open: 38.84583808993371,
292 | 		high: 41.75165839362154,
293 | 		low: 33.37106955991806,
294 | 		close: 35.93904098275507,
295 | 	},
296 | 	{
297 | 		time: { year: 2018, month: 10, day: 31 },
298 | 		open: 37.070183005323564,
299 | 		high: 44.84460203857022,
300 | 		low: 35.23671284121251,
301 | 		close: 36.329972003600034,
302 | 	},
303 | 	{
304 | 		time: { year: 2018, month: 11, day: 1 },
305 | 		open: 43.31997309164893,
306 | 		high: 48.43216497187469,
307 | 		low: 38.30881963355285,
308 | 		close: 41.554948540677586,
309 | 	},
310 | 	{
311 | 		time: { year: 2018, month: 11, day: 2 },
312 | 		open: 41.33946811092929,
313 | 		high: 46.65347243834853,
314 | 		low: 37.472215586661335,
315 | 		close: 39.26832265482503,
316 | 	},
317 | 	{
318 | 		time: { year: 2018, month: 11, day: 3 },
319 | 		open: 44.76468593661226,
320 | 		high: 44.76468593661226,
321 | 		low: 40.039672147314235,
322 | 		close: 43.42106786288436,
323 | 	},
324 | 	{
325 | 		time: { year: 2018, month: 11, day: 4 },
326 | 		open: 49.13160326887013,
327 | 		high: 49.13160326887013,
328 | 		low: 40.93648693038296,
329 | 		close: 42.17817698294767,
330 | 	},
331 | 	{
332 | 		time: { year: 2018, month: 11, day: 5 },
333 | 		open: 50.46706012970579,
334 | 		high: 54.38104598422352,
335 | 		low: 38.159930155343616,
336 | 		close: 47.5899156640143,
337 | 	},
338 | 	{
339 | 		time: { year: 2018, month: 11, day: 6 },
340 | 		open: 48.25899506613569,
341 | 		high: 48.25899506613569,
342 | 		low: 45.63208604138365,
343 | 		close: 45.63208604138365,
344 | 	},
345 | 	{
346 | 		time: { year: 2018, month: 11, day: 7 },
347 | 		open: 52.45484210527629,
348 | 		high: 57.55979771849961,
349 | 		low: 45.23447676016779,
350 | 		close: 46.01127464234881,
351 | 	},
352 | 	{
353 | 		time: { year: 2018, month: 11, day: 8 },
354 | 		open: 53.228216675179624,
355 | 		high: 54.07804814570622,
356 | 		low: 40.61161433961706,
357 | 		close: 47.689867390699014,
358 | 	},
359 | 	{
360 | 		time: { year: 2018, month: 11, day: 9 },
361 | 		open: 46.193099316212816,
362 | 		high: 56.190537353078824,
363 | 		low: 45.01246323828753,
364 | 		close: 49.14012661656766,
365 | 	},
366 | 	{
367 | 		time: { year: 2018, month: 11, day: 10 },
368 | 		open: 50.409245396927986,
369 | 		high: 52.3082002787041,
370 | 		low: 41.764144138886394,
371 | 		close: 52.3082002787041,
372 | 	},
373 | 	{
374 | 		time: { year: 2018, month: 11, day: 11 },
375 | 		open: 48.58146178816203,
376 | 		high: 52.653922195022126,
377 | 		low: 47.34031788474959,
378 | 		close: 47.34031788474959,
379 | 	},
380 | 	{
381 | 		time: { year: 2018, month: 11, day: 12 },
382 | 		open: 46.80040325283692,
383 | 		high: 56.709349494076804,
384 | 		low: 45.81605691554122,
385 | 		close: 45.81605691554122,
386 | 	},
387 | 	{
388 | 		time: { year: 2018, month: 11, day: 13 },
389 | 		open: 46.042722425788355,
390 | 		high: 58.476056411825695,
391 | 		low: 46.042722425788355,
392 | 		close: 51.2300776481609,
393 | 	},
394 | 	{
395 | 		time: { year: 2018, month: 11, day: 14 },
396 | 		open: 53.909068487588385,
397 | 		high: 60.240990154306715,
398 | 		low: 45.230741063278664,
399 | 		close: 51.34529637385427,
400 | 	},
401 | 	{
402 | 		time: { year: 2018, month: 11, day: 15 },
403 | 		open: 53.739609857086606,
404 | 		high: 53.739609857086606,
405 | 		low: 44.38017019990068,
406 | 		close: 47.595960698697894,
407 | 	},
408 | 	{
409 | 		time: { year: 2018, month: 11, day: 16 },
410 | 		open: 52.52688238296145,
411 | 		high: 60.9220040817774,
412 | 		low: 44.27700764117003,
413 | 		close: 55.27309771985698,
414 | 	},
415 | 	{
416 | 		time: { year: 2018, month: 11, day: 17 },
417 | 		open: 54.46100795908005,
418 | 		high: 57.57937841117058,
419 | 		low: 49.50543170388487,
420 | 		close: 49.50543170388487,
421 | 	},
422 | 	{
423 | 		time: { year: 2018, month: 11, day: 18 },
424 | 		open: 51.12284024600029,
425 | 		high: 57.646718858433026,
426 | 		low: 48.73280269653226,
427 | 		close: 51.35457902694444,
428 | 	},
429 | 	{
430 | 		time: { year: 2018, month: 11, day: 19 },
431 | 		open: 53.536130807863266,
432 | 		high: 53.536130807863266,
433 | 		low: 51.29649965636722,
434 | 		close: 52.99088526565045,
435 | 	},
436 | 	{
437 | 		time: { year: 2018, month: 11, day: 20 },
438 | 		open: 50.92761950009885,
439 | 		high: 57.70671943558014,
440 | 		low: 46.45030483558741,
441 | 		close: 52.229112575743066,
442 | 	},
443 | 	{
444 | 		time: { year: 2018, month: 11, day: 21 },
445 | 		open: 49.30035068900293,
446 | 		high: 58.67691694734525,
447 | 		low: 44.63563165197862,
448 | 		close: 58.67691694734525,
449 | 	},
450 | 	{
451 | 		time: { year: 2018, month: 11, day: 22 },
452 | 		open: 54.230476484061036,
453 | 		high: 59.03831193868438,
454 | 		low: 50.77849134047791,
455 | 		close: 59.03831193868438,
456 | 	},
457 | 	{
458 | 		time: { year: 2018, month: 11, day: 23 },
459 | 		open: 57.282420985156854,
460 | 		high: 60.4869735007396,
461 | 		low: 44.14116488798797,
462 | 		close: 57.93461310007337,
463 | 	},
464 | 	{
465 | 		time: { year: 2018, month: 11, day: 24 },
466 | 		open: 54.86833150125539,
467 | 		high: 64.25102812467448,
468 | 		low: 52.36616043331222,
469 | 		close: 52.36616043331222,
470 | 	},
471 | 	{
472 | 		time: { year: 2018, month: 11, day: 25 },
473 | 		open: 51.689239380620386,
474 | 		high: 64.29747922654688,
475 | 		low: 50.71498529572432,
476 | 		close: 60.518206306602394,
477 | 	},
478 | 	{
479 | 		time: { year: 2018, month: 11, day: 26 },
480 | 		open: 55.74863310659164,
481 | 		high: 60.816819055612584,
482 | 		low: 46.11238607935206,
483 | 		close: 59.23044859881929,
484 | 	},
485 | 	{
486 | 		time: { year: 2018, month: 11, day: 27 },
487 | 		open: 52.57406222528308,
488 | 		high: 64.2058753841427,
489 | 		low: 48.163404012323305,
490 | 		close: 60.593847809696896,
491 | 	},
492 | 	{
493 | 		time: { year: 2018, month: 11, day: 28 },
494 | 		open: 57.50710740029724,
495 | 		high: 60.12123058977347,
496 | 		low: 49.61839271711267,
497 | 		close: 53.29152711098895,
498 | 	},
499 | 	{
500 | 		time: { year: 2018, month: 11, day: 29 },
501 | 		open: 57.33581828303538,
502 | 		high: 58.92432332528284,
503 | 		low: 53.27790061455899,
504 | 		close: 57.02787118731709,
505 | 	},
506 | 	{
507 | 		time: { year: 2018, month: 11, day: 30 },
508 | 		open: 57.527445314328595,
509 | 		high: 67.63249690962569,
510 | 		low: 49.603261485289146,
511 | 		close: 54.589123556483656,
512 | 	},
513 | 	{
514 | 		time: { year: 2018, month: 12, day: 1 },
515 | 		open: 59.98835793934424,
516 | 		high: 65.51917884840141,
517 | 		low: 52.32535994476165,
518 | 		close: 62.127135611086565,
519 | 	},
520 | 	{
521 | 		time: { year: 2018, month: 12, day: 2 },
522 | 		open: 52.509550731662536,
523 | 		high: 58.49971806419494,
524 | 		low: 52.509550731662536,
525 | 		close: 54.759948868082255,
526 | 	},
527 | 	{
528 | 		time: { year: 2018, month: 12, day: 3 },
529 | 		open: 58.08470541982317,
530 | 		high: 62.74987556918568,
531 | 		low: 47.85627992158991,
532 | 		close: 58.690428071336406,
533 | 	},
534 | 	{
535 | 		time: { year: 2018, month: 12, day: 4 },
536 | 		open: 58.28482939034761,
537 | 		high: 69.16675825892361,
538 | 		low: 57.41588944088662,
539 | 		close: 57.74515245619454,
540 | 	},
541 | 	{
542 | 		time: { year: 2018, month: 12, day: 5 },
543 | 		open: 60.004299871302464,
544 | 		high: 65.82447121605708,
545 | 		low: 53.13330527599658,
546 | 		close: 57.64488004774012,
547 | 	},
548 | 	{
549 | 		time: { year: 2018, month: 12, day: 6 },
550 | 		open: 61.92746155137417,
551 | 		high: 64.36944842979646,
552 | 		low: 49.470442234694225,
553 | 		close: 59.94404434023895,
554 | 	},
555 | 	{
556 | 		time: { year: 2018, month: 12, day: 7 },
557 | 		open: 63.72235832229121,
558 | 		high: 66.33649390307095,
559 | 		low: 49.91822946887207,
560 | 		close: 63.56396375320479,
561 | 	},
562 | 	{
563 | 		time: { year: 2018, month: 12, day: 8 },
564 | 		open: 56.64594047326664,
565 | 		high: 65.3730920902599,
566 | 		low: 52.604389283975664,
567 | 		close: 60.71684658387917,
568 | 	},
569 | 	{
570 | 		time: { year: 2018, month: 12, day: 9 },
571 | 		open: 58.89798885700999,
572 | 		high: 68.04578543284373,
573 | 		low: 58.89798885700999,
574 | 		close: 63.36111469854223,
575 | 	},
576 | 	{
577 | 		time: { year: 2018, month: 12, day: 10 },
578 | 		open: 58.869685789579826,
579 | 		high: 70.99828637845869,
580 | 		low: 52.36901833289119,
581 | 		close: 63.15473262144694,
582 | 	},
583 | 	{
584 | 		time: { year: 2018, month: 12, day: 11 },
585 | 		open: 57.61362492091653,
586 | 		high: 66.41975632948531,
587 | 		low: 50.827182111530895,
588 | 		close: 61.770769489947064,
589 | 	},
590 | 	{
591 | 		time: { year: 2018, month: 12, day: 12 },
592 | 		open: 57.869332957269656,
593 | 		high: 66.28374056429257,
594 | 		low: 57.05028878520954,
595 | 		close: 63.87762958979595,
596 | 	},
597 | 	{
598 | 		time: { year: 2018, month: 12, day: 13 },
599 | 		open: 68.14347595614306,
600 | 		high: 73.46304446829079,
601 | 		low: 50.83319311788897,
602 | 		close: 66.9144140431443,
603 | 	},
604 | 	{
605 | 		time: { year: 2018, month: 12, day: 14 },
606 | 		open: 56.95907344942102,
607 | 		high: 68.81432823196859,
608 | 		low: 56.95907344942102,
609 | 		close: 60.69722290026252,
610 | 	},
611 | 	{
612 | 		time: { year: 2018, month: 12, day: 15 },
613 | 		open: 69.14662166493828,
614 | 		high: 69.14662166493828,
615 | 		low: 58.59143795311565,
616 | 		close: 66.25235616866007,
617 | 	},
618 | 	{
619 | 		time: { year: 2018, month: 12, day: 16 },
620 | 		open: 64.0373004661208,
621 | 		high: 72.91321850066319,
622 | 		low: 52.079104978168345,
623 | 		close: 65.92678310822487,
624 | 	},
625 | 	{
626 | 		time: { year: 2018, month: 12, day: 17 },
627 | 		open: 68.81814300123497,
628 | 		high: 69.51927964796873,
629 | 		low: 62.70935477415118,
630 | 		close: 65.64565364397754,
631 | 	},
632 | 	{
633 | 		time: { year: 2018, month: 12, day: 18 },
634 | 		open: 63.47554821643351,
635 | 		high: 73.6284398311906,
636 | 		low: 58.996882824636856,
637 | 		close: 58.996882824636856,
638 | 	},
639 | 	{
640 | 		time: { year: 2018, month: 12, day: 19 },
641 | 		open: 69.97765183896102,
642 | 		high: 69.97765183896102,
643 | 		low: 58.73355952507237,
644 | 		close: 58.73355952507237,
645 | 	},
646 | 	{
647 | 		time: { year: 2018, month: 12, day: 20 },
648 | 		open: 63.22638756186111,
649 | 		high: 65.67137242291682,
650 | 		low: 59.9542779777421,
651 | 		close: 61.20003065016431,
652 | 	},
653 | 	{
654 | 		time: { year: 2018, month: 12, day: 21 },
655 | 		open: 59.690029086102506,
656 | 		high: 78.08665559197297,
657 | 		low: 54.862707942292275,
658 | 		close: 70.58935191024504,
659 | 	},
660 | 	{
661 | 		time: { year: 2018, month: 12, day: 22 },
662 | 		open: 66.29092355620301,
663 | 		high: 71.82667261213395,
664 | 		low: 65.28001993201676,
665 | 		close: 71.82667261213395,
666 | 	},
667 | 	{
668 | 		time: { year: 2018, month: 12, day: 23 },
669 | 		open: 60.92645998120027,
670 | 		high: 74.21283998861118,
671 | 		low: 57.331119016099116,
672 | 		close: 60.36728842356329,
673 | 	},
674 | 	{
675 | 		time: { year: 2018, month: 12, day: 24 },
676 | 		open: 60.211957192084036,
677 | 		high: 72.37883919241614,
678 | 		low: 60.211957192084036,
679 | 		close: 72.37883919241614,
680 | 	},
681 | 	{
682 | 		time: { year: 2018, month: 12, day: 25 },
683 | 		open: 64.80282266865653,
684 | 		high: 71.00204457933133,
685 | 		low: 54.58446926152339,
686 | 		close: 69.9468262738086,
687 | 	},
688 | 	{
689 | 		time: { year: 2018, month: 12, day: 26 },
690 | 		open: 66.28091239894763,
691 | 		high: 81.00843300529249,
692 | 		low: 54.56212171317677,
693 | 		close: 69.58528111643206,
694 | 	},
695 | 	{
696 | 		time: { year: 2018, month: 12, day: 27 },
697 | 		open: 66.38479296949795,
698 | 		high: 79.97207476893692,
699 | 		low: 59.738742243860464,
700 | 		close: 73.77893045661807,
701 | 	},
702 | 	{
703 | 		time: { year: 2018, month: 12, day: 28 },
704 | 		open: 73.80105714462456,
705 | 		high: 73.80105714462456,
706 | 		low: 59.95172576316864,
707 | 		close: 73.49823170047799,
708 | 	},
709 | 	{
710 | 		time: { year: 2018, month: 12, day: 29 },
711 | 		open: 75.65816205696441,
712 | 		high: 75.65816205696441,
713 | 		low: 63.710206287837266,
714 | 		close: 63.710206287837266,
715 | 	},
716 | 	{
717 | 		time: { year: 2018, month: 12, day: 30 },
718 | 		open: 70.43199072631421,
719 | 		high: 80.48229715762909,
720 | 		low: 62.65542750589909,
721 | 		close: 63.42588929424237,
722 | 	},
723 | 	{
724 | 		time: { year: 2018, month: 12, day: 31 },
725 | 		open: 74.18101512382138,
726 | 		high: 79.0918171034821,
727 | 		low: 57.80109358134577,
728 | 		close: 72.91361896511863,
729 | 	},
730 | 	// hide-end
731 | ];
732 | series.setData(data);
733 | 
734 | // determining the dates for the 'buy' and 'sell' markers added below.
735 | const datesForMarkers = [data[data.length - 39], data[data.length - 19]];
736 | let indexOfMinPrice = 0;
737 | for (let i = 1; i < datesForMarkers.length; i++) {
738 | 	if (datesForMarkers[i].high < datesForMarkers[indexOfMinPrice].high) {
739 | 		indexOfMinPrice = i;
740 | 	}
741 | }
742 | 
743 | // highlight-start
744 | const markers = [
745 | 	{
746 | 		time: data[data.length - 48].time,
747 | 		position: 'aboveBar',
748 | 		color: '#f68410',
749 | 		shape: 'circle',
750 | 		text: 'D',
751 | 	},
752 | ];
753 | for (let i = 0; i < datesForMarkers.length; i++) {
754 | 	if (i !== indexOfMinPrice) {
755 | 		markers.push({
756 | 			time: datesForMarkers[i].time,
757 | 			position: 'aboveBar',
758 | 			color: '#e91e63',
759 | 			shape: 'arrowDown',
760 | 			text: 'Sell @ ' + Math.floor(datesForMarkers[i].high + 2),
761 | 		});
762 | 	} else {
763 | 		markers.push({
764 | 			time: datesForMarkers[i].time,
765 | 			position: 'belowBar',
766 | 			color: '#2196F3',
767 | 			shape: 'arrowUp',
768 | 			text: 'Buy @ ' + Math.floor(datesForMarkers[i].low - 2),
769 | 		});
770 | 	}
771 | }
772 | /** @type {import('lightweight-charts').createSeriesMarkers} */
773 | createSeriesMarkers(series, markers);
774 | // highlight-end
775 | 
776 | chart.timeScale().fitContent();
777 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/series-markers.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Add Series Markers
 3 | sidebar_label: Series Markers
 4 | description: An example of how to add markers to a series on the chart.
 5 | pagination_prev: null
 6 | pagination_next: null
 7 | keywords:
 8 |   - series
 9 |   - markers
10 | ---
11 | 
12 | A series marker is an annotation which can be drawn on the chart at a specific point.
13 | It can be used to draw attention to specific events within the data set.
14 | This example shows how to add series markers to your chart.
15 | 
16 | ## Short answer
17 | 
18 | You can add markers to a series by passing an array of [`seriesMarker`](/docs/api/type-aliases/SeriesMarker)
19 | objects to the [`createSeriesMarkers`](/docs/next/api/functions/createSeriesMarkers) method on
20 | an [`ISeriesApi`](/docs/api/interfaces/ISeriesApi) instance.
21 | 
22 | ```js
23 | const markers = [
24 |     {
25 |         time: { year: 2018, month: 12, day: 23 },
26 |         position: 'aboveBar',
27 |         color: '#f68410',
28 |         shape: 'circle',
29 |         text: 'A',
30 |     },
31 | ];
32 | createSeriesMarkers(series, markers);
33 | ```
34 | 
35 | You can see a full [working example](#full-example) below.
36 | 
37 | ## Further information
38 | 
39 | A series marker is an annotation which can be attached to a specific data point within a series.
40 | We don't need to specify a vertical price value but rather only the `time` property since the
41 | marker will determine it's vertical position from the data points values (such as `high` and
42 | `low` in the case of candlestick data) and the specified `position` property ([SeriesMarkerPosition](/docs/api/type-aliases/SeriesMarkerPosition)).
43 | 
44 | ## Resources
45 | 
46 | You can view the related APIs here:
47 | - [SeriesMarker](/docs/api/type-aliases/SeriesMarker) - Series Marker interface.
48 | - [SeriesMarkerPosition](/docs/api/type-aliases/SeriesMarkerPosition) - Positions that can be set for the marker.
49 | - [SeriesMarkerShape](/docs/api/type-aliases/SeriesMarkerShape) - Shapes that can be set for the marker.
50 | - [createSeriesMarkers](/docs/next/api/functions/createSeriesMarkers) - Method for adding markers to a series.
51 | - [Time Types](/docs/api/type-aliases/Time) - Different time formats available to use.
52 | 
53 | ## Full example
54 | 
55 | import UsageGuidePartial from "../_usage-guide-partial.mdx";
56 | import CodeBlock from "@theme/CodeBlock";
57 | import code from "!!raw-loader!./series-markers.js";
58 | 
59 | <CodeBlock replaceThemeConstants chart className="language-js" hideableCode chartOnTop codeUsage={<UsageGuidePartial />}>
60 | 	{code}
61 | </CodeBlock>
62 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/set-crosshair-position-syncing.js:
--------------------------------------------------------------------------------
 1 | // remove-start
 2 | // Lightweight Charts™ Example: Crosshair syncing
 3 | // https://tradingview.github.io/lightweight-charts/tutorials/how_to/set-crosshair-position
 4 | // remove-end
 5 | 
 6 | // hide-start
 7 | function generateData(startValue, startDate) {
 8 | 	const res = [];
 9 | 	const time = startDate ?? (new Date(Date.UTC(2018, 0, 1, 0, 0, 0, 0)));
10 | 	for (let i = 0; i < 500; ++i) {
11 | 		res.push({
12 | 			time: time.getTime() / 1000,
13 | 			value: i + startValue,
14 | 		});
15 | 
16 | 		time.setUTCDate(time.getUTCDate() + 1);
17 | 	}
18 | 
19 | 	return res;
20 | }
21 | 
22 | const chart1 = createChart(
23 | 	document.getElementById('container'),
24 | 	{
25 | 		height: 250,
26 | 		crosshair: {
27 | 			mode: 0,
28 | 		},
29 | 		timeScale: {
30 | 			visible: false,
31 | 		},
32 | 		layout: {
33 | 			background: {
34 | 				type: 'solid',
35 | 				color: '#FFF5F5',
36 | 			},
37 | 		},
38 | 	}
39 | );
40 | const mainSeries1 = chart1.addSeries(LineSeries, {
41 | 	color: 'red',
42 | });
43 | 
44 | mainSeries1.setData(generateData(0));
45 | 
46 | const chart2 = createChart(
47 | 	document.getElementById('container'),
48 | 	{
49 | 		height: 250,
50 | 		layout: {
51 | 			background: {
52 | 				type: 'solid',
53 | 				color: '#F5F5FF',
54 | 			},
55 | 		},
56 | 	}
57 | );
58 | 
59 | const mainSeries2 = chart2.addSeries(LineSeries, {
60 | 	color: 'blue',
61 | });
62 | 
63 | mainSeries2.setData(generateData(100));
64 | // hide-end
65 | 
66 | chart1.timeScale().subscribeVisibleLogicalRangeChange(timeRange => {
67 | 	chart2.timeScale().setVisibleLogicalRange(timeRange);
68 | });
69 | 
70 | chart2.timeScale().subscribeVisibleLogicalRangeChange(timeRange => {
71 | 	chart1.timeScale().setVisibleLogicalRange(timeRange);
72 | });
73 | 
74 | function getCrosshairDataPoint(series, param) {
75 | 	if (!param.time) {
76 | 		return null;
77 | 	}
78 | 	const dataPoint = param.seriesData.get(series);
79 | 	return dataPoint || null;
80 | }
81 | 
82 | function syncCrosshair(chart, series, dataPoint) {
83 | 	if (dataPoint) {
84 | 		chart.setCrosshairPosition(dataPoint.value, dataPoint.time, series);
85 | 		return;
86 | 	}
87 | 	chart.clearCrosshairPosition();
88 | }
89 | chart1.subscribeCrosshairMove(param => {
90 | 	const dataPoint = getCrosshairDataPoint(mainSeries1, param);
91 | 	syncCrosshair(chart2, mainSeries2, dataPoint);
92 | });
93 | chart2.subscribeCrosshairMove(param => {
94 | 	const dataPoint = getCrosshairDataPoint(mainSeries2, param);
95 | 	syncCrosshair(chart1, mainSeries1, dataPoint);
96 | });
97 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/set-crosshair-position-tracking.js:
--------------------------------------------------------------------------------
 1 | // remove-start
 2 | // Lightweight Charts™ Example: Crosshair syncing
 3 | // https://tradingview.github.io/lightweight-charts/tutorials/how_to/set-crosshair-position
 4 | // remove-end
 5 | 
 6 | // hide-start
 7 | function generateData() {
 8 | 	const res = [];
 9 | 	const time = new Date(Date.UTC(2018, 0, 1, 0, 0, 0, 0));
10 | 	for (let i = 0; i < 500; ++i) {
11 | 		res.push({
12 | 			time: time.getTime() / 1000,
13 | 			value: i,
14 | 		});
15 | 
16 | 		time.setUTCDate(time.getUTCDate() + 1);
17 | 	}
18 | 
19 | 	return res;
20 | }
21 | 
22 | const chart = createChart(
23 | 	document.getElementById('container'),
24 | 	{
25 | 		handleScale: false,
26 | 		handleScroll: false,
27 | 	}
28 | );
29 | 
30 | const mainSeries = chart.addSeries({
31 | 	priceFormat: {
32 | 		minMove: 1,
33 | 		precision: 0,
34 | 	},
35 | });
36 | 
37 | mainSeries.setData(generateData());
38 | 
39 | chart.timeScale().fitContent();
40 | // hide-end
41 | 
42 | document.getElementById('container').addEventListener('touchmove', e => {
43 | 	const bcr = document.getElementById('container').getBoundingClientRect();
44 | 	const x = bcr.left + e.touches[0].clientX;
45 | 	const y = bcr.top + e.touches[0].clientY;
46 | 
47 | 	const price = mainSeries.coordinateToPrice(y);
48 | 	const time = chart.timeScale().coordinateToTime(x);
49 | 
50 | 	if (!Number.isFinite(price) || !Number.isFinite(time)) {
51 | 		return;
52 | 	}
53 | 
54 | 	chart.setCrosshairPosition(price, time, mainSeries);
55 | });
56 | 
57 | document.getElementById('container').addEventListener('touchend', () => {
58 | 	chart.clearCrosshairPosition();
59 | });
60 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/set-crosshair-position.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Set crosshair position
 3 | sidebar_label: Set crosshair position
 4 | description: Examples of how to add a programatically set the crosshair position.
 5 | pagination_prev: null
 6 | pagination_next: null
 7 | keywords:
 8 |   - crosshair
 9 |   - tracking
10 |   - example
11 | ---
12 | 
13 | import CodeBlock from "@theme/CodeBlock";
14 | 
15 | import MinimumVersionWrapper from "../../src/components/MinimumVersionWrapper";
16 | 
17 | Lightweight Charts™ allows the crosshair position to be set programatically using the [`setCrosshairPosition`](/docs/api/interfaces/IChartApi#setcrosshairposition), and cleared using [`clearCrosshairPosition`](/docs/api/interfaces/IChartApi#clearcrosshairposition).
18 | 
19 | Usually the crosshair position is set automatically by the user's actions. However in some cases you may want to set it explicitly. For example if you want to synchronise the crosshairs of two separate charts.
20 | 
21 | import syncingCode from "!!raw-loader!./set-crosshair-position-syncing.js";
22 | import trackingCode from "!!raw-loader!./set-crosshair-position-tracking.js";
23 | import VersionWarningAdmonition from "@site/src/components/VersionWarningAdmonition";
24 | 
25 | {/*
26 |   Show warning when not on the required version
27 |   Tutorials section isn't versioned yet, hence the need for the warning message
28 | */}
29 | 
30 | <MinimumVersionWrapper version={4.1} fallback={() => {
31 |   return (<VersionWarningAdmonition
32 |     notCurrent="These tutorials are for version 4.1 (or greater) of Lightweight Charts™."
33 |     type="caution"
34 |     displayVersionMessage
35 |   />);
36 | }}>
37 | 
38 |   ## Syncing two charts
39 | 
40 |   <CodeBlock replaceThemeConstants chart className="language-js" hideableCode iframeStyle={{ height: '500px' }} chartOnTop>
41 |     {syncingCode}
42 |   </CodeBlock>
43 | 
44 |   ## Tracking without long-press (on mobile)
45 | 
46 |   If scrolling and scaling is disabled, then the API can be used to enable a kind of tracking mode without the user having to long-press the screen.
47 | 
48 |   <CodeBlock replaceThemeConstants chart className="language-js" hideableCode chartOnTop>
49 |     {trackingCode}
50 |   </CodeBlock>
51 | 
52 | </MinimumVersionWrapper>
53 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/tooltip-floating.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Floating Tooltip
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/how_to/tooltips
  4 | 
  5 | // remove-end
  6 | const chartOptions = {
  7 | 	layout: {
  8 | 		textColor: CHART_TEXT_COLOR,
  9 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
 10 | 	},
 11 | };
 12 | // remove-line
 13 | /** @type {import('lightweight-charts').IChartApi} */
 14 | const chart = createChart(document.getElementById('container'), chartOptions);
 15 | 
 16 | chart.applyOptions({
 17 | 	crosshair: {
 18 | 		// hide the horizontal crosshair line
 19 | 		horzLine: {
 20 | 			visible: false,
 21 | 			labelVisible: false,
 22 | 		},
 23 | 		// hide the vertical crosshair label
 24 | 		vertLine: {
 25 | 			labelVisible: false,
 26 | 		},
 27 | 	},
 28 | 	// hide the grid lines
 29 | 	grid: {
 30 | 		vertLines: {
 31 | 			visible: false,
 32 | 		},
 33 | 		horzLines: {
 34 | 			visible: false,
 35 | 		},
 36 | 	},
 37 | });
 38 | const series = chart.addSeries(AreaSeries, {
 39 | 	topColor: AREA_TOP_COLOR,
 40 | 	bottomColor: AREA_BOTTOM_COLOR,
 41 | 	lineColor: LINE_LINE_COLOR,
 42 | 	lineWidth: 2,
 43 | 	crossHairMarkerVisible: false,
 44 | });
 45 | series.priceScale().applyOptions({
 46 | 	scaleMargins: {
 47 | 		top: 0.3, // leave some space for the legend
 48 | 		bottom: 0.25,
 49 | 	},
 50 | });
 51 | 
 52 | series.setData([
 53 | 	{ time: '2018-10-19', value: 26.19 },
 54 | 	// hide-start
 55 | 	{ time: '2018-10-22', value: 25.87 },
 56 | 	{ time: '2018-10-23', value: 25.83 },
 57 | 	{ time: '2018-10-24', value: 25.78 },
 58 | 	{ time: '2018-10-25', value: 25.82 },
 59 | 	{ time: '2018-10-26', value: 25.81 },
 60 | 	{ time: '2018-10-29', value: 25.82 },
 61 | 	{ time: '2018-10-30', value: 25.71 },
 62 | 	{ time: '2018-10-31', value: 25.82 },
 63 | 	{ time: '2018-11-01', value: 25.72 },
 64 | 	{ time: '2018-11-02', value: 25.74 },
 65 | 	{ time: '2018-11-05', value: 25.81 },
 66 | 	{ time: '2018-11-06', value: 25.75 },
 67 | 	{ time: '2018-11-07', value: 25.73 },
 68 | 	{ time: '2018-11-08', value: 25.75 },
 69 | 	{ time: '2018-11-09', value: 25.75 },
 70 | 	{ time: '2018-11-12', value: 25.76 },
 71 | 	{ time: '2018-11-13', value: 25.8 },
 72 | 	{ time: '2018-11-14', value: 25.77 },
 73 | 	{ time: '2018-11-15', value: 25.75 },
 74 | 	{ time: '2018-11-16', value: 25.75 },
 75 | 	{ time: '2018-11-19', value: 25.75 },
 76 | 	{ time: '2018-11-20', value: 25.72 },
 77 | 	{ time: '2018-11-21', value: 25.78 },
 78 | 	{ time: '2018-11-23', value: 25.72 },
 79 | 	{ time: '2018-11-26', value: 25.78 },
 80 | 	{ time: '2018-11-27', value: 25.85 },
 81 | 	{ time: '2018-11-28', value: 25.85 },
 82 | 	{ time: '2018-11-29', value: 25.55 },
 83 | 	{ time: '2018-11-30', value: 25.41 },
 84 | 	{ time: '2018-12-03', value: 25.41 },
 85 | 	{ time: '2018-12-04', value: 25.42 },
 86 | 	{ time: '2018-12-06', value: 25.33 },
 87 | 	{ time: '2018-12-07', value: 25.39 },
 88 | 	{ time: '2018-12-10', value: 25.32 },
 89 | 	{ time: '2018-12-11', value: 25.48 },
 90 | 	{ time: '2018-12-12', value: 25.39 },
 91 | 	{ time: '2018-12-13', value: 25.45 },
 92 | 	{ time: '2018-12-14', value: 25.52 },
 93 | 	{ time: '2018-12-17', value: 25.38 },
 94 | 	{ time: '2018-12-18', value: 25.36 },
 95 | 	{ time: '2018-12-19', value: 25.65 },
 96 | 	{ time: '2018-12-20', value: 25.7 },
 97 | 	{ time: '2018-12-21', value: 25.66 },
 98 | 	{ time: '2018-12-24', value: 25.66 },
 99 | 	{ time: '2018-12-26', value: 25.65 },
100 | 	{ time: '2018-12-27', value: 25.66 },
101 | 	{ time: '2018-12-28', value: 25.68 },
102 | 	{ time: '2018-12-31', value: 25.77 },
103 | 	{ time: '2019-01-02', value: 25.72 },
104 | 	{ time: '2019-01-03', value: 25.69 },
105 | 	{ time: '2019-01-04', value: 25.71 },
106 | 	{ time: '2019-01-07', value: 25.72 },
107 | 	{ time: '2019-01-08', value: 25.72 },
108 | 	{ time: '2019-01-09', value: 25.66 },
109 | 	{ time: '2019-01-10', value: 25.85 },
110 | 	{ time: '2019-01-11', value: 25.92 },
111 | 	{ time: '2019-01-14', value: 25.94 },
112 | 	{ time: '2019-01-15', value: 25.95 },
113 | 	{ time: '2019-01-16', value: 26.0 },
114 | 	{ time: '2019-01-17', value: 25.99 },
115 | 	{ time: '2019-01-18', value: 25.6 },
116 | 	{ time: '2019-01-22', value: 25.81 },
117 | 	{ time: '2019-01-23', value: 25.7 },
118 | 	{ time: '2019-01-24', value: 25.74 },
119 | 	{ time: '2019-01-25', value: 25.8 },
120 | 	{ time: '2019-01-28', value: 25.83 },
121 | 	{ time: '2019-01-29', value: 25.7 },
122 | 	{ time: '2019-01-30', value: 25.78 },
123 | 	{ time: '2019-01-31', value: 25.35 },
124 | 	{ time: '2019-02-01', value: 25.6 },
125 | 	{ time: '2019-02-04', value: 25.65 },
126 | 	{ time: '2019-02-05', value: 25.73 },
127 | 	{ time: '2019-02-06', value: 25.71 },
128 | 	{ time: '2019-02-07', value: 25.71 },
129 | 	{ time: '2019-02-08', value: 25.72 },
130 | 	{ time: '2019-02-11', value: 25.76 },
131 | 	{ time: '2019-02-12', value: 25.84 },
132 | 	{ time: '2019-02-13', value: 25.85 },
133 | 	{ time: '2019-02-14', value: 25.87 },
134 | 	{ time: '2019-02-15', value: 25.89 },
135 | 	{ time: '2019-02-19', value: 25.9 },
136 | 	{ time: '2019-02-20', value: 25.92 },
137 | 	{ time: '2019-02-21', value: 25.96 },
138 | 	{ time: '2019-02-22', value: 26.0 },
139 | 	{ time: '2019-02-25', value: 25.93 },
140 | 	{ time: '2019-02-26', value: 25.92 },
141 | 	{ time: '2019-02-27', value: 25.67 },
142 | 	{ time: '2019-02-28', value: 25.79 },
143 | 	{ time: '2019-03-01', value: 25.86 },
144 | 	{ time: '2019-03-04', value: 25.94 },
145 | 	{ time: '2019-03-05', value: 26.02 },
146 | 	{ time: '2019-03-06', value: 25.95 },
147 | 	{ time: '2019-03-07', value: 25.89 },
148 | 	{ time: '2019-03-08', value: 25.94 },
149 | 	{ time: '2019-03-11', value: 25.91 },
150 | 	{ time: '2019-03-12', value: 25.92 },
151 | 	{ time: '2019-03-13', value: 26.0 },
152 | 	{ time: '2019-03-14', value: 26.05 },
153 | 	{ time: '2019-03-15', value: 26.11 },
154 | 	{ time: '2019-03-18', value: 26.1 },
155 | 	{ time: '2019-03-19', value: 25.98 },
156 | 	{ time: '2019-03-20', value: 26.11 },
157 | 	{ time: '2019-03-21', value: 26.12 },
158 | 	{ time: '2019-03-22', value: 25.88 },
159 | 	{ time: '2019-03-25', value: 25.85 },
160 | 	{ time: '2019-03-26', value: 25.72 },
161 | 	{ time: '2019-03-27', value: 25.73 },
162 | 	{ time: '2019-03-28', value: 25.8 },
163 | 	{ time: '2019-03-29', value: 25.77 },
164 | 	{ time: '2019-04-01', value: 26.06 },
165 | 	{ time: '2019-04-02', value: 25.93 },
166 | 	{ time: '2019-04-03', value: 25.95 },
167 | 	{ time: '2019-04-04', value: 26.06 },
168 | 	{ time: '2019-04-05', value: 26.16 },
169 | 	{ time: '2019-04-08', value: 26.12 },
170 | 	{ time: '2019-04-09', value: 26.07 },
171 | 	{ time: '2019-04-10', value: 26.13 },
172 | 	{ time: '2019-04-11', value: 26.04 },
173 | 	{ time: '2019-04-12', value: 26.04 },
174 | 	{ time: '2019-04-15', value: 26.05 },
175 | 	{ time: '2019-04-16', value: 26.01 },
176 | 	{ time: '2019-04-17', value: 26.09 },
177 | 	{ time: '2019-04-18', value: 26.0 },
178 | 	{ time: '2019-04-22', value: 26.0 },
179 | 	{ time: '2019-04-23', value: 26.06 },
180 | 	{ time: '2019-04-24', value: 26.0 },
181 | 	{ time: '2019-04-25', value: 25.81 },
182 | 	{ time: '2019-04-26', value: 25.88 },
183 | 	{ time: '2019-04-29', value: 25.91 },
184 | 	{ time: '2019-04-30', value: 25.9 },
185 | 	{ time: '2019-05-01', value: 26.02 },
186 | 	{ time: '2019-05-02', value: 25.97 },
187 | 	{ time: '2019-05-03', value: 26.02 },
188 | 	{ time: '2019-05-06', value: 26.03 },
189 | 	{ time: '2019-05-07', value: 26.04 },
190 | 	{ time: '2019-05-08', value: 26.05 },
191 | 	{ time: '2019-05-09', value: 26.05 },
192 | 	{ time: '2019-05-10', value: 26.08 },
193 | 	{ time: '2019-05-13', value: 26.05 },
194 | 	{ time: '2019-05-14', value: 26.01 },
195 | 	{ time: '2019-05-15', value: 26.03 },
196 | 	{ time: '2019-05-16', value: 26.14 },
197 | 	{ time: '2019-05-17', value: 26.09 },
198 | 	{ time: '2019-05-20', value: 26.01 },
199 | 	{ time: '2019-05-21', value: 26.12 },
200 | 	{ time: '2019-05-22', value: 26.15 },
201 | 	{ time: '2019-05-23', value: 26.18 },
202 | 	{ time: '2019-05-24', value: 26.16 },
203 | 	{ time: '2019-05-28', value: 26.23 },
204 | 	// hide-end
205 | ]);
206 | 
207 | const container = document.getElementById('container');
208 | 
209 | const toolTipWidth = 80;
210 | const toolTipHeight = 80;
211 | const toolTipMargin = 15;
212 | 
213 | // Create and style the tooltip html element
214 | const toolTip = document.createElement('div');
215 | toolTip.style = `width: 96px; height: 80px; position: absolute; display: none; padding: 8px; box-sizing: border-box; font-size: 12px; text-align: left; z-index: 1000; top: 12px; left: 12px; pointer-events: none; border: 1px solid; border-radius: 2px;font-family: -apple-system, BlinkMacSystemFont, 'Trebuchet MS', Roboto, Ubuntu, sans-serif; -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;`;
216 | toolTip.style.background = CHART_BACKGROUND_COLOR;
217 | toolTip.style.color = CHART_TEXT_COLOR;
218 | toolTip.style.borderColor = LINE_LINE_COLOR;
219 | container.appendChild(toolTip);
220 | 
221 | // update tooltip
222 | chart.subscribeCrosshairMove(param => {
223 | 	if (
224 | 		param.point === undefined ||
225 | 		!param.time ||
226 | 		param.point.x < 0 ||
227 | 		param.point.x > container.clientWidth ||
228 | 		param.point.y < 0 ||
229 | 		param.point.y > container.clientHeight
230 | 	) {
231 | 		toolTip.style.display = 'none';
232 | 	} else {
233 | 		// time will be in the same format that we supplied to setData.
234 | 		// thus it will be YYYY-MM-DD
235 | 		const dateStr = param.time;
236 | 		toolTip.style.display = 'block';
237 | 		const data = param.seriesData.get(series);
238 | 		const price = data.value !== undefined ? data.value : data.close;
239 | 		toolTip.innerHTML = `<div style="color: ${LINE_LINE_COLOR}">Apple Inc.</div><div style="font-size: 24px; margin: 4px 0px; color: ${CHART_TEXT_COLOR}">
240 | 			${Math.round(100 * price) / 100}
241 | 			</div><div style="color: ${CHART_TEXT_COLOR}">
242 | 			${dateStr}
243 | 			</div>`;
244 | 
245 | 		// highlight-start
246 | 		const coordinate = series.priceToCoordinate(price);
247 | 		let shiftedCoordinate = param.point.x - 50;
248 | 		if (coordinate === null) {
249 | 			return;
250 | 		}
251 | 		shiftedCoordinate = Math.max(
252 | 			0,
253 | 			Math.min(container.clientWidth - toolTipWidth, shiftedCoordinate)
254 | 		);
255 | 		const coordinateY =
256 | 			coordinate - toolTipHeight - toolTipMargin > 0
257 | 				? coordinate - toolTipHeight - toolTipMargin
258 | 				: Math.max(
259 | 					0,
260 | 					Math.min(
261 | 						container.clientHeight - toolTipHeight - toolTipMargin,
262 | 						coordinate + toolTipMargin
263 | 					)
264 | 				);
265 | 		toolTip.style.left = shiftedCoordinate + 'px';
266 | 		toolTip.style.top = coordinateY + 'px';
267 | 		// highlight-end
268 | 	}
269 | });
270 | 
271 | chart.timeScale().fitContent();
272 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/tooltip-magnifier.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Magnifier Tooltip
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/how_to/tooltips
  4 | 
  5 | // remove-end
  6 | const chartOptions = {
  7 | 	layout: {
  8 | 		textColor: CHART_TEXT_COLOR,
  9 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
 10 | 	},
 11 | };
 12 | // remove-line
 13 | /** @type {import('lightweight-charts').IChartApi} */
 14 | const chart = createChart(document.getElementById('container'), chartOptions);
 15 | 
 16 | chart.applyOptions({
 17 | 	leftPriceScale: {
 18 | 		visible: true,
 19 | 		borderVisible: false,
 20 | 	},
 21 | 	rightPriceScale: {
 22 | 		visible: false,
 23 | 	},
 24 | 	timeScale: {
 25 | 		borderVisible: false,
 26 | 	},
 27 | 	crosshair: {
 28 | 		horzLine: {
 29 | 			visible: false,
 30 | 			labelVisible: false,
 31 | 		},
 32 | 		vertLine: {
 33 | 			visible: true,
 34 | 			style: 0,
 35 | 			width: 2,
 36 | 			color: 'rgba(32, 38, 46, 0.1)',
 37 | 			labelVisible: false,
 38 | 		},
 39 | 	},
 40 | 	// hide the grid lines
 41 | 	grid: {
 42 | 		vertLines: {
 43 | 			visible: false,
 44 | 		},
 45 | 		horzLines: {
 46 | 			visible: false,
 47 | 		},
 48 | 	},
 49 | });
 50 | 
 51 | const series = chart.addSeries(AreaSeries, {
 52 | 	topColor: BASELINE_BOTTOM_FILL_COLOR1,
 53 | 	bottomColor: BASELINE_BOTTOM_FILL_COLOR2,
 54 | 	lineColor: BASELINE_BOTTOM_LINE_COLOR,
 55 | 	lineWidth: 2,
 56 | 	crossHairMarkerVisible: false,
 57 | 	priceLineVisible: false,
 58 | 	lastValueVisible: false,
 59 | });
 60 | series.priceScale().applyOptions({
 61 | 	scaleMargins: {
 62 | 		top: 0.3, // leave some space for the legend
 63 | 		bottom: 0.25,
 64 | 	},
 65 | });
 66 | 
 67 | series.setData([
 68 | 	{ time: '2018-03-28', value: 154 },
 69 | 	// hide-start
 70 | 	{ time: '2018-03-29', value: 154.2 },
 71 | 	{ time: '2018-03-30', value: 155.60001 },
 72 | 	{ time: '2018-04-02', value: 156.25 },
 73 | 	{ time: '2018-04-03', value: 156.25 },
 74 | 	{ time: '2018-04-04', value: 156.05 },
 75 | 	{ time: '2018-04-05', value: 158.05 },
 76 | 	{ time: '2018-04-06', value: 157.3 },
 77 | 	{ time: '2018-04-09', value: 144 },
 78 | 	{ time: '2018-04-10', value: 144.8 },
 79 | 	{ time: '2018-04-11', value: 143.5 },
 80 | 	{ time: '2018-04-12', value: 147.05 },
 81 | 	{ time: '2018-04-13', value: 144.85001 },
 82 | 	{ time: '2018-04-16', value: 145.39999 },
 83 | 	{ time: '2018-04-17', value: 147.3 },
 84 | 	{ time: '2018-04-18', value: 153.55 },
 85 | 	{ time: '2018-04-19', value: 150.95 },
 86 | 	{ time: '2018-04-20', value: 149.39999 },
 87 | 	{ time: '2018-04-23', value: 148.5 },
 88 | 	{ time: '2018-04-24', value: 146.60001 },
 89 | 	{ time: '2018-04-25', value: 144.45 },
 90 | 	{ time: '2018-04-26', value: 145.60001 },
 91 | 	{ time: '2018-04-27', value: 144.3 },
 92 | 	{ time: '2018-04-30', value: 144 },
 93 | 	{ time: '2018-05-02', value: 147.3 },
 94 | 	{ time: '2018-05-03', value: 144.2 },
 95 | 	{ time: '2018-05-04', value: 141.64999 },
 96 | 	{ time: '2018-05-07', value: 141.89999 },
 97 | 	{ time: '2018-05-08', value: 140.39999 },
 98 | 	{ time: '2018-05-10', value: 139.8 },
 99 | 	{ time: '2018-05-11', value: 137.5 },
100 | 	{ time: '2018-05-14', value: 136.14999 },
101 | 	{ time: '2018-05-15', value: 138 },
102 | 	{ time: '2018-05-16', value: 137.95 },
103 | 	{ time: '2018-05-17', value: 137.95 },
104 | 	{ time: '2018-05-18', value: 136.75 },
105 | 	{ time: '2018-05-21', value: 136.2 },
106 | 	{ time: '2018-05-22', value: 135 },
107 | 	{ time: '2018-05-23', value: 132.55 },
108 | 	{ time: '2018-05-24', value: 132.7 },
109 | 	{ time: '2018-05-25', value: 132.2 },
110 | 	{ time: '2018-05-28', value: 131.55 },
111 | 	{ time: '2018-05-29', value: 131.85001 },
112 | 	{ time: '2018-05-30', value: 139.85001 },
113 | 	{ time: '2018-05-31', value: 140.8 },
114 | 	{ time: '2018-06-01', value: 139.64999 },
115 | 	{ time: '2018-06-04', value: 137.10001 },
116 | 	{ time: '2018-06-05', value: 139.25 },
117 | 	{ time: '2018-06-06', value: 141.3 },
118 | 	{ time: '2018-06-07', value: 145 },
119 | 	{ time: '2018-06-08', value: 143.89999 },
120 | 	{ time: '2018-06-11', value: 142.7 },
121 | 	{ time: '2018-06-13', value: 144.05 },
122 | 	{ time: '2018-06-14', value: 143.55 },
123 | 	{ time: '2018-06-15', value: 140.5 },
124 | 	{ time: '2018-06-18', value: 139.64999 },
125 | 	{ time: '2018-06-19', value: 138 },
126 | 	{ time: '2018-06-20', value: 141 },
127 | 	{ time: '2018-06-21', value: 140.55 },
128 | 	{ time: '2018-06-22', value: 140.55 },
129 | 	{ time: '2018-06-25', value: 140.75 },
130 | 	{ time: '2018-06-26', value: 140.64999 },
131 | 	{ time: '2018-06-27', value: 141.14999 },
132 | 	{ time: '2018-06-28', value: 139.8 },
133 | 	{ time: '2018-06-29', value: 139.8 },
134 | 	{ time: '2018-07-02', value: 140.14999 },
135 | 	{ time: '2018-07-03', value: 143.05 },
136 | 	{ time: '2018-07-04', value: 140 },
137 | 	{ time: '2018-07-05', value: 129.2 },
138 | 	{ time: '2018-07-06', value: 129.55 },
139 | 	{ time: '2018-07-09', value: 128.3 },
140 | 	{ time: '2018-07-10', value: 126.55 },
141 | 	{ time: '2018-07-11', value: 124.3 },
142 | 	{ time: '2018-07-12', value: 124.8 },
143 | 	{ time: '2018-07-13', value: 123.25 },
144 | 	{ time: '2018-07-16', value: 123 },
145 | 	{ time: '2018-07-17', value: 124.25 },
146 | 	{ time: '2018-07-18', value: 123 },
147 | 	{ time: '2018-07-19', value: 121 },
148 | 	{ time: '2018-07-20', value: 121.45 },
149 | 	{ time: '2018-07-23', value: 123.8 },
150 | 	{ time: '2018-07-24', value: 122.15 },
151 | 	{ time: '2018-07-25', value: 121.3 },
152 | 	{ time: '2018-07-26', value: 122.7 },
153 | 	{ time: '2018-07-27', value: 122.2 },
154 | 	{ time: '2018-07-30', value: 121.7 },
155 | 	{ time: '2018-07-31', value: 122.95 },
156 | 	{ time: '2018-08-01', value: 121 },
157 | 	{ time: '2018-08-02', value: 116 },
158 | 	{ time: '2018-08-03', value: 118.1 },
159 | 	{ time: '2018-08-06', value: 114.3 },
160 | 	{ time: '2018-08-07', value: 114.25 },
161 | 	{ time: '2018-08-08', value: 111.85 },
162 | 	{ time: '2018-08-09', value: 109.7 },
163 | 	{ time: '2018-08-10', value: 105 },
164 | 	{ time: '2018-08-13', value: 105.75 },
165 | 	{ time: '2018-08-14', value: 107.25 },
166 | 	{ time: '2018-08-15', value: 107.4 },
167 | 	{ time: '2018-08-16', value: 110.5 },
168 | 	{ time: '2018-08-17', value: 109 },
169 | 	{ time: '2018-08-20', value: 108.95 },
170 | 	{ time: '2018-08-21', value: 108.35 },
171 | 	{ time: '2018-08-22', value: 108.6 },
172 | 	{ time: '2018-08-23', value: 105.65 },
173 | 	{ time: '2018-08-24', value: 104.45 },
174 | 	{ time: '2018-08-27', value: 106.2 },
175 | 	{ time: '2018-08-28', value: 106.55 },
176 | 	{ time: '2018-08-29', value: 111.8 },
177 | 	{ time: '2018-08-30', value: 115.5 },
178 | 	{ time: '2018-08-31', value: 115.5 },
179 | 	{ time: '2018-09-03', value: 114.55 },
180 | 	{ time: '2018-09-04', value: 112.75 },
181 | 	{ time: '2018-09-05', value: 111.5 },
182 | 	{ time: '2018-09-06', value: 108.1 },
183 | 	{ time: '2018-09-07', value: 108.55 },
184 | 	{ time: '2018-09-10', value: 106.5 },
185 | 	{ time: '2018-09-11', value: 105.1 },
186 | 	{ time: '2018-09-12', value: 107.2 },
187 | 	{ time: '2018-09-13', value: 107.1 },
188 | 	{ time: '2018-09-14', value: 105.75 },
189 | 	{ time: '2018-09-17', value: 106.05 },
190 | 	{ time: '2018-09-18', value: 109.15 },
191 | 	{ time: '2018-09-19', value: 111.4 },
192 | 	{ time: '2018-09-20', value: 111 },
193 | 	{ time: '2018-09-21', value: 111 },
194 | 	{ time: '2018-09-24', value: 108.95 },
195 | 	{ time: '2018-09-25', value: 106.65 },
196 | 	{ time: '2018-09-26', value: 106.7 },
197 | 	{ time: '2018-09-27', value: 107.05 },
198 | 	{ time: '2018-09-28', value: 106.55 },
199 | 	{ time: '2018-10-01', value: 106.2 },
200 | 	{ time: '2018-10-02', value: 106.4 },
201 | 	{ time: '2018-10-03', value: 107.1 },
202 | 	{ time: '2018-10-04', value: 106.4 },
203 | 	{ time: '2018-10-05', value: 104.65 },
204 | 	{ time: '2018-10-08', value: 102.65 },
205 | 	{ time: '2018-10-09', value: 102.1 },
206 | 	{ time: '2018-10-10', value: 102.15 },
207 | 	{ time: '2018-10-11', value: 100.9 },
208 | 	{ time: '2018-10-12', value: 102 },
209 | 	{ time: '2018-10-15', value: 100.15 },
210 | 	{ time: '2018-10-16', value: 99 },
211 | 	{ time: '2018-10-17', value: 98 },
212 | 	{ time: '2018-10-18', value: 96 },
213 | 	{ time: '2018-10-19', value: 95.5 },
214 | 	{ time: '2018-10-22', value: 92.400002 },
215 | 	{ time: '2018-10-23', value: 92.300003 },
216 | 	{ time: '2018-10-24', value: 92.900002 },
217 | 	{ time: '2018-10-25', value: 91.849998 },
218 | 	{ time: '2018-10-26', value: 91.599998 },
219 | 	{ time: '2018-10-29', value: 94.050003 },
220 | 	{ time: '2018-10-30', value: 98.25 },
221 | 	{ time: '2018-10-31', value: 97.25 },
222 | 	{ time: '2018-11-01', value: 96.879997 },
223 | 	{ time: '2018-11-02', value: 101.78 },
224 | 	{ time: '2018-11-06', value: 102.4 },
225 | 	{ time: '2018-11-07', value: 100.6 },
226 | 	{ time: '2018-11-08', value: 98.5 },
227 | 	{ time: '2018-11-09', value: 95.139999 },
228 | 	{ time: '2018-11-12', value: 96.900002 },
229 | 	{ time: '2018-11-13', value: 97.400002 },
230 | 	{ time: '2018-11-14', value: 103.3 },
231 | 	{ time: '2018-11-15', value: 102.74 },
232 | 	{ time: '2018-11-16', value: 101.2 },
233 | 	{ time: '2018-11-19', value: 98.720001 },
234 | 	{ time: '2018-11-20', value: 102.2 },
235 | 	{ time: '2018-11-21', value: 108.8 },
236 | 	{ time: '2018-11-22', value: 109.9 },
237 | 	{ time: '2018-11-23', value: 113.74 },
238 | 	{ time: '2018-11-26', value: 110.9 },
239 | 	{ time: '2018-11-27', value: 113.28 },
240 | 	{ time: '2018-11-28', value: 113.6 },
241 | 	{ time: '2018-11-29', value: 113.14 },
242 | 	{ time: '2018-11-30', value: 114.4 },
243 | 	{ time: '2018-12-03', value: 111.84 },
244 | 	{ time: '2018-12-04', value: 106.7 },
245 | 	{ time: '2018-12-05', value: 107.8 },
246 | 	{ time: '2018-12-06', value: 106.44 },
247 | 	{ time: '2018-12-07', value: 103.7 },
248 | 	{ time: '2018-12-10', value: 101.02 },
249 | 	{ time: '2018-12-11', value: 102.72 },
250 | 	{ time: '2018-12-12', value: 101.8 },
251 | 	{ time: '2018-12-13', value: 102 },
252 | 	{ time: '2018-12-14', value: 102.1 },
253 | 	{ time: '2018-12-17', value: 101.04 },
254 | 	{ time: '2018-12-18', value: 101.6 },
255 | 	{ time: '2018-12-19', value: 102 },
256 | 	{ time: '2018-12-20', value: 102.02 },
257 | 	{ time: '2018-12-21', value: 102.2 },
258 | 	{ time: '2018-12-24', value: 102.1 },
259 | 	{ time: '2018-12-25', value: 100.8 },
260 | 	{ time: '2018-12-26', value: 101.02 },
261 | 	{ time: '2018-12-27', value: 100.5 },
262 | 	{ time: '2018-12-28', value: 101 },
263 | 	{ time: '2019-01-03', value: 101.5 },
264 | 	{ time: '2019-01-04', value: 101.1 },
265 | 	{ time: '2019-01-08', value: 101.1 },
266 | 	{ time: '2019-01-09', value: 102.06 },
267 | 	{ time: '2019-01-10', value: 105.14 },
268 | 	{ time: '2019-01-11', value: 104.66 },
269 | 	{ time: '2019-01-14', value: 106.22 },
270 | 	{ time: '2019-01-15', value: 106.98 },
271 | 	{ time: '2019-01-16', value: 108.4 },
272 | 	{ time: '2019-01-17', value: 109.06 },
273 | 	{ time: '2019-01-18', value: 107 },
274 | 	{ time: '2019-01-21', value: 105.8 },
275 | 	{ time: '2019-01-22', value: 105.24 },
276 | 	{ time: '2019-01-23', value: 105.4 },
277 | 	{ time: '2019-01-24', value: 105.38 },
278 | 	{ time: '2019-01-25', value: 105.7 },
279 | 	{ time: '2019-01-28', value: 105.8 },
280 | 	{ time: '2019-01-29', value: 106.1 },
281 | 	{ time: '2019-01-30', value: 108.6 },
282 | 	{ time: '2019-01-31', value: 107.92 },
283 | 	{ time: '2019-02-01', value: 105.22 },
284 | 	{ time: '2019-02-04', value: 102.44 },
285 | 	{ time: '2019-02-05', value: 102.26 },
286 | 	{ time: '2019-02-06', value: 102 },
287 | 	{ time: '2019-02-07', value: 101.62 },
288 | 	{ time: '2019-02-08', value: 101.9 },
289 | 	{ time: '2019-02-11', value: 101.78 },
290 | 	{ time: '2019-02-12', value: 102.7 },
291 | 	{ time: '2019-02-13', value: 100.14 },
292 | 	{ time: '2019-02-14', value: 101.36 },
293 | 	{ time: '2019-02-15', value: 101.62 },
294 | 	{ time: '2019-02-18', value: 100.74 },
295 | 	{ time: '2019-02-19', value: 100 },
296 | 	{ time: '2019-02-20', value: 100.04 },
297 | 	{ time: '2019-02-21', value: 100 },
298 | 	{ time: '2019-02-22', value: 100.12 },
299 | 	{ time: '2019-02-25', value: 100.04 },
300 | 	{ time: '2019-02-26', value: 98.980003 },
301 | 	{ time: '2019-02-27', value: 97.699997 },
302 | 	{ time: '2019-02-28', value: 97.099998 },
303 | 	{ time: '2019-03-01', value: 96.760002 },
304 | 	{ time: '2019-03-04', value: 98.360001 },
305 | 	{ time: '2019-03-05', value: 96.260002 },
306 | 	{ time: '2019-03-06', value: 98.120003 },
307 | 	{ time: '2019-03-07', value: 99.68 },
308 | 	{ time: '2019-03-11', value: 102.1 },
309 | 	{ time: '2019-03-12', value: 100.22 },
310 | 	{ time: '2019-03-13', value: 100.5 },
311 | 	{ time: '2019-03-14', value: 99.660004 },
312 | 	{ time: '2019-03-15', value: 100.08 },
313 | 	{ time: '2019-03-18', value: 99.919998 },
314 | 	{ time: '2019-03-19', value: 99.459999 },
315 | 	{ time: '2019-03-20', value: 98.220001 },
316 | 	{ time: '2019-03-21', value: 97.300003 },
317 | 	{ time: '2019-03-22', value: 97.660004 },
318 | 	{ time: '2019-03-25', value: 97 },
319 | 	{ time: '2019-03-26', value: 97.019997 },
320 | 	{ time: '2019-03-27', value: 96.099998 },
321 | 	{ time: '2019-03-28', value: 96.699997 },
322 | 	{ time: '2019-03-29', value: 96.300003 },
323 | 	{ time: '2019-04-01', value: 97.779999 },
324 | 	{ time: '2019-04-02', value: 98.360001 },
325 | 	{ time: '2019-04-03', value: 98.5 },
326 | 	{ time: '2019-04-04', value: 98.360001 },
327 | 	{ time: '2019-04-05', value: 99.540001 },
328 | 	{ time: '2019-04-08', value: 98.580002 },
329 | 	{ time: '2019-04-09', value: 97.239998 },
330 | 	{ time: '2019-04-10', value: 97.32 },
331 | 	{ time: '2019-04-11', value: 98.400002 },
332 | 	{ time: '2019-04-12', value: 98.220001 },
333 | 	{ time: '2019-04-15', value: 98.720001 },
334 | 	{ time: '2019-04-16', value: 99.120003 },
335 | 	{ time: '2019-04-17', value: 98.620003 },
336 | 	{ time: '2019-04-18', value: 98 },
337 | 	{ time: '2019-04-19', value: 97.599998 },
338 | 	{ time: '2019-04-22', value: 97.599998 },
339 | 	{ time: '2019-04-23', value: 96.800003 },
340 | 	{ time: '2019-04-24', value: 96.32 },
341 | 	{ time: '2019-04-25', value: 96.339996 },
342 | 	{ time: '2019-04-26', value: 97.120003 },
343 | 	{ time: '2019-04-29', value: 96.980003 },
344 | 	{ time: '2019-04-30', value: 96.32 },
345 | 	{ time: '2019-05-02', value: 96.860001 },
346 | 	{ time: '2019-05-03', value: 96.699997 },
347 | 	{ time: '2019-05-06', value: 94.940002 },
348 | 	{ time: '2019-05-07', value: 94.5 },
349 | 	{ time: '2019-05-08', value: 94.239998 },
350 | 	{ time: '2019-05-10', value: 92.900002 },
351 | 	{ time: '2019-05-13', value: 91.279999 },
352 | 	{ time: '2019-05-14', value: 91.599998 },
353 | 	{ time: '2019-05-15', value: 90.080002 },
354 | 	{ time: '2019-05-16', value: 91.68 },
355 | 	{ time: '2019-05-17', value: 91.959999 },
356 | 	{ time: '2019-05-20', value: 91.080002 },
357 | 	{ time: '2019-05-21', value: 90.760002 },
358 | 	{ time: '2019-05-22', value: 91 },
359 | 	{ time: '2019-05-23', value: 90.739998 },
360 | 	{ time: '2019-05-24', value: 91 },
361 | 	{ time: '2019-05-27', value: 91.199997 },
362 | 	{ time: '2019-05-28', value: 90.68 },
363 | 	{ time: '2019-05-29', value: 91.120003 },
364 | 	{ time: '2019-05-30', value: 90.419998 },
365 | 	{ time: '2019-05-31', value: 93.800003 },
366 | 	{ time: '2019-06-03', value: 96.800003 },
367 | 	{ time: '2019-06-04', value: 96.34 },
368 | 	{ time: '2019-06-05', value: 95.94 },
369 | 	// hide-end
370 | ]);
371 | 
372 | const container = document.getElementById('container');
373 | 
374 | const toolTipWidth = 96;
375 | 
376 | // Create and style the tooltip html element
377 | const toolTip = document.createElement('div');
378 | toolTip.style = `width: ${toolTipWidth}px; height: 300px; position: absolute; display: none; padding: 8px; box-sizing: border-box; font-size: 12px; text-align: left; z-index: 1000; top: 12px; left: 12px; pointer-events: none; border-radius: 4px 4px 0px 0px; border-bottom: none; box-shadow: 0 2px 5px 0 rgba(117, 134, 150, 0.45);font-family: -apple-system, BlinkMacSystemFont, 'Trebuchet MS', Roboto, Ubuntu, sans-serif; -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;`;
379 | toolTip.style.background = `rgba(${CHART_BACKGROUND_RGB_COLOR}, 0.25)`;
380 | toolTip.style.color = CHART_TEXT_COLOR;
381 | toolTip.style.borderColor = BASELINE_BOTTOM_LINE_COLOR;
382 | container.appendChild(toolTip);
383 | 
384 | // update tooltip
385 | chart.subscribeCrosshairMove(param => {
386 | 	if (
387 | 		param.point === undefined ||
388 | 		!param.time ||
389 | 		param.point.x < 0 ||
390 | 		param.point.x > container.clientWidth ||
391 | 		param.point.y < 0 ||
392 | 		param.point.y > container.clientHeight
393 | 	) {
394 | 		toolTip.style.display = 'none';
395 | 	} else {
396 | 		// time will be in the same format that we supplied to setData.
397 | 		// thus it will be YYYY-MM-DD
398 | 		const dateStr = param.time;
399 | 		toolTip.style.display = 'block';
400 | 		const data = param.seriesData.get(series);
401 | 		const price = data.value !== undefined ? data.value : data.close;
402 | 		toolTip.innerHTML = `<div style="color: ${BASELINE_BOTTOM_LINE_COLOR}">⬤ ABC Inc.</div><div style="font-size: 24px; margin: 4px 0px; color: ${CHART_TEXT_COLOR}">
403 | 			${Math.round(100 * price) / 100}
404 | 			</div><div style="color: ${CHART_TEXT_COLOR}">
405 | 			${dateStr}
406 | 			</div>`;
407 | 
408 | 		// highlight-start
409 | 		let left = param.point.x; // relative to timeScale
410 | 		const timeScaleWidth = chart.timeScale().width();
411 | 		const priceScaleWidth = chart.priceScale('left').width();
412 | 		const halfTooltipWidth = toolTipWidth / 2;
413 | 		left += priceScaleWidth - halfTooltipWidth;
414 | 		left = Math.min(left, priceScaleWidth + timeScaleWidth - toolTipWidth);
415 | 		left = Math.max(left, priceScaleWidth);
416 | 
417 | 		toolTip.style.left = left + 'px';
418 | 		toolTip.style.top = 0 + 'px';
419 | 		// highlight-end
420 | 	}
421 | });
422 | 
423 | chart.timeScale().fitContent();
424 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/tooltip-tracking.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Tracking Tooltip
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/how_to/tooltips
  4 | 
  5 | // remove-end
  6 | const chartOptions = {
  7 | 	layout: {
  8 | 		textColor: CHART_TEXT_COLOR,
  9 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
 10 | 	},
 11 | };
 12 | // remove-line
 13 | /** @type {import('lightweight-charts').IChartApi} */
 14 | const chart = createChart(document.getElementById('container'), chartOptions);
 15 | 
 16 | chart.applyOptions({
 17 | 	rightPriceScale: {
 18 | 		scaleMargins: {
 19 | 			top: 0.3, // leave some space for the legend
 20 | 			bottom: 0.25,
 21 | 		},
 22 | 	},
 23 | 	crosshair: {
 24 | 		// hide the horizontal crosshair line
 25 | 		horzLine: {
 26 | 			visible: false,
 27 | 			labelVisible: false,
 28 | 		},
 29 | 		// hide the vertical crosshair label
 30 | 		vertLine: {
 31 | 			labelVisible: false,
 32 | 		},
 33 | 	},
 34 | 	// hide the grid lines
 35 | 	grid: {
 36 | 		vertLines: {
 37 | 			visible: false,
 38 | 		},
 39 | 		horzLines: {
 40 | 			visible: false,
 41 | 		},
 42 | 	},
 43 | });
 44 | 
 45 | const series = chart.addSeries(AreaSeries, {
 46 | 	topColor: BASELINE_TOP_FILL_COLOR1,
 47 | 	bottomColor: BASELINE_TOP_FILL_COLOR2,
 48 | 	lineColor: BASELINE_TOP_LINE_COLOR,
 49 | 	lineWidth: 2,
 50 | 	crossHairMarkerVisible: false,
 51 | });
 52 | 
 53 | series.setData([
 54 | 	{ time: '2016-07-18', value: 98.66 },
 55 | 	// hide-start
 56 | 	{ time: '2016-07-25', value: 104.21 },
 57 | 	{ time: '2016-08-01', value: 107.48 },
 58 | 	{ time: '2016-08-08', value: 108.18 },
 59 | 	{ time: '2016-08-15', value: 109.36 },
 60 | 	{ time: '2016-08-22', value: 106.94 },
 61 | 	{ time: '2016-08-29', value: 107.73 },
 62 | 	{ time: '2016-09-05', value: 103.13 },
 63 | 	{ time: '2016-09-12', value: 114.92 },
 64 | 	{ time: '2016-09-19', value: 112.71 },
 65 | 	{ time: '2016-09-26', value: 113.05 },
 66 | 	{ time: '2016-10-03', value: 114.06 },
 67 | 	{ time: '2016-10-10', value: 117.63 },
 68 | 	{ time: '2016-10-17', value: 116.6 },
 69 | 	{ time: '2016-10-24', value: 113.72 },
 70 | 	{ time: '2016-10-31', value: 108.84 },
 71 | 	{ time: '2016-11-07', value: 108.43 },
 72 | 	{ time: '2016-11-14', value: 110.06 },
 73 | 	{ time: '2016-11-21', value: 111.79 },
 74 | 	{ time: '2016-11-28', value: 109.9 },
 75 | 	{ time: '2016-12-05', value: 113.95 },
 76 | 	{ time: '2016-12-12', value: 115.97 },
 77 | 	{ time: '2016-12-19', value: 116.52 },
 78 | 	{ time: '2016-12-26', value: 115.82 },
 79 | 	{ time: '2017-01-02', value: 117.91 },
 80 | 	{ time: '2017-01-09', value: 119.04 },
 81 | 	{ time: '2017-01-16', value: 120.0 },
 82 | 	{ time: '2017-01-23', value: 121.95 },
 83 | 	{ time: '2017-01-30', value: 129.08 },
 84 | 	{ time: '2017-02-06', value: 132.12 },
 85 | 	{ time: '2017-02-13', value: 135.72 },
 86 | 	{ time: '2017-02-20', value: 136.66 },
 87 | 	{ time: '2017-02-27', value: 139.78 },
 88 | 	{ time: '2017-03-06', value: 139.14 },
 89 | 	{ time: '2017-03-13', value: 139.99 },
 90 | 	{ time: '2017-03-20', value: 140.64 },
 91 | 	{ time: '2017-03-27', value: 143.66 },
 92 | 	{ time: '2017-04-03', value: 143.34 },
 93 | 	{ time: '2017-04-10', value: 141.05 },
 94 | 	{ time: '2017-04-17', value: 142.27 },
 95 | 	{ time: '2017-04-24', value: 143.65 },
 96 | 	{ time: '2017-05-01', value: 148.96 },
 97 | 	{ time: '2017-05-08', value: 156.1 },
 98 | 	{ time: '2017-05-15', value: 153.06 },
 99 | 	{ time: '2017-05-22', value: 153.61 },
100 | 	{ time: '2017-05-29', value: 155.45 },
101 | 	{ time: '2017-06-05', value: 148.98 },
102 | 	{ time: '2017-06-12', value: 142.27 },
103 | 	{ time: '2017-06-19', value: 146.28 },
104 | 	{ time: '2017-06-26', value: 144.02 },
105 | 	{ time: '2017-07-03', value: 144.18 },
106 | 	{ time: '2017-07-10', value: 149.04 },
107 | 	{ time: '2017-07-17', value: 150.27 },
108 | 	{ time: '2017-07-24', value: 149.5 },
109 | 	{ time: '2017-07-31', value: 156.39 },
110 | 	{ time: '2017-08-07', value: 157.48 },
111 | 	{ time: '2017-08-14', value: 157.5 },
112 | 	{ time: '2017-08-21', value: 159.86 },
113 | 	{ time: '2017-08-28', value: 164.05 },
114 | 	{ time: '2017-09-04', value: 158.63 },
115 | 	{ time: '2017-09-11', value: 159.88 },
116 | 	{ time: '2017-09-18', value: 151.89 },
117 | 	{ time: '2017-09-25', value: 154.12 },
118 | 	{ time: '2017-10-02', value: 155.3 },
119 | 	{ time: '2017-10-09', value: 156.99 },
120 | 	{ time: '2017-10-16', value: 156.25 },
121 | 	{ time: '2017-10-23', value: 163.05 },
122 | 	{ time: '2017-10-30', value: 172.5 },
123 | 	{ time: '2017-11-06', value: 174.67 },
124 | 	{ time: '2017-11-13', value: 170.15 },
125 | 	{ time: '2017-11-20', value: 174.97 },
126 | 	{ time: '2017-11-27', value: 171.05 },
127 | 	{ time: '2017-12-04', value: 169.37 },
128 | 	{ time: '2017-12-11', value: 173.97 },
129 | 	{ time: '2017-12-18', value: 175.01 },
130 | 	{ time: '2017-12-25', value: 169.23 },
131 | 	{ time: '2018-01-01', value: 175.0 },
132 | 	{ time: '2018-01-08', value: 177.09 },
133 | 	{ time: '2018-01-15', value: 178.46 },
134 | 	{ time: '2018-01-22', value: 171.51 },
135 | 	{ time: '2018-01-29', value: 160.5 },
136 | 	{ time: '2018-02-05', value: 156.41 },
137 | 	{ time: '2018-02-12', value: 172.43 },
138 | 	{ time: '2018-02-19', value: 175.5 },
139 | 	{ time: '2018-02-26', value: 176.21 },
140 | 	{ time: '2018-03-05', value: 179.98 },
141 | 	{ time: '2018-03-12', value: 178.02 },
142 | 	{ time: '2018-03-19', value: 164.94 },
143 | 	{ time: '2018-03-26', value: 167.78 },
144 | 	{ time: '2018-04-02', value: 168.38 },
145 | 	{ time: '2018-04-09', value: 174.73 },
146 | 	{ time: '2018-04-16', value: 165.72 },
147 | 	{ time: '2018-04-23', value: 162.32 },
148 | 	{ time: '2018-04-30', value: 183.83 },
149 | 	{ time: '2018-05-07', value: 188.59 },
150 | 	{ time: '2018-05-14', value: 186.31 },
151 | 	{ time: '2018-05-21', value: 188.58 },
152 | 	{ time: '2018-05-28', value: 190.24 },
153 | 	{ time: '2018-06-04', value: 191.7 },
154 | 	{ time: '2018-06-11', value: 188.84 },
155 | 	{ time: '2018-06-18', value: 184.92 },
156 | 	{ time: '2018-06-25', value: 185.11 },
157 | 	{ time: '2018-07-02', value: 187.97 },
158 | 	{ time: '2018-07-09', value: 191.33 },
159 | 	{ time: '2018-07-16', value: 191.44 },
160 | 	{ time: '2018-07-23', value: 190.98 },
161 | 	{ time: '2018-07-30', value: 207.99 },
162 | 	{ time: '2018-08-06', value: 207.53 },
163 | 	{ time: '2018-08-13', value: 217.58 },
164 | 	{ time: '2018-08-20', value: 216.16 },
165 | 	{ time: '2018-08-27', value: 227.63 },
166 | 	{ time: '2018-09-03', value: 221.3 },
167 | 	{ time: '2018-09-10', value: 223.84 },
168 | 	{ time: '2018-09-17', value: 217.66 },
169 | 	{ time: '2018-09-24', value: 225.74 },
170 | 	{ time: '2018-10-01', value: 224.29 },
171 | 	{ time: '2018-10-08', value: 222.11 },
172 | 	{ time: '2018-10-15', value: 219.31 },
173 | 	{ time: '2018-10-22', value: 216.3 },
174 | 	{ time: '2018-10-29', value: 207.48 },
175 | 	{ time: '2018-11-05', value: 204.47 },
176 | 	{ time: '2018-11-12', value: 193.53 },
177 | 	{ time: '2018-11-19', value: 172.29 },
178 | 	{ time: '2018-11-26', value: 178.58 },
179 | 	{ time: '2018-12-03', value: 168.49 },
180 | 	{ time: '2018-12-10', value: 165.48 },
181 | 	{ time: '2018-12-17', value: 150.73 },
182 | 	{ time: '2018-12-24', value: 156.23 },
183 | 	{ time: '2018-12-31', value: 148.26 },
184 | 	{ time: '2019-01-07', value: 152.29 },
185 | 	{ time: '2019-01-14', value: 156.82 },
186 | 	{ time: '2019-01-21', value: 157.76 },
187 | 	{ time: '2019-01-28', value: 166.52 },
188 | 	{ time: '2019-02-04', value: 170.41 },
189 | 	{ time: '2019-02-11', value: 170.42 },
190 | 	{ time: '2019-02-18', value: 172.97 },
191 | 	{ time: '2019-02-25', value: 174.97 },
192 | 	{ time: '2019-03-04', value: 172.91 },
193 | 	{ time: '2019-03-11', value: 186.12 },
194 | 	{ time: '2019-03-18', value: 191.05 },
195 | 	{ time: '2019-03-25', value: 189.95 },
196 | 	{ time: '2019-04-01', value: 197.0 },
197 | 	{ time: '2019-04-08', value: 198.87 },
198 | 	{ time: '2019-04-15', value: 203.86 },
199 | 	{ time: '2019-04-22', value: 204.3 },
200 | 	{ time: '2019-04-29', value: 211.75 },
201 | 	{ time: '2019-05-06', value: 197.18 },
202 | 	{ time: '2019-05-13', value: 189.0 },
203 | 	{ time: '2019-05-20', value: 178.97 },
204 | 	{ time: '2019-05-27', value: 179.03 },
205 | 	// hide-end
206 | ]);
207 | 
208 | const container = document.getElementById('container');
209 | 
210 | const toolTipWidth = 80;
211 | const toolTipHeight = 80;
212 | const toolTipMargin = 15;
213 | 
214 | // Create and style the tooltip html element
215 | const toolTip = document.createElement('div');
216 | toolTip.style = `width: 96px; height: 80px; position: absolute; display: none; padding: 8px; box-sizing: border-box; font-size: 12px; text-align: left; z-index: 1000; top: 12px; left: 12px; pointer-events: none; border: 1px solid; border-radius: 2px;font-family: -apple-system, BlinkMacSystemFont, 'Trebuchet MS', Roboto, Ubuntu, sans-serif; -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;`;
217 | toolTip.style.background = CHART_BACKGROUND_COLOR;
218 | toolTip.style.color = CHART_TEXT_COLOR;
219 | toolTip.style.borderColor = BASELINE_TOP_LINE_COLOR;
220 | container.appendChild(toolTip);
221 | 
222 | // update tooltip
223 | chart.subscribeCrosshairMove(param => {
224 | 	if (
225 | 		param.point === undefined ||
226 | 		!param.time ||
227 | 		param.point.x < 0 ||
228 | 		param.point.x > container.clientWidth ||
229 | 		param.point.y < 0 ||
230 | 		param.point.y > container.clientHeight
231 | 	) {
232 | 		toolTip.style.display = 'none';
233 | 	} else {
234 | 		// time will be in the same format that we supplied to setData.
235 | 		// thus it will be YYYY-MM-DD
236 | 		const dateStr = param.time;
237 | 		toolTip.style.display = 'block';
238 | 		const data = param.seriesData.get(series);
239 | 		const price = data.value !== undefined ? data.value : data.close;
240 | 		toolTip.innerHTML = `<div style="color: ${BASELINE_TOP_LINE_COLOR}">ABC Inc.</div><div style="font-size: 24px; margin: 4px 0px; color: ${CHART_TEXT_COLOR}">
241 | 			${Math.round(100 * price) / 100}
242 | 			</div><div style="color: ${CHART_TEXT_COLOR}">
243 | 			${dateStr}
244 | 			</div>`;
245 | 
246 | 		// highlight-start
247 | 		const y = param.point.y;
248 | 		let left = param.point.x + toolTipMargin;
249 | 		if (left > container.clientWidth - toolTipWidth) {
250 | 			left = param.point.x - toolTipMargin - toolTipWidth;
251 | 		}
252 | 
253 | 		let top = y + toolTipMargin;
254 | 		if (top > container.clientHeight - toolTipHeight) {
255 | 			top = y - toolTipHeight - toolTipMargin;
256 | 		}
257 | 		toolTip.style.left = left + 'px';
258 | 		toolTip.style.top = top + 'px';
259 | 		// highlight-end
260 | 	}
261 | });
262 | 
263 | chart.timeScale().fitContent();
264 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/tooltips.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | title: Tooltips
  3 | sidebar_label: Tooltips
  4 | description: Examples on how to implement a tooltip for your chart.
  5 | pagination_prev: null
  6 | pagination_next: null
  7 | keywords:
  8 |   - example
  9 |   - tooltip
 10 | ---
 11 | 
 12 | import VersionWarningAdmonition from "@site/src/components/VersionWarningAdmonition";
 13 | 
 14 | {/*
 15 |   Show warning when not on the latest published version
 16 |   Tutorials section isn't versioned yet, hence the need for the warning message
 17 |   THESE TUTORIALS NEED TO BE UPDATED FOR VERSION 4
 18 | */}
 19 | 
 20 | <VersionWarningAdmonition
 21 | 	notCurrent="This example is for the latest published version of Lightweight Charts."
 22 | 	type="caution"
 23 | 	displayVersionMessage
 24 | />
 25 | 
 26 | Lightweight Charts™ doesn't include a built-in tooltip feature, however it is something which can be added
 27 | to your chart by following the examples presented below.
 28 | 
 29 | ## How to
 30 | 
 31 | In order to add a tooltip to the chart we need to create and position an `html` into the desired position above
 32 | the chart. We can then subscribe to the crosshairMove events ([subscribeCrosshairMove](/docs/api/interfaces/IChartApi#subscribecrosshairmove)) provided by the [`IChartApi`](/docs/api/interfaces/IChartApi) instance, and manually
 33 | update the content within our `html` tooltip element and change it's position.
 34 | 
 35 | ```js
 36 | chart.subscribeCrosshairMove(param => {
 37 |     if (
 38 |         param.point === undefined ||
 39 | 		!param.time ||
 40 | 		param.point.x < 0 ||
 41 | 		param.point.y < 0
 42 |     ) {
 43 |         toolTip.style.display = 'none';
 44 |     } else {
 45 |         const dateStr = dateToString(param.time);
 46 |         toolTip.style.display = 'block';
 47 |         const data = param.seriesData.get(series);
 48 |         const price = data.value !== undefined ? data.value : data.close;
 49 |         toolTip.innerHTML = `<div>${price.toFixed(2)}</div>`;
 50 | 
 51 |         // Position tooltip according to mouse cursor position
 52 |         toolTip.style.left = param.point.x + 'px';
 53 |         toolTip.style.top = param.point.y + 'px';
 54 |     }
 55 | });
 56 | ```
 57 | 
 58 | The process of creating the tooltip html element and positioning can be seen within the examples below.
 59 | Essentially, we create a new div element within the container div (holding the chart) and then position
 60 | and style it using `css`.
 61 | 
 62 | You can see full [working examples](#examples) below.
 63 | 
 64 | ### Getting the mouse cursors position
 65 | 
 66 | The parameter object ([MouseEventParams Interface](/docs/api/interfaces/MouseEventParams)) passed to the
 67 | crosshairMove handler function ([MouseEventhandler](/docs/api/type-aliases/MouseEventHandler)) contains a
 68 | [point](/docs/api/interfaces/Point) property which gives the current mouse cursor position relative to
 69 | the top left corner of the chart.
 70 | 
 71 | ### Getting the data points position
 72 | 
 73 | It is possible to convert a price value into it's current vertical position on the chart by using
 74 | the [priceToCoordinate](/docs/api/interfaces/ISeriesApi#pricetocoordinate) method on the series' instance.
 75 | This along with the `param.point.x` can be used to determine the position of the data point.
 76 | 
 77 | ```js
 78 | chart.subscribeCrosshairMove(param => {
 79 |     const x = param.point.x;
 80 |     const data = param.seriesData.get(series);
 81 |     const price = data.value !== undefined ? data.value : data.close;
 82 |     const y = series.priceToCoordinate(price);
 83 |     console.log(`The data point is at position: ${x}, ${y}`);
 84 | });
 85 | ```
 86 | 
 87 | ## Resources
 88 | 
 89 | - [subscribeCrosshairMove](/docs/api/interfaces/IChartApi#subscribecrosshairmove)
 90 | - [MouseEventParams Interface](/docs/api/interfaces/MouseEventParams)
 91 | - [MouseEventhandler](/docs/api/type-aliases/MouseEventHandler)
 92 | - [priceToCoordinate](/docs/api/interfaces/ISeriesApi#pricetocoordinate)
 93 | 
 94 | Below are a few external resources related to creating and styling html elements:
 95 | 
 96 | - [createElement](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)
 97 | - [innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML)
 98 | - [style property](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style)
 99 | 
100 | ## Examples
101 | 
102 | import UsageGuidePartial from "../_usage-guide-partial.mdx";
103 | 
104 | <UsageGuidePartial />
105 | 
106 | import CodeBlock from "@theme/CodeBlock";
107 | 
108 | ### Floating Tooltip
109 | 
110 | The floating tooltip in this example will position itself next to the current datapoint.
111 | 
112 | import floatingCode from "!!raw-loader!./tooltip-floating.js";
113 | 
114 | <CodeBlock replaceThemeConstants chart className="language-js" hideableCode chartOnTop>
115 | 	{floatingCode}
116 | </CodeBlock>
117 | 
118 | ### Tracking Tooltip
119 | 
120 | The tracking tooltip will position itself next to the user's cursor.
121 | 
122 | import trackingCode from "!!raw-loader!./tooltip-tracking.js";
123 | 
124 | <CodeBlock replaceThemeConstants chart className="language-js" hideableCode chartOnTop>
125 | 	{trackingCode}
126 | </CodeBlock>
127 | 
128 | ### Magnifier Tooltip
129 | 
130 | The magnifier tooltip will position itself along the top edge of the chart while following
131 | the user's cursor along the horizontal time axis.
132 | 
133 | import magnifierCode from "!!raw-loader!./tooltip-magnifier.js";
134 | 
135 | <CodeBlock replaceThemeConstants chart className="language-js" hideableCode chartOnTop>
136 | 	{magnifierCode}
137 | </CodeBlock>
138 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/two-price-scales.js:
--------------------------------------------------------------------------------
  1 | // remove-start
  2 | // Lightweight Charts™ Example: Two Price Scales
  3 | // https://tradingview.github.io/lightweight-charts/tutorials/how_to/two-price-scales
  4 | 
  5 | // remove-end
  6 | const chartOptions = {
  7 | 	// highlight-start
  8 | 	rightPriceScale: {
  9 | 		visible: true,
 10 | 	},
 11 | 	leftPriceScale: {
 12 | 		visible: true,
 13 | 	},
 14 | 	// highlight-end
 15 | 	layout: {
 16 | 		textColor: CHART_TEXT_COLOR,
 17 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
 18 | 	},
 19 | 	// highlight-start
 20 | 	crosshair: {
 21 | 		mode: 0, // CrosshairMode.Normal
 22 | 	},
 23 | 	// highlight-end
 24 | };
 25 | // remove-line
 26 | /** @type {import('lightweight-charts').IChartApi} */
 27 | const chart = createChart(document.getElementById('container'), chartOptions);
 28 | chart
 29 | 	.addSeries(LineSeries, {
 30 | 		color: LINE_LINE_COLOR,
 31 | 		lineWidth: 2,
 32 | 	})
 33 | 	.setData([
 34 | 		{ time: { year: 2018, month: 9, day: 22 }, value: 25.531816900940186 },
 35 | 		// hide-start
 36 | 		{ time: { year: 2018, month: 9, day: 23 }, value: 26.350850429478125 },
 37 | 		{ time: { year: 2018, month: 9, day: 24 }, value: 25.05218443850655 },
 38 | 		{ time: { year: 2018, month: 9, day: 25 }, value: 25.41022485894306 },
 39 | 		{ time: { year: 2018, month: 9, day: 26 }, value: 25.134847363259958 },
 40 | 		{ time: { year: 2018, month: 9, day: 27 }, value: 24.239250761300525 },
 41 | 		{ time: { year: 2018, month: 9, day: 28 }, value: 28.8673009313941 },
 42 | 		{ time: { year: 2018, month: 9, day: 29 }, value: 27.028082380884264 },
 43 | 		{ time: { year: 2018, month: 9, day: 30 }, value: 27.181577793470662 },
 44 | 		{ time: { year: 2018, month: 10, day: 1 }, value: 28.658957209998505 },
 45 | 		{ time: { year: 2018, month: 10, day: 2 }, value: 30.418392247817536 },
 46 | 		{ time: { year: 2018, month: 10, day: 3 }, value: 26.41825183552505 },
 47 | 		{ time: { year: 2018, month: 10, day: 4 }, value: 30.0951233353539 },
 48 | 		{ time: { year: 2018, month: 10, day: 5 }, value: 30.30985059775389 },
 49 | 		{ time: { year: 2018, month: 10, day: 6 }, value: 30.71612555943148 },
 50 | 		{ time: { year: 2018, month: 10, day: 7 }, value: 28.222424591003268 },
 51 | 		{ time: { year: 2018, month: 10, day: 8 }, value: 31.01149570947896 },
 52 | 		{ time: { year: 2018, month: 10, day: 9 }, value: 30.390225881550307 },
 53 | 		{ time: { year: 2018, month: 10, day: 10 }, value: 29.451733557312163 },
 54 | 		{ time: { year: 2018, month: 10, day: 11 }, value: 34.14376900459634 },
 55 | 		{ time: { year: 2018, month: 10, day: 12 }, value: 30.223333215683407 },
 56 | 		{ time: { year: 2018, month: 10, day: 13 }, value: 35.1548736041708 },
 57 | 		{ time: { year: 2018, month: 10, day: 14 }, value: 37.795223779011096 },
 58 | 		{ time: { year: 2018, month: 10, day: 15 }, value: 38.95966228546306 },
 59 | 		{ time: { year: 2018, month: 10, day: 16 }, value: 35.59132526195566 },
 60 | 		{ time: { year: 2018, month: 10, day: 17 }, value: 38.42249768195307 },
 61 | 		{ time: { year: 2018, month: 10, day: 18 }, value: 40.82520015585623 },
 62 | 		{ time: { year: 2018, month: 10, day: 19 }, value: 37.401446370157814 },
 63 | 		{ time: { year: 2018, month: 10, day: 20 }, value: 44.14728329801845 },
 64 | 		{ time: { year: 2018, month: 10, day: 21 }, value: 43.908512951087765 },
 65 | 		{ time: { year: 2018, month: 10, day: 22 }, value: 47.139711966410914 },
 66 | 		{ time: { year: 2018, month: 10, day: 23 }, value: 43.78495537329606 },
 67 | 		{ time: { year: 2018, month: 10, day: 24 }, value: 46.37910782721347 },
 68 | 		{ time: { year: 2018, month: 10, day: 25 }, value: 48.280192310089234 },
 69 | 		{ time: { year: 2018, month: 10, day: 26 }, value: 49.63767420501933 },
 70 | 		{ time: { year: 2018, month: 10, day: 27 }, value: 43.05752682224708 },
 71 | 		{ time: { year: 2018, month: 10, day: 28 }, value: 48.32708061157758 },
 72 | 		{ time: { year: 2018, month: 10, day: 29 }, value: 53.39600337663517 },
 73 | 		{ time: { year: 2018, month: 10, day: 30 }, value: 46.711006266435355 },
 74 | 		{ time: { year: 2018, month: 10, day: 31 }, value: 54.13809826985657 },
 75 | 		{ time: { year: 2018, month: 11, day: 1 }, value: 55.79021790616995 },
 76 | 		{ time: { year: 2018, month: 11, day: 2 }, value: 49.2873885580548 },
 77 | 		{ time: { year: 2018, month: 11, day: 3 }, value: 56.97009522871737 },
 78 | 		{ time: { year: 2018, month: 11, day: 4 }, value: 50.823930530973975 },
 79 | 		{ time: { year: 2018, month: 11, day: 5 }, value: 54.960060077375076 },
 80 | 		{ time: { year: 2018, month: 11, day: 6 }, value: 62.0222568413422 },
 81 | 		{ time: { year: 2018, month: 11, day: 7 }, value: 58.20081640960216 },
 82 | 		{ time: { year: 2018, month: 11, day: 8 }, value: 65.13004590769961 },
 83 | 		{ time: { year: 2018, month: 11, day: 9 }, value: 57.78891076252559 },
 84 | 		{ time: { year: 2018, month: 11, day: 10 }, value: 58.792896124952186 },
 85 | 		{ time: { year: 2018, month: 11, day: 11 }, value: 61.87890147945707 },
 86 | 		{ time: { year: 2018, month: 11, day: 12 }, value: 60.93156560716248 },
 87 | 		{ time: { year: 2018, month: 11, day: 13 }, value: 57.85928164082374 },
 88 | 		{ time: { year: 2018, month: 11, day: 14 }, value: 70.95139577968187 },
 89 | 		{ time: { year: 2018, month: 11, day: 15 }, value: 71.59735270974251 },
 90 | 		{ time: { year: 2018, month: 11, day: 16 }, value: 68.6730845432055 },
 91 | 		{ time: { year: 2018, month: 11, day: 17 }, value: 70.1298800651962 },
 92 | 		{ time: { year: 2018, month: 11, day: 18 }, value: 68.82963709012753 },
 93 | 		{ time: { year: 2018, month: 11, day: 19 }, value: 70.66316240517193 },
 94 | 		{ time: { year: 2018, month: 11, day: 20 }, value: 67.83320577283186 },
 95 | 		{ time: { year: 2018, month: 11, day: 21 }, value: 75.08486799785067 },
 96 | 		{ time: { year: 2018, month: 11, day: 22 }, value: 72.87979342888752 },
 97 | 		{ time: { year: 2018, month: 11, day: 23 }, value: 78.84973566116827 },
 98 | 		{ time: { year: 2018, month: 11, day: 24 }, value: 77.59573370643601 },
 99 | 		{ time: { year: 2018, month: 11, day: 25 }, value: 74.74726921909757 },
100 | 		{ time: { year: 2018, month: 11, day: 26 }, value: 69.68128245039887 },
101 | 		{ time: { year: 2018, month: 11, day: 27 }, value: 84.2489916330028 },
102 | 		{ time: { year: 2018, month: 11, day: 28 }, value: 85.49947753269504 },
103 | 		{ time: { year: 2018, month: 11, day: 29 }, value: 79.8486264148003 },
104 | 		{ time: { year: 2018, month: 11, day: 30 }, value: 87.69287202402485 },
105 | 		{ time: { year: 2018, month: 12, day: 1 }, value: 78.01690218289475 },
106 | 		{ time: { year: 2018, month: 12, day: 2 }, value: 90.03789034980372 },
107 | 		{ time: { year: 2018, month: 12, day: 3 }, value: 80.8840602849401 },
108 | 		{ time: { year: 2018, month: 12, day: 4 }, value: 76.88131503723805 },
109 | 		{ time: { year: 2018, month: 12, day: 5 }, value: 80.31060219295262 },
110 | 		{ time: { year: 2018, month: 12, day: 6 }, value: 93.94619117220051 },
111 | 		{ time: { year: 2018, month: 12, day: 7 }, value: 94.87133202008548 },
112 | 		{ time: { year: 2018, month: 12, day: 8 }, value: 82.60328626838404 },
113 | 		{ time: { year: 2018, month: 12, day: 9 }, value: 97.16768398118845 },
114 | 		{ time: { year: 2018, month: 12, day: 10 }, value: 86.28219316727935 },
115 | 		{ time: { year: 2018, month: 12, day: 11 }, value: 88.98768390749808 },
116 | 		{ time: { year: 2018, month: 12, day: 12 }, value: 86.9799632094888 },
117 | 		{ time: { year: 2018, month: 12, day: 13 }, value: 94.84612878449812 },
118 | 		{ time: { year: 2018, month: 12, day: 14 }, value: 102.1160216124386 },
119 | 		{ time: { year: 2018, month: 12, day: 15 }, value: 87.0646295567293 },
120 | 		{ time: { year: 2018, month: 12, day: 16 }, value: 88.48802912330535 },
121 | 		{ time: { year: 2018, month: 12, day: 17 }, value: 89.68490260440238 },
122 | 		{ time: { year: 2018, month: 12, day: 18 }, value: 86.66224375818467 },
123 | 		{ time: { year: 2018, month: 12, day: 19 }, value: 88.05916917094234 },
124 | 		{ time: { year: 2018, month: 12, day: 20 }, value: 78.96513176162487 },
125 | 		{ time: { year: 2018, month: 12, day: 21 }, value: 90.54239307317953 },
126 | 		{ time: { year: 2018, month: 12, day: 22 }, value: 92.40550159209458 },
127 | 		{ time: { year: 2018, month: 12, day: 23 }, value: 82.47365747958841 },
128 | 		{ time: { year: 2018, month: 12, day: 24 }, value: 91.55327647717618 },
129 | 		{ time: { year: 2018, month: 12, day: 25 }, value: 89.34790162747024 },
130 | 		{ time: { year: 2018, month: 12, day: 26 }, value: 85.68927849920716 },
131 | 		{ time: { year: 2018, month: 12, day: 27 }, value: 85.86795553966918 },
132 | 		{ time: { year: 2018, month: 12, day: 28 }, value: 90.55358282944198 },
133 | 		{ time: { year: 2018, month: 12, day: 29 }, value: 91.28939932554621 },
134 | 		{ time: { year: 2018, month: 12, day: 30 }, value: 100.90495261248472 },
135 | 		{ time: { year: 2018, month: 12, day: 31 }, value: 98.99348823473713 },
136 | 		// hide-end
137 | 	]);
138 | 
139 | const candlestickSeries = chart.addSeries(CandlestickSeries, {
140 | 	// highlight-start
141 | 	priceScaleId: 'left',
142 | 	// highlight-end
143 | 	upColor: BAR_UP_COLOR, downColor: BAR_DOWN_COLOR, borderVisible: false,
144 | 	wickUpColor: BAR_UP_COLOR, wickDownColor: BAR_DOWN_COLOR,
145 | });
146 | 
147 | candlestickSeries.setData([
148 | 	{
149 | 		close: 108.9974612905403,
150 | 		high: 121.20998259466148,
151 | 		low: 96.65376292551082,
152 | 		open: 104.5614412226746,
153 | 		time: { year: 2018, month: 9, day: 22 },
154 | 	},
155 | 	// hide-start
156 | 	{
157 | 		close: 110.46815600023501,
158 | 		high: 111.3650273696516,
159 | 		low: 82.65543461471314,
160 | 		open: 110.16538466099634,
161 | 		time: { year: 2018, month: 9, day: 23 },
162 | 	},
163 | 	{
164 | 		close: 90.62131977740425,
165 | 		high: 109.19838270252615,
166 | 		low: 82.30106956144076,
167 | 		open: 105.03104735287424,
168 | 		time: { year: 2018, month: 9, day: 24 },
169 | 	},
170 | 	{
171 | 		close: 96.80120024431532,
172 | 		high: 101.92074283374939,
173 | 		low: 89.25819769856513,
174 | 		open: 89.25819769856513,
175 | 		time: { year: 2018, month: 9, day: 25 },
176 | 	},
177 | 	{
178 | 		close: 94.87113928076117,
179 | 		high: 104.12503365679314,
180 | 		low: 85.42405005240111,
181 | 		open: 104.12503365679314,
182 | 		time: { year: 2018, month: 9, day: 26 },
183 | 	},
184 | 	{
185 | 		close: 100.76494087674855,
186 | 		high: 102.60508417239113,
187 | 		low: 80.76268547064865,
188 | 		open: 92.93299948659636,
189 | 		time: { year: 2018, month: 9, day: 27 },
190 | 	},
191 | 	{
192 | 		close: 101.45855928883597,
193 | 		high: 110.26727325817173,
194 | 		low: 91.10348900896837,
195 | 		open: 93.4362185148034,
196 | 		time: { year: 2018, month: 9, day: 28 },
197 | 	},
198 | 	{
199 | 		close: 91.68871815146144,
200 | 		high: 103.73263644407702,
201 | 		low: 73.5329263610334,
202 | 		open: 92.96467883926464,
203 | 		time: { year: 2018, month: 9, day: 29 },
204 | 	},
205 | 	{
206 | 		close: 89.39633140354033,
207 | 		high: 101.06569518834237,
208 | 		low: 81.71149885084162,
209 | 		open: 83.08248758612376,
210 | 		time: { year: 2018, month: 9, day: 30 },
211 | 	},
212 | 	{
213 | 		close: 93.09498513675378,
214 | 		high: 93.09498513675378,
215 | 		low: 76.81138276012628,
216 | 		open: 91.97280452613565,
217 | 		time: { year: 2018, month: 10, day: 1 },
218 | 	},
219 | 	{
220 | 		close: 89.26733004009083,
221 | 		high: 89.26733004009083,
222 | 		low: 76.27851645958225,
223 | 		open: 85.83860311023625,
224 | 		time: { year: 2018, month: 10, day: 2 },
225 | 	},
226 | 	{
227 | 		close: 89.66035763006947,
228 | 		high: 89.66035763006947,
229 | 		low: 67.63677527399729,
230 | 		open: 77.79584976144585,
231 | 		time: { year: 2018, month: 10, day: 3 },
232 | 	},
233 | 	{
234 | 		close: 89.59687813884807,
235 | 		high: 97.05916949817754,
236 | 		low: 72.9823390058379,
237 | 		open: 77.37388423995716,
238 | 		time: { year: 2018, month: 10, day: 4 },
239 | 	},
240 | 	{
241 | 		close: 83.6425403120788,
242 | 		high: 91.72593377862522,
243 | 		low: 65.27208271740422,
244 | 		open: 85.92711686401718,
245 | 		time: { year: 2018, month: 10, day: 5 },
246 | 	},
247 | 	{
248 | 		close: 82.99053929200655,
249 | 		high: 93.4482645370556,
250 | 		low: 65.98920655616067,
251 | 		open: 71.8940788814462,
252 | 		time: { year: 2018, month: 10, day: 6 },
253 | 	},
254 | 	{
255 | 		close: 73.09595957510754,
256 | 		high: 86.65935598412881,
257 | 		low: 62.710852488609326,
258 | 		open: 80.78945254092527,
259 | 		time: { year: 2018, month: 10, day: 7 },
260 | 	},
261 | 	{
262 | 		close: 80.12127692112905,
263 | 		high: 87.49034842093855,
264 | 		low: 60.09987438133361,
265 | 		open: 70.2408873110499,
266 | 		time: { year: 2018, month: 10, day: 8 },
267 | 	},
268 | 	{
269 | 		close: 77.60439116240829,
270 | 		high: 83.20908153481327,
271 | 		low: 68.56836128158209,
272 | 		open: 75.83440719565763,
273 | 		time: { year: 2018, month: 10, day: 9 },
274 | 	},
275 | 	{
276 | 		close: 73.8952889203428,
277 | 		high: 81.89987377779327,
278 | 		low: 57.8891283348631,
279 | 		open: 66.51904017615065,
280 | 		time: { year: 2018, month: 10, day: 10 },
281 | 	},
282 | 	{
283 | 		close: 75.08452506029613,
284 | 		high: 75.08452506029613,
285 | 		low: 59.208194031968155,
286 | 		open: 72.14475369395771,
287 | 		time: { year: 2018, month: 10, day: 11 },
288 | 	},
289 | 	{
290 | 		close: 73.08898607472305,
291 | 		high: 73.08898607472305,
292 | 		low: 63.05632280826725,
293 | 		open: 66.93050765469924,
294 | 		time: { year: 2018, month: 10, day: 12 },
295 | 	},
296 | 	{
297 | 		close: 58.993371469509704,
298 | 		high: 73.08872095153116,
299 | 		low: 53.52204433018574,
300 | 		open: 66.12840939191403,
301 | 		time: { year: 2018, month: 10, day: 13 },
302 | 	},
303 | 	{
304 | 		close: 57.150755012485,
305 | 		high: 74.57414896810235,
306 | 		low: 52.6552427480398,
307 | 		open: 68.50876667562338,
308 | 		time: { year: 2018, month: 10, day: 14 },
309 | 	},
310 | 	{
311 | 		close: 58.03147289822832,
312 | 		high: 69.62445357159157,
313 | 		low: 53.8260018823565,
314 | 		open: 61.62298899368165,
315 | 		time: { year: 2018, month: 10, day: 15 },
316 | 	},
317 | 	{
318 | 		close: 60.6852855399041,
319 | 		high: 69.02095441024431,
320 | 		low: 54.00939224622043,
321 | 		open: 64.81901552322648,
322 | 		time: { year: 2018, month: 10, day: 16 },
323 | 	},
324 | 	{
325 | 		close: 57.508820449565285,
326 | 		high: 63.82926565242872,
327 | 		low: 54.07370975509682,
328 | 		open: 54.07370975509682,
329 | 		time: { year: 2018, month: 10, day: 17 },
330 | 	},
331 | 	{
332 | 		close: 51.60796818909221,
333 | 		high: 64.88712939579875,
334 | 		low: 51.60796818909221,
335 | 		open: 53.489226476218434,
336 | 		time: { year: 2018, month: 10, day: 18 },
337 | 	},
338 | 	{
339 | 		close: 55.139520748382864,
340 | 		high: 59.161320710177925,
341 | 		low: 52.228139922762765,
342 | 		open: 52.228139922762765,
343 | 		time: { year: 2018, month: 10, day: 19 },
344 | 	},
345 | 	{
346 | 		close: 47.47868992247237,
347 | 		high: 58.0836625917653,
348 | 		low: 46.43213518526832,
349 | 		open: 47.59258635788406,
350 | 		time: { year: 2018, month: 10, day: 20 },
351 | 	},
352 | 	{
353 | 		close: 47.22596723150508,
354 | 		high: 51.55468175560989,
355 | 		low: 45.22654435521185,
356 | 		open: 47.452459556200054,
357 | 		time: { year: 2018, month: 10, day: 21 },
358 | 	},
359 | 	{
360 | 		close: 53.39724151191295,
361 | 		high: 58.256006746786035,
362 | 		low: 46.40105667413804,
363 | 		open: 53.41548527476272,
364 | 		time: { year: 2018, month: 10, day: 22 },
365 | 	},
366 | 	{
367 | 		close: 45.015877277800854,
368 | 		high: 51.2955426978105,
369 | 		low: 40.26534748806228,
370 | 		open: 43.90158660063875,
371 | 		time: { year: 2018, month: 10, day: 23 },
372 | 	},
373 | 	{
374 | 		close: 49.307312373439665,
375 | 		high: 49.93643636637581,
376 | 		low: 43.20705757075934,
377 | 		open: 45.672934511555795,
378 | 		time: { year: 2018, month: 10, day: 24 },
379 | 	},
380 | 	{
381 | 		close: 45.15418019295631,
382 | 		high: 48.59676744409583,
383 | 		low: 37.628047445918504,
384 | 		open: 40.33862825788268,
385 | 		time: { year: 2018, month: 10, day: 25 },
386 | 	},
387 | 	{
388 | 		close: 43.2972018283068,
389 | 		high: 43.2972018283068,
390 | 		low: 36.335943004352245,
391 | 		open: 42.605991542720965,
392 | 		time: { year: 2018, month: 10, day: 26 },
393 | 	},
394 | 	{
395 | 		close: 39.1153643552137,
396 | 		high: 44.311406627923844,
397 | 		low: 35.31457011784855,
398 | 		open: 42.00000202357808,
399 | 		time: { year: 2018, month: 10, day: 27 },
400 | 	},
401 | 	{
402 | 		close: 36.06960076896885,
403 | 		high: 42.89041111567749,
404 | 		low: 33.58326637182405,
405 | 		open: 37.40942817102858,
406 | 		time: { year: 2018, month: 10, day: 28 },
407 | 	},
408 | 	{
409 | 		close: 35.8981036950969,
410 | 		high: 42.19793419602979,
411 | 		low: 33.62190962880232,
412 | 		open: 36.87246325249825,
413 | 		time: { year: 2018, month: 10, day: 29 },
414 | 	},
415 | 	{
416 | 		close: 31.378205119641457,
417 | 		high: 37.33501102832602,
418 | 		low: 31.30137162225214,
419 | 		open: 35.651275660713694,
420 | 		time: { year: 2018, month: 10, day: 30 },
421 | 	},
422 | 	{
423 | 		close: 33.574536057730576,
424 | 		high: 37.30152570719593,
425 | 		low: 27.369689193426243,
426 | 		open: 34.330180925654936,
427 | 		time: { year: 2018, month: 10, day: 31 },
428 | 	},
429 | 	{
430 | 		close: 28.91735096504839,
431 | 		high: 32.62196350117741,
432 | 		low: 27.072564759401843,
433 | 		open: 29.398552328599372,
434 | 		time: { year: 2018, month: 11, day: 1 },
435 | 	},
436 | 	{
437 | 		close: 28.44143154172122,
438 | 		high: 31.042019861166594,
439 | 		low: 23.383320830495375,
440 | 		open: 27.275885037308072,
441 | 		time: { year: 2018, month: 11, day: 2 },
442 | 	},
443 | 	{
444 | 		close: 25.92162714418916,
445 | 		high: 30.57604443170622,
446 | 		low: 25.418671641150752,
447 | 		open: 26.775196275924657,
448 | 		time: { year: 2018, month: 11, day: 3 },
449 | 	},
450 | 	{
451 | 		close: 26.376994016637433,
452 | 		high: 28.198647836523744,
453 | 		low: 21.492969733673334,
454 | 		open: 26.27980943059139,
455 | 		time: { year: 2018, month: 11, day: 4 },
456 | 	},
457 | 	{
458 | 		close: 28.60834088674494,
459 | 		high: 28.60834088674494,
460 | 		low: 21.89002840571941,
461 | 		open: 25.376464895884993,
462 | 		time: { year: 2018, month: 11, day: 5 },
463 | 	},
464 | 	{
465 | 		close: 31.103861067101136,
466 | 		high: 31.103861067101136,
467 | 		low: 24.39227668420513,
468 | 		open: 28.994785427089838,
469 | 		time: { year: 2018, month: 11, day: 6 },
470 | 	},
471 | 	{
472 | 		close: 28.6308138310307,
473 | 		high: 35.430817482769164,
474 | 		low: 24.069515410358232,
475 | 		open: 27.109407394069084,
476 | 		time: { year: 2018, month: 11, day: 7 },
477 | 	},
478 | 	{
479 | 		close: 29.468889521733466,
480 | 		high: 37.54082586961352,
481 | 		low: 27.90833873315644,
482 | 		open: 33.16901271715577,
483 | 		time: { year: 2018, month: 11, day: 8 },
484 | 	},
485 | 	{
486 | 		close: 35.887823124204296,
487 | 		high: 39.21804237580939,
488 | 		low: 30.951078044055627,
489 | 		open: 30.951078044055627,
490 | 		time: { year: 2018, month: 11, day: 9 },
491 | 	},
492 | 	{
493 | 		close: 34.361137347097575,
494 | 		high: 35.27083445807796,
495 | 		low: 27.825889562160082,
496 | 		open: 34.86040182980157,
497 | 		time: { year: 2018, month: 11, day: 10 },
498 | 	},
499 | 	{
500 | 		close: 36.61336645243868,
501 | 		high: 40.31460537175622,
502 | 		low: 33.96383400053921,
503 | 		open: 39.70037560142739,
504 | 		time: { year: 2018, month: 11, day: 11 },
505 | 	},
506 | 	{
507 | 		close: 41.321693986803055,
508 | 		high: 44.45481986667003,
509 | 		low: 35.67563772228475,
510 | 		open: 38.67059795413642,
511 | 		time: { year: 2018, month: 11, day: 12 },
512 | 	},
513 | 	{
514 | 		close: 40.15038854039306,
515 | 		high: 41.50912000191902,
516 | 		low: 32.610637769394444,
517 | 		open: 41.50912000191902,
518 | 		time: { year: 2018, month: 11, day: 13 },
519 | 	},
520 | 	{
521 | 		close: 44.092601065208015,
522 | 		high: 44.092601065208015,
523 | 		low: 37.778306506100726,
524 | 		open: 38.99045898154136,
525 | 		time: { year: 2018, month: 11, day: 14 },
526 | 	},
527 | 	{
528 | 		close: 41.42426637839382,
529 | 		high: 44.72189614841937,
530 | 		low: 41.42426637839382,
531 | 		open: 44.72189614841937,
532 | 		time: { year: 2018, month: 11, day: 15 },
533 | 	},
534 | 	{
535 | 		close: 41.19513795258408,
536 | 		high: 49.08084695291049,
537 | 		low: 36.24282165100056,
538 | 		open: 44.909248500660254,
539 | 		time: { year: 2018, month: 11, day: 16 },
540 | 	},
541 | 	{
542 | 		close: 44.24935708161703,
543 | 		high: 53.028535501565486,
544 | 		low: 40.32056743060158,
545 | 		open: 46.198546801109984,
546 | 		time: { year: 2018, month: 11, day: 17 },
547 | 	},
548 | 	{
549 | 		close: 43.18555863372182,
550 | 		high: 52.34250206788521,
551 | 		low: 43.18555863372182,
552 | 		open: 49.58135271619679,
553 | 		time: { year: 2018, month: 11, day: 18 },
554 | 	},
555 | 	{
556 | 		close: 50.8568887039091,
557 | 		high: 52.60441957102357,
558 | 		low: 39.917719271944364,
559 | 		open: 48.197532365645806,
560 | 		time: { year: 2018, month: 11, day: 19 },
561 | 	},
562 | 	{
563 | 		close: 48.79128595974164,
564 | 		high: 52.45087789296739,
565 | 		low: 46.80633073487828,
566 | 		open: 52.45087789296739,
567 | 		time: { year: 2018, month: 11, day: 20 },
568 | 	},
569 | 	{
570 | 		close: 46.97300046781947,
571 | 		high: 55.80689868049132,
572 | 		low: 46.97300046781947,
573 | 		open: 55.80689868049132,
574 | 		time: { year: 2018, month: 11, day: 21 },
575 | 	},
576 | 	{
577 | 		close: 55.58129861112469,
578 | 		high: 55.58129861112469,
579 | 		low: 49.087279242343996,
580 | 		open: 53.16719476594961,
581 | 		time: { year: 2018, month: 11, day: 22 },
582 | 	},
583 | 	{
584 | 		close: 50.058979311730226,
585 | 		high: 62.55333249171461,
586 | 		low: 50.058979311730226,
587 | 		open: 52.628489607588826,
588 | 		time: { year: 2018, month: 11, day: 23 },
589 | 	},
590 | 	{
591 | 		close: 51.193155229085995,
592 | 		high: 59.08949991997865,
593 | 		low: 51.193155229085995,
594 | 		open: 55.352594157474755,
595 | 		time: { year: 2018, month: 11, day: 24 },
596 | 	},
597 | 	{
598 | 		close: 60.099338327208436,
599 | 		high: 66.93510126958154,
600 | 		low: 55.27299867222781,
601 | 		open: 61.05897620044226,
602 | 		time: { year: 2018, month: 11, day: 25 },
603 | 	},
604 | 	{
605 | 		close: 58.3802630890727,
606 | 		high: 71.50922937699602,
607 | 		low: 50.95210438359451,
608 | 		open: 62.4679688326532,
609 | 		time: { year: 2018, month: 11, day: 26 },
610 | 	},
611 | 	{
612 | 		close: 57.875350873413225,
613 | 		high: 65.59903214448208,
614 | 		low: 57.875350873413225,
615 | 		open: 62.747405667247016,
616 | 		time: { year: 2018, month: 11, day: 27 },
617 | 	},
618 | 	{
619 | 		close: 61.231150731698605,
620 | 		high: 66.3829902228434,
621 | 		low: 61.231150731698605,
622 | 		open: 65.01028486919516,
623 | 		time: { year: 2018, month: 11, day: 28 },
624 | 	},
625 | 	{
626 | 		close: 64.9698540874806,
627 | 		high: 77.09783903299783,
628 | 		low: 58.455031795628194,
629 | 		open: 58.455031795628194,
630 | 		time: { year: 2018, month: 11, day: 29 },
631 | 	},
632 | 	{
633 | 		close: 72.40978471883417,
634 | 		high: 72.40978471883417,
635 | 		low: 53.05804901549206,
636 | 		open: 65.907298021202,
637 | 		time: { year: 2018, month: 11, day: 30 },
638 | 	},
639 | 	{
640 | 		close: 74.60745731538934,
641 | 		high: 78.33742117000789,
642 | 		low: 54.42067144918077,
643 | 		open: 73.20930147914103,
644 | 		time: { year: 2018, month: 12, day: 1 },
645 | 	},
646 | 	{
647 | 		close: 64.10866184869924,
648 | 		high: 76.14506447001202,
649 | 		low: 61.5224432669736,
650 | 		open: 69.33984127682314,
651 | 		time: { year: 2018, month: 12, day: 2 },
652 | 	},
653 | 	{
654 | 		close: 65.92038759928786,
655 | 		high: 76.98479070362022,
656 | 		low: 65.92038759928786,
657 | 		open: 69.32298264631615,
658 | 		time: { year: 2018, month: 12, day: 3 },
659 | 	},
660 | 	{
661 | 		close: 68.23682161095334,
662 | 		high: 77.6723729460968,
663 | 		low: 68.23682161095334,
664 | 		open: 74.39471534484744,
665 | 		time: { year: 2018, month: 12, day: 4 },
666 | 	},
667 | 	{
668 | 		close: 67.45035792565862,
669 | 		high: 83.53728553118547,
670 | 		low: 67.45035792565862,
671 | 		open: 74.79418570077237,
672 | 		time: { year: 2018, month: 12, day: 5 },
673 | 	},
674 | 	{
675 | 		close: 79.26722967320323,
676 | 		high: 79.26722967320323,
677 | 		low: 68.40654829383521,
678 | 		open: 68.40654829383521,
679 | 		time: { year: 2018, month: 12, day: 6 },
680 | 	},
681 | 	{
682 | 		close: 74.95305464030587,
683 | 		high: 81.65884414224071,
684 | 		low: 64.08761481290135,
685 | 		open: 81.65884414224071,
686 | 		time: { year: 2018, month: 12, day: 7 },
687 | 	},
688 | 	{
689 | 		close: 86.30802154315482,
690 | 		high: 91.21953112925642,
691 | 		low: 65.46112304993535,
692 | 		open: 77.82514647663533,
693 | 		time: { year: 2018, month: 12, day: 8 },
694 | 	},
695 | 	{
696 | 		close: 82.67218208289492,
697 | 		high: 92.45833377442081,
698 | 		low: 76.80728739647081,
699 | 		open: 87.18916937056241,
700 | 		time: { year: 2018, month: 12, day: 9 },
701 | 	},
702 | 	{
703 | 		close: 73.86125805398967,
704 | 		high: 83.68952750914036,
705 | 		low: 73.86125805398967,
706 | 		open: 75.76119064173785,
707 | 		time: { year: 2018, month: 12, day: 10 },
708 | 	},
709 | 	{
710 | 		close: 79.00109311074502,
711 | 		high: 88.74271558831151,
712 | 		low: 69.00900811612337,
713 | 		open: 88.74271558831151,
714 | 		time: { year: 2018, month: 12, day: 11 },
715 | 	},
716 | 	{
717 | 		close: 80.98779620162513,
718 | 		high: 97.07429720104427,
719 | 		low: 73.76970378608283,
720 | 		open: 88.57288529720472,
721 | 		time: { year: 2018, month: 12, day: 12 },
722 | 	},
723 | 	{
724 | 		close: 87.83619759370346,
725 | 		high: 91.29759438607132,
726 | 		low: 74.00740214639268,
727 | 		open: 87.51853658661781,
728 | 		time: { year: 2018, month: 12, day: 13 },
729 | 	},
730 | 	{
731 | 		close: 87.50134898892377,
732 | 		high: 102.95635188637507,
733 | 		low: 81.0513723219724,
734 | 		open: 94.74009794290814,
735 | 		time: { year: 2018, month: 12, day: 14 },
736 | 	},
737 | 	{
738 | 		close: 92.40159548029843,
739 | 		high: 103.24363067710844,
740 | 		low: 75.44605394394573,
741 | 		open: 95.99903495559444,
742 | 		time: { year: 2018, month: 12, day: 15 },
743 | 	},
744 | 	{
745 | 		close: 87.43619322092951,
746 | 		high: 99.39349139000474,
747 | 		low: 80.24624983473528,
748 | 		open: 99.39349139000474,
749 | 		time: { year: 2018, month: 12, day: 16 },
750 | 	},
751 | 	{
752 | 		close: 84.42724177432086,
753 | 		high: 95.57485075893881,
754 | 		low: 84.42724177432086,
755 | 		open: 90.71070399095831,
756 | 		time: { year: 2018, month: 12, day: 17 },
757 | 	},
758 | 	{
759 | 		close: 96.04408990868804,
760 | 		high: 101.02158248010466,
761 | 		low: 94.38544669520195,
762 | 		open: 101.02158248010466,
763 | 		time: { year: 2018, month: 12, day: 18 },
764 | 	},
765 | 	{
766 | 		close: 97.2120815653703,
767 | 		high: 103.35830035963959,
768 | 		low: 78.72594316029567,
769 | 		open: 86.98009038330306,
770 | 		time: { year: 2018, month: 12, day: 19 },
771 | 	},
772 | 	{
773 | 		close: 105.23366706522204,
774 | 		high: 106.56174456393981,
775 | 		low: 94.6658899187065,
776 | 		open: 106.56174456393981,
777 | 		time: { year: 2018, month: 12, day: 20 },
778 | 	},
779 | 	{
780 | 		close: 89.53750874231946,
781 | 		high: 112.27917367188074,
782 | 		low: 87.13586952228918,
783 | 		open: 96.0857985693989,
784 | 		time: { year: 2018, month: 12, day: 21 },
785 | 	},
786 | 	{
787 | 		close: 88.55787263435407,
788 | 		high: 112.62138454627025,
789 | 		low: 80.42783344898223,
790 | 		open: 88.34340019789849,
791 | 		time: { year: 2018, month: 12, day: 22 },
792 | 	},
793 | 	{
794 | 		close: 86.00639650371167,
795 | 		high: 110.94532193307279,
796 | 		low: 74.78703575498496,
797 | 		open: 92.4275741143068,
798 | 		time: { year: 2018, month: 12, day: 23 },
799 | 	},
800 | 	{
801 | 		close: 90.45119640254379,
802 | 		high: 92.51500970997435,
803 | 		low: 82.69475430846728,
804 | 		open: 86.21662699549296,
805 | 		time: { year: 2018, month: 12, day: 24 },
806 | 	},
807 | 	{
808 | 		close: 93.38124264891343,
809 | 		high: 93.38124264891343,
810 | 		low: 84.5674956907938,
811 | 		open: 87.54923273867136,
812 | 		time: { year: 2018, month: 12, day: 25 },
813 | 	},
814 | 	{
815 | 		close: 87.88725775527871,
816 | 		high: 90.14253631595105,
817 | 		low: 77.28638555494503,
818 | 		open: 83.93199044032968,
819 | 		time: { year: 2018, month: 12, day: 26 },
820 | 	},
821 | 	{
822 | 		close: 71.77940077333062,
823 | 		high: 89.25710176370582,
824 | 		low: 67.74278646676306,
825 | 		open: 78.5346198695072,
826 | 		time: { year: 2018, month: 12, day: 27 },
827 | 	},
828 | 	{
829 | 		close: 72.08757207606054,
830 | 		high: 79.36518615067514,
831 | 		low: 69.18787486704672,
832 | 		open: 69.18787486704672,
833 | 		time: { year: 2018, month: 12, day: 28 },
834 | 	},
835 | 	{
836 | 		close: 73.87977927793119,
837 | 		high: 77.62891475860795,
838 | 		low: 70.42293039125319,
839 | 		open: 70.42293039125319,
840 | 		time: { year: 2018, month: 12, day: 29 },
841 | 	},
842 | 	{
843 | 		close: 74.86330345366132,
844 | 		high: 75.88473282167168,
845 | 		low: 62.89549355427313,
846 | 		open: 74.86554252962132,
847 | 		time: { year: 2018, month: 12, day: 30 },
848 | 	},
849 | 	{
850 | 		close: 71.00787215611817,
851 | 		high: 71.00787215611817,
852 | 		low: 57.29681995441558,
853 | 		open: 60.04464694823929,
854 | 		time: { year: 2018, month: 12, day: 31 },
855 | 	},
856 | 	// hide-end
857 | ]);
858 | 
859 | chart.timeScale().fitContent();
860 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/two-price-scales.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Two Price Scales
 3 | sidebar_label: Two Price Scales
 4 | description: An example of how to add two price scales to a chart.
 5 | pagination_prev: null
 6 | pagination_next: null
 7 | keywords:
 8 |   - price
 9 |   - scale
10 | ---
11 | 
12 | It is possible to have two price scales visible on a Lightweight Charts™,
13 | namely one on the right side (default) and another on the left. This example
14 | shows how to configure your chart to contain two price scales.
15 | 
16 | ## Short answer
17 | 
18 | Ensure that `rightPriceScale` and `leftPriceScale` has the `visibility` property
19 | set to `true` within the [chart options](/docs/api/interfaces/ChartOptionsBase#leftpricescale).
20 | 
21 | ```js
22 | chart.applyOptions({
23 |     rightPriceScale: {
24 |         visible: true,
25 |     },
26 |     leftPriceScale: {
27 |         visible: true,
28 |     },
29 | });
30 | ```
31 | 
32 | and assign the `priceScaleId` property on the [series options](/docs/api/interfaces/SeriesOptionsCommon#pricescaleid)
33 | for the series which you would like to use the left scale. Note that by default a
34 | series will use the right scale thus we don't need to set that property on the other series.
35 | 
36 | ```js
37 | const leftSeries = chart.addSeries(CandlestickSeries, {
38 |     priceScaleId: 'left',
39 | });
40 | ```
41 | 
42 | You can see a full [working example](#full-example) below.
43 | 
44 | ## Tips
45 | 
46 | By default the crosshair will snap to the data points of the first series.
47 | You may prefer to set the [crosshair mode](/docs/api/enumerations/CrosshairMode) to
48 | `normal` so that you get a crosshair which allows sits directly beneath your cursor.
49 | 
50 | ```js
51 | chart.applyOptions({
52 |     crosshair: {
53 |         mode: 0, // CrosshairMode.Normal
54 |     },
55 | });
56 | ```
57 | 
58 | ## Resources
59 | 
60 | You can learn more about price scales here: [Price scale](/docs/price-scale)
61 | 
62 | and view the related APIs here:
63 | - [Chart Options](/docs/api/interfaces/ChartOptionsBase#leftpricescale)
64 | - [PriceScaleOptions](/docs/api/interfaces/PriceScaleOptions)
65 | - [SeriesOptionsCommon priceScaleId](/docs/api/interfaces/SeriesOptionsCommon#pricescaleid)
66 | 
67 | ## Full example
68 | 
69 | import UsageGuidePartial from "../_usage-guide-partial.mdx";
70 | import CodeBlock from "@theme/CodeBlock";
71 | import code from "!!raw-loader!./two-price-scales.js";
72 | 
73 | <CodeBlock replaceThemeConstants chart className="language-js" hideableCode chartOnTop codeUsage={<UsageGuidePartial />}>
74 |     {code}
75 | </CodeBlock>
76 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/watermark-advanced.js:
--------------------------------------------------------------------------------
 1 | // remove-start
 2 | // Lightweight Charts™ Example: Image Watermark
 3 | // https://tradingview.github.io/lightweight-charts/tutorials/how_to/watermark
 4 | 
 5 | // remove-end
 6 | const chartOptions = {
 7 | 	layout: {
 8 | 		textColor: CHART_TEXT_COLOR,
 9 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
10 | 	},
11 | };
12 | // remove-line
13 | /** @type {import('lightweight-charts').IChartApi} */
14 | const chart = createChart(document.getElementById('container'), chartOptions);
15 | 
16 | // highlight-start
17 | // imageDataUrl would usually be an url like '/images/my-image.png'
18 | const imageDataUrl = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOTIiIGhlaWdodD0iMTI4IiB2aWV3Qm94PSIwIDAgMjkyIDEyOCI+PHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBkPSJtMTgyLjkzIDcuNi42My0uMzdhNjQuMSA2NC4xIDAgMCAwIDIuNDMtNS4zMWw0Ljc3LTEuMzlhNjQuNjggNjQuNjggMCAwIDEtNC43MiAxMC41NGMuMzggMTAuNDUtMy45MyAyMS4xNS0xMS4xIDI5LjM3LTExLjY2IDEzLjQxLTI2Ljk4IDE1Ljk3LTQzLjU3IDEzLjc4bDEuMDctLjk4YTIxLjEgMjEuMSAwIDAgMCAzLjcyLTQuMDUgNDguMzcgNDguMzcgMCAwIDEtMTEuMDQgMi44NGMtMTAuNjUtNS41NC0yMS42NC0xNC45NC0yNC4yNy0yNy4yNyA5LjE5LTE3IDI4Ljk1LTI0LjAxIDQ3LjM5LTE5Ljk0YTIyLjU3IDIyLjU3IDAgMCAwIDUuODYgOS4wMmMtLjEyLTEuOTItLjEtMy44NC0uMS01Ljc2bC4wMS0xLjc4YzQuOCAyLjk2IDkuNjYgNS44NSAxNS41MiA1LjcgNC4wOC0uMSA4LjQtMS41MiAxMy40LTQuNFptLTIyLjU1IDIzLjI4YTguNDggOC40OCAwIDAgMC0xMi40NS0uMzNsLTcuOS03LjI2QTguNiA4LjYgMCAwIDAgMTMyIDEyYy02LjE0IDAtMTAuMjUgNi42My03LjcgMTIuMDlsLTEzLjAyIDEyLjE5Yy00LjEtNC45Ny01LjY4LTkuMy02LjE3LTEwLjk0IDguMzYtMTMuNzIgMjQuNDYtMjAuMTggNDAuMTUtMTcuMDcgMi45MyA2LjkgOC4zOCAxMC43MiAxNC43NyAxMy45NmwtLjMzLTEuMTRjLS43NC0yLjU2LTEuNDctNS4xLTEuNjItNy43OCA3LjA1IDMuNDUgMTQuNiAzLjM1IDIxLjc2LjMxLTQuNzYgNy4yNy0xMS4xMyAxNC4yMi0xOS40NiAxNy4yNlptLTIyLjU2LTQuMTkgOC4wMyA3LjM4QTguNiA4LjYgMCAwIDAgMTU0IDQ1YTguNiA4LjYgMCAwIDAgOC4yNS0xMC41NWM3Ljk5LTMuMDggMTQuMzctOS4zOCAxOS4yOC0xNi4yMy0zLjQ3IDE5LjQ3LTIxLjk2IDM0LjYxLTQxLjkgMzIuOTggMS43Ny0yLjg0IDIuNDktNi4wNiAzLjIxLTkuMjhsLjM1LTEuNTZjLTUuNDcgMy43Ny0xMC42NyA2LjM4LTE3LjM3IDcuNTJhNDkuOSA0OS45IDAgMCAxLTExLjg1LTguNjVsMTIuODMtMTJhOC41OCA4LjU4IDAgMCAwIDExLjAyLS41NFpNMTMyIDE2YTQuNSA0LjUgMCAxIDAgMCA5IDQuNSA0LjUgMCAwIDAgMC05Wm0xNy41IDIwLjVhNC41IDQuNSAwIDEgMSA5IDAgNC41IDQuNSAwIDAgMS05IDBaTTIxLjYzIDcxLjhhMi4zMyAyLjMzIDAgMCAxIDIuMzMgMi4zNCAyLjM0IDIuMzQgMCAwIDEtMi4zMyAyLjM3IDIuMzggMi4zOCAwIDAgMS0yLjM3LTIuMzcgMi4zOCAyLjM4IDAgMCAxIDIuMzctMi4zM1ptMS43NiA4LjJ2MTZoLTMuNTJWODBoMy41MlptLTYuNDYgMTZIMi43OFY3My4yOGgzLjc1djE5LjE0aDEwLjRWOTZabTI2LjM5LTEuMDlWODBIMzkuOHYyLjE0YTYuMjYgNi4yNiAwIDAgMC01LjEyLTIuNDZjLTQuMzIgMC03LjY4IDMuNTgtNy42OCA4LjEgMCA0LjU0IDMuMzYgOC4xMiA3LjY4IDguMTIgMi4yIDAgNC4xNi0xLjA4IDUuMTItMi41djEuNDhjMCAzLjIzLTIuMTggNS00LjgzIDVhNy4wMyA3LjAzIDAgMCAxLTUuMzItMi4zNGwtMi4xNCAyLjUyYzEuNTcgMS43NiA0LjM1IDIuOTUgNy40OSAyLjk1IDQuNzMgMCA4LjMyLTIuNTMgOC4zMi04LjFabS0xMi43Ny03LjEzYTQuNyA0LjcgMCAwIDEgNC43Ny00LjkgNC43IDQuNyAwIDAgMSA0Ljc3IDQuOSA0LjcgNC43IDAgMCAxLTQuNzcgNC45IDQuNyA0LjcgMCAwIDEtNC43Ny00LjlaTTUxLjU4IDk2aC0zLjUyVjcyaDMuNTJ2MTAuMThjLjk2LTEuNiAyLjc4LTIuNSA0Ljg2LTIuNSAzLjcxIDAgNi4xMSAyLjYyIDYuMTEgNi42OVY5NmgtMy41MnYtOS4wNmMwLTIuNTItMS4yOC00LjA2LTMuMzMtNC4wNi0yLjMzIDAtNC4xMiAxLjgyLTQuMTIgNS4yNVY5NlptMjQuODYtLjJ2LTMuMTNjLS41Mi4yLTEuMjIuMzItMS45LjMyLTEuODIgMC0yLjY4LS43My0yLjY4LTIuNzJ2LTcuMTNoNC41OFY4MGgtNC41OHYtNC40NWgtMy41MlY4MGgtMy4zM3YzLjE0aDMuMzN2Ny43YzAgMy42MiAyLjQgNS4zMiA1LjQ3IDUuMzIgMS4wOSAwIDEuOTItLjEzIDIuNjMtLjM1Wm0yMC4zLjJIOTMuNGwtMy41Mi0xMC4zN0w4Ni4zOSA5NmgtMy4zMmwtNS4zOC0xNmgzLjcybDMuNDUgMTEgMy42OC0xMWgyLjY5bDMuNjUgMTEgMy40OS0xMWgzLjc0bC01LjM4IDE2Wm02Ljc2LThjMCA0Ljg2IDMuNDkgOC4zMiA4LjM1IDguMzIgMy4zNiAwIDUuODYtMS40NCA3LjMtMy43MWwtMi43LTEuOTJhNS4wMyA1LjAzIDAgMCAxLTQuNTcgMi40M2MtMi42NSAwLTQuNzctMS43My00LjkzLTQuMzVoMTIuNThjLjAzLS41MS4wMy0uOC4wMy0xLjE1IDAtNS4xNi0zLjUyLTcuOTQtNy43MS03Ljk0QTguMTIgOC4xMiAwIDAgMCAxMDMuNSA4OFptOC4yMi01LjM0YzIuMDUgMCAzLjkgMS4yNCA0LjI5IDMuNTVoLTguOWMuNDgtMi4zNyAyLjU2LTMuNTUgNC42MS0zLjU1Wm0xMy4yMi0xMC44NWEyLjMzIDIuMzMgMCAwIDEgMi4zNCAyLjMzIDIuMzQgMi4zNCAwIDAgMS0yLjM0IDIuMzcgMi4zOCAyLjM4IDAgMCAxLTIuMzctMi4zNyAyLjM4IDIuMzggMCAwIDEgMi4zNy0yLjMzWm0yMS43IDIzLjFWODBoLTMuNTN2Mi4xNGE2LjI2IDYuMjYgMCAwIDAtNS4xMi0yLjQ2Yy00LjMyIDAtNy42OCAzLjU4LTcuNjggOC4xIDAgNC41NCAzLjM2IDguMTIgNy42OCA4LjEyIDIuMiAwIDQuMTYtMS4wOCA1LjEyLTIuNXYxLjQ4YzAgMy4yMy0yLjE4IDUtNC44MyA1YTcuMDMgNy4wMyAwIDAgMS01LjMxLTIuMzRsLTIuMTUgMi41MmMxLjU3IDEuNzYgNC4zNiAyLjk1IDcuNSAyLjk1IDQuNzMgMCA4LjMxLTIuNTMgOC4zMS04LjFaTTEyNi43IDk2aC0zLjUyVjgwaDMuNTJ2MTZabTcuMTYtOC4yMmE0LjcgNC43IDAgMCAxIDQuNzctNC45IDQuNyA0LjcgMCAwIDEgNC43NyA0LjkgNC43IDQuNyAwIDAgMS00Ljc3IDQuOSA0LjcgNC43IDAgMCAxLTQuNzctNC45Wk0xNTQuOSA5NmgtMy41MlY3MmgzLjUydjEwLjE4Yy45Ni0xLjYgMi43OC0yLjUgNC44Ni0yLjUgMy43MSAwIDYuMTEgMi42MiA2LjExIDYuNjlWOTZoLTMuNTJ2LTkuMDZjMC0yLjUyLTEuMjgtNC4wNi0zLjMyLTQuMDYtMi4zNCAwLTQuMTMgMS44Mi00LjEzIDUuMjVWOTZabTI0Ljg2LS4ydi0zLjEzYy0uNTEuMi0xLjIyLjMyLTEuODkuMzItMS44MiAwLTIuNjktLjczLTIuNjktMi43MnYtNy4xM2g0LjU4VjgwaC00LjU4di00LjQ1aC0zLjUyVjgwaC0zLjMzdjMuMTRoMy4zM3Y3LjdjMCAzLjYyIDIuNCA1LjMyIDUuNDcgNS4zMiAxLjEgMCAxLjkyLS4xMyAyLjYzLS4zNVptMjEuNTkuNThhMTEuNjcgMTEuNjcgMCAwIDEtMTEuNzUtMTEuNzRjMC02LjU2IDUuMjItMTEuNzQgMTEuNzUtMTEuNzQgNC40NSAwIDguMjIgMi4yNyAxMC4yNCA1Ljc2bC0zLjIzIDEuODVhNy45NCA3Ljk0IDAgMCAwLTcuMDEtNCA3Ljk2IDcuOTYgMCAwIDAtNy45NyA4LjEzIDcuOTYgNy45NiAwIDAgMCA3Ljk3IDguMTMgNy45NCA3Ljk0IDAgMCAwIDctNGwzLjI0IDEuODVhMTEuNjYgMTEuNjYgMCAwIDEtMTAuMjQgNS43NlptMTMuNC0uMzhoMy41MnYtNy44N2MwLTMuNDMgMS44LTUuMjUgNC4xMy01LjI1IDIuMDUgMCAzLjMzIDEuNTQgMy4zMyA0LjA2Vjk2aDMuNTJ2LTkuNjNjMC00LjA3LTIuNC02LjY5LTYuMTEtNi42OS0yLjA4IDAtMy45LjktNC44NyAyLjVWNzJoLTMuNTJ2MjRabTI1LjU2LjMyYy00LjM4IDAtNy43LTMuNzQtNy43LTguMzJzMy4zMi04LjMyIDcuNy04LjMyYzIuMyAwIDQuMjMgMS4xOCA1LjEyIDIuNDZWODBoMy41MnYxNmgtMy41MnYtMi4xNGE2LjM4IDYuMzggMCAwIDEtNS4xMiAyLjQ2Wm0uNjQtMy4yYzIuODUgMCA0Ljc3LTIuMjQgNC43Ny01LjEycy0xLjkyLTUuMTItNC43Ny01LjEyYy0yLjg0IDAtNC43NiAyLjI0LTQuNzYgNS4xMnMxLjkxIDUuMTIgNC43NiA1LjEyWk0yNTMuNzEgOTZoMy41MnYtNy44YzAtMy4yIDEuODMtNC45IDMuODQtNC45LjY0IDAgMS4xNS4xIDEuNzYuMjh2LTMuNjFjLS40OC0uMS0uOTMtLjEzLTEuMzctLjEzYTQuNSA0LjUgMCAwIDAtNC4yMyAzVjgwaC0zLjUydjE2Wm0yMS43My0zLjMzdjMuMTRjLS43LjIyLTEuNTQuMzUtMi42My4zNS0zLjA3IDAtNS40Ny0xLjctNS40Ny01LjMxdi03LjcxaC0zLjMzVjgwaDMuMzN2LTQuNDVoMy41MlY4MGg0LjU4djMuMTRoLTQuNTh2Ny4xM2MwIDEuOTkuODYgMi43MiAyLjY5IDIuNzIuNjcgMCAxLjM3LS4xMyAxLjg5LS4zMlptMTQuMjEtMS4zMWMwLTIuNjItMS42Ni00LjAzLTQuNDgtNC44NmwtMS42My0uNDhjLTEuNTctLjQ1LTEuOTItMS4xMi0xLjkyLTEuOSAwLS45NSAxLjA5LTEuNSAyLjE1LTEuNSAxLjMgMCAyLjMzLjY0IDMuMDQgMS42NGwyLjQzLTEuODZjLTEuMTItMS43Ni0zLjAxLTIuNzItNS40MS0yLjcyLTMuMiAwLTUuNyAxLjczLTUuNzMgNC41OC0uMDMgMi4zNiAxLjQxIDQuMTIgNC4yIDQuOWwxLjQuMzhjMS45Mi41NyAyLjQ3IDEuMTIgMi40NyAyLjA0IDAgMS4xMi0xLjA2IDEuNy0yLjMgMS43LTEuNjQgMC0zLjItLjgtMy44NS0yLjJsLTIuNTkgMS44NWMxLjE1IDIuMjcgMy41OCAzLjM5IDYuNDMgMy4zOSAzLjMgMCA1LjgtMS44OSA1LjgtNC45NlptLTE0My4zOCAyMS40YzAgLjQ2LS4zNy44NC0uODMuODRhLjg2Ljg2IDAgMCAxLS44Ny0uODVjMC0uNDYuMzktLjg1Ljg3LS44NS40NiAwIC44My4zOS44My44NVptLS4yOSAxMS4yNGgtMS4xMnYtOGgxLjEydjhabS01Mi4wMi4xNmE0LjA0IDQuMDQgMCAwIDAgMy45OC00LjE2IDQuMDQgNC4wNCAwIDAgMC0zLjk4LTQuMTZjLTEuMjQgMC0yLjM5LjY0LTIuOTYgMS41VjExMmgtMS4xMnYxMkg5MXYtMS4zNGMuNTcuODYgMS43MiAxLjUgMi45NiAxLjVabS0uMTItMS4wNGMtMS43NCAwLTIuOTQtMS40LTIuOTQtMy4xMiAwLTEuNzMgMS4yLTMuMTIgMi45NC0zLjEyIDEuNzUgMCAyLjk1IDEuNCAyLjk1IDMuMTIgMCAxLjczLTEuMiAzLjEyLTIuOTUgMy4xMlptNy45IDQuMjIgNS4zLTExLjM0aC0xLjI2bC0yLjkzIDYuMzUtMi45My02LjM1aC0xLjI0bDMuNTUgNy42LTEuNzYgMy43NGgxLjI2Wk0xMTUuMyAxMjRoLTEuMnYtMTAuMmgtMy42OHYtMS4xNmg4LjU2djEuMTVoLTMuNjhWMTI0Wm0zLjgyIDBoMS4xMnYtNC4wMmMwLTIuMDQgMS4yMy0yLjk0IDIuMjItMi45NC4yNCAwIC40NS4wMy42Ny4xMXYtMS4xN2EyLjQ0IDIuNDQgMCAwIDAtMi45IDEuNjZWMTE2aC0xLjExdjhabTExLjcyLTEuMzRhMy42NCAzLjY0IDAgMCAxLTIuOTYgMS41IDQuMDQgNC4wNCAwIDAgMS0zLjk4LTQuMTYgNC4wNCA0LjA0IDAgMCAxIDMuOTgtNC4xNmMxLjIzIDAgMi4zOS42NCAyLjk2IDEuNVYxMTZoMS4xMnY4aC0xLjEydi0xLjM0Wm0tNS44LTIuNjZjMCAxLjczIDEuMiAzLjEyIDIuOTUgMy4xMiAxLjc1IDAgMi45NS0xLjQgMi45NS0zLjEyIDAtMS43My0xLjItMy4xMi0yLjk1LTMuMTItMS43NCAwLTIuOTQgMS40LTIuOTQgMy4xMlptMTIuOTggNC4xNmMxLjIzIDAgMi4zOS0uNjQgMi45Ni0xLjVWMTI0aDEuMTJ2LTEySDE0MXY1LjM0YTMuNjQgMy42NCAwIDAgMC0yLjk2LTEuNSA0LjA0IDQuMDQgMCAwIDAtMy45OCA0LjE2IDQuMDQgNC4wNCAwIDAgMCAzLjk4IDQuMTZabS4xMS0xLjA0Yy0xLjc0IDAtMi45NC0xLjQtMi45NC0zLjEyIDAtMS43MyAxLjItMy4xMiAyLjk0LTMuMTIgMS43NSAwIDIuOTUgMS40IDIuOTUgMy4xMiAwIDEuNzMtMS4yIDMuMTItMi45NSAzLjEyWm0xMC42Ljg4aDEuMTF2LTMuOThjMC0xLjk5IDEuMS0zLjE0IDIuNS0zLjE0IDEuMTkgMCAyLjAyLjg2IDIuMDIgMi4yN1YxMjRoMS4xMnYtNWMwLTEuOTYtMS4yNy0zLjE2LTMuMDEtMy4xNi0xLjA0IDAtMi4wNS40NS0yLjYzIDEuNVYxMTZoLTEuMTF2OFptMTYuNzEtLjQyYzAgMi42MS0xLjcyIDMuOTItMy45NSAzLjkyLTEuODQgMC0zLjE3LS44My0zLjc3LTEuNzRsLjg4LS43NWEzLjQgMy40IDAgMCAwIDIuOSAxLjQ1YzEuMzcgMCAyLjgyLS44MyAyLjgyLTIuOTR2LTEuMDJjLS41Ny44Ni0xLjcgMS41LTIuOTIgMS41YTMuOTQgMy45NCAwIDAgMS0zLjk2LTQuMDggMy45NCAzLjk0IDAgMCAxIDMuOTYtNC4wOGMxLjIzIDAgMi4zNS42NCAyLjkyIDEuNVYxMTZoMS4xMnY3LjU4Wm0tNi44NC0zLjY2YzAgMS43MyAxLjE2IDMuMDQgMi45IDMuMDQgMS43NSAwIDIuOTItMS4zMSAyLjkyLTMuMDRzLTEuMTctMy4wNC0yLjkxLTMuMDRjLTEuNzUgMC0yLjkxIDEuMzEtMi45MSAzLjA0Wm0xMy41NSA0LjA4IDQuODgtMTEuMzZoLTEuMzVsLTQuMDMgOS4zOC00LjAzLTkuMzhoLTEuMzZsNC45IDExLjM2aC45OVptNy44NC0xMS4yNWMwIC40Ny0uMzcuODUtLjgzLjg1YS44Ni44NiAwIDAgMS0uODYtLjg1YzAtLjQ2LjM4LS44NS44Ni0uODUuNDcgMCAuODMuMzkuODMuODVabS0uMjggMTEuMjVoLTEuMTN2LThoMS4xM3Y4Wm02LjIuMTZhMy45IDMuOSAwIDAgMCAzLjU2LTEuOTVsLS45MS0uNmEyLjc4IDIuNzggMCAwIDEtMi42NCAxLjUxIDIuODcgMi44NyAwIDAgMS0yLjk2LTIuOTNoNi43NXYtLjNjLS4wMi0yLjU2LTEuNjgtNC4wNS0zLjc2LTQuMDVhNC4wNSA0LjA1IDAgMCAwLTQuMTUgNC4xNmMwIDIuMyAxLjYgNC4xNiA0LjEyIDQuMTZabS0uMDEtNy4yOGMxLjM0IDAgMi40NS44OCAyLjY0IDIuMzJoLTUuNDlhMi44NCAyLjg0IDAgMCAxIDIuODUtMi4zMlptMTMuNTUgNy4xMmgtLjkzbC0yLjEtNi4xLTIuMTQgNi4xaC0uOTJsLTIuNzQtOGgxLjE1bDIuMDggNi4wOCAyLjExLTYuMDhoLjg3bDIuMTEgNi4wOCAyLjA4LTYuMDhoMS4xN2wtMi43NCA4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PC9zdmc+';
19 | createImageWatermark(chart.panes()[0], imageDataUrl, {
20 | 	alpha: 0.5,
21 | 	padding: 20,
22 | });
23 | // highlight-end
24 | 
25 | const lineSeries = chart.addSeries(AreaSeries, {
26 | 	topColor: AREA_TOP_COLOR,
27 | 	bottomColor: AREA_BOTTOM_COLOR,
28 | 	lineColor: LINE_LINE_COLOR,
29 | 	lineWidth: 2,
30 | });
31 | 
32 | const data = [
33 | 	{ value: 0, time: 1642425322 },
34 | 	// hide-start
35 | 	{ value: 8, time: 1642511722 },
36 | 	{ value: 10, time: 1642598122 },
37 | 	{ value: 20, time: 1642684522 },
38 | 	{ value: 3, time: 1642770922 },
39 | 	{ value: 43, time: 1642857322 },
40 | 	{ value: 41, time: 1642943722 },
41 | 	{ value: 43, time: 1643030122 },
42 | 	{ value: 56, time: 1643116522 },
43 | 	{ value: 46, time: 1643202922 },
44 | 	// hide-end
45 | ];
46 | 
47 | lineSeries.setData(data);
48 | 
49 | chart.timeScale().fitContent();
50 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/watermark-simple.js:
--------------------------------------------------------------------------------
 1 | // remove-start
 2 | // Lightweight Charts™ Example: Watermark Simple
 3 | // https://tradingview.github.io/lightweight-charts/tutorials/how_to/watermark
 4 | 
 5 | // remove-end
 6 | const chartOptions = {
 7 | 	layout: {
 8 | 		textColor: CHART_TEXT_COLOR,
 9 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
10 | 	},
11 | };
12 | // remove-line
13 | /** @type {import('lightweight-charts').IChartApi} */
14 | const chart = createChart(document.getElementById('container'), chartOptions);
15 | 
16 | // remove-line
17 | /** @type {import('lightweight-charts').createTextWatermark} */
18 | // highlight-start
19 | createTextWatermark(chart.panes()[0], {
20 | 	horzAlign: 'center',
21 | 	vertAlign: 'center',
22 | 	lines: [
23 | 		{
24 | 			text: 'Watermark Example',
25 | 			color: 'rgba(171, 71, 188, 0.5)',
26 | 			fontSize: 24,
27 | 		},
28 | 	],
29 | });
30 | // highlight-end
31 | 
32 | const lineSeries = chart.addSeries(AreaSeries, {
33 | 	topColor: AREA_TOP_COLOR,
34 | 	bottomColor: AREA_BOTTOM_COLOR,
35 | 	lineColor: LINE_LINE_COLOR,
36 | 	lineWidth: 2,
37 | });
38 | 
39 | const data = [
40 | 	{ value: 0, time: 1642425322 },
41 | 	// hide-start
42 | 	{ value: 8, time: 1642511722 },
43 | 	{ value: 10, time: 1642598122 },
44 | 	{ value: 20, time: 1642684522 },
45 | 	{ value: 3, time: 1642770922 },
46 | 	{ value: 43, time: 1642857322 },
47 | 	{ value: 41, time: 1642943722 },
48 | 	{ value: 43, time: 1643030122 },
49 | 	{ value: 56, time: 1643116522 },
50 | 	{ value: 46, time: 1643202922 },
51 | 	// hide-end
52 | ];
53 | 
54 | lineSeries.setData(data);
55 | 
56 | chart.timeScale().fitContent();
57 | 


--------------------------------------------------------------------------------
/website/tutorials/how_to/watermark.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | title: Watermark
  3 | sidebar_label: Watermark
  4 | description: Examples of how to add a watermark to your chart.
  5 | pagination_prev: null
  6 | pagination_next: null
  7 | keywords:
  8 |   - watermark
  9 |   - example
 10 | ---
 11 | 
 12 | Lightweight Charts™ has a built-in feature for displaying simple text watermarks on your chart.
 13 | This example shows how to configure and add this simple text watermark to your chart.
 14 | If you are looking to add a more complex watermark then have a look at the [image watermark example](#image-watermark-example)
 15 | included below.
 16 | 
 17 | ## Short answer
 18 | 
 19 | A simple text watermark can be configured and added by using the [`createTextWatermark`](/docs/next/api/functions/createTextWatermark) function exported
 20 | from the library as follows:
 21 | 
 22 | ```js
 23 | import { createTextWatermark } from 'lightweight-charts';
 24 | 
 25 | const firstPane = chart.panes()[0];
 26 | const textWatermark = createTextWatermark(firstPane, {
 27 |     horzAlign: 'center',
 28 |     vertAlign: 'center',
 29 |     lines: [
 30 |         {
 31 |             text: 'Watermark Example',
 32 |             color: 'rgba(171, 71, 188, 0.5)',
 33 |             fontSize: 24,
 34 |         },
 35 |     ],
 36 | });
 37 | 
 38 | ```
 39 | 
 40 | The options available for the watermark are: [TextWatermark Options](/docs/next/api/interfaces/TextWatermarkOptions).
 41 | 
 42 | You can see full [working examples](#examples) below.
 43 | 
 44 | ## Resources
 45 | 
 46 | - [`createTextWatermark` function](/docs/next/api/functions/createTextWatermark).
 47 | - [TextWatermark Options](/docs/next/api/interfaces/TextWatermarkOptions)
 48 | 
 49 | ## Examples
 50 | 
 51 | import UsageGuidePartial from "../_usage-guide-partial.mdx";
 52 | 
 53 | <UsageGuidePartial />
 54 | 
 55 | import CodeBlock from "@theme/CodeBlock";
 56 | 
 57 | ### Simple Watermark Example
 58 | 
 59 | import codeSimple from "!!raw-loader!./watermark-simple.js";
 60 | 
 61 | <CodeBlock replaceThemeConstants chart className="language-js" hideableCode chartOnTop>
 62 | 	{codeSimple}
 63 | </CodeBlock>
 64 | 
 65 | ### Image Watermark Example
 66 | 
 67 | If a simple text watermark doesn't meet your requirements then you can use the Image watermark via [`createImageWatermark`](/docs/next/api/functions/createImageWatermark) function exported
 68 | from the library as follows:
 69 | 
 70 | ```js
 71 | import { createImageWatermark } from 'lightweight-charts';
 72 | 
 73 | const firstPane = chart.panes()[0];
 74 | const imageWatermark = createImageWatermark(firstPane, '/images/my-image.png', {
 75 |     alpha: 0.5,
 76 |     padding: 20,
 77 | });
 78 | ```
 79 | 
 80 | The options available for the watermark are: [ImageWatermark Options](/docs/next/api/interfaces/ImageWatermarkOptions).
 81 | 
 82 | You can see full [working examples](#examples) below.
 83 | 
 84 | ## Resources
 85 | 
 86 | - [`createImageWatermark` pane primitive](/docs/next/api/functions/createTextWatermark).
 87 | - [ImageWatermark Options](/docs/next/api/interfaces/ImageWatermarkOptions)
 88 | 
 89 | :::tip
 90 | 
 91 | Since the watermark image is black content with a transparent background, it may not be visible when
 92 | viewing the documentation site in dark mode.
 93 | 
 94 | :::
 95 | 
 96 | import codeAdvanced from "!!raw-loader!./watermark-advanced.js";
 97 | 
 98 | <CodeBlock replaceThemeConstants chart className="language-js" hideableCode chartOnTop>
 99 | 	{codeAdvanced}
100 | </CodeBlock>
101 | 


--------------------------------------------------------------------------------
/website/tutorials/index.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_position: 0
  3 | pagination_next: null
  4 | ---
  5 | 
  6 | import CardLinkList from "@site/src/components/CardLinkList";
  7 | import Shapes from "@site/src/img/shapes.svg";
  8 | import ReactLogo from "@site/src/img/react.svg";
  9 | import VuejsLogo from "@site/src/img/vuejs.svg";
 10 | import WebComponentsLogo from "@site/src/img/webcomponents.svg";
 11 | import A11y from "@site/src/img/a11y.svg";
 12 | 
 13 | # Tutorials
 14 | 
 15 | import VersionWarningAdmonition from "@site/src/components/VersionWarningAdmonition";
 16 | 
 17 | {/*
 18 |   Show warning when not on the latest published version
 19 |   Tutorials section isn't versioned yet, hence the need for the warning message
 20 | */}
 21 | 
 22 | <VersionWarningAdmonition
 23 | 	notCurrent="These tutorials are for the latest published version of Lightweight Charts."
 24 | 	type="caution"
 25 | 	displayVersionMessage
 26 | />
 27 | 
 28 | ## Guides
 29 | 
 30 | <CardLinkList
 31 | 	items={[
 32 | 		{
 33 | 			href: "/tutorials/customization/intro",
 34 | 			title: "Customization",
 35 | 			image: <Shapes />,
 36 | 			description: "Customizing appearance & features",
 37 | 		},
 38 | 		{
 39 | 			href: "/tutorials/a11y/intro",
 40 | 			title: "Accessibility",
 41 | 			image: <A11y />,
 42 | 			description: "How to improve A11y support",
 43 | 		},
 44 | 	]}
 45 | />
 46 | 
 47 | ## Framework integrations
 48 | 
 49 | This section contains some tutorials how to use Lightweight Charts™ with some popular frameworks.
 50 | 
 51 | <CardLinkList
 52 | 	items={[
 53 | 		{
 54 | 			href: "/tutorials/react/simple",
 55 | 			title: "React",
 56 | 			image: <ReactLogo />,
 57 | 			description: "Integration guide for React",
 58 | 		},
 59 | 		{
 60 | 			href: "/tutorials/vuejs/wrapper",
 61 | 			title: "Vue.js",
 62 | 			image: <VuejsLogo />,
 63 | 			description: "Integration guide for Vue.js",
 64 | 		},
 65 | 		{
 66 | 			href: "/tutorials/webcomponents/custom-element",
 67 | 			title: "Web Components",
 68 | 			image: <WebComponentsLogo />,
 69 | 			description: "Web components custom element",
 70 | 		},
 71 | 	]}
 72 | />
 73 | 
 74 | :::info
 75 | 
 76 | If you think that a tutorial is missing feel free to ask [in the discussions](https://github.com/tradingview/lightweight-charts/discussions)
 77 | or submit your own.
 78 | 
 79 | :::
 80 | 
 81 | ## How To
 82 | 
 83 | A collection of code examples showcasing the various capabilities of the library, and how to implement common additional features.
 84 | 
 85 | import { useDocsSidebar } from '@docusaurus/plugin-content-docs/client';
 86 | export const HowToList = () => {
 87 | 	const examplesCategory = useDocsSidebar().items.find(
 88 | 		item => item.type === "category" && item.label === "How To"
 89 | 	);
 90 | 	const examples = examplesCategory.items.filter(doc => doc.type === "link");
 91 | 	return (
 92 | 		<ul>
 93 | 			{examples.map(docLink => (
 94 | 				<li key={docLink.docId}>
 95 | 					<a href={docLink.href}>{docLink.label}</a>
 96 | 				</li>
 97 | 			))}
 98 | 		</ul>
 99 | 	);
100 | };
101 | 
102 | <HowToList />
103 | 
104 | ## Examples / Demos
105 | 
106 | A collection of demos showcasing the various capabilities of the library.
107 | 
108 | export const ExamplesList = () => {
109 | 	const examplesCategory = useDocsSidebar().items.find(
110 | 		item => item.type === "category" && item.label === "Examples / Demos"
111 | 	);
112 | 	const examples = examplesCategory.items.filter(doc => doc.type === "link");
113 | 	return (
114 | 		<ul>
115 | 			{examples.map(docLink => (
116 | 				<li key={docLink.docId}>
117 | 					<a href={docLink.href}>{docLink.label}</a>
118 | 				</li>
119 | 			))}
120 | 		</ul>
121 | 	);
122 | };
123 | 
124 | <ExamplesList />
125 | 
126 | ## Analysis indicators
127 | 
128 | The [analysis indicator](./tutorials/analysis-indicators) examples below serve as a starting point for creating your own indicators.
129 | You can use them directly in your projects.
130 | Follow the links to see the indicators' source code on GitHub.
131 | 
132 | To run them locally, follow the [setup instructions](https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/) in the repository.
133 | You can also explore each indicator in action on a [live demo page](https://tradingview.github.io/lightweight-charts/indicator-examples/).
134 | 
135 | <CardLinkList
136 | 	items={[
137 | 		{
138 | 			href: "https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/average-price",
139 | 			title: "Average Price",
140 | 			description: "Calculates the average of prices (e.g., open, high, low, close)",
141 | 		},
142 | 		{
143 | 			href: "https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/correlation",
144 | 			title: "Correlation",
145 | 			description: "Measures the statistical relationship between two data series",
146 | 		},
147 | 		{
148 | 			href: "https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/median-price",
149 | 			title: "Median Price",
150 | 			description: "Returns the median (middle) value between high and low prices",
151 | 		},
152 | 		{
153 | 			href: "https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/momentum",
154 | 			title: "Momentum",
155 | 			description: "Measures the rate of change in price over time",
156 | 		},
157 | 		{
158 | 			href: "https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/moving-average",
159 | 			title: "Simple Moving Average",
160 | 			description: "Smooths data by averaging values over a fixed period",
161 | 		},
162 | 		{
163 | 			href: "https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/percent-change",
164 | 			title: "Percent Change",
165 | 			description: "Shows the relative change between two values as a percentage",
166 | 		},
167 | 		{
168 | 			href: "https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/product",
169 | 			title: "Product",
170 | 			description: "Multiplies a series of values",
171 | 		},
172 | 		{
173 | 			href: "https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/ratio",
174 | 			title: "Ratio",
175 | 			description: "Divides one value by another",
176 | 		},
177 | 		{
178 | 			href: "https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/spread",
179 | 			title: "Spread",
180 | 			description: "Calculates the difference between two values",
181 | 		},
182 | 		{
183 | 			href: "https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/sum",
184 | 			title: "Sum",
185 | 			description: "Adds up a series of values",
186 | 		},
187 | 		{
188 | 			href: "https://github.com/tradingview/lightweight-charts/tree/master/indicator-examples/src/indicators/weighted-close",
189 | 			title: "Weighted Close",
190 | 			description: "Calculates a weighted average of high, low, and close prices",
191 | 		},
192 | 	]}
193 | />
194 | 


--------------------------------------------------------------------------------
/website/tutorials/react/01-simple.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_label: 'Simple example'
 3 | hide_table_of_contents: true
 4 | ---
 5 | 
 6 | # React - Simple example
 7 | 
 8 | :::info
 9 | 
10 | The following only describes a relatively simple example that only renders an [area series](/docs/series-types#area) that could be tweaked to render any other type of [series](/docs/series-types).
11 | 
12 | For a more complete scenario where you could wrap Lightweight Charts™ into a component having sub components, please consult this [example](./advanced).
13 | 
14 | :::
15 | 
16 | On this page you will learn how to easily use Lightweight Charts™ with React.
17 | 
18 | ## Preparing your project
19 | 
20 | For the example purpose we are using [Parcel starter kit](https://github.com/brandiqa/react-parcel-starter) but feel free to use any other tool or starter kit.
21 | 
22 | ```console
23 | git clone git@github.com:brandiqa/react-parcel-starter.git lwc-react
24 | cd lwc-react
25 | npm install
26 | ```
27 | 
28 | To run your project simply
29 | 
30 | ```console
31 | npm start
32 | ```
33 | 
34 | This will create a web page accessible by default on [http://localhost:1234](http://localhost:1234).
35 | 
36 | ## Creating a charting component
37 | 
38 | The example _React component_ on this page may not fit your requirements completely. Creating a general purpose declarative wrapper for Lightweight Charts™ imperative API is a challenge, but hopefully you can adapt this example to your use case.
39 | 
40 | :::info
41 | 
42 | For this example we are using props to set chart colors based on the current theme (light or dark). In your real code it might be a better idea to use a [Context](https://reactjs.org/docs/context.html#when-to-use-context).
43 | :::
44 | 
45 | import { ThemedChart } from '@site/src/components/tutorials/themed-chart-colors-wrapper';
46 | import CodeBlock from '@theme/CodeBlock';
47 | import code from '!!raw-loader!@site/src/components/tutorials/simple-react-example';
48 | 
49 | <CodeBlock replaceThemeConstants className="language-jsx">{code}</CodeBlock>
50 | 
51 | and you'll have a reusable component that could then be enhanced, tweaked to meet your needs, adding properties and even functionalities.
52 | 
53 | If you've successfully followed all the steps you should see something similar to
54 | 
55 | import { App } from '@site/src/components/tutorials/simple-react-example';
56 | import styles from '@site/src/pages/chart.module.css';
57 | 
58 | <div className={styles.ChartContainer}>
59 |     <ThemedChart ChartComponent={App}/>
60 | </div>
61 | 


--------------------------------------------------------------------------------
/website/tutorials/react/02-advanced.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_label: 'Advanced example'
  3 | hide_table_of_contents: true
  4 | ---
  5 | 
  6 | # React - Advanced example
  7 | 
  8 | :::info
  9 | 
 10 | The following describes a more complex scenario where a user could imagine splitting the responsibilities of the chart between components.
 11 | 
 12 | If you want to consult a simpler approach please consult this [example](./simple).
 13 | 
 14 | :::
 15 | 
 16 | :::warning
 17 | 
 18 | By following the steps below we assume you're familiar with Lightweight Charts™, how to set up a project using it and how to render a chart.
 19 | 
 20 | If not, please follow this [guide](./simple).
 21 | 
 22 | :::
 23 | 
 24 | If you're familiar with Lightweight Charts™ you probably already know that a _Chart_ is a container that can contain one or more [_Series_](/docs/series-types).
 25 | Each _Series_ has its own options (for instance [AreaStyleOptions](/docs/api/interfaces/AreaStyleOptions), [LineStyleOptions](/docs/api/interfaces/LineStyleOptions), etc) in addition to [price](/docs/price-scale) and/or [time](/docs/time-scale) scale.
 26 | 
 27 | Based on this principle, one could easily imagine having a main component _Chart_ that could have some _Series_ children that could themselves have other children and so on.
 28 | Therefore the structure could become something like
 29 | 
 30 | ```
 31 | <Chart component>
 32 |     <Series component 1>
 33 |         <child component />
 34 |     </Series component 1>
 35 |     <Series component n>
 36 |         <child component />
 37 |     </Series component n>
 38 | </Chart component>
 39 | ```
 40 | 
 41 | Even though it's possible to create a Chart without a Series, the complexity arises when another component wants to interact with any of its siblings/parent, like updating a series by adding more data or resizing the chart itself.
 42 | 
 43 | Given this tutorial is about React this is how we are going to define components relying on React [Hooks](https://reactjs.org/docs/hooks-intro.html) and [composition](https://reactjs.org/docs/composition-vs-inheritance.html).
 44 | 
 45 | However, one drawback with the way React and its hooks like _useEffect_ [work](https://github.com/facebook/react/issues/16728) in a parent/children implementation is that their respective hooks are called in a bottom-up order for instanciation but top-to-bottom when it comes to clean-up.
 46 | 
 47 | The following skeleton illustrates the mechanism.
 48 | 
 49 | ```js
 50 | import React, { useEffect } from 'react';
 51 | 
 52 | export const ParentComponent = () => {
 53 |     // this effect will be triggered in position 3
 54 |     useEffect(() =>
 55 |         () => {
 56 |             // this clean up will be triggered in position 1
 57 |         }
 58 |     , []);
 59 | 
 60 |     // this effect will be triggered in position 4
 61 |     useEffect(() =>
 62 |         () => {
 63 |             // this clean up will be triggered in position 2
 64 |         }
 65 |     , []);
 66 | 
 67 |     // The parent will then return Following bit is to propagate all props & internalRef object down to children
 68 |     return (
 69 |         <ChildComponent />
 70 |     );
 71 | };
 72 | ParentComponent.displayName = 'ParentComponent';
 73 | 
 74 | export const ChildComponent = () => {
 75 |     // this effect will be triggered in position 1
 76 |     useEffect(() =>
 77 |         () => {
 78 |             // this clean up will be triggered in position 3
 79 |         }
 80 |     , []);
 81 | 
 82 |     // this effect will be triggered in position 2
 83 |     useEffect(() =>
 84 |         () => {
 85 |             // this clean up will be triggered in position 4
 86 |         }
 87 |     , []);
 88 | 
 89 |     return (
 90 |         <div />
 91 |     );
 92 | };
 93 | ChildComponent.displayName = 'ChildComponent';
 94 | ```
 95 | 
 96 | In essence, taking the example above, it means that a `ChildComponent` (aka Series) would be created first whilst requiring a `ParentComponent` (aka Chart).
 97 | 
 98 | To achieve that, we will have to rely on a few hooks and take advantage of the way they work in addition to use [ref/forwardRef](https://reactjs.org/docs/forwarding-refs.html) which is a technique to pass down properties from one component to its children.
 99 | 
100 | In the end the "visible" structure and usage will be alike but internally it will be something like:
101 | 
102 | ```
103 | <Chart component>
104 |     <ChartContainer>
105 |         <Series component 1>
106 |             <child component />
107 |         </Series component 1>
108 |         <Series component n>
109 |             <child component />
110 |         </Series component n>
111 |     </ChartContainer>
112 | </Chart component>
113 | ```
114 | 
115 | where the ChartContainer's role would be needed to attach a DOMElement on which the chart will render.
116 | ChartContainer will be responsible for creating a **ref**erence that will hold functions to handle the lifecycle of the chart.
117 | That reference will then be propagated down to the Series.
118 | 
119 | The same technique will be used within the Series component to handle this time the lifecycle of any Series along with adding data to be plotted.
120 | 
121 | Moreover those 2 "main" components will "expose" whatever functions the user wants from the internal reference object at a higher level, meaning once those references are accessible any other component would then be able to act on either the Chart or any Series.
122 | 
123 | Here's a skeleton of what the final structure would be like:
124 | 
125 | ```js
126 | import React, { useEffect, useImperativeHandle, useRef, createContext, forwardRef } from 'react';
127 | 
128 | const Context = createContext();
129 | 
130 | export const MainComponent = props =>
131 |     // Creates the first reference and instanciate a ParentComponent
132 |     (
133 |         <div ref={chartReference}>
134 |             <ParentComponent {...props} container={container} />
135 |         </div>
136 |     );
137 | 
138 | export const ParentComponent = forwardRef((props, ref) => {
139 |     const internalRef = useRef({
140 |         method1() {
141 |             // This function would be responsible for creating the chart for instance
142 |         },
143 |         methodn() {
144 |             // This function would be responsible for cleaning up the chart
145 |         },
146 |     });
147 | 
148 |     // this effect will be triggered in position 3
149 |     useEffect(() =>
150 |         () => {
151 |             // this clean up will be triggered in position 1
152 |         }
153 |     , []);
154 | 
155 |     // this effect will be triggered in position 4
156 |     useEffect(() =>
157 |         () => {
158 |             // this clean up will be triggered in position 2
159 |         }
160 |     , []);
161 | 
162 |     useImperativeHandle(ref, () => {
163 |         // That's the hook responsible for exposing part of/entirety of internalRef
164 |     }, []);
165 | 
166 |     // Following bit is to propagate all props & internalRef object down to children
167 |     return (
168 |         <Context.Provider value={internalRef.current}>
169 |             {props.children}
170 |         </Context.Provider>
171 |     );
172 | });
173 | ParentComponent.displayName = 'ParentComponent';
174 | 
175 | export const ChildComponent = forwardRef((props, ref) => {
176 |     const internalRef = useRef({
177 |         method1() {
178 |             // This function would be responsible for creating a series
179 |         },
180 |         methodn() {
181 |             // This function would be responsible for removing it
182 |         },
183 |     });
184 | 
185 |     // this effect will be triggered in position 1
186 |     useEffect(() =>
187 |         () => {
188 |             // this clean up will be triggered in position 3
189 |         }
190 |     , []);
191 | 
192 |     // this effect will be triggered in position 2
193 |     useEffect(() =>
194 |         () => {
195 |             // this clean up will be triggered in position 4
196 |         }
197 |     , []);
198 | 
199 |     useImperativeHandle(ref, () => {
200 |         // That's the hook responsible for exposing part of/entirety of internalRef
201 |     }, []);
202 | 
203 |     // Following bit is to propagate all props & internalRef object down to children
204 |     return (
205 |         <Context.Provider value={internalRef.current}>
206 |             {props.children}
207 |         </Context.Provider>
208 |     );
209 | });
210 | ChildComponent.displayName = 'ChildComponent';
211 | ```
212 | 
213 | By considering all the above you could end up with Chart/Series components looking like the following
214 | 
215 | :::info
216 | 
217 | For this example we are using props to set chart colors based on the current theme (light or dark). In your real code it might be a better idea to use a [Context](https://reactjs.org/docs/context.html#when-to-use-context).
218 | :::
219 | 
220 | import { ThemedChart } from '@site/src/components/tutorials/themed-chart-colors-wrapper';
221 | import CodeBlock from '@theme/CodeBlock';
222 | import code from '!!raw-loader!@site/src/components/tutorials/advanced-react-example';
223 | 
224 | <CodeBlock replaceThemeConstants className="language-jsx">{code}</CodeBlock>
225 | 
226 | The code above will produce a line series.
227 | Given a `series1` reference is created to be passed to the Series component you could reuse that object via `series1.current.[any function applicable on Series]`.
228 | 
229 | For instance and as shown below `series1.current.update(new data)` is used upon clicking on the button.
230 | 
231 | import { App } from '@site/src/components/tutorials/advanced-react-example';
232 | import styles from '@site/src/pages/chart.module.css';
233 | 
234 | <div className={styles.ChartContainer}>
235 |     <ThemedChart ChartComponent={App} />
236 | </div>
237 | 


--------------------------------------------------------------------------------
/website/tutorials/react/_category_.yml:
--------------------------------------------------------------------------------
1 | label: "React"
2 | 


--------------------------------------------------------------------------------
/website/tutorials/vuejs/01-wrapper.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | title: Vue.js - Wrapper Component
  3 | description:
  4 |   A simple example of how to use Lightweight Charts™ within the Vue.js framework.
  5 | pagination_prev: null
  6 | pagination_next: null
  7 | keywords:
  8 |   - vue
  9 |   - vue.js
 10 |   - example
 11 | ---
 12 | 
 13 | # Vue.js - Wrapper Component
 14 | 
 15 | :::info
 16 | 
 17 | The following describes a relatively simple example that only allows for a
 18 | single [series](/docs/series-types) to be rendered. This example can be used as
 19 | a starting point and could be tweaked further using our extensive
 20 | [API](/docs/api).
 21 | 
 22 | **Please note: this example is intended to be used with Vue.js 3**
 23 | 
 24 | :::
 25 | 
 26 | This guide will focus on the key concepts required to get Lightweight Charts™
 27 | running within a Vue component. Please note this guide is not intended as a
 28 | complete step-by-step tutorial. The example Vue components can be found at the
 29 | [bottom](#complete-sample-code) of this guide.
 30 | 
 31 | If you are new to Vue.js then please have a look at the
 32 | [official Vue.js tutorials](https://vuejs.org/guide/introduction.html) before
 33 | proceeding further with this example.
 34 | 
 35 | ## About the example wrapper component
 36 | 
 37 | The example Vue wrapper component has the following features.
 38 | 
 39 | The ability to:
 40 | 
 41 | - specify the series type via a component attribute,
 42 | - specify the series data via a component property,
 43 | - control the chart, series, time scale, and price scale options via properties,
 44 | - enable automatic resizing of the chart when the browser is resized.
 45 | 
 46 | The example may not fit your requirements completely. Creating a general-purpose
 47 | declarative wrapper for Lightweight Charts™ imperative API is a challenge, but
 48 | hopefully, you can adapt this example to your use case.
 49 | 
 50 | ### Component showcase
 51 | 
 52 | Presented below is the finished wrapper component which is discussed throughout
 53 | this guide. The interactive buttons beneath the chart are showcasing how to
 54 | interact with the component and that code is provided below as well (within the
 55 | example app component).
 56 | 
 57 | import BrowserOnly from '@docusaurus/BrowserOnly';
 58 | 
 59 | <BrowserOnly fallback={<div>Loading...</div>}>
 60 |     {() => {
 61 |         require('./assets/web-component.js');
 62 |         return <vue-example></vue-example>;
 63 |     }}
 64 | </BrowserOnly>
 65 | 
 66 | ### Vue API styles
 67 | 
 68 | Vue components can be authored in two different
 69 | [API styles](https://vuejs.org/guide/introduction.html#api-styles): _Options
 70 | API_ and _Composition API_.
 71 | 
 72 | This example will make use of the **Composition API**, but complete code
 73 | examples for both APIs will be presented at the end of the tutorial.
 74 | 
 75 | The Vue component could be used within any Vue setup, you can learn more on the
 76 | Vue documentation site:
 77 | [Ways of Vue](https://vuejs.org/guide/extras/ways-of-using-vue.html)
 78 | 
 79 | ## Integrating Lightweight Charts™ with Vue
 80 | 
 81 | ### Avoid using `Refs` for storing API instances
 82 | 
 83 | The preferred way to store a reference to the created chart
 84 | ([IChartApi](/docs/api/interfaces/IChartApi) instance), or any other of the
 85 | library's instances, is to make use of a plain JS variable or class field
 86 | instead of using Vue's [`ref`](https://vuejs.org/api/reactivity-core.html#ref)
 87 | functionality.
 88 | 
 89 | When Vue wraps an object in a reference object, it modifies the object (to
 90 | enable reactivity) in such a way that it interferes with the internal logic of
 91 | the Lightweight Charts™. This can lead to unexpected behaviour. If you really need
 92 | to use a [`ref`](https://vuejs.org/api/reactivity-core.html#ref) then please
 93 | consider using
 94 | [`shallowRef`](https://vuejs.org/api/reactivity-advanced.html#shallowref)
 95 | instead.
 96 | 
 97 | We can instead create a variable to hold these instances outside of any vue
 98 | hooks (such as
 99 | [`onMounted`](https://vuejs.org/api/composition-api-lifecycle.html#onmounted),
100 | [`watch`](https://vuejs.org/api/reactivity-core.html#watch)) within the body of
101 | the script.
102 | 
103 | ```html
104 | <script setup>
105 |     import { onMounted } from 'vue';
106 | 
107 |     // variable to store the created chart instance
108 |     let chart;
109 | 
110 |     onMounted() {
111 |         // ...
112 |     }
113 | </script>
114 | ```
115 | 
116 | ### Use the `onMounted` lifecycle hook to create the chart
117 | 
118 | Lightweight Charts™ requires an html element to use as its container, you can
119 | create a simple div element within the component's `template` and ask Vue to
120 | create a reference to that element by adding the `ref="chartContainer"`
121 | attribute to the div element and the corresponding variable within the script
122 | section: `const chartContainer = ref();`
123 | 
124 | The ideal time to create the chart is during the `mounted` lifecycle hook
125 | provided by the Vue component. The container div will be created and ready for
126 | use at this stage. Within the
127 | [`onMounted`](https://vuejs.org/api/composition-api-lifecycle.html#onmounted)
128 | hook we can call Lightweight Charts™ [`createChart`](/docs/api/functions/createChart)
129 | constructor and pass it the value of the container reference (which is the div
130 | element).
131 | 
132 | :::tip
133 | 
134 | Remember to also clean up when the component is unmounted
135 | ([`onUnmounted`](https://vuejs.org/api/composition-api-lifecycle.html#onunmounted)
136 | hook) by calling the [`remove`](/docs/api/interfaces/IChartApi#remove) method on
137 | the saved chart instance.
138 | 
139 | :::
140 | 
141 | ```html
142 | <script setup>
143 |     import { onMounted, ref } from 'vue';
144 |     import { createChart } from 'lightweight-charts';
145 | 
146 |     let chart;
147 |     const chartContainer = ref();
148 | 
149 |     onMounted(() => {
150 |         // Create the Lightweight Charts Instance using the container ref.
151 |         chart = createChart(chartContainer.value);
152 |     });
153 | 
154 |     onUnmounted(() => {
155 |         if (chart) {
156 |             chart.remove();
157 |             chart = null;
158 |         }
159 |     });
160 | </script>
161 | <template>
162 |     <div class="lw-chart" ref="chartContainer"></div>
163 | </template>
164 | <style scoped>
165 |     .lw-chart {
166 |         height: 100%;
167 |     }
168 | </style>
169 | ```
170 | 
171 | ### Providing option properties
172 | 
173 | A simple way to provide customisation of the chart to the component's consumers
174 | is to create component properties for the options you wish to be customised.
175 | Lightweight Charts™ has a variety of customisation options which can be applied
176 | through the [`applyOptions`](/docs/api/interfaces/IChartApi#applyoptions) method
177 | on an Api instance (such as [IChartApi](/docs/api/interfaces/IChartApi),
178 | [ISeriesApi](/docs/api/interfaces/ISeriesApi),
179 | [IPriceScaleApi](/docs/api/interfaces/IPriceScaleApi), and
180 | [ITimeScaleApi](/docs/api/interfaces/ITimeScaleApi)).
181 | 
182 | We can define properties for use as the components API as follows:
183 | 
184 | ```html
185 | <script setup>
186 |     import { defineProps } from 'vue';
187 | 
188 |     const props = defineProps({
189 |         type: {
190 |             type: String,
191 |             default: 'line',
192 |         },
193 |         data: {
194 |             type: Array,
195 |             required: true,
196 |         },
197 |         chartOptions: {
198 |             type: Object,
199 |         },
200 |         seriesOptions: {
201 |             type: Object,
202 |         },
203 |     });
204 | </script>
205 | ```
206 | 
207 | These properties can be used during the creation of Api instances, for example:
208 | 
209 | ```js
210 | chart = createChart(chartContainer.value, props.chartOptions);
211 | ```
212 | 
213 | We can instruct Vue to
214 | [`watch`](https://vuejs.org/api/reactivity-core.html#watch) these properties for
215 | changes and allow us to provide code to react to these changes. Using this
216 | mechanism, we can provide a direct mapping between the options properties and
217 | the `applyOptions` methods on the instance. This allows the consumer of the
218 | component to apply changes to the current options at any point during the
219 | lifecycle of the chart.
220 | 
221 | :::info
222 | 
223 | Please note: the current options aren't reset when applying the new options, and
224 | the new options can be a partial object. Thus it is possible to change one
225 | option at a time while still keeping the current options.
226 | 
227 | :::
228 | 
229 | ```js
230 | watch(
231 |     () => props.chartOptions,
232 |     newOptions => {
233 |         if (!chart) {
234 |             return;
235 |         }
236 |         chart.applyOptions(newOptions);
237 |     }
238 | );
239 | 
240 | watch(
241 |     () => props.priceScaleOptions,
242 |     newOptions => {
243 |         if (!chart) {
244 |             return;
245 |         }
246 |         chart.priceScale().applyOptions(newOptions);
247 |     }
248 | );
249 | ```
250 | 
251 | ### Exposing the chart instance or additional methods
252 | 
253 | There may be cases where you want to provide access to the chart instance, or
254 | provide useful methods, to the consumer of the component. This can be achieved
255 | with the
256 | [`defineExpose`](https://vuejs.org/api/sfc-script-setup.html#defineexpose) hook
257 | provided by Vue.
258 | 
259 | ```js
260 | import { defineExpose } from 'vue';
261 | 
262 | // A simple method to call `fitContent` on the time scale
263 | const fitContent = () => {
264 |     if (!chart) {
265 |         return;
266 |     }
267 |     chart.timeScale().fitContent();
268 | };
269 | 
270 | // Expose the chart instance via a method
271 | const getChart = () => chart;
272 | 
273 | defineExpose({ fitContent, getChart });
274 | ```
275 | 
276 | The consumer of the component can create a reference to a specific instance of
277 | the component and use the reference's value to evoke one of the exposed methods.
278 | 
279 | ```html
280 | <script setup>
281 |     import { ref } from 'vue';
282 |     import LWChart from './components/LWChart.vue';
283 | 
284 |     // ...
285 | 
286 |     const myChart = ref();
287 | 
288 |     const fitContent = () => {
289 |         // call a method on the component.
290 |         myChart.value.fitContent();
291 |     };
292 | </script>
293 | <template>
294 |     <LWChart type="line" :data="myData" ref="myChart" />
295 |     <button type="button" @click="fitContent">Fit Content</button>
296 | </template>
297 | ```
298 | 
299 | ## Complete Sample Code
300 | 
301 | Presented below is the complete component source code for the Vue components. We
302 | have also provided a sample Vue App component which showcases how to make use of
303 | these components within a typical Vue application.
304 | 
305 | You can view a complete Vue project using these components at this
306 | [StackBlitz example](https://stackblitz.com/edit/vitejs-vite-r4bbai?file=src/App.vue).
307 | 
308 | ### Composition API
309 | 
310 | The following code block contains the source code for the sample Vue component
311 | using the Composition API.
312 | 
313 | <p><a href={require('!!file-loader!./assets/composition-api.vue').default} download="lw-chart.vue" target="\_blank">Download file</a></p>
314 | 
315 | import CodeBlock from '@theme/CodeBlock';
316 | import InstantDetails from '@site/src/components/InstantDetails';
317 | import compositionCode from '!!raw-loader!./assets/composition-api.vue';
318 | 
319 | <InstantDetails>
320 |     <summary>Click here to reveal the code.</summary>
321 |     <CodeBlock className="language-html">{compositionCode}</CodeBlock>
322 | </InstantDetails>
323 | 
324 | ### Options API
325 | 
326 | The following code block contains the source code for the sample Vue component
327 | using the Options API.
328 | 
329 | <p><a href={require('!!file-loader!./assets/options-api.vue').default} download="lw-chart.vue" target="\_blank">Download file</a></p>
330 | 
331 | import optionsCode from '!!raw-loader!./assets/options-api.vue';
332 | 
333 | <InstantDetails>
334 |     <summary>Click here to reveal the code.</summary>
335 |     <CodeBlock className="language-html">{optionsCode}</CodeBlock>
336 | </InstantDetails>
337 | 
338 | ### Example Vue App Component
339 | 
340 | The following code block contains the source code for a sample Vue Application
341 | component which makes use of the Vue components shown above. It showcases a few
342 | ways to control and interact with the component.
343 | 
344 | <p><a href={require('!!file-loader!./assets/app.vue').default} download="app.vue" target="\_blank">Download file</a></p>
345 | 
346 | import appCode from '!!raw-loader!./assets/app.vue';
347 | 
348 | <InstantDetails>
349 |     <summary>Click here to reveal the code.</summary>
350 |     <CodeBlock className="language-html">{appCode}</CodeBlock>
351 | </InstantDetails>
352 | 


--------------------------------------------------------------------------------
/website/tutorials/vuejs/_category_.yml:
--------------------------------------------------------------------------------
1 | label: "Vue.js"
2 | 


--------------------------------------------------------------------------------
/website/tutorials/vuejs/assets/.eslintrc.js:
--------------------------------------------------------------------------------
1 | module.exports = {
2 | 	globals: {
3 | 		document: false,
4 | 		window: false,
5 | 	},
6 | };
7 | 


--------------------------------------------------------------------------------
/website/tutorials/vuejs/assets/app.vue:
--------------------------------------------------------------------------------
  1 | <script setup>
  2 | // This starter template is using Vue 3 <script setup> SFCs
  3 | // Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
  4 | import { ref } from 'vue';
  5 | 
  6 | /*
  7 |  * There are example components in both API styles: Options API, and Composition API
  8 |  *
  9 |  * Select your preferred style from the imports below:
 10 |  */
 11 | // import LWChart from './components/composition-api/LWChart.vue';
 12 | import LWChart from './components/options-api/LWChart.vue';
 13 | 
 14 | /**
 15 |  * Generates sample data for the Lightweight Charts™ example
 16 |  * @param  {Boolean} ohlc Whether generated dat should include open, high, low, and close values
 17 |  * @returns {Array} sample data
 18 |  */
 19 | function generateSampleData(ohlc) {
 20 | 	const randomFactor = 25 + Math.random() * 25;
 21 | 	function samplePoint(i) {
 22 | 		return (
 23 | 			i *
 24 | 				(0.5 +
 25 | 					Math.sin(i / 10) * 0.2 +
 26 | 					Math.sin(i / 20) * 0.4 +
 27 | 					Math.sin(i / randomFactor) * 0.8 +
 28 | 					Math.sin(i / 500) * 0.5) +
 29 | 			200
 30 | 		);
 31 | 	}
 32 | 
 33 | 	const res = [];
 34 | 	let date = new Date(Date.UTC(2018, 0, 1, 0, 0, 0, 0));
 35 | 	const numberOfPoints = ohlc ? 100 : 500;
 36 | 	for (var i = 0; i < numberOfPoints; ++i) {
 37 | 		const time = date.getTime() / 1000;
 38 | 		const value = samplePoint(i);
 39 | 		if (ohlc) {
 40 | 			const randomRanges = [
 41 | 				-1 * Math.random(),
 42 | 				Math.random(),
 43 | 				Math.random(),
 44 | 			].map(i => i * 10);
 45 | 			const sign = Math.sin(Math.random() - 0.5);
 46 | 			res.push({
 47 | 				time,
 48 | 				low: value + randomRanges[0],
 49 | 				high: value + randomRanges[1],
 50 | 				open: value + sign * randomRanges[2],
 51 | 				close: samplePoint(i + 1),
 52 | 			});
 53 | 		} else {
 54 | 			res.push({
 55 | 				time,
 56 | 				value,
 57 | 			});
 58 | 		}
 59 | 
 60 | 		date.setUTCDate(date.getUTCDate() + 1);
 61 | 	}
 62 | 
 63 | 	return res;
 64 | }
 65 | 
 66 | const chartOptions = ref({});
 67 | const data = ref(generateSampleData(false));
 68 | const seriesOptions = ref({
 69 | 	color: 'rgb(45, 77, 205)',
 70 | });
 71 | const chartType = ref('line');
 72 | const lwChart = ref();
 73 | 
 74 | function randomShade() {
 75 | 	return Math.round(Math.random() * 255);
 76 | }
 77 | 
 78 | const randomColor = (alpha = 1) => {
 79 | 	return `rgba(${randomShade()}, ${randomShade()}, ${randomShade()}, ${alpha})`;
 80 | };
 81 | 
 82 | const colorsTypeMap = {
 83 | 	area: [
 84 | 		['topColor', 0.4],
 85 | 		['bottomColor', 0],
 86 | 		['lineColor', 1],
 87 | 	],
 88 | 	bar: [
 89 | 		['upColor', 1],
 90 | 		['downColor', 1],
 91 | 	],
 92 | 	baseline: [
 93 | 		['topFillColor1', 0.28],
 94 | 		['topFillColor2', 0.05],
 95 | 		['topLineColor', 1],
 96 | 		['bottomFillColor1', 0.28],
 97 | 		['bottomFillColor2', 0.05],
 98 | 		['bottomLineColor', 1],
 99 | 	],
100 | 	candlestick: [
101 | 		['upColor', 1],
102 | 		['downColor', 1],
103 | 		['borderUpColor', 1],
104 | 		['borderDownColor', 1],
105 | 		['wickUpColor', 1],
106 | 		['wickDownColor', 1],
107 | 	],
108 | 	histogram: [['color', 1]],
109 | 	line: [['color', 1]],
110 | };
111 | 
112 | // Set a random colour for the series as an example of how
113 | // to apply new options to series. A similar appraoch will work on the
114 | // option properties.
115 | const changeColors = () => {
116 | 	const options = {};
117 | 	const colorsToSet = colorsTypeMap[chartType.value];
118 | 	colorsToSet.forEach(c => {
119 | 		options[c[0]] = randomColor(c[1]);
120 | 	});
121 | 	seriesOptions.value = options;
122 | };
123 | 
124 | const changeData = () => {
125 | 	const candlestickTypeData = ['candlestick', 'bar'].includes(chartType.value);
126 | 	const newData = generateSampleData(candlestickTypeData);
127 | 	data.value = newData;
128 | 	if (chartType.value === 'baseline') {
129 | 		const average =
130 | 			newData.reduce((s, c) => {
131 | 				return s + c.value;
132 | 			}, 0) / newData.length;
133 | 		seriesOptions.value = { baseValue: { type: 'price', price: average } };
134 | 	}
135 | };
136 | 
137 | const changeType = () => {
138 | 	const types = [
139 | 		'line',
140 | 		'area',
141 | 		'baseline',
142 | 		'histogram',
143 | 		'candlestick',
144 | 		'bar',
145 | 	].filter(t => t !== chartType.value);
146 | 	const randIndex = Math.round(Math.random() * (types.length - 1));
147 | 	chartType.value = types[randIndex];
148 | 	changeData();
149 | 
150 | 	// call a method on the component.
151 | 	lwChart.value.fitContent();
152 | };
153 | </script>
154 | 
155 | <template>
156 | 	<div class="chart-container">
157 | 		<LWChart
158 | 			:type="chartType"
159 | 			:data="data"
160 | 			:autosize="true"
161 | 			:chart-options="chartOptions"
162 | 			:series-options="seriesOptions"
163 | 			ref="lwChart"
164 | 		/>
165 | 	</div>
166 | 	<button type="button" @click="changeColors">Set Random Colors</button>
167 | 	<button type="button" @click="changeType">Change Chart Type</button>
168 | 	<button type="button" @click="changeData">Change Data</button>
169 | </template>
170 | <style scoped>
171 | .chart-container {
172 | 	height: calc(100% - 3.2em);
173 | }
174 | </style>
175 | 


--------------------------------------------------------------------------------
/website/tutorials/vuejs/assets/composition-api.vue:
--------------------------------------------------------------------------------
  1 | <script setup>
  2 | import {
  3 | 	ref,
  4 | 	onMounted,
  5 | 	onUnmounted,
  6 | 	watch,
  7 | 	defineExpose,
  8 | 	defineProps,
  9 | } from 'vue';
 10 | import {
 11 | 	createChart,
 12 | 	LineSeries,
 13 | 	AreaSeries,
 14 | 	BarSeries,
 15 | 	CandlestickSeries,
 16 | 	HistogramSeries,
 17 | 	BaselineSeries,
 18 | } from 'lightweight-charts';
 19 | 
 20 | const props = defineProps({
 21 | 	type: {
 22 | 		type: String,
 23 | 		default: 'line',
 24 | 	},
 25 | 	data: {
 26 | 		type: Array,
 27 | 		required: true,
 28 | 	},
 29 | 	autosize: {
 30 | 		default: true,
 31 | 		type: Boolean,
 32 | 	},
 33 | 	chartOptions: {
 34 | 		type: Object,
 35 | 	},
 36 | 	seriesOptions: {
 37 | 		type: Object,
 38 | 	},
 39 | 	timeScaleOptions: {
 40 | 		type: Object,
 41 | 	},
 42 | 	priceScaleOptions: {
 43 | 		type: Object,
 44 | 	},
 45 | });
 46 | 
 47 | function getChartSeriesDefinition(type) {
 48 | 	switch (type.toLowerCase()) {
 49 | 		case 'line':
 50 | 			return LineSeries;
 51 | 		case 'area':
 52 | 			return AreaSeries;
 53 | 		case 'bar':
 54 | 			return BarSeries;
 55 | 		case 'candlestick':
 56 | 			return CandlestickSeries;
 57 | 		case 'histogram':
 58 | 			return HistogramSeries;
 59 | 		case 'baseline':
 60 | 			return BaselineSeries;
 61 | 	}
 62 | 	return LineSeries;
 63 | }
 64 | 
 65 | // Lightweight Charts™ instances are stored as normal JS variables
 66 | // If you need to use a ref then it is recommended that you use `shallowRef` instead
 67 | let series;
 68 | let chart;
 69 | 
 70 | const chartContainer = ref();
 71 | 
 72 | const fitContent = () => {
 73 | 	if (!chart) return;
 74 | 	chart.timeScale().fitContent();
 75 | };
 76 | 
 77 | const getChart = () => {
 78 | 	return chart;
 79 | };
 80 | 
 81 | defineExpose({ fitContent, getChart });
 82 | 
 83 | // Auto resizes the chart when the browser window is resized.
 84 | const resizeHandler = () => {
 85 | 	if (!chart || !chartContainer.value) return;
 86 | 	const dimensions = chartContainer.value.getBoundingClientRect();
 87 | 	chart.resize(dimensions.width, dimensions.height);
 88 | };
 89 | 
 90 | // Creates the chart series and sets the data.
 91 | const addSeriesAndData = props => {
 92 | 	const seriesDefinition = getChartSeriesDefinition(props.type);
 93 | 	series = chart.addSeries(seriesDefinition, props.seriesOptions);
 94 | 	series.setData(props.data);
 95 | };
 96 | 
 97 | onMounted(() => {
 98 | 	// Create the Lightweight Charts Instance using the container ref.
 99 | 	chart = createChart(chartContainer.value, props.chartOptions);
100 | 	addSeriesAndData(props);
101 | 
102 | 	if (props.priceScaleOptions) {
103 | 		chart.priceScale().applyOptions(props.priceScaleOptions);
104 | 	}
105 | 
106 | 	if (props.timeScaleOptions) {
107 | 		chart.timeScale().applyOptions(props.timeScaleOptions);
108 | 	}
109 | 
110 | 	chart.timeScale().fitContent();
111 | 
112 | 	if (props.autosize) {
113 | 		window.addEventListener('resize', resizeHandler);
114 | 	}
115 | });
116 | 
117 | onUnmounted(() => {
118 | 	if (chart) {
119 | 		chart.remove();
120 | 		chart = null;
121 | 	}
122 | 	if (series) {
123 | 		series = null;
124 | 	}
125 | 	window.removeEventListener('resize', resizeHandler);
126 | });
127 | 
128 | /*
129 |  * Watch for changes to any of the component properties.
130 | 
131 |  * If an options property is changed then we will apply those options
132 |  * on top of any existing options previously set (since we are using the
133 |  * `applyOptions` method).
134 |  *
135 |  * If there is a change to the chart type, then the existing series is removed
136 |  * and the new series is created, and assigned the data.
137 |  *
138 |  */
139 | watch(
140 | 	() => props.autosize,
141 | 	enabled => {
142 | 		if (!enabled) {
143 | 			window.removeEventListener('resize', resizeHandler);
144 | 			return;
145 | 		}
146 | 		window.addEventListener('resize', resizeHandler);
147 | 	}
148 | );
149 | 
150 | watch(
151 | 	() => props.type,
152 | 	newType => {
153 | 		if (series && chart) {
154 | 			chart.removeSeries(series);
155 | 		}
156 | 		addSeriesAndData(props);
157 | 	}
158 | );
159 | 
160 | watch(
161 | 	() => props.data,
162 | 	newData => {
163 | 		if (!series) return;
164 | 		series.setData(newData);
165 | 	}
166 | );
167 | 
168 | watch(
169 | 	() => props.chartOptions,
170 | 	newOptions => {
171 | 		if (!chart) return;
172 | 		chart.applyOptions(newOptions);
173 | 	}
174 | );
175 | 
176 | watch(
177 | 	() => props.seriesOptions,
178 | 	newOptions => {
179 | 		if (!series) return;
180 | 		series.applyOptions(newOptions);
181 | 	}
182 | );
183 | 
184 | watch(
185 | 	() => props.priceScaleOptions,
186 | 	newOptions => {
187 | 		if (!chart) return;
188 | 		chart.priceScale().applyOptions(newOptions);
189 | 	}
190 | );
191 | 
192 | watch(
193 | 	() => props.timeScaleOptions,
194 | 	newOptions => {
195 | 		if (!chart) return;
196 | 		chart.timeScale().applyOptions(newOptions);
197 | 	}
198 | );
199 | </script>
200 | 
201 | <template>
202 | 	<div class="lw-chart" ref="chartContainer"></div>
203 | </template>
204 | 
205 | <style scoped>
206 | .lw-chart {
207 | 	height: 100%;
208 | }
209 | </style>
210 | 


--------------------------------------------------------------------------------
/website/tutorials/vuejs/assets/options-api.vue:
--------------------------------------------------------------------------------
  1 | <script>
  2 | import {
  3 | 	createChart,
  4 | 	LineSeries,
  5 | 	AreaSeries,
  6 | 	BarSeries,
  7 | 	CandlestickSeries,
  8 | 	HistogramSeries,
  9 | 	BaselineSeries,
 10 | } from 'lightweight-charts';
 11 | 
 12 | // Lightweight Chart instances are stored as normal JS variables
 13 | // If you need to use a ref then it is recommended that you use `shallowRef` instead
 14 | let series;
 15 | let chart;
 16 | 
 17 | function getChartSeriesDefinition(type) {
 18 | 	switch (type.toLowerCase()) {
 19 | 		case 'line':
 20 | 			return LineSeries;
 21 | 		case 'area':
 22 | 			return AreaSeries;
 23 | 		case 'bar':
 24 | 			return BarSeries;
 25 | 		case 'candlestick':
 26 | 			return CandlestickSeries;
 27 | 		case 'histogram':
 28 | 			return HistogramSeries;
 29 | 		case 'baseline':
 30 | 			return BaselineSeries;
 31 | 	}
 32 | 	return LineSeries;
 33 | }
 34 | 
 35 | // Creates the chart series and sets the data.
 36 | const addSeriesAndData = (type, seriesOptions, data) => {
 37 | 	const seriesDefinition = getChartSeriesDefinition(type);
 38 | 	series = chart.addSeries(seriesDefinition, seriesOptions);
 39 | 	series.setData(data);
 40 | };
 41 | 
 42 | // Auto resizes the chart when the browser window is resized.
 43 | const resizeHandler = container => {
 44 | 	if (!chart || !container) return;
 45 | 	const dimensions = container.getBoundingClientRect();
 46 | 	chart.resize(dimensions.width, dimensions.height);
 47 | };
 48 | 
 49 | export default {
 50 | 	props: {
 51 | 		type: {
 52 | 			type: String,
 53 | 			default: 'line',
 54 | 		},
 55 | 		data: {
 56 | 			type: Array,
 57 | 			required: true,
 58 | 		},
 59 | 		autosize: {
 60 | 			default: true,
 61 | 			type: Boolean,
 62 | 		},
 63 | 		chartOptions: {
 64 | 			type: Object,
 65 | 		},
 66 | 		seriesOptions: {
 67 | 			type: Object,
 68 | 		},
 69 | 		timeScaleOptions: {
 70 | 			type: Object,
 71 | 		},
 72 | 		priceScaleOptions: {
 73 | 			type: Object,
 74 | 		},
 75 | 	},
 76 | 	mounted() {
 77 | 		// Create the Lightweight Charts Instance using the container ref.
 78 | 		chart = createChart(this.$refs.chartContainer, this.chartOptions);
 79 | 		addSeriesAndData(this.type, this.seriesOptions, this.data);
 80 | 
 81 | 		if (this.priceScaleOptions) {
 82 | 			chart.priceScale().applyOptions(this.priceScaleOptions);
 83 | 		}
 84 | 
 85 | 		if (this.timeScaleOptions) {
 86 | 			chart.timeScale().applyOptions(this.timeScaleOptions);
 87 | 		}
 88 | 
 89 | 		chart.timeScale().fitContent();
 90 | 
 91 | 		if (this.autosize) {
 92 | 			window.addEventListener('resize', () =>
 93 | 				resizeHandler(this.$refs.chartContainer)
 94 | 			);
 95 | 		}
 96 | 	},
 97 | 	unmounted() {
 98 | 		if (chart) {
 99 | 			chart.remove();
100 | 			chart = null;
101 | 		}
102 | 		if (series) {
103 | 			series = null;
104 | 		}
105 | 		window.removeEventListener('resize', resizeHandler);
106 | 	},
107 | 	/*
108 | 	 * Watch for changes to any of the component properties.
109 | 	 *
110 | 	 * If an options property is changed then we will apply those options
111 | 	 * on top of any existing options previously set (since we are using the
112 | 	 * `applyOptions` method).
113 | 	 *
114 | 	 * If there is a change to the chart type, then the existing series is removed
115 | 	 * and the new series is created, and assigned the data.
116 | 	 *
117 | 	 */
118 | 	watch: {
119 | 		autosize(enabled) {
120 | 			if (!enabled) {
121 | 				window.removeEventListener('resize', () =>
122 | 					resizeHandler(this.$refs.chartContainer)
123 | 				);
124 | 				return;
125 | 			}
126 | 			window.addEventListener('resize', () =>
127 | 				resizeHandler(this.$refs.chartContainer)
128 | 			);
129 | 		},
130 | 		type(newType) {
131 | 			if (series && chart) {
132 | 				chart.removeSeries(series);
133 | 			}
134 | 			addSeriesAndData(this.type, this.seriesOptions, this.data);
135 | 		},
136 | 		data(newData) {
137 | 			if (!series) return;
138 | 			series.setData(newData);
139 | 		},
140 | 		chartOptions(newOptions) {
141 | 			if (!chart) return;
142 | 			chart.applyOptions(newOptions);
143 | 		},
144 | 		seriesOptions(newOptions) {
145 | 			if (!series) return;
146 | 			series.applyOptions(newOptions);
147 | 		},
148 | 		priceScaleOptions(newOptions) {
149 | 			if (!chart) return;
150 | 			chart.priceScale().applyOptions(newOptions);
151 | 		},
152 | 		timeScaleOptions(newOptions) {
153 | 			if (!chart) return;
154 | 			chart.timeScale().applyOptions(newOptions);
155 | 		},
156 | 	},
157 | 	methods: {
158 | 		fitContent() {
159 | 			if (!chart) return;
160 | 			chart.timeScale().fitContent();
161 | 		},
162 | 		getChart() {
163 | 			return chart;
164 | 		},
165 | 	},
166 | 	expose: ['fitContent', 'getChart'],
167 | };
168 | </script>
169 | 
170 | <template>
171 | 	<div class="lw-chart" ref="chartContainer"></div>
172 | </template>
173 | 
174 | <style scoped>
175 | .lw-chart {
176 | 	height: 100%;
177 | }
178 | </style>
179 | 


--------------------------------------------------------------------------------
/website/tutorials/vuejs/assets/web-component.js:
--------------------------------------------------------------------------------
  1 | /*
  2 |  * This is the Web Component version of the App Vue component
  3 |  *
  4 |  * This WC is used as the on-page example for the Vue tutorial, and includes
  5 |  * some specific logic for reacting to the current docusaurus theme and adjusting the
  6 |  * chart colours as required.
  7 |  */
  8 | import { defineCustomElement } from 'vue/dist/vue.esm-bundler';
  9 | import {
 10 | 	createChart,
 11 | 	ColorType,
 12 | 	LineSeries,
 13 | 	AreaSeries,
 14 | 	BarSeries,
 15 | 	CandlestickSeries,
 16 | 	HistogramSeries,
 17 | 	BaselineSeries,
 18 | } from 'lightweight-charts';
 19 | import { themeColors } from '../../../theme-colors';
 20 | 
 21 | let series;
 22 | let chart;
 23 | 
 24 | function getChartSeriesDefinition(type) {
 25 | 	switch (type) {
 26 | 		case 'line':
 27 | 			return LineSeries;
 28 | 		case 'area':
 29 | 			return AreaSeries;
 30 | 		case 'candlestick':
 31 | 			return CandlestickSeries;
 32 | 		case 'baseline':
 33 | 			return BaselineSeries;
 34 | 		case 'bar':
 35 | 			return BarSeries;
 36 | 		case 'histogram':
 37 | 			return HistogramSeries;
 38 | 	}
 39 | 	throw new Error(`${type} is an unsupported series type`);
 40 | }
 41 | 
 42 | const addSeriesAndData = (type, seriesOptions, data) => {
 43 | 	series = chart.addSeries(getChartSeriesDefinition(type), seriesOptions);
 44 | 	series.setData(data);
 45 | };
 46 | 
 47 | const resizeHandler = container => {
 48 | 	if (!chart || !container) {
 49 | 		return;
 50 | 	}
 51 | 	const dimensions = container.getBoundingClientRect();
 52 | 	chart.resize(dimensions.width, dimensions.height);
 53 | };
 54 | 
 55 | const LWChart = {
 56 | 	props: {
 57 | 		type: {
 58 | 			type: String,
 59 | 			default: 'line',
 60 | 		},
 61 | 		data: {
 62 | 			type: Array,
 63 | 			required: true,
 64 | 		},
 65 | 		autosize: {
 66 | 			default: true,
 67 | 			type: Boolean,
 68 | 		},
 69 | 		chartOptions: {
 70 | 			type: Object,
 71 | 		},
 72 | 		seriesOptions: {
 73 | 			type: Object,
 74 | 		},
 75 | 		timeScaleOptions: {
 76 | 			type: Object,
 77 | 		},
 78 | 		priceScaleOptions: {
 79 | 			type: Object,
 80 | 		},
 81 | 	},
 82 | 	template: `<div class="lw-chart" ref="lightweightChart"></div>`,
 83 | 	mounted() {
 84 | 		chart = createChart(this.$refs.lightweightChart, this.chartOptions);
 85 | 		addSeriesAndData(this.type, this.seriesOptions, this.data);
 86 | 
 87 | 		if (this.priceScaleOptions) {
 88 | 			chart.priceScale().applyOptions(this.priceScaleOptions);
 89 | 		}
 90 | 
 91 | 		if (this.timeScaleOptions) {
 92 | 			chart.timeScale().applyOptions(this.timeScaleOptions);
 93 | 		}
 94 | 
 95 | 		chart.timeScale().fitContent();
 96 | 
 97 | 		if (this.autosize) {
 98 | 			window.addEventListener('resize', () =>
 99 | 				resizeHandler(this.$refs.lightweightChart)
100 | 			);
101 | 		}
102 | 	},
103 | 	unmounted() {
104 | 		if (chart) {
105 | 			chart.remove();
106 | 			chart = null;
107 | 		}
108 | 		if (series) {
109 | 			series = null;
110 | 		}
111 | 	},
112 | 	watch: {
113 | 		autosize(enabled) {
114 | 			if (!enabled) {
115 | 				window.removeEventListener('resize', () =>
116 | 					resizeHandler(this.$refs.lightweightChart)
117 | 				);
118 | 				return;
119 | 			}
120 | 			window.addEventListener('resize', () =>
121 | 				resizeHandler(this.$refs.lightweightChart)
122 | 			);
123 | 		},
124 | 		type() {
125 | 			if (series && chart) {
126 | 				chart.removeSeries(series);
127 | 			}
128 | 			addSeriesAndData(this.type, this.seriesOptions, this.data);
129 | 		},
130 | 		data(newData) {
131 | 			if (!series) {
132 | 				return;
133 | 			}
134 | 			series.setData(newData);
135 | 		},
136 | 		chartOptions(newOptions) {
137 | 			if (!chart) {
138 | 				return;
139 | 			}
140 | 			chart.applyOptions(newOptions);
141 | 		},
142 | 		seriesOptions(newOptions) {
143 | 			if (!series) {
144 | 				return;
145 | 			}
146 | 			series.applyOptions(newOptions);
147 | 		},
148 | 		priceScaleOptions(newOptions) {
149 | 			if (!chart) {
150 | 				return;
151 | 			}
152 | 			chart.priceScale().applyOptions(newOptions);
153 | 		},
154 | 		timeScaleOptions(newOptions) {
155 | 			if (!chart) {
156 | 				return;
157 | 			}
158 | 			chart.timeScale().applyOptions(newOptions);
159 | 		},
160 | 	},
161 | 	methods: {
162 | 		fitContent() {
163 | 			if (!chart) {
164 | 				return;
165 | 			}
166 | 			chart.timeScale().fitContent();
167 | 		},
168 | 		getChart: () => chart,
169 | 	},
170 | 	expose: ['fitContent', 'getChart'],
171 | };
172 | 
173 | function generateSampleData(ohlc) {
174 | 	const randomFactor = 25 + Math.random() * 25;
175 | 	const samplePoint = i =>
176 | 		i *
177 | 			(0.5 +
178 | 				Math.sin(i / 10) * 0.2 +
179 | 				Math.sin(i / 20) * 0.4 +
180 | 				Math.sin(i / randomFactor) * 0.8 +
181 | 				Math.sin(i / 500) * 0.5) +
182 | 		200;
183 | 
184 | 	const res = [];
185 | 	const date = new Date(Date.UTC(2018, 0, 1, 0, 0, 0, 0));
186 | 	const numberOfPoints = ohlc ? 100 : 500;
187 | 	for (let i = 0; i < numberOfPoints; ++i) {
188 | 		const time = date.getTime() / 1000;
189 | 		const value = samplePoint(i);
190 | 		if (ohlc) {
191 | 			const randomRanges = [
192 | 				-1 * Math.random(),
193 | 				Math.random(),
194 | 				Math.random(),
195 | 			].map(j => j * 10);
196 | 			const sign = Math.sin(Math.random() - 0.5);
197 | 			res.push({
198 | 				time,
199 | 				low: value + randomRanges[0],
200 | 				high: value + randomRanges[1],
201 | 				open: value + sign * randomRanges[2],
202 | 				close: samplePoint(i + 1),
203 | 			});
204 | 		} else {
205 | 			res.push({
206 | 				time,
207 | 				value,
208 | 			});
209 | 		}
210 | 
211 | 		date.setUTCDate(date.getUTCDate() + 1);
212 | 	}
213 | 
214 | 	return res;
215 | }
216 | 
217 | function randomShade() {
218 | 	return Math.round(Math.random() * 255);
219 | }
220 | 
221 | function randomColor(alpha = 1) {
222 | 	return `rgba(${randomShade()}, ${randomShade()}, ${randomShade()}, ${alpha})`;
223 | }
224 | 
225 | const colorsTypeMap = {
226 | 	area: [
227 | 		['topColor', 0.4],
228 | 		['bottomColor', 0],
229 | 		['lineColor', 1],
230 | 	],
231 | 	bar: [
232 | 		['upColor', 1],
233 | 		['downColor', 1],
234 | 	],
235 | 	baseline: [
236 | 		['topFillColor1', 0.28],
237 | 		['topFillColor2', 0.05],
238 | 		['topLineColor', 1],
239 | 		['bottomFillColor1', 0.28],
240 | 		['bottomFillColor2', 0.05],
241 | 		['bottomLineColor', 1],
242 | 	],
243 | 	candlestick: [
244 | 		['upColor', 1],
245 | 		['downColor', 1],
246 | 		['borderUpColor', 1],
247 | 		['borderDownColor', 1],
248 | 		['wickUpColor', 1],
249 | 		['wickDownColor', 1],
250 | 	],
251 | 	histogram: [['color', 1]],
252 | 	line: [['color', 1]],
253 | };
254 | 
255 | const checkPageTheme = () =>
256 | 	document.documentElement.getAttribute('data-theme') === 'dark';
257 | 
258 | window.__VUE_PROD_DEVTOOLS__ = false; // ¯\_(ツ)_/¯ required for a production build of the documentation site
259 | const VueExample = defineCustomElement({
260 | 	components: {
261 | 		LWChart,
262 | 	},
263 | 	data: () => ({
264 | 		chartOptions: {
265 | 			layout: {
266 | 				background: {
267 | 					color: 'transparent',
268 | 					type: ColorType.Solid,
269 | 				},
270 | 			},
271 | 		},
272 | 		dataset: generateSampleData(false),
273 | 		seriesOptions: {},
274 | 		chartType: 'area',
275 | 	}),
276 | 	template: `
277 |         <div class="chart-container">
278 |           <LWChart
279 |             :type="chartType"
280 |             :data="dataset"
281 |             :autosize="true"
282 |             :chart-options="chartOptions"
283 |             :series-options="seriesOptions"
284 |             ref="lwChart"
285 |           />
286 |         </div>
287 |         <button type="button" @click="changeColors">Set Random Colors</button>
288 |         <button type="button" @click="changeType">Change Chart Type</button>
289 |         <button type="button" @click="changeData">Change Data</button>
290 |         `,
291 | 	styles: [
292 | 		`
293 |       button {
294 |         border-radius: 8px;
295 |         border: 1px solid transparent;
296 |         padding: 0.5em 1em;
297 |         font-size: 1em;
298 |         font-weight: 500;
299 |         font-family: inherit;
300 |         background-color: var(--hero-button-background-color-active, #e9e9e9);
301 |         color: var(--hero-button-text-color, #e9e9e9);
302 |         cursor: pointer;
303 |         transition: border-color 0.25s;
304 |         margin-left: 0.5em;
305 |       }
306 |       button:hover {
307 |         border-color: #3179F5;
308 |         background-color: var(--hero-button-background-color-hover);
309 |         color: var(--hero-button-text-color-hover-active);
310 |       }
311 |       button:focus,
312 |       button:focus-visible {
313 |         outline: 4px auto -webkit-focus-ring-color;
314 |       }
315 | 
316 |       .chart-container {
317 |         height: var(--lwchart-height, 300px);
318 |       }
319 | 
320 |       .lw-chart {
321 |         height: 100%;
322 |       }
323 |     `,
324 | 	],
325 | 	mounted() {
326 | 		this.changeChartTheme(checkPageTheme());
327 | 
328 | 		if (window.MutationObserver) {
329 | 			const callback = _ => {
330 | 				this.changeChartTheme(checkPageTheme());
331 | 			};
332 | 			this.observer = new window.MutationObserver(callback);
333 | 			this.observer.observe(document.documentElement, { attributes: true });
334 | 		}
335 | 	},
336 | 	unmounted() {
337 | 		if (this.observer) {
338 | 			this.observer.disconnect();
339 | 		}
340 | 	},
341 | 	methods: {
342 | 		changeColors() {
343 | 			const options = {};
344 | 			const colorsToSet = colorsTypeMap[this.chartType];
345 | 			colorsToSet.forEach(c => {
346 | 				options[c[0]] = randomColor(c[1]);
347 | 			});
348 | 			this.seriesOptions = options;
349 | 		},
350 | 		changeData() {
351 | 			const candlestickTypeData = ['candlestick', 'bar'].includes(
352 | 				this.chartType
353 | 			);
354 | 			const newData = generateSampleData(candlestickTypeData);
355 | 			this.dataset = newData;
356 | 			if (this.chartType === 'baseline') {
357 | 				const average =
358 | 					newData.reduce((s, c) => s + c.value, 0) / newData.length;
359 | 				this.seriesOptions = {
360 | 					baseValue: { type: 'price', price: average },
361 | 				};
362 | 			}
363 | 		},
364 | 		changeType() {
365 | 			const types = [
366 | 				'line',
367 | 				'area',
368 | 				'baseline',
369 | 				'histogram',
370 | 				'candlestick',
371 | 				'bar',
372 | 			].filter(t => t !== this.chartType);
373 | 			const randIndex = Math.round(Math.random() * (types.length - 1));
374 | 			this.chartType = types[randIndex];
375 | 			this.changeData();
376 | 
377 | 			// call a method on the component.
378 | 			this.$refs.lwChart.fitContent();
379 | 		},
380 | 		changeChartTheme(isDark) {
381 | 			const theme = isDark ? themeColors.DARK : themeColors.LIGHT;
382 | 			const gridColor = isDark ? '#424F53' : '#D6DCDE';
383 | 			this.chartOptions = {
384 | 				layout: {
385 | 					textColor: theme.CHART_TEXT_COLOR,
386 | 					background: {
387 | 						color: theme.CHART_BACKGROUND_COLOR,
388 | 					},
389 | 				},
390 | 				grid: {
391 | 					vertLines: {
392 | 						color: gridColor,
393 | 					},
394 | 					horzLines: {
395 | 						color: gridColor,
396 | 					},
397 | 				},
398 | 			};
399 | 		},
400 | 	},
401 | });
402 | 
403 | window.customElements.define('vue-example', VueExample);
404 | 


--------------------------------------------------------------------------------
/website/tutorials/webcomponents/01-custom-element.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | title: Web Components - Custom Element
  3 | description:
  4 |   A simple example of how to use Lightweight Charts™ within the Web component
  5 |   custom element.
  6 | pagination_prev: null
  7 | pagination_next: null
  8 | keywords:
  9 |   - web component
 10 |   - custom element
 11 |   - example
 12 | ---
 13 | 
 14 | # Web Components - Custom Element
 15 | 
 16 | :::info
 17 | 
 18 | The following describes a relatively simple example that only allows for a
 19 | single [series](/docs/series-types) to be rendered. This example can be used as
 20 | a starting point, and could be tweaked further using our extensive
 21 | [API](/docs/api).
 22 | 
 23 | :::
 24 | 
 25 | This guide will focus on the key concepts required to get Lightweight Charts™
 26 | running within a Vanilla JS web component (using
 27 | [custom elements](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements)).
 28 | Please note this guide is not intended as a complete step-by-step tutorial. The
 29 | example web component custom element can be found at the
 30 | [bottom](#complete-sample-code) of this guide.
 31 | 
 32 | If you are new to Web Components then please have a look at the following
 33 | resources before proceeding further with this example.
 34 | 
 35 | - [MDN: Using Custom Elements](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements)
 36 | - [Custom Elements Best Practices](https://web.dev/custom-elements-best-practices/)
 37 | - [Open Web Components](https://open-wc.org)
 38 | 
 39 | ## About the example custom element
 40 | 
 41 | The example Web Components custom element has the following features.
 42 | 
 43 | The ability to:
 44 | 
 45 | - specify the series type via a component attribute,
 46 | - specify the series data via a component property,
 47 | - control the chart, series, time scale, and price scale options via properties,
 48 | - enable automatic resizing of the chart when the browser is resized.
 49 | 
 50 | The example may not fit your requirements completely. Creating a general-purpose
 51 | declarative wrapper for Lightweight Charts™ imperative API is a challenge, but
 52 | hopefully, you can adapt this example to your use case.
 53 | 
 54 | ### Component showcase
 55 | 
 56 | Presented below is the finished wrapper custom element which is discussed
 57 | throughout this guide. The interactive buttons beneath the chart are showcasing
 58 | how to interact with the component and that code is provided below as well
 59 | (within the example app custom element).
 60 | 
 61 | import BrowserOnly from '@docusaurus/BrowserOnly';
 62 | 
 63 | <BrowserOnly fallback={<div>Loading...</div>}>
 64 |     {() => {
 65 |         require('./assets/wc-example.js');
 66 |         return <lightweight-chart-example></lightweight-chart-example>;
 67 |     }}
 68 | </BrowserOnly>
 69 | 
 70 | ## Creating the chart
 71 | 
 72 | Web Components are a suite of different technologies which allow you to
 73 | encapsulate functionality within custom elements.
 74 | [Custom elements](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements)
 75 | make use of the standard web languages `html`, `css`, and `js` which means that
 76 | there aren't many specific changes, or extra knowledge, required to get
 77 | Lightweight Charts™ working within a custom element.
 78 | 
 79 | The process of creating a chart is essentially the same as when using the
 80 | library normally, except that we are encapsulating all the `html`, `css`, and
 81 | `js` code specific to the chart within our custom element.
 82 | 
 83 | Starting with a simple boilerplate custom element, as shown below:
 84 | 
 85 | ```js
 86 | (function() {
 87 |     class LightweightChartWC extends HTMLElement {
 88 |         connectedCallback() {
 89 |             this.attachShadow({ mode: 'open' });
 90 |         }
 91 | 
 92 |         disconnectedCallback() {}
 93 |     }
 94 | 
 95 |     // Register our custom element with a specific tag name.
 96 |     window.customElements.define('lightweight-chart', LightweightChartWC);
 97 | })();
 98 | ```
 99 | 
100 | The first step is to define the `html` for the custom element. For Lightweight
101 | Charts, all we need to do is create a `div` element to act as our container
102 | element. You can create the html by cloning a `template` (as seen in our usage
103 | example below) or by imperatively using the DOM JS api as shown below:
104 | 
105 | ```js
106 | // hide-start
107 | class LightweightChartWC extends HTMLElement {
108 |     // ...
109 |     // hide-end
110 |     // Within the class definition
111 |     connectedCallback() {
112 |         // Create the div container for the chart
113 |         const container = document.createElement('div');
114 |         container.setAttribute('class', 'chart-container');
115 | 
116 |         this.shadowRoot.append(container);
117 |     }
118 |     // hide-line
119 | }
120 | ```
121 | 
122 | Next we will want to define some basic styles to ensure that the container
123 | element fills the available space and that the element can be hidden using the
124 | `hidden` attribute.
125 | 
126 | ```js
127 | // Outside of the Class definition
128 | const elementStyles = `
129 |     :host {
130 |         display: block;
131 |     }
132 |     :host[hidden] {
133 |         display: none;
134 |     }
135 |     .chart-container {
136 |         height: 100%;
137 |         width: 100%;
138 |     }
139 | `;
140 | 
141 | // ...
142 | 
143 | // hide-start
144 | class LightweightChartWC extends HTMLElement {
145 |     // ...
146 |     // hide-end
147 |     // Within the class definition
148 |     connectedCallback() {
149 |         // highlight-fade-start
150 |         // Create the div container for the chart
151 |         const container = document.createElement('div');
152 |         container.setAttribute('class', 'chart-container');
153 |         // highlight-fade-end
154 |         // create the stylesheet for the custom element
155 |         const style = document.createElement('style');
156 |         style.textContent = elementStyles;
157 |         this.shadowRoot.append(style, container);
158 |     }
159 |     // hide-line
160 | }
161 | ```
162 | 
163 | Finally, we can now create the chart using Lightweight Charts™. Depending on your
164 | build process, you may either need to import Lightweight Charts™, or access it
165 | from the global scope (if loaded as a standalone script). To create the chart,
166 | we call the [`createChart`](/docs/api/functions/createChart) constructor function, passing
167 | our container element as the first argument. The returned variable will be a
168 | [`IChartApi`](/docs/api/interfaces/IChartApi) instance which we can use as shown
169 | in the API documentation. The IChartApi instance provides all the required
170 | functionality to create series, assign data, and more. See our
171 | [Getting started](/docs) guide for a quick example.
172 | 
173 | ```js
174 | // hide-start
175 | class LightweightChartWC extends HTMLElement {
176 |     // ...
177 |     // hide-end
178 |     connectedCallback() {
179 |         // highlight-fade-start
180 |         // Create the div container for the chart
181 |         const container = document.createElement('div');
182 |         container.setAttribute('class', 'chart-container');
183 | 
184 |         // create the stylesheet for the custom element
185 |         const style = document.createElement('style');
186 |         style.textContent = elementStyles;
187 |         this.shadowRoot.append(style, container);
188 |         // highlight-fade-end
189 | 
190 |         // Create the Lightweight Chart
191 |         this.chart = createChart(container);
192 |     }
193 |     // hide-line
194 | }
195 | ```
196 | 
197 | ## Attributes and properties
198 | 
199 | Whilst we could encapsulate everything required to create a chart within the
200 | custom element, generally we wish to allow further customisation of the chart to
201 | the consumers of the custom element. Attributes and properties are a great way
202 | to provide this 'API' to the consumer.
203 | 
204 | As a general rule of thumb, it is better to use attributes for options which are
205 | defined using simple values (number, string, boolean), and properties for rich
206 | data types.
207 | 
208 | In our example, we will be using attributes for the series type option (type)
209 | and the autosize flag which enables automatic resizing of the chart when the
210 | window is resized. We will be using properties to provide the interfaces for
211 | setting the series data, and options for the chart. Additionally, the IChartApi
212 | instance will be accessable via the `chart` property such that the consumer has
213 | full access to the entire API provided by Lightweight Charts™.
214 | 
215 | ### Attributes
216 | 
217 | Attributes for the custom element can be set directly on the custom element
218 | (within the html), or via javascript as seen for the properties in the next
219 | section.
220 | 
221 | ```html
222 | <lightweight-chart autosize type="area"></lightweight-chart>
223 | ```
224 | 
225 | Attributes can be set and read from within the custom element's definition as
226 | follows:
227 | 
228 | ```js
229 | // read `type` attribute
230 | const type = this.getAttribute('type');
231 | 
232 | // set `type` attribute
233 | this.setAttribute('type', 'line');
234 | ```
235 | 
236 | It is recommended that attributes be mirrored as properties on the custom
237 | element (and reflected such that any changes appear on the html as well). This
238 | can be achieved as follows:
239 | 
240 | ```js
241 | // hide-start
242 | class LightweightChartWC extends HTMLElement {
243 |     // ...
244 |     // hide-end
245 |     // Within the class definition
246 |     set type(value) {
247 |         this.setAttribute('type', value || 'line');
248 |     }
249 | 
250 |     get type() {
251 |         return this.getAttribute('type') || 'line';
252 |     }
253 |     // hide-line
254 | }
255 | ```
256 | 
257 | We can observe any changes to an attribute by defining the static
258 | `observedAttributes` getter on the custom element and the
259 | `attributeChangedCallback` method on the class definition.
260 | 
261 | ```js
262 | class LightweightChartWC extends HTMLElement {
263 |     // Attributes to observe. When changes occur, `attributeChangedCallback` is called.
264 |     static get observedAttributes() {
265 |         return ['type', 'autosize'];
266 |     }
267 | 
268 |     /**
269 |      * `attributeChangedCallback()` is called when any of the attributes in the
270 |      * `observedAttributes` array are changed.
271 |      */
272 |     attributeChangedCallback(name, _oldValue, newValue) {
273 |         if (!this.chart) {
274 |             return;
275 |         }
276 |         const hasValue = newValue !== null;
277 |         switch (name) {
278 |         case 'type':
279 |             // handle the changed attribute
280 |             break;
281 |         case 'autosize':
282 |             // handle the changed attribute
283 |             break;
284 |         }
285 |     }
286 | }
287 | ```
288 | 
289 | ### Properties
290 | 
291 | Properties for the custom element are read and set through javascript on a
292 | reference to a custom element's instance. This instance can be created using
293 | standard DOM methods such as `querySelector`.
294 | 
295 | ```js
296 | // Get a reference to an instance of the custom element on the page
297 | const myChartElement = document.querySelector('lightweight-chart');
298 | 
299 | // read the data property
300 | const currentData = myChartElement.data;
301 | 
302 | // set the seriesOptions property
303 | myChartElement.seriesOptions = {
304 |     color: 'blue',
305 | };
306 | ```
307 | 
308 | We can define setters and getters for the properties if we need more control
309 | over the property instead of it being just a value.
310 | 
311 | ```js
312 | // hide-start
313 | class LightweightChartWC extends HTMLElement {
314 |     // ...
315 |     // hide-end
316 |     // Within the class definition
317 |     set options(value) {
318 |         if (!this.chart) {
319 |             return;
320 |         }
321 |         this.chart.applyOptions(value);
322 |     }
323 | 
324 |     get options() {
325 |         if (!this.chart) {
326 |             return null;
327 |         }
328 |         return this.chart.options();
329 |     }
330 |     // hide-line
331 | }
332 | ```
333 | 
334 | As mentioned earlier, it is recommended that any API which accepts complex (or
335 | rich data) beyond a simple string, number, or boolean value should be property.
336 | However, since properties can only be set via javascript there may be cases
337 | where it would be preferable to define these values within the html markup. We
338 | can provide an attribute interface for these properties which can be used to
339 | define the initial values, then remove those attributes from the markup and
340 | ignore any further changes to those attributes.
341 | 
342 | ```js
343 | // hide-line
344 | class LightweightChartWC extends HTMLElement {
345 |     /**
346 |      * Any data properties which are provided as JSON string values
347 |      * when the component is attached to the DOM will be used as the
348 |      * initial values for those properties.
349 |      *
350 |      * Note: once the component is attached, then any changes to these
351 |      * attributes will be ignored (not observed), and should rather be
352 |      * set using the property directly.
353 |      */
354 |     _tryLoadInitialProperty(name) {
355 |         if (this.hasAttribute(name)) {
356 |             const valueString = this.getAttribute(name);
357 |             let value;
358 |             try {
359 |                 value = JSON.parse(valueString);
360 |             } catch (error) {
361 |                 console.error(
362 |                     `Unable to read attribute ${name}'s value during initialisation.`
363 |                 );
364 |                 return;
365 |             }
366 |             // change kebab case attribute name to camel case.
367 |             const propertyName = name
368 |                 .split('-')
369 |                 .map((text, index) => {
370 |                     if (index < 1) {
371 |                         return text;
372 |                     }
373 |                     return `${text.charAt(0).toUpperCase()}${text.slice(1)}`;
374 |                 })
375 |                 .join('');
376 |             this[propertyName] = value;
377 |             this.removeAttribute(name);
378 |         }
379 |     }
380 | 
381 |     connectedCallback() {
382 |         // ...
383 | 
384 |         // Read initial values using attributes and then clear the attributes
385 |         // since we don't want to 'reflect' data properties onto the elements
386 |         // attributes.
387 |         const richDataProperties = [
388 |             'options',
389 |             'series-options',
390 |             'pricescale-options',
391 |             'timescale-options',
392 |         ];
393 |         richDataProperties.forEach(propertyName => {
394 |             this._tryLoadInitialProperty(propertyName);
395 |         });
396 |     }
397 |     // hide-line
398 | }
399 | ```
400 | 
401 | These attributes can be used to define the initial values for the properties as
402 | follows (using JSON notation):
403 | 
404 | ```html
405 | <lightweight-chart
406 |     data='[{"time": "2022-09-14", "value": 123.45},{"time": "2022-09-15", "value": 123.45}]'
407 |     series-options='{"color":"blue"}'
408 | ></lightweight-chart>
409 | ```
410 | 
411 | ## Accessing the chart instance or additional methods
412 | 
413 | The IChartApi instance will be accessible via the `chart` property on the custom
414 | element. This can be used by the consumer of the custom element to fully control
415 | the chart within the element.
416 | 
417 | ```js
418 | // Get a reference to an instance of the custom element on the page
419 | const myChartElement = document.querySelector('lightweight-chart');
420 | 
421 | const chartApi = myChartElement.chart;
422 | 
423 | // For example, call the `fitContent` method on the time scale
424 | chartApi.timeScale().fitContent();
425 | ```
426 | 
427 | ## Using a Custom Element
428 | 
429 | Custom elements can be used just like any other normal html element after the
430 | custom element has been defined and registered. The example custom element will
431 | define and register itself (using
432 | `window.customElements.define('lightweight-chart', LightweightChartWC);`) when
433 | the script is loaded and executed, so all you need to do is include the script
434 | tag on the page.
435 | 
436 | Depending on your build step for your page, you may either need to import
437 | Lightweight Charts™ via an import statement, or access the library via the global
438 | variable defined when using the standalone script version.
439 | 
440 | ```js
441 | // if using esm version (installed via npm):
442 | // import { createChart } from 'lightweight-charts';
443 | 
444 | // If using standalone version (loaded via a script tag):
445 | const { createChart } = LightweightCharts;
446 | ```
447 | 
448 | Similarily, the custom element can either be loaded via an 'side-effect' import
449 | statement:
450 | 
451 | ```js
452 | // side-effect import statement (use within a module js file)
453 | import './lw-chart.js';
454 | ```
455 | 
456 |  or via a script tag:
457 | 
458 |  ```html
459 | <script src="lw-chart.js" defer></script>
460 | ```
461 | 
462 | Once the custom element script has been loaded and executed then you can use the
463 | custom element anywhere that you can use normal html, including within other
464 | frameworks like React, Vue, and Angular. See
465 | [Custom Elements Everywhere](https://custom-elements-everywhere.com) for more
466 | information.
467 | 
468 | ### Standalone script example html file
469 | 
470 | If you are loading the Lightweight Charts™ library via the standalone script
471 | version then you can also load the custom element via a script tag (see above
472 | section for more info) and construct your html page as follows:
473 | 
474 | ```html
475 | <!DOCTYPE html>
476 | <html>
477 |     <head>
478 |         <meta charset="UTF-8" />
479 |         <meta
480 |             name="viewport"
481 |             content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0"
482 |         />
483 |         <title>Web component Example</title>
484 |         <script
485 |             type="text/javascript"
486 |             src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.development.js"
487 |         ></script>
488 |         <style>
489 |             #my-chart {
490 |                 height: 100vh;
491 |                 width: 100vw;
492 |             }
493 |         </style>
494 |     </head>
495 | 
496 |     <body style="padding: 0; margin: 0">
497 |         <lightweight-chart
498 |             id="my-chart"
499 |             autosize
500 |             type="line"
501 |             series-options='{"color": "red"}'
502 |             data='[{ "time": "2018-10-19", "value": 52.89 },{ "time": "2018-10-22", "value": 51.65 }]'
503 |         ></lightweight-chart>
504 | 
505 |         <script src="lw-chart.js" defer></script>
506 |     </body>
507 | </html>
508 | ```
509 | 
510 | ## Complete Sample Code
511 | 
512 | Presented below is the complete custom element source code for the Web
513 | component. We have also provided a sample custom element component which
514 | showcases how to make use of these components within a typical html page.
515 | 
516 | ### Wrapper Custom Element
517 | 
518 | The following code block contains the source code for the wrapper custom
519 | element.
520 | 
521 | <p>
522 |     <a
523 |         href={require('!!file-loader!./assets/lw-chart.js').default}
524 |         download="lw-chart.js"
525 |         target="\_blank"
526 |     >
527 |         Download file
528 |     </a>
529 | </p>
530 | 
531 | import CodeBlock from '@theme/CodeBlock';
532 | import InstantDetails from '@site/src/components/InstantDetails';
533 | import wrapperCode from '!!raw-loader!./assets/lw-chart.js';
534 | 
535 | <InstantDetails>
536 |     <summary>Click here to reveal the code.</summary>
537 |     <CodeBlock className="language-js">{wrapperCode}</CodeBlock>
538 | </InstantDetails>
539 | 
540 | ### Example Usage Custom Element
541 | 
542 | The following code block contains the source code for the custom element
543 | showcasing how to use the above custom element.
544 | 
545 | <p>
546 |     <a
547 |         href={require('!!file-loader!./assets/wc-example.js').default}
548 |         download="wc-example.js"
549 |         target="\_blank"
550 |     >
551 |         Download file
552 |     </a>
553 | </p>
554 | 
555 | import exampleCode from '!!raw-loader!./assets/wc-example.js';
556 | 
557 | <InstantDetails>
558 |     <summary>Click here to reveal the code.</summary>
559 |     <CodeBlock className="language-js">{exampleCode}</CodeBlock>
560 | </InstantDetails>
561 | 


--------------------------------------------------------------------------------
/website/tutorials/webcomponents/_category_.yml:
--------------------------------------------------------------------------------
1 | label: "Web Components"
2 | 


--------------------------------------------------------------------------------
/website/tutorials/webcomponents/assets/.eslintrc.js:
--------------------------------------------------------------------------------
 1 | module.exports = {
 2 | 	globals: {
 3 | 		document: false,
 4 | 		window: false,
 5 | 		HTMLElement: false,
 6 | 	},
 7 | 	rules: {
 8 | 		'no-console': 'off',
 9 | 		'no-prototype-builtins': 'off',
10 | 	},
11 | };
12 | 


--------------------------------------------------------------------------------
/website/tutorials/webcomponents/assets/lw-chart.js:
--------------------------------------------------------------------------------
  1 | // if using esm version (installed via npm):
  2 | import { createChart, LineSeries, AreaSeries, CandlestickSeries, BaselineSeries, HistogramSeries, BarSeries } from 'lightweight-charts';
  3 | 
  4 | // If using standalone version (loaded via a script tag):
  5 | // const { createChart } = LightweightCharts;
  6 | 
  7 | (function() {
  8 | 	// Styles for the custom element
  9 | 	const elementStyles = `
 10 |                     :host {
 11 |                         display: block;
 12 |                     }
 13 |                     :host[hidden] {
 14 |                         display: none;
 15 |                     }
 16 |                     .chart-container {
 17 |                         height: 100%;
 18 |                         width: 100%;
 19 |                     }
 20 |                 `;
 21 | 
 22 | 	// Class definition for the custom element
 23 | 	class LightweightChartWC extends HTMLElement {
 24 | 		// Attributes to observe. When changes occur, `attributeChangedCallback` is called.
 25 | 		static get observedAttributes() {
 26 | 			return ['type', 'autosize'];
 27 | 		}
 28 | 
 29 | 		static getChartSeriesDefinition(type) {
 30 | 			switch (type) {
 31 | 				case 'line':
 32 | 					return LineSeries;
 33 | 				case 'area':
 34 | 					return AreaSeries;
 35 | 				case 'candlestick':
 36 | 					return CandlestickSeries;
 37 | 				case 'baseline':
 38 | 					return BaselineSeries;
 39 | 				case 'bar':
 40 | 					return BarSeries;
 41 | 				case 'histogram':
 42 | 					return HistogramSeries;
 43 | 			}
 44 | 			throw new Error(`${type} is an unsupported series type`);
 45 | 		}
 46 | 
 47 | 		constructor() {
 48 | 			super();
 49 | 			this.chart = undefined;
 50 | 			this.series = undefined;
 51 | 			this.__data = [];
 52 | 			this._resizeEventHandler = () => this._resizeHandler();
 53 | 		}
 54 | 
 55 | 		/**
 56 | 		 * `connectedCallback()` fires when the element is inserted into the DOM.
 57 | 		 */
 58 | 		connectedCallback() {
 59 | 			this.attachShadow({ mode: 'open' });
 60 | 
 61 | 			/**
 62 | 			 * Attributes you may want to set, but should only change if
 63 | 			 * not already specified.
 64 | 			 */
 65 | 			// if (!this.hasAttribute('tabindex'))
 66 | 			// this.setAttribute('tabindex', -1);
 67 | 
 68 | 			// A user may set a property on an _instance_ of an element,
 69 | 			// before its prototype has been connected to this class.
 70 | 			// The `_upgradeProperty()` method will check for any instance properties
 71 | 			// and run them through the proper class setters.
 72 | 			this._upgradeProperty('type');
 73 | 			this._upgradeProperty('autosize');
 74 | 
 75 | 			// We load the data attribute before creating the chart
 76 | 			// so the `setTypeAndData` method can have an initial value.
 77 | 			this._tryLoadInitialProperty('data');
 78 | 
 79 | 			// Create the div container for the chart
 80 | 			const container = document.createElement('div');
 81 | 			container.setAttribute('class', 'chart-container');
 82 | 			// create the stylesheet for the custom element
 83 | 			const style = document.createElement('style');
 84 | 			style.textContent = elementStyles;
 85 | 			this.shadowRoot.append(style, container);
 86 | 
 87 | 			// Create the Lightweight Chart
 88 | 			this.chart = createChart(container);
 89 | 			this.setTypeAndData();
 90 | 
 91 | 			// Read initial values using attributes and then clear the attributes
 92 | 			// since we don't want to 'reflect' data properties onto the elements
 93 | 			// attributes.
 94 | 			const richDataProperties = [
 95 | 				'options',
 96 | 				'series-options',
 97 | 				'pricescale-options',
 98 | 				'timescale-options',
 99 | 			];
100 | 			richDataProperties.forEach(propertyName => {
101 | 				this._tryLoadInitialProperty(propertyName);
102 | 			});
103 | 
104 | 			if (this.autosize) {
105 | 				window.addEventListener('resize', this._resizeEventHandler);
106 | 			}
107 | 		}
108 | 
109 | 		/**
110 | 		 * Any data properties which are provided as JSON string values
111 | 		 * when the component is attached to the DOM will be used as the
112 | 		 * initial values for those properties.
113 | 		 *
114 | 		 * Note: once the component is attached, then any changes to these
115 | 		 * attributes will be ignored (not observed), and should rather be
116 | 		 * set using the property directly.
117 | 		 */
118 | 		_tryLoadInitialProperty(name) {
119 | 			if (this.hasAttribute(name)) {
120 | 				const valueString = this.getAttribute(name);
121 | 				let value;
122 | 				try {
123 | 					value = JSON.parse(valueString);
124 | 				} catch (error) {
125 | 					console.error(
126 | 						`Unable to read attribute ${name}'s value during initialisation.`
127 | 					);
128 | 					return;
129 | 				}
130 | 				// change kebab case attribute name to camel case.
131 | 				const propertyName = name
132 | 					.split('-')
133 | 					.map((text, index) => {
134 | 						if (index < 1) {return text;}
135 | 						return `${text.charAt(0).toUpperCase()}${text.slice(1)}`;
136 | 					})
137 | 					.join('');
138 | 				this[propertyName] = value;
139 | 				this.removeAttribute(name);
140 | 			}
141 | 		}
142 | 
143 | 		// Create a chart series (according to the 'type' attribute) and set it's data.
144 | 		setTypeAndData() {
145 | 			if (this.series && this.chart) {
146 | 				this.chart.removeSeries(this.series);
147 | 			}
148 | 			this.series =
149 | 				this.chart.addSeries(LightweightChartWC.getChartSeriesDefinition(this.type));
150 | 			this.series.setData(this.data);
151 | 		}
152 | 
153 | 		_upgradeProperty(prop) {
154 | 			if (this.hasOwnProperty(prop)) {
155 | 				const value = this[prop];
156 | 				delete this[prop];
157 | 				this[prop] = value;
158 | 			}
159 | 		}
160 | 
161 | 		/**
162 | 		 * `disconnectedCallback()` fires when the element is removed from the DOM.
163 | 		 * It's a good place to do clean up work like releasing references and
164 | 		 * removing event listeners.
165 | 		 */
166 | 		disconnectedCallback() {
167 | 			if (this.chart) {
168 | 				this.chart.remove();
169 | 				this.chart = null;
170 | 			}
171 | 			window.removeEventListener('resize', this._resizeEventHandler);
172 | 		}
173 | 
174 | 		/**
175 | 		 * Reflected Properties
176 | 		 *
177 | 		 * These Properties and their corresponding attributes should mirror one another.
178 | 		 */
179 | 		set type(value) {
180 | 			this.setAttribute('type', value || 'line');
181 | 		}
182 | 
183 | 		get type() {
184 | 			return this.getAttribute('type') || 'line';
185 | 		}
186 | 
187 | 		set autosize(value) {
188 | 			const autosize = Boolean(value);
189 | 			if (autosize) {this.setAttribute('autosize', '');} else {this.removeAttribute('autosize');}
190 | 		}
191 | 
192 | 		get autosize() {
193 | 			return this.hasAttribute('autosize');
194 | 		}
195 | 
196 | 		/**
197 | 		 * Rich Data Properties
198 | 		 *
199 | 		 * These Properties are not reflected to a corresponding attribute.
200 | 		 */
201 | 		set data(value) {
202 | 			let newData = value;
203 | 			if (typeof newData !== 'object' || !Array.isArray(newData)) {
204 | 				newData = [];
205 | 				console.warn('Lightweight Charts: Data should be an array');
206 | 			}
207 | 			this.__data = newData;
208 | 			if (this.series) {
209 | 				this.series.setData(this.__data);
210 | 			}
211 | 		}
212 | 
213 | 		get data() {
214 | 			return this.__data;
215 | 		}
216 | 
217 | 		set options(value) {
218 | 			if (!this.chart) {return;}
219 | 			this.chart.applyOptions(value);
220 | 		}
221 | 
222 | 		get options() {
223 | 			if (!this.chart) {return null;}
224 | 			return this.chart.options();
225 | 		}
226 | 
227 | 		set seriesOptions(value) {
228 | 			if (!this.series) {return;}
229 | 			this.series.applyOptions(value);
230 | 		}
231 | 
232 | 		get seriesOptions() {
233 | 			if (!this.series) {return null;}
234 | 			return this.series.options();
235 | 		}
236 | 
237 | 		set priceScaleOptions(value) {
238 | 			if (!this.chart) {return;}
239 | 			this.chart.priceScale().applyOptions(value);
240 | 		}
241 | 
242 | 		get priceScaleOptions() {
243 | 			if (!this.series) {return null;}
244 | 			return this.chart.priceScale().options();
245 | 		}
246 | 
247 | 		set timeScaleOptions(value) {
248 | 			if (!this.chart) {return;}
249 | 			this.chart.timeScale().applyOptions(value);
250 | 		}
251 | 
252 | 		get timeScaleOptions() {
253 | 			if (!this.series) {return null;}
254 | 			return this.chart.timeScale().options();
255 | 		}
256 | 
257 | 		/**
258 | 		 * `attributeChangedCallback()` is called when any of the attributes in the
259 | 		 * `observedAttributes` array are changed.
260 | 		 */
261 | 		attributeChangedCallback(name, _oldValue, newValue) {
262 | 			if (!this.chart) {return;}
263 | 			const hasValue = newValue !== null;
264 | 			switch (name) {
265 | 				case 'type':
266 | 					this.data = [];
267 | 					this.setTypeAndData();
268 | 					break;
269 | 				case 'autosize':
270 | 					if (hasValue) {
271 | 						window.addEventListener('resize', () => this._resizeEventHandler);
272 | 						// call once when added to an existing element
273 | 						this._resizeEventHandler();
274 | 					} else {
275 | 						window.removeEventListener('resize', this._resizeEventHandler);
276 | 					}
277 | 					break;
278 | 			}
279 | 		}
280 | 
281 | 		_resizeHandler() {
282 | 			const container = this.shadowRoot.querySelector('div.chart-container');
283 | 			if (!this.chart || !container) {return;}
284 | 			const dimensions = container.getBoundingClientRect();
285 | 			this.chart.resize(dimensions.width, dimensions.height);
286 | 		}
287 | 	}
288 | 
289 | 	window.customElements.define('lightweight-chart', LightweightChartWC);
290 | })();
291 | 


--------------------------------------------------------------------------------
/website/tutorials/webcomponents/assets/wc-example.js:
--------------------------------------------------------------------------------
  1 | import './lw-chart.js';
  2 | import { themeColors } from '../../../theme-colors';
  3 | 
  4 | (function() {
  5 | 	const template = document.createElement('template');
  6 | 	template.innerHTML = `
  7 |     <style>
  8 |     :host {
  9 |         display: block;
 10 |     }
 11 |     :host[hidden] {
 12 |         display: none;
 13 |     }
 14 |     #example {
 15 |         display: flex;
 16 |         flex-direction: column;
 17 |         height: 100%;
 18 |         width: 100%;
 19 |     }
 20 |     #chart {
 21 |         flex-grow: 1;
 22 |     }
 23 |     #buttons {
 24 |         flex-direction: row;
 25 |     }
 26 |     button {
 27 |         border-radius: 8px;
 28 |         border: 1px solid transparent;
 29 |         padding: 0.5em 1em;
 30 |         font-size: 1em;
 31 |         font-weight: 500;
 32 |         font-family: inherit;
 33 |         background-color: var(--hero-button-background-color-active, #e9e9e9);
 34 |         color: var(--hero-button-text-color, #e9e9e9);
 35 |         cursor: pointer;
 36 |         transition: border-color 0.25s;
 37 |         margin-left: 0.5em;
 38 |       }
 39 |       button:hover {
 40 |         border-color: #3179F5;
 41 |         background-color: var(--hero-button-background-color-hover);
 42 |         color: var(--hero-button-text-color-hover-active);
 43 |       }
 44 |       button:focus,
 45 |       button:focus-visible {
 46 |         outline: 4px auto -webkit-focus-ring-color;
 47 |       }
 48 |         
 49 |       #example-chart {
 50 |         height: var(--lwchart-height, 300px);
 51 |       }
 52 |     </style>
 53 |     <div id="example">
 54 |         <div id="example-container">
 55 |             <lightweight-chart id="example-chart"
 56 |                 autosize
 57 |                 type="line"
 58 |             ></lightweight-chart>
 59 |         </div>
 60 |         <div id="buttons">
 61 |             <button id="change-colours-button" type="button">Set Random Colors</button>
 62 |             <button id="change-type-button" type="button">Change Chart Type</button>
 63 |             <button id="change-data-button" type="button">Change Data</button>
 64 |         </div>
 65 |     </div>
 66 |   `;
 67 | 
 68 | 	function generateSampleData(ohlc) {
 69 | 		const randomFactor = 25 + Math.random() * 25;
 70 | 		const samplePoint = i =>
 71 | 			i *
 72 | 				(0.5 +
 73 | 					Math.sin(i / 10) * 0.2 +
 74 | 					Math.sin(i / 20) * 0.4 +
 75 | 					Math.sin(i / randomFactor) * 0.8 +
 76 | 					Math.sin(i / 500) * 0.5) +
 77 | 			200;
 78 | 
 79 | 		const res = [];
 80 | 		const date = new Date(Date.UTC(2018, 0, 1, 0, 0, 0, 0));
 81 | 		const numberOfPoints = ohlc ? 100 : 500;
 82 | 		for (let i = 0; i < numberOfPoints; ++i) {
 83 | 			const time = date.getTime() / 1000;
 84 | 			const value = samplePoint(i);
 85 | 			if (ohlc) {
 86 | 				const randomRanges = [
 87 | 					-1 * Math.random(),
 88 | 					Math.random(),
 89 | 					Math.random(),
 90 | 				].map(j => j * 10);
 91 | 				const sign = Math.sin(Math.random() - 0.5);
 92 | 				res.push({
 93 | 					time,
 94 | 					low: value + randomRanges[0],
 95 | 					high: value + randomRanges[1],
 96 | 					open: value + sign * randomRanges[2],
 97 | 					close: samplePoint(i + 1),
 98 | 				});
 99 | 			} else {
100 | 				res.push({
101 | 					time,
102 | 					value,
103 | 				});
104 | 			}
105 | 
106 | 			date.setUTCDate(date.getUTCDate() + 1);
107 | 		}
108 | 
109 | 		return res;
110 | 	}
111 | 
112 | 	const randomShade = () => Math.round(Math.random() * 255);
113 | 
114 | 	const randomColor = (alpha = 1) =>
115 | 		`rgba(${randomShade()}, ${randomShade()}, ${randomShade()}, ${alpha})`;
116 | 
117 | 	const colorsTypeMap = {
118 | 		area: [
119 | 			['topColor', 0.4],
120 | 			['bottomColor', 0],
121 | 			['lineColor', 1],
122 | 		],
123 | 		bar: [
124 | 			['upColor', 1],
125 | 			['downColor', 1],
126 | 		],
127 | 		baseline: [
128 | 			['topFillColor1', 0.28],
129 | 			['topFillColor2', 0.05],
130 | 			['topLineColor', 1],
131 | 			['bottomFillColor1', 0.28],
132 | 			['bottomFillColor2', 0.05],
133 | 			['bottomLineColor', 1],
134 | 		],
135 | 		candlestick: [
136 | 			['upColor', 1],
137 | 			['downColor', 1],
138 | 			['borderUpColor', 1],
139 | 			['borderDownColor', 1],
140 | 			['wickUpColor', 1],
141 | 			['wickDownColor', 1],
142 | 		],
143 | 		histogram: [['color', 1]],
144 | 		line: [['color', 1]],
145 | 	};
146 | 
147 | 	const checkPageTheme = () =>
148 | 		document.documentElement.getAttribute('data-theme') === 'dark';
149 | 
150 | 	class LightweightChartExampleWC extends HTMLElement {
151 | 		constructor() {
152 | 			super();
153 | 			this.chartElement = undefined;
154 | 		}
155 | 
156 | 		connectedCallback() {
157 | 			this.attachShadow({ mode: 'open' });
158 | 			this.shadowRoot.appendChild(template.content.cloneNode(true));
159 | 
160 | 			this.changeChartTheme(checkPageTheme());
161 | 
162 | 			if (window.MutationObserver) {
163 | 				const callback = _ => {
164 | 					this.changeChartTheme(checkPageTheme());
165 | 				};
166 | 				this.observer = new window.MutationObserver(callback);
167 | 				this.observer.observe(document.documentElement, { attributes: true });
168 | 			}
169 | 
170 | 			this.chartElement = this.shadowRoot.querySelector('#example-chart');
171 | 			this._changeData();
172 | 
173 | 			this.addButtonClickHandlers();
174 | 			this.chartElement.chart.timeScale().fitContent();
175 | 		}
176 | 
177 | 		addButtonClickHandlers() {
178 | 			this.changeColours = () => this._changeColours();
179 | 			this.changeType = () => this._changeType();
180 | 			this.changeData = () => this._changeData();
181 | 			this.shadowRoot
182 | 				.querySelector('#change-colours-button')
183 | 				.addEventListener('click', this.changeColours);
184 | 			this.shadowRoot
185 | 				.querySelector('#change-type-button')
186 | 				.addEventListener('click', this.changeType);
187 | 			this.shadowRoot
188 | 				.querySelector('#change-data-button')
189 | 				.addEventListener('click', this.changeData);
190 | 		}
191 | 
192 | 		removeButtonClickHandlers() {
193 | 			if (this.changeColours) {
194 | 				this.shadowRoot
195 | 					.querySelector('#change-colours-button')
196 | 					.removeEventListener('click', this.changeColours);
197 | 			}
198 | 			if (this.changeType) {
199 | 				this.shadowRoot
200 | 					.querySelector('#change-type-button')
201 | 					.removeEventListener('click', this.changeType);
202 | 			}
203 | 			if (this.changeData) {
204 | 				this.shadowRoot
205 | 					.querySelector('#change-data-button')
206 | 					.removeEventListener('click', this.changeData);
207 | 			}
208 | 		}
209 | 
210 | 		_changeColours() {
211 | 			if (!this.chartElement) {
212 | 				return;
213 | 			}
214 | 			const options = {};
215 | 			const colorsToSet = colorsTypeMap[this.chartElement.type];
216 | 			colorsToSet.forEach(c => {
217 | 				options[c[0]] = randomColor(c[1]);
218 | 			});
219 | 			this.chartElement.seriesOptions = options;
220 | 		}
221 | 
222 | 		_changeData() {
223 | 			if (!this.chartElement) {
224 | 				return;
225 | 			}
226 | 			const candlestickTypeData = ['candlestick', 'bar'].includes(
227 | 				this.chartElement.type
228 | 			);
229 | 			const newData = generateSampleData(candlestickTypeData);
230 | 			this.chartElement.data = newData;
231 | 			if (this.chartElement.type === 'baseline') {
232 | 				const average =
233 | 					newData.reduce((s, c) => s + c.value, 0) / newData.length;
234 | 				this.chartElement.seriesOptions = {
235 | 					baseValue: { type: 'price', price: average },
236 | 				};
237 | 			}
238 | 		}
239 | 
240 | 		_changeType() {
241 | 			if (!this.chartElement) {
242 | 				return;
243 | 			}
244 | 			const types = [
245 | 				'line',
246 | 				'area',
247 | 				'baseline',
248 | 				'histogram',
249 | 				'candlestick',
250 | 				'bar',
251 | 			].filter(t => t !== this.chartElement.type);
252 | 			const randIndex = Math.round(Math.random() * (types.length - 1));
253 | 			this.chartElement.type = types[randIndex];
254 | 			this._changeData();
255 | 
256 | 			// call a method on the component.
257 | 			this.chartElement.chart.timeScale().fitContent();
258 | 		}
259 | 
260 | 		disconnectedCallback() {}
261 | 
262 | 		changeChartTheme(isDark) {
263 | 			if (!this.chartElement) {
264 | 				return;
265 | 			}
266 | 			const theme = isDark ? themeColors.DARK : themeColors.LIGHT;
267 | 			const gridColor = isDark ? '#424F53' : '#D6DCDE';
268 | 			this.chartElement.options = {
269 | 				layout: {
270 | 					textColor: theme.CHART_TEXT_COLOR,
271 | 					background: {
272 | 						color: theme.CHART_BACKGROUND_COLOR,
273 | 					},
274 | 				},
275 | 				grid: {
276 | 					vertLines: {
277 | 						color: gridColor,
278 | 					},
279 | 					horzLines: {
280 | 						color: gridColor,
281 | 					},
282 | 				},
283 | 			};
284 | 		}
285 | 	}
286 | 
287 | 	window.customElements.define(
288 | 		'lightweight-chart-example',
289 | 		LightweightChartExampleWC
290 | 	);
291 | })();
292 | 

