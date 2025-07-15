└── website
    └── versioned_docs
        └── version-5.0
            ├── android.md
            ├── chart-types.mdx
            ├── intro.mdx
            ├── ios.md
            ├── migrations
                ├── _category_.yml
                ├── from-v2-to-v3.md
                ├── from-v3-to-v4.md
                └── from-v4-to-v5.md
            ├── panes.md
            ├── plugins
                ├── .eslintrc.js
                ├── canvas-rendering-target.md
                ├── custom_series.md
                ├── explainer-layers-demo.js
                ├── explainer-sections-demo.js
                ├── intro.md
                ├── pane-primitives.md
                ├── pixel-perfect-rendering
                │   ├── _category_.yml
                │   ├── index.md
                │   └── widths
                │   │   ├── _category_.yml
                │   │   ├── candlestick.md
                │   │   ├── columns.md
                │   │   ├── crosshair.md
                │   │   └── full-bar-width.md
                └── series-primitives.mdx
            ├── price-scale.md
            ├── release-notes.md
            ├── series-types.mdx
            ├── time-scale.md
            └── time-zones.md


/website/versioned_docs/version-5.0/android.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | id: android
  3 | description: You can use Lightweight Charts™ inside an Android application. To use Lightweight Charts™ in that context, you can use our Android wrapper, which will allow you to interact with Lightweight Charts™ library, which will be rendered in a web view.
  4 | keywords:
  5 |     - charts
  6 |     - android
  7 |     - canvas
  8 |     - charting library
  9 |     - charting
 10 |     - html5 charts
 11 |     - financial charting library
 12 | sidebar_position: 8
 13 | ---
 14 | 
 15 | # Android wrapper
 16 | 
 17 | :::note
 18 | You can find the source code of the Lightweight Charts™ Android wrapper in [this repository](https://github.com/tradingview/lightweight-charts-android).
 19 | :::
 20 | 
 21 | :::info
 22 | 
 23 | This wrapper is currently still using `v3.8.0`. This will be updated to `v4.0.0` in the near future.
 24 | 
 25 | :::
 26 | 
 27 | You can use Lightweight Charts™ inside an Android application. To use Lightweight Charts™ in that context, you can use our Android wrapper, which will allow you to interact with Lightweight Charts™ library, which will be rendered in a web view.
 28 | 
 29 | ## Installation
 30 | 
 31 | :::info
 32 | Requires minSdkVersion 21, and installed WebView with support of ES6
 33 | :::
 34 | 
 35 | In `/build.gradle`
 36 | 
 37 | ```groovy
 38 | allprojects {
 39 |     repositories {
 40 |         google()
 41 |         mavenCentral()
 42 |     }
 43 | }
 44 | ```
 45 | 
 46 | In `/gradle_module/build.gradle`
 47 | 
 48 | ```groovy
 49 | dependencies {
 50 |     //...
 51 |     implementation 'com.tradingview:lightweightcharts:3.8.0'
 52 | }
 53 | ```
 54 | 
 55 | ## Usage
 56 | 
 57 | Add view to the layout.
 58 | 
 59 | ```xml
 60 | <androidx.constraintlayout.widget.ConstraintLayout
 61 |         android:layout_width="match_parent"
 62 |         android:layout_height="match_parent">
 63 | 
 64 |         <com.tradingview.lightweightcharts.view.ChartsView
 65 |             android:id="@+id/charts_view"
 66 |             android:layout_width="0dp"
 67 |             android:layout_height="0dp"
 68 |             app:layout_constraintBottom_toBottomOf="parent"
 69 |             app:layout_constraintLeft_toLeftOf="parent"
 70 |             app:layout_constraintRight_toRightOf="parent"
 71 |             app:layout_constraintTop_toTopOf="parent" />
 72 | 
 73 | </androidx.constraintlayout.widget.ConstraintLayout>
 74 | ```
 75 | 
 76 | Configure the chart layout.
 77 | 
 78 | ```kotlin
 79 | charts_view.api.applyOptions {
 80 |     layout = layoutOptions {
 81 |         background = SolidColor(Color.LTGRAY)
 82 |         textColor = Color.BLACK.toIntColor()
 83 |     }
 84 |     localization = localizationOptions {
 85 |         locale = "ru-RU"
 86 |         priceFormatter = PriceFormatter(template = "{price:#2:#3}
quot;)
 87 |         timeFormatter = TimeFormatter(
 88 |             locale = "ru-RU",
 89 |             dateTimeFormat = DateTimeFormat.DATE_TIME
 90 |         )
 91 |     }
 92 | }
 93 | ```
 94 | 
 95 | Add any series to the chart and store a reference to it.
 96 | 
 97 | ```kotlin
 98 | lateinit var histogramSeries: SeriesApi
 99 | charts_view.api.addHistogramSeries(
100 |     onSeriesCreated = { series ->
101 |         histogramSeries = series
102 |     }
103 | )
104 | ```
105 | 
106 | Add data to the series.
107 | 
108 | ```kotlin
109 | val data = listOf(
110 |     HistogramData(Time.BusinessDay(2019, 6, 11), 40.01f),
111 |     HistogramData(Time.BusinessDay(2019, 6, 12), 52.38f),
112 |     HistogramData(Time.BusinessDay(2019, 6, 13), 36.30f),
113 |     HistogramData(Time.BusinessDay(2019, 6, 14), 34.48f),
114 |     WhitespaceData(Time.BusinessDay(2019, 6, 15)),
115 |     WhitespaceData(Time.BusinessDay(2019, 6, 16)),
116 |     HistogramData(Time.BusinessDay(2019, 6, 17), 41.50f),
117 |     HistogramData(Time.BusinessDay(2019, 6, 18), 34.82f)
118 | )
119 | histogramSeries.setData(data)
120 | ```
121 | 
122 | ## How to run the provided example
123 | 
124 | The [GitHub repository](https://github.com/tradingview/lightweight-charts-android) for lightweight-charts-android contains an example of the library in action.
125 | You can run the example (LighweightCharts.app) by cloning the repository and opening it in Android Studio. You will need to have [NodeJS/NPM](https://nodejs.org/) installed.
126 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/chart-types.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_position: 2
  3 | ---
  4 | 
  5 | # Chart types
  6 | 
  7 | Lightweight Charts offers different types of charts to suit various data visualization needs. This article provides an overview of the available chart types and how to create them.
  8 | 
  9 | ## Standard Time-based Chart
 10 | 
 11 | The standard time-based chart is the most common type, suitable for displaying time series data.
 12 | 
 13 | - **Creation method**: [`createChart`](api/functions/createChart)
 14 | - **Horizontal scale**: Time-based
 15 | - **Use case**: General-purpose charting for financial and time series data
 16 | 
 17 | ```js
 18 | import { createChart } from 'lightweight-charts';
 19 | 
 20 | const chart = createChart(document.getElementById('container'), options);
 21 | ```
 22 | 
 23 | This chart type uses time values for the horizontal scale and is ideal for most financial and time series data visualizations.
 24 | 
 25 | import CodeBlock from '@theme/CodeBlock';
 26 | export const timeBasedExample = `const chartOptions = { layout: { textColor: CHART_TEXT_COLOR, background: { type: 'solid', color: CHART_BACKGROUND_COLOR } } };
 27 | const chart = createChart(document.getElementById('container'), chartOptions);
 28 | const areaSeries = chart.addSeries(AreaSeries, { lineColor: LINE_LINE_COLOR, topColor: AREA_TOP_COLOR, bottomColor: AREA_BOTTOM_COLOR });
 29 | 
 30 | const data = [{ value: 0, time: 1642425322 }, { value: 8, time: 1642511722 }, { value: 10, time: 1642598122 }, { value: 20, time: 1642684522 }, { value: 3, time: 1642770922 }, { value: 43, time: 1642857322 }, { value: 41, time: 1642943722 }, { value: 43, time: 1643030122 }, { value: 56, time: 1643116522 }, { value: 46, time: 1643202922 }];
 31 | 
 32 | areaSeries.setData(data);
 33 | 
 34 | chart.timeScale().fitContent();`;
 35 | 
 36 | <CodeBlock className="language-js" replaceThemeConstants chart>{timeBasedExample}</CodeBlock>
 37 | 
 38 | ## Yield Curve Chart
 39 | 
 40 | The yield curve chart is specifically designed for displaying yield curves, common in financial analysis.
 41 | 
 42 | - **Creation method**: [`createYieldCurveChart`](api/functions/createYieldCurveChart)
 43 | - **Horizontal scale**: Linearly spaced, defined in monthly time duration units
 44 | - **Key differences**:
 45 |   - Whitespace is ignored for crosshair and grid lines
 46 |   - Specialized for yield curve representation
 47 | 
 48 | ```js
 49 | import { createYieldCurveChart } from 'lightweight-charts';
 50 | 
 51 | const chart = createYieldCurveChart(document.getElementById('container'), options);
 52 | ```
 53 | 
 54 | Use this chart type when you need to visualize yield curves or similar financial data where the horizontal scale represents time durations rather than specific dates.
 55 | 
 56 | :::tip
 57 | 
 58 | If you want to spread out the beginning of the plot further and don't need a linear time scale, you can enforce a minimum spacing around each point by increasing the [`minBarSpacing`](api/interfaces/TimeScaleOptions.md#minbarspacing) option in the TimeScaleOptions. To prevent the rest of the chart from spreading too wide, adjust the `baseResolution` to a larger number, such as `12` (months).
 59 | 
 60 | :::
 61 | 
 62 | export const yieldCurveExample = `const chartOptions = {
 63 |     layout: { textColor: CHART_TEXT_COLOR, background: { type: 'solid', color: CHART_BACKGROUND_COLOR } },
 64 |     yieldCurve: { baseResolution: 1, minimumTimeRange: 10, startTimeRange: 3 },
 65 |     handleScroll: false, handleScale: false,
 66 | };
 67 | 
 68 | const chart = createYieldCurveChart(document.getElementById('container'), chartOptions);
 69 | const lineSeries = chart.addSeries(LineSeries, { color: LINE_LINE_COLOR });
 70 | 
 71 | const curve = [{ time: 1, value: 5.378 }, { time: 2, value: 5.372 }, { time: 3, value: 5.271 }, { time: 6, value: 5.094 }, { time: 12, value: 4.739 }, { time: 24, value: 4.237 }, { time: 36, value: 4.036 }, { time: 60, value: 3.887 }, { time: 84, value: 3.921 }, { time: 120, value: 4.007 }, { time: 240, value: 4.366 }, { time: 360, value: 4.290 }];
 72 | 
 73 | lineSeries.setData(curve);
 74 | 
 75 | chart.timeScale().fitContent();`;
 76 | 
 77 | <CodeBlock className="language-js" replaceThemeConstants chart>{yieldCurveExample}</CodeBlock>
 78 | 
 79 | ## Options Chart (Price-based)
 80 | 
 81 | The options chart is a specialized type that uses price values on the horizontal scale instead of time.
 82 | 
 83 | - **Creation method**: [`createOptionsChart`](api/functions/createOptionsChart)
 84 | - **Horizontal scale**: Price-based (numeric)
 85 | - **Use case**: Visualizing option chains, price distributions, or any data where price is the primary x-axis metric
 86 | 
 87 | ```js
 88 | import { createOptionsChart } from 'lightweight-charts';
 89 | 
 90 | const chart = createOptionsChart(document.getElementById('container'), options);
 91 | ```
 92 | 
 93 | This chart type is particularly useful for financial instruments like options, where the price is a more relevant x-axis metric than time.
 94 | 
 95 | export const optionsExample = `const chartOptions = {
 96 |     layout: { textColor: CHART_TEXT_COLOR, background: { type: 'solid', color: CHART_BACKGROUND_COLOR } },
 97 | };
 98 | 
 99 | const chart = createOptionsChart(document.getElementById('container'), chartOptions);
100 | const lineSeries = chart.addSeries(LineSeries, { color: LINE_LINE_COLOR });
101 | 
102 | const data = [];
103 | for (let i = 0; i < 1000; i++) {
104 |     data.push({
105 |         time: i * 0.25,
106 |         value: Math.sin(i / 100) + i / 500,
107 |     });
108 | }
109 | 
110 | lineSeries.setData(data);
111 | 
112 | chart.timeScale().fitContent();`;
113 | 
114 | <CodeBlock className="language-js" replaceThemeConstants chart>{optionsExample}</CodeBlock>
115 | 
116 | ## Custom Horizontal Scale Chart
117 | 
118 | For advanced use cases, Lightweight Charts allows creating charts with custom horizontal scale behavior.
119 | 
120 | - **Creation method**: [`createChartEx`](api/functions/createChartEx)
121 | - **Horizontal scale**: Custom-defined
122 | - **Use case**: Specialized charting needs with non-standard horizontal scales
123 | 
124 | ```js
125 | import { createChartEx, defaultHorzScaleBehavior } from 'lightweight-charts';
126 | 
127 | const customBehavior = new (defaultHorzScaleBehavior())();
128 | // Customize the behavior as needed
129 | 
130 | const chart = createChartEx(document.getElementById('container'), customBehavior, options);
131 | ```
132 | 
133 | This method provides the flexibility to define custom horizontal scale behavior, allowing for unique and specialized chart types.
134 | 
135 | ## Choosing the Right Chart Type
136 | 
137 | - Use `createChart` for most standard time-based charting needs.
138 | - Choose `createYieldCurveChart` when working specifically with yield curves or similar financial data.
139 | - Opt for `createOptionsChart` when you need to visualize data with price as the primary horizontal axis, such as option chains.
140 | - Use `createChartEx` when you need a custom horizontal scale behavior that differs from the standard time-based or price-based scales.
141 | 
142 | Each chart type provides specific functionality and is optimized for different use cases. Consider your data structure and visualization requirements when selecting the appropriate chart type for your application.
143 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/intro.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | slug: /
  3 | id: intro
  4 | sidebar_position: 0
  5 | ---
  6 | 
  7 | # Getting started
  8 | 
  9 | ## Requirements
 10 | 
 11 | Lightweight Charts™ is _a client-side_ library that is not designed to work on the server side, for example, with Node.js.
 12 | 
 13 | The library code targets the [_ES2020_ language specification](https://262.ecma-international.org/11.0/).
 14 | Therefore, the browsers you work with should support this language revision. Consider the following [table](https://compat-table.github.io/compat-table/es2016plus/) to ensure the browser compatibility.
 15 | 
 16 | To support previous revisions, you can set up a transpilation process for the `lightweight-charts` package in your build system using tools such as Babel.
 17 | If you encounter any issues, open a [GitHub issue](https://github.com/tradingview/lightweight-charts/issues) with detailed information, and we will investigate potential solutions.
 18 | 
 19 | ## Installation
 20 | 
 21 | To set up the library, install the [`lightweight-charts`](https://www.npmjs.com/package/lightweight-charts) npm package:
 22 | 
 23 | ```console
 24 | npm install --save lightweight-charts
 25 | ```
 26 | 
 27 | The package includes TypeScript declarations, enabling seamless integration within TypeScript projects.
 28 | 
 29 | ### Build variants
 30 | 
 31 | The library ships with the following build variants:
 32 | 
 33 | |Dependencies included|Mode|ES module|IIFE (`window.LightweightCharts`)|
 34 | |-|-|-|-|
 35 | |No|PROD|`lightweight-charts.production.mjs`|N/A|
 36 | |No|DEV|`lightweight-charts.development.mjs`|N/A|
 37 | |Yes (standalone)|PROD|`lightweight-charts.standalone.production.mjs`|`lightweight-charts.standalone.production.js`|
 38 | |Yes (standalone)|DEV|`lightweight-charts.standalone.development.mjs`|`lightweight-charts.standalone.development.js`|
 39 | 
 40 | ## License and attribution
 41 | 
 42 | The Lightweight Charts™ license **requires** specifying TradingView as the product creator.
 43 | You should add the following attributes to a public page of your website or mobile application:
 44 | 
 45 | - Attribution notice from the [`NOTICE`](https://github.com/tradingview/lightweight-charts/blob/master/NOTICE) file
 46 | - The [https://www.tradingview.com](https://www.tradingview.com) link
 47 | 
 48 | ## Creating a chart
 49 | 
 50 | As a first step, import the library to your file:
 51 | 
 52 | ```js
 53 | import { createChart } from 'lightweight-charts';
 54 | ```
 55 | To create a chart, use the [`createChart`](/api/functions/createChart.md) function. You can call the function multiple times to create as many charts as needed:
 56 | 
 57 | ```js
 58 | import { createChart } from 'lightweight-charts';
 59 | 
 60 | // ...
 61 | const firstChart = createChart(document.getElementById('firstContainer'));
 62 | const secondChart = createChart(document.getElementById('secondContainer'));
 63 | ```
 64 | 
 65 | As a result, `createChart` returns an [`IChartApi`](/api/interfaces/IChartApi.md) object that allows you to interact with the created chart.
 66 | 
 67 | ## Creating a series
 68 | 
 69 | When the chart is created, you can display data on it.
 70 | 
 71 | The basic primitive to display data is a [series](/api/interfaces/ISeriesApi.md).
 72 | The library supports the following series types:
 73 | 
 74 | - Area
 75 | - Bar
 76 | - Baseline
 77 | - Candlestick
 78 | - Histogram
 79 | - Line
 80 | 
 81 | To create a series, use the [`addSeries`](/api/interfaces/IChartApi.md#addseries) method from [`IChartApi`](/api/interfaces/IChartApi.md).
 82 | As a parameter, specify a [series type](/series-types.mdx) you would like to create:
 83 | 
 84 | ```js
 85 | import { AreaSeries, BarSeries, BaselineSeries, createChart } from 'lightweight-charts';
 86 | 
 87 | const chart = createChart(container);
 88 | 
 89 | const areaSeries = chart.addSeries(AreaSeries);
 90 | const barSeries = chart.addSeries(BarSeries);
 91 | const baselineSeries = chart.addSeries(BaselineSeries);
 92 | // ...
 93 | ```
 94 | 
 95 | Note that a series **cannot be transferred** from one type to another one, since different series types require different data and options types.
 96 | 
 97 | ## Setting and updating a data
 98 | 
 99 | When the series is created, you can populate it with data.
100 | Note that the API calls remain the same regardless of the series type, although the data format may vary.
101 | 
102 | ### Setting the data to a series
103 | 
104 | To set the data to a series, you should call the [`ISeriesApi.setData`](/api/interfaces/ISeriesApi.md#setdata) method:
105 | 
106 | import CodeBlock from '@theme/CodeBlock';
107 | export const example = `const chartOptions = { layout: { textColor: CHART_TEXT_COLOR, background: { type: 'solid', color: CHART_BACKGROUND_COLOR } } };
108 | const chart = createChart(document.getElementById('container'), chartOptions);
109 | const areaSeries = chart.addSeries(AreaSeries, {
110 |     lineColor: LINE_LINE_COLOR, topColor: AREA_TOP_COLOR,
111 |     bottomColor: AREA_BOTTOM_COLOR,
112 | });
113 | areaSeries.setData([
114 |     { time: '2018-12-22', value: 32.51 },
115 |     { time: '2018-12-23', value: 31.11 },
116 |     { time: '2018-12-24', value: 27.02 },
117 |     { time: '2018-12-25', value: 27.32 },
118 |     { time: '2018-12-26', value: 25.17 },
119 |     { time: '2018-12-27', value: 28.89 },
120 |     { time: '2018-12-28', value: 25.46 },
121 |     { time: '2018-12-29', value: 23.92 },
122 |     { time: '2018-12-30', value: 22.68 },
123 |     { time: '2018-12-31', value: 22.67 },
124 | ]);
125 | 
126 | const candlestickSeries = chart.addSeries(CandlestickSeries, {
127 |     upColor: BAR_UP_COLOR, downColor: BAR_DOWN_COLOR, borderVisible: false,
128 |     wickUpColor: BAR_UP_COLOR, wickDownColor: BAR_DOWN_COLOR,
129 | });
130 | candlestickSeries.setData([
131 |     { time: '2018-12-22', open: 75.16, high: 82.84, low: 36.16, close: 45.72 },
132 |     { time: '2018-12-23', open: 45.12, high: 53.90, low: 45.12, close: 48.09 },
133 |     { time: '2018-12-24', open: 60.71, high: 60.71, low: 53.39, close: 59.29 },
134 |     { time: '2018-12-25', open: 68.26, high: 68.26, low: 59.04, close: 60.50 },
135 |     { time: '2018-12-26', open: 67.71, high: 105.85, low: 66.67, close: 91.04 },
136 |     { time: '2018-12-27', open: 91.04, high: 121.40, low: 82.70, close: 111.40 },
137 |     { time: '2018-12-28', open: 111.51, high: 142.83, low: 103.34, close: 131.25 },
138 |     { time: '2018-12-29', open: 131.33, high: 151.17, low: 77.68, close: 96.43 },
139 |     { time: '2018-12-30', open: 106.33, high: 110.20, low: 90.39, close: 98.10 },
140 |     { time: '2018-12-31', open: 109.87, high: 114.69, low: 85.66, close: 111.26 },
141 | ]);
142 | 
143 | chart.timeScale().fitContent();`;
144 | 
145 | <CodeBlock className="language-js" replaceThemeConstants chart>{example}</CodeBlock>
146 | 
147 | You can also use `setData` to replace all data items.
148 | 
149 | ### Updating the data in a series
150 | 
151 | If your data is updated, for example in real-time, you may also need to refresh the chart accordingly.
152 | To do this, call the [`ISeriesApi.update`](/api/interfaces/ISeriesApi.md#update) method that allows you to update the last data item or add a new one.
153 | 
154 | ```js
155 | import { AreaSeries, CandlestickSeries, createChart } from 'lightweight-charts';
156 | 
157 | const chart = createChart(container);
158 | 
159 | const areaSeries = chart.addSeries(AreaSeries);
160 | areaSeries.setData([
161 |     // Other data items
162 |     { time: '2018-12-31', value: 22.67 },
163 | ]);
164 | 
165 | const candlestickSeries = chart.addSeries(CandlestickSeries);
166 | candlestickSeries.setData([
167 |     // Other data items
168 |     { time: '2018-12-31', open: 109.87, high: 114.69, low: 85.66, close: 111.26 },
169 | ]);
170 | 
171 | // ...
172 | 
173 | // Update the most recent bar
174 | areaSeries.update({ time: '2018-12-31', value: 25 });
175 | candlestickSeries.update({ time: '2018-12-31', open: 109.87, high: 114.69, low: 85.66, close: 112 });
176 | 
177 | // Creating the new bar
178 | areaSeries.update({ time: '2019-01-01', value: 20 });
179 | candlestickSeries.update({ time: '2019-01-01', open: 112, high: 112, low: 100, close: 101 });
180 | ```
181 | 
182 | We do not recommend calling [`ISeriesApi.setData`](/api/interfaces/ISeriesApi.md#setdata) to update the chart, as this method replaces all series data and can significantly affect the performance.
183 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/ios.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | id: ios
  3 | description: You can use Lightweight Charts™ inside an iOS application. To use Lightweight Charts™ in that context, you can use our iOS wrapper, which will allow you to interact with Lightweight Charts™ library, which will be rendered in a web view.
  4 | keywords:
  5 |     - charts
  6 |     - iOS
  7 |     - canvas
  8 |     - charting library
  9 |     - charting
 10 |     - html5 charts
 11 |     - financial charting library
 12 | sidebar_position: 8
 13 | ---
 14 | 
 15 | # iOS wrapper
 16 | 
 17 | :::note
 18 | You can find the source code of the Lightweight Charts™ iOS wrapper in [this repository](https://github.com/tradingview/LightweightChartsIOS).
 19 | :::
 20 | 
 21 | :::info
 22 | 
 23 | This wrapper is currently still using `v3.8.0`. This will be updated to `v4.0.0` in the near future.
 24 | 
 25 | :::
 26 | 
 27 | You can use Lightweight Charts™ inside an iOS application. To use Lightweight Charts™ in that context, you can use our iOS wrapper, which will allow you to interact with Lightweight Charts™ library, which will be rendered in a web view.
 28 | 
 29 | ## Installation
 30 | 
 31 | :::info
 32 | Requires iOS 10.0+
 33 | :::
 34 | 
 35 | ### CocoaPods
 36 | 
 37 | [CocoaPods](https://cocoapods.org) is a dependency manager for Cocoa projects. For usage and installation instructions, visit their website. To integrate LightweightCharts into your Xcode project using CocoaPods, specify it in your `Podfile`:
 38 | 
 39 | ```ruby
 40 | pod 'LightweightCharts', '~> 3.8.0'
 41 | ```
 42 | 
 43 | ### Swift Package Manager
 44 | 
 45 | The [Swift Package Manager](https://swift.org/package-manager/) is a tool for automating the distribution of Swift code and is integrated into the `swift` compiler.
 46 | 
 47 | Once you have your Swift package set up, adding LightweightCharts as a dependency is as easy as adding it to the `dependencies` value of your `Package.swift`.
 48 | 
 49 | ```swift
 50 | dependencies: [
 51 |     .package(url: "https://github.com/tradingview/LightweightChartsIOS", .upToNextMajor(from: "4.0.0"))
 52 | ]
 53 | ```
 54 | 
 55 | ## Usage
 56 | 
 57 | Once the library has been installed in your repo, you're ready to create your first chart.
 58 | 
 59 | First of all, in a file where you would like to create a chart, you need to import the library:
 60 | 
 61 | ```swift
 62 | import LightweightCharts
 63 | ```
 64 | 
 65 | Create instance of LightweightCharts, which is a subclass of UIView, and add it to your view.
 66 | 
 67 | ```swift
 68 | var chart: LightweightCharts!
 69 | 
 70 | // ...
 71 | chart = LightweightCharts()
 72 | view.addSubview(chart)
 73 | // ... setup layout
 74 | ```
 75 | 
 76 | Add any series to the chart and store a reference to it.
 77 | 
 78 | ```swift
 79 | var series: BarSeries!
 80 | 
 81 | // ...
 82 | series = chart.addBarSeries(options: nil)
 83 | ```
 84 | 
 85 | Add data to the series.
 86 | 
 87 | ```swift
 88 | let data = [
 89 |     BarData(time: .string("2018-10-19"), open: 180.34, high: 180.99, low: 178.57, close: 179.85),
 90 |     BarData(time: .string("2018-10-22"), open: 180.82, high: 181.40, low: 177.56, close: 178.75),
 91 |     BarData(time: .string("2018-10-23"), open: 175.77, high: 179.49, low: 175.44, close: 178.53),
 92 |     BarData(time: .string("2018-10-24"), open: 178.58, high: 182.37, low: 176.31, close: 176.97),
 93 |     BarData(time: .string("2018-10-25"), open: 177.52, high: 180.50, low: 176.83, close: 179.07)
 94 | ]
 95 | 
 96 | // ...
 97 | series.setData(data: data)
 98 | ```
 99 | 
100 | ## How to run the provided example
101 | 
102 | The [GitHub repository](https://github.com/tradingview/LightweightChartsIOS) for LightweightChartsIOS contains an example of the library in action. To run the example, start by cloning the repository, go to the _Example_ directory, and then run
103 | 
104 | ```sh
105 | pod install
106 | ```
107 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/migrations/_category_.yml:
--------------------------------------------------------------------------------
1 | label: "Migration guides"
2 | position: 5
3 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/migrations/from-v2-to-v3.md:
--------------------------------------------------------------------------------
  1 | # From v2 to v3
  2 | 
  3 | Lightweight Charts™ library 3.0 announces the major improvements: supporting two price scales and improving the time scale API.
  4 | In order of keep the API clear and consistent, we decided to allow breaking change of the API.
  5 | 
  6 | In this document you can find the migration guide from the previous version to 3.0.
  7 | 
  8 | ## Time Scale API
  9 | 
 10 | Previously, to handle changing visible time range you needed to use `subscribeVisibleTimeRangeChange` and `unsubscribeVisibleTimeRangeChange` to subscribe and unsubscribe from visible range events.
 11 | These methods were available in the chart object  (e.g. you call it like `chart.subscribeVisibleTimeRangeChange(func)`).
 12 | 
 13 | In 3.0 in order to make API more consistent with the new API we decided to move these methods to [ITimeScaleApi](/api/interfaces/ITimeScaleApi.md)
 14 | (along with the new subscription methods [`ITimeScaleApi.subscribeVisibleLogicalRangeChange`](/api/interfaces/ITimeScaleApi.md#subscribevisiblelogicalrangechange) and [`ITimeScaleApi.unsubscribeVisibleLogicalRangeChange`](/api/interfaces/ITimeScaleApi.md#unsubscribevisiblelogicalrangechange)).
 15 | 
 16 | So, to migrate your code to 3.0 you just need to replace:
 17 | 
 18 | - `chart.subscribeVisibleTimeRangeChange` with `chart.timeScale().subscribeVisibleTimeRangeChange`
 19 | - `chart.unsubscribeVisibleTimeRangeChange` with `chart.timeScale().unsubscribeVisibleTimeRangeChange`
 20 | 
 21 | ## Two price scales
 22 | 
 23 | We understand disadvantages of breaking changes in the API, so we have not removed support of the current API at all, but have deprecated it, so the most common cases will continue to work.
 24 | 
 25 | You can refer to the new API [here](../price-scale.md).
 26 | 
 27 | Following are migration rules.
 28 | 
 29 | ### Default behavior
 30 | 
 31 | Default behavior is not changed. If you do not specify price scale options, the chart will have the right price scale visible and all the series will assign to it.
 32 | 
 33 | ### Left price scale
 34 | 
 35 | If you need the price scale to be drawn on the left side, you should make the following changes.
 36 | instead of
 37 | 
 38 | ```js
 39 | const chart = LightweightCharts.createChart(container, {
 40 |     priceScale: {
 41 |         position: 'left',
 42 |     },
 43 | });
 44 | ```
 45 | 
 46 | use
 47 | 
 48 | ```js
 49 | const chart = LightweightCharts.createChart(container, {
 50 |     rightPriceScale: {
 51 |         visible: false,
 52 |     },
 53 |     leftPriceScale: {
 54 |         visible: true,
 55 |     },
 56 | });
 57 | ```
 58 | 
 59 | then specify target price scale while creating a series:
 60 | 
 61 | ```js
 62 | const histSeries = chart.addHistogramSeries({
 63 |     priceScaleId: 'left',
 64 | });
 65 | ```
 66 | 
 67 | New version fully supports this case via the old API, however this support will be removed in the future releases.
 68 | 
 69 | ### No price scale
 70 | 
 71 | To create chart without any visible price scale, instead of
 72 | 
 73 | ```js
 74 | const chart = LightweightCharts.createChart(container, {
 75 |     priceScale: {
 76 |         position: 'none',
 77 |     },
 78 | });
 79 | ```
 80 | 
 81 | use
 82 | 
 83 | ```js
 84 | const chart = LightweightCharts.createChart(container, {
 85 |     leftPriceScale: {
 86 |         visible: false,
 87 |     },
 88 |     rightPriceScale: {
 89 |         visible: false,
 90 |     },
 91 | });
 92 | ```
 93 | 
 94 | New version fully supports this case via the old API, however this support will be removed in the future releases.
 95 | 
 96 | ### Creating overlay
 97 | 
 98 | To create an overlay series, instead of
 99 | 
100 | ```js
101 | const histogramSeries = chart.addHistogramSeries({
102 |     overlay: true,
103 | });
104 | ```
105 | 
106 | use
107 | 
108 | ```js
109 | const histogramSeries = chart.addHistogramSeries({
110 |     // or any other _the same_ id for all overlay series
111 |     priceScaleId: '',
112 | });
113 | ```
114 | 
115 | New version fully supports this case via the old API, however this support will be removed in the future releases.
116 | 
117 | ### Move price scale from right to left or vice versa
118 | 
119 | To do this, instead of
120 | 
121 | ```js
122 | const chart = LightweightCharts.createChart(container);
123 | 
124 | const mainSeries = chart.addLineSeries();
125 | 
126 | // ...
127 | 
128 | chart.applyOptions({
129 |     priceScale: {
130 |         position: 'left',
131 |     },
132 | });
133 | ```
134 | 
135 | use
136 | 
137 | ```js
138 | const chart = LightweightCharts.createChart(container);
139 | 
140 | const mainSeries = chart.addLineSeries();
141 | 
142 | // ...
143 | 
144 | chart.applyOptions({
145 |     leftPriceScale: {
146 |         visible: true,
147 |     },
148 |     rightPriceScale: {
149 |         visible: false,
150 |     },
151 | });
152 | 
153 | mainSeries.applyOptions({
154 |     priceScaleId: 'left',
155 | });
156 | ```
157 | 
158 | New version does not support this case via the old API, so, if you use it, you should migrate your code in order of keeping it working.
159 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/migrations/from-v3-to-v4.md:
--------------------------------------------------------------------------------
  1 | # From v3 to v4
  2 | 
  3 | In this document you can find the migration guide from the previous version v3 to v4.
  4 | 
  5 | ## Exported enum `LasPriceAnimationMode` has been removed
  6 | 
  7 | Please use [`LastPriceAnimationMode`](/api/enumerations/LastPriceAnimationMode.md) instead.
  8 | 
  9 | ## `scaleMargins` option has been removed from series options
 10 | 
 11 | Previously, you could do something like the following:
 12 | 
 13 | ```js
 14 | const series = chart.addLineSeries({
 15 |     scaleMargins: { /* options here */},
 16 | });
 17 | ```
 18 | 
 19 | And `scaleMargins` option was applied to series' price scale as `scaleMargins` option.
 20 | 
 21 | Since v4 this option won't be applied to the price scale and will be just ignored (if you're using TypeScript you will get a compilation error).
 22 | 
 23 | To fix this, you need to apply these options to series' price scale:
 24 | 
 25 | ```js
 26 | const series = chart.addLineSeries();
 27 | 
 28 | series.priceScale().applyOptions({
 29 |     scaleMargins: { /* options here */},
 30 | });
 31 | ```
 32 | 
 33 | ## `backgroundColor` from `layout` options has been removed
 34 | 
 35 | If you want to have solid background color you need to use [`background`](/api/interfaces/LayoutOptions.md#background) property instead, e.g. instead of:
 36 | 
 37 | ```js
 38 | const chart = createChart({
 39 |     layout: {
 40 |         backgroundColor: 'red',
 41 |     },
 42 | });
 43 | ```
 44 | 
 45 | use
 46 | 
 47 | ```js
 48 | const chart = createChart({
 49 |     layout: {
 50 |         background: {
 51 |             type: ColorType.Solid,
 52 |             color: 'red',
 53 |         },
 54 |     },
 55 | });
 56 | ```
 57 | 
 58 | ## `overlay` property of series options has been removed
 59 | 
 60 | Please follow [the guide for migrating from v2 to v3](./from-v2-to-v3.md#creating-overlay) where this option was deprecated.
 61 | 
 62 | ## `priceScale` option has been removed
 63 | 
 64 | Please follow [the guide for migrating from v2 to v3](./from-v2-to-v3.md#two-price-scales).
 65 | 
 66 | ## `priceScale()` method of chart API now requires to provide price scale id
 67 | 
 68 | Before v4 you could write the following code:
 69 | 
 70 | ```js
 71 | const priceScale = chart.priceScale();
 72 | ```
 73 | 
 74 | And in `priceScale` you had a right price scale if it is visible and a left price scale otherwise.
 75 | 
 76 | Since v4 you have to provide an ID of price scale explicitly, e.g. if you want to get a right price scale you need to provide `'right'`:
 77 | 
 78 | ```js
 79 | const rightPriceScale = chart.priceScale('right');
 80 | const leftPriceScale = chart.priceScale('left');
 81 | ```
 82 | 
 83 | ## `drawTicks` from `leftPriceScale` and `rightPriceScale` options has been renamed to `ticksVisible`
 84 | 
 85 | Since v4 you have to use `ticksVisible` instead of `drawTicks`.
 86 | 
 87 | ```js
 88 | const chart = createChart({
 89 |     leftPriceScale: {
 90 |         ticksVisible: false,
 91 |     },
 92 |     rightPriceScale: {
 93 |         ticksVisible: false,
 94 |     },
 95 | });
 96 | ```
 97 | 
 98 | Also this option is off by default.
 99 | 
100 | ## The type of outbound time values has been changed
101 | 
102 | Affected API:
103 | 
104 | - [`IChartApi.subscribeClick`](/api/interfaces/IChartApi.md#subscribeclick) (via [`MouseEventParams.time`](/api/interfaces/MouseEventParams.md#time))
105 | - [`IChartApi.subscribeCrosshairMove`](/api/interfaces/IChartApi.md#subscribecrosshairmove) (via [`MouseEventParams.time`](/api/interfaces/MouseEventParams.md#time))
106 | - [`LocalizationOptions.timeFormatter`](/api/interfaces/LocalizationOptions.md#timeformatter) (via argument of [`TimeFormatterFn`](/api/type-aliases/TimeFormatterFn.md))
107 | - [`TimeScaleOptions.tickMarkFormatter`](/api/interfaces/TimeScaleOptions.md#tickmarkformatter) (via argument of [`TickMarkFormatter`](/api/type-aliases/TickMarkFormatter.md))
108 | 
109 | Previously the type of an inbound time (a values you provide to the library, e.g. in [`ISeriesApi.setData`](/api/interfaces/ISeriesApi.md#setdata)) was different from an outbound one (a values the library provides to your code, e.g. an argument of [`LocalizationOptions.timeFormatter`](/api/interfaces/LocalizationOptions.md#timeformatter)).
110 | So the difference between types was that outbound time couldn't be a business day string.
111 | 
112 | Since v4 we improved our API in this matter and now the library will return exactly the same values back for all time-related properties.
113 | 
114 | Thus, if you provide a string to your series in [`ISeriesApi.setData`](/api/interfaces/ISeriesApi.md#setdata), you'll receive exactly the same value back:
115 | 
116 | ```js
117 | series.setData([
118 |     { time: '2001-01-01', value: 1 },
119 | ]);
120 | 
121 | chart.applyOptions({
122 |     localization: {
123 |         timeFormatter: time => time, // will be '2001-01-01' for the bar above
124 |     },
125 |     timeScale: {
126 |         tickMarkFormatter: time => time, // will be '2001-01-01' for the bar above
127 |     },
128 | });
129 | 
130 | chart.subscribeCrosshairMove(param => {
131 |     console.log(param.time); // will be '2001-01-01' if you hover the bar above
132 | });
133 | 
134 | chart.subscribeClick(param => {
135 |     console.log(param.time); // will be '2001-01-01' if you click on the bar above
136 | });
137 | ```
138 | 
139 | Handling this breaking change depends on your needs and your handlers, but generally speaking you need to convert provided time to a desired format manually if it is required.
140 | For example, you could use provided helpers to check the type of a time:
141 | 
142 | ```js
143 | import {
144 |     createChart,
145 |     isUTCTimestamp,
146 |     isBusinessDay,
147 | } from 'lightweight-charts';
148 | 
149 | const chart = createChart(document.body);
150 | 
151 | chart.subscribeClick(param => {
152 |     if (param.time === undefined) {
153 |         // the time is undefined, i.e. there is no any data point where a time could be received from
154 |         return;
155 |     }
156 | 
157 |     if (isUTCTimestamp(param.time)) {
158 |         // param.time is UTCTimestamp
159 |     } else if (isBusinessDay(param.time)) {
160 |         // param.time is a BusinessDay object
161 |     } else {
162 |         // param.time is a business day string in ISO format, e.g. `'2010-01-01'`
163 |     }
164 | });
165 | ```
166 | 
167 | ## `seriesPrices` property from `MouseEventParams` has been removed
168 | 
169 | Affected API:
170 | 
171 | - [`IChartApi.subscribeClick`](/api/interfaces/IChartApi.md#subscribeclick)
172 | - [`IChartApi.subscribeCrosshairMove`](/api/interfaces/IChartApi.md#subscribecrosshairmove)
173 | 
174 | The property `seriesPrices` of [`MouseEventParams`](/api/interfaces/MouseEventParams.md) has been removed.
175 | 
176 | Instead, you can use [`MouseEventParams.seriesData`](/api/interfaces/MouseEventParams.md#seriesdata) - it is pretty similar to the old `seriesPrices`, but it contains series' data items instead of just prices:
177 | 
178 | ```js
179 | lineSeries.setData([{ time: '2001-01-01', value: 1 }]);
180 | barSeries.setData([{ time: '2001-01-01', open: 5, high: 10, low: 1, close: 7 }]);
181 | 
182 | chart.subscribeCrosshairMove(param => {
183 |     console.log(param.seriesData.get(lineSeries)); // { time: '2001-01-01', value: 1 } or undefined
184 |     console.log(param.seriesData.get(barSeries)); // { time: '2001-01-01', open: 5, high: 10, low: 1, close: 7 } or undefined
185 | });
186 | ```
187 | 
188 | ## `MouseEventParams` field `hoveredMarkerId` was renamed to `hoveredObjectId`
189 | 
190 | Since v4 you have to use `hoveredObjectId` instead of `hoveredMarkerId`.
191 | 
192 | ```js
193 | chart.subscribeCrosshairMove(param => {
194 |     console.log(param.hoveredObjectId);
195 | });
196 | 
197 | chart.subscribeClick(param => {
198 |     console.log(param.hoveredObjectId);
199 | });
200 | ```
201 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/migrations/from-v4-to-v5.md:
--------------------------------------------------------------------------------
  1 | # From v4 to v5
  2 | 
  3 | In this document you can find the migration guide from the previous version v4
  4 | to v5.
  5 | 
  6 | ## Table of Contents
  7 | 
  8 | - [Series changes](#series-changes)
  9 | - [Series Markers](#series-markers)
 10 | - [Watermarks](#watermarks)
 11 | - [Plugin Typings](#plugin-typings)
 12 | 
 13 | ## Series changes
 14 | 
 15 | ### Overview of Changes {#overview-changes-series}
 16 | 
 17 | - Unified series creation API using single `addSeries` function
 18 | - Better tree-shaking support
 19 | - Individual series types must now be imported separately (for ESM)
 20 | 
 21 | ### Migration Steps {#migration-steps-series}
 22 | 
 23 | Replace all series creation calls with the new `addSeries` syntax. Here's how the migration works for each series type:
 24 | 
 25 | #### Before (v4) {#v4-series}
 26 | 
 27 | ```js
 28 | // Example with Line Series in v4
 29 | import { createChart } from 'lightweight-charts';
 30 | const chart = createChart(container, {});
 31 | const lineSeries = chart.addLineSeries({ color: 'red' });
 32 | ```
 33 | 
 34 | #### After (v5) {#v5-series}
 35 | 
 36 | ```js
 37 | // Example with Line Series in v5
 38 | import { createChart, LineSeries } from 'lightweight-charts';
 39 | const chart = createChart(container, {});
 40 | const lineSeries = chart.addSeries(LineSeries, { color: 'red' });
 41 | ```
 42 | 
 43 | #### Migration Reference {#migration-reference-series}
 44 | 
 45 | Here's how to migrate each series type:
 46 | 
 47 | | v4 Method | v5 Method |
 48 | |-----------|-----------|
 49 | | `chart.addLineSeries(options)` | `chart.addSeries(LineSeries, options)` |
 50 | | `chart.addAreaSeries(options)` | `chart.addSeries(AreaSeries, options)` |
 51 | | `chart.addBarSeries(options)` | `chart.addSeries(BarSeries, options)` |
 52 | | `chart.addBaselineSeries(options)` | `chart.addSeries(BaselineSeries, options)` |
 53 | | `chart.addCandlestickSeries(options)` | `chart.addSeries(CandlestickSeries, options)` |
 54 | | `chart.addHistogramSeries(options)` | `chart.addSeries(HistogramSeries, options)` |
 55 | 
 56 | ### Usage Examples {#usage-examples-series}
 57 | 
 58 | ESM (ES Modules):
 59 | 
 60 | ```js
 61 | import { createChart, LineSeries } from 'lightweight-charts';
 62 | 
 63 | const chart = createChart(container, {});
 64 | const lineSeries = chart.addSeries(LineSeries, { color: 'red' });
 65 | ```
 66 | 
 67 | UMD (Universal Module Definition):
 68 | 
 69 | ```js
 70 | const chart = LightweightCharts.createChart(container, {});
 71 | const lineSeries = chart.addSeries(LightweightCharts.LineSeries, { color: 'red' });
 72 | ```
 73 | 
 74 | Note: Make sure to import the specific series type (e.g., `LineSeries`, `AreaSeries`) along with `createChart` when using ES Modules. For UMD builds, all series types are available under the `LightweightCharts` namespace.
 75 | 
 76 | ## Series Markers
 77 | 
 78 | ### Overview of Changes {#overview-changes-markers}
 79 | 
 80 | - Markers moved to separate primitive for optimized bundle size
 81 | - New ⁠`createSeriesMarkers` function required
 82 | - Marker management through dedicated primitive instance
 83 | 
 84 | ### Migration Steps {#migration-steps-markers}
 85 | 
 86 | #### Before (v4) {#v4-markers}
 87 | 
 88 | ```javascript
 89 | // Markers were directly managed through the series instance
 90 | series.setMarkers([
 91 |     {
 92 |         time: '2019-04-09',
 93 |         position: 'aboveBar',
 94 |         color: 'black',
 95 |         shape: 'arrowDown',
 96 |     },
 97 | ]);
 98 | 
 99 | // Getting markers
100 | const markers = series.markers();
101 | ```
102 | 
103 | #### After (v5) {#v5-markers}
104 | 
105 | ```javascript
106 | // Import the markers primitive
107 | import { createSeriesMarkers } from 'lightweight-charts';
108 | 
109 | // Create a markers primitive instance
110 | const seriesMarkers = createSeriesMarkers(series, [
111 |     {
112 |         time: '2019-04-09',
113 |         position: 'aboveBar',
114 |         color: 'black',
115 |         shape: 'arrowDown',
116 |     },
117 | ]);
118 | 
119 | // Getting markers
120 | const markers = seriesMarkers.markers();
121 | 
122 | // Updating markers
123 | seriesMarkers.setMarkers([/* new markers */]);
124 | 
125 | // Remove all markers
126 | seriesMarkers.setMarkers([]);
127 | ```
128 | 
129 | ### Key Changes {#key-changes-markers}
130 | 
131 | - You must now import `createSeriesMarkers` separately
132 | - Instead of calling methods directly on the series instance, create a markers primitive using `createSeriesMarkers`
133 | - The markers API is now accessed through the markers primitive instance
134 | - The marker configuration object format remains the same
135 | - This change results in smaller bundle sizes when markers aren't used
136 | 
137 | If your application doesn't use markers, you can now benefit from a smaller bundle size as this functionality is no longer included in the core package.
138 | 
139 | ## Watermarks
140 | 
141 | ### Overview of Changes {#overview-changes-watermarks}
142 | 
143 | In the new version of Lightweight Charts, the watermark feature has undergone significant changes:
144 | 
145 | - Extraction from Core: The watermark functionality has been extracted from the core library.
146 | - Re-implementation: It's now re-implemented as a Pane Primitive (plugin) included within the library.
147 | - Improved Tree-shaking: This change makes the feature more tree-shakeable, potentially reducing bundle sizes for users who don't need watermarks.
148 | - Added an Image Watermark Primitive: In addition to the usual text based watermark, there is now
149 | an image watermark feature provided by the [`createImageWatermark`](/api/functions/createImageWatermark.md) plugin.
150 | 
151 | ### Migration Steps {#migration-steps-watermarks}
152 | 
153 | #### Before (v4) {#v4-watermarks}
154 | 
155 | ```js
156 | const chart = createChart(container, {
157 |     watermark: {
158 |         text: 'Watermark Text',
159 |         color: 'rgba(255,0,0,0.5)',
160 |     },
161 | });
162 | ```
163 | 
164 | #### After (v5) {#v5-watermarks}
165 | 
166 | ```js
167 | import { createChart, createTextWatermark } from 'lightweight-charts';
168 | 
169 | const chart = createChart(container, options);
170 | const firstPane = chart.panes()[0];
171 | 
172 | createTextWatermark(firstPane, {
173 |     horzAlign: 'center',
174 |     vertAlign: 'center',
175 |     lines: [{
176 |         text: 'Watermark Text',
177 |         color: 'rgba(255,0,0,0.5)',
178 |         fontSize: 50,
179 |     }],
180 | });
181 | 
182 | ```
183 | 
184 | ### Accessing the New TextWatermark
185 | 
186 | The TextWatermark plugin is now available as follows:
187 | 
188 | - **ESM builds**: Import [`createTextWatermark`](/api/functions/createTextWatermark.md) directly.
189 | - **Standalone script build**: Access via `LightweightCharts.createTextWatermark`.
190 | 
191 | ### Changes in Options
192 | 
193 | The options structure for watermarks has been revised:
194 | 
195 | 1. **Multiple Lines**: The plugin now supports multiple lines of text.
196 | 2. **Text Options**: Text-related options are now defined per line within the `lines` property of the options object.
197 | 
198 | ### Attaching the Watermark
199 | 
200 | To use the plugin, you need pass a pane object to the `createTextWatermark` function. The pane object specifies where the watermark should be attached:
201 | 
202 | 1. **Single Pane**: If you're using only one pane, you can easily fetch it using `chart.panes()[0]`.
203 | 2. **Multiple Panes**: For charts with multiple panes, you'll need to specify which pane to attach the watermark to.
204 | 
205 | ### Example: Implementing a Text Watermark
206 | 
207 | Here's a comprehensive example demonstrating how to implement a text watermark in the new version:
208 | 
209 | ```js
210 | const chart = createChart(container, options);
211 | const mainSeries = chart.addSeries(LineSeries);
212 | mainSeries.setData(generateData());
213 | 
214 | const firstPane = chart.panes()[0];
215 | createTextWatermark(firstPane, {
216 |     horzAlign: 'center',
217 |     vertAlign: 'center',
218 |     lines: [
219 |         {
220 |             text: 'Hello',
221 |             color: 'rgba(255,0,0,0.5)',
222 |             fontSize: 100,
223 |             fontStyle: 'bold',
224 |         },
225 |         {
226 |             text: 'This is a text watermark',
227 |             color: 'rgba(0,0,255,0.5)',
228 |             fontSize: 50,
229 |             fontStyle: 'italic',
230 |             fontFamily: 'monospace',
231 |         },
232 |     ],
233 | });
234 | ```
235 | 
236 | ## Plugin Typings
237 | 
238 | ### Overview of Changes {#overview-changes-plugins}
239 | 
240 | Some of the plugin types and interfaces have been renamed due to the additional
241 | of Pane Primitives.
242 | 
243 | - `ISeriesPrimitivePaneView` → `IPrimitivePaneView`
244 | - `ISeriesPrimitivePaneRenderer` → `IPrimitivePaneRenderer`
245 | - `SeriesPrimitivePaneViewZOrder` → `PrimitivePaneViewZOrder`
246 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/panes.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 4
 3 | ---
 4 | 
 5 | # Panes
 6 | 
 7 | Panes are essential elements that help segregate data visually within a single chart.
 8 | Panes are useful when you have a chart that needs to show more than one kind of data. For example, you might want to see a stock's price over time in one pane and its trading volume in another. This setup helps users get a fuller picture without cluttering the chart.
 9 | 
10 | By default, Lightweight Charts™ has a single pane, however, you can add more panes to the chart to display different series in separate areas. For detailed examples and code snippets on how to implement panes in your charts [see tutorial](/tutorials/how_to/panes).
11 | 
12 | ## Customization Options
13 | 
14 | Lightweight Charts™ offers a few [customization options](/api/interfaces/LayoutPanesOptions.md) to tailor the appearance and behavior of panes:
15 | 
16 | - [Pane Separator Color](/api/interfaces/LayoutPanesOptions.md#separatorcolor): Customize the color of the pane separators to match the chart design or improve visibility.
17 | 
18 | - [Separator Hover Color](/api/interfaces/LayoutPanesOptions.md#separatorhovercolor): Enhance user interaction by changing the color of separators on mouse hover.
19 | 
20 | - [Resizable Panes](/api/interfaces/LayoutPanesOptions.md#enableresize): Opt to enable or disable the resizing of panes by the user, offering flexibility in how data is displayed.
21 | 
22 | ## Managing Panes
23 | 
24 | While the specific methods to manipulate panes are covered in the detailed [example](/tutorials/how_to/panes), it's important to note that Lightweight Charts™ provides an [API for pane management](/api/interfaces/IPaneApi.md). This includes adding new panes, moving series between panes, adjusting pane height, and removing panes. The API ensures that developers have full control over the pane lifecycle and organization within their charts.
25 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/plugins/.eslintrc.js:
--------------------------------------------------------------------------------
 1 | module.exports = {
 2 | 	globals: {
 3 | 		document: false,
 4 | 		createChart: false,
 5 | 		LineSeries: false,
 6 | 		AreaSeries: false,
 7 | 		BarSeries: false,
 8 | 		BaselineSeries: false,
 9 | 		CandlestickSeries: false,
10 | 		HistogramSeries: false,
11 | 	},
12 | };
13 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/plugins/canvas-rendering-target.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_label: Canvas Rendering Target
  3 | sidebar_position: 4
  4 | ---
  5 | 
  6 | # Canvas Rendering Target
  7 | 
  8 | The renderer functions used within the plugins (both Custom Series, and Drawing
  9 | Primitives) are provided with a `CanvasRenderingTarget2D` interface on which the
 10 | drawing logic (using the
 11 | [Browser's 2D Canvas API](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D))
 12 | should be executed. `CanvasRenderingTarget2D` is provided by the
 13 | [Fancy Canvas](https://github.com/tradingview/fancy-canvas) library.
 14 | 
 15 | :::info
 16 | 
 17 | The typescript definitions can be viewed here:
 18 | 
 19 | - [fancy-canvas on npmjs.com](https://www.npmjs.com/package/fancy-canvas?activeTab=code)
 20 | 
 21 | and specifically the definition for `CanvasRenderingTarget2D` can be viewed
 22 | here:
 23 | 
 24 | - [canvas-rendering-target.d.ts](https://unpkg.com/fancy-canvas/canvas-rendering-target.d.ts)
 25 | 
 26 | :::
 27 | 
 28 | ## Using `CanvasRenderingTarget2D`
 29 | 
 30 | `CanvasRenderingTarget2D` provides two rendering scope which you can use:
 31 | 
 32 | - `useMediaCoordinateSpace`
 33 | - `useBitmapCoordinateSpace`
 34 | 
 35 | ## Difference between Bitmap and Media
 36 | 
 37 | Bitmap sizing represents the actual physical pixels on the device's screen,
 38 | while the media size represents the size of a pixel according to the operating
 39 | system (and browser) which is generally an integer representing the ratio of
 40 | actual physical pixels are used to render a media pixel. This integer ratio is
 41 | referred to as the device pixel ratio.
 42 | 
 43 | Using the bitmap sizing allows for more control over the drawn image to ensure
 44 | that the graphics are crisp and pixel perfect, however this generally means that
 45 | the code will contain a lot multiplication of coordinates by the pixel ratio. In
 46 | cases where you don't need to draw using the bitmap sizing then it is easier to
 47 | use media sizing as you don't need to worry about the devices pixel ratio.
 48 | 
 49 | ### Bitmap Coordinate Space
 50 | 
 51 | `useBitmapCoordinateSpace` can be used to if you would like draw using the
 52 | actual devices pixels as the coordinate sizing. The provided scope (of type
 53 | `BitmapCoordinatesRenderingScope`) contains readonly values for the following:
 54 | 
 55 | - `context`
 56 |   ([CanvasRenderingContext2D](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D)).
 57 |   Context which can be used for rendering.
 58 | - `horizontalPixelRatio` (number)
 59 | - `verticalPixelRatio` (number)
 60 | - `bitmapSize` (Size). Height and width of the canvas in bitmap dimensions.
 61 | - `mediaSize` (Size). Height and width of the canvas in media dimensions.
 62 | 
 63 | #### Bitmap Coordinate Space Usage
 64 | 
 65 | ```js title='javascript'
 66 | // target is an instance of CanvasRenderingTarget2D
 67 | target.useBitmapCoordinateSpace(scope => {
 68 |     // scope is an instance of BitmapCoordinatesRenderingScope
 69 | 
 70 |     // example of drawing a filled rectangle which fills the canvas
 71 |     scope.context.beginPath();
 72 |     scope.context.rect(0, 0, scope.bitmapSize.width, scope.bitmapSize.height);
 73 |     scope.context.fillStyle = 'rgba(100, 200, 50, 0.5)';
 74 |     scope.context.fill();
 75 | });
 76 | ```
 77 | 
 78 | ### Media Coordinate Space
 79 | 
 80 | `useMediaCoordinateSpace` can be used to if you would like draw using the media
 81 | dimensions as the coordinate sizing. The provided scope (of type
 82 | `MediaCoordinatesRenderingScope`) contains readonly values for the following:
 83 | 
 84 | - `context`
 85 |   ([CanvasRenderingContext2D](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D)).
 86 |   Context which can be used for rendering.
 87 | - `mediaSize` (Size). Height and width of the canvas in media dimensions.
 88 | 
 89 | #### Media Coordinate Space Usage
 90 | 
 91 | ```js title='javascript'
 92 | // target is an instance of CanvasRenderingTarget2D
 93 | target.useMediaCoordinateSpace(scope => {
 94 |     // scope is an instance of BitmapCoordinatesRenderingScope
 95 | 
 96 |     // example of drawing a filled rectangle which fills the canvas
 97 |     scope.context.beginPath();
 98 |     scope.context.rect(0, 0, scope.mediaSize.width, scope.mediaSize.height);
 99 |     scope.context.fillStyle = 'rgba(100, 200, 50, 0.5)';
100 |     scope.context.fill();
101 | });
102 | ```
103 | 
104 | ## General Tips
105 | 
106 | It is recommended that rendering functions should save and restore the canvas
107 | context before and after all the rendering logic to ensure that the canvas state
108 | is the same as when the renderer function was evoked. To handle the case
109 | when an error in the code might prevent the restore function from being evoked,
110 | you should use the try - finally code block to ensure that the context is
111 | correctly restored in all cases.
112 | 
113 | **Note** that `useBitmapCoordinateSpace` and `useMediaCoordinateSpace` will automatically
114 | save and restore the canvas context for the logic defined within them. This tip for your
115 | additional rendering functions within the `use*CoordinateSpace`.
116 | 
117 | ```js title='javascript'
118 | function myRenderingFunction(scope) {
119 |     const ctx = scope.context;
120 | 
121 |     // save the current state of the context to the stack
122 |     ctx.save();
123 | 
124 |     try {
125 |         // example code
126 |         scope.context.beginPath();
127 |         scope.context.rect(0, 0, scope.mediaSize.width, scope.mediaSize.height);
128 |         scope.context.fillStyle = 'rgba(100, 200, 50, 0.5)';
129 |         scope.context.fill();
130 |     } finally {
131 |         // restore the saved context from the stack
132 |         ctx.restore();
133 |     }
134 | }
135 | 
136 | target.useMediaCoordinateSpace(scope => {
137 |     myRenderingFunction(scope);
138 |     myOtherRenderingFunction(scope);
139 |     /* ... */
140 | });
141 | ```
142 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/plugins/custom_series.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_label: Custom Series Types
  3 | sidebar_position: 3
  4 | ---
  5 | 
  6 | # Custom Series Types
  7 | 
  8 | Custom series allow developers to create new types of series with their own data
  9 | structures, and rendering logic (implemented using
 10 | [CanvasRenderingContext2D](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D)
 11 | methods). These custom series extend the current capabilities of our built-in
 12 | series, providing a consistent API which mirrors the built-in chart types.
 13 | 
 14 | :::note
 15 | 
 16 | These series are expected to have a uniform width for each data point, which
 17 | ensures that the chart maintains a consistent look and feel across all series
 18 | types. The only restriction on the data structure is that it should extend the
 19 | [`CustomData`](../api/interfaces/CustomData.md) interface (have a valid time
 20 | property for each data point).
 21 | 
 22 | :::
 23 | 
 24 | ## Defining a Custom Series
 25 | 
 26 | A custom series should implement the
 27 | [`ICustomSeriesPaneView`](../api/interfaces/ICustomSeriesPaneView.md) interface.
 28 | The interface defines the basic functionality and structure required for
 29 | creating a custom series view.
 30 | 
 31 | It includes the following methods and properties:
 32 | 
 33 | ### Renderer
 34 | 
 35 | - ICustomSeriesPaneView property:
 36 |   [`renderer`](../api/interfaces/ICustomSeriesPaneView.md#renderer)
 37 | 
 38 | This method should return a renderer which implements the
 39 | [`ICustomSeriesPaneRenderer`](../api/interfaces/ICustomSeriesPaneRenderer.md)
 40 | interface and is used to draw the series data on the main chart pane.
 41 | 
 42 | The [`draw`](../api/interfaces/ICustomSeriesPaneRenderer.md#draw) method of the
 43 | renderer is evoked whenever the chart needs to draw the series.
 44 | 
 45 | The [`PriceToCoordinateConverter`](../api/type-aliases/PriceToCoordinateConverter.md)
 46 | provided as the 2nd argument to the draw method is a convenience function for
 47 | changing prices into vertical coordinate values. It is provided since the
 48 | series' original data will most likely be defined in price values, and the
 49 | renderer needs to draw with coordinates. The values returned by the converter
 50 | will be defined in mediaSize (unscaled by `devicePixelRatio`).
 51 | 
 52 | :::tip
 53 | 
 54 | `CanvasRenderingTarget2D` provided within the `draw` function is explained in
 55 | more detail on the [Canvas Rendering Target](./canvas-rendering-target) page.
 56 | 
 57 | :::
 58 | 
 59 | ### Update
 60 | 
 61 | - ICustomSeriesPaneView property:
 62 |   [`update`](../api/interfaces/ICustomSeriesPaneView.md#update)
 63 | 
 64 | This method will be called with the latest data for the renderer to use during
 65 | the next paint.
 66 | 
 67 | The update method is evoked with two parameters: `data` (discussed below), and
 68 | `seriesOptions`. seriesOptions is a reference to the currently applied options
 69 | for the series
 70 | 
 71 | The [`PaneRendererCustomData`](../api/interfaces/PaneRendererCustomData.md)
 72 | interface provides the data that can be used within the renderer for drawing the
 73 | series data. It includes the following properties:
 74 | 
 75 | - `bars`: List of all the series' items and their x coordinates. See
 76 |   [`CustomBarItemData`](../api/interfaces/CustomBarItemData.md) for more details
 77 | - `barSpacing`: Spacing between consecutive bars.
 78 | - `visibleRange`: The current visible range of items on the chart.
 79 | 
 80 | ### Price Value Builder
 81 | 
 82 | - ICustomSeriesPaneView property:
 83 |   [`priceValueBuilder`](../api/interfaces/ICustomSeriesPaneView.md#pricevaluebuilder)
 84 | 
 85 | A function for interpreting the custom series data and returning an array of
 86 | numbers representing the prices values for the item, specifically the equivalent
 87 | highest, lowest, and current price values for the data item.
 88 | 
 89 | These price values are used by the chart to determine the auto-scaling (to
 90 | ensure the items are in view) and the crosshair and price line positions. The
 91 | largest and smallest values in the array will be used to specify the visible
 92 | range of the painted item, and the last value will be used for the crosshair and
 93 | price line position.
 94 | 
 95 | ### Whitespace
 96 | 
 97 | - ICustomSeriesPaneView property:
 98 |   [`isWhitespace`](../api/interfaces/ICustomSeriesPaneView.md#iswhitespace)
 99 | 
100 | A function used by the library to determine which data points provided by the
101 | user should be considered Whitespace. The method should return `true` when the
102 | data point is Whitespace. Data points which are whitespace data won't be provided to
103 | the renderer, or the `priceValueBuilder`.
104 | 
105 | ### Default Options
106 | 
107 | - ICustomSeriesPaneView property:
108 |   [`defaultOptions`](../api/interfaces/ICustomSeriesPaneView.md#defaultoptions)
109 | 
110 | The default options to be used for the series. The user can override these
111 | values using the options argument in
112 | [`addCustomSeries`](../api/interfaces/IChartApi.md#addcustomseries), or via the
113 | [`applyOptions`](../api/interfaces/ISeriesApi.md#applyoptions) method on the
114 | `ISeriesAPI`.
115 | 
116 | ### Destroy
117 | 
118 | - ICustomSeriesPaneView property:
119 |   [`destroy`](../api/interfaces/ICustomSeriesPaneView.md#destroy)
120 | 
121 | This method will be evoked when the series has been removed from the chart. This
122 | method should be used to clean up any objects, references, and other items that
123 | could potentially cause memory leaks.
124 | 
125 | This method should contain all the necessary code to clean up the object before
126 | it is removed from memory. This includes removing any event listeners or timers
127 | that are attached to the object, removing any references to other objects, and
128 | resetting any values or properties that were modified during the lifetime of the
129 | object.
130 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/plugins/explainer-layers-demo.js:
--------------------------------------------------------------------------------
  1 | class PaneRenderer {
  2 | 	constructor(layer, showName, index, numBands) {
  3 | 		this._layer = layer;
  4 | 		this._showName = showName;
  5 | 		this._index = index;
  6 | 		this._selected = 'all';
  7 | 		this._numBands = numBands;
  8 | 	}
  9 | 	draw(target) {
 10 | 		if (this._layer.background) {
 11 | 			return;
 12 | 		}
 13 | 		if (this._selected !== 'all' && this._selected !== this._layer.id) {
 14 | 			return;
 15 | 		}
 16 | 		this._drawImpl(target);
 17 | 	}
 18 | 	drawBackground(target) {
 19 | 		if (!this._layer.background) {
 20 | 			return;
 21 | 		}
 22 | 		if (this._selected !== 'all' && this._selected !== this._layer.id) {
 23 | 			return;
 24 | 		}
 25 | 		this._drawImpl(target);
 26 | 	}
 27 | 
 28 | 	_drawingAngle(scope) {
 29 | 		const isPriceScale = scope.mediaSize.width < 100;
 30 | 		const isTimeScale = scope.mediaSize.height < 50;
 31 | 		if (isPriceScale) {
 32 | 			return 0;
 33 | 		}
 34 | 		if (isTimeScale) {
 35 | 			return Math.PI / 2;
 36 | 		}
 37 | 		return Math.PI / 3;
 38 | 	}
 39 | 
 40 | 	_drawImpl(target) {
 41 | 		target.useMediaCoordinateSpace(scope => {
 42 | 			const ctx = scope.context;
 43 | 			ctx.save();
 44 | 			if (this._selected === 'all') {
 45 | 				const isScale = scope.mediaSize.height < 50 || scope.mediaSize.width < 100;
 46 | 				const numBands = this._numBands + (isScale ? 2 : 0);
 47 | 				const angle = this._drawingAngle(scope);
 48 | 				const shift = Math.cos(angle) * scope.mediaSize.height;
 49 | 				const bandWidth = Math.round(
 50 | 					(scope.mediaSize.width - shift) / numBands
 51 | 				);
 52 | 				const offset = isScale ? 2 : 0;
 53 | 				const startX = (this._index + (isScale ? 1 : 0)) * bandWidth;
 54 | 				ctx.beginPath();
 55 | 				ctx.moveTo(startX, scope.mediaSize.height);
 56 | 				ctx.lineTo(startX + shift, offset);
 57 | 				ctx.lineTo(startX + shift + bandWidth, offset);
 58 | 				ctx.lineTo(startX + bandWidth, scope.mediaSize.height);
 59 | 				ctx.closePath();
 60 | 				ctx.fillStyle = this._layer.color;
 61 | 				ctx.fill();
 62 | 				if (this._showName) {
 63 | 					ctx.fillStyle = this._layer.textColor;
 64 | 					ctx.font = 'normal 16px sans-serif';
 65 | 					ctx.translate(startX, scope.mediaSize.height);
 66 | 					ctx.rotate(-1.06 * angle);
 67 | 					ctx.fillText(this._layer.name, 20, 20);
 68 | 				}
 69 | 			} else {
 70 | 				ctx.beginPath();
 71 | 				ctx.rect(0, 0, scope.mediaSize.width, scope.mediaSize.height);
 72 | 				ctx.fillStyle = this._layer.color;
 73 | 				ctx.fill();
 74 | 			}
 75 | 			ctx.restore();
 76 | 		});
 77 | 	}
 78 | 	update(name) {
 79 | 		this._selected = name;
 80 | 	}
 81 | }
 82 | 
 83 | class PaneView {
 84 | 	constructor(layer, showName, index, numBands) {
 85 | 		this._layer = layer;
 86 | 		this._renderer = new PaneRenderer(layer, showName, index, numBands);
 87 | 	}
 88 | 	zOrder() {
 89 | 		return this._layer.zOrder;
 90 | 	}
 91 | 	renderer() {
 92 | 		return this._renderer;
 93 | 	}
 94 | 	update(name) {
 95 | 		this._renderer.update(name);
 96 | 	}
 97 | }
 98 | 
 99 | class LayersPrimitive {
100 | 	constructor() {
101 | 		this.layers = {
102 | 			bottom: {
103 | 				name: 'bottom',
104 | 				color: '#f72585',
105 | 				textColor: '#ffffff',
106 | 				zOrder: 'bottom',
107 | 				background: false,
108 | 				id: 'bottom',
109 | 			},
110 | 			normalBackground: {
111 | 				name: 'normal (background)',
112 | 				color: '#7209b7',
113 | 				textColor: '#ffffff',
114 | 				zOrder: 'normal',
115 | 				background: true,
116 | 				id: 'normalBackground',
117 | 			},
118 | 			normal: {
119 | 				name: 'normal',
120 | 				color: '#4361ee',
121 | 				textColor: '#ffffff',
122 | 				zOrder: 'normal',
123 | 				background: false,
124 | 				id: 'normal',
125 | 			},
126 | 			top: {
127 | 				name: 'top',
128 | 				color: '#4cc9f0',
129 | 				textColor: '#000000',
130 | 				zOrder: 'top',
131 | 				background: false,
132 | 				id: 'top',
133 | 			},
134 | 		};
135 | 		const layerKeys = ['bottom', 'normalBackground', 'normal', 'top'];
136 | 		const numBands = layerKeys.length;
137 | 		this._paneViews = layerKeys.map(
138 | 			(key, index) => new PaneView(this.layers[key], true, index, numBands)
139 | 		);
140 | 		this._pricePaneViews = layerKeys.map(
141 | 			(key, index) => new PaneView(this.layers[key], false, index, numBands)
142 | 		);
143 | 		this._timePaneViews = layerKeys.map(
144 | 			(key, index) => new PaneView(this.layers[key], false, index, numBands)
145 | 		);
146 | 	}
147 | 
148 | 	changeSelectedLayer(id) {
149 | 		if (id !== 'all' && !Object.keys(this.layers).includes(id)) {
150 | 			return;
151 | 		}
152 | 		this._paneViews.forEach(view => view.update(id));
153 | 		this._pricePaneViews.forEach(view => view.update(id));
154 | 		this._timePaneViews.forEach(view => view.update(id));
155 | 		if (this._requestUpdate) {
156 | 			this._requestUpdate();
157 | 		}
158 | 	}
159 | 
160 | 	attached({ requestUpdate }) {
161 | 		this._requestUpdate = requestUpdate;
162 | 	}
163 | 	detached() {
164 | 		this._requestUpdate = undefined;
165 | 	}
166 | 
167 | 	updateAllViews() {}
168 | 
169 | 	paneViews() {
170 | 		return this._paneViews;
171 | 	}
172 | 
173 | 	timeAxisPaneViews() {
174 | 		return this._timePaneViews;
175 | 	}
176 | 
177 | 	priceAxisPaneViews() {
178 | 		return this._pricePaneViews;
179 | 	}
180 | }
181 | 
182 | let randomFactor = 25 + Math.random() * 25;
183 | const samplePoint = i =>
184 | 	i *
185 | 		(0.5 +
186 | 			Math.sin(i / 10) * 0.2 +
187 | 			Math.sin(i / 20) * 0.4 +
188 | 			Math.sin(i / randomFactor) * 0.8 +
189 | 			Math.sin(i / 500) * 0.5) +
190 | 	200;
191 | 
192 | function generateLineData(numberOfPoints = 500) {
193 | 	randomFactor = 25 + Math.random() * 25;
194 | 	const res = [];
195 | 	const date = new Date(Date.UTC(2018, 0, 1, 12, 0, 0, 0));
196 | 	for (let i = 0; i < numberOfPoints; ++i) {
197 | 		const time = date.getTime() / 1000;
198 | 		const value = samplePoint(i);
199 | 		res.push({
200 | 			time,
201 | 			value,
202 | 			customValues: {
203 | 				text: 'hello',
204 | 			},
205 | 		});
206 | 
207 | 		date.setUTCDate(date.getUTCDate() + 1);
208 | 	}
209 | 
210 | 	return res;
211 | }
212 | 
213 | const chartOptions = {
214 | 	layout: {
215 | 		textColor: CHART_TEXT_COLOR,
216 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
217 | 	},
218 | };
219 | 
220 | const chart = createChart(document.getElementById('container'), chartOptions);
221 | 
222 | const lineSeries = chart.addSeries(LineSeries, {
223 | 	color: CHART_TEXT_COLOR,
224 | });
225 | const data = generateLineData();
226 | lineSeries.setData(data);
227 | const layersPrimitive = new LayersPrimitive();
228 | lineSeries.attachPrimitive(layersPrimitive);
229 | 
230 | function generateLayerOption(id, name, selected) {
231 | 	const element = document.createElement('option');
232 | 	element.value = id;
233 | 	element.innerHTML = name;
234 | 	element.selected = selected;
235 | 	return element;
236 | }
237 | 
238 | const chartContainer = document.querySelector('#container');
239 | if (chartContainer) {
240 | 	const layerSelect = document.createElement('select');
241 | 	layerSelect.id = 'layer-select';
242 | 	layerSelect.name = 'layer';
243 | 	chartContainer.parentElement.appendChild(layerSelect);
244 | 	layerSelect.style.position = 'absolute';
245 | 	layerSelect.style.zIndex = 10;
246 | 	layerSelect.style.left = '10px';
247 | 	layerSelect.style.top = '10px';
248 | }
249 | 
250 | const layerSelectDiv = document.querySelector('#layer-select');
251 | // eslint-disable-next-line no-console
252 | console.log(layerSelectDiv);
253 | if (layerSelectDiv) {
254 | 	layerSelectDiv.appendChild(generateLayerOption('all', 'All', true));
255 | 	for (const layerInfo of Object.values(layersPrimitive.layers)) {
256 | 		layerSelectDiv.appendChild(
257 | 			generateLayerOption(layerInfo.id, layerInfo.name, false)
258 | 		);
259 | 	}
260 | 	layerSelectDiv.addEventListener('change', () => {
261 | 		layersPrimitive.changeSelectedLayer(layerSelectDiv.value);
262 | 	});
263 | }
264 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/plugins/explainer-sections-demo.js:
--------------------------------------------------------------------------------
  1 | /* eslint-disable max-classes-per-file */
  2 | class AxisView {
  3 | 	constructor(text, color, position) {
  4 | 		this._color = color;
  5 | 		this._text = text;
  6 | 		this._position = position;
  7 | 	}
  8 | 	coordinate() {
  9 | 		return this._position;
 10 | 	}
 11 | 	text() {
 12 | 		return this._text;
 13 | 	}
 14 | 	textColor() {
 15 | 		return '#FFFFFF';
 16 | 	}
 17 | 	backColor() {
 18 | 		return this._color;
 19 | 	}
 20 | }
 21 | 
 22 | class LegendPaneRenderer {
 23 | 	constructor(sections) {
 24 | 		this._sections = Object.values(sections);
 25 | 	}
 26 | 	draw(target) {
 27 | 		const count = this._sections.length;
 28 | 		const longestText = this._sections.reduce((longest, section) => {
 29 | 			if (section.name.length > longest.length) {
 30 | 				return section.name;
 31 | 			}
 32 | 			return longest;
 33 | 		}, '');
 34 | 		target.useMediaCoordinateSpace(scope => {
 35 | 			const ctx = scope.context;
 36 | 			const longestTextMeasurements = ctx.measureText(longestText);
 37 | 			ctx.beginPath();
 38 | 			ctx.roundRect(
 39 | 				20,
 40 | 				20,
 41 | 				longestTextMeasurements.width + 40,
 42 | 				(count + 0) * 20 + 10,
 43 | 				8
 44 | 			);
 45 | 			ctx.globalAlpha = 0.95;
 46 | 			ctx.fillStyle = '#FFFFFF';
 47 | 			ctx.fill();
 48 | 			ctx.globalAlpha = 1;
 49 | 			let currentY = 30;
 50 | 			this._sections.forEach(section => {
 51 | 				ctx.beginPath();
 52 | 				ctx.roundRect(30, currentY, 10, 10, 3);
 53 | 				ctx.fillStyle = section.color;
 54 | 				ctx.fill();
 55 | 				ctx.fillStyle = '#000000';
 56 | 				ctx.textBaseline = 'bottom';
 57 | 				ctx.fillText(section.name, 50, currentY + 10);
 58 | 				currentY += 20;
 59 | 			});
 60 | 		});
 61 | 	}
 62 | }
 63 | 
 64 | class LegendView {
 65 | 	constructor(sections) {
 66 | 		this._renderer = new LegendPaneRenderer(sections);
 67 | 	}
 68 | 	zOrder() {
 69 | 		return 'top';
 70 | 	}
 71 | 	renderer() {
 72 | 		return this._renderer;
 73 | 	}
 74 | }
 75 | 
 76 | class PaneRenderer {
 77 | 	constructor(color) {
 78 | 		this._color = color;
 79 | 	}
 80 | 	draw(target) {
 81 | 		target.useMediaCoordinateSpace(scope => {
 82 | 			const ctx = scope.context;
 83 | 			ctx.beginPath();
 84 | 			ctx.rect(0, 0, scope.mediaSize.width, scope.mediaSize.height);
 85 | 			ctx.globalAlpha = 0.3;
 86 | 			ctx.fillStyle = this._color;
 87 | 			ctx.fill();
 88 | 			ctx.globalAlpha = 0.6;
 89 | 			ctx.lineWidth = 8;
 90 | 			ctx.strokeStyle = this._color;
 91 | 			ctx.stroke();
 92 | 			ctx.globalAlpha = 1;
 93 | 		});
 94 | 	}
 95 | }
 96 | 
 97 | class PaneView {
 98 | 	constructor(color) {
 99 | 		this._renderer = new PaneRenderer(color);
100 | 	}
101 | 	zOrder() {
102 | 		return 'bottom';
103 | 	}
104 | 	renderer() {
105 | 		return this._renderer;
106 | 	}
107 | }
108 | 
109 | class SectionsPrimitive {
110 | 	constructor() {
111 | 		this.sections = {
112 | 			pane: { color: '#4cc9f0', name: 'Chart Pane (paneViews)' },
113 | 			price: { color: '#f72585', name: 'Price Pane (priceAxisPaneViews)' },
114 | 			time: { color: '#4361ee', name: 'Time Pane (timeAxisPaneViews)' },
115 | 			priceLabel: { color: '#f77f00', name: 'Price Label (priceAxisViews)' },
116 | 			timeLabel: { color: '#40916c', name: 'Time Label (timeAxisViews)' },
117 | 		};
118 | 		this._paneViews = [
119 | 			new PaneView(this.sections.pane.color),
120 | 			new LegendView(this.sections),
121 | 		];
122 | 		this._pricePaneViews = [new PaneView(this.sections.price.color)];
123 | 		this._timePaneViews = [new PaneView(this.sections.time.color)];
124 | 		this._priceAxisViews = [
125 | 			new AxisView('price label', this.sections.priceLabel.color, 80),
126 | 		];
127 | 		this._timeAxisViews = [
128 | 			new AxisView('time label', this.sections.timeLabel.color, 200),
129 | 		];
130 | 	}
131 | 
132 | 	updateAllViews() {}
133 | 
134 | 	paneViews() {
135 | 		return this._paneViews;
136 | 	}
137 | 
138 | 	timeAxisPaneViews() {
139 | 		return this._timePaneViews;
140 | 	}
141 | 
142 | 	priceAxisPaneViews() {
143 | 		return this._pricePaneViews;
144 | 	}
145 | 
146 | 	timeAxisViews() {
147 | 		return this._timeAxisViews;
148 | 	}
149 | 
150 | 	priceAxisViews() {
151 | 		return this._priceAxisViews;
152 | 	}
153 | }
154 | 
155 | let randomFactor = 25 + Math.random() * 25;
156 | const samplePoint = i =>
157 | 	i *
158 | 		(0.5 +
159 | 			Math.sin(i / 10) * 0.2 +
160 | 			Math.sin(i / 20) * 0.4 +
161 | 			Math.sin(i / randomFactor) * 0.8 +
162 | 			Math.sin(i / 500) * 0.5) +
163 | 	200;
164 | 
165 | function generateLineData(numberOfPoints = 500) {
166 | 	randomFactor = 25 + Math.random() * 25;
167 | 	const res = [];
168 | 	const date = new Date(Date.UTC(2018, 0, 1, 12, 0, 0, 0));
169 | 	for (let i = 0; i < numberOfPoints; ++i) {
170 | 		const time = date.getTime() / 1000;
171 | 		const value = samplePoint(i);
172 | 		res.push({
173 | 			time,
174 | 			value,
175 | 			customValues: {
176 | 				text: 'hello',
177 | 			},
178 | 		});
179 | 
180 | 		date.setUTCDate(date.getUTCDate() + 1);
181 | 	}
182 | 
183 | 	return res;
184 | }
185 | 
186 | const chartOptions = {
187 | 	layout: {
188 | 		textColor: CHART_TEXT_COLOR,
189 | 		background: { type: 'solid', color: CHART_BACKGROUND_COLOR },
190 | 	},
191 | };
192 | 
193 | const chart = createChart(document.getElementById('container'), chartOptions);
194 | 
195 | const lineSeries = chart.addSeries(LineSeries, {
196 | 	color: CHART_TEXT_COLOR,
197 | });
198 | const data = generateLineData();
199 | lineSeries.setData(data);
200 | lineSeries.attachPrimitive(new SectionsPrimitive());
201 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/plugins/intro.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_label: Introduction
  3 | sidebar_position: 0
  4 | ---
  5 | 
  6 | # Plugins Introduction
  7 | 
  8 | The library provides a rich set of charting capabilities out of the box, but
  9 | developers can also extend its functionality by building custom plugins.
 10 | 
 11 | Plugins in Lightweight Charts™️ come in three types:
 12 | [custom series](#custom-series), [drawing primitives](#drawing-primitives),
 13 | and [pane primitives](#pane-primitives).
 14 | Custom series allow developers to define new types of series, while drawing
 15 | primitives enable the creation of custom visualizations, drawing tools, and
 16 | chart annotations (and more) which can be attached to an existing series.
 17 | Pane primitives are similar to series primitives but are attached to the chart
 18 | pane itself, allowing for chart-wide annotations or features like watermarks.
 19 | 
 20 | :::tip Picking between the Custom Series and Drawing Primitives
 21 | 
 22 | In the majority of cases you will most likely be better served by using a
 23 | [Drawing Primitive](#drawing-primitives) plugin unless you are specifically
 24 | looking to create a new type of series.
 25 | 
 26 | :::
 27 | 
 28 | With the flexibility provided by these plugins, developers can create highly
 29 | customizable charting applications for their users.
 30 | 
 31 | ## Custom Series
 32 | 
 33 | Custom series allow developers to create new types of series with their own data
 34 | structures, and rendering logic (implemented using
 35 | [CanvasRenderingContext2D](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D)
 36 | methods). These custom series extend the current capabilities of our built-in
 37 | series, providing a consistent API which mirrors the built-in chart types. These
 38 | series are expected to have a uniform width for each data point, which ensures
 39 | that the chart maintains a consistent look and feel across all series types. The
 40 | only restriction on the data structure is that it should extend the
 41 | WhitespaceData interface (have a valid time property for each data point).
 42 | 
 43 | **You can find a more detailed guide to developing custom series in the
 44 | [Custom Series Types](./custom_series/) article.**
 45 | 
 46 | ### Adding a custom series to a chart
 47 | 
 48 | A custom series can be added to a chart using the
 49 | [`addCustomSeries`](../api/interfaces/IChartApi.md#addcustomseries) method
 50 | which expects an instance of a class implementing the
 51 | [ICustomSeriesPaneView](../api/interfaces/ICustomSeriesPaneView.md) interface
 52 | as the first argument, and an optional set of options as the second argument.
 53 | The series can then be used just like any other series, for example you would
 54 | use `setData` method to provide data to the series.
 55 | 
 56 | ```javascript title='javascript'
 57 | class MyCustomSeries {
 58 |     /* Class implementing the ICustomSeriesPaneView interface */
 59 | }
 60 | 
 61 | // Create an instantiated custom series.
 62 | const customSeriesInstance = new MyCustomSeries();
 63 | 
 64 | const chart = createChart(document.getElementById('container'));
 65 | const myCustomSeries = chart.addCustomSeries(customSeriesInstance, {
 66 |     // options for the MyCustomSeries
 67 |     customOption: 10,
 68 | });
 69 | 
 70 | const data = [
 71 |     { time: 1642425322, value: 123, customValue: 456 },
 72 |     /* ... more data */
 73 | ];
 74 | 
 75 | myCustomSeries.setData(data);
 76 | ```
 77 | 
 78 | ## Drawing Primitives
 79 | 
 80 | Drawing primitives provide a more flexible approach to extending the charting
 81 | capabilities of Lightweight Charts™️. They are attached to a specific series and
 82 | can draw anywhere on the chart, including the main chart pane, price scales, and
 83 | time scales.
 84 | 
 85 | Primitives can be used to create custom drawing tools or indicators, or to add
 86 | entirely new visualizations to the chart. Primitives can be drawn at different
 87 | levels in the visual stack, allowing for complex compositions of multiple
 88 | primitives.
 89 | 
 90 | **You can find a more detailed guide to developing series primitives in the
 91 | [Series Primitives](./series-primitives/) article.**
 92 | 
 93 | ### Adding a primitive to an existing series
 94 | 
 95 | A custom series primitive can be added to an existing series using the
 96 | [`attachPrimitive()`](../api/interfaces/ISeriesApi.md#attachprimitive) method
 97 | which expects an instantiated object implementing the
 98 | [ISeriesPrimitive](../api/type-aliases/ISeriesPrimitive.md) interface as the first
 99 | argument.
100 | 
101 | ```javascript title='javascript'
102 | class MyCustomPrimitive {
103 |     /* Class implementing the ISeriesPrimitive interface */
104 | }
105 | 
106 | // Create an instantiated series primitive.
107 | const myCustomPrimitive = new MyCustomPrimitive();
108 | 
109 | const chart = createChart(document.getElementById('container'));
110 | const lineSeries = chart.addSeries(LineSeries);
111 | 
112 | const data = [
113 |     { time: 1642425322, value: 123 },
114 |     /* ... more data */
115 | ];
116 | 
117 | // Attach the primitive to the series
118 | lineSeries.attachPrimitive(myCustomPrimitive);
119 | ```
120 | 
121 | ## Pane Primitives
122 | 
123 | Pane Primitives are similar to Series Primitives but are attached to the chart pane itself rather than a specific series. They are ideal for creating chart-wide annotations or features that are not tied to any particular series data.
124 | 
125 | ### Adding a Pane Primitive to a chart
126 | 
127 | A Pane Primitive can be added to a chart using the `attachPrimitive()` method on the `IPaneApi` interface. Here's an example:
128 | 
129 | ```javascript
130 | class MyCustomPanePrimitive {
131 |     /* Class implementing the IPanePrimitive interface */
132 | }
133 | 
134 | // Create an instantiated pane primitive.
135 | const myCustomPanePrimitive = new MyCustomPanePrimitive();
136 | 
137 | const chart = createChart(document.getElementById('container'));
138 | const mainPane = chart.panes()[0]; // Get the main pane
139 | 
140 | // Attach the primitive to the pane
141 | mainPane.attachPrimitive(myCustomPanePrimitive);
142 | ```
143 | 
144 | Pane Primitives offer a powerful way to add chart-wide features or annotations without the need to associate them with a specific series.
145 | 
146 | ## Examples
147 | 
148 | We have a few example plugins within the `plugin-examples` folder of the Lightweight Charts™️ repo: [plugin-examples](https://github.com/tradingview/lightweight-charts/tree/master/plugin-examples).
149 | 
150 | You can view a demo site for these plugin examples here: [Plugin Examples Demos](https://tradingview.github.io/lightweight-charts/plugin-examples).
151 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/plugins/pane-primitives.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_label: Pane Primitives
 3 | sidebar_position: 2
 4 | ---
 5 | 
 6 | # Pane Primitives
 7 | 
 8 | In addition to Series Primitives, the library now supports Pane Primitives. These are essentially the same as Series Primitives but are designed to draw on the pane of a chart rather than being associated with a specific series. Pane Primitives can be used for features like watermarks or other chart-wide annotations.
 9 | 
10 | ## Key Differences from Series Primitives
11 | 
12 | 1. Pane Primitives are attached to the chart pane rather than a specific series.
13 | 2. They cannot draw on the price and time scales.
14 | 3. They are ideal for chart-wide features that are not tied to a particular series.
15 | 
16 | ## Adding a Pane Primitive
17 | 
18 | Pane Primitives can be added to a chart using the `attachPrimitive` method on the [`IPaneApi`](../api/interfaces/IPaneApi.md) interface. Here's an example:
19 | 
20 | ```javascript
21 | const chart = createChart(document.getElementById('container'));
22 | const pane = chart.panes()[0]; // Get the first (main) pane
23 | 
24 | const myPanePrimitive = new MyCustomPanePrimitive();
25 | pane.attachPrimitive(myPanePrimitive);
26 | ```
27 | 
28 | ## Implementing a Pane Primitive
29 | 
30 | To create a Pane Primitive, you should implement the [`IPanePrimitive`](../api/type-aliases/IPanePrimitive.md) interface. This interface is similar to [`ISeriesPrimitive`](../api/type-aliases/ISeriesPrimitive.md), but with some key differences:
31 | 
32 | - It doesn't include methods for drawing on price and time scales.
33 | - The `paneViews` method is used to define what will be drawn on the chart pane.
34 | 
35 | Here's a basic example of a Pane Primitive implementation:
36 | 
37 | ```javascript
38 | class MyCustomPanePrimitive {
39 |     paneViews() {
40 |         return [
41 |             {
42 |                 renderer: {
43 |                     draw: target => {
44 |                         // Custom drawing logic here
45 |                     },
46 |                 },
47 |             },
48 |         ];
49 |     }
50 | 
51 |     // Other methods as needed...
52 | }
53 | ```
54 | 
55 | For more details on implementing Pane Primitives, refer to the [`IPanePrimitive`](../api/type-aliases/IPanePrimitive.md) interface documentation.
56 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/plugins/pixel-perfect-rendering/_category_.yml:
--------------------------------------------------------------------------------
1 | label: "Pixel Perfect Rendering"
2 | position: 5
3 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/plugins/pixel-perfect-rendering/index.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_position: 0
  3 | sidebar_label: Pixel Perfect Rendering
  4 | pagination_title: Pixel Perfect Rendering
  5 | title: Best Practices for Pixel Perfect Rendering in Canvas Drawings
  6 | description: Best Practices for Pixel Perfect Rendering in Canvas Drawings when creating plugins for the Lightweight Charts
  7 | keywords:
  8 |   - plugins
  9 |   - extensions
 10 |   - rendering
 11 |   - canvas
 12 |   - bitmap
 13 |   - media
 14 |   - pixels
 15 | pagination_prev: null
 16 | ---
 17 | 
 18 | To achieve crisp pixel perfect rendering for your plugins, it is recommended that the canvas drawings are created using bitmap coordinates. The difference between media and bitmap coordinate spaces is discussed on the [Canvas Rendering Target](../canvas-rendering-target.md) page. **Essentially, all drawing actions should use integer positions and dimensions when on the bitmap coordinate space.**
 19 | 
 20 | To ensure consistency between your plugins and the library's built-in logic for rendering points on the chart, use of the following calculation functions.
 21 | 
 22 | :::info
 23 | 
 24 | Variable names containing `media` refer to positions / dimensions specified using the media coordinate space (such as the x and y coordinates provided by the library to the renderers), and names containing `bitmap` refer to positions / dimensions on the bitmap coordinate space (actual device screen pixels).
 25 | 
 26 | :::
 27 | 
 28 | ## Centered Shapes
 29 | 
 30 | If you need to draw a shape which is centred on a position (for example a price or x coordinate) and has a desired width then you could use the `positionsLine` function presented below. This can be used for drawing a horizontal line at a specific price, or a vertical line aligned with the centre of series point.
 31 | 
 32 | ```typescript
 33 | interface BitmapPositionLength {
 34 |     /** coordinate for use with a bitmap rendering scope */
 35 |     position: number;
 36 |     /** length for use with a bitmap rendering scope */
 37 |     length: number;
 38 | }
 39 | 
 40 | function centreOffset(lineBitmapWidth: number): number {
 41 |     return Math.floor(lineBitmapWidth * 0.5);
 42 | }
 43 | 
 44 | /**
 45 |  * Calculates the bitmap position for an item with a desired length (height or width), and centred according to
 46 |  * a position coordinate defined in media sizing.
 47 |  * @param positionMedia - position coordinate for the bar (in media coordinates)
 48 |  * @param pixelRatio - pixel ratio. Either horizontal for x positions, or vertical for y positions
 49 |  * @param desiredWidthMedia - desired width (in media coordinates)
 50 |  * @returns Position of the start point and length dimension.
 51 |  */
 52 | export function positionsLine(
 53 |     positionMedia: number,
 54 |     pixelRatio: number,
 55 |     desiredWidthMedia: number = 1,
 56 |     widthIsBitmap?: boolean
 57 | ): BitmapPositionLength {
 58 |     const scaledPosition = Math.round(pixelRatio * positionMedia);
 59 |     const lineBitmapWidth = widthIsBitmap
 60 |         ? desiredWidthMedia
 61 |         : Math.round(desiredWidthMedia * pixelRatio);
 62 |     const offset = centreOffset(lineBitmapWidth);
 63 |     const position = scaledPosition - offset;
 64 |     return { position, length: lineBitmapWidth };
 65 | }
 66 | ```
 67 | 
 68 | ## Dual Point Shapes
 69 | 
 70 | If you need to draw a shape between two coordinates (for example, y coordinates for a high and low price) then you can use the `positionsBox` function as presented below.
 71 | 
 72 | ```typescript
 73 | /**
 74 |  * Determines the bitmap position and length for a dimension of a shape to be drawn.
 75 |  * @param position1Media - media coordinate for the first point
 76 |  * @param position2Media - media coordinate for the second point
 77 |  * @param pixelRatio - pixel ratio for the corresponding axis (vertical or horizontal)
 78 |  * @returns Position of the start point and length dimension.
 79 |  */
 80 | export function positionsBox(
 81 |     position1Media: number,
 82 |     position2Media: number,
 83 |     pixelRatio: number
 84 | ): BitmapPositionLength {
 85 |     const scaledPosition1 = Math.round(pixelRatio * position1Media);
 86 |     const scaledPosition2 = Math.round(pixelRatio * position2Media);
 87 |     return {
 88 |         position: Math.min(scaledPosition1, scaledPosition2),
 89 |         length: Math.abs(scaledPosition2 - scaledPosition1) + 1,
 90 |     };
 91 | }
 92 | ```
 93 | 
 94 | ## Default Widths
 95 | 
 96 | Please refer to the following pages for functions defining the default widths of shapes drawn by the library:
 97 | 
 98 | - [Crosshair and Grid Lines](./widths/crosshair.md)
 99 | - [Candlesticks](./widths/candlestick.md)
100 | - [Columns (Histogram)](./widths/columns.md)
101 | - [Full Bar Width](./widths/full-bar-width.md)
102 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/plugins/pixel-perfect-rendering/widths/_category_.yml:
--------------------------------------------------------------------------------
1 | label: "Default Widths"
2 | position: 0
3 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/plugins/pixel-perfect-rendering/widths/candlestick.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 0
 3 | sidebar_label: Candlesticks
 4 | pagination_title: Candlestick Widths
 5 | title: Candlestick Width Calculations
 6 | description: Describes the calculation for candlestick body widths
 7 | keywords:
 8 |   - plugins
 9 |   - extensions
10 |   - rendering
11 |   - canvas
12 |   - bitmap
13 |   - media
14 |   - pixels
15 |   - candlestick
16 |   - width
17 | ---
18 | 
19 | :::tip
20 | 
21 | It is recommend that you first read the [Pixel Perfect Rendering](../index.md) page.
22 | 
23 | :::
24 | 
25 | The following functions can be used to get the calculated width that the library would use for a candlestick at a specific bar spacing and device pixel ratio.
26 | 
27 | Below a bar spacing of 4, the library will attempt to use as large a width as possible without the possibility of overlapping, whilst above 4 then the width will start to trend towards an 80% width of the available space.
28 | 
29 | :::warning
30 | 
31 | It is expected that candles can overlap slightly at smaller bar spacings (more pronounced on lower resolution devices). This produces a more readable chart. If you need to ensure that bars can never overlap then rather use the widths for [Columns](./columns.md) or the [full bar width](./full-bar-width.md) calculation.
32 | 
33 | :::
34 | 
35 | ```typescript
36 | function optimalCandlestickWidth(
37 |     barSpacing: number,
38 |     pixelRatio: number
39 | ): number {
40 |     const barSpacingSpecialCaseFrom = 2.5;
41 |     const barSpacingSpecialCaseTo = 4;
42 |     const barSpacingSpecialCaseCoeff = 3;
43 |     if (barSpacing >= barSpacingSpecialCaseFrom && barSpacing <= barSpacingSpecialCaseTo) {
44 |         return Math.floor(barSpacingSpecialCaseCoeff * pixelRatio);
45 |     }
46 |     // coeff should be 1 on small barspacing and go to 0.8 while bar spacing grows
47 |     const barSpacingReducingCoeff = 0.2;
48 |     const coeff =
49 |         1 -
50 |         (barSpacingReducingCoeff *
51 |             Math.atan(
52 |                 Math.max(barSpacingSpecialCaseTo, barSpacing) - barSpacingSpecialCaseTo
53 |             )) /
54 |             (Math.PI * 0.5);
55 |     const res = Math.floor(barSpacing * coeff * pixelRatio);
56 |     const scaledBarSpacing = Math.floor(barSpacing * pixelRatio);
57 |     const optimal = Math.min(res, scaledBarSpacing);
58 |     return Math.max(Math.floor(pixelRatio), optimal);
59 | }
60 | 
61 | /**
62 |  * Calculates the candlestick width that the library would use for the current
63 |  * bar spacing.
64 |  * @param barSpacing - bar spacing in media coordinates
65 |  * @param horizontalPixelRatio - horizontal pixel ratio
66 |  * @returns The width (in bitmap coordinates) that the chart would use to draw a candle body
67 |  */
68 | export function candlestickWidth(
69 |     barSpacing: number,
70 |     horizontalPixelRatio: number
71 | ): number {
72 |     let width = optimalCandlestickWidth(barSpacing, horizontalPixelRatio);
73 |     if (width >= 2) {
74 |         const wickWidth = Math.floor(horizontalPixelRatio);
75 |         if (wickWidth % 2 !== width % 2) {
76 |             width--;
77 |         }
78 |     }
79 |     return width;
80 | }
81 | ```
82 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/plugins/pixel-perfect-rendering/widths/columns.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_position: 0
  3 | sidebar_label: Columns
  4 | pagination_title: Histogram Column Widths
  5 | title: Histogram Column Width Calculations
  6 | description: Describes the calculation for histogram column widths
  7 | keywords:
  8 |   - plugins
  9 |   - extensions
 10 |   - rendering
 11 |   - canvas
 12 |   - bitmap
 13 |   - media
 14 |   - pixels
 15 |   - histogram
 16 |   - column
 17 |   - width
 18 | ---
 19 | 
 20 | :::tip
 21 | 
 22 | It is recommend that you first read the [Pixel Perfect Rendering](../index.md) page.
 23 | 
 24 | :::
 25 | 
 26 | The following functions can be used to get the calculated width that the library would use for a histogram column at a specific bar spacing and device pixel ratio.
 27 | 
 28 | You can use the `calculateColumnPositionsInPlace` function instead of the `calculateColumnPositions` function to perform the calculation on an existing array of items without needing to create additional arrays (which is more efficient). It is recommended that you memoize the majority of the calculations below to improve the rendering performance.
 29 | 
 30 | ```typescript
 31 | const alignToMinimalWidthLimit = 4;
 32 | const showSpacingMinimalBarWidth = 1;
 33 | 
 34 | /**
 35 |  * Spacing gap between columns.
 36 |  * @param barSpacingMedia - spacing between bars (media coordinate)
 37 |  * @param horizontalPixelRatio - horizontal pixel ratio
 38 |  * @returns Spacing gap between columns (in Bitmap coordinates)
 39 |  */
 40 | function columnSpacing(barSpacingMedia: number, horizontalPixelRatio: number) {
 41 |     return Math.ceil(barSpacingMedia * horizontalPixelRatio) <=
 42 |         showSpacingMinimalBarWidth
 43 |         ? 0
 44 |         : Math.max(1, Math.floor(horizontalPixelRatio));
 45 | }
 46 | 
 47 | /**
 48 |  * Desired width for columns. This may not be the final width because
 49 |  * it may be adjusted later to ensure all columns on screen have a
 50 |  * consistent width and gap.
 51 |  * @param barSpacingMedia - spacing between bars (media coordinate)
 52 |  * @param horizontalPixelRatio - horizontal pixel ratio
 53 |  * @param spacing - Spacing gap between columns (in Bitmap coordinates). (optional, provide if you have already calculated it)
 54 |  * @returns Desired width for column bars (in Bitmap coordinates)
 55 |  */
 56 | function desiredColumnWidth(
 57 |     barSpacingMedia: number,
 58 |     horizontalPixelRatio: number,
 59 |     spacing?: number
 60 | ) {
 61 |     return (
 62 |         Math.round(barSpacingMedia * horizontalPixelRatio) -
 63 |         (spacing ?? columnSpacing(barSpacingMedia, horizontalPixelRatio))
 64 |     );
 65 | }
 66 | 
 67 | interface ColumnCommon {
 68 |     /** Spacing gap between columns */
 69 |     spacing: number;
 70 |     /** Shift columns left by one pixel */
 71 |     shiftLeft: boolean;
 72 |     /** Half width of a column */
 73 |     columnHalfWidthBitmap: number;
 74 |     /** horizontal pixel ratio */
 75 |     horizontalPixelRatio: number;
 76 | }
 77 | 
 78 | /**
 79 |  * Calculated values which are common to all the columns on the screen, and
 80 |  * are required to calculate the individual positions.
 81 |  * @param barSpacingMedia - spacing between bars (media coordinate)
 82 |  * @param horizontalPixelRatio - horizontal pixel ratio
 83 |  * @returns calculated values for subsequent column calculations
 84 |  */
 85 | function columnCommon(
 86 |     barSpacingMedia: number,
 87 |     horizontalPixelRatio: number
 88 | ): ColumnCommon {
 89 |     const spacing = columnSpacing(barSpacingMedia, horizontalPixelRatio);
 90 |     const columnWidthBitmap = desiredColumnWidth(
 91 |         barSpacingMedia,
 92 |         horizontalPixelRatio,
 93 |         spacing
 94 |     );
 95 |     const shiftLeft = columnWidthBitmap % 2 === 0;
 96 |     const columnHalfWidthBitmap = (columnWidthBitmap - (shiftLeft ? 0 : 1)) / 2;
 97 |     return {
 98 |         spacing,
 99 |         shiftLeft,
100 |         columnHalfWidthBitmap,
101 |         horizontalPixelRatio,
102 |     };
103 | }
104 | 
105 | interface ColumnPosition {
106 |     left: number;
107 |     right: number;
108 |     shiftLeft: boolean;
109 | }
110 | 
111 | /**
112 |  * Calculate the position for a column. These values can be later adjusted
113 |  * by a second pass which corrects widths, and shifts columns.
114 |  * @param xMedia - column x position (center) in media coordinates
115 |  * @param columnData - precalculated common values (returned by `columnCommon`)
116 |  * @param previousPosition - result from this function for the previous bar.
117 |  * @returns initial column position
118 |  */
119 | function calculateColumnPosition(
120 |     xMedia: number,
121 |     columnData: ColumnCommon,
122 |     previousPosition: ColumnPosition | undefined
123 | ): ColumnPosition {
124 |     const xBitmapUnRounded = xMedia * columnData.horizontalPixelRatio;
125 |     const xBitmap = Math.round(xBitmapUnRounded);
126 |     const xPositions: ColumnPosition = {
127 |         left: xBitmap - columnData.columnHalfWidthBitmap,
128 |         right:
129 |             xBitmap +
130 |             columnData.columnHalfWidthBitmap -
131 |             (columnData.shiftLeft ? 1 : 0),
132 |         shiftLeft: xBitmap > xBitmapUnRounded,
133 |     };
134 |     const expectedAlignmentShift = columnData.spacing + 1;
135 |     if (previousPosition) {
136 |         if (xPositions.left - previousPosition.right !== expectedAlignmentShift) {
137 |             // need to adjust alignment
138 |             if (previousPosition.shiftLeft) {
139 |                 previousPosition.right = xPositions.left - expectedAlignmentShift;
140 |             } else {
141 |                 xPositions.left = previousPosition.right + expectedAlignmentShift;
142 |             }
143 |         }
144 |     }
145 |     return xPositions;
146 | }
147 | 
148 | function fixPositionsAndReturnSmallestWidth(
149 |     positions: ColumnPosition[],
150 |     initialMinWidth: number
151 | ): number {
152 |     return positions.reduce((smallest: number, position: ColumnPosition) => {
153 |         if (position.right < position.left) {
154 |             position.right = position.left;
155 |         }
156 |         const width = position.right - position.left + 1;
157 |         return Math.min(smallest, width);
158 |     }, initialMinWidth);
159 | }
160 | 
161 | function fixAlignmentForNarrowColumns(
162 |     positions: ColumnPosition[],
163 |     minColumnWidth: number
164 | ) {
165 |     return positions.map((position: ColumnPosition) => {
166 |         const width = position.right - position.left + 1;
167 |         if (width <= minColumnWidth) return position;
168 |         if (position.shiftLeft) {
169 |             position.right -= 1;
170 |         } else {
171 |             position.left += 1;
172 |         }
173 |         return position;
174 |     });
175 | }
176 | 
177 | /**
178 |  * Calculates the column positions and widths for the x positions.
179 |  * This function creates a new array. You may get faster performance using the
180 |  * `calculateColumnPositionsInPlace` function instead
181 |  * @param xMediaPositions - x positions for the bars in media coordinates
182 |  * @param barSpacingMedia - spacing between bars in media coordinates
183 |  * @param horizontalPixelRatio - horizontal pixel ratio
184 |  * @returns Positions for the columns
185 |  */
186 | export function calculateColumnPositions(
187 |     xMediaPositions: number[],
188 |     barSpacingMedia: number,
189 |     horizontalPixelRatio: number
190 | ): ColumnPosition[] {
191 |     const common = columnCommon(barSpacingMedia, horizontalPixelRatio);
192 |     const positions = new Array<ColumnPosition>(xMediaPositions.length);
193 |     let previous: ColumnPosition | undefined = undefined;
194 |     for (let i = 0; i < xMediaPositions.length; i++) {
195 |         positions[i] = calculateColumnPosition(
196 |             xMediaPositions[i],
197 |             common,
198 |             previous
199 |         );
200 |         previous = positions[i];
201 |     }
202 |     const initialMinWidth = Math.ceil(barSpacingMedia * horizontalPixelRatio);
203 |     const minColumnWidth = fixPositionsAndReturnSmallestWidth(
204 |         positions,
205 |         initialMinWidth
206 |     );
207 |     if (common.spacing > 0 && minColumnWidth < alignToMinimalWidthLimit) {
208 |         return fixAlignmentForNarrowColumns(positions, minColumnWidth);
209 |     }
210 |     return positions;
211 | }
212 | 
213 | export interface ColumnPositionItem {
214 |     x: number;
215 |     column?: ColumnPosition;
216 | }
217 | 
218 | /**
219 |  * Calculates the column positions and widths for bars using the existing
220 |  * array of items.
221 |  * @param items - bar items which include an `x` property, and will be mutated to contain a column property
222 |  * @param barSpacingMedia - bar spacing in media coordinates
223 |  * @param horizontalPixelRatio - horizontal pixel ratio
224 |  * @param startIndex - start index for visible bars within the items array
225 |  * @param endIndex - end index for visible bars within the items array
226 |  */
227 | export function calculateColumnPositionsInPlace(
228 |     items: ColumnPositionItem[],
229 |     barSpacingMedia: number,
230 |     horizontalPixelRatio: number,
231 |     startIndex: number,
232 |     endIndex: number
233 | ): void {
234 |     const common = columnCommon(barSpacingMedia, horizontalPixelRatio);
235 |     let previous: ColumnPosition | undefined = undefined;
236 |     for (let i = startIndex; i < Math.min(endIndex, items.length); i++) {
237 |         items[i].column = calculateColumnPosition(items[i].x, common, previous);
238 |         previous = items[i].column;
239 |     }
240 |     const minColumnWidth = (items as ColumnPositionItem[]).reduce(
241 |         (smallest: number, item: ColumnPositionItem, index: number) => {
242 |             if (!item.column || index < startIndex || index > endIndex)
243 |                 return smallest;
244 |             if (item.column.right < item.column.left) {
245 |                 item.column.right = item.column.left;
246 |             }
247 |             const width = item.column.right - item.column.left + 1;
248 |             return Math.min(smallest, width);
249 |         },
250 |         Math.ceil(barSpacingMedia * horizontalPixelRatio)
251 |     );
252 |     if (common.spacing > 0 && minColumnWidth < alignToMinimalWidthLimit) {
253 |         (items as ColumnPositionItem[]).forEach(
254 |             (item: ColumnPositionItem, index: number) => {
255 |                 if (!item.column || index < startIndex || index > endIndex) return;
256 |                 const width = item.column.right - item.column.left + 1;
257 |                 if (width <= minColumnWidth) return item;
258 |                 if (item.column.shiftLeft) {
259 |                     item.column.right -= 1;
260 |                 } else {
261 |                     item.column.left += 1;
262 |                 }
263 |                 return item.column;
264 |             }
265 |         );
266 |     }
267 | }
268 | 
269 | ```
270 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/plugins/pixel-perfect-rendering/widths/crosshair.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 0
 3 | sidebar_label: Crosshair
 4 | pagination_title: Crosshair Widths
 5 | title: Crosshair and Grid Line Width Calculations
 6 | description: Describes the calculation for the crosshair line and grid line widths
 7 | keywords:
 8 |   - plugins
 9 |   - extensions
10 |   - rendering
11 |   - canvas
12 |   - bitmap
13 |   - media
14 |   - pixels
15 |   - crosshair
16 |   - grid
17 |   - line
18 |   - width
19 | ---
20 | 
21 | :::tip
22 | 
23 | It is recommend that you first read the [Pixel Perfect Rendering](../index.md) page.
24 | 
25 | :::
26 | 
27 | The following functions can be used to get the calculated width that the library would use for a crosshair or grid line at a specific device pixel ratio.
28 | 
29 | ```typescript
30 | /**
31 |  * Default grid / crosshair line width in Bitmap sizing
32 |  * @param horizontalPixelRatio - horizontal pixel ratio
33 |  * @returns default grid / crosshair line width in Bitmap sizing
34 |  */
35 | export function gridAndCrosshairBitmapWidth(
36 |     horizontalPixelRatio: number
37 | ): number {
38 |     return Math.max(1, Math.floor(horizontalPixelRatio));
39 | }
40 | 
41 | /**
42 |  * Default grid / crosshair line width in Media sizing
43 |  * @param horizontalPixelRatio - horizontal pixel ratio
44 |  * @returns default grid / crosshair line width in Media sizing
45 |  */
46 | export function gridAndCrosshairMediaWidth(
47 |     horizontalPixelRatio: number
48 | ): number {
49 |     return (
50 |         gridAndCrosshairBitmapWidth(horizontalPixelRatio) / horizontalPixelRatio
51 |     );
52 | }
53 | 
54 | ```
55 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/plugins/pixel-perfect-rendering/widths/full-bar-width.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 0
 3 | sidebar_label: Full Bar Width
 4 | pagination_title: Full Bar Width
 5 | title: Full Bar Width Calculations
 6 | description: Describes the calculation for full bar widths
 7 | keywords:
 8 |   - plugins
 9 |   - extensions
10 |   - rendering
11 |   - canvas
12 |   - bitmap
13 |   - media
14 |   - pixels
15 |   - histogram
16 |   - column
17 |   - width
18 | ---
19 | 
20 | :::tip
21 | 
22 | It is recommend that you first read the [Pixel Perfect Rendering](../index.md) page.
23 | 
24 | :::
25 | 
26 | The following functions can be used to get the calculated width that the library would use for the full width of a bar (data point) at a specific bar spacing and device pixel ratio. This can be used when you would like to use the full width available for each data point on the x axis, and don't want any gaps to be visible.
27 | 
28 | ```typescript
29 | interface BitmapPositionLength {
30 |     /** coordinate for use with a bitmap rendering scope */
31 |     position: number;
32 |     /** length for use with a bitmap rendering scope */
33 |     length: number;
34 | }
35 | 
36 | /**
37 |  * Calculates the position and width which will completely full the space for the bar.
38 |  * Useful if you want to draw something that will not have any gaps between surrounding bars.
39 |  * @param xMedia - x coordinate of the bar defined in media sizing
40 |  * @param halfBarSpacingMedia - half the width of the current barSpacing (un-rounded)
41 |  * @param horizontalPixelRatio - horizontal pixel ratio
42 |  * @returns position and width which will completely full the space for the bar
43 |  */
44 | export function fullBarWidth(
45 |     xMedia: number,
46 |     halfBarSpacingMedia: number,
47 |     horizontalPixelRatio: number
48 | ): BitmapPositionLength {
49 |     const fullWidthLeftMedia = xMedia - halfBarSpacingMedia;
50 |     const fullWidthRightMedia = xMedia + halfBarSpacingMedia;
51 |     const fullWidthLeftBitmap = Math.round(
52 |         fullWidthLeftMedia * horizontalPixelRatio
53 |     );
54 |     const fullWidthRightBitmap = Math.round(
55 |         fullWidthRightMedia * horizontalPixelRatio
56 |     );
57 |     const fullWidthBitmap = fullWidthRightBitmap - fullWidthLeftBitmap;
58 |     return {
59 |         position: fullWidthLeftBitmap,
60 |         length: fullWidthBitmap,
61 |     };
62 | }
63 | ```
64 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/plugins/series-primitives.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_label: Series Primitives
  3 | sidebar_position: 1
  4 | ---
  5 | 
  6 | # Series Primitives
  7 | 
  8 | Primitives are extensions to the series which can define views and renderers to
  9 | draw on the chart using
 10 | [CanvasRenderingContext2D](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D).
 11 | 
 12 | Primitives are defined by implementing the
 13 | [`ISeriesPrimitive`](../api/type-aliases/ISeriesPrimitive.md) interface. The
 14 | interface defines the basic functionality and structure required for creating
 15 | custom primitives.
 16 | 
 17 | ## Views
 18 | 
 19 | The primary purpose of a series primitive is to provide one, or more, views to
 20 | the library which contain the state and logic required to draw on the chart
 21 | panes.
 22 | 
 23 | There are two types of views which are supported within `ISeriesPrimitive` which
 24 | are:
 25 | 
 26 | - [`IPrimitivePaneView`](../api/interfaces/IPrimitivePaneView.md)
 27 | - [`ISeriesPrimitiveAxisView`](../api/interfaces/ISeriesPrimitiveAxisView.md)
 28 | 
 29 | The library will evoke the following getter functions (if defined) to get
 30 | references to the primitive's defined views for the corresponding section of the
 31 | chart:
 32 | 
 33 | - [`paneViews`](../api/interfaces/ISeriesPrimitiveBase.md#paneviews)
 34 | - [`priceAxisPaneViews`](../api/interfaces/ISeriesPrimitiveBase.md#priceaxispaneviews)
 35 | - [`timeAxisPaneViews`](../api/interfaces/ISeriesPrimitiveBase.md#timeaxispaneviews)
 36 | - [`priceAxisViews`](../api/interfaces/ISeriesPrimitiveBase.md#priceaxisviews)
 37 | - [`timeAxisViews`](../api/interfaces/ISeriesPrimitiveBase.md#timeaxisviews)
 38 | 
 39 | The first three views allow drawing on the corresponding panes (main chart pane,
 40 | price scale pane, and horizontal time scale pane) using the
 41 | [CanvasRenderingContext2D](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D)
 42 | and should implement the `ISeriesPrimitivePaneView` interface.
 43 | 
 44 | The views returned by the `priceAxisViews` and `timeAxisViews` getter methods
 45 | should implement the `ISeriesPrimitiveAxisView` interface and are used to define
 46 | labels to be drawn on the corresponding scales.
 47 | 
 48 | Below is a visual example showing the various sections of the chart where a
 49 | Primitive can draw.
 50 | 
 51 | import CodeBlock from '@theme/CodeBlock';
 52 | import sectionsExplainerCode from '!!raw-loader!./explainer-sections-demo.js';
 53 | 
 54 | <CodeBlock replaceThemeConstants chart className="language-js" chartOnly>
 55 | 	{sectionsExplainerCode}
 56 | </CodeBlock>
 57 | 
 58 | ### IPrimitivePaneView
 59 | 
 60 | The [`IPrimitivePaneView`](../api/interfaces/IPrimitivePaneView.md)
 61 | interface can be used to define a view which provides a renderer (implementing
 62 | the
 63 | [`IPrimitivePaneRenderer`](../api/interfaces/IPrimitivePaneRenderer.md)
 64 | interface) for drawing on the corresponding area of the chart using the
 65 | [CanvasRenderingContext2D](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D)
 66 | API. The view can define a
 67 | [`zOrder`](../api/interfaces/IPrimitivePaneView.md#zorder) to control where
 68 | in the visual stack the drawing will occur (See
 69 | [`PrimitivePaneViewZOrder`](../api/type-aliases/PrimitivePaneViewZOrder.md)
 70 | for more information).
 71 | 
 72 | Renderers should provide a
 73 | [`draw`](../api/interfaces/IPrimitivePaneRenderer.md#draw) method which will
 74 | be given a `CanvasRenderingTarget2D` target on which it can draw. Additionally,
 75 | a renderer can optionally provide a
 76 | [`drawBackground`](../api/interfaces/IPrimitivePaneRenderer.md#drawbackground)
 77 | method for drawing beneath other elements on the same zOrder.
 78 | 
 79 | :::tip
 80 | 
 81 | `CanvasRenderingTarget2D` is explained in more detail on the [Canvas Rendering Target](./canvas-rendering-target) page.
 82 | 
 83 | :::
 84 | 
 85 | #### Interactive Demo of zOrder layers
 86 | 
 87 | Below is an interactive demo chart illustrating where each zOrder is drawn
 88 | relative to the existing chart elements such as the grid, series, and crosshair.
 89 | 
 90 | import layersExplainerCode from '!!raw-loader!./explainer-layers-demo.js';
 91 | 
 92 | <CodeBlock replaceThemeConstants chart className="language-js" chartOnly>
 93 | 	{layersExplainerCode}
 94 | </CodeBlock>
 95 | 
 96 | ### ISeriesPrimitiveAxisView
 97 | 
 98 | The [`ISeriesPrimitiveAxisView`](../api/interfaces/ISeriesPrimitiveAxisView.md)
 99 | interface can be used to define a label on the price or time axis.
100 | 
101 | This interface provides several methods to define the appearance and position of
102 | the label, such as the
103 | [`coordinate`](../api/interfaces/ISeriesPrimitiveAxisView.md#coordinate) method,
104 | which should return the desired coordinate for the label on the axis. It also
105 | defines optional methods to set the fixed coordinate, text, text color,
106 | background color, and visibility of the label.
107 | 
108 | Please see the
109 | [`ISeriesPrimitiveAxisView`](../api/interfaces/ISeriesPrimitiveAxisView.md)
110 | interface for more details.
111 | 
112 | ## Lifecycle Methods
113 | 
114 | Your primitive can use the
115 | [`attached`](../api/interfaces/ISeriesPrimitiveBase.md#attached) and
116 | [`detached`](../api/interfaces/ISeriesPrimitiveBase.md#detached) lifecycle methods to
117 | manage the lifecycle of the primitive, such as creating or removing external
118 | objects and event handlers.
119 | 
120 | ### attached
121 | 
122 | This method is called when the primitive is attached to a chart. The attached
123 | method is evoked with a
124 | [single argument](../api/interfaces/SeriesAttachedParameter.md) containing
125 | properties for the chart, series, and a callback to request an update. The
126 | `chart` and `series` properties are references to the chart API and the series
127 | API instances for convenience purposes so that they don't need to be manually
128 | provided within the primitive's constructor (if needed by the primitive).
129 | 
130 | The `requestUpdate` callback allows the primitive to notify the chart that it
131 | should be updated and redrawn.
132 | 
133 | ### detached
134 | 
135 | This method is called when the primitive is detached from a chart. This can be
136 | used to remove any external objects or event handlers that were created during
137 | the attached lifecycle method.
138 | 
139 | ## Updating Views
140 | 
141 | Your primitive should update the views in the
142 | [`updateAllViews()`](../api/interfaces/ISeriesPrimitiveBase.md#updateallviews) method
143 | such that when the renderers are evoked, they can draw with the latest
144 | information. The library invokes this method when it wants to update and redraw
145 | the chart. If you would like to notify the library that it should trigger an
146 | update then you can use the `requestUpdate` callback provided by the attached
147 | lifecycle method.
148 | 
149 | ## Extending the Autoscale Info
150 | 
151 | The [`autoscaleInfo()`](../api/interfaces/ISeriesPrimitiveBase.md#autoscaleinfo)
152 | method can be provided to extend the base autoScale information of the series.
153 | This can be used to ensure that the chart is automatically scaled correctly to
154 | include all the graphics drawn by the primitive.
155 | 
156 | Whenever the chart needs to calculate the vertical visible range of the series
157 | within the current time range then it will evoke this method. This method can be
158 | omitted and the library will use the normal autoscale information for the
159 | series. If the method is implemented then the returned values will be merged
160 | with the base autoscale information to define the vertical visible range.
161 | 
162 | :::warning
163 | 
164 | Please note that this method will be evoked very often during
165 | scrolling and zooming of the chart, thus it is recommended that this method is
166 | either simple to execute, or makes use of optimisations such as caching to
167 | ensure that the chart remains responsive.
168 | 
169 | :::
170 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/price-scale.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 3
 3 | ---
 4 | 
 5 | # Price scale
 6 | 
 7 | Price Scale (or price axis) is a vertical scale that mostly maps prices to coordinates and vice versa.
 8 | The rules of converting depend on a price scale mode, a height of the chart and visible part of the data.
 9 | 
10 | ![Price scales](/img/price-scales.png "Price scales")
11 | 
12 | By default, chart has 2 predefined price scales: `left` and `right`, and an unlimited number of overlay scales.
13 | 
14 | Only `left` and `right` price scales could be displayed on the chart, all overlay scales are hidden.
15 | 
16 | If you want to change `left` price scale, you need to use [`leftPriceScale`](/api/interfaces/ChartOptionsBase.md#leftpricescale) option, to change `right` price scale use [`rightPriceScale`](/api/interfaces/ChartOptionsBase.md#rightpricescale), to change default options for an overlay price scale use [`overlayPriceScales`](/api/interfaces/ChartOptionsBase.md#overlaypricescales) option.
17 | 
18 | Alternatively, you can use [`IChartApi.priceScale`](/api/interfaces/IChartApi.md#pricescale) method to get an API object of any price scale or [`ISeriesApi.priceScale`](/api/interfaces/ISeriesApi.md#pricescale) to get an API object of series' price scale (the price scale that the series is attached to).
19 | 
20 | ## Creating a price scale
21 | 
22 | By default a chart has only 2 price scales: `left` and `right`.
23 | 
24 | If you want to create an overlay price scale, you can simply assign [`priceScaleId`](/api/interfaces/SeriesOptionsCommon.md#pricescaleid) option to a series (note that a value should be differ from `left` and `right`) and a chart will automatically create an overlay price scale with provided ID.
25 | If a price scale with such ID already exists then a series will be attached to this existing price scale.
26 | Further you can use provided price scale ID to get its corresponding API object via [`IChartApi.priceScale`](/api/interfaces/IChartApi.md#pricescale) method.
27 | 
28 | ## Removing a price scale
29 | 
30 | The default price scales (`left` and `right`) cannot be removed, you can only hide them by setting [`visible`](/api/interfaces/PriceScaleOptions.md#visible) option to `false`.
31 | 
32 | An overlay price scale exists while there is at least 1 series attached to this price scale.
33 | Thus, to remove an overlay price scale remove all series attached to this price scale.
34 | 
35 | <!-- Note that this method is not implemented yet :(
36 | ## Equality of price scale API objects
37 | 
38 | `lightweight-charts` library does not guarantee to return the same reference of [`IPriceScaleApi`](/api/interfaces/IPriceScaleApi.md) object for the same price scale ID.
39 | So you should never compare these objects by a reference, use the result from [`IPriceScaleApi.id`](/api/interfaces/IPriceScaleApi.md#id) method instead.
40 | -->
41 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/release-notes.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | title: Release Notes
  3 | description: List of changes made for each release of the library.
  4 | keywords:
  5 |     - charts
  6 |     - changelog
  7 |     - canvas
  8 |     - charting library
  9 |     - charting
 10 |     - html5 charts
 11 |     - financial charting library
 12 | sidebar_position: 9
 13 | toc_min_heading_level: 2
 14 | toc_max_heading_level: 2
 15 | ---
 16 | 
 17 | <!-- markdownlint-disable no-emphasis-as-heading -->
 18 | <!-- ^ using emphasis as headings so we don't have duplicate headers -->
 19 | ## 5.0.8
 20 | 
 21 | **Enhancements**
 22 | 
 23 | - Improved pane API with several new methods and options:
 24 |   - Added `addDefaultPane` option to chart options, allowing creation of charts with no initial panes
 25 |   - Added `addPane` method to `IChartApi` for programmatically adding panes
 26 |   - Added `setPreserveEmptyPane` and `preserveEmptyPane` methods to control empty pane behavior
 27 |   - Added `getStretchFactor` and `setStretchFactor` methods to control relative pane sizes
 28 |   - Added `addCustomSeries` and `addSeries` methods to `IPaneApi` for creating series directly on a specific pane
 29 |   - Updated `getHTMLElement` to return `null` when a pane hasn't been created yet
 30 |   - These improvements provide greater flexibility when working with multi-pane charts
 31 |   (PR [#1894](https://github.com/tradingview/lightweight-charts/pull/1894), fixes [#1898](https://github.com/tradingview/lightweight-charts/issues/1898), [#1896](https://github.com/tradingview/lightweight-charts/issues/1896), [#1872](https://github.com/tradingview/lightweight-charts/issues/1872), [#1907](https://github.com/tradingview/lightweight-charts/issues/1907))
 32 | - Added additional price scale tick mark formatting capabilities:
 33 |   - Added `formatTickmarks` method to `IPriceFormatter` interface
 34 |   - Added `tickmarksPriceFormatter` and `tickmarksPercentageFormatter` options to `LocalizationOptionsBase`
 35 |   - Added `tickmarksFormatter` option to `PriceFormatCustom`
 36 |   - These new formatters provide all tick mark values at once, allowing for context-aware formatting decisions such as determining the optimal precision level needed
 37 |   (PR [#1903](https://github.com/tradingview/lightweight-charts/pull/1903))
 38 | 
 39 | [Changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v5.0.7..v5.0.8).
 40 | 
 41 | ## 5.0.7
 42 | 
 43 | **Enhancements**
 44 | 
 45 | - Added price scale visible range control with new methods in `IPriceScaleApi`: `setVisibleRange(range)`, `getVisibleRange()`, and `setAutoScale(on)`. These methods allow for programmatic control of the visible price range on a price scale. Also added `ensureEdgeTickMarksVisible` option to `PriceScaleOptions`, which ensures tick marks are always visible at the very top and bottom of the price scale, providing clear boundary indicators. These features are particularly useful for charts with zooming and panning disabled that are primarily for display purposes. (PR [#1856](https://github.com/tradingview/lightweight-charts/pull/1856))
 46 | - Added control over the rendering stacking order of series markers through a new `zOrder` option in the series markers plugin. This enhancement provides greater flexibility in controlling marker visibility and layering in complex charts. (PR [#1876](https://github.com/tradingview/lightweight-charts/pull/1876)).
 47 | 
 48 | [Changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v5.0.6..v5.0.7).
 49 | 
 50 | ## 5.0.6
 51 | 
 52 | **Enhancements**
 53 | 
 54 | - Implemented series order functionality, allowing control over the rendering order of series within a pane. Series with higher order values are rendered on top of those with lower values. Added two new methods to `ISeriesApi`: `seriesOrder()` to get the current order index and `setSeriesOrder(order)` to set a specific order. (PR [#1868](https://github.com/tradingview/lightweight-charts/pull/1868))
 55 | 
 56 | [Changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v5.0.5..v5.0.6).
 57 | 
 58 | ## 5.0.5
 59 | 
 60 | **Bug Fixes**
 61 | 
 62 | - Fixed an issue where the series marker plugin could throw an exception if the series data required for individual markers could not be found (such as when the data is cleared or changed via ⁠setData on the series). (PR [#1845](https://github.com/tradingview/lightweight-charts/pull/1845))
 63 | 
 64 | [Changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v5.0.4..v5.0.5).
 65 | 
 66 | ## 5.0.4
 67 | 
 68 | **Improvements**
 69 | 
 70 | - Fixed performance degradation when adding series markers to charts with large datasets (15,000+ data points) by optimizing marker calculations to only run when necessary. (PR [#1835](https://github.com/tradingview/lightweight-charts/pull/1835), fixes [#1808](https://github.com/tradingview/lightweight-charts/issues/1808))
 71 | - Added price-based positioning for series markers, allowing more precise control over marker placement. New position types include `atPriceTop`, `atPriceBottom`, and `atPriceMiddle`, which require a `price` value to be specified. (PR [#1826](https://github.com/tradingview/lightweight-charts/pull/1826), thanks to [@EranGrin](https://github.com/EranGrin))
 72 | - Added `MagnetOHLC` to `CrosshairMode`. This mode sticks the crosshair's horizontal line to the price value of a single-value series or to the open/high/low/close price of OHLC-based series. (PR [#1831](https://github.com/tradingview/lightweight-charts/pull/1831), thanks to [@Jonney](https://github.com/Jonney))
 73 | 
 74 | **Bug Fixes**
 75 | 
 76 | - Fixed an issue where the crosshair marker would be visible on the first data point when the chart is initially loaded, before any user interaction. This behavior has been reverted to match version 4, where the crosshair remains hidden until user interaction. (PR [#1840](https://github.com/tradingview/lightweight-charts/pull/1840))
 77 | 
 78 | [Changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v5.0.3..v5.0.4).
 79 | 
 80 | ## 5.0.3
 81 | 
 82 | **Bug Fixes**
 83 | 
 84 | - Fixed an issue where changing the price scale for one pane would impact all panes in multi-pane setups. Added pane index parameter to the price scale API to ensure changes only affect the intended pane. (PR [#1821](https://github.com/tradingview/lightweight-charts/pull/1821), fixes [#1817](https://github.com/tradingview/lightweight-charts/issues/1817))
 85 | - Fixed an issue where a cursorStyle defined in a primitive hit-test wouldn't be applied. Additionally improved cursor style handling to maintain the correct cursor when the mouse remains in the same position while price/time scales are adjusted. (PR [#1823](https://github.com/tradingview/lightweight-charts/pull/1823))
 86 | 
 87 | [Changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v5.0.2..v5.0.3).
 88 | 
 89 | ## 5.0.2
 90 | 
 91 | **Bug Fixes**
 92 | 
 93 | - Fixed an issue where the crosshair marker would remain visible after the mouse pointer has left the chart. (PR [#1807](https://github.com/tradingview/lightweight-charts/issues/1807))
 94 | 
 95 | [Changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v5.0.1..v5.0.2).
 96 | 
 97 | ---
 98 | 
 99 | ## 5.0.0
100 | 
101 | Version 5.0.0 represents a significant milestone in the evolution of Lightweight Charts™, delivering on our commitment to keep the library truly "lightweight". Despite adding numerous new features, improvements, and fixes, we've managed to reduce the bundle size by up to 16%, bringing the base bundle size down to just 35kB. This remarkable reduction was achieved through enhanced tree-shaking capabilities, modernized architecture, and careful optimization of core features.
102 | 
103 | This release introduces highly requested features like multi-pane support and new chart types. It also modernizes the codebase and improves its architecture to set a foundation for future enhancements without compromising on size.
104 | 
105 | ### Major Updates
106 | 
107 | #### Multi-Pane Support
108 | 
109 | One of our most requested features, multi-pane support is now available. It allows you to create complex chart layouts with multiple independent viewing areas. This enhancement enables sophisticated technical analysis setups and better visualization of related data series. Additional key benefits include:
110 | 
111 | - Full support for multiple panes within a single chart
112 | - Independent scale and series management per pane
113 | - Flexible pane sizing and arrangement options
114 | 
115 | See [Panes](./panes.md) for more information.
116 | 
117 | #### New Chart Types
118 | 
119 | **Yield Curve Charts**
120 | 
121 | - New specialized chart type for displaying yield curves
122 | - Custom horizontal scale behavior with linear spacing
123 | - Optimized whitespace handling
124 | 
125 | **Options Charts**
126 | 
127 | - Price-based horizontal scale support
128 | - Specialized formatting and interaction handling
129 | - Ideal for options chain visualization
130 | 
131 | See [Chart types](./chart-types.mdx) for more information about the [Yield Curve Chart](./chart-types.mdx#yield-curve-chart) and [Options Chart](./chart-types.mdx#options-chart-price-based) types.
132 | 
133 | #### Enhanced Color Support
134 | 
135 | - Expanded native support for sRGB-based colors (RGB, RGBA, hex, named colors, HSL)
136 | - Support for expanded color gamuts like Display P3
137 | - Ability to specify a custom color parser to add support for non-sRGB formats
138 | - Reduced bundle size through browser-native color parsing
139 | 
140 | #### Architectural Improvements
141 | 
142 | - Watermark feature reimplemented as plugins (`TextWatermark` and `ImageWatermark`)
143 | - Series Markers extracted as a plugin for better tree-shaking
144 | - New Up/Down Markers Plugin for price change visualization
145 | - Introduction of Pane Primitives for plugin attachment
146 | 
147 | ### Breaking Changes
148 | 
149 | - New unified series creation API (see [migration guide](./migrations/from-v4-to-v5.md))
150 | - Dropped CommonJS support and updated JS syntax version to ES2020
151 | - Watermark functionality moved to plugins
152 | - Series markers implementation changed to plugin system
153 | 
154 | ### Enhancements
155 | 
156 | - Added relative gradient option for baseline and area series (`relativeGradient`)
157 | - New time scale option for maximum bar spacing (`maxBarSpacing`)
158 | - Added `priceLines()` method to `ISeriesApi` interface
159 | - Enhanced watermark capabilities with multi-line text support
160 | - Improved plugin system with Pane Primitives support
161 | - Better tree-shaking capabilities for smaller bundle sizes
162 | 
163 | ### Bug Fixes
164 | 
165 | - Fixed primitive detachment update issues ([#1594](https://github.com/tradingview/lightweight-charts/issues/1594))
166 | - Various performance and rendering improvements
167 | 
168 | ### Migration Guide
169 | 
170 | We've prepared a comprehensive migration guide to help you upgrade from v4 to v5. Key areas to note:
171 | 
172 | 1. Series Creation API changes
173 | 2. Watermarks and Series Markers moving to separate plugins
174 | 3. Plugin system updates
175 | 
176 | See the full migration guide: [Migrating from v4 to v5](./migrations/from-v4-to-v5.md)
177 | 
178 | ### Technical Notes
179 | 
180 | This release uses ES2020 syntax and no longer supports CommonJS. If you need to support older environments, you'll need to set up transpilation for the `lightweight-charts` package in your build system using tools like Babel.
181 | 
182 | As always, we thank you for your support and help in making Lightweight Charts™ the best product on the financial web. We look forward to seeing what you build with these new capabilities!
183 | 
184 | You can always send us your feedback via GitHub.
185 | Happy trading!
186 | 
187 | Team TradingView
188 | 
189 | See [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v4.2.3..v5.0.1).
190 | 
191 | ---
192 | 
193 | ## 4.2.3
194 | 
195 | **Minor Improvements**
196 | 
197 | - Improve check for crosshair label visibility on the price scale. This improves upon previous work (#1743 in v4.2.2) by reducing the allocated space for the crosshair when it is enabled, but the label is disabled. (PR [#1757](https://github.com/tradingview/lightweight-charts/issues/1757))
198 | 
199 | **Bug Fixes**
200 | 
201 | - Added additional prototype pollution protection for internal merge helper function. (PR [#1758](https://github.com/tradingview/lightweight-charts/issues/1758))
202 | 
203 | [Changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v4.2.2..v4.2.3).
204 | 
205 | ---
206 | 
207 | ## 4.2.2
208 | 
209 | **Minor Improvements**
210 | 
211 | - Improved price scale width calculation by not allocating space for crosshair labels when the crosshair is disabled. (PR [#1743](https://github.com/tradingview/lightweight-charts/issues/1743))
212 | 
213 | **Bug Fixes**
214 | 
215 | - Fixed calculations for `fixLeftEdge` and `fixRightEdge` on the first render when both are true and data is added to an initially empty chart. Fixes issue [#1356](https://github.com/tradingview/lightweight-charts/issues/1356). (PR [#1741](https://github.com/tradingview/lightweight-charts/issues/1741))
216 | 
217 | [Changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v4.2.1..v4.2.2).
218 | 
219 | ---
220 | 
221 | ## 4.2.1
222 | 
223 | **Bug Fixes**
224 | 
225 | - Fixed an issue where the series title part of a price scale label appeared blurry when using Firefox.
226 | 
227 | [Changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v4.2.0..v4.2.1).
228 | 
229 | ---
230 | 
231 | ## 4.2.0
232 | 
233 | **Enhancements**
234 | 
235 | - Added new [`attributionLogo`](https://tradingview.github.io/lightweight-charts/docs/api/interfaces/LayoutOptions#attributionLogo) option to `LayoutOptions`. This feature displays the TradingView attribution logo on the main chart pane by default, helping users meet the library's licensing requirements for attribution.
236 |   - The TradingView attribution logo can be easily hidden by setting the `attributionLogo` option to `false` in the chart's `layout` option.
237 | - Improved data validation for `OhlcData` and `SingleValueData`. Introduced `isFulfilledBarData` for `OhlcData` and `isFulfilledLineData` for `SingleValueData`, ensuring more accurate validation of data types. Contributed by [@mozeryansky](https://github.com/mozeryansky) (PR [#1579](https://github.com/tradingview/lightweight-charts/pull/1579), fixes [#1526](https://github.com/tradingview/lightweight-charts/issues/1526)).
238 | 
239 | [Changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v4.1.7..v4.2.0).
240 | 
241 | ---
242 | 
243 | ## 4.1.7
244 | 
245 | **Enhancements**
246 | 
247 | - Further Refinement of the Price Scale Label Alignment (PR [#1630](https://github.com/tradingview/lightweight-charts/pull/1630))
248 | 
249 | [Changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v4.1.6..v4.1.7).
250 | 
251 | ---
252 | 
253 | ## 4.1.6
254 | 
255 | **Enhancements**
256 | 
257 | - Improved Price Scale Label Alignment: Enhanced the alignment algorithm for price scale labels to ensure they do not move out of the viewport. This improves the visibility of price labels, particularly when they are near the edges of the scale. Fixes [#1620](https://github.com/tradingview/lightweight-charts/issues/1620) (PR [#1621](https://github.com/tradingview/lightweight-charts/pull/1621))
258 | 
259 | [Changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v4.1.5..v4.1.6).
260 | 
261 | ---
262 | 
263 | ## 4.1.5
264 | 
265 | **Enhancements**
266 | 
267 | - Added `IHorzScaleBehavior.shouldResetTickmarkLabels`. (PR [#1614](https://github.com/tradingview/lightweight-charts/pull/1614))
268 | 
269 | [Changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v4.1.4..v4.1.5).
270 | 
271 | ---
272 | 
273 | ## 4.1.4
274 | 
275 | **Bug Fixes**
276 | 
277 | - Fixed hoveredSeries being undefined during series removal and creation. (PR [#1529](https://github.com/tradingview/lightweight-charts/pull/1529), fixes [#1406](https://github.com/tradingview/lightweight-charts/pull/1406), fixes [#1499](https://github.com/tradingview/lightweight-charts/pull/1499))
278 | - Fixed price label rendering artefact. (PR [#1585](https://github.com/tradingview/lightweight-charts/pull/1585), fixes [#1584](https://github.com/tradingview/lightweight-charts/pull/1584))
279 | - Fixed an issue that prevented primitives with `zOrder` set to `top` from drawing above the last price animation. (PR [#1576](https://github.com/tradingview/lightweight-charts/pull/1576))
280 | - Fixed possible ReDos. (PR [#1536](https://github.com/tradingview/lightweight-charts/pull/1536))
281 | - Fixed marker positioning, which could cause a space between histogram and bottom of the chart. (PR [#1538](https://github.com/tradingview/lightweight-charts/pull/1538) & [#1539](https://github.com/tradingview/lightweight-charts/pull/1539), fixes [#1382](https://github.com/tradingview/lightweight-charts/pull/1382))
282 | 
283 | [Changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v4.1.3..v4.1.4).
284 | 
285 | ---
286 | 
287 | ## 4.1.3
288 | 
289 | **Minor Improvements**
290 | 
291 | - Added option to disable bold labels in the time scale. (PR [#1510](https://github.com/tradingview/lightweight-charts/pull/1510))
292 | 
293 | **Bug Fixes**
294 | 
295 | - Fixed sub-pixel horizontal alignment of the crosshair marker and series markers. (PR [#1505](https://github.com/tradingview/lightweight-charts/pull/1505), fixes [#1504](https://github.com/tradingview/lightweight-charts/issues/1504))
296 | 
297 | [Changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v4.1.2..v4.1.3).
298 | 
299 | ---
300 | 
301 | ## 4.1.2
302 | 
303 | **Bug Fixes**
304 | 
305 | - Fix for 'Total canvas memory use exceeds the maximum limit' error raised on iOS Safari. (PR [#1485](https://github.com/tradingview/lightweight-charts/pull/1485))
306 | 
307 | **Minor Improvements**
308 | 
309 | - Improved error messages for price scale margins. (PR [#1489](https://github.com/tradingview/lightweight-charts/pull/1489))
310 | 
311 | [Changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v4.1.1..v4.1.2).
312 | 
313 | ---
314 | 
315 | ## 4.1.1
316 | 
317 | **Bug Fixes**
318 | 
319 | - Fixed `shiftVisibleRangeOnNewBar` behaviour for realtime updates to a series. Additionally, a new option `allowShiftVisibleRangeOnWhitespaceReplacement` has been added if you wish to have the old 4.0 behaviour for when new data replaces existing whitespace. (PR [#1444](https://github.com/tradingview/lightweight-charts/pull/1444))
320 | - When disabling touch scrolling on the chart via either the `vertTouchDrag` or `horzTouchDrag` setting in the `handleScroll` options, any touch scroll events over the corresponding scale will now be ignored so the page can be scrolled. (PR [#1445](https://github.com/tradingview/lightweight-charts/pull/1445))
321 | 
322 | [Changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v4.1.0..v4.1.1).
323 | 
324 | ---
325 | 
326 | ## 4.1.0
327 | 
328 | Version 4.1 of Lightweight Charts introduces exciting new features, including the introduction of Plugins, which provide developers the ability to extend the library's functionality. Additionally, this release includes enhancements to customize the horizontal scale and various minor improvements and bug fixes.
329 | 
330 | **Major Updates**
331 | 
332 | **Plugins**
333 | 
334 | Developers can now leverage the power of Plugins in Lightweight Charts. Two types of Plugins are supported -  [Custom Series](/plugins/intro.md#custom-series) and [Drawing Primitives](/plugins/intro.md#drawing-primitives), offering the ability to define new series types and create custom visualizations, drawing tools, and annotations.
335 | 
336 | With the flexibility provided by these plugins, developers can create highly customizable charting applications for their users.
337 | 
338 | To get started with plugins, please refer to our [Plugins Documentation](/plugins/intro.md) for a better understanding of what is possible and how plugins work. You can also explore our collection of [plugin examples](https://github.com/tradingview/lightweight-charts/tree/master/plugin-examples) (with a [preview hosted here](https://tradingview.github.io/lightweight-charts/plugin-examples/)) for inspiration and guidance on implementing specific functionality.
339 | 
340 | To help you get started quickly, we have created an NPM package called [create-lwc-plugin](https://www.npmjs.com/package/create-lwc-plugin), which sets up a plugin project for you. This way, you can hit the ground running with your plugin development.
341 | 
342 | **Horizontal Scale Customization**
343 | 
344 | The horizontal scale is no longer restricted to only time-based values. The API has been extended to allow customization of the horizontal scale behavior, and enable uses cases like options chart where price values are displayed in the horizontal scale. The most common use-case would be to customise the tick marks behaviour.
345 | 
346 | The [createChartEx](/api/functions/createChartEx.md) function should be used instead of the usual `createChart` function, and an instance of a class implementing [IHorzScaleBehavior](/api/interfaces/IHorzScaleBehavior.md) should be provided.
347 | 
348 | A simple example can be found in this test case: [horizontal-price-scale.js](https://github.com/tradingview/lightweight-charts/blob/master/tests/e2e/graphics/test-cases/horizontal-price-scale.js)
349 | 
350 | **Enhancements**
351 | 
352 | - Added point markers styling option for line-based series. (closes [#365](https://github.com/tradingview/lightweight-charts/issues/365)) [Docs](/api/interfaces/LineStyleOptions.md#pointmarkersvisible)
353 | - Added double click subscriber for the main chart pane. (closes [#1385](https://github.com/tradingview/lightweight-charts/issues/1385)) [Docs](/api/interfaces/IChartApi.md#subscribedblclick)
354 | - Added `setCrosshairPosition` API, allowing programmatic setting of the crosshair position. (fixes [#1198](https://github.com/tradingview/lightweight-charts/issues/1198), [#1163](https://github.com/tradingview/lightweight-charts/issues/1163), [#438](https://github.com/tradingview/lightweight-charts/issues/438)) [Docs](/api/interfaces/IChartApi.md#setcrosshairposition)
355 | - Added an option to disable crosshair. Introduced the `Hidden` option in the `CrosshairMode` setting. (closes [#749](https://github.com/tradingview/lightweight-charts/issues/749), thanks to [@luk707](https://github.com/luk707))
356 | - Allow overriding tick mark label length via the `tickMarkMaxCharacterLength` option. (closes [#1396](https://github.com/tradingview/lightweight-charts/issues/1396)) [Docs](/api/interfaces/HorzScaleOptions.md#tickmarkmaxcharacterlength)
357 | - Support for overriding the percentage formatter within the localization options. (fixes [#1328](https://github.com/tradingview/lightweight-charts/issues/1328), [#1291](https://github.com/tradingview/lightweight-charts/issues/1291)) [Docs](/api/interfaces/LocalizationOptions.md#percentageformatter)
358 | - Added `paneSize` getter to `IChartApi`, returning the dimensions of the chart pane. (issue [#1411](https://github.com/tradingview/lightweight-charts/issues/1411)) [Docs](/api/interfaces/IChartApi.md#panesize)
359 | - Added options to set minimum dimensions for the price and time scales. (closes [#1062](https://github.com/tradingview/lightweight-charts/issues/1062), related to [#1163](https://github.com/tradingview/lightweight-charts/issues/1163), [#50](https://github.com/tradingview/lightweight-charts/issues/50)) [Docs](/api/interfaces/TimeScaleOptions.md#minimumheight), [Docs](/api/interfaces/PriceScaleOptions.md#minimumwidth)
360 | 
361 | **Bug Fixes**
362 | 
363 | - Fixed chart layout when direction is set to RTL. (PR [#1338](https://github.com/tradingview/lightweight-charts/pull/1338))
364 | - Fixed re-enabling of `autoSize` after disabling it. (PR [#1274](https://github.com/tradingview/lightweight-charts/pull/1377))
365 | - Corrected percentage mode and zero first value. (fixes [#1386](https://github.com/tradingview/lightweight-charts/issues/1386))
366 | - Prevent chart shifting when new data replaces existing whitespace. (fixes [#1201](https://github.com/tradingview/lightweight-charts/issues/1201))
367 | 
368 | Thanks to our Contributors for this Release:
369 | 
370 | - [@luk707](https://github.com/luk707)
371 | 
372 | You can always send us your feedback via GitHub.
373 | We look forward to hearing from you! And as always, happy trading!
374 | 
375 | Team TradingView
376 | 
377 | See [issues assigned to this version's milestone](https://github.com/tradingview/lightweight-charts/milestone/24?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v4.0.1..v4.1.0).
378 | 
379 | ---
380 | 
381 | ## 4.0.1
382 | 
383 | **Enhancements**
384 | 
385 | - Add the ability to specify font colour for the Priceline labels. [#1274](https://github.com/tradingview/lightweight-charts/issues/1274) [#1287](https://github.com/tradingview/lightweight-charts/issues/1287)
386 | - Ignore resize method if `autoSize` is active, and added API to check if active. [#1301](https://github.com/tradingview/lightweight-charts/issues/1301)
387 | 
388 | **Bug fixes**
389 | 
390 | - Typo in customization guide. Thanks [@UcheAzubuko](https://github.com/UcheAzubuko). [#1284](https://github.com/tradingview/lightweight-charts/issues/1284)
391 | - Inability to immediately add markers when `autoSize` chart option is enabled. Thanks [@victorbrambati](https://github.com/victorbrambati). [#1271](https://github.com/tradingview/lightweight-charts/issues/1271) [#1281](https://github.com/tradingview/lightweight-charts/issues/1281)
392 | - First render when using `autosize` doesn't show the latest bars. Thanks [@victorbrambati](https://github.com/victorbrambati) [#1281](https://github.com/tradingview/lightweight-charts/issues/1281). [#1282](https://github.com/tradingview/lightweight-charts/issues/1282)
393 | - Series rendering bug when outside of visible range. [#1293](https://github.com/tradingview/lightweight-charts/issues/1293) [#1294](https://github.com/tradingview/lightweight-charts/issues/1294)
394 | - Auto contrast text color for crosshair labels. [#1309](https://github.com/tradingview/lightweight-charts/issues/1309) [#1310](https://github.com/tradingview/lightweight-charts/issues/1310)
395 | - Hit box from the text of marker incorrectly shifted to the right. [#1270](https://github.com/tradingview/lightweight-charts/issues/1270) [#1305](https://github.com/tradingview/lightweight-charts/issues/1305)
396 | 
397 | As always, we thank you for your support and help in making Lightweight Charts™ the best product on the financial web. And a big shout out to our hero contributors [@victorbrambati](https://github.com/victorbrambati), and [@UcheAzubuko](https://github.com/UcheAzubuko)!
398 | 
399 | You can always send us your feedback via GitHub.
400 | 
401 | We look forward to hearing from you! And as always, happy trading!
402 | Team TradingView
403 | 
404 | See [issues assigned to this version's milestone](https://github.com/tradingview/lightweight-charts/milestone/25?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v4.0.0..v4.0.1).
405 | 
406 | ---
407 | 
408 | ## 4.0.0
409 | 
410 | Long overdue as it’s been nearly 1 year since our last major update, but behold before all the changes that have happened over the last 12 months.
411 | 
412 | In total, more than 20 tickets have been addressed with one of the most important ones being **fancy-canvas** – the library we use to configure HTML canvas in Lightweight Charts™.
413 | 
414 | Please view the migration guide here: [Migrating from v3 to v4](./migrations/from-v3-to-v4).
415 | 
416 | **Breaking changes**
417 | 
418 | - Fancy-canvas 2 | [#818](https://github.com/tradingview/lightweight-charts/issues/818)
419 | - Added support for ES module exports | [#613](https://github.com/tradingview/lightweight-charts/issues/613)
420 | - We are now generating two more build types: esm, standalone & cjs
421 | - Updated scales design | [#606](https://github.com/tradingview/lightweight-charts/issues/606)
422 |   - Changed scales look & feel according to the new design
423 | - Add possibility to disable time axis ticks | [#1043](https://github.com/tradingview/lightweight-charts/issues/1043)
424 | - Added `ticksVisible` to `TimeScaleOptions`, renamed `drawTicks` to `ticksVisible` in `PriceScaleOptions`.
425 | - Custom price lines should be atop of the series | [#684](https://github.com/tradingview/lightweight-charts/issues/684)
426 |   - Price line to be added on top of any series - shout out to thanhlmm
427 | - Remove deprecated code | [#626](https://github.com/tradingview/lightweight-charts/issues/626)
428 | - Fix types inconsistency on API level with time | [#470](https://github.com/tradingview/lightweight-charts/issues/470)
429 | - Add API to get chart values (data, markers, etc) | [#414](https://github.com/tradingview/lightweight-charts/issues/414)
430 |   - Added methods:
431 |     - `ISeriesApi.markers`
432 |     - `ISeriesApi.dataByIndex`
433 |   - Changed time types everywhere in the public API to `Time`
434 | 
435 | **Enhancements**
436 | 
437 | - Handle resize with ResizeObserver if it's exist in window | [#71](https://github.com/tradingview/lightweight-charts/issues/71)
438 |   - There was an issue when resizing the chart (such as rotating the screen of a phone/tablet).
439 | - Add possibility to use default tick mark formatter implementation as a fallback | [#1210](https://github.com/tradingview/lightweight-charts/issues/1210)
440 |   - Allow the custom tick mark formatter to return null so that it will use the default formatter for that specific mark.
441 | - Add possibility to invert Area series filled area | [#1115](https://github.com/tradingview/lightweight-charts/issues/1115)
442 |   - Adds invertFilledArea property to the AreaStyleOptions which when set to true will invert the filled area (draw above the line instead of below it).
443 | - Documentation website improvements | [#1001](https://github.com/tradingview/lightweight-charts/issues/1001) [#1002](https://github.com/tradingview/lightweight-charts/issues/1002)
444 |   - Provides a way to apply theme-based colors to a chart whenever the Docusaurus theme is changed.
445 | - Add ability to draw parts of area with different colors | [#1100](https://github.com/tradingview/lightweight-charts/issues/1100)
446 |   - Add a possibility to change line, top and bottom colors for the different parts of an area series
447 | - Add possibility to change price axis text color | [#1114](https://github.com/tradingview/lightweight-charts/issues/1114)
448 | - Reset price and time scale double click options | [#1118](https://github.com/tradingview/lightweight-charts/issues/1118)
449 |   - Distinguishing the reset between price & time scale vs having only one option
450 | - Add curved lines | [#506](https://github.com/tradingview/lightweight-charts/issues/506)
451 |   - Add a new line type that draws curved lines between series points.
452 | 
453 | **Chores**
454 | 
455 | - Replace deprecated String.prototype.substr | [#1048](https://github.com/tradingview/lightweight-charts/issues/1048)
456 |   - Shout out to CommanderRoot
457 | 
458 | **Bug fixes**
459 | 
460 | - Refactoring resize the chart | [#367](https://github.com/tradingview/lightweight-charts/issues/367)
461 | - The chart is blank on printed page in Chromium | [#873](https://github.com/tradingview/lightweight-charts/issues/873)
462 |   - Chart was blank when printing
463 | - Horizontal scroll animations improvements | [#1136](https://github.com/tradingview/lightweight-charts/issues/1136)
464 |   - Fixes glitches when resetting the chart time scale while scrolling
465 | - Draw series last price & price line labels on the top layer | [#1046](https://github.com/tradingview/lightweight-charts/issues/1046)
466 |   - Fixes an issue where price line could be place over price scale labels
467 | - Incorrect price line labels formatting | [#1032](https://github.com/tradingview/lightweight-charts/issues/1032)
468 |   - When setting the price scale mode to anything than 'Normal' the price for PriceLine wasn't properly calculated.
469 | - lockVisibleTimeRangeOnResize does not work with fixLeftEdge | [#991](https://github.com/tradingview/lightweight-charts/issues/991)
470 |   - The visible range is no longer changed after resizing the chart.
471 | - Crosshair label text appears on the chart during initial render | [#1255](https://github.com/tradingview/lightweight-charts/issues/1255)
472 |   - Small text artefacts from the crosshair no longer appear on the time axis before any interaction with the chart.
473 | 
474 | As always, we thank you for your support and help in making Lightweight Charts™ the best product on the financial web. And a big shout out to our hero contributors [thanhlmm](https://github.com/thanhlmm), [CommanderRoot](https://github.com/CommanderRoot), [samhainsamhainsamhain](https://github.com/samhainsamhainsamhain) & colleague [Nipheris](https://github.com/Nipheris)!
475 | You can always send us your feedback via GitHub.
476 | We look forward to hearing from you! And as always, happy trading!
477 | Team TradingView
478 | 
479 | See [issues assigned to this version's milestone](https://github.com/tradingview/lightweight-charts/milestone/18?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v3.8.0..v4.0.0).
480 | 
481 | ---
482 | 
483 | ## 3.8.0
484 | 
485 | We're happy to announce the next release of Lightweight Charts™ library. This release includes many improvements and bug fixes (as usual), but we are thrilled to say that from this version the library has its own [documentation website](https://tradingview.github.io/lightweight-charts/) that replaces the documentation in the repository. Check it out and share your feedback in [this discussion thread](https://github.com/tradingview/lightweight-charts/discussions/921).
486 | 
487 | **Enhancement**
488 | 
489 | - Documentation website (see [#875](https://github.com/tradingview/lightweight-charts/issues/875), [#918](https://github.com/tradingview/lightweight-charts/issues/918), [#411](https://github.com/tradingview/lightweight-charts/issues/411), [#919](https://github.com/tradingview/lightweight-charts/issues/919), [#922](https://github.com/tradingview/lightweight-charts/issues/922), [#983](https://github.com/tradingview/lightweight-charts/issues/983), [#980](https://github.com/tradingview/lightweight-charts/issues/980), [#1006](https://github.com/tradingview/lightweight-charts/issues/1006))
490 | - Quick tracking mode (see [#830](https://github.com/tradingview/lightweight-charts/issues/830))
491 | - Improved mouse behaviour on touch devices (like mouse connected to mobile phone/tablet) (see [#106](https://github.com/tradingview/lightweight-charts/issues/106))
492 | - Custom color for items of candlestick and line series (see [#195](https://github.com/tradingview/lightweight-charts/issues/195))
493 | - Labels might be cut off when disabling scale and scroll ([#947](https://github.com/tradingview/lightweight-charts/issues/947))
494 | - Add ability to disable visibility of price line line (see [#969](https://github.com/tradingview/lightweight-charts/issues/969))
495 | 
496 | **Fixed**
497 | 
498 | - timeScale.fitContent is not working correctly (see [#966](https://github.com/tradingview/lightweight-charts/issues/966))
499 | - Delegate.unsubscribeAll method works in opposite way (see [#995](https://github.com/tradingview/lightweight-charts/issues/995))
500 | - Last price animation is active when no data added to the right (but to the left) (see [#886](https://github.com/tradingview/lightweight-charts/issues/886))
501 | - subscribeClick on mobile always get the last index of all the items (see [#657](https://github.com/tradingview/lightweight-charts/issues/657))
502 | - Incorrect crosshair position on scrolling by dragging by mouse (see [#987](https://github.com/tradingview/lightweight-charts/issues/987))
503 | - A painting slows down after a while with tons of updates (see [#946](https://github.com/tradingview/lightweight-charts/issues/946))
504 | - Bars disappear with devicePixelRatio less than 1 (see [#982](https://github.com/tradingview/lightweight-charts/issues/982))
505 | - There are no tick marks on the price axis (see [#939](https://github.com/tradingview/lightweight-charts/issues/939))
506 | - Disabling scrolling by disabled horzTouchDrag and vertTouchDrag options disables moving crosshair in tracking mode (see [#434](https://github.com/tradingview/lightweight-charts/issues/434))
507 | - Reducing precision doesn't update price scale width (see [#550](https://github.com/tradingview/lightweight-charts/issues/550))
508 | - Chart width is jumping on series change from area to candles (see [#943](https://github.com/tradingview/lightweight-charts/issues/943))
509 | - Log axis is not scaling on small number (see [#874](https://github.com/tradingview/lightweight-charts/issues/874))
510 | - Overlay series title is not rendered when no series use right price scale (see [#926](https://github.com/tradingview/lightweight-charts/issues/926))
511 | - scrollToPosition with big negative value and when no data breaks the chart (see [#889](https://github.com/tradingview/lightweight-charts/issues/889))
512 | - When rendering multiple charts with baseline series, baseValue of the last element is used on all charts series. (see [#898](https://github.com/tradingview/lightweight-charts/issues/898))
513 | 
514 | Thanks to our contributors:
515 | 
516 | - [@zaleGZL](https://github.com/zaleGZL) zale
517 | 
518 | See [issues assigned to this version's milestone](https://github.com/tradingview/lightweight-charts/milestone/23?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v3.7.0..v3.8.0).
519 | 
520 | ---
521 | 
522 | ## 3.7.0
523 | 
524 | **Enhancement**
525 | 
526 | - The new baseline series chart (see [#151](https://github.com/tradingview/lightweight-charts/issues/151))
527 | - Documentation about time zones support (see [#781](https://github.com/tradingview/lightweight-charts/issues/781))
528 | - Added methods to get time axis size and subscribe on size change (see [#853](https://github.com/tradingview/lightweight-charts/issues/853))
529 | - Improved performance of setting/updating series data (see [#418](https://github.com/tradingview/lightweight-charts/issues/418) and [#838](https://github.com/tradingview/lightweight-charts/issues/838))
530 | - Use lowerbound in TimeScale timeToIndex search (see [#767](https://github.com/tradingview/lightweight-charts/issues/767))
531 | - Add JSDoc comments for existing API docs (see [#870](https://github.com/tradingview/lightweight-charts/issues/870))
532 | 
533 | **Fixed**
534 | 
535 | - Increased min price tick mark step up to 1e-14 (from 1e-9) (see [#841](https://github.com/tradingview/lightweight-charts/issues/841))
536 | - Fix typo in customization docs (see [#844](https://github.com/tradingview/lightweight-charts/issues/844))
537 | - Do not paint time axis if it not visible (see [#865](https://github.com/tradingview/lightweight-charts/issues/865))
538 | - Remove color customisation from settings.json (see [#869](https://github.com/tradingview/lightweight-charts/issues/869))
539 | 
540 | Thanks to our contributors:
541 | 
542 | - [@thanhlmm](https://github.com/thanhlmm) Thanh Le
543 | 
544 | See [issues assigned to this version's milestone](https://github.com/tradingview/lightweight-charts/milestone/22?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v3.6.1..v3.7.0).
545 | 
546 | ---
547 | 
548 | ## 3.6.1
549 | 
550 | **Fixed**
551 | 
552 | - In v3.6.0 there was a typo in `LasPriceAnimationMode` const enum (`Last` without `t`), which was fixed in this release. The incorrect name is still available to import and could be used in your code so no breaking change so far (see e5133cb0c50fc557182aba4011e170aaf30a5b1a)
553 | 
554 | See [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v3.6.0..v3.6.1).
555 | 
556 | ---
557 | 
558 | ## 3.6.0
559 | 
560 | On this day 10 years ago, 10th September 2011, the very first version of the TradingView website was deployed. To celebrate 10th anniversary we're happy to announce the new version of lightweight-charts library v3.6.0 🎉🎉🎉
561 | 
562 | **Enhancement**
563 | 
564 | - Gradient chart background color (see [#831](https://github.com/tradingview/lightweight-charts/issues/831))
565 | - How to add buffer animation to price jump (see [#567](https://github.com/tradingview/lightweight-charts/issues/567))
566 | - Kinetic scroll (see [#832](https://github.com/tradingview/lightweight-charts/issues/832))
567 | 
568 | **Fixed**
569 | 
570 | - Incorrect initial barSpacing when both fixRightEdge and fixLeftEdge are enabled (see [#823](https://github.com/tradingview/lightweight-charts/issues/823))
571 | - Time axis label get cut on the edge if a fix edge option is enabled (see [#835](https://github.com/tradingview/lightweight-charts/issues/835))
572 | - Price axis doesn't respect the width of crosshair label (see [#834](https://github.com/tradingview/lightweight-charts/issues/834))
573 | - Fixed both timescale edges make lockVisibleTimeRangeOnResize turn wrong (see [#814](https://github.com/tradingview/lightweight-charts/issues/814))
574 | - `Error: Value is null` error while set the data is container has 0x0 size (see [#821](https://github.com/tradingview/lightweight-charts/issues/821))
575 | 
576 | Thanks to our contributors:
577 | 
578 | - [@thanhlmm](https://github.com/thanhlmm) Thanh Le
579 | 
580 | See [issues assigned to this version's milestone](https://github.com/tradingview/lightweight-charts/milestone/21?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v3.5.0..v3.6.0).
581 | 
582 | ---
583 | 
584 | ## 3.5.0
585 | 
586 | **A note about rendering order of series, which might be interpret as a bug or breaking change since this release**
587 | 
588 | This is not really a breaking change, but might be interpret like that. In [#794](https://github.com/tradingview/lightweight-charts/issues/794) we've fixed the wrong order of series, thus now all series will be displayed in opposite order (they will be displayed in order of creating now; previously they were displayed in reversed order).
589 | 
590 | To fix that, just change the order of creating the series (thus instead of create series A, then series B create series B first and then series A) - see [#812](https://github.com/tradingview/lightweight-charts/issues/812).
591 | 
592 | **Fixed**
593 | 
594 | - Screenshot output missing piece on bottom right (see [#798](https://github.com/tradingview/lightweight-charts/issues/798))
595 | - Overlapped line chart show wrong color order when hover (see [#794](https://github.com/tradingview/lightweight-charts/issues/794))
596 | - Price line label show on both axis (see [#795](https://github.com/tradingview/lightweight-charts/issues/795))
597 | 
598 | Thanks to our contributors:
599 | 
600 | - [@thanhlmm](https://github.com/thanhlmm) Thanh Le
601 | 
602 | See [issues assigned to this version's milestone](https://github.com/tradingview/lightweight-charts/milestone/20?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v3.4.0..v3.5.0).
603 | 
604 | ---
605 | 
606 | ## 3.4.0
607 | 
608 | **Enhancement**
609 | 
610 | - Add option to fix right edge (see [#218](https://github.com/tradingview/lightweight-charts/issues/218))
611 | - Drop restriction for min bar spacing value (see [#558](https://github.com/tradingview/lightweight-charts/issues/558))
612 | - Round corners of the line-style plots (see [#731](https://github.com/tradingview/lightweight-charts/issues/731))
613 | 
614 | **Fixed**
615 | 
616 | - AutoscaleProvider documentation error (see [#773](https://github.com/tradingview/lightweight-charts/issues/773))
617 | - Candlestick upColor and downColor is not changed on applyOptions (see [#750](https://github.com/tradingview/lightweight-charts/issues/750))
618 | - Cleared and reset data appears at visually different location (see [#757](https://github.com/tradingview/lightweight-charts/issues/757))
619 | - Remove unused internal method from SeriesApi (see [#768](https://github.com/tradingview/lightweight-charts/issues/768))
620 | - Removing data for the last series doesn't actually remove the data (see [#752](https://github.com/tradingview/lightweight-charts/issues/752))
621 | - `to` date of getVisibleRange contains partially visible data item and it's impossible to hover it (see [#624](https://github.com/tradingview/lightweight-charts/issues/624))
622 | - series.priceFormatter().format(price) does not work (see [#790](https://github.com/tradingview/lightweight-charts/issues/790))
623 | 
624 | See [issues assigned to this version's milestone](https://github.com/tradingview/lightweight-charts/milestone/19?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v3.3.0..v3.4.0).
625 | 
626 | ---
627 | 
628 | ## 3.3.0
629 | 
630 | **Enhancement**
631 | 
632 | - Add type predicates for series type (see [#670](https://github.com/tradingview/lightweight-charts/issues/670))
633 | - Create Grid instance for every pane (see [#382](https://github.com/tradingview/lightweight-charts/issues/382))
634 | - Add possibility to chose crosshairMarker color, so it will be independent from line-series color (see [#310](https://github.com/tradingview/lightweight-charts/issues/310))
635 | - Implement option not to shift the time scale at all when data is added with `setData` (see [#584](https://github.com/tradingview/lightweight-charts/issues/584))
636 | 
637 | **Fixed**
638 | 
639 | - Incorrect bar height when its value is more than chart's height (see [#673](https://github.com/tradingview/lightweight-charts/issues/673))
640 | - Disabling autoScale for non-visible series (see [#687](https://github.com/tradingview/lightweight-charts/issues/687))
641 | 
642 | Thanks to our contributors:
643 | 
644 | - [@dubroff](https://github.com/dubroff)
645 | - [@SuperPenguin](https://github.com/SuperPenguin) Andree Yosua
646 | - [@mecm1993](https://github.com/mecm1993) Manuel Cepeda
647 | 
648 | See [issues assigned to this version's milestone](https://github.com/tradingview/lightweight-charts/milestone/17?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v3.2.0..v3.3.0).
649 | 
650 | ---
651 | 
652 | ## 3.2.0
653 | 
654 | **Enhancement**
655 | 
656 | - Feat/gzip friendly colors (see [#598](https://github.com/tradingview/lightweight-charts/issues/598))
657 | - Add coordinateToLogical and logicalToCoordinate (see [#587](https://github.com/tradingview/lightweight-charts/issues/587))
658 | - Add API to show/hide series without removing it (see [#471](https://github.com/tradingview/lightweight-charts/issues/471))
659 | - Add run-time validation of inputs in debug mode (see [#315](https://github.com/tradingview/lightweight-charts/issues/315))
660 | - Pixel perfect renderers fixes (see [#535](https://github.com/tradingview/lightweight-charts/issues/535))
661 | - Add title option to createPriceLine (see [#357](https://github.com/tradingview/lightweight-charts/issues/357))
662 | 
663 | **Fixed**
664 | 
665 | - Set rightOffset and scrollToPosition async as well as setVisibleRange (see [#406](https://github.com/tradingview/lightweight-charts/issues/406))
666 | - timeScale() changes visible range on setData() (see [#549](https://github.com/tradingview/lightweight-charts/issues/549))
667 | - Remove chart's size restriction or make it smaller (see [#366](https://github.com/tradingview/lightweight-charts/issues/366))
668 | - LineStyle.Dotted make no effect (see [#572](https://github.com/tradingview/lightweight-charts/issues/572))
669 | - If priceScaleId is empty string, invalid price scale api is returned (see [#537](https://github.com/tradingview/lightweight-charts/issues/537))
670 | - Incorrect Selection seen on long press in ios webview on chart (see [#609](https://github.com/tradingview/lightweight-charts/issues/609))
671 | - One-point line series is invisible (see [#597](https://github.com/tradingview/lightweight-charts/issues/597))
672 | - Empty price scale after creating series with the same price range (see [#615](https://github.com/tradingview/lightweight-charts/issues/615))
673 | 
674 | **Infra and dev env**
675 | 
676 | - Compress artifacts in graphics tests in CI (see [#145](https://github.com/tradingview/lightweight-charts/issues/145))
677 | - Run tests against production build (see [#503](https://github.com/tradingview/lightweight-charts/issues/503))
678 | - Add test to check code usage coverage (see [#495](https://github.com/tradingview/lightweight-charts/issues/495))
679 | - Migrate from codechecks (see [#356](https://github.com/tradingview/lightweight-charts/issues/356))
680 | - Updated dev deps
681 | 
682 | Thanks to our contributors:
683 | 
684 | - Andree Yosua [@SuperPenguin](https://github.com/SuperPenguin)
685 | - Christos [@christose](https://github.com/christose)
686 | - Shergin Rodion [@beholderrk](https://github.com/beholderrk)
687 | - wenhoujx [@wenhoujx](https://github.com/wenhoujx)
688 | 
689 | See [issues assigned to this version's milestone](https://github.com/tradingview/lightweight-charts/milestone/11?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v3.1.5..v3.2.0).
690 | 
691 | ---
692 | 
693 | ## 3.1.5
694 | 
695 | It's a just re-published accidentally published 3.1.4 version, which didn't actually fix the issue [#536](https://github.com/tradingview/lightweight-charts/issues/536).
696 | 
697 | Version 3.1.4 has been deprecated.
698 | 
699 | **Fixed**
700 | 
701 | - TypeError `_internal_priceScale is not a function` while getting series price scale (see [#536](https://github.com/tradingview/lightweight-charts/issues/536))
702 | 
703 | See [issues assigned to this version's milestone](https://github.com/tradingview/lightweight-charts/milestone/16?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v3.1.3..v3.1.5).
704 | 
705 | ---
706 | 
707 | ## 3.1.3
708 | 
709 | **Fixed**
710 | 
711 | - `handleScroll` and `handleScale` options aren't applied (see [#527](https://github.com/tradingview/lightweight-charts/issues/527))
712 | 
713 | See [issues assigned to this version's milestone](https://github.com/tradingview/lightweight-charts/milestone/14?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v3.1.2..v3.1.3).
714 | 
715 | ---
716 | 
717 | ## 3.1.2
718 | 
719 | **Fixed**
720 | 
721 | - Crosshair doesn't work on touch devices (see [#511](https://github.com/tradingview/lightweight-charts/issues/511))
722 | 
723 | See [issues assigned to this version's milestone](https://github.com/tradingview/lightweight-charts/milestone/13?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v3.1.1..v3.1.2).
724 | 
725 | ---
726 | 
727 | ## 3.1.1
728 | 
729 | **Fixed**
730 | 
731 | - Fixed production build of 3.1 version (see [#502](https://github.com/tradingview/lightweight-charts/issues/502) and [62aa93724e40fbb1b678d9b44655279a1df529c5](https://github.com/tradingview/lightweight-charts/commit/62aa93724e40fbb1b678d9b44655279a1df529c5))
732 | 
733 | See [issues assigned to this version's milestone](https://github.com/tradingview/lightweight-charts/milestone/12?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v3.1.0..v3.1.1).
734 | 
735 | ---
736 | 
737 | ## 3.1.0
738 | 
739 | **Enhancement**
740 | 
741 | - Whitespaces support (see [#209](https://github.com/tradingview/lightweight-charts/issues/209))
742 | - Custom font families for watermarks (see [#437](https://github.com/tradingview/lightweight-charts/issues/437))
743 | 
744 | **Fixed**
745 | 
746 | - Added support for 'transparent' color (see [#491](https://github.com/tradingview/lightweight-charts/issues/491))
747 | - Refactor DataLayer/ChartApi (see [#270](https://github.com/tradingview/lightweight-charts/issues/270))
748 | - Remove series then scroll to right after not working (see [#355](https://github.com/tradingview/lightweight-charts/issues/355))
749 | - Scaling via mouse click and drag doesn't work if chart is inside shadow root (see [#427](https://github.com/tradingview/lightweight-charts/issues/427))
750 | - Applying watermark in setTimeout doesn't make an effect (see [#485](https://github.com/tradingview/lightweight-charts/issues/485))
751 | - Importing the library in server-side context caused `ReferenceError` (see [#446](https://github.com/tradingview/lightweight-charts/issues/446))
752 | 
753 | **Undocumented breaking changes**
754 | 
755 | We know that some of users probably used some hacky-workarounds calling internal methods to achieve multi-pane support. In this release, to reduce size of the bundle we [dropped out a code for pane's separator](https://github.com/tradingview/lightweight-charts/pull/496) (which allows to resize panes).
756 | 
757 | As soon this workaround is undocumented and we don't support this feature yet - we don't bump a major version. But we think it's better to let you know that it has been changed.
758 | 
759 | **Development**
760 | 
761 | - Dropped support NodeJS < 12.18
762 | - Migrated from TSLint to ESLint (see [#314](https://github.com/tradingview/lightweight-charts/issues/314))
763 | - Migrated from clean-publish to in-house script to clear package.json (see [#474](https://github.com/tradingview/lightweight-charts/issues/474))
764 | 
765 | Thanks to our contributors:
766 | 
767 | - Meet Mangukiya [@meetmangukiya](https://github.com/meetmangukiya)
768 | - NekitCorp [@NekitCorp](https://github.com/NekitCorp)
769 | 
770 | See [issues assigned to this version's milestone](https://github.com/tradingview/lightweight-charts/milestone/9?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v3.0.1..v3.1.0).
771 | 
772 | ---
773 | 
774 | ## 3.0.1
775 | 
776 | **Fixed**
777 | 
778 | - Correctly handle `overlay: true` in series options while create series to backward compat (see [#475](https://github.com/tradingview/lightweight-charts/issues/475))
779 | 
780 | See [issues assigned to this version's milestone](https://github.com/tradingview/lightweight-charts/milestone/10?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v3.0.0..v3.0.1).
781 | 
782 | ---
783 | 
784 | ## 3.0.0
785 | 
786 | **Breaking changes**
787 | 
788 | We have some breaking changes since the latest version due some features and API improvements:
789 | 
790 | - Methods `subscribeVisibleTimeRangeChange` and `unsubscribeVisibleTimeRangeChange` has been moved from ChartApi to TimeScaleApi
791 | - Since 3.0 you can specify price axis you'd like to place the series on. The same for moving the series between price scales (see migration guide below)
792 | 
793 | See [breaking changes doc](https://github.com/tradingview/lightweight-charts/blob/master/docs/3.0-breaking-changes.md) with migration guide to migrate smoothly.
794 | 
795 | **Enhancement**
796 | 
797 | - Added ability to customize time scale tick marks formatter (see [#226](https://github.com/tradingview/lightweight-charts/issues/226))
798 | - Added ability to put text for series markers (see [#207](https://github.com/tradingview/lightweight-charts/issues/207))
799 | - Added ability to specify your own date formatter (see [#368](https://github.com/tradingview/lightweight-charts/issues/368))
800 | - Improved tick marks generation algorithm for the first point (see [#387](https://github.com/tradingview/lightweight-charts/issues/387))
801 | - Made inbound types weakly (outbound ones should be strict) (see [#374](https://github.com/tradingview/lightweight-charts/issues/374))
802 | - Removed non-exported const enum's JS code (see [#432](https://github.com/tradingview/lightweight-charts/issues/432))
803 | - Introduced [ts-transformer-properties-rename](https://github.com/timocov/ts-transformer-properties-rename) instead of [ts-transformer-minify-privates](https://github.com/timocov/ts-transformer-minify-privates) (see [#436](https://github.com/tradingview/lightweight-charts/issues/436))
804 | 
805 | **Added**
806 | 
807 | - Add ability to override series' autoscale range (see [#392](https://github.com/tradingview/lightweight-charts/issues/392))
808 | - Add API to get price scale's width (see [#452](https://github.com/tradingview/lightweight-charts/issues/452))
809 | - Disabling/enabling scaling axis for both price and time (see [#440](https://github.com/tradingview/lightweight-charts/issues/440))
810 | - Get screen coordinate by a time point (see [#435](https://github.com/tradingview/lightweight-charts/issues/435))
811 | - Remove tick mark from price label (see [#378](https://github.com/tradingview/lightweight-charts/issues/378))
812 | - Support the second price axis (see [#129](https://github.com/tradingview/lightweight-charts/issues/129))
813 | - Visible time range should have bars count of the space from left/right (see [#335](https://github.com/tradingview/lightweight-charts/issues/335))
814 | 
815 | **Fixed**
816 | 
817 | - `series.setMarkers` requires at least one data point (see [#372](https://github.com/tradingview/lightweight-charts/issues/372))
818 | - Impossible to override the only width or height in constructor (see [#353](https://github.com/tradingview/lightweight-charts/issues/353))
819 | - Incorrect alignment of markers if series has gaps (see [#464](https://github.com/tradingview/lightweight-charts/issues/464))
820 | - Multiple series: error while trying to scroll the chart (see [#373](https://github.com/tradingview/lightweight-charts/issues/373))
821 | - Replace const enums with enums to let use them in projects with enabled isolatedModules option (see [#375](https://github.com/tradingview/lightweight-charts/issues/375))
822 | 
823 | Thanks to our contributors:
824 | 
825 | - Ben Guidarelli [@barnjamin](https://github.com/barnjamin)
826 | - gkaindl [@gkaindl](https://github.com/gkaindl)
827 | - scrwdrv [@scrwdrv](https://github.com/scrwdrv)
828 | - Yusuf Sahin HAMZA [@yusufsahinhamza](https://github.com/yusufsahinhamza)
829 | 
830 | See [issues assigned to this version's milestone](https://github.com/tradingview/lightweight-charts/milestone/7?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v2.0.0..v3.0.0).
831 | 
832 | ---
833 | 
834 | ## 2.0.0
835 | 
836 | **Breaking changes**
837 | 
838 | - Removed unused `lineWidth` property from `HistogramStyleOptions` interface (it affects nothing, but could break your compilation)
839 | - Changed order of `width` and `height` args in `resize` method ([#157](https://github.com/tradingview/lightweight-charts/issues/157))
840 | - Pattern for all non-solid (dotted, dashed, large dashed and sparse dotted) line styles was a bit changed ([#274](https://github.com/tradingview/lightweight-charts/issues/274))
841 | 
842 | **Enhancement**
843 | 
844 | - Pixel-perfect rendering ([#274](https://github.com/tradingview/lightweight-charts/issues/274))
845 | - Time scale enhancements ([#352](https://github.com/tradingview/lightweight-charts/issues/352))
846 | 
847 | **Added**
848 | 
849 | - Disable all kinds of scrolls and touch with one option ([#230](https://github.com/tradingview/lightweight-charts/issues/230))
850 | - Added to the acceptable date formats ([#296](https://github.com/tradingview/lightweight-charts/issues/296))
851 | - Add option to show the "global" last value of the series instead of the last visible ([#203](https://github.com/tradingview/lightweight-charts/issues/203))
852 | 
853 | **Fixed**
854 | 
855 | - Price line didn`t hightlight price ([#273](https://github.com/tradingview/lightweight-charts/issues/273))
856 | - CreatePriceLine not removed ([#285](https://github.com/tradingview/lightweight-charts/issues/285))
857 | - Crosshair line not visible when priceScale position set to none ([#302](https://github.com/tradingview/lightweight-charts/issues/302))
858 | - chart.resize parameter is inverted ([#157](https://github.com/tradingview/lightweight-charts/issues/157))
859 | - Removed unnecessary spacing from left/right (1 bar from each side) in `fitContent` ([#345](https://github.com/tradingview/lightweight-charts/issues/345))
860 | 
861 | Thanks to our contributors:
862 | 
863 | - Andree Yosua [@SuperPenguin](https://github.com/SuperPenguin)
864 | - kpaape [@kpaape](https://github.com/kpaape)
865 | - Matt Conway [@RetWolf](https://github.com/RetWolf)
866 | 
867 | See [issues assigned to this version’s milestone](https://github.com/tradingview/lightweight-charts/milestone/6?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v1.2.2..v2.0.0).
868 | 
869 | ---
870 | 
871 | ## 1.2.2
872 | 
873 | **Fixed**
874 | 
875 | - Bug while rendering few datasets with not equal timescale ([#321](https://github.com/tradingview/lightweight-charts/issues/321))
876 | 
877 | ---
878 | 
879 | ## 1.2.1
880 | 
881 | **Added**
882 | 
883 | - Add custom price lines ([#183](https://github.com/tradingview/lightweight-charts/issues/183))
884 | - Migrate canvas-related logic to fancy-canvas library ([#141](https://github.com/tradingview/lightweight-charts/issues/141))
885 | - Add coordinateToPrice method to ISeriesApi ([#171](https://github.com/tradingview/lightweight-charts/issues/171))
886 | 
887 | **Fixed**
888 | 
889 | - Scrolling by price is incorrect ([#213](https://github.com/tradingview/lightweight-charts/issues/213))
890 | - Histogram (volume) does not honor color setting (sometimes) ([#233](https://github.com/tradingview/lightweight-charts/issues/233))
891 | - Logarithmic scaling is applied to volume ([#227](https://github.com/tradingview/lightweight-charts/issues/227))
892 | - hoveredSeries in mouse events params is always undefined ([#190](https://github.com/tradingview/lightweight-charts/issues/190))
893 | - `lineType` option does not work for area/line series ([#220](https://github.com/tradingview/lightweight-charts/issues/220))
894 | - Double clicking on time scale will reset fix left edge ([#224](https://github.com/tradingview/lightweight-charts/issues/224))
895 | - Series' marker does not aligned after autoscale ([#212](https://github.com/tradingview/lightweight-charts/issues/212))
896 | - Error on setData empty array for overlay histogram series ([#267](https://github.com/tradingview/lightweight-charts/issues/267))
897 | - Added some missing docs ([#211](https://github.com/tradingview/lightweight-charts/issues/211) [#193](https://github.com/tradingview/lightweight-charts/issues/193) [#245](https://github.com/tradingview/lightweight-charts/issues/245))
898 | 
899 | See [issues assigned to this version’s milestone](https://github.com/tradingview/lightweight-charts/milestone/4?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v1.1.0...v1.2.1).
900 | 
901 | ---
902 | 
903 | ## 1.1.0
904 | 
905 | **Added**
906 | 
907 | - Apply localization to specific series ([#62](https://github.com/tradingview/lightweight-charts/issues/62))
908 | - Series-based markers ([#24](https://github.com/tradingview/lightweight-charts/issues/24))
909 | - Reduced size of the library by using [`ts-transformer-minify-privates`](https://github.com/timocov/ts-transformer-minify-privates) transformer ([#98](https://github.com/tradingview/lightweight-charts/issues/98))
910 | 
911 | **Fixed**
912 | 
913 | - The chart can't start from the left ([#144](https://github.com/tradingview/lightweight-charts/issues/144))
914 | - OHLC charts render incorrect when `value` is provided ([#165](https://github.com/tradingview/lightweight-charts/issues/165))
915 | - Price axis is not shown if series is created inside promise chain ([#164](https://github.com/tradingview/lightweight-charts/issues/164))
916 | - The line chart can't move to the left ([#143](https://github.com/tradingview/lightweight-charts/issues/143))
917 | - Lots of non-passive event listener warnings ([#139](https://github.com/tradingview/lightweight-charts/issues/139))
918 | - applyOptions of histogram series with color doesn't affect the data ([#112](https://github.com/tradingview/lightweight-charts/issues/112))
919 | - Price Axis Scaling Bug ([#122](https://github.com/tradingview/lightweight-charts/issues/122))
920 | - LineSeries is not displayed if starting x value is out of viewport ([#116](https://github.com/tradingview/lightweight-charts/issues/116))
921 | - Crosshair isn't updated when timescale is changed ([#120](https://github.com/tradingview/lightweight-charts/issues/120))
922 | - Pinch isn't prevented by long tap ([#95](https://github.com/tradingview/lightweight-charts/issues/95))
923 | 
924 | Thanks to our contributors:
925 | 
926 | - zach [@n8tb1t](https://github.com/n8tb1t)
927 | - Chris Kaczor [@krzkaczor](https://github.com/krzkaczor)
928 | 
929 | See [issues assigned to this version’s milestone](https://github.com/tradingview/lightweight-charts/milestone/2?closed=1) or [changes since the last published version](https://github.com/tradingview/lightweight-charts/compare/v1.0.2...v1.1.0).
930 | 
931 | ---
932 | 
933 | ## 1.0.2
934 | 
935 | **Fixed**
936 | 
937 | - The histogram last bar not hide in chart ([#133](https://github.com/tradingview/lightweight-charts/issues/133))
938 | 
939 | ---
940 | 
941 | ## 1.0.1
942 | 
943 | **Fixed**
944 | 
945 | - Setting the data to series fails after setting the data to histogram series with custom color ([#110](https://github.com/tradingview/lightweight-charts/issues/110))
946 | 
947 | ---
948 | 
949 | ## 1.0.0
950 | 
951 | The first release.
952 | 
953 | The docs for this version are available [here](https://github.com/tradingview/lightweight-charts/tree/v1.0.0/docs).
954 | 
955 | ---
956 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/series-types.mdx:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_position: 1
  3 | ---
  4 | 
  5 | # Series
  6 | 
  7 | This article describes supported series types and ways to [customize](#customization) them.
  8 | 
  9 | ## Supported types
 10 | 
 11 | ### Area
 12 | 
 13 | - **Series Definition**: [`AreaSeries`](/api/variables/AreaSeries.md)
 14 | - **Data format**: [`SingleValueData`](/api/interfaces/SingleValueData.md) or [`WhitespaceData`](/api/interfaces/WhitespaceData.md)
 15 | - **Style options**: a mix of [`SeriesOptionsCommon`](/api/interfaces/SeriesOptionsCommon.md) and [`AreaStyleOptions`](/api/interfaces/AreaStyleOptions.md)
 16 | 
 17 | This series is represented with a colored area between the [time scale](./time-scale.md) and line connecting all data points:
 18 | 
 19 | import CodeBlock from '@theme/CodeBlock';
 20 | export const areaExample = `const chartOptions = { layout: { textColor: CHART_TEXT_COLOR, background: { type: 'solid', color: CHART_BACKGROUND_COLOR } } };
 21 | const chart = createChart(document.getElementById('container'), chartOptions);
 22 | const areaSeries = chart.addSeries(AreaSeries, { lineColor: LINE_LINE_COLOR, topColor: AREA_TOP_COLOR, bottomColor: AREA_BOTTOM_COLOR });
 23 | 
 24 | const data = [{ value: 0, time: 1642425322 }, { value: 8, time: 1642511722 }, { value: 10, time: 1642598122 }, { value: 20, time: 1642684522 }, { value: 3, time: 1642770922 }, { value: 43, time: 1642857322 }, { value: 41, time: 1642943722 }, { value: 43, time: 1643030122 }, { value: 56, time: 1643116522 }, { value: 46, time: 1643202922 }];
 25 | 
 26 | areaSeries.setData(data);
 27 | 
 28 | chart.timeScale().fitContent();
 29 | `;
 30 | 
 31 | <CodeBlock className="language-js" replaceThemeConstants chart>{areaExample}</CodeBlock>
 32 | 
 33 | ### Bar
 34 | 
 35 | - **Series Definition**: [`BarSeries`](/api/variables/BarSeries.md)
 36 | - **Data format**: [`BarData`](/api/interfaces/BarData.md) or [`WhitespaceData`](/api/interfaces/WhitespaceData.md)
 37 | - **Style options**: a mix of [`SeriesOptionsCommon`](/api/interfaces/SeriesOptionsCommon.md) and [`BarStyleOptions`](/api/interfaces/BarStyleOptions.md)
 38 | 
 39 | This series illustrates price movements with vertical bars.
 40 | The length of each bar corresponds to the range between the highest and lowest price values.
 41 | Open and close values are represented with the tick marks on the left and right side of the bar, respectively:
 42 | 
 43 | export const barExample = `const chartOptions = { layout: { textColor: CHART_TEXT_COLOR, background: { type: 'solid', color: CHART_BACKGROUND_COLOR } } };
 44 | const chart = createChart(document.getElementById('container'), chartOptions);
 45 | const barSeries = chart.addSeries(BarSeries, { upColor: BAR_UP_COLOR, downColor: BAR_DOWN_COLOR });
 46 | 
 47 | const data = [
 48 |   { open: 10, high: 10.63, low: 9.49, close: 9.55, time: 1642427876 },
 49 |   { open: 9.55, high: 10.30, low: 9.42, close: 9.94, time: 1642514276 },
 50 |   { open: 9.94, high: 10.17, low: 9.92, close: 9.78, time: 1642600676 },
 51 |   { open: 9.78, high: 10.59, low: 9.18, close: 9.51, time: 1642687076 },
 52 |   { open: 9.51, high: 10.46, low: 9.10, close: 10.17, time: 1642773476 },
 53 |   { open: 10.17, high: 10.96, low: 10.16, close: 10.47, time: 1642859876 },
 54 |   { open: 10.47, high: 11.39, low: 10.40, close: 10.81, time: 1642946276 },
 55 |   { open: 10.81, high: 11.60, low: 10.30, close: 10.75, time: 1643032676 },
 56 |   { open: 10.75, high: 11.60, low: 10.49, close: 10.93, time: 1643119076 },
 57 |   { open: 10.93, high: 11.53, low: 10.76, close: 10.96, time: 1643205476 },
 58 |   { open: 10.96, high: 11.90, low: 10.80, close: 11.50, time: 1643291876 },
 59 |   { open: 11.50, high: 12.00, low: 11.30, close: 11.80, time: 1643378276 },
 60 |   { open: 11.80, high: 12.20, low: 11.70, close: 12.00, time: 1643464676 },
 61 |   { open: 12.00, high: 12.50, low: 11.90, close: 12.30, time: 1643551076 },
 62 |   { open: 12.30, high: 12.80, low: 12.10, close: 12.60, time: 1643637476 },
 63 |   { open: 12.60, high: 13.00, low: 12.50, close: 12.90, time: 1643723876 },
 64 |   { open: 12.90, high: 13.50, low: 12.70, close: 13.20, time: 1643810276 },
 65 |   { open: 13.20, high: 13.70, low: 13.00, close: 13.50, time: 1643896676 },
 66 |   { open: 13.50, high: 14.00, low: 13.30, close: 13.80, time: 1643983076 },
 67 |   { open: 13.80, high: 14.20, low: 13.60, close: 14.00, time: 1644069476 },
 68 | ];
 69 | 
 70 | barSeries.setData(data);
 71 | 
 72 | chart.timeScale().fitContent();
 73 | `;
 74 | 
 75 | <CodeBlock className="language-js" replaceThemeConstants chart>{barExample}</CodeBlock>
 76 | 
 77 | ### Baseline
 78 | 
 79 | - **Series Definition**: [`BaselineSeries`](/api/variables/BaselineSeries.md)
 80 | - **Data format**: [`SingleValueData`](/api/interfaces/SingleValueData.md) or [`WhitespaceData`](/api/interfaces/WhitespaceData.md)
 81 | - **Style options**: a mix of [`SeriesOptionsCommon`](/api/interfaces/SeriesOptionsCommon.md) and [`BaselineStyleOptions`](/api/interfaces/BaselineStyleOptions.md)
 82 | 
 83 | This series is represented with two colored areas between the [the base value line](/api/interfaces/BaselineStyleOptions.md#basevalue) and line connecting all data points:
 84 | 
 85 | export const baselineExample = `const chartOptions = { layout: { textColor: CHART_TEXT_COLOR, background: { type: 'solid', color: CHART_BACKGROUND_COLOR } } };
 86 | const chart = createChart(document.getElementById('container'), chartOptions);
 87 | const baselineSeries = chart.addSeries(BaselineSeries, { baseValue: { type: 'price', price: 25 }, topLineColor: BASELINE_TOP_LINE_COLOR, topFillColor1: BASELINE_TOP_FILL_COLOR1, topFillColor2: BASELINE_TOP_FILL_COLOR2, bottomLineColor: BASELINE_BOTTOM_LINE_COLOR, bottomFillColor1: BASELINE_BOTTOM_FILL_COLOR1, bottomFillColor2: BASELINE_BOTTOM_FILL_COLOR2 });
 88 | 
 89 | const data = [{ value: 1, time: 1642425322 }, { value: 8, time: 1642511722 }, { value: 10, time: 1642598122 }, { value: 20, time: 1642684522 }, { value: 3, time: 1642770922 }, { value: 43, time: 1642857322 }, { value: 41, time: 1642943722 }, { value: 43, time: 1643030122 }, { value: 56, time: 1643116522 }, { value: 46, time: 1643202922 }];
 90 | 
 91 | baselineSeries.setData(data);
 92 | 
 93 | chart.timeScale().fitContent();
 94 | `;
 95 | 
 96 | <CodeBlock className="language-js" replaceThemeConstants chart>{baselineExample}</CodeBlock>
 97 | 
 98 | ### Candlestick
 99 | 
100 | - **Series Definition**: [`CandlestickSeries`](/api/variables/CandlestickSeries.md)
101 | - **Data format**: [`CandlestickData`](/api/interfaces/CandlestickData.md) or [`WhitespaceData`](/api/interfaces/WhitespaceData.md)
102 | - **Style options**: a mix of [`SeriesOptionsCommon`](/api/interfaces/SeriesOptionsCommon.md) and [`CandlestickStyleOptions`](/api/interfaces/CandlestickStyleOptions.md)
103 | 
104 | This series illustrates price movements with candlesticks.
105 | The solid body of each candlestick represents the open and close values for the time period. Vertical lines, known as wicks, above and below the candle body represent the high and low values, respectively:
106 | 
107 | export const candlestickExample = `const chartOptions = { layout: { textColor: CHART_TEXT_COLOR, background: { type: 'solid', color: CHART_BACKGROUND_COLOR } } };
108 | const chart = createChart(document.getElementById('container'), chartOptions);
109 | const candlestickSeries = chart.addSeries(CandlestickSeries, { upColor: BAR_UP_COLOR, downColor: BAR_DOWN_COLOR, borderVisible: false, wickUpColor: BAR_UP_COLOR, wickDownColor: BAR_DOWN_COLOR });
110 | 
111 | const data = [{ open: 10, high: 10.63, low: 9.49, close: 9.55, time: 1642427876 }, { open: 9.55, high: 10.30, low: 9.42, close: 9.94, time: 1642514276 }, { open: 9.94, high: 10.17, low: 9.92, close: 9.78, time: 1642600676 }, { open: 9.78, high: 10.59, low: 9.18, close: 9.51, time: 1642687076 }, { open: 9.51, high: 10.46, low: 9.10, close: 10.17, time: 1642773476 }, { open: 10.17, high: 10.96, low: 10.16, close: 10.47, time: 1642859876 }, { open: 10.47, high: 11.39, low: 10.40, close: 10.81, time: 1642946276 }, { open: 10.81, high: 11.60, low: 10.30, close: 10.75, time: 1643032676 }, { open: 10.75, high: 11.60, low: 10.49, close: 10.93, time: 1643119076 }, { open: 10.93, high: 11.53, low: 10.76, close: 10.96, time: 1643205476 }];
112 | 
113 | candlestickSeries.setData(data);
114 | 
115 | chart.timeScale().fitContent();
116 | `;
117 | 
118 | <CodeBlock className="language-js" replaceThemeConstants chart>{candlestickExample}</CodeBlock>
119 | 
120 | ### Histogram
121 | 
122 | - **Series Definition**: [`HistogramSeries`](/api/variables/HistogramSeries.md)
123 | - **Data format**: [`HistogramData`](/api/interfaces/HistogramData.md) or [`WhitespaceData`](/api/interfaces/WhitespaceData.md)
124 | - **Style options**: a mix of [`SeriesOptionsCommon`](/api/interfaces/SeriesOptionsCommon.md) and [`HistogramStyleOptions`](/api/interfaces/HistogramStyleOptions.md)
125 | 
126 | This series illustrates the distribution of values with columns:
127 | 
128 | export const histogramExample = `const chartOptions = { layout: { textColor: CHART_TEXT_COLOR, background: { type: 'solid', color: CHART_BACKGROUND_COLOR } } };
129 | const chart = createChart(document.getElementById('container'), chartOptions);
130 | const histogramSeries = chart.addSeries(HistogramSeries, { color: HISTOGRAM_COLOR });
131 | 
132 | const data = [{ value: 1, time: 1642425322 }, { value: 8, time: 1642511722 }, { value: 10, time: 1642598122 }, { value: 20, time: 1642684522 }, { value: 3, time: 1642770922, color: 'red' }, { value: 43, time: 1642857322 }, { value: 41, time: 1642943722, color: 'red' }, { value: 43, time: 1643030122 }, { value: 56, time: 1643116522 }, { value: 46, time: 1643202922, color: 'red' }];
133 | 
134 | histogramSeries.setData(data);
135 | 
136 | chart.timeScale().fitContent();
137 | `;
138 | 
139 | <CodeBlock className="language-js" replaceThemeConstants chart>{histogramExample}</CodeBlock>
140 | 
141 | ### Line
142 | 
143 | - **Series Definition**: [`LineSeries`](/api/variables/LineSeries.md)
144 | - **Data format**: [`LineData`](/api/interfaces/LineData.md) or [`WhitespaceData`](/api/interfaces/WhitespaceData.md)
145 | - **Style options**: a mix of [`SeriesOptionsCommon`](/api/interfaces/SeriesOptionsCommon.md) and [`LineStyleOptions`](/api/interfaces/LineStyleOptions.md)
146 | 
147 | This series is represented with a set of data points connected by straight line segments:
148 | 
149 | export const lineExample = `const chartOptions = { layout: { textColor: CHART_TEXT_COLOR, background: { type: 'solid', color: CHART_BACKGROUND_COLOR } } };
150 | const chart = createChart(document.getElementById('container'), chartOptions);
151 | const lineSeries = chart.addSeries(LineSeries, { color: LINE_LINE_COLOR });
152 | 
153 | const data = [{ value: 0, time: 1642425322 }, { value: 8, time: 1642511722 }, { value: 10, time: 1642598122 }, { value: 20, time: 1642684522 }, { value: 3, time: 1642770922 }, { value: 43, time: 1642857322 }, { value: 41, time: 1642943722 }, { value: 43, time: 1643030122 }, { value: 56, time: 1643116522 }, { value: 46, time: 1643202922 }];
154 | 
155 | lineSeries.setData(data);
156 | 
157 | chart.timeScale().fitContent();
158 | `;
159 | 
160 | <CodeBlock className="language-js" replaceThemeConstants chart>{lineExample}</CodeBlock>
161 | 
162 | ### Custom series (plugins)
163 | 
164 | The library enables you to create custom series types, also known as series plugins, to expand its functionality. With this feature, you can add new series types, indicators, and other visualizations.
165 | 
166 | To define a custom series type, create a class that implements the [`ICustomSeriesPaneView`](/api/interfaces/ICustomSeriesPaneView.md) interface. This class defines the rendering code that Lightweight Charts&trade; uses to draw the series on the chart.
167 | Once your custom series type is defined, it can be added to any chart instance using the [`addCustomSeries()`](/api/interfaces/IChartApi.md#addcustomseries) method. Custom series types function like any other series.
168 | 
169 | For more information, refer to the [Plugins](./plugins/intro.md) article.
170 | 
171 | ## Customization
172 | 
173 | Each series type offers a unique set of customization options listed on the [`SeriesStyleOptionsMap`](/api/interfaces/SeriesStyleOptionsMap.md) page.
174 | 
175 | You can adjust series options in two ways:
176 | 
177 | - Specify the default options using the corresponding parameter while creating a series:
178 | 
179 |     ```js
180 |     // Change default top & bottom colors of an area series in creating time
181 |     const series = chart.addSeries(AreaSeries, {
182 |         topColor: 'red',
183 |         bottomColor: 'green',
184 |     });
185 |     ````
186 | 
187 | - Use the [`ISeriesApi.applyOptions`](/api/interfaces/ISeriesApi.md#applyoptions) method to apply other options on the fly:
188 | 
189 |     ```js
190 |     // Updating candlestick series options on the fly
191 |     candlestickSeries.applyOptions({
192 |         upColor: 'red',
193 |         downColor: 'blue',
194 |     });
195 |     ```
196 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/time-scale.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_position: 5
  3 | ---
  4 | 
  5 | # Time scale
  6 | 
  7 | ## Overview
  8 | 
  9 | Time scale (or time axis) is a horizontal scale that displays the time of data points at the bottom of the chart.
 10 | 
 11 | ![Time scale](/img/time-scale.png "Time scale")
 12 | 
 13 | The horizontal scale can also represent price or other custom values. Refer to the [Chart types](/chart-types.mdx) article for more information.
 14 | 
 15 | ### Time scale appearance
 16 | 
 17 | Use [`TimeScaleOptions`](/api/interfaces/TimeScaleOptions.md) to adjust the time scale appearance. You can specify these options in two ways:
 18 | 
 19 | - On chart initialization. To do this, provide the desired options as a [`timeScale`](api/interfaces/ChartOptionsBase#timescale) parameter when calling [`createChart`](/api/functions/createChart.md).
 20 | - On the fly using either the [`ITimeScaleApi.applyOptions`](/api/interfaces/ITimeScaleApi.md#applyoptions) or [`IChartApi.applyOptions`](/api/interfaces/IChartApi.md#applyoptions) method. Both methods produce the same result.
 21 | 
 22 | ### Time scale API
 23 | 
 24 | Call the [`IChartApi.timeScale`](/api/interfaces/IChartApi.md#timescale) method to get an instance of the [`ITimeScaleApi`](/api/interfaces/ITimeScaleApi.md) interface. This interface provides an extensive API for controlling the time scale. For example, you can adjust the visible range, convert a time point or [index](/api/type-aliases/Logical.md) to a coordinate, and subscribe to events.
 25 | 
 26 | ```javascript
 27 | chart.timeScale().resetTimeScale();
 28 | ```
 29 | 
 30 | ## Visible range
 31 | 
 32 | Visible range is a chart area that is currently visible on the canvas. This area can be measured with both [data](#data-range) and [logical](#logical-range) range.
 33 | Data range usually includes bar timestamps, while logical range has bar indices.
 34 | 
 35 | You can adjust the visible range using the following methods:
 36 | 
 37 | - [`setVisibleRange`]
 38 | - [`getVisibleRange`]
 39 | - [`setVisibleLogicalRange`]
 40 | - [`getVisibleLogicalRange`]
 41 | 
 42 | ### Data range
 43 | 
 44 | The data range includes only values from the first to the last bar visible on the chart. If the visible area has empty space, this part of the scale is not included in the data range.
 45 | 
 46 | Note that you cannot extrapolate time with the [`setVisibleRange`] method. For example, the chart does not have data prior `2018-01-01` date. If you set the visible range from `2016-01-01`, it will be automatically adjusted to `2018-01-01`.
 47 | 
 48 | If you want to adjust the visible range more flexible, operate with the [logical range](#logical-range) instead.
 49 | 
 50 | ### Logical range
 51 | 
 52 | The logical range represents a continuous line of values. These values are logical [indices](/api/type-aliases/Logical.md) on the scale that illustrated as red lines in the image below:
 53 | 
 54 | ![Logical range](/img/logical-range.png "Logical range")
 55 | 
 56 | The logical range starts from the first data point across all series, with negative indices before it and positive ones after.
 57 | 
 58 | The indices can have fractional parts. The integer part represents the fully visible bar, while the fractional part indicates partial visibility. For example, the `5.2` index means that the fifth bar is fully visible, while the sixth bar is 20% visible.
 59 | A half-index, such as `3.5`, represents the middle of the bar.
 60 | 
 61 | In the library, the logical range is represented with the [`LogicalRange`](/api/type-aliases/LogicalRange.md) object. This object has the `from` and `to` properties, which are logical indices on the time scale. For example, the visible logical range on the chart above is approximately from `-4.73` to `5.05`.
 62 | 
 63 | The [`setVisibleLogicalRange`] method allows you to specify the visible range beyond the bounds of the available data. This can be useful for setting a [chart margin](#chart-margin) or aligning series visually.
 64 | 
 65 | ## Chart margin
 66 | 
 67 | Margin is the space between the chart's borders and the series. It depends on the following time scale options:
 68 | 
 69 | - [`barSpacing`](/api/interfaces/TimeScaleOptions.md#barspacing). The default value is `6`.
 70 | - [`rightOffset`](/api/interfaces/TimeScaleOptions.md#rightoffset). The default value is `0`.
 71 | 
 72 | You can specify these options as described in [above](#time-scale-appearance).
 73 | 
 74 | Note that if a series contains only a few data points, the chart may have a large margin on the left side.
 75 | 
 76 | ![A series with a few points](/img/extra-margin.png)
 77 | 
 78 | In this case, you can call the [`fitContent`](/api/interfaces/ITimeScaleApi.md#fitcontent) method that adjust the view and fits all data within the chart.
 79 | 
 80 | ```javascript
 81 | chart.timeScale().fitContent();
 82 | ```
 83 | 
 84 | If calling `fitContent` has no effect, it might be due to how the library displays data.
 85 | 
 86 | The library allocates specific width for each data point to maintain consistency between different chart types.
 87 | For example, for line series, the plot point is placed at the center of this allocated space, while candlestick series use most of the width for the candle body.
 88 | The allocated space for each data point is proportional to the chart width.
 89 | As a result, series with fewer data points may have a small margin on both sides.
 90 | 
 91 | ![Margin](/img/margin.png)
 92 | 
 93 | You can specify the [logical range](#logical-range) with the [`setVisibleLogicalRange`](/api/interfaces/ITimeScaleApi.md#setvisiblelogicalrange) method to display the series exactly to the edges.
 94 | For example, the code sample below adjusts the range by half a bar-width on both sides.
 95 | 
 96 | ```javascript
 97 | const vr = chart.timeScale().getVisibleLogicalRange();
 98 | chart.timeScale().setVisibleLogicalRange({ from: vr.from + 0.5, to: vr.to - 0.5 });
 99 | ```
100 | 
101 | [`setVisibleRange`]: /api/interfaces/ITimeScaleApi.md#setvisiblerange
102 | [`getVisibleRange`]: /api/interfaces/ITimeScaleApi.md#getvisiblerange
103 | [`setVisibleLogicalRange`]: /api/interfaces/ITimeScaleApi.md#setvisiblelogicalrange
104 | [`getVisibleLogicalRange`]: /api/interfaces/ITimeScaleApi.md#getvisiblelogicalrange
105 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-5.0/time-zones.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 6
 3 | ---
 4 | # Time zones
 5 | 
 6 | ## Overview
 7 | 
 8 | Lightweight Charts™ **does not** natively **support** time zones. If necessary, you should handle time zone adjustments manually.
 9 | 
10 | The library processes all date and time values in UTC. To support time zones, adjust each bar's timestamp in your dataset based on the appropriate time zone offset.
11 | Therefore, a UTC timestamp should correspond to the local time in the target time zone.
12 | 
13 | Consider the example. A data point has the `2021-01-01T10:00:00.000Z` timestamp in UTC. You want to display it in the `Europe/Moscow` time zone, which has the `UTC+03:00` offset according to the [IANA time zone database](https://www.iana.org/time-zones). To do this, adjust the original UTC timestamp by adding 3 hours. Therefore, the new timestamp should be `2021-01-01T13:00:00.000Z`.
14 | 
15 | :::info
16 | 
17 | When converting time zones, consider the following:
18 | 
19 | - Adding a time zone offset could change not only the time but the date as well.
20 | - An offset may vary due to DST (Daylight Saving Time) or other regional adjustments.
21 | - If your data is measured in business days and does not include a time component, in most cases, you should not adjust it to a time zone.
22 | 
23 | :::
24 | 
25 | ## Approaches
26 | 
27 | Consider the approaches below to convert time values to the required time zone.
28 | 
29 | ### Using pure JavaScript
30 | 
31 | For more information on this approach, refer to [StackOverflow](https://stackoverflow.com/a/54127122/3893439).
32 | 
33 | ```js
34 | function timeToTz(originalTime, timeZone) {
35 |     const zonedDate = new Date(new Date(originalTime * 1000).toLocaleString('en-US', { timeZone }));
36 |     return zonedDate.getTime() / 1000;
37 | }
38 | ```
39 | 
40 | If you only need to support a client (local) time zone, you can use the following function:
41 | 
42 | ```js
43 | function timeToLocal(originalTime) {
44 |     const d = new Date(originalTime * 1000);
45 |     return Date.UTC(d.getFullYear(), d.getMonth(), d.getDate(), d.getHours(), d.getMinutes(), d.getSeconds(), d.getMilliseconds()) / 1000;
46 | }
47 | ```
48 | 
49 | ### Using the date-fns-tz library
50 | 
51 | You can use the `utcToZonedTime` function from the [`date-fns-tz`](https://github.com/marnusw/date-fns-tz) library as follows:
52 | 
53 | ```js
54 | import { utcToZonedTime } from 'date-fns-tz';
55 | 
56 | function timeToTz(originalTime, timeZone) {
57 |     const zonedDate = utcToZonedTime(new Date(originalTime * 1000), timeZone);
58 |     return zonedDate.getTime() / 1000;
59 | }
60 | ```
61 | 
62 | ### Using the IANA time zone database
63 | 
64 | If you process a large dataset and approaches above do not meet your performance requirements, consider using the [`tzdata`](https://www.npmjs.com/package/tzdata).
65 | 
66 | This approach can significantly improve performance for the following reasons:
67 | 
68 | - You do not need to calculate the time zone offset for every data point individually. Instead, you can look up the correct offset just once for the first timestamp using a fast binary search.
69 | - After finding the starting offset, you go through the rest data and check whether an offset should be changed, for example, because of DST starting/ending.
70 | 
71 | ## Why are time zones not supported?
72 | 
73 | The approaches above were not implemented in Lightweight Charts™ for the following reasons:
74 | 
75 | - Using [pure JavaScript](#using-pure-javascript) is slow. In our tests, processing 100,000 data points took over 20 seconds.
76 | - Using the [date-fns-tz library](#using-the-date-fns-tz-library) introduces additional dependencies and is also slow. In our tests, processing 100,000 data points took 18 seconds.
77 | - Incorporating the [IANA time zone database](#using-the-iana-time-zone-database) increases the bundle size by [29.9 kB](https://bundlephobia.com/package/tzdata), which is nearly the size of the entire Lightweight Charts™ library.
78 | 
79 | Since time zone support is not required for all users, it is intentionally left out of the library to maintain high performance and a lightweight package size.
80 | 


--------------------------------------------------------------------------------