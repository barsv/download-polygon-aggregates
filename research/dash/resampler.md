Directory structure:
└── predict-idlab-plotly-resampler/
    ├── README.md
    ├── CHANGELOG.md
    ├── CONTRIBUTING.md
    ├── LICENSE
    ├── Makefile
    ├── mkdocs.yml
    ├── pyproject.toml
    ├── examples/
    │   ├── README.md
    │   ├── datashader.ipynb
    │   ├── figurewidget_example.ipynb
    │   ├── helper.py
    │   ├── requirements.txt
    │   ├── dash_apps/
    │   │   ├── 01_minimal_global.py
    │   │   ├── 02_minimal_cache.py
    │   │   ├── 03_minimal_cache_dynamic.py
    │   │   ├── 04_minimal_cache_overview.py
    │   │   ├── 05_cache_overview_subplots.py
    │   │   ├── 06_cache_overview_range_buttons.py
    │   │   ├── 11_sine_generator.py
    │   │   ├── 12_file_selector.py
    │   │   ├── 13_coarse_fine.py
    │   │   └── utils/
    │   │       ├── callback_helpers.py
    │   │       └── graph_construction.py
    │   ├── example_utils/
    │   │   └── loglttb.py
    │   └── other_apps/
    │       └── streamlit_app.py
    ├── mkdocs/
    │   ├── dash_app_integration.md
    │   ├── FAQ.md
    │   ├── gen_ref_pages.py
    │   ├── getting_started.md
    │   └── index.md
    ├── plotly_resampler/
    │   ├── __init__.py
    │   ├── registering.py
    │   ├── aggregation/
    │   │   ├── __init__.py
    │   │   ├── aggregation_interface.py
    │   │   ├── aggregators.py
    │   │   ├── gap_handler_interface.py
    │   │   ├── gap_handlers.py
    │   │   └── plotly_aggregator_parser.py
    │   └── figure_resampler/
    │       ├── __init__.py
    │       ├── figure_resampler.py
    │       ├── figurewidget_resampler.py
    │       ├── jupyter_dash_persistent_inline_output.py
    │       ├── utils.py
    │       └── assets/
    │           └── coarse_fine.js
    ├── tests/
    │   ├── __init__.py
    │   ├── conftest.py
    │   ├── fr_selenium.py
    │   ├── test_aggregators.py
    │   ├── test_figure_resampler_selenium.py
    │   ├── test_multiple_axes.py
    │   ├── test_plotly_express.py
    │   ├── test_rangeslider.py
    │   ├── test_registering.py
    │   ├── test_serialization.py
    │   ├── test_utils.py
    │   └── utils.py
    └── .github/
        ├── FUNDING.yml
        ├── ISSUE_TEMPLATE/
        │   └── bug_report.md
        └── workflows/
            ├── codeql.yml
            ├── deploy-mkdocs.yml
            ├── lint.yml
            └── test.yml


Files Content:

(Files content cropped to 300k characters, download full ingest to see more)
================================================
FILE: README.md
================================================
<p align="center">
    <a href="#readme">
        <img alt="Plotly-Resampler logo" src="https://raw.githubusercontent.com/predict-idlab/plotly-resampler/main/mkdocs/static/logo.svg" width=65%>
    </a>
</p>

[![PyPI Latest Release](https://img.shields.io/pypi/v/plotly-resampler.svg)](https://pypi.org/project/plotly-resampler/)
[![support-version](https://img.shields.io/pypi/pyversions/plotly-resampler)](https://img.shields.io/pypi/pyversions/plotly-resampler)
[![codecov](https://img.shields.io/codecov/c/github/predict-idlab/plotly-resampler?logo=codecov)](https://codecov.io/gh/predict-idlab/plotly-resampler)
[![CodeQL](https://github.com/predict-idlab/plotly-resampler/actions/workflows/codeql.yml/badge.svg)](https://github.com/predict-idlab/plotly-resampler/actions/workflows/codeql.yml)
[![Downloads](https://static.pepy.tech/badge/plotly-resampler)](https://pepy.tech/project/plotly-resampler)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?)](http://makeapullrequest.com)
[![Testing](https://github.com/predict-idlab/plotly-resampler/actions/workflows/test.yml/badge.svg)](https://github.com/predict-idlab/plotly-resampler/actions/workflows/test.yml)
[![Documentation](https://img.shields.io/badge/read%20our%20docs!-informational)](https://predict-idlab.github.io/plotly-resampler/latest)
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?logo=discord&logoColor=white)](https://discord.gg/k2d59GrxPX)

<!-- [![Downloads](https://pepy.tech/badge/plotly-resampler)](https://pepy.tech/project/plotly-resampler) -->

> `plotly_resampler`: visualize large sequential data by **adding resampling functionality to Plotly figures**

`plotly-resampler` improves the scalability of [Plotly](https://github.com/plotly/plotly.py) for visualizing large time series datasets. Specifically, our library _dynamically_ **aggregates time-series data respective to the current graph view**, ensuring efficient and responsive updates during user interactions like panning or zooming via callbacks.

This core aggregation functionality is achieved by utilizing by _time-series data point selection algorithms_, for which `plotly-resampler` leverages the highly optimized implementations available in [tsdownsample](https://github.com/predict-idlab/tsdownsample). Our default data aggregation method is `MinMaxLTTB` (and selects 1000 data points for plotting). For a deeper understanding of this method, you can consult to the algorithm's dedicated [MinMaxLTTB repository](https://github.com/predict-idlab/MinMaxLTTB) and the associated [research paper](https://arxiv.org/abs/2305.00332).

![basic example gif](https://raw.githubusercontent.com/predict-idlab/plotly-resampler/main/mkdocs/static/basic_example.gif)

In [this Plotly-Resampler demo](https://github.com/predict-idlab/plotly-resampler/blob/main/examples/basic_example.ipynb) over `110,000,000` data points are visualized!

<!-- These dynamic aggregation callbacks are realized with: -->
<!-- * [Dash](https://github.com/plotly/dash) when a `go.Figure` object is wrapped with dynamic aggregation functionality, see example ⬆️. -->
<!-- * The [FigureWidget.layout.on_change](https://plotly.com/python-api-reference/generated/plotly.html?highlight=on_change#plotly.basedatatypes.BasePlotlyType.on_change) method, when a `go.FigureWidget` is used within a `.ipynb` environment. -->

<!-- #### Useful links -->

<!-- - [Documentation]() work in progress 🚧  -->
<!-- - [Example notebooks](https://github.com/predict-idlab/plotly-resampler/tree/main/examples/) -->

### 🛠️ Installation

| [**pip**](https://pypi.org/project/plotly_resampler/) | `pip install plotly-resampler` |
| ---| ----|
<!-- | [**conda**](https://anaconda.org/conda-forge/plotly_resampler/) | `conda install -c conda-forge plotly_resampler` | -->

<br>
<details><summary><b>👀 What is the difference between plotly-resampler figures and plain plotly figures?</b></summary>

`plotly-resampler` can be thought of as wrapper around plain plotly figures which adds visualization scalability to line-charts by dynamically aggregating the data w.r.t. the front-end view. `plotly-resampler` thus adds dynamic aggregation functionality to plain plotly figures.

**❗ Important to know**:

* ``show`` *always* generates a static HTML view of the figure, prohibiting dynamic aggregation.
* To have dynamic aggregation:
  * Use `show_dash` with `FigureResampler` to initiate a **Dash** app to realize the dynamic aggregation with **callbacks**.<br>(or output the object in a cell via ``IPython.display``), which will also spawn a dash-web app
  * with ``FigureWidgetResampler``, you need to use ``IPython.display`` on the object, which uses widget-events to realize dynamic aggregation (via the running **IPython kernel**).

**Other changes of plotly-resampler figures w.r.t. vanilla plotly**:

* **double-clicking** within a line-chart area **does not Reset Axes**, as it results in an “Autoscale” event. We decided to implement an Autoscale event as updating your y-range such that it shows all the data that is in your x-range.
   * **Note**: vanilla Plotly figures their Autoscale result in Reset Axes behavior, in our opinion this did not make a lot of sense. It is therefore that we have overriden this behavior in plotly-resampler.
</details><br>

### 📋 Features

  * **Convenient** to use:
    * just add either
      * `register_plotly_resampler` function to your notebook with the best suited `mode` argument.
      * `FigureResampler` decorator around a plotly Figure and call `.show_dash()`
      * `FigureWidgetResampler` decorator around a plotly Figure and output the instance in a cell
    * allows all other plotly figure construction flexibility to be used!
  * **Environment-independent**
    * can be used in Jupyter, vscode-notebooks, Pycharm-notebooks, Google Colab, DataSpell, and even as application (on a server)
  * Interface for **various aggregation algorithms**:
    * ability to develop or select your preferred sequence aggregation method

## 🚀 Usage

**Add dynamic aggregation** to your plotly Figure _(unfold your fitting use case)_
* 🤖 <b>Automatically</b> _(minimal code overhead)_:
  <details><summary>Use the <code>register_plotly_resampler</code> function</summary>
    <br>

    1. Import and call the `register_plotly_resampler` method
    2. Just use your regular graph construction code

    * **code example**:
      ```python
      import plotly.graph_objects as go; import numpy as np
      from plotly_resampler import register_plotly_resampler

      # Call the register function once and all Figures/FigureWidgets will be wrapped
      # according to the register_plotly_resampler its `mode` argument
      register_plotly_resampler(mode='auto')

      x = np.arange(1_000_000)
      noisy_sin = (3 + np.sin(x / 200) + np.random.randn(len(x)) / 10) * x / 1_000


      # auto mode: when working in an IPython environment, this will automatically be a 
      # FigureWidgetResampler else, this will be an FigureResampler
      f = go.Figure()
      f.add_trace({"y": noisy_sin + 2, "name": "yp2"})
      f
      ```

    > **Note**: This wraps **all** plotly graph object figures with a 
    > `FigureResampler` | `FigureWidgetResampler`. This can thus also be 
    > used for the `plotly.express` interface. 🎉

  </details>

* 👷 <b>Manually</b> _(higher data aggregation configurability, more speedup possibilities)_:
  * Within a <b><i>jupyter</i></b> environment without creating a <i>web application</i>
    1. wrap the plotly Figure with `FigureWidgetResampler`
    2. output the `FigureWidgetResampler` instance in a cell
      ```python
      import plotly.graph_objects as go; import numpy as np
      from plotly_resampler import FigureResampler, FigureWidgetResampler

      x = np.arange(1_000_000)
      noisy_sin = (3 + np.sin(x / 200) + np.random.randn(len(x)) / 10) * x / 1_000

      # OPTION 1 - FigureWidgetResampler: dynamic aggregation via `FigureWidget.layout.on_change`
      fig = FigureWidgetResampler(go.Figure())
      fig.add_trace(go.Scattergl(name='noisy sine', showlegend=True), hf_x=x, hf_y=noisy_sin)

      fig
      ```
  * Using a <b><i>web-application</i></b> with <b><a href="https://github.com/plotly/dash">dash</a></b> callbacks
    1. wrap the plotly Figure with `FigureResampler`
    2. call `.show_dash()` on the `Figure`
      ```python
      import plotly.graph_objects as go; import numpy as np
      from plotly_resampler import FigureResampler, FigureWidgetResampler

      x = np.arange(1_000_000)
      noisy_sin = (3 + np.sin(x / 200) + np.random.randn(len(x)) / 10) * x / 1_000

      # OPTION 2 - FigureResampler: dynamic aggregation via a Dash web-app
      fig = FigureResampler(go.Figure())
      fig.add_trace(go.Scattergl(name='noisy sine', showlegend=True), hf_x=x, hf_y=noisy_sin)

      fig.show_dash(mode='inline')
      ```
  > **Tip** 💡:
   > For significant faster initial loading of the Figure, we advise to wrap the 
   > constructor of the plotly Figure and add the trace data as `hf_x` and `hf_y`

<br>

> **Note**:
> Any plotly Figure can be wrapped with `FigureResampler` and `FigureWidgetResampler`! 🎉
> But **only** the `go.Scatter`/`go.Scattergl` **traces are resampled**.

## 💭 Important considerations & tips

* When running the code on a server, you should forward the port of the `FigureResampler.show_dash()` method to your local machine.<br>
  **Note** that you can add dynamic aggregation to plotly figures with the `FigureWidgetResampler` wrapper without needing to forward a port!
* The `FigureWidgetResampler` *uses the IPython main thread* for its data aggregation functionality, so when this main thread is occupied, no resampling logic can be executed. For example; if you perform long computations within your notebook, the kernel will be occupied during these computations, and will only execute the resampling operations that take place during these computations after finishing that computation.
* In general, when using downsampling one should be aware of (possible) [aliasing](https://en.wikipedia.org/wiki/Aliasing) effects.
  The <b style="color:orange">[R]</b> in the legend indicates when the corresponding trace is being resampled (and thus possibly distorted) or not. Additionally, the `~<range>` suffix represent the mean aggregation bin size in terms of the sequence index.
* The plotly **autoscale** event (triggered by the autoscale button or a double-click within the graph), **does not reset the axes but autoscales the current graph-view** of plotly-resampler figures. This design choice was made as it seemed more intuitive for the developers to support this behavior with double-click than the default axes-reset behavior. The graph axes can ofcourse be resetted by using the `reset_axis` button.  If you want to give feedback and discuss this further with the developers, see issue [#49](https://github.com/predict-idlab/plotly-resampler/issues/49).

## 📜 Citation and papers

The paper about the plotly-resampler toolkit itself (preprint): https://arxiv.org/abs/2206.08703

```bibtex
@inproceedings{van2022plotly,
  title={Plotly-resampler: Effective visual analytics for large time series},
  author={Van Der Donckt, Jonas and Van Der Donckt, Jeroen and Deprost, Emiel and Van Hoecke, Sofie},
  booktitle={2022 IEEE Visualization and Visual Analytics (VIS)},
  pages={21--25},
  year={2022},
  organization={IEEE}
}
```

**Related papers**:
- **Visual representativeness** of time series data point selection algorithms (preprint): https://arxiv.org/abs/2304.00900 <br>
  code: https://github.com/predict-idlab/ts-datapoint-selection-vis
-  **MinMaxLTTB** - an efficient data point selection algorithm (preprint): https://arxiv.org/abs/2305.00332 <br>
  code: https://github.com/predict-idlab/MinMaxLTTB


<br>

---

<p align="center">
👤 <i>Jonas Van Der Donckt, Jeroen Van Der Donckt, Emiel Deprost</i>
</p>



================================================
FILE: CHANGELOG.md
================================================
# Latest


# v0.10.0
## New Features
🚨  `Nan` handling has been delegated to the `aggregators`, this implies that `plotly-resampler` does not perform any nan-checks anymore (making it faster) 🐎.

Consequently, we removed the `check_nans` argument of the FigureResampler constructor and its `add_traces` method. This argument was used to check for NaNs in the input data, but this is now handled by the `nan_policy` argument of specific aggregators (see for instance the constructor of the `MinMax` and `MinMaxLTTB` aggregator). 🔍 

## What's Changed
* Address FutureWarning: 'H' is deprecated and will be removed in a future version. Please use 'h' instead of 'H'. by @t-jakubek in https://github.com/predict-idlab/plotly-resampler/pull/291
* :rocket: Python 3.12 support by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/292
* :fire: delegate nan behavior to aggregators by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/294


# v0.9.2
### ⚡ `overview` / `rangeslider` support 🎉 

* ➡️  [code example](https://github.com/predict-idlab/plotly-resampler/blob/main/examples/dash_apps/05_cache_overview_subplots.py):
* 🖍️ [high level docs](https://predict-idlab.github.io/plotly-resampler/v0.9.2/getting_started/#overview)
* 🔍 [API docs](https://predict-idlab.github.io/plotly-resampler/v0.9.2/api/figure_resampler/figure_resampler/#figure_resampler.figure_resampler.FigureResampler.__init__)
  * make sure to take a look at the doc strings of the `create_overview`, `overview_row_idxs`, and `overview_kwargs` arguments of the  `FigureResampler` its constructor.
![Peek 2023-10-25 01-51](https://github.com/predict-idlab/plotly-resampler/assets/38005924/5b3a40e0-f058-4d7e-8303-47e51896347a)



### 💨 remove [traceUpdater](https://github.com/predict-idlab/trace-updater) dash component as a dependency.
> **context**: see #281 #271 
> `traceUpdater` was developed during a period when Dash did not yet contain the [Patch ](https://dash.plotly.com/partial-properties)feature for partial property updates. As such, `traceUpdater` has become somewhat redundant is now effectively replaced with Patch.

🚨 This is a breaking change with previous `Dash` apps!!!

## What's Changed
* Support nested admonitions  by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/245
* 👷 build: create codeql.yml by @NielsPraet in https://github.com/predict-idlab/plotly-resampler/pull/248
* :sparkles: first draft of improved xaxis filtering by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/250
* :arrow_up: update dependencies by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/260
* :muscle: update dash-extensions by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/261
* fix for #263 by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/264
* Rangeslider support by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/254
* :pray: fix mkdocs by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/268
* ✈️  fix for #270 by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/272
* :mag: adding init kwargs to show dash - fix for #265 by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/269
* Refactor/remove trace updater by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/281
* Bug/pop rangeselector by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/279
* :sparkles: fix for #275 by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/286
* Bug/rangeselector by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/287


**Full Changelog**: https://github.com/predict-idlab/plotly-resampler/compare/v0.9.1...v0.9.2


# v0.9.1
## Major changes:
Support for multiple axes. 

The `.GIF` below demonstrates how multiple axes on a subplots can be used to enhance the number of visible traces, without using more (vertical) screen space 🔥!

Make sure to take a look at our [examples](https://github.com/predict-idlab/plotly-resampler/blob/main/examples/other_examples.ipynb)

![Peek 2023-07-13 10-24](https://github.com/predict-idlab/plotly-resampler/assets/38005924/aa5d278f-7baf-4251-91b5-7445eb7d53d0)

## What's Changed (generated)
* :fire: multiple y-axes support by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/244
 

 # v0.9.0
## Major changes:
### Even faster aggregation 🐎
We switched our aggregation backend to [tsdownsample](https://github.com/predict-idlab/tsdownsample), which alleviates the need to compile our C code on non-supported devices, and has parallelization capabilities. 
`tsdownsample` leverages the [argminmax](https://github.com/jvdd/argminmax) crate, which has SIMD-optimized instruction to find vertical extrema really fast! 

With parallelization enabled, you should clearly see a bump in perfomance when visualizing (multiple) large traces! 🐎

### Versioned docs! :party:
We restyled our [documentation](https://predict-idlab.github.io/plotly-resampler/latest) and added versioning! 🎉

https://predict-idlab.github.io/plotly-resampler/latest/

Go check it out! :point_up:

### Other Features
- Support for **log-scale** axes (and thus log-bin-based aggregators) - check [this pull-request](https://github.com/predict-idlab/plotly-resampler/pull/207)
![](https://cdn.discordapp.com/attachments/372491075153166338/1129004610472906782/image.png)

> The above image shows how the `log` aggregator (row2) will use log-scale bins. This can be seen in the 1-1000 range when comparing both subplots. <br>*Note: the shown data has a fixed delta-x of 1. Hence, here are no exact equally spaced bins for the left part of the LogLTTB.*

- Add a fill-value option to gap handlers
![](https://cdn.discordapp.com/attachments/372491075153166338/1129004638016897045/image.png)

> The above image shows how the `fill_value` option can be used to fill gaps with a specific value.<br> This can be of greate use, when you use the `fill='tozeroy'` option in plotly **and gaps occur in your data**, as this will, combined with `line_shape='vh'`, fill the area between the trace and the x-axis and gaps will be a flat zero-line.
### Bugfixes
- support for pandas2.0 intricacies

## What's Changed (generated)
* fix: handle bool dtype for x in LTTB_core_py by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/183
* fix: add colors to streamlit example :art: by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/187
* docs: describe solution in FAQ for slow datetime arrays by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/184
* Rework aggregator interface  by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/186
* :rocket: integrate with tsdownsample by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/191
* refactor: use composition for gap handling by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/199
* ✨ np.array interface implementation by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/154
* 🧹  fix typo in docstring + remove LTTB from MinMaxLTTB + remove interleave_gaps by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/201
* chore: use ruff instead of isort by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/200
* 🌈 adding marker props by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/148
* Datetime bugfix by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/209
* Fixes #210 by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/211
* Log support by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/207
* Datetime range by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/213
* :sparkles: add fill_value option to gap handlers by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/218
* :sparkles: fix `limit_to_view=True` but no gaps inserted bug by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/220
* :bug: convert trace props to array + check for nan removal by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/225
* Figurewidget datetime bug by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/232
* ♻️ deprecate JupyterDash in favor for updated Dash version by @NielsPraet in https://github.com/predict-idlab/plotly-resampler/pull/233
* :eyes: comment out reset layout by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/228
* Docs/versioned docs (#236) by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/237

# v 0.8.0

## Major changes

### Faster aggregation 🐎 
the `lttbc` dependency is removed; and we added our own (faster) lttb C implementation. Additionally we provide a Python fallback when this lttb-C building fails. In the near future, we will look into CIBuildWheels to build the wheels for the major OS & Python matrix versions.  
A well deserved s/o to [dgoeris/lttbc](https://github.com/dgoeries/lttbc), who heavily inspired our implementation!

### Figure Output serialization 📸 
Plotly-resampler now also has the option to store the output figure as an Image in notebook output. As long the notebook is connected, the interactive plotly-resampler figure is shown; but once the figure / notebook isn't connected anymore, a static image will be rendered in the notebook output.

## What's Changed (generated)
* :bug: return self when calling add_traces by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/75
* :fire: add streamlit integration example by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/80
* ✨ adding `convert_traces_kwargs` by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/81
* Fix numeric `hf_y` input as dtype object by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/90
* :fire: add support for figure dict input + propagate _grid_str by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/92
* :pray: fix tests for all OS by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/95
* Add python3dot10 by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/96
* :sunrise: FigureResampler display improvements by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/97
* :package: serialization support +  :level_slider: update OS & python version in test-matrix by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/87
* Lttbv2 🍒 ⛏️  branch by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/103
* :robot: hack together output retention in notebooks by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/105
* :package: improve docs by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/104

& some other minor bug fixes :see_no_evil: 

**Full Changelog**: https://github.com/predict-idlab/plotly-resampler/compare/v0.7.0...v0.8.0

---

# V0.7.0

## What's Changed

**You can register plotly_resampler**; this adds dynamic resampling functionality *under the hood* to plotly.py! 🥳
As a result, you can stop wrapping plotly figures with a plotly-resampler decorator (as this all happens automatically) 
> You only need to call the `register_plotly_resampler` method and all plotly figures will be wrapped (under the hood) according to that method's configuration.

-> More info in the [README](https://github.com/predict-idlab/plotly-resampler#usage) and [docs](https://predict-idlab.github.io/plotly-resampler/getting_started.html#how-to-use)!

Aditionally, all resampler Figures are now composable; implying that they can be decorated by themselves and all other types of plotly-(resampler) figures. This eases the switching from a FigureResampler to FigureWidgetResampler and vice-versa.


## What's Changed (PR's)
* 🦌 Adding reset-axes functionality by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/48
* 🐛 Small bugfixes by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/52
* 🔍  investigating gap-detection methodology by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/53
* :mag: fix float index problem of #63 by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/64
* :wrench: hotfix for rounding error by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/66
* 🗳️ Compose figs by @jonasvdd in https://github.com/predict-idlab/plotly-resampler/pull/72
* :sparkles: register plotly-resampler by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/70
* :robot: update dependencies + new release by @jvdd in https://github.com/predict-idlab/plotly-resampler/pull/74


**Full Changelog**: https://github.com/predict-idlab/plotly-resampler/compare/v0.6.0...v0.7.0


================================================
FILE: CONTRIBUTING.md
================================================
# How to contribute

First of all, thank you for considering contributing to `plotly-resampler`.<br>
It's people like you that will help make `plotly-resampler` a great toolkit. 🤝

As usual, contributions are managed through GitHub Issues and Pull Requests.  
We invite you to use GitHub's [Issues](https://github.com/predict-idlab/plotly-resampler/issues) to report bugs, request features, or ask questions about the project. To ask use-specific questions, please use the [Discussions](https://github.com/predict-idlab/plotly-resampler/discussions) instead.

If you are new to GitHub, you can read more about how to contribute [here](https://docs.github.com/en/get-started/quickstart/contributing-to-projects).

## How to develop locally

*Note: this guide is tailored to developers using linux*

The following steps assume that your console is at the root folder of this repository.

### Create a new (poetry) Python environment

It is best practice to use a new Python environment when starting on a new project.

We describe two options; 

<details>
<summary><i>Advised option</i>: using poetry shell</summary>
For dependency management we use poetry (read more below).<br>
Hence, we advise to use poetry shell to create a Python environment for this project.

1. Install poetry: https://python-poetry.org/docs/#installation <br>
   (If necessary add poetry to the PATH)
2. Create & activate a new python environment: <code>poetry shell</code>

After the poetry shell command your python environment is activated.
</details>

<details>
<summary><i>Alternative option</i>: using python-venv</summary>
As alternative option, you can create a Python environment by using python-venv

1. Create a new Python environment: <code>python -m venv venv</code>
2. Activate this environment; <code>source venv/bin/activate</code>
</details>

Make sure that this environment is activated when developing (e.g., installing dependencies, running tests).


### Installing & building the dependencies

We use [`poetry`](https://python-poetry.org/) as dependency manager for this project. 
- The dependencies for installation & development are written in the [`pyproject.toml`](pyproject.toml) file (which is quite similar to a requirements.txt file). 
- To ensure that package versions are consistent with everyone who works on this project poetry uses a [`poetry.lock`](poetry.lock) file (read more [here](https://python-poetry.org/docs/basic-usage/#installing-with-poetrylock)).

To install the requirements
```sh
pip install poetry          # install poetry (if you do use the venv option)
poetry install --all-extras # install all the dependencies
```

### Formatting the code

We use [`black`](https://github.com/psf/black) and [`ruff`](https://github.com/charliermarsh/ruff) to format the code.

To format the code, run the following command (more details in the [`Makefile`](Makefile)):
```sh
make format
```

### Checking the linting

We use [`ruff`](https://github.com/charliermarsh/ruff) to check the linting.

To check the linting, run the following command (more details in the [`Makefile`](Makefile)):
```sh
make lint
```

### Running the tests (& code coverage)

You can run the tests with the following code (more details in the [`Makefile`](Makefile)):

```sh
make test
```

To get the selenium tests working you should have Google Chrome installed.

If you want to visually follow the selenium tests;
* change the `TESTING_LOCAL` variable in [`tests/conftest.py`](tests/conftest.py) to `True`

### Generating the docs

When you've added or updated a feature; it is always a good practice to alter the 
documentation and [changelog.md](CHANGELOG.md).

The current listing below gives you the provided steps to regenerate the documentation.

1. Make sure that your python env is active (e.g., by running `poetry shell`)
2. Navigate to `docs/sphinx` and run from that directory:
```bash
sphinx-autogen -o _autosummary && make clean html
```

---

Bonus points for contributions that include a performance analysis with a benchmark script and profiling output (please report on the GitHub issue).




================================================
FILE: LICENSE
================================================
MIT License

Copyright (c) 2023 Jonas Van Der Donckt, Jeroen Van Der Donckt, Emiel Deprost.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


================================================
FILE: Makefile
================================================
black = black plotly_resampler examples tests

.PHONY: format
format:
	ruff --fix plotly_resampler tests
	$(black)

.PHONY: lint
lint:
	poetry run ruff plotly_resampler tests
	poetry run $(black) --check --diff

.PHONY: test
test:
	poetry run pytest --cov-report term-missing --cov=plotly_resampler tests

.PHONY: docs
docs:
	poetry run mkdocs build -c -f mkdocs.yml

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf *.egg-info
	rm -f .coverage
	rm -rf build

	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -f `find . -type f -name '*.cpython-*' `



================================================
FILE: mkdocs.yml
================================================
site_name: Plotly Resampler Documentation
site_url: https://predict-idlab.github.io/plotly-resampler/
repo_url: https://github.com/predict-idlab/plotly-resampler
repo_name: plotly-resampler
site_description: Documentation for the Plotly Resampler; a wrapper for plotly Figures to visualize large time-series data.
site_author:
docs_dir: mkdocs

nav:
  - "Get started 🚀": "getting_started.md"
  - "Dash apps 🤝": "dash_app_integration.md"
  - "API 📖": "api/"
  - "FAQ ❓": "FAQ.md"

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight
  - pymdownx.inlinehilite
  - attr_list
  - sane_lists
  - smarty
  - toc:
      permalink: true
  - pymdownx.emoji:
      emoji_index: !!python/name:materialx.emoji.twemoji
      emoji_generator: !!python/name:materialx.emoji.to_svg

plugins:
  - mike
  - search
  - gen-files:
      scripts:
        - mkdocs/gen_ref_pages.py
  - literate-nav:
      nav_file: SUMMARY.md
  - section-index
  - mkdocstrings:
      default_handler: python
      handlers:
        python:
          paths: [plotly_resampler]
          options:
            docstring_style: numpy

theme:
  name: material
  locale: en
  logo: static/icon.png
  features:
    - navigation.tabs
    - navigation.path
    - content.code.copy
  palette:
    # Palette toggle for light mode
    - scheme: default
      primary: teal
      toggle:
        icon: material/weather-night

        name: Switch to dark mode

    # Palette toggle for dark mode
    - scheme: slate
      primary: black
      toggle:
        icon: material/weather-sunny
        name: Switch to light mode
  icon:
    repo: fontawesome/brands/github

extra:
  version:
    provider: mike



================================================
FILE: pyproject.toml
================================================
[tool.poetry]
name = "plotly-resampler"  # Do not forget to update the __init__.py __version__ variable
version = "0.11.0rc1"
description = "Visualizing large time series with plotly"
authors = ["Jonas Van Der Donckt", "Jeroen Van Der Donckt", "Emiel Deprost"]
readme = "README.md"
license = "MIT"
repository = "https://github.com/predict-idlab/plotly-resampler"
documentation = "https://predict-idlab.github.io/plotly-resampler/latest"
keywords = ["time-series", "visualization", "resampling", "plotly", "plotly-dash"]
packages = [
    { include = "plotly_resampler" }
]
include = [
    # C extensions must be included in the wheel distributions
    {path = "plotly_resampler/aggregation/algorithms/*.so", format = "wheel"},
    {path = "plotly_resampler/aggregation/algorithms/*.pyd", format = "wheel"}
]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Operating System :: POSIX :: Linux",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
]

[tool.poetry.dependencies]
python = "^3.8"
plotly = ">=5.5.0,<7.0.0"
dash = ">=2.11.0"  # from dash 2.11, jupyter support is included
pandas =[
    { version = ">=1", python = "<3.13" },
    { version = ">=2.2.3", python = ">=3.13" }
] 
numpy = [
    { version = ">=1.14", python = "<3.11" },
    { version = ">=1.24", python = ">=3.11,<3.13" },
    { version = ">=2.0", python = ">=3.13" }
]
orjson = "^3.10.0"  # Faster json serialization (from 3.10 onwards f16 is supported)
# Optional dependencies
Flask-Cors = { version = "^4.0.2", optional = true }
# Lock kaleido dependency until https://github.com/plotly/Kaleido/issues/156 is resolved
kaleido = {version = "0.2.1", optional = true}
tsdownsample = ">=0.1.3"

[tool.poetry.extras]
# Optional dependencies
inline_persistent = ["kaleido", "Flask-Cors", "ipython"]

[tool.poetry.dev-dependencies]
pytest = "^7.2.0"
pytest-cov = "^3.0.0"
selenium = "4.2.0"
pytest-selenium = "^2.0.1"
blinker= "1.7.0"   # we need version 1.7.0  (otherwise we get a blinker._saferef module not found error
selenium-wire = "^5.0"
pyarrow = [
    {version = ">=15.0", python = "<3.13"},
    {version = ">=18.0", python = ">=3.13"},
]
ipywidgets = "^7.7.1" # needs to be v7 in order to support serialization
memory-profiler = "^0.60.0"
line-profiler = "^4.0"
ruff = "^0.0.262"
black = "^24.3.0"
pytest-lazy-fixture = "^0.6.3"
# yep = "^0.4"  # c code profiling
mkdocs = "^1.5.3"
mkdocstrings = "^0.20.0"
mkdocstrings-python = "^1.7.3"
griffe = ">=0.32.0" 
mkdocs-gen-files = "^0.5.0"
mike = "^1.1.2"
mkdocs-material = "^9.1.18"
mkdocs-literate-nav = "^0.6.0"
mkdocs-section-index = "^0.3.5"
cffi = ">=1.16"
anywidget = "^0.9.13"

# Linting
[tool.ruff]
select = ["E", "F", "I"]
line-length = 88
ignore = ["E501"] # Never enforce `E501` (line length violations).
[tool.ruff.per-file-ignores]
"tests/test_registering.py" = ["F401", "F811"]
"tests/test_serialization.py" = ["F401", "F811"]

# Formatting
[tool.black]
line-length = 88

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"



================================================
FILE: examples/README.md
================================================
# plotly-resampler examples

This directory withholds several examples, highlighting the applicability of plotly-resampler for various use cases.


## Prerequisites

To successfully run these examples, make sure that you've installed all the [requirements](requirements.txt) by running:
```bash
pip install -r requirements.txt
```

## 1. Example notebooks
### 1.1 basic examples

The [basic example notebook](basic_example.ipynb) covers most use-cases in which plotly-resampler will be employed. It serves as an ideal starting point for data-scientists who want to use plotly-resampler in their day-to-day jupyter environments.

Additionally, this notebook also shows some more advanced functionalities, such as:
* Retaining (a static) plotly-resampler figure in your notebook
* How to utilize an x-axis overview (i.e., a rangeslider) to navigate through your time series
* Showing how to style the marker color and size of plotly-resampler figures
* Adjusting trace data of plotly-resampler figures at runtime
* How to add (shaded) confidence bounds to your time series
* The flexibility of configuring different aggregation-algorithms and number of shown samples per trace
* How plotly-resampler can be used for logarithmic x-axes and an implementation of a logarithmic aggregation algorithm, i.e., [LogLTTB](example_utils/loglttb.py)
* Using different `fill_value` for gap handling of filled area plots.
* Using multiple y-axes in a single subplot (see the [other_examples](other_examples.ipynb))

**Note**: the basic example notebook requires `plotly-resampler>=0.9.0rc3`.

### 1.2 Figurewidget example

The [figurewidget example notebook](figurewidget_example.ipynb) utilizes the `FigureWidgetResampler` wrapper to create a `go.FigureWidget` with dynamic aggregation functionality. A major advantage of this approach is that this does not create a web application, avoiding starting an application on a port (and forwarding that port when working remotely).

Additionally, this notebook highlights how to use the `FigureWidget` its on-click callback to utilize plotly for large **time series annotation**.

## 2. Dash apps

The [dash_apps](dash_apps/) folder contains example dash apps in which `plotly-resampler` is integrated

|                                                          | description                                                                                                                                                                                                                                                                         |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **minimal examples** |                                                                                                                                                                                                                                                                                     |
| [global variable](dash_apps/01_minimal_global.py) | *bad practice*: minimal example in which a global `FigureResampler` variable is used                                                                                                                                                                                                |
| [server side caching](dash_apps/02_minimal_cache.py) | *good practice*: minimal example in which we perform server side caching of the `FigureResampler` variable                                                                                                                                                                          |
| [runtime graph construction](dash_apps/03_minimal_cache_dynamic.py) | minimal example where graphs are constructed based on user interactions at runtime. [Pattern matching callbacks](https://dash.plotly.com/pattern-matching-callbacks) are used construct these plotly-resampler graphs dynamically. Again, server side caching is performed.         |
| [xaxis overview (rangeslider)](dash_apps/04_minimal_cache_overview.py) | minimal example where a linked xaxis overview is shown below the `FigureResampler` figure. This xaxis rangeslider utilizes [clientside callbacks](https://dash.plotly.com/clientside-callbacks) to realize this behavior. |
| [xaxis overview (subplots)](dash_apps/05_cache_overview_subplots.py) | example where a linked xaxis overview is shown below the `FigureResampler` figure (with subplots). |
| [overview range selector button](dash_apps/06_cache_overview_range_buttons.py) | example where (i) a linked xaxis overview is shown below the `FigureResampler` figure, and (ii) a rangeselector along with a reset axis button is utilized to zoom in on specific window sizes. |
| **advanced apps** |                                                                                                                                                                                                                                                                                     |
| [dynamic sine generator](dash_apps/11_sine_generator.py) | exponential sine generator which uses [pattern matching callbacks](https://dash.plotly.com/pattern-matching-callbacks) to remove and construct plotly-resampler graphs dynamically                                                                                                  |
| [file visualization](dash_apps/12_file_selector.py) | load and visualize multiple `.parquet` files with plotly-resampler                                                                                                                                                                                                                  |
| [dynamic static graph](dash_apps/13_coarse_fine.py) | Visualization dashboard in which a dynamic (i.e., plotly-resampler graph) and a coarse, static graph (i.e., go.Figure) are shown (made for [this issue](https://github.com/predict-idlab/plotly-resampler/issues/56)). Graph interaction events on the coarse graph update the dynamic graph. |

## 3. Other apps

The [other_apps](other_apps/) folder contains examples of `plotly-resampler` being *integrated* in other apps / frameworks

| app-name | description |
| --- | --- |
| [streamlit integration](other_apps/streamlit_app.py) | visualize a large noisy sine in a [streamlit](https://streamlit.io/) app |


================================================
FILE: examples/datashader.ipynb
================================================
# Jupyter notebook converted to Python script.

"""
This notebook is a derivation of the [datashader time series](https://datashader.org/user_guide/Timeseries.html) notebook and serves as a mean to compare the datashader vs. plotly-resampler functionality.
"""

%load_ext autoreload
%autoreload 2

# !pip install jupyter_bokeh datashader panel holoviews bokeh

import datetime
import pandas as pd
import numpy as np
import xarray as xr
import datashader as ds
import datashader.transfer_functions as tf
from collections import OrderedDict
import panel as pn
import holoviews as hv
from holoviews.operation.datashader import datashade

from plotly_resampler import FigureResampler, EfficientLTTB
import plotly.graph_objects as go

hv.extension("bokeh")
pn.extension(comms='ipywidgets')

"""
### Generate fake data
"""

"""
This data has 10 signal modalties, which are highly correlated and one modality (`a`) has some outliers.
"""

# Constants
np.random.seed(2)
n = 1_000_000                                # Number of points
cols = list('abcdefg')                       # Column names of samples
start = datetime.datetime(2010, 10, 1, 0)    # Start time

# Generate a fake signal
signal = np.random.normal(0, 0.3, size=n).cumsum() + 50

# Generate many noisy samples from the signal
noise = lambda var, bias, n: np.random.normal(bias, var, n)
data = {c: signal + noise(1, 10*(np.random.random() - 0.5), n) for c in cols}

# Add some "rogue lines" that differ from the rest 
cols += ['x'] ; data['x'] = signal + np.random.normal(0, 0.02, size=n).cumsum() # Gradually diverges
cols += ['y'] ; data['y'] = signal + noise(1, 20*(np.random.random() - 0.5), n) # Much noisier
cols += ['z'] ; data['z'] = signal # No noise at all

# Pick a few samples from the first line and really blow them out
locs = np.random.choice(n, 10)
data['a'][locs] *= 2

# Create a dataframe
data['Time'] = [start + datetime.timedelta(minutes=1)*i for i in range(n)]

df = pd.DataFrame(data)
df.tail(3)

df['ITime'] = pd.to_datetime(df['Time']).astype('int64')

# Default plot ranges:
x_range = (df.iloc[0].ITime, df.iloc[-1].ITime)
y_range = (1.2*signal.min(), 1.2*signal.max())

print("x_range: {0} y_range: {1}".format(x_range,y_range))

"""
## 1. Plotting all the datapoints
"""

%%time
cvs = ds.Canvas(x_range=x_range, y_range=y_range, plot_height=300, plot_width=900)
aggs= OrderedDict((c, cvs.line(df, 'ITime', c)) for c in cols)

"""
### A single, noisy trace
"""

%%time
# Visualize a single column
img = tf.shade(aggs['a'])
img

"""
The result looks similar to what you might find in any plotting program, but it uses all 100,000 datapoints, and would work similarly for 1, 10, or 100 million points (determined by the n attribute above).
"""

"""
Why is using all the datapoints important? To see, let’s downsample the data by a factor of 10, plotting 10,000 datapoints for the same curve:
"""

mask = (df.index % 10) == 0
tf.shade(cvs.line(df[mask][['a','ITime']], 'ITime', 'a'))

%%time
fr = FigureResampler(default_n_shown_samples=2000)
for c in ['a']:
    fr.add_trace(go.Scattergl(name=c, line_width=1), hf_x=df.Time, hf_y=df[c])
fr.update_layout(template='plotly_white')
fr.show_dash(mode='inline', port=8049)

"""
### All the traces
"""

renamed = [aggs[key].rename({key: 'value'}) for key in aggs]
merged = xr.concat(renamed, 'cols')

total = tf.shade(merged.sum(dim='cols').astype('uint32'), how='linear')
total

"""
With study, the overall structure of this dataset should be clear, according to what we know we put in when we created them:

1. Individual rogue datapoints from curve ‘a’ are clearly visible (the seven sharp spikes)
2. The trend is clearly visible (for the viridis colormap, the darkest greens show the areas of highest overlap)
3. Line ‘x’ that gradually diverges from the trend is clearly visible (as the light blue (low-count) areas that increase below the right half of the plot).

(Note that if you change the random seed or the number of datapoints, the specific values and locations will differ from those mentioned in the text.)

**None of these observations would have been possible with downsampled, overplotted curves as would be typical of other plotting approaches.**
"""

%%time
fr = FigureResampler(default_n_shown_samples=2_000)
for c in cols:
    fr.add_trace(
        go.Scattergl(name=c, marker_color='darkblue', opacity=.15, line_width=1),
        hf_x=df.Time, hf_y=df[c]
    )
fr.update_layout(template='plotly_white')
fr.show_dash(mode='inline', port=8048)

"""
---
"""

"""
## **Intermezzo** Incorporating LTTB into holoviews
"""

s = df['a']
s.index = df['ITime']
s.index.name = 'timestamp'

s.reset_index()

s = df['x']
s.index = df['ITime']

"""
TODO alter this into a dynamic map of an overlay of traces.
"""

%%time
def resample_lttb(x_range) -> hv.Curve:
    if x_range is None or (np.isnan(x_range[0]) or np.isnan(x_range[1])):
        s_ = s
    else:
        s_ = s.loc[int(x_range[0]) : int(x_range[1])]

    s_ = EfficientLTTB().aggregate(s_, n_out=2000)
    s_.index.name = "timestamp"
    return hv.Curve(s_.reset_index(), "timestamp")


layout = hv.Overlay(
    [hv.DynamicMap(resample_lttb, streams=[hv.streams.RangeX()]) for _ in range(1)]
).collate()
layout.opts(hv.opts.Curve(axiswise=True, width=800, height=500, tools=["xwheel_zoom"]))

"""
---
"""

"""
## Datashader vs plotly-resampler
"""

"""
### Datashader vs plotly-resampler: `noisy-sine`
"""

n = 1_000_000
x = np.arange(n)
noisy_sine = (np.sin(x / 3_000) + (np.random.randn(n) / 10)) * x / 5_000
df_ = pd.DataFrame({"ns": noisy_sine, "ns_abs": np.abs(noisy_sine)})

opts = hv.opts.RGB(width=800, height=400)
ndoverlay = hv.NdOverlay({c:hv.Curve((df_.index, df_[c])) for c in df_.columns})
datashade(ndoverlay, cnorm='linear', aggregator=ds.count(), line_width=3).opts(opts)

fr = FigureResampler(default_n_shown_samples=3000)
for c in set(df_.columns).difference(["Time"]):
    fr.add_trace(
        go.Scattergl(
            name=c,
            marker_color="blue",
            mode="lines+markers",
            opacity=0.1,
            marker_size=3,
        ),
        hf_y=df_[c],
    )
fr.show_dash(mode="inline", port=8091)

"""
### Datashader vs plotly-resampler: `multiple-trends`
"""

signals = [np.random.normal(0, 0.3, size=n).cumsum() + 50,
           np.random.normal(0, 0.3, size=n).cumsum() + 50,
           np.random.normal(0, 0.3, size=n).cumsum() + 50]
data = {c: signals[i%3] + noise(1+i, 5*(np.random.random() - 0.5), n)  for (i,c) in enumerate(cols)}
y_range = (1.2*min([s.min() for s in signals]), 1.2*max([s.max() for s in signals]))    

data['Time'] = df['Time']
dfm = pd.DataFrame(data)
dfm.shape

opts = hv.opts.RGB(width=600, height=300)
ndoverlay = hv.NdOverlay({c:hv.Curve((dfm.index, dfm[c]), vdims=['Time']) for c in cols})
datashade(ndoverlay, cnorm='linear', aggregator=ds.count(), line_width=3).opts(opts)

fr = FigureResampler(default_n_shown_samples=2000)
for c in set(dfm.columns).difference(['Time']):
    fr.add_trace(go.Scattergl(name=c, marker_color='blue', opacity=0.1), hf_x=dfm.Time, hf_y=dfm[c])
fr.update_layout(template='plotly_white')
fr.show_dash(mode='inline', port=8091)



================================================
FILE: examples/figurewidget_example.ipynb
================================================
# Jupyter notebook converted to Python script.

%load_ext autoreload
%autoreload 2

import plotly.graph_objs as go
import numpy as np
from plotly_resampler.figure_resampler import FigureWidgetResampler
from plotly.subplots import make_subplots

n = 1_000_000  # the nbr of data points
x = np.arange(n)
y = np.sin(x / 200) + np.random.random(len(x)) / 10

"""
**note**: 
* to use `FigureWidgetResampler`, you need to have `ipywidgets` installed
* `FigureWidgetResampler` does not start a web applcication, making this wrapper suitable jupyter based-environemnts, where multiple `FigureWidgets` can be created
"""

"""
### Basic `FigureWidgetResampler` example
"""

"""
To utilize FigureWidgetResampler, you just need to:
* wrap your figure with a `FigureWidgetResampler`
* output this wrapped instance in a cell
"""

# Wrap a figure with FigureWidgetResampler
fw_fig = FigureWidgetResampler(make_subplots(rows=2, shared_xaxes=False))

fw_fig.add_trace(go.Scattergl(), hf_x=x, hf_y=y * 1.000003**x, row=1, col=1)
fw_fig.add_trace(go.Scattergl(), hf_x=x, hf_y=(y + 3) * 0.999997**x, row=2, col=1)
fw_fig.update_layout(height=500, showlegend=True)

# Output this wrapped instance in a cell
fw_fig
# Output:
#   FigureWidgetResampler({

#       'data': [{'name': '<b style="color:sandybrown">[R]</b> trace 0 <i style="color:#fc…

"""
Note how the cells below are able to add data to the `FigureWidget`
"""

fw_fig.add_trace(go.Scattergl(), hf_x=x, hf_y=y * 1.0000028**x, row=1, col=1)
fw_fig.add_trace(go.Scattergl(), hf_x=x, hf_y=y * 1.000002**x, row=1, col=1)

fw_fig.add_trace(go.Scattergl(), hf_x=x, hf_y=(y + 3) * 0.999999**x, row=2, col=1)

"""
### time-series **annotation** using the on-click callback
"""

from ipywidgets import Dropdown
from IPython.display import display

# Proxy for a label class
label_dict = {
    "peak": {
        "type": "marker",
        "trace_index": 1,
        "plt_kwargs": {
        "mode": "markers", "marker_symbol": "star", "marker_size": 12, "marker_color": "red"
        }
    },
    "through": {
        "type": "marker",
        "trace_index": 2,
        "plt_kwargs": {
        "mode": "markers", "marker_symbol": "cross", "marker_size": 12, "line_color": "orange"
        }
    },
    "rise": {
        "type": "x-range",
        "plt_kwargs": {
            "line_width": 0, "fillcolor": "green", "opacity": 0.3
        }
    },
    "fall": {
        "type": "x-range",
        "plt_kwargs": {
            "line_width": 0, "fillcolor": "purple", "opacity": 0.3
        }
    }
}

# Create a label selector
label_selector = Dropdown()
label_selector.options = list(label_dict.keys())

# Construct the figure
fw_fig = FigureWidgetResampler()
fw_fig.add_trace(go.Scattergl(name="noisy sine", opacity=0.8), hf_x=x, hf_y=y)
for k, v in label_dict.items():
    if v.get("type", "").lower() == 'marker':
        fw_fig.add_trace(go.Scattergl(name=k, **v.get("plt_kwargs", {})))


# Update logic
prev_x = []
point_list = []

def update_point(trace, points, selector):
    global prev_x, point_list
    config = label_dict[label_selector.value]

    if config.get("type", "") == 'x-range':
        prev_x.append(points.xs[0])
        if len(prev_x) == 2:
            fw_fig.add_vrect(prev_x[0], prev_x[1], **config.get("plt_kwargs", {}))
            prev_x = []

    with fw_fig.batch_update():
        if config.get("type", "") == 'marker':
            trace_index = config.get("trace_index")
            fw_fig.data[trace_index].x = list(fw_fig.data[trace_index].x) + points.xs
            fw_fig.data[trace_index].y = list(fw_fig.data[trace_index].y) + points.ys

fw_fig.data[0].on_click(update_point)

display(label_selector)
fw_fig
# Output:
#   Dropdown(options=('peak', 'through', 'rise', 'fall'), value='peak')
#   FigureWidgetResampler({

#       'data': [{'name': '<b style="color:sandybrown">[R]</b> noisy sine <i style="color:…

"""
### Adjusting the figure data using the `hf_data` property
"""

fw_fig = FigureWidgetResampler(make_subplots(rows=2, shared_xaxes=False), verbose=True)
fw_fig.update_layout(template='plotly_dark', height=600)
fw_fig.add_trace(go.Scattergl(), hf_x=x, hf_y=y, row=1, col=1)
fw_fig.add_trace(go.Scattergl(), hf_x=x, hf_y=y, row=2, col=1)
fw_fig
# Output:
#   	[i] DOWNSAMPLE None	1000000->1000

#   	[i] DOWNSAMPLE None	1000000->1000

#   FigureWidgetResampler({

#       'data': [{'name': '<b style="color:sandybrown">[R]</b> trace 0 <i style="color:#fc…

# After you've ran this cell, reset the axes of the above figure 
# or zoom in-out on the x-range
fw_fig.hf_data[0]['y'] = - (y  + 3) * x / 1000
fw_fig.hf_data[1]['y'] =  (y  + 3) * x / 1000

"""
### Multiple shared traces
"""

fig = FigureWidgetResampler()

# 10 sensors, 500_000 datapoints each on a singe plot
for i in range(10):
    fig.add_trace(go.Scattergl(name=str(i)), hf_x=x, hf_y=y + i)

fig.update_layout(
    height=600, title=f"10 traces -> {10*500_000:,} datapoints", title_x=0.5
)
fig
# Output:
#   FigureWidgetResampler({

#       'data': [{'name': '<b style="color:sandybrown">[R]</b> 0 <i style="color:#fc9944">…



================================================
FILE: examples/helper.py
================================================
from typing import Union

import pandas as pd


def groupby_consecutive(
    df: Union[pd.Series, pd.DataFrame], col_name: str = None
) -> pd.DataFrame:
    """Merges consecutive `column_name` values in a single dataframe.

    This is especially useful if you want to represent sparse data in a more
    compact format.

    Parameters
    ----------
    df : Union[pd.Series, pd.DataFrame]
        Must be time-indexed!
    col_name : str, optional
        If a dataFrame is passed, you will need to specify the `col_name` on which
        the consecutive-grouping will need to take plase.

    Returns
    -------
    pd.DataFrame
        A new `DataFrame` view, with columns:
        [`start`, `end`, `n_consecutive`, `col_name`], representing the
        start- and endtime of the consecutive range, the number of consecutive samples,
        and the col_name's consecutive values.
    """
    if type(df) == pd.Series:
        col_name = df.name
        df = df.to_frame()

    assert col_name in df.columns

    df_cum = (
        (df[col_name].diff(1) != 0)
        .astype("int")
        .cumsum()
        .rename("value_grp")
        .to_frame()
    )
    df_cum["sequence_idx"] = df.index
    df_cum[col_name] = df[col_name]

    df_grouped = pd.DataFrame(
        {
            "start": df_cum.groupby("value_grp")["sequence_idx"].first(),
            "end": df_cum.groupby("value_grp")["sequence_idx"].last(),
            "n_consecutive": df_cum.groupby("value_grp").size(),
            col_name: df_cum.groupby("value_grp")[col_name].first(),
        }
    ).reset_index(drop=True)
    df_grouped["next_start"] = df_grouped.start.shift(-1).fillna(df_grouped["end"])
    return df_grouped



================================================
FILE: examples/requirements.txt
================================================
pyfunctional>=1.4.3
dash-bootstrap-components>=1.2.0
dash-extensions==1.0.20  # fixated on this version as more recent versions do not work
ipywidgets>=7.7.0
memory-profiler>=0.60.0
line-profiler>=3.5.1
pyarrow>=17.0.0
kaleido>=0.2.1
flask-cors>=3.0.10


================================================
FILE: examples/dash_apps/01_minimal_global.py
================================================
"""Minimal dash app example.

Click on a button, and see a plotly-resampler graph of two noisy sinusoids.
No dynamic graph construction / pattern matching callbacks are needed.

This example uses a global FigureResampler object, which is considered a bad practice.
source: https://dash.plotly.com/sharing-data-between-callbacks:

    Dash is designed to work in multi-user environments where multiple people view the
    application at the same time and have independent sessions.
    If your app uses and modifies a global variable, then one user's session could set
    the variable to some value which would affect the next user's session.

"""

import numpy as np
import plotly.graph_objects as go
from dash import Dash, Input, Output, callback_context, dcc, html, no_update

from plotly_resampler import FigureResampler

# Data that will be used for the plotly-resampler figures
x = np.arange(2_000_000)
noisy_sin = (3 + np.sin(x / 200) + np.random.randn(len(x)) / 10) * x / 1_000


# --------------------------------------Globals ---------------------------------------
app = Dash(__name__)
fig: FigureResampler = FigureResampler()
# NOTE: in this example, this reference to a FigureResampler is essential to preserve
# throughout the whole dash app! If your dash app wants to create a new go.Figure(),
# you should not construct a new FigureResampler object, but replace the figure of this
# FigureResampler object by using the FigureResampler.replace() method.

app.layout = html.Div(
    [
        html.H1("plotly-resampler global variable", style={"textAlign": "center"}),
        html.Button("plot chart", id="plot-button", n_clicks=0),
        html.Hr(),
        # The graph object  - which we will empower with plotly-resampler
        dcc.Graph(id="graph-id"),
    ]
)


# ------------------------------------ DASH logic -------------------------------------
# The callback used to construct and store the graph's data on the serverside
@app.callback(
    Output("graph-id", "figure"),
    Input("plot-button", "n_clicks"),
    prevent_initial_call=True,
)
def plot_graph(n_clicks):
    ctx = callback_context
    if len(ctx.triggered) and "plot-button" in ctx.triggered[0]["prop_id"]:
        # Note how the replace method is used here on the global figure object
        global fig
        if len(fig.data):
            # Replace the figure with an empty one to clear the graph
            fig.replace(go.Figure())
        fig.add_trace(go.Scattergl(name="log"), hf_x=x, hf_y=noisy_sin * 0.9999995**x)
        fig.add_trace(go.Scattergl(name="exp"), hf_x=x, hf_y=noisy_sin * 1.000002**x)
        return fig
    else:
        return no_update


# The plotly-resampler callback to update the graph after a relayout event (= zoom/pan)
fig.register_update_graph_callback(app=app, graph_id="graph-id")

# --------------------------------- Running the app ---------------------------------
if __name__ == "__main__":
    app.run_server(debug=True, port=9023)



================================================
FILE: examples/dash_apps/02_minimal_cache.py
================================================
"""Minimal dash app example.

Click on a button, and see a plotly-resampler graph of two noisy sinusoids.
No dynamic graph construction / pattern matching callbacks are needed.

This example uses the dash-extensions its ServerSide functionality to cache
the FigureResampler per user/session on the server side. This way, no global figure
variable is used and shows the best practice of using plotly-resampler within dash-apps.

"""

import numpy as np
import plotly.graph_objects as go
from dash import Input, Output, State, callback_context, dcc, html, no_update
from dash_extensions.enrich import DashProxy, Serverside, ServersideOutputTransform

from plotly_resampler import FigureResampler
from plotly_resampler.aggregation import MinMaxLTTB

# Data that will be used for the plotly-resampler figures
x = np.arange(2_000_000)
noisy_sin = (3 + np.sin(x / 200) + np.random.randn(len(x)) / 10) * x / 1_000

# --------------------------------------Globals ---------------------------------------
app = DashProxy(__name__, transforms=[ServersideOutputTransform()])

app.layout = html.Div(
    [
        html.H1("plotly-resampler + dash-extensions", style={"textAlign": "center"}),
        html.Button("plot chart", id="plot-button", n_clicks=0),
        html.Hr(),
        # The graph object - which we will empower with plotly-resampler
        dcc.Graph(id="graph-id"),
        # Note: we also add a dcc.Store component, which will be used to link the
        #       server side cached FigureResampler object
        dcc.Loading(dcc.Store(id="store")),
    ]
)


# ------------------------------------ DASH logic -------------------------------------
# The callback used to construct and store the FigureResampler on the serverside
@app.callback(
    [Output("graph-id", "figure"), Output("store", "data")],
    Input("plot-button", "n_clicks"),
    prevent_initial_call=True,
)
def plot_graph(n_clicks):
    ctx = callback_context
    if len(ctx.triggered) and "plot-button" in ctx.triggered[0]["prop_id"]:
        fig: FigureResampler = FigureResampler(
            go.Figure(), default_downsampler=MinMaxLTTB(parallel=True)
        )

        # Figure construction logic
        fig.add_trace(go.Scattergl(name="log"), hf_x=x, hf_y=noisy_sin * 0.9999995**x)
        fig.add_trace(go.Scattergl(name="exp"), hf_x=x, hf_y=noisy_sin * 1.000002**x)

        return fig, Serverside(fig)
    else:
        return no_update


# The plotly-resampler callback to update the graph after a relayout event (= zoom/pan)
# As we use the figure again as output, we need to set: allow_duplicate=True
@app.callback(
    Output("graph-id", "figure", allow_duplicate=True),
    Input("graph-id", "relayoutData"),
    State("store", "data"),  # The server side cached FigureResampler per session
    prevent_initial_call=True,
    memoize=True,
)
def update_fig(relayoutdata: dict, fig: FigureResampler):
    if fig is None:
        return no_update
    return fig.construct_update_data_patch(relayoutdata)


# --------------------------------- Running the app ---------------------------------
if __name__ == "__main__":
    app.run_server(debug=True, port=9023)



================================================
FILE: examples/dash_apps/03_minimal_cache_dynamic.py
================================================
"""Minimal dynamic dash app example.

Click on a button, and draw a new plotly-resampler graph of two noisy sinusoids.
This example uses pattern-matching callbacks to update dynamically constructed graphs.
The plotly-resampler graphs themselves are cached on the server side.

The main difference between this example and 02_minimal_cache.py is that here, we want
to cache using a dcc.Store that is not yet available on the client side. As a result we
split up our logic into two callbacks: (1) the callback used to construct the necessary
components and send them to the client-side, and (2) the callback used to construct the
actual plotly-resampler graph and cache it on the server side. These two callbacks are
chained together using the dcc.Interval component.

"""

from typing import List
from uuid import uuid4

import numpy as np
import plotly.graph_objects as go
from dash import MATCH, Input, Output, State, dcc, html, no_update
from dash_extensions.enrich import (
    DashProxy,
    Serverside,
    ServersideOutputTransform,
    Trigger,
    TriggerTransform,
)

from plotly_resampler import FigureResampler
from plotly_resampler.aggregation import MinMaxLTTB

# Data that will be used for the plotly-resampler figures
x = np.arange(2_000_000)
noisy_sin = (3 + np.sin(x / 200) + np.random.randn(len(x)) / 10) * x / 1_000

# --------------------------------------Globals ---------------------------------------
app = DashProxy(__name__, transforms=[ServersideOutputTransform(), TriggerTransform()])

app.layout = html.Div(
    [
        html.Div(children=[html.Button("Add Chart", id="add-chart", n_clicks=0)]),
        html.Div(id="container", children=[]),
    ]
)


# ------------------------------------ DASH logic -------------------------------------
# This method adds the needed components to the front-end, but does not yet contain the
# FigureResampler graph construction logic.
@app.callback(
    Output("container", "children"),
    Input("add-chart", "n_clicks"),
    State("container", "children"),
    prevent_initial_call=True,
)
def add_graph_div(n_clicks: int, div_children: List[html.Div]):
    uid = str(uuid4())
    new_child = html.Div(
        children=[
            dcc.Graph(id={"type": "dynamic-graph", "index": uid}, figure=go.Figure()),
            # Note: we also add a dcc.Store component, which will be used to link the
            #       server side cached FigureResampler object
            dcc.Loading(dcc.Store(id={"type": "store", "index": uid})),
            # This dcc.Interval components makes sure that the `construct_display_graph`
            # callback is fired once after these components are added to the session
            # its front-end
            dcc.Interval(
                id={"type": "interval", "index": uid}, max_intervals=1, interval=1
            ),
        ],
    )
    div_children.append(new_child)
    return div_children


# This method constructs the FigureResampler graph and caches it on the server side
@app.callback(
    Output({"type": "dynamic-graph", "index": MATCH}, "figure"),
    Output({"type": "store", "index": MATCH}, "data"),
    State("add-chart", "n_clicks"),
    Trigger({"type": "interval", "index": MATCH}, "n_intervals"),
    prevent_initial_call=True,
)
def construct_display_graph(n_clicks) -> FigureResampler:
    fig = FigureResampler(
        go.Figure(),
        default_n_shown_samples=2_000,
        default_downsampler=MinMaxLTTB(parallel=True),
    )

    # Figure construction logic based on a state variable, in our case n_clicks
    sigma = n_clicks * 1e-6
    fig.add_trace(dict(name="log"), hf_x=x, hf_y=noisy_sin * (1 - sigma) ** x)
    fig.add_trace(dict(name="exp"), hf_x=x, hf_y=noisy_sin * (1 + sigma) ** x)
    fig.update_layout(title=f"<b>graph - {n_clicks}</b>", title_x=0.5)

    return fig, Serverside(fig)


# The plotly-resampler callback to update the graph after a relayout event (= zoom/pan)
# As we use the figure again as output, we need to set: allow_duplicate=True
@app.callback(
    Output({"type": "dynamic-graph", "index": MATCH}, "figure", allow_duplicate=True),
    Input({"type": "dynamic-graph", "index": MATCH}, "relayoutData"),
    State({"type": "store", "index": MATCH}, "data"),
    prevent_initial_call=True,
    memoize=True,
)
def update_fig(relayoutdata: dict, fig: FigureResampler):
    if fig is not None:
        return fig.construct_update_data_patch(relayoutdata)
    return no_update


# --------------------------------- Running the app ---------------------------------
if __name__ == "__main__":
    app.run_server(debug=True, port=9023)



================================================
FILE: examples/dash_apps/04_minimal_cache_overview.py
================================================
"""Minimal dash app example.

Click on a button, and see a plotly-resampler graph of two sinusoids.
In addition, another graph is shown, which is an overview of the main graph.
This other graph is bidirectionally linked to the main graph; when you select a region
in the overview graph, the main graph will zoom in on that region and vice versa.

This example uses the dash-extensions its ServersideOutput functionality to cache
the FigureResampler per user/session on the server side. This way, no global figure
variable is used and shows the best practice of using plotly-resampler within dash-apps.

"""

import dash
import numpy as np
import plotly.graph_objects as go
from dash import Input, Output, State, callback_context, dcc, html, no_update
from dash_extensions.enrich import DashProxy, Serverside, ServersideOutputTransform

# The overview figure requires clientside callbacks, whose JavaScript code is located
# in the assets folder. We need to tell dash where to find this folder.
from plotly_resampler import ASSETS_FOLDER, FigureResampler

# -------------------------------- Data and constants ---------------------------------
# Data that will be used for the plotly-resampler figures
x = np.arange(2_000_000)
noisy_sin = (3 + np.sin(x / 200) + np.random.randn(len(x)) / 10) * x / 1_000

# The ids of the components used in the app (we put them here to avoid typos)
GRAPH_ID = "graph-id"
OVERVIEW_GRAPH_ID = "overview-graph"
STORE_ID = "store"


# --------------------------------------Globals ---------------------------------------
# NOTE: Remark how the assets folder is passed to the Dash(proxy) application and how
#       the lodash script is included as an external script.
app = DashProxy(
    __name__,
    transforms=[ServersideOutputTransform()],
    assets_folder=ASSETS_FOLDER,
    external_scripts=["https://cdn.jsdelivr.net/npm/lodash/lodash.min.js"],
)

app.layout = html.Div(
    [
        html.H1("plotly-resampler + dash-extensions", style={"textAlign": "center"}),
        html.Button("plot chart", id="plot-button", n_clicks=0),
        html.Hr(),
        # The graph, overview graph, and serverside store for the FigureResampler graph
        dcc.Graph(id=GRAPH_ID),
        dcc.Graph(id=OVERVIEW_GRAPH_ID),
        dcc.Loading(dcc.Store(id=STORE_ID)),
    ]
)


# ------------------------------------ DASH logic -------------------------------------
# --- construct and store the FigureResampler on the serverside ---
@app.callback(
    [
        Output(GRAPH_ID, "figure"),
        Output(OVERVIEW_GRAPH_ID, "figure"),
        Output(STORE_ID, "data"),
    ],
    Input("plot-button", "n_clicks"),
    prevent_initial_call=True,
)
def plot_graph(_):
    global app
    ctx = callback_context
    if len(ctx.triggered) and "plot-button" in ctx.triggered[0]["prop_id"]:
        fig: FigureResampler = FigureResampler(create_overview=True)

        # Figure construction logic
        fig.add_trace(go.Scattergl(name="log"), hf_x=x, hf_y=noisy_sin * 0.9999995**x)
        fig.add_trace(go.Scattergl(name="exp"), hf_x=x, hf_y=noisy_sin * 1.000002**x)

        fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02))
        fig.update_layout(margin=dict(b=10), template="plotly_white")

        coarse_fig = fig._create_overview_figure()
        return fig, coarse_fig, Serverside(fig)
    else:
        return no_update


# --- Clientside callbacks used to bidirectionally link the overview and main graph ---
app.clientside_callback(
    dash.ClientsideFunction(namespace="clientside", function_name="main_to_coarse"),
    dash.Output(OVERVIEW_GRAPH_ID, "id", allow_duplicate=True),
    dash.Input(GRAPH_ID, "relayoutData"),
    [dash.State(OVERVIEW_GRAPH_ID, "id"), dash.State(GRAPH_ID, "id")],
    prevent_initial_call=True,
)

app.clientside_callback(
    dash.ClientsideFunction(namespace="clientside", function_name="coarse_to_main"),
    dash.Output(GRAPH_ID, "id", allow_duplicate=True),
    dash.Input(OVERVIEW_GRAPH_ID, "selectedData"),
    [dash.State(GRAPH_ID, "id"), dash.State(OVERVIEW_GRAPH_ID, "id")],
    prevent_initial_call=True,
)


# ------ FigureResampler update callback ------


# The plotly-resampler callback to update the graph after a relayout event (= zoom/pan)
# As we use the figure again as output, we need to set: allow_duplicate=True
@app.callback(
    Output(GRAPH_ID, "figure", allow_duplicate=True),
    Input(GRAPH_ID, "relayoutData"),
    State(STORE_ID, "data"),  # The server side cached FigureResampler per session
    prevent_initial_call=True,
)
def update_fig(relayoutdata: dict, fig: FigureResampler):
    if fig is None:
        return no_update
    return fig.construct_update_data_patch(relayoutdata)


# --------------------------------- Running the app ---------------------------------
if __name__ == "__main__":
    app.run_server(debug=True, port=9023, use_reloader=False)



================================================
FILE: examples/dash_apps/05_cache_overview_subplots.py
================================================
"""Minimal dash app example.

Click on a button, and see a plotly-resampler graph of an exponential and log curve
(and combinations thereof) spread over 4 subplots.
In addition, another graph is shown below, which is an overview of subplot columns from
the main graph. This other graph is bidirectionally linked to the main graph; when you
select a region in the overview graph, the main graph will zoom in on that region and
vice versa.

This example uses the dash-extensions its ServersideOutput functionality to cache
the FigureResampler per user/session on the server side. This way, no global figure
variable is used and shows the best practice of using plotly-resampler within dash-apps.

"""

import dash
import numpy as np
import plotly.graph_objects as go
from dash import Input, Output, State, callback_context, dcc, html, no_update
from dash_extensions.enrich import DashProxy, Serverside, ServersideOutputTransform
from plotly.subplots import make_subplots

# The overview figure requires clientside callbacks, whose JavaScript code is located
# in the assets folder. We need to tell dash where to find this folder.
from plotly_resampler import ASSETS_FOLDER, FigureResampler
from plotly_resampler.aggregation import MinMaxLTTB

# -------------------------------- Data and constants ---------------------------------
# Data that will be used for the plotly-resampler figures
x = np.arange(2_000_000)
noisy_sin = (3 + np.sin(x / 200) + np.random.randn(len(x)) / 10) * x / 1_000

# The ids of the components used in the app (we put them here to avoid typos)
GRAPH_ID = "graph-id"
OVERVIEW_GRAPH_ID = "overview-graph"
STORE_ID = "store"


# --------------------------------------Globals ---------------------------------------
# NOTE: Remark how the assets folder is passed to the Dash(proxy) application and how
#       the lodash script is included as an external script.
app = DashProxy(
    __name__,
    transforms=[ServersideOutputTransform()],
    assets_folder=ASSETS_FOLDER,
    external_scripts=["https://cdn.jsdelivr.net/npm/lodash/lodash.min.js"],
)

app.layout = html.Div(
    [
        html.H1("plotly-resampler + dash-extensions", style={"textAlign": "center"}),
        html.Button("plot chart", id="plot-button", n_clicks=0),
        html.Hr(),
        # The graph, overview graph, and serverside store for the FigureResampler graph
        dcc.Graph(id=GRAPH_ID),
        dcc.Graph(id=OVERVIEW_GRAPH_ID),
        dcc.Loading(dcc.Store(id=STORE_ID)),
    ]
)


# ------------------------------------ DASH logic -------------------------------------
# --- construct and store the FigureResampler on the serverside ---
@app.callback(
    [
        Output(GRAPH_ID, "figure"),
        Output(OVERVIEW_GRAPH_ID, "figure"),
        Output(STORE_ID, "data"),
    ],
    Input("plot-button", "n_clicks"),
    prevent_initial_call=True,
)
def plot_graph(_):
    global app
    ctx = callback_context
    if len(ctx.triggered) and "plot-button" in ctx.triggered[0]["prop_id"]:
        # NOTE: remark how the `overview_row_idxs` argument specifies the row indices
        # (start at 0) of the subplots that will be used to construct the overview
        # graph. In this list the position of the values indicate the column index of
        # the subplot. In this case, the overview graph will show for the first column
        # the second subplot row (1), and for the second column the first subplot row
        # (0).
        fig: FigureResampler = FigureResampler(
            make_subplots(
                rows=2, cols=2, shared_xaxes="columns", horizontal_spacing=0.03
            ),
            create_overview=True,
            overview_row_idxs=[1, 0],
            default_downsampler=MinMaxLTTB(parallel=True),
        )

        # Figure construction logic
        # fmt: off
        log = noisy_sin * 0.9999995**x
        exp = noisy_sin * 1.000002**x
        fig.add_trace(go.Scattergl(name="log", legend='legend1'), hf_x=x, hf_y=log)
        fig.add_trace(go.Scattergl(name="exp", legend='legend1'), hf_x=x, hf_y=exp)

        fig.add_trace(go.Scattergl(name="-log", legend='legend2'), hf_x=x, hf_y=-exp, row=1, col=2)

        fig.add_trace(go.Scattergl(name="log", legend='legend3'), hf_x=x, hf_y=-log, row=2, col=1)
        fig.add_trace(go.Scattergl(name="3-exp", legend='legend3'), hf_x=x, hf_y=3 - exp, row=2, col=1)

        fig.add_trace(go.Scattergl(name="log", legend='legend4'), hf_x=x, hf_y=log**2, row=2, col=2)

        # fmt: on
        fig.update_layout(
            legend1=dict(orientation="h", yanchor="bottom", y=1.02),
            legend2=dict(orientation="h", yanchor="bottom", y=1.02, x=0.52),
            legend3=dict(orientation="h", y=0.51, x=0),
            legend4=dict(orientation="h", y=0.51, x=0.52),
        )
        fig.update_layout(margin=dict(b=10), template="plotly_white")

        coarse_fig = fig._create_overview_figure()
        return fig, coarse_fig, Serverside(fig)
    else:
        return no_update


# --- Clientside callbacks used to bidirectionally link the overview and main graph ---
app.clientside_callback(
    dash.ClientsideFunction(namespace="clientside", function_name="main_to_coarse"),
    dash.Output(
        OVERVIEW_GRAPH_ID, "id", allow_duplicate=True
    ),  # TODO -> look for clean output
    dash.Input(GRAPH_ID, "relayoutData"),
    [dash.State(OVERVIEW_GRAPH_ID, "id"), dash.State(GRAPH_ID, "id")],
    prevent_initial_call=True,
)

app.clientside_callback(
    dash.ClientsideFunction(namespace="clientside", function_name="coarse_to_main"),
    dash.Output(GRAPH_ID, "id", allow_duplicate=True),
    dash.Input(OVERVIEW_GRAPH_ID, "selectedData"),
    [dash.State(GRAPH_ID, "id"), dash.State(OVERVIEW_GRAPH_ID, "id")],
    prevent_initial_call=True,
)


# --- FigureResampler update callback ---


# The plotly-resampler callback to update the graph after a relayout event (= zoom/pan)
# As we use the figure again as output, we need to set: allow_duplicate=True
@app.callback(
    Output(GRAPH_ID, "figure", allow_duplicate=True),
    Input(GRAPH_ID, "relayoutData"),
    State(STORE_ID, "data"),  # The server side cached FigureResampler per session
    prevent_initial_call=True,
)
def update_fig(relayoutdata, fig: FigureResampler):
    if fig is None:
        return no_update
    return fig.construct_update_data_patch(relayoutdata)


# --------------------------------- Running the app ---------------------------------
if __name__ == "__main__":
    app.run_server(debug=True, port=9023, use_reloader=False)



================================================
FILE: examples/dash_apps/06_cache_overview_range_buttons.py
================================================
"""Minimal dash app example.

Click on a button, and see a plotly-resampler graph of an exponential and log curve is 
shown. In addition, another graph is shown below, which is an overview of the main 
graph. This other graph is bidirectionally linked to the main graph; when you
select a region in the overview graph, the main graph will zoom in on that region and
vice versa.

On the left top of the main graph, you can see a range selector. This range selector
allows to zoom in with a fixed time range.

Lastly, there is a button present to reset the axes of the main graph. This button
replaces the default reset axis button as the default button removes the spikes.
(specifically, the `xaxis.showspikes` and `yaxis.showspikes` are set to False; This is 
most likely a bug in plotly-resampler, but I have not yet found out why).

This example uses the dash-extensions its ServersideOutput functionality to cache
the FigureResampler per user/session on the server side. This way, no global figure
variable is used and shows the best practice of using plotly-resampler within dash-apps.

"""

import dash
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from dash import Input, Output, State, callback_context, dcc, html, no_update
from dash_extensions.enrich import DashProxy, Serverside, ServersideOutputTransform

# The overview figure requires clientside callbacks, whose JavaScript code is located
# in the assets folder. We need to tell dash where to find this folder.
from plotly_resampler import ASSETS_FOLDER, FigureResampler
from plotly_resampler.aggregation import MinMaxLTTB

# -------------------------------- Data and constants ---------------------------------
# Data that will be used for the plotly-resampler figures
x = np.arange(2_000_000)
x_time = pd.date_range("2020-01-01", periods=len(x), freq="1min")
noisy_sin = (3 + np.sin(x / 200) + np.random.randn(len(x)) / 10) * x / 1_000

# The ids of the components used in the app (we put them here to avoid typos later on)
GRAPH_ID = "graph-id"
OVERVIEW_GRAPH_ID = "overview-graph"
STORE_ID = "store"
PLOT_BTN_ID = "plot-button"

# --------------------------------------Globals ---------------------------------------
# NOTE: Remark how
#   (1) the assets folder is passed to the Dash(proxy) application
#   (2) the lodash script is included as an external script.
app = DashProxy(
    __name__,
    transforms=[ServersideOutputTransform()],
    assets_folder=ASSETS_FOLDER,
    external_scripts=["https://cdn.jsdelivr.net/npm/lodash/lodash.min.js"],
)

# Construct the app layout
app.layout = html.Div(
    [
        html.H1("plotly-resampler + dash-extensions", style={"textAlign": "center"}),
        html.Button("plot chart", id=PLOT_BTN_ID, n_clicks=0),
        html.Hr(),
        # The graph, overview graph, and serverside store for the FigureResampler graph
        dcc.Graph(
            id=GRAPH_ID,
            # NOTE: we remove the reset scale button as it removes the spikes and
            # we provide our own reset-axis button upon graph construction
            config={"modeBarButtonsToRemove": ["resetscale"]},
        ),
        dcc.Graph(id=OVERVIEW_GRAPH_ID, config={"displayModeBar": False}),
        dcc.Loading(dcc.Store(id=STORE_ID)),
    ]
)


# ------------------------------------ DASH logic -------------------------------------
# --- construct and store the FigureResampler on the serverside ---
@app.callback(
    [
        Output(GRAPH_ID, "figure"),
        Output(OVERVIEW_GRAPH_ID, "figure"),
        Output(STORE_ID, "data"),
    ],
    Input(PLOT_BTN_ID, "n_clicks"),
    prevent_initial_call=True,
)
def plot_graph(_):
    ctx = callback_context
    if not len(ctx.triggered) or PLOT_BTN_ID not in ctx.triggered[0]["prop_id"]:
        return no_update

    # 1. Create the figure and add data
    fig = FigureResampler(
        # fmt: off
        go.Figure(layout=dict(
            # dragmode="pan",
            hovermode="x unified",
            xaxis=dict(rangeselector=dict(buttons=list([
                dict(count=7, label="1 week", step="day", stepmode="backward"),
                dict(count=1, label="1 month", step="month", stepmode="backward"),
                dict(count=2, label="2 months", step="month", stepmode="backward"),
                dict(count=1, label="1 year", step="year", stepmode="backward"),
            ]))),
        )),
        # fmt: on
        default_downsampler=MinMaxLTTB(parallel=True),
        create_overview=True,
    )

    # Figure construction logic
    log = noisy_sin * 0.9999995**x
    exp = noisy_sin * 1.000002**x
    fig.add_trace(go.Scattergl(name="log"), hf_x=x_time, hf_y=log)
    fig.add_trace(go.Scattergl(name="exp"), hf_x=x_time, hf_y=exp)

    fig.update_layout(
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    fig.update_layout(
        margin=dict(b=10),
        template="plotly_white",
        height=650,  # , hovermode="x unified",
        # https://plotly.com/python/custom-buttons/
        updatemenus=[
            dict(
                type="buttons",
                x=0.45,
                xanchor="left",
                y=1.09,
                yanchor="top",
                buttons=[
                    dict(
                        label="reset axes",
                        method="relayout",
                        args=[
                            {
                                "xaxis.autorange": True,
                                "yaxis.autorange": True,
                                "xaxis.showspikes": True,
                                "yaxis.showspikes": False,
                            }
                        ],
                    ),
                ],
            )
        ],
    )
    # fig.update_traces(xaxis="x")
    # fig.update_xaxes(showspikes=True, spikemode="across", spikesnap="cursor")

    coarse_fig = fig._create_overview_figure()
    return fig, coarse_fig, Serverside(fig)


# --- Clientside callbacks used to bidirectionally link the overview and main graph ---
app.clientside_callback(
    dash.ClientsideFunction(namespace="clientside", function_name="main_to_coarse"),
    dash.Output(
        OVERVIEW_GRAPH_ID, "id", allow_duplicate=True
    ),  # TODO -> look for clean output
    dash.Input(GRAPH_ID, "relayoutData"),
    [dash.State(OVERVIEW_GRAPH_ID, "id"), dash.State(GRAPH_ID, "id")],
    prevent_initial_call=True,
)

app.clientside_callback(
    dash.ClientsideFunction(namespace="clientside", function_name="coarse_to_main"),
    dash.Output(GRAPH_ID, "id", allow_duplicate=True),
    dash.Input(OVERVIEW_GRAPH_ID, "selectedData"),
    [dash.State(GRAPH_ID, "id"), dash.State(OVERVIEW_GRAPH_ID, "id")],
    prevent_initial_call=True,
)


# --- FigureResampler update callback ---
# The plotly-resampler callback to update the graph after a relayout event (= zoom/pan)
# As we use the figure again as output, we need to set: allow_duplicate=True
@app.callback(
    Output(GRAPH_ID, "figure", allow_duplicate=True),
    Input(GRAPH_ID, "relayoutData"),
    State(STORE_ID, "data"),  # The server side cached FigureResampler per session
    prevent_initial_call=True,
)
def update_fig(relayoutdata, fig: FigureResampler):
    if fig is None:
        return no_update
    return fig.construct_update_data_patch(relayoutdata)


if __name__ == "__main__":
    # Start the app
    app.run(debug=True, host="localhost", port=8055, use_reloader=False)



================================================
FILE: examples/dash_apps/11_sine_generator.py
================================================
"""Dash runtime sine generator app example.

In this example, users can configure parameters of a sine wave and then generate the
sine-wave graph at runtime using the create-new-graph button. There is also an option
to remove the graph.

This app uses server side caching of the FigureResampler object. As it uses the same
concepts of the 03_minimal_cache_dynamic.py example, the runtime graph construction
callback is again split up into two callbacks: (1) the callback used to construct the
necessary components and send them to the front-end and (2) the callback used to
construct the plotly-resampler figure and cache it on the server side.

"""

from uuid import uuid4

import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objects as go
from dash import MATCH, Input, Output, State, callback_context, dcc, html, no_update
from dash_extensions.enrich import (
    DashProxy,
    Serverside,
    ServersideOutputTransform,
    Trigger,
    TriggerTransform,
)

from plotly_resampler import FigureResampler

# --------------------------------------Globals ---------------------------------------
app = DashProxy(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.LUX],
    transforms=[ServersideOutputTransform(), TriggerTransform()],
)

# -------- Construct the app layout --------
app.layout = html.Div(
    [
        html.Div(html.H1("Exponential sine generator"), style={"textAlign": "center"}),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Form(
                        [
                            dbc.Label("#datapoints:", style={"margin-left": "10px"}),
                            html.Br(),
                            dcc.Input(
                                id="nbr-datapoints",
                                placeholder="n",
                                type="number",
                                style={"margin-left": "10px"},
                            ),
                            *([html.Br()] * 2),
                            dbc.Label("exponent:", style={"margin-left": "10px"}),
                            html.Br(),
                            dcc.Input(
                                id="expansion-factor",
                                placeholder="pow",
                                type="number",
                                min=0.95,
                                max=1.00001,
                                style={"margin-left": "10px"},
                            ),
                            *([html.Br()] * 2),
                            dbc.Button(
                                "Create new graph",
                                id="add-graph-btn",
                                color="primary",
                                style={
                                    "textalign": "center",
                                    "width": "max-content",
                                    "margin-left": "10px",
                                },
                            ),
                            *([html.Br()] * 2),
                            dbc.Button(
                                "Remove last graph",
                                id="remove-graph-btn",
                                color="danger",
                                style={
                                    "textalign": "center",
                                    "width": "max-content",
                                    "margin-left": "10px",
                                },
                            ),
                        ],
                    ),
                    style={"align": "top"},
                    md=2,
                ),
                dbc.Col(html.Div(id="graph-container"), md=10),
            ],
        ),
    ]
)


# ------------------------------------ DASH logic -------------------------------------
# This method adds the needed components to the front-end, but does not yet contain the
# FigureResampler graph construction logic.
@app.callback(
    Output("graph-container", "children"),
    Input("add-graph-btn", "n_clicks"),
    Input("remove-graph-btn", "n_clicks"),
    [
        State("nbr-datapoints", "value"),
        State("expansion-factor", "value"),
        State("graph-container", "children"),
    ],
    prevent_initial_call=True,
)
def add_or_remove_graph(add_graph, remove_graph, n, exp, gc_children):
    if (add_graph is None or n is None or exp is None) and (remove_graph is None):
        return no_update

    # Transform the graph data to a figure
    gc_children = [] if gc_children is None else gc_children

    # Check if we need to remove a graph
    clicked_btns = [p["prop_id"] for p in callback_context.triggered]
    if any("remove-graph" in btn_name for btn_name in clicked_btns):
        if not len(gc_children):
            return no_update
        return gc_children[:-1]

    # No graph needs to be removed -> create a new graph
    uid = str(uuid4())
    new_child = html.Div(
        children=[
            # Note: we also add a dcc.Store component, which will be used to link the
            #       server side cached FigureResampler object
            dcc.Graph(id={"type": "dynamic-graph", "index": uid}, figure=go.Figure()),
            dcc.Loading(dcc.Store(id={"type": "store", "index": uid})),
            # This dcc.Interval components makes sure that the `construct_display_graph`
            # callback is fired once after these components are added to the session
            # its front-end
            dcc.Interval(
                id={"type": "interval", "index": uid}, max_intervals=1, interval=1
            ),
        ],
    )
    gc_children.append(new_child)
    return gc_children


# This method constructs the FigureResampler graph and caches it on the server side
@app.callback(
    Output({"type": "dynamic-graph", "index": MATCH}, "figure"),
    Output({"type": "store", "index": MATCH}, "data"),
    State("nbr-datapoints", "value"),
    State("expansion-factor", "value"),
    State("add-graph-btn", "n_clicks"),
    Trigger({"type": "interval", "index": MATCH}, "n_intervals"),
    prevent_initial_call=True,
)
def construct_display_graph(n, exp, n_added_graphs) -> FigureResampler:
    # Figure construction logic based on state variables
    x = np.arange(n)
    expansion_scaling = exp**x
    y = (
        np.sin(x / 200) * expansion_scaling
        + np.random.randn(n) / 10 * expansion_scaling
    )

    fr = FigureResampler(go.Figure(), verbose=True)
    fr.add_trace(go.Scattergl(name="sin"), hf_x=x, hf_y=y)
    fr.update_layout(
        height=350,
        showlegend=True,
        legend=dict(orientation="h", y=1.12, xanchor="right", x=1),
        template="plotly_white",
        title=f"graph {n_added_graphs} - n={n:,} pow={exp}",
        title_x=0.5,
    )

    return fr, Serverside(fr)


# --- FigureResampler update callback ---


# The plotly-resampler callback to update the graph after a relayout event (= zoom/pan)
# As we use the figure again as output, we need to set: allow_duplicate=True
@app.callback(
    Output({"type": "dynamic-graph", "index": MATCH}, "figure", allow_duplicate=True),
    Input({"type": "dynamic-graph", "index": MATCH}, "relayoutData"),
    State({"type": "store", "index": MATCH}, "data"),
    prevent_initial_call=True,
    memoize=True,
)
def update_fig(relayoutdata: dict, fig: FigureResampler):
    if fig is not None:
        return fig.construct_update_data_patch(relayoutdata)
    return no_update


# --------------------------------- Running the app ---------------------------------
if __name__ == "__main__":
    app.run_server(debug=True, port=9023, use_reloader=False)



================================================
FILE: examples/dash_apps/12_file_selector.py
================================================
"""Dash file parquet visualization app example.

In this use case, we have dropdowns which allows the end-user to select multiple
parquet files, which are visualized using FigureResampler after clicking on a button.

"""

__author__ = "Jonas Van Der Donckt"

from pathlib import Path
from typing import List

import dash_bootstrap_components as dbc
import plotly.graph_objects as go

from dash import callback_context, dcc, html, no_update
from dash_extensions.enrich import Output, Input, State
from dash_extensions.enrich import DashProxy, Serverside, ServersideOutputTransform
from utils.callback_helpers import get_selector_states, multiple_folder_file_selector
from utils.graph_construction import visualize_multiple_files

from plotly_resampler import FigureResampler

# --------------------------------------Globals ---------------------------------------
app = DashProxy(
    __name__,
    external_stylesheets=[dbc.themes.LUX],
    transforms=[ServersideOutputTransform()],
)

# --------- File selection configurations ---------
name_folder_list = [
    {
        # the key-string below is the title which will be shown in the dash app
        "example data": {"folder": Path(__file__).parent.parent.joinpath("data")},
        "other folder": {"folder": Path(__file__).parent.parent.joinpath("data")},
    },
    # NOTE: A new item om this level creates a new file-selector card.
    # { "PC data": { "folder": Path("/home/jonas/data/wesad/empatica/") } }
    # TODO: change the folder path above to a location where you have some
    # `.parquet` files stored on your machine.
]


# --------- DASH layout logic ---------
def serve_layout() -> dbc.Container:
    """Constructs the app's layout.

    Returns
    -------
    dbc.Container
        A Container withholding the layout.

    """
    return dbc.Container(
        [
            dbc.Container(
                html.H1("Data loading and visualization dashboard"),
                style={"textAlign": "center"},
            ),
            html.Hr(),
            dbc.Row(
                [
                    # Add file selection layout (+ assign callbacks)
                    dbc.Col(multiple_folder_file_selector(app, name_folder_list), md=2),
                    # Add the graph and the dcc.Store (for serialization)
                    dbc.Col(
                        [
                            dcc.Graph(id="graph-id", figure=go.Figure()),
                            dcc.Loading(dcc.Store(id="store")),
                        ],
                        md=10,
                    ),
                ],
                align="center",
            ),
        ],
        fluid=True,
    )


app.layout = serve_layout()


# ------------------------------------ DASH logic -------------------------------------
@app.callback(
    [Output("graph-id", "figure"), Output("store", "data")],
    [Input("plot-button", "n_clicks"), *get_selector_states(len(name_folder_list))],
    prevent_initial_call=True,
)
def plot_graph(n_clicks, *folder_list):
    it = iter(folder_list)
    file_list: List[Path] = []
    for folder, files in zip(it, it):
        if not all((folder, files)):
            continue
        else:
            for file in files:
                file_list.append((Path(folder).joinpath(file)))

    ctx = callback_context
    if len(ctx.triggered) and "plot-button" in ctx.triggered[0]["prop_id"]:
        if len(file_list):
            fig: FigureResampler = visualize_multiple_files(file_list)
            return fig, Serverside(fig)
    else:
        return no_update


# --------- FigureResampler update callback ---------


# The plotly-resampler callback to update the graph after a relayout event (= zoom/pan)
# As we use the figure again as output, we need to set: allow_duplicate=True
@app.callback(
    Output("graph-id", "figure", allow_duplicate=True),
    Input("graph-id", "relayoutData"),
    State("store", "data"),  # The server side cached FigureResampler per session
    prevent_initial_call=True,
)
def update_fig(relayoutdata: dict, fig: FigureResampler):
    if fig is None:
        return no_update
    return fig.construct_update_data_patch(relayoutdata)


# --------------------------------- Running the app ---------------------------------
if __name__ == "__main__":
    app.run_server(debug=True, port=9023, use_reloader=False)



================================================
FILE: examples/dash_apps/13_coarse_fine.py
================================================
"""Dash file parquet visualization app example with a coarse and fine-grained view.

In this use case, we have dropdowns which allows end-users to select multiple
parquet files, which are visualized using FigureResampler after clicking on a button.

There a two graphs displayed; a coarse and a dynamic graph. Interactions with the
coarse graph will affect the dynamic graph it's shown range. Note that the autosize
of the coarse graph is not linked.

TODO: add an rectangle on the coarse graph

"""

from __future__ import annotations

__author__ = "Jonas Van Der Donckt"

from pathlib import Path
from typing import List

import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash import Input, Output, State, callback_context, dcc, html, no_update
from dash_extensions.enrich import DashProxy, Serverside, ServersideOutputTransform
from utils.callback_helpers import get_selector_states, multiple_folder_file_selector
from utils.graph_construction import visualize_multiple_files

from plotly_resampler import FigureResampler

# --------------------------------------Globals ---------------------------------------
app = DashProxy(
    __name__,
    suppress_callback_exceptions=False,
    external_stylesheets=[dbc.themes.LUX],
    transforms=[ServersideOutputTransform()],
)

# --------- File selection configurations ---------
name_folder_list = [
    {
        # the key-string below is the title which will be shown in the dash app
        "example data": {"folder": Path(__file__).parent.parent.joinpath("data")},
        "other folder": {"folder": Path(__file__).parent.parent.joinpath("data")},
    },
    # NOTE: A new item om this level creates a new file-selector card.
    # { "PC data": { "folder": Path("/home/jonas/data/wesad/empatica/") } }
    # TODO: change the folder path above to a location where you have some
    # `.parquet` files stored on your machine.
]


# --------- DASH layout logic ---------
def serve_layout() -> dbc.Container:
    """Constructs the app's layout.

    Returns
    -------
    dbc.Container
        A Container withholding the layout.

    """
    return dbc.Container(
        [
            dbc.Container(
                html.H1("Data visualization - coarse & dynamic graph"),
                style={"textAlign": "center"},
            ),
            html.Hr(),
            dbc.Row(
                [
                    # Add file selection layout (+ assign callbacks)
                    dbc.Col(
                        multiple_folder_file_selector(
                            app, name_folder_list, multi=False
                        ),
                        md=2,
                    ),
                    # Add the graphs, the dcc.Store (for serialization) and the
                    dbc.Col(
                        [
                            # The coarse graph whose updates will fetch data for the
                            dcc.Graph(
                                id="coarse-graph",
                                figure=go.Figure(),
                                config={"modeBarButtonsToAdd": ["drawrect"]},
                            ),
                            html.Br(),
                            dcc.Graph(id="plotly-resampler-graph", figure=go.Figure()),
                            dcc.Loading(dcc.Store(id="store")),
                        ],
                        md=10,
                    ),
                ],
                align="center",
            ),
        ],
        fluid=True,
    )


app.layout = serve_layout()


# ------------------------------------ DASH logic -------------------------------------
# --------- graph construction logic + callback ---------
@app.callback(
    [
        Output("coarse-graph", "figure"),
        Output("plotly-resampler-graph", "figure"),
        Output("store", "data"),
    ],
    [Input("plot-button", "n_clicks"), *get_selector_states(len(name_folder_list))],
    prevent_initial_call=True,
)
def construct_plot_graph(n_clicks, *folder_list):
    it = iter(folder_list)
    file_list: List[Path] = []
    for folder, files in zip(it, it):
        if not all((folder, files)):
            continue
        else:
            files = [files] if not isinstance(files, list) else file_list
            for file in files:
                file_list.append((Path(folder).joinpath(file)))

    ctx = callback_context
    if len(ctx.triggered) and "plot-button" in ctx.triggered[0]["prop_id"]:
        if len(file_list):
            # Create two graphs, a dynamic plotly-resampler graph and a coarse graph
            dynamic_fig: FigureResampler = visualize_multiple_files(file_list)
            coarse_fig: go.Figure = go.Figure(
                FigureResampler(dynamic_fig, default_n_shown_samples=3_000)
            )

            coarse_fig.update_layout(title="<b>coarse view</b>", height=250)
            coarse_fig.update_layout(margin=dict(l=0, r=0, b=0, t=40, pad=10))
            coarse_fig.update_layout(showlegend=False)
            coarse_fig._config = coarse_fig._config.update(
                {"modeBarButtonsToAdd": ["drawrect"]}
            )

            dynamic_fig._global_n_shown_samples = 1000
            dynamic_fig.update_layout(title="<b>dynamic view<b>", height=450)
            dynamic_fig.update_layout(margin=dict(l=0, r=0, b=40, t=40, pad=10))
            dynamic_fig.update_layout(
                legend=dict(
                    orientation="h", y=-0.11, xanchor="right", x=1, font_size=18
                )
            )

            return coarse_fig, dynamic_fig, Serverside(dynamic_fig)
    else:
        return no_update


# Register the graph update callbacks to the layout
# As we use the figure again as output, we need to set: allow_duplicate=True
@app.callback(
    Output("plotly-resampler-graph", "figure", allow_duplicate=True),
    Input("coarse-graph", "relayoutData"),
    Input("plotly-resampler-graph", "relayoutData"),
    State("store", "data"),
    prevent_initial_call=True,
)
def update_dynamic_fig(
    coarse_grained_relayout: dict | None,
    fine_grained_relayout: dict | None,
    fr_fig: FigureResampler,
):
    if fr_fig is None:  # When the figure does not exist -> do nothing
        return no_update

    ctx = callback_context
    trigger_id = ctx.triggered[0].get("prop_id", "").split(".")[0]

    if trigger_id == "plotly-resampler-graph":
        return fr_fig.construct_update_data_patch(fine_grained_relayout)
    elif trigger_id == "coarse-graph":
        return fr_fig.construct_update_data_patch(coarse_grained_relayout)

    return no_update


# --------------------------------- Running the app ---------------------------------
if __name__ == "__main__":
    app.run_server(debug=True, port=9023, use_reloader=False)



================================================
FILE: examples/dash_apps/utils/callback_helpers.py
================================================
"""Dash helper functions for constructing a file seelector
"""

__author__ = "Jonas Van Der Donckt"

import itertools
from pathlib import Path
from typing import Dict, List

import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html
from functional import seq


def _update_file_widget(folder):
    if folder is None:
        return []
    return [
        {"label": filename, "value": filename}
        for filename in sorted(
            set(
                list(
                    seq(Path(folder).iterdir())
                    .filter(lambda x: x.is_file() and x.name.endswith("parquet"))
                    .map(lambda x: x.name)
                )
            )
        )
    ]


def _register_selection_callbacks(app, ids=None):
    if ids is None:
        ids = [""]

    for id in ids:
        app.callback(
            Output(f"file-selector{id}", "options"),
            [Input(f"folder-selector{id}", "value")],
        )(_update_file_widget)


def multiple_folder_file_selector(
    app, name_folders_list: List[Dict[str, dict]], multi=True
) -> dbc.Card:
    """Constructs a folder user date selector

    Creates a `dbc.Card` component which can be

    Parameters
    ----------
    app:
        The dash application.
    name_folders_list:List[Dict[str, Union[Path, str]]]
         A dict with key, the display-key and values the correspondign path.

    Returns
    -------
    A bootstrap card component
    """
    selector = dbc.Card(
        [
            dbc.Card(
                [
                    dbc.Col(
                        [
                            dbc.Label("folder"),
                            dcc.Dropdown(
                                id=f"folder-selector{i}",
                                options=[
                                    {"label": l, "value": str(f["folder"])}
                                    for (l, f) in name_folders.items()
                                ],
                                clearable=False,
                            ),
                            dbc.Label("file"),
                            dcc.Dropdown(
                                id=f"file-selector{i}",
                                options=[],
                                clearable=True,
                                multi=multi,
                            ),
                            html.Br(),
                        ]
                    ),
                ]
            )
            for i, name_folders in enumerate(name_folders_list, 1)
        ]
        + [
            dbc.Card(
                dbc.Col(
                    [
                        html.Br(),
                        dbc.Button(
                            "create figure",
                            id="plot-button",
                            color="primary",
                        ),
                    ],
                    style={"textAlign": "center"},
                ),
            )
        ],
        body=True,
    )

    _register_selection_callbacks(app=app, ids=range(1, len(name_folders_list) + 1))
    return selector


def get_selector_states(n: int) -> List[State]:
    """Return a list of all the folder-file selector fields, which are used as State

    Parameters
    ----------
    n: int
        The number of folder selectors

    """
    return list(
        itertools.chain.from_iterable(
            [
                (
                    State(f"folder-selector{i}", "value"),
                    State(f"file-selector{i}", "value"),
                )
                for i in range(1, n + 1)
            ]
        )
    )



================================================
FILE: examples/dash_apps/utils/graph_construction.py
================================================
from pathlib import Path
from typing import List, Union

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from plotly_resampler import FigureResampler
from plotly_resampler.aggregation import MinMaxLTTB


# --------- graph construction logic + callback ---------
def visualize_multiple_files(file_list: List[Union[str, Path]]) -> FigureResampler:
    """Create FigureResampler where each subplot row represents all signals from a file.

    Parameters
    ----------
    file_list: List[Union[str, Path]]

    Returns
    -------
    FigureResampler
        Returns a view of the existing, global FigureResampler object.

    """
    fig = FigureResampler(
        make_subplots(rows=len(file_list), shared_xaxes=False),
        default_downsampler=MinMaxLTTB(parallel=True),
    )
    fig.update_layout(height=min(900, 350 * len(file_list)))

    for i, f in enumerate(file_list, 1):
        df = pd.read_parquet(f)  # TODO: replace with more generic data loading code
        if "timestamp" in df.columns:
            df = df.set_index("timestamp")

        for c in df.columns[::-1]:
            fig.add_trace(go.Scattergl(name=c), hf_x=df.index, hf_y=df[c], row=i, col=1)
    return fig



================================================
FILE: examples/example_utils/loglttb.py
================================================
"""An (non-optimized) python implementation of the LTTB algorithm that utilizes 
log-scale buckets.
"""

import numpy as np
from plotly_resampler.aggregation.aggregation_interface import DataPointSelector
from typing import Union


class LogLTTB(DataPointSelector):
    @staticmethod
    def _argmax_area(prev_x, prev_y, avg_next_x, avg_next_y, x_bucket, y_bucket) -> int:
        """Vectorized triangular area argmax computation.

        Parameters
        ----------
        prev_x : float
            The previous selected point is x value.
        prev_y : float
            The previous selected point its y value.
        avg_next_x : float
            The x mean of the next bucket
        avg_next_y : float
            The y mean of the next bucket
        x_bucket : np.ndarray
            All x values in the bucket
        y_bucket : np.ndarray
            All y values in the bucket

        Returns
        -------
        int
            The index of the point with the largest triangular area.
        """
        return np.abs(
            x_bucket * (prev_y - avg_next_y)
            + y_bucket * (avg_next_x - prev_x)
            + (prev_x * avg_next_y - avg_next_x * prev_y)
        ).argmax()

    def _arg_downsample(
        self, x: Union[np.ndarray, None], y: np.ndarray, n_out: int, **kwargs
    ) -> np.ndarray:
        """Downsample to `n_out` points using the log variant of the LTTB algorithm.

        Parameters
        ----------
        x : np.ndarray
            The x-values of the data.
        y : np.ndarray
            The y-values of the data.
        n_out : int
            The number of points to downsample to.

        Returns
        -------
        np.ndarray
            The indices of the downsampled data.
        """
        # We need a valid x array to determine the x-range
        assert x is not None, "x cannot be None for this downsampler"

        # the log function to use
        lf = np.log1p

        offset = np.unique(
            np.searchsorted(
                x, np.exp(np.linspace(lf(x[0]), lf(x[-1]), n_out + 1)).astype(np.int64)
            )
        )

        # Construct the output array
        sampled_x = np.empty(len(offset) + 1, dtype="int64")
        sampled_x[0] = 0
        sampled_x[-1] = x.shape[0] - 1

        # Convert x & y to int if it is boolean
        if x.dtype == np.bool_:
            x = x.astype(np.int8)
        if y.dtype == np.bool_:
            y = y.astype(np.int8)

        a = 0
        for i in range(len(offset) - 2):
            a = (
                self._argmax_area(
                    prev_x=x[a],
                    prev_y=y[a],
                    avg_next_x=np.mean(x[offset[i + 1] : offset[i + 2]]),
                    avg_next_y=y[offset[i + 1] : offset[i + 2]].mean(),
                    x_bucket=x[offset[i] : offset[i + 1]],
                    y_bucket=y[offset[i] : offset[i + 1]],
                )
                + offset[i]
            )
            sampled_x[i + 1] = a

        # ------------ EDGE CASE ------------
        # next-average of last bucket = last point
        sampled_x[-2] = (
            self._argmax_area(
                prev_x=x[a],
                prev_y=y[a],
                avg_next_x=x[-1],  # last point
                avg_next_y=y[-1],
                x_bucket=x[offset[-2] : offset[-1]],
                y_bucket=y[offset[-2] : offset[-1]],
            )
            + offset[-2]
        )
        return sampled_x



================================================
FILE: examples/other_apps/streamlit_app.py
================================================
"""Minimal streamlit app example.

This example shows how to integrate plotly-resampler in a streamlit app.
The following thee steps are required;
1. use FigureResampler
2. run the visualization (which is a dash app) in a (sub)process on a certain port
3. add as iframe component to streamlit

To run this example execute the following command:
$ streamlit run streamlit_app.py

Note: to have colored traces in the streamlit app, you should always include the
following code: `import plotly.io as pio; pio.templates.default = "plotly"`

"""

__author__ = "Jeroen Van Der Donckt"

# Explicitly set pio.templates in order to have colored traces in the streamlit app!
# -> https://discuss.streamlit.io/t/streamlit-overrides-colours-of-plotly-chart/34943/5
import plotly.io as pio

pio.templates.default = "plotly"

# 0. Create a noisy sine wave
import numpy as np
import plotly.graph_objects as go

from plotly_resampler import FigureResampler

x = np.arange(1_000_000)
noisy_sin = (3 + np.sin(x / 200) + np.random.randn(len(x)) / 10) * x / 1_000

### 1. Use FigureResampler
fig = FigureResampler(default_n_shown_samples=2_000)
fig.add_trace(go.Scattergl(name="noisy sine", showlegend=True), hf_x=x, hf_y=noisy_sin)
fig.update_layout(height=700)

### 2. Run the visualization (which is a dash app) in a (sub)process on a certain port
# Note: starting a process allows executing code after `.show_dash` is called
from multiprocessing import Process

port = 9022
proc = Process(target=fig.show_dash, kwargs=dict(mode="external", port=port)).start()

# Deleting the lines below this and running this file will result in a classic running dash app
# Note: for just a dash app it is not even necessary to execute .show_dash in a (sub)process

### 3. Add as iframe component to streamlit
import streamlit.components.v1 as components

components.iframe(f"http://localhost:{port}", height=700)



================================================
FILE: mkdocs/dash_app_integration.md
================================================
# Dash apps 🤝

This documentation page describes how you can integrate `plotly-resampler` in a [dash](https://dash.plotly.com/) application.

Examples of dash apps with `plotly-resampler` can be found in the
[examples folder](https://github.com/predict-idlab/plotly-resampler/tree/main/examples) of the GitHub repository.

## Registering callbacks in a new dash app

When you add a `FigureResampler` figure in a basic dash app, you should:

- Register the [`FigureResampler`][figure_resampler.FigureResampler] figure its callbacks to the dash app.
      - The id of the [dcc.Graph](https://dash.plotly.com/dash-core-components/graph) component that contains the
      [`FigureResampler`][figure_resampler.FigureResampler] figure should be passed to the
      [`register_update_graph_callback`][figure_resampler.FigureResampler.register_update_graph_callback] method.

**Code illustration**:

```python
# Construct the to-be resampled figure
fig = FigureResampler(px.line(...))

# Construct app & its layout
app = dash.Dash(__name__)
app.layout = html.Div(children=[dcc.Graph(id="graph-id", figure=fig)])

# Register the callback
fig.register_update_graph_callback(app, "graph-id")

# start the app
app.run_server(debug=True)
```

!!! warning

    The above example serves as an illustration, but uses a _global variable_ to store the `FigureResampler` instance;
    this is not a good practice. Ideally you should cache the `FigureResampler` per session on the server side.
    In the [examples folder](https://github.com/predict-idlab/plotly-resampler/tree/main/examples),
    we provide several dash app examples where we perform server side caching of such figures.



================================================
FILE: mkdocs/FAQ.md
================================================
# FAQ ❓

??? abstract "What does the orange `~time|number` suffix in legend name indicate?"

    This tilde suffix is only shown when the data is aggregated and represents the _mean aggregation bin size_
    which is the mean index-range difference between two consecutive aggregated samples.

    > - for _time-indexed data_: the mean time-range between 2 consecutive (sampled) samples.
    > - for _numeric-indexed data_: the mean numeric range between 2 consecutive (sampled) samples.

    When the index is a range-index; the mean aggregation bin size represents the mean downsample ratio; i.e.,
    the mean number of samples that are aggregated into one sample.

??? abstract "What is the difference between plotly-resampler figures and plain plotly figures?"

    plotly-resampler can be thought of as wrapper around plain plotly figures
    which adds line-chart visualization scalability by dynamically aggregating the data of the figures w.r.t.
    the front-end view. plotly-resampler thus adds dynamic aggregation functionality to plain plotly figures.

    **important to know**:

    - `show` _always_ returns a static html view of the figure, i.e., no dynamic aggregation can be performed on that view.
    - To have dynamic aggregation:
          - with `FigureResampler`, you need to call `show_dash` (or output the object in a cell via `IPython.display`) ->
          which spawns a dash-web app, and the dynamic aggregation is realized with dash callback
          - with `FigureWidgetResampler`, you need to use `IPython.display` on the object,
          which uses widget-events to realize dynamic aggregation (via the running IPython kernel).

    **other changes of plotly-resampler figures w.r.t. vanilla plotly**:

    - double-clicking within a line-chart area does not Reset Axes, as it results in an “Autoscale” event.
    We decided to implement an Autoscale event as updating your y-range such that it shows all the data that
    is in your x-range
         - **Note**: vanilla Plotly figures their Autoscale result in Reset Axes behavior,
         in our opinion this did not make a lot of sense.
         It is therefore that we have overriden this behavior in plotly-resampler.

??? abstract "My `FigureResampler.show_dash` keeps hanging (indefinitely) with the error message: `OSError: Port already in use`"

    !!! info "Disclaimer"
        Since v0.9.0 we use Dash instead of JupyterDash for Jupyter integration which should have resolved this issue!


    Plotly-resampler its `FigureResampler.show_dash` method leverages the [jupyterdash](https://github.com/plotly/jupyter-dash)
    toolkit to easily allow integration of dash apps in notebooks.
    However, there is a [known issue](https://github.com/plotly/jupyter-dash/pull/105) with jupyterDash that causes the `FigureResampler.show_dash`
    method to hang when the port is already in use. In a future Pull-Request they will hopefully fix this issue.
    We internally track this [issue](https://github.com/predict-idlab/plotly-resampler/issues/123) as well -
    please comment there if you want to provide feedback.

    In the meantime, you can use the following workaround (if you do not care about the [Werkzeug security issue](https://github.com/predict-idlab/plotly-resampler/pull/174)):
    `pip install werkzeug==2.1.2`.

??? abstract "What is the difference in approach between plotly-resampler and datashader?"

    [Datashader](https://datashader.org/getting_started/Introduction.html) is a highly scalable
    [open-source](https://github.com/holoviz/datashader) library for analyzing and visualizing large datasets.
    More specifically, datashader _“rasterizes”_ or _“aggregates”_ datasets into regular grids
    that can be analyzed further or viewed as **images**.

    **The main differences are**:

    Datashader can deal with various kinds of data (e.g., location related data, point clouds),
    whereas plotly-resampler is more tailored towards time-series data visualizations.
    Furthermore, datashader outputs a **rasterized image/array** encompassing all traces their data,
    whereas plotly-resampler outputs an **aggregated series** per trace.
    Thus, datashader is more suited for analyzing data where you do not want to pin-out a certain series/trace.

    In our opinion, datashader truly shines (for the time series use case) when:

    - you want a global, overlaying view of all your traces
    - you want to visualize a large number of time series in a single plot (many traces)
    - there is a lot of noise on your high-frequency data and you want to uncover the underlying pattern
    - you want to render all data points in your visualization

    In our opinion, plotly-resampler shines when:

    - you need the capabilities to interact with the traces (e.g., hovering, toggling traces, hovertext per trace)
    - you want to use a less complex (but more restricted) visualization interface (as opposed to holoviews), i.e., plotly
    - you want to make existing plotly time-series figures more scalable and efficient
    - to build scalable Dash apps for time-series data visualization

    Furthermore combined with holoviews, datashader can also be employed in an interactive manner, see the example below.

    ```python
       from holoviews.operation.datashader import datashade
       import datashader as ds
       import holoviews as hv
       import numpy as np
       import pandas as pd
       import panel as pn

       hv.extension("bokeh")
       pn.extension(comms='ipywidgets')

       # Create the dummy dataframe
       n = 1_000_000
       x = np.arange(n)
       noisy_sine = (np.sin(x / 3_000) + (np.random.randn(n) / 10)) * x / 5_000
       df = pd.DataFrame(
          {"ns": noisy_sine, "ns_abs": np.abs(noisy_sine),}
       )

       # Visualize interactively with datashader
       opts = hv.opts.RGB(width=800, height=400)
       ndoverlay = hv.NdOverlay({c:hv.Curve((df.index, df[c])) for c in df.columns})
       datashade(ndoverlay, cnorm='linear', aggregator=ds.count(), line_width=3).opts(opts)
    ```

    ![interactive datashader example](static/datashader.png)

??? abstract "Pandas or numpy datetime works much slower than unix epoch timestamps?"

    This stems from the plotly scatter(gl) constructor being much slower for non-numeric data.
    Plotly performs a different serialization for datetime arrays (which are interpreted as object arrays).
    However, plotly-resampler should not be limited by this - to avoid this issue,
    add your datetime data as _hf_x_ to your plotly-resampler `FigureResampler.add_trace`
    (or `FigureWidgetResampler.add_trace`) method. This avoids adding (& serializing) _all_ the data to the scatter object,
    since plotly-resampler will pass the aggregated data to the scatter object.

    Some illustration:

    ```python
    import plotly.graph_objects as go
    import pandas as pd
    import numpy as np
    from plotly_resampler import FigureResampler

    # Create the dummy dataframe
    y = np.arange(1_000_000)
    x = pd.date_range(start="2020-01-01", periods=len(y), freq="1s")

    # Create the plotly-resampler figure
    fig = FigureResampler()
    # fig.add_trace(go.Scatter(x=x, y=y))  # This is slow
    fig.add_trace(go.Scatter(), hf_x=x, hf_y=y)  # This is fast

    # ... (add more traces, etc.)
    ```



================================================
FILE: mkdocs/gen_ref_pages.py
================================================
"""Generate the code reference pages."""

from pathlib import Path

import mkdocs_gen_files

SRC_DIR = "plotly_resampler"
API_DIR = "api"

nav = mkdocs_gen_files.nav.Nav()

for path in sorted(Path(SRC_DIR).rglob("*.py")):
    module_path = path.relative_to(SRC_DIR).with_suffix("")
    doc_path = path.relative_to(SRC_DIR).with_suffix(".md")
    full_doc_path = Path(API_DIR, doc_path)

    parts = tuple(module_path.parts)

    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
    elif parts[-1] == "__main__":
        continue

    if len(parts) == 0:
        continue

    nav[parts] = doc_path.as_posix()

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        identifier = ".".join(parts)
        print("::: " + identifier, file=fd)

    mkdocs_gen_files.set_edit_path(full_doc_path, path)

with mkdocs_gen_files.open(API_DIR + "/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())



================================================
FILE: mkdocs/getting_started.md
================================================
# Get started 🚀

The `plotly-resampler` package offers two primary modules:

- [`figure_resampler`][figure_resampler]: a wrapper for _plotly.graph_objects Figures_,
  coupling dynamic resampling functionality with the _Figure_.
- [`aggregation`][aggregation]: This module contains interfaces for the various aggregation methods implemented in [tsdownsample](https://github.com/predict-idlab/tsdownsample).

## Installation ⚙️

Install via [pip](https://pypi.org/project/plotly-resampler/):

```
pip install plotly-resampler
```

## Usage 📈

Plotly-Resampler facilitates dynamic resampling in two ways:

- **Automatic Approach** (low code overhead)
    - utilize the [`register_plotly_resampler`][registering.register_plotly_resampler] function
    - steps:
        1. Import and invoke [`register_plotly_resampler`][registering.register_plotly_resampler]
        2. That's it! 🎉<br>Just proceed with your standard gaph construction workflow.
    - Upon invoking [`register_plotly_resampler`][registering.register_plotly_resampler], all new defined plotly graph objects are transformed into either 
      [`FigureResampler`][figure_resampler.FigureResampler] or
      [`FigureWidgetResampler`][figure_resampler.FigureWidgetResampler] object.  The `mode` parameter in this method determines which resampling Figure type is used.

- **Manual Approach** (data aggregation configurability, graph construction speedups)
    1. By utilizing [Dash](https://github.com/plotly/dash) callbacks to augment a `go.Figure` with dynamic aggregation functionality.
        - steps:
            1. wrap the plotly Figure with [`FigureResampler`][figure_resampler.FigureResampler]
            2. call [`.show_dash()`][figure_resampler.FigureResampler.show_dash] on the Figure
        !!! note
            This is particularly advantageous when working with Dash or outside Jupyter environments.

    2. By utilizing [FigureWidget.layout.on_change](https://plotly.com/python-api-reference/generated/plotly.html?highlight=on_change#plotly.basedatatypes.BasePlotlyType.on_change)
      , when a `go.FigureWidget` is used within a `.ipynb` environment.
        - steps:
            1. wrap your plotly Figure
              (can be a `go.Figure` with [`FigureWidgetResampler`][figure_resampler.FigureWidgetResampler])
            2. output the `FigureWidgetResampler` instance in a cell

            !!! note
                This is especially useful when developing in `jupyter` environments and when **you cannot open/forward a network-port.**


!!! tip

    For **significant faster initial loading** of the Figure, we advise to 

    1. wrap the constructor of the plotly Figure with either [`FigureResampler`][figure_resampler.FigureResampler] or [`FigureWidgetResampler`][figure_resampler.FigureWidgetResampler]
    2. add the trace data as `hf_x` and `hf_y`

!!! note

    Any plotly Figure can be wrapped with dynamic aggregation functionality! 🎉<br>
    But **only** `go.Scatter/go.Scattergl` traces **will be resampled**!

## Examples ✅

### register_plotly_resampler

```python
import plotly.graph_objects as go; import numpy as np
from plotly_resampler import register_plotly_resampler, unregister_plotly_resampler

# Call the register function once and all Figures/FigureWidgets will be wrapped
# according to the register_plotly_resampler its `mode` argument
register_plotly_resampler(mode='auto')

x = np.arange(1_000_000)
noisy_sin = (3 + np.sin(x / 200) + np.random.randn(len(x)) / 10) * x / 1_000


# when working in an IPython environment, this will automatically be a
# FigureWidgetResampler else, this will be an FigureResampler
f = go.Figure()
f.add_trace({"y": noisy_sin + 2, "name": "yp2"})
f

# to undo the wrapping, call the unregister_plotly_resampler function
```

### FigureResampler

```python
# NOTE: this example works in a notebook environment
import plotly.graph_objects as go; import numpy as np
from plotly_resampler import FigureResampler

x = np.arange(1_000_000)
sin = (3 + np.sin(x / 200) + np.random.randn(len(x)) / 10) * x / 1_000

fig = FigureResampler(go.Figure())
fig.add_trace(go.Scattergl(name='noisy sine', showlegend=True), hf_x=x, hf_y=sin)

fig.show_dash(mode='inline')
```

### Overview

In the example below, we demonstrate the (x-axis)`overview` feature of plotly-ressampler.
For more information you can check out the [examples](https://github.com/predict-idlab/plotly-resampler/tree/main/examples) to find dash apps and in-notebook use-cases.

!!! Note:
  - This overview is only available for the `FigureResampler` and not for the `FigureWidgetResampler`.
  - As a recent and experimental feature, user feedback is crucial. Please report any issues encountered!


![FigureResampler overview](static/basic_example_overview.gif)

### FigureWidget

The gif below demonstrates the example usage of [`FigureWidgetResampler`][figure_resampler.FigureWidgetResampler], where `JupyterLab` is used as the environment and the `FigureWidgetResampler`.<br><br>
Note how (i) the figure output is redirected into a new view, and (ii) how you are able to dynamically add traces!

![FigureWidget example](static/figurewidget.gif)

Furthermore, plotly’s `FigureWidget` allows to conveniently add callbacks to for example click events. This allows creating a high-frequency time series annotation app in a couple of lines; as shown in the gif below and in this [notebook](https://github.com/predict-idlab/plotly-resampler/blob/main/examples/figurewidget_example.ipynb).

![Annotate Twitter](static/annotate_twitter.gif)

## Important considerations & tips 🚨

- When running the code on a server, you should forward the port of the
  [`FigureResampler.show_dash`][figure_resampler.FigureResampler.show_dash] method to your local machine.  
  **Note** that you can add dynamic aggregation to plotly figures with the
  [`FigureWidgetResampler`][figure_resampler.FigureWidgetResampler] wrapper without needing to forward a port!
- In general, when using downsampling one should be aware of (possible) [aliasing](https://en.wikipedia.org/wiki/Aliasing) effects.
  The `[R]` in the legend indicates when the corresponding trace is resampled (and thus possibly distorted).
  The `~ delta` suffix in the legend represents the mean index delta for consecutive aggregated data points.
- The plotly **autoscale** event (triggered by the autoscale button or a double-click within the graph),
  **does not reset the axes but autoscales the current graph-view of plotly-resampler figures**.
  This design choice was made as it seemed more intuitive for the developers to support this behavior
  with double-click than the default axes-reset behavior.
  The graph axes can ofcourse be resetted by using the reset_axis button.
  If you want to give feedback and discuss this further with the developers, see this issue [#49](https://github.com/predict-idlab/plotly-resampler/issues/49).

### Dynamically adjusting the scatter data 🔩

The raw high-frequency trace data of plotly-resampler figures can be adjusted using the `hf_data` property.

Working example ⬇️:

```python
import plotly.graph_objects as go; import numpy as np
from plotly_resampler import FigureResampler
# Note: a FigureWidgetResampler can be used here as well

# Construct the hf-data
x = np.arange(1_000_000)
sin = (3 + np.sin(x / 200) + np.random.randn(len(x)) / 10) * x / 1_000

fig = FigureResampler(go.Figure())
fig.add_trace(go.Scattergl(name='noisy sine', showlegend=True), hf_x=x, hf_y=sin)
fig.show_dash(mode='inline')

# After some time -> update the hf_data y property of the trace
# As we only have 1 trace, this needs to be mapped
fig.hf_data[-1]['y'] = - sin ** 2
```

!!! note

    _hf_data_ only withholds high-frequency traces (i.e., traces that are aggregated).
    To add non high-frequency traces (i.e., traces with fewer data points than _max_n_samples_),
    you need to set the `limit_to_view` argument to _True_ when adding the corresponding trace with the
    [`add_trace`][figure_resampler.figure_resampler_interface.AbstractFigureAggregator.add_trace] function.

!!! tip

    The `FigureWidgetResampler` graph will not be automatically redrawn after adjusting the fig its _hf_data_ property.
    The redrawing can be triggered by manually calling either:

    - [`FigureWidgetResampler.reload_data`][figure_resampler.FigureWidgetResampler.reload_data],
    which keeps the current-graph range.
    - [`FigureWidgetResampler.reset_axes`][figure_resampler.FigureWidgetResampler.reset_axes],
    which performs a graph update.

### Plotly-resampler & not high-frequency traces 🔍

!!! tip

    In the _Skin conductance example_ of the [basic_example.ipynb](https://github.com/predict-idlab/plotly-resampler/tree/main/examples),
    we deal with such low-frequency traces.

The `add_trace` method allows configuring argument which allows us to deal with low-frequency traces.

#### Use-cases

- **not resampling** trace data: To achieve this, set:

  - `#!python max_n_samples = len(hf_x)`

- **not resampling** trace data, but **slicing to the view**: To achieve this, set:
  - `#!python max_n_samples = len(hf_x)`
  - `#!python limit_to_view = True`

!!! note

    For, **irregularly sampled traces** which are **filled** (e.g. _colored background_ signal quality trace of the skin conductance example),
    it is important that you set `gap_handler` to `NoGapHandler` for that trace.

    Otherwise, when you leave `gap_handler` to `MedDiffGapHandler`, you may get weird background shapes such as ⬇️:
    ![Skin conductance example with gap interleaving](static/skin_conductance_interleave_gaps_true.png)

    When `gap_handler` is set to `NoGapHandler` you get ⬇️:
    ![Skin conductance example without gap interleaving](static/skin_conductance_interleave_gaps_false.png)



================================================
FILE: mkdocs/index.md
================================================
# Welcome to plotly-resampler's documentation!

This is the documentation of ![plotly-resampler](https://github.com/predict-idlab/plotly-resampler);
a wrapper for plotly Figures to **visualize large time-series** data.

![Basic Example](static/basic_example.gif)

As shown in the demo above, `plotly-resampler` maintains its interactiveness on large data by applying front-end
**resampling respective to the view**.

[:fontawesome-solid-download: PyPI](https://pypi.org/project/plotly-resampler/){ .md-button .md-button--primary }
[:simple-github: Github](https://github.com/predict-idlab/plotly-resampler){ .md-button .md-button--primary }
[:simple-doi: DOI](https://doi.org/10.48550/arXiv.2206.08703){ .md-button .md-button--primary }



================================================
FILE: plotly_resampler/__init__.py
================================================
"""**plotly_resampler**: visualizing large sequences."""

import contextlib

from .aggregation import LTTB, EveryNthPoint, MinMaxLTTB
from .figure_resampler import ASSETS_FOLDER, FigureResampler, FigureWidgetResampler
from .registering import register_plotly_resampler, unregister_plotly_resampler

__docformat__ = "numpy"
__author__ = "Jonas Van Der Donckt, Jeroen Van Der Donckt, Emiel Deprost"
__version__ = "0.11.0rc1"

__all__ = [
    "__version__",
    "FigureResampler",
    "FigureWidgetResampler",
    "ASSETS_FOLDER",
    "MinMaxLTTB",
    "LTTB",
    "EveryNthPoint",
    "register_plotly_resampler",
    "unregister_plotly_resampler",
]


# Enable ipywidgets on google colab!
with contextlib.suppress(ImportError, ModuleNotFoundError):
    import sys

    if "google.colab" in sys.modules:
        from google.colab import output

        output.enable_custom_widget_manager()



================================================
FILE: plotly_resampler/registering.py
================================================
"""Register plotly-resampler to (un)wrap plotly-graph-objects."""

__author__ = "Jeroen Van Der Donckt, Jonas Van Der Donckt, Emiel Deprost"

from functools import wraps

import plotly

from plotly_resampler import FigureResampler, FigureWidgetResampler
from plotly_resampler.figure_resampler.figure_resampler_interface import (
    AbstractFigureAggregator,
)

WRAPPED_PREFIX = "[Plotly-Resampler]__"
PLOTLY_MODULES = [
    plotly.graph_objs,
    plotly.graph_objects,
]  # wait for this PR https://github.com/plotly/plotly.py/pull/3779
PLOTLY_CONSTRUCTOR_WRAPPER = {
    "Figure": FigureResampler,
    "FigureWidget": FigureWidgetResampler,
}


def _already_wrapped(constr):
    return constr.__name__.startswith(WRAPPED_PREFIX)


def _get_plotly_constr(constr):
    """Return the constructor of the underlying plotly graph object and thus omit the
    possibly wrapped [`AbstractFigureAggregator`][figure_resampler.figure_resampler_interface.AbstractFigureAggregator]
    instance.

    Parameters
    ----------
    constr : callable
        The constructor of a instantiated plotly-object.

    Returns
    -------
    callable
        The constructor of a ``go.FigureWidget`` or a ``go.Figure``.
    """
    if _already_wrapped(constr):
        return constr.__wrapped__  # get the original constructor
    return constr


### Registering the wrappers


def _is_ipython_env():
    """Check if we are in an IPython environment (with a kernel)."""
    try:
        from IPython import get_ipython

        return "IPKernelApp" in get_ipython().config
    except (ImportError, AttributeError):
        return False


def _register_wrapper(
    module: type,
    constr_name: str,
    pr_class: AbstractFigureAggregator,
    **aggregator_kwargs,
):
    constr = getattr(module, constr_name)
    constr = _get_plotly_constr(constr)  # get the original plotly constructor

    # print(f"Wrapping {constr_name} with {pr_class}")

    @wraps(constr)
    def wrapped_constr(*args, **kwargs):
        # print(f"Executing constructor wrapper for {constr_name}", constr)
        return pr_class(constr(*args, **kwargs), **aggregator_kwargs)

    wrapped_constr.__name__ = WRAPPED_PREFIX + constr_name
    setattr(module, constr_name, wrapped_constr)


def register_plotly_resampler(mode="auto", **aggregator_kwargs):
    """Register plotly-resampler to plotly.graph_objects.

    This function results in the use of plotly-resampler under the hood.

    !!! note
        We advise to use mode= ``widget`` when working in an IPython based environment
        as this will just behave as a ``go.FigureWidget``, but with dynamic aggregation.
        When using mode= ``auto`` or ``figure``; most figures will be wrapped as
        [`FigureResampler`][figure_resampler.FigureResampler], on which
        [`show_dash`][figure_resampler.FigureResampler.show_dash] needs to be called.

    !!! note
        This function is mostly useful for notebooks. For dash-apps, we advise to look
        at the dash app examples on [GitHub](https://github.com/predict-idlab/plotly-resampler/tree/main/examples#2-dash-apps)

    Parameters
    ----------
    mode : str, optional
        The mode of the plotly-resampler.
        Possible values are: 'auto', 'figure', 'widget', None.
        If 'auto' is used, the mode is determined based on the environment; if it is in
        an IPython environment, the mode is 'widget', otherwise it is 'figure'.
        If 'figure' is used, all plotly figures are wrapped as FigureResampler objects.
        If 'widget' is used, all plotly figure widgets are wrapped as
        FigureWidgetResampler objects (we advise to use this mode in IPython environment
        with a kernel).
        If None is used, wrapping is done as expected (go.Figure -> FigureResampler,
        go.FigureWidget -> FigureWidgetResampler).
    aggregator_kwargs : dict, optional
        The keyword arguments to pass to the plotly-resampler decorator its constructor.
        See more details in [`FigureResampler`][figure_resampler.FigureResampler] and
        [`FigureWidgetResampler`][figure_resampler.FigureWidgetResampler].

    """
    for constr_name, pr_class in PLOTLY_CONSTRUCTOR_WRAPPER.items():
        if (mode == "auto" and _is_ipython_env()) or mode == "widget":
            pr_class = FigureWidgetResampler
        elif mode == "figure":
            pr_class = FigureResampler
        # else: default mode -> wrap according to PLOTLY_CONSTRUCTOR_WRAPPER

        for module in PLOTLY_MODULES:
            _register_wrapper(module, constr_name, pr_class, **aggregator_kwargs)


### Unregistering the wrappers


def _unregister_wrapper(module: type, constr_name: str):
    constr = getattr(module, constr_name)
    if _already_wrapped(constr):
        constr = constr.__wrapped__
        setattr(module, constr_name, constr)


def unregister_plotly_resampler():
    """Unregister plotly-resampler from plotly.graph_objects."""
    for constr in PLOTLY_CONSTRUCTOR_WRAPPER.keys():
        for module in PLOTLY_MODULES:
            _unregister_wrapper(module, constr)



================================================
FILE: plotly_resampler/aggregation/__init__.py
================================================
"""
Compatible implementation for various downsample methods and open interface to 
other downsample methods.

"""

__author__ = "Jonas Van Der Donckt"


from .aggregation_interface import AbstractAggregator
from .aggregators import (
    LTTB,
    EveryNthPoint,
    FuncAggregator,
    MinMaxAggregator,
    MinMaxLTTB,
    MinMaxOverlapAggregator,
)
from .gap_handler_interface import AbstractGapHandler
from .gap_handlers import MedDiffGapHandler, NoGapHandler
from .plotly_aggregator_parser import PlotlyAggregatorParser

__all__ = [
    "AbstractAggregator",
    "AbstractGapHandler",
    "PlotlyAggregatorParser",
    "LTTB",
    "MinMaxLTTB",
    "EveryNthPoint",
    "FuncAggregator",
    "MedDiffGapHandler",
    "MinMaxAggregator",
    "MinMaxOverlapAggregator",
    "NoGapHandler",
]



================================================
FILE: plotly_resampler/aggregation/aggregation_interface.py
================================================
"""AbstractAggregator interface-class, subclassed by concrete aggregators."""

from __future__ import annotations

__author__ = "Jonas Van Der Donckt"

import re
from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

import numpy as np


class AbstractAggregator(ABC):
    def __init__(
        self,
        x_dtype_regex_list: Optional[List[str]] = None,
        y_dtype_regex_list: Optional[List[str]] = None,
        **downsample_kwargs,
    ):
        """Constructor of AbstractSeriesAggregator.

        Parameters
        ----------
        x_dtype_regex_list: List[str], optional
            List containing the regex matching the supported datatypes for the x array,
            by default None.
        y_dtype_regex_list: List[str], optional
            List containing the regex matching the supported datatypes for the y array,
            by default None.
        downsample_kwargs: dict
            Additional kwargs passed to the downsample method.

        """
        self.x_dtype_regex_list = x_dtype_regex_list
        self.y_dtype_regex_list = y_dtype_regex_list
        self.downsample_kwargs = downsample_kwargs

    @staticmethod
    def _check_n_out(n_out: int) -> None:
        """Check if the n_out is valid."""
        assert isinstance(n_out, (int, np.integer))
        assert n_out > 0

    @staticmethod
    def _process_args(*args) -> Tuple[np.ndarray | None, np.ndarray]:
        """Process the args into the x and y arrays.

        If only y is passed, x is set to None.
        """
        assert len(args) in [1, 2], "Must pass either 1 or 2 arrays"
        x, y = (None, args[0]) if len(args) == 1 else args
        return x, y

    @staticmethod
    def _check_arr(arr: np.ndarray, regex_list: Optional[List[str]] = None):
        """Check if the array is valid."""
        assert isinstance(arr, np.ndarray), f"Expected np.ndarray, got {type(arr)}"
        assert arr.ndim == 1
        AbstractAggregator._supports_dtype(arr, regex_list)

    def _check_x_y(self, x: np.ndarray | None, y: np.ndarray) -> None:
        """Check if the x and y arrays are valid."""
        # Check x (if not None)
        if x is not None:
            self._check_arr(x, self.x_dtype_regex_list)
            assert x.shape == y.shape, "x and y must have the same shape"
        # Check y
        self._check_arr(y, self.y_dtype_regex_list)

    @staticmethod
    def _supports_dtype(arr: np.ndarray, dtype_regex_list: Optional[List[str]] = None):
        # base case
        if dtype_regex_list is None:
            return

        for dtype_regex_str in dtype_regex_list:
            m = re.compile(dtype_regex_str).match(str(arr.dtype))
            if m is not None:  # a match is found
                return
        raise ValueError(
            f"{arr.dtype} doesn't match with any regex in {dtype_regex_list}"
        )


class DataAggregator(AbstractAggregator, ABC):
    """Implementation of the AbstractAggregator interface for data aggregation.

    DataAggregator differs from DataPointSelector in that it doesn't select data points,
    but rather aggregates the data (e.g., mean).
    As such, the `_aggregate` method is responsible for aggregating the data, and thus
    returns a tuple of the aggregated x and y values.

    Concrete implementations of this class must implement the `_aggregate` method, and
    have full responsibility on how they deal with other high-frequency properties, such
    as `hovertext`, `marker_size`, 'marker_color`, etc ...
    """

    @abstractmethod
    def _aggregate(
        self,
        x: np.ndarray | None,
        y: np.ndarray,
        n_out: int,
    ) -> Tuple[np.ndarray, np.ndarray]:
        raise NotImplementedError

    def aggregate(
        self,
        *args,
        n_out: int,
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Aggregate the data.

        Parameters
        ----------
        x, y: np.ndarray
            The x and y data of the to-be-aggregated series.
            The x array is optional (i.e., if only 1 array is passed, it is assumed to
            be the y array).
            The array(s) must be 1-dimensional, and have the same length (if x is
            passed).
            These cannot be passed as keyword arguments, as they are positional-only.
        n_out: int
            The number of samples which the downsampled series should contain.
            This should be passed as a keyword argument.

        Returns
        -------
        Tuple[np.ndarray, np.ndarray]
            The aggregated x and y data, respectively.

        """
        # Check n_out
        assert n_out is not None

        # Get x and y
        x, y = DataPointSelector._process_args(*args)

        # Check x and y
        self._check_x_y(x, y)

        return self._aggregate(x=x, y=y, n_out=n_out)


class DataPointSelector(AbstractAggregator, ABC):
    """Implementation of the AbstractAggregator interface for data point selection.

    DataPointSelector differs from DataAggregator in that they don't aggregate the data
    (e.g., mean) but instead select data points (e.g., first, last, min, max, etc ...).
    As such, the `_arg_downsample` method returns the index positions of the selected
    data points.

    This class utilizes the `arg_downsample` method to compute the index positions.
    """

    @abstractmethod
    def _arg_downsample(
        self,
        x: np.ndarray | None,
        y: np.ndarray,
        n_out: int,
    ) -> np.ndarray:
        # Note: this method can utilize the self.downsample_kwargs property
        raise NotImplementedError

    def arg_downsample(
        self,
        *args,
        n_out: int,
    ) -> np.ndarray:
        """Compute the index positions for the downsampled representation.

        Parameters
        ----------
        x, y: np.ndarray
            The x and y data of the to-be-aggregated series.
            The x array is optional (i.e., if only 1 array is passed, it is assumed to
            be the y array).
            The array(s) must be 1-dimensional, and have the same length (if x is
            passed).
            These cannot be passed as keyword arguments, as they are positional-only.
        n_out: int
            The number of samples which the downsampled series should contain.
            This should be passed as a keyword argument.

        Returns
        -------
        np.ndarray
            The index positions of the selected data points.

        """
        # Check n_out
        DataPointSelector._check_n_out(n_out)

        # Get x and y
        x, y = DataPointSelector._process_args(*args)

        # Check x and y
        self._check_x_y(x, y)

        if len(y) <= n_out:
            # Fewer samples than n_out -> return all indices
            return np.arange(len(y))

        # More samples that n_out -> perform data aggregation
        return self._arg_downsample(x=x, y=y, n_out=n_out)



================================================
FILE: plotly_resampler/aggregation/aggregators.py
================================================
# -*- coding: utf-8 -*-
"""Compatible implementation for various aggregation/downsample methods.

"""

from __future__ import annotations

__author__ = "Jonas Van Der Donckt"


import math
from typing import Tuple

import numpy as np
from tsdownsample import (
    EveryNthDownsampler,
    LTTBDownsampler,
    MinMaxDownsampler,
    MinMaxLTTBDownsampler,
    NaNMinMaxDownsampler,
    NaNMinMaxLTTBDownsampler,
)

from ..aggregation.aggregation_interface import DataAggregator, DataPointSelector


def _to_tsdownsample_args(
    x: np.ndarray | None, y: np.ndarray
) -> Tuple[np.ndarray, ...]:
    """Converts x & y to the arguments expected by tsdownsample."""
    if x is None:
        return (y,)
    return (x, y)


class LTTB(DataPointSelector):
    """Largest Triangle Three Buckets (LTTB) aggregation method.

    This is arguably the most widely used aggregation method. It is based on the
    effective area of a triangle (inspired from the line simplification domain).
    The algorithm has $O(n)$ complexity, however, for large datasets, it can be much
    slower than other algorithms (e.g. MinMax) due to the higher cost of calculating
    the areas of triangles.

    Thesis: [https://skemman.is/bitstream/1946/15343/3/SS_MSthesis.pdf](https://skemman.is/bitstream/1946/15343/3/SS_MSthesis.pdf) <br/>
    Details on visual representativeness & stability: [https://arxiv.org/abs/2304.00900](https://arxiv.org/abs/2304.00900)

    !!! tip

        `LTTB` doesn't scale super-well when moving to really large datasets, so when
        dealing with more than 1 million samples, you might consider using
        [`MinMaxLTTB`][aggregation.aggregators.MinMaxLTTB].


    !!! note

        * This class is mainly designed to operate on numerical data as LTTB calculates
          distances on the values. <br/>
          When dealing with categories, the data is encoded into its numeric codes,
          these codes are the indices of the category array.
        * To aggregate category data with LTTB, your ``pd.Series`` must be of dtype
          'category'. <br/>

          **tip**:

          if there is an order in your categories, order them that way, LTTB uses
          the ordered category codes values (see bullet above) to calculate distances and
          make aggregation decisions. <br/>
          **code**:
            ```python
                >>> import pandas as pd
                >>> s = pd.Series(["a", "b", "c", "a"])
                >>> cat_type = pd.CategoricalDtype(categories=["b", "c", "a"], ordered=True)
                >>> s_cat = s.astype(cat_type)
            ```
        * `LTTB` has no downsample kwargs, as it cannot be paralellized. Instead, you can
          use the [`MinMaxLTTB`][aggregation.aggregators.MinMaxLTTB] downsampler, which performs
          minmax preselection (in parallel if configured so), followed by LTTB.

    """

    def __init__(self):
        super().__init__(
            y_dtype_regex_list=[rf"{dtype}\d*" for dtype in ("float", "int", "uint")]
            + ["category", "bool"],
        )
        self.downsampler = LTTBDownsampler()

    def _arg_downsample(
        self,
        x: np.ndarray | None,
        y: np.ndarray,
        n_out: int,
    ) -> np.ndarray:
        return self.downsampler.downsample(*_to_tsdownsample_args(x, y), n_out=n_out)


class MinMaxOverlapAggregator(DataPointSelector):
    """Aggregation method which performs binned min-max aggregation over 50% overlapping
    windows.

    ![minmax operator image](https://github.com/predict-idlab/plotly-resampler/blob/main/mkdocs/static/minmax_operator.png)

    In the above image, **bin_size**: represents the size of *(len(series) / n_out)*.
    As the windows have 50% overlap and are consecutive, the min & max values are
    calculated on a windows with size (2x bin-size).

    This is *very* similar to the MinMaxAggregator, emperical results showed no
    observable difference between both approaches.

    !!! note

        This method is implemented in Python (leveraging numpy for vecotrization), but
        is **significantly slower than the MinMaxAggregator** (which is implemented in
        the tsdownsample toolkit in Rust). <br/>
        As such, this class does not support any downsample kwargs.

    !!! note

        This downsampler supports all dtypes.

    """

    def _arg_downsample(
        self,
        x: np.ndarray | None,
        y: np.ndarray,
        n_out: int,
    ) -> np.ndarray:
        # The block size 2x the bin size we also perform the ceil-operation
        # to ensure that the block_size * n_out / 2 < len(x)
        block_size = math.ceil(y.shape[0] / (n_out + 1) * 2)
        argmax_offset = block_size // 2

        # Calculate the offset range which will be added to the argmin and argmax pos
        offset = np.arange(
            0, stop=y.shape[0] - block_size - argmax_offset, step=block_size
        )

        # Calculate the argmin & argmax on the reshaped view of `y` &
        # add the corresponding offset
        argmin = (
            y[: block_size * offset.shape[0]].reshape(-1, block_size).argmin(axis=1)
            + offset
        )
        argmax = (
            y[argmax_offset : block_size * offset.shape[0] + argmax_offset]
            .reshape(-1, block_size)
            .argmax(axis=1)
            + offset
            + argmax_offset
        )

        # Sort the argmin & argmax (where we append the first and last index item)
        return np.unique(np.concatenate((argmin, argmax, [0, y.shape[0] - 1])))


class MinMaxAggregator(DataPointSelector):
    """Aggregation method which performs binned min-max aggregation over fully
    overlapping windows.

    This is arguably the most computational efficient downsampling method, as it only
    performs (non-expensive) comparisons on the data in a single pass.

    Details on visual representativeness & stability: [https://arxiv.org/abs/2304.00900](https://arxiv.org/abs/2304.00900)

    !!! note

        This method is rather efficient when scaling to large data sizes and can be used
        as a data-reduction step before feeding it to the [`LTTB`][aggregation.aggregators.LTTB]
        algorithm, as [`MinMaxLTTB`][aggregation.aggregators.MinMaxLTTB] does with the
        [`MinMaxOverlapAggregator`][aggregation.aggregators.MinMaxOverlapAggregator].

    """

    def __init__(self, nan_policy="omit", **downsample_kwargs):
        """
        Parameters
        ----------
        **downsample_kwargs
            Keyword arguments passed to the :class:`MinMaxDownsampler`.
            - The `parallel` argument is set to False by default.
        nan_policy: str, optional
            The policy to handle NaNs. Can be 'omit' or 'keep'. By default, 'omit'.

        """
        # this downsampler supports all dtypes
        super().__init__(**downsample_kwargs)
        if nan_policy not in ("omit", "keep"):
            raise ValueError("nan_policy must be either 'omit' or 'keep'")
        if nan_policy == "omit":
            self.downsampler = MinMaxDownsampler()
        else:
            self.downsampler = NaNMinMaxDownsampler()

    def _arg_downsample(
        self,
        x: np.ndarray | None,
        y: np.ndarray,
        n_out: int,
    ) -> np.ndarray:
        return self.downsampler.downsample(
            *_to_tsdownsample_args(x, y), n_out=n_out, **self.downsample_kwargs
        )


class MinMaxLTTB(DataPointSelector):
    """Efficient version off LTTB by first reducing really large datasets with
    the [`MinMaxAggregator`][aggregation.aggregators.MinMaxAggregator] and then further aggregating the
    reduced result with [`LTTB`][aggregation.aggregators.LTTB].

    Starting from 10M data points, this method performs the MinMax-prefetching of data
    points to enhance computational efficiency.

    Inventors: Jonas & Jeroen Van Der Donckt - 2022

    Paper: [https://arxiv.org/pdf/2305.00332.pdf](https://arxiv.org/pdf/2305.00332.pdf)
    """

    def __init__(
        self, minmax_ratio: int = 4, nan_policy: str = "omit", **downsample_kwargs
    ):
        """
        Parameters
        ----------
        minmax_ratio: int, optional
            The ratio between the number of data points in the MinMax-prefetching and
            the number of data points that will be outputted by LTTB. By default, 4.
        nan_policy: str, optional
            The policy to handle NaNs. Can be 'omit' or 'keep'. By default, 'omit'.
        **downsample_kwargs
            Keyword arguments passed to the `MinMaxLTTBDownsampler`.
            - The `parallel` argument is set to False by default.
            - The `minmax_ratio` argument is set to 4 by default, which was empirically
              proven to be a good default.

        """
        if nan_policy not in ("omit", "keep"):
            raise ValueError("nan_policy must be either 'omit' or 'keep'")
        if nan_policy == "omit":
            self.minmaxlttb = MinMaxLTTBDownsampler()
        else:
            self.minmaxlttb = NaNMinMaxLTTBDownsampler()

        self.minmax_ratio = minmax_ratio

        super().__init__(
            y_dtype_regex_list=[rf"{dtype}\d*" for dtype in ("float", "int", "uint")]
            + ["category", "bool"],
            **downsample_kwargs,
        )

    def _arg_downsample(
        self,
        x: np.ndarray | None,
        y: np.ndarray,
        n_out: int,
    ) -> np.ndarray:
        return self.minmaxlttb.downsample(
            *_to_tsdownsample_args(x, y),
            n_out=n_out,
            minmax_ratio=self.minmax_ratio,
            **self.downsample_kwargs,
        )


class EveryNthPoint(DataPointSelector):
    """Naive (but fast) aggregator method which returns every N'th point.

    !!! note
        This downsampler supports all dtypes.
    """

    def _arg_downsample(
        self,
        x: np.ndarray | None,
        y: np.ndarray,
        n_out: int,
    ) -> np.ndarray:
        return EveryNthDownsampler().downsample(y, n_out=n_out)


class FuncAggregator(DataAggregator):
    """Aggregator instance which uses the passed aggregation func.

    !!! warning

        The user has total control which `aggregation_func` is passed to this method,
        hence the user should be careful to not make copies of the data, nor write to
        the data. Furthermore, the user should beware of performance issues when
        using more complex aggregation functions.

    !!! warning "Attention"

        The user has total control which `aggregation_func` is passed to this method,
        hence it is the users' responsibility to handle categorical and bool-based
        data types.

    """

    def __init__(
        self,
        aggregation_func,
        x_dtype_regex_list=None,
        y_dtype_regex_list=None,
        **downsample_kwargs,
    ):
        """
        Parameters
        ----------
        aggregation_func: Callable
            The aggregation function which will be applied on each pin.

        """
        self.aggregation_func = aggregation_func
        super().__init__(x_dtype_regex_list, y_dtype_regex_list, **downsample_kwargs)

    def _aggregate(
        self,
        x: np.ndarray | None,
        y: np.ndarray,
        n_out: int,
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Aggregate the data using the object's aggregation function.

        Parameters
        ----------
        x: np.ndarray | None
            The x-values of the data. Can be None if no x-values are available.
        y: np.ndarray
            The y-values of the data.
        n_out: int
            The number of output data points.
        **kwargs
            Additional keyword arguments, which are passed to the aggregation function.

        Returns
        -------
        Tuple[np.ndarray, np.ndarray]
            The aggregated x & y values.
            If `x` is None, then the indices of the first element of each bin is
            returned as x-values.

        """
        # Create an index-estimation for real-time data
        # Add one to the index so it's pointed at the end of the window
        # Note: this can be adjusted to .5 to center the data
        # Multiply it with the group size to get the real index-position
        # TODO: add option to select start / middle / end as index
        if x is None:
            # equidistant index
            idxs = np.linspace(0, len(y), n_out + 1).astype(int)
        else:
            xdt = x.dtype
            if np.issubdtype(xdt, np.datetime64) or np.issubdtype(xdt, np.timedelta64):
                x = x.view("int64")
            # Thanks to `linspace`, the data is evenly distributed over the index-range
            # The searchsorted function returns the index positions
            idxs = np.searchsorted(x, np.linspace(x[0], x[-1], n_out + 1))

        y_agg = np.array(
            [
                self.aggregation_func(y[t0:t1], **self.downsample_kwargs)
                for t0, t1 in zip(idxs[:-1], idxs[1:])
            ]
        )

        if x is not None:
            x_agg = x[idxs[:-1]]
        else:
            # x is None -> return the indices of the first element of each bin
            x_agg = idxs[:-1]

        return x_agg, y_agg



================================================
FILE: plotly_resampler/aggregation/gap_handler_interface.py
================================================
"""AbstractGapHandler interface-class, subclassed by concrete gap handlers."""

from __future__ import annotations

__author__ = "Jeroen Van Der Donckt"

from abc import ABC, abstractmethod
from typing import Optional, Tuple

import numpy as np


class AbstractGapHandler(ABC):
    def __init__(self, fill_value: Optional[float] = None):
        """Constructor of AbstractGapHandler.

        Parameters
        ----------
        fill_value: float, optional
            The value to fill the gaps with, by default None.
            Note that setting this value to 0 for filled area plots is particularly
            useful.

        """
        self.fill_value = fill_value

    @abstractmethod
    def _get_gap_mask(self, x_agg: np.ndarray) -> Optional[np.ndarray]:
        """Get a boolean mask indicating the indices where there are gaps.

        If you require custom gap handling, you can implement this method to return a
        boolean mask indicating the indices where there are gaps.

        Parameters
        ----------
        x_agg: np.ndarray
            The x array. This is used to determine the gaps.

        Returns
        -------
        Optional[np.ndarray]
            A boolean mask indicating the indices where there are gaps. If there are no
            gaps, None is returned.

        """
        pass

    def insert_fill_value_between_gaps(
        self,
        x_agg: np.ndarray,
        y_agg: np.ndarray,
        idxs: np.ndarray,
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Insert the fill_value in the y_agg array where there are gaps.

        Gaps are determined by the x_agg array. The `_get_gap_mask` method is used to
        determine a boolean mask indicating the indices where there are gaps.

        Parameters
        ----------
        x_agg: np.ndarray
            The x array. This is used to determine the gaps.
        y_agg: np.ndarray
            The y array. A copy of this array will be expanded with fill_values where
            there are gaps.
        idxs: np.ndarray
            The index array. This is relevant aggregators that perform data point
            selection (e.g., max, min, etc.) - this array will be expanded with the
            same indices where there are gaps.

        Returns
        -------
        Tuple[np.ndarray, np.ndarray]
            The expanded y_agg array and the expanded idxs array respectively.

        """
        gap_mask = self._get_gap_mask(x_agg)
        if gap_mask is None:
            # no gaps are found, nothing to do
            return y_agg, idxs

        # An array filled with 1s and 2s, where 2 indicates a large gap mask
        # (i.e., that index will be repeated twice)
        repeats = np.ones(x_agg.shape, dtype="int") + gap_mask

        # use the repeats to expand the idxs, and agg_y array
        idx_exp_nan = np.repeat(idxs, repeats)
        y_agg_exp_nan = np.repeat(y_agg, repeats)

        # only float arrays can contain NaN values
        if issubclass(y_agg_exp_nan.dtype.type, np.integer) or issubclass(
            y_agg_exp_nan.dtype.type, np.bool_
        ):
            y_agg_exp_nan = y_agg_exp_nan.astype("float")

        # Set the NaN values
        # We add the gap index offset (via the np.arange) to the indices to account for
        # the repeats (i.e., expanded y_agg array).
        y_agg_exp_nan[np.where(gap_mask)[0] + np.arange(gap_mask.sum())] = (
            self.fill_value
        )

        return y_agg_exp_nan, idx_exp_nan



================================================
FILE: plotly_resampler/aggregation/gap_handlers.py
================================================
# -*- coding: utf-8 -*-
"""Compatible implementation for various gap handling methods."""

from __future__ import annotations

__author__ = "Jeroen Van Der Donckt"

from typing import Optional, Tuple

import numpy as np

from plotly_resampler.aggregation.gap_handler_interface import AbstractGapHandler


class NoGapHandler(AbstractGapHandler):
    """No gap handling."""

    def _get_gap_mask(self, x_agg: np.ndarray) -> Optional[np.ndarray]:
        return


class MedDiffGapHandler(AbstractGapHandler):
    """Gap handling based on the median diff of the x_agg array."""

    def _calc_med_diff(self, x_agg: np.ndarray) -> Tuple[float, np.ndarray]:
        """Calculate the median diff of the x_agg array.

        As median is more robust to outliers than the mean, the median is used to define
        the gap threshold.

        This method performs a divide and conquer heuristic to calculate the median;
        1. divide the array into `n_blocks` blocks (with `n_blocks` = 128)
        2. calculate the mean of each block
        3. calculate the median of the means
        => This proves to be a good approximation of the median of the full array, while
              being much faster than calculating the median of the full array.
        """
        # remark: thanks to the prepend -> x_diff.shape === len(s)
        x_diff = np.diff(x_agg, prepend=x_agg[0])

        # To do so - use an approach where we reshape the data
        # into `n_blocks` blocks and calculate the mean and then the median on that
        # Why use `median` instead of a global mean?
        #   => when you have large gaps, they will be represented by a large diff
        #      which will skew the mean way more than the median!
        n_blocks = 128
        if x_agg.shape[0] > 5 * n_blocks:
            blck_size = x_diff.shape[0] // n_blocks

            # convert the index series index diff into a reshaped view (i.e., sid_v)
            sid_v: np.ndarray = x_diff[: blck_size * n_blocks].reshape(n_blocks, -1)

            # calculate the mean fore each block and then the median of those means
            med_diff = np.median(np.mean(sid_v, axis=1))
        else:
            med_diff = np.median(x_diff)

        return med_diff, x_diff

    def _get_gap_mask(self, x_agg: np.ndarray) -> Optional[np.ndarray]:
        """Get a boolean mask indicating the indices where there are gaps.

        If you require custom gap handling, you can implement this method to return a
        boolean mask indicating the indices where there are gaps.

        Parameters
        ----------
        x_agg: np.ndarray
            The x array. This is used to determine the gaps.

        Returns
        -------
        Optional[np.ndarray]
            A boolean mask indicating the indices where there are gaps. If there are no
            gaps, None is returned.

        """
        med_diff, x_diff = self._calc_med_diff(x_agg)

        # TODO: this 4 was revealed to me in a dream, but it seems to work well
        # After some consideration, we altered this to a 4.1
        gap_mask = x_diff > 4.1 * med_diff
        if not any(gap_mask):
            return
        return gap_mask



================================================
FILE: plotly_resampler/aggregation/plotly_aggregator_parser.py
================================================
from __future__ import annotations

import bisect
from typing import Tuple, Union

import numpy as np
import pandas as pd
import pytz

from .aggregation_interface import DataAggregator, DataPointSelector
from .gap_handler_interface import AbstractGapHandler
from .gap_handlers import NoGapHandler


class PlotlyAggregatorParser:
    @staticmethod
    def parse_hf_data(
        hf_data: np.ndarray | pd.Categorical | pd.Series | pd.Index,
    ) -> np.ndarray | pd.Categorical:
        """Parse the high-frequency data to a numpy array."""
        # Categorical data (pandas)
        #   - pd.Series with categorical dtype -> calling .values will returns a
        #       pd.Categorical
        #   - pd.CategoricalIndex -> calling .values returns a pd.Categorical
        #   - pd.Categorical: has no .values attribute -> will not be parsed
        if isinstance(hf_data, pd.RangeIndex):
            return None
        if isinstance(hf_data, (pd.Series, pd.Index)):
            return hf_data.values
        return hf_data

    @staticmethod
    def to_same_tz(
        ts: Union[pd.Timestamp, None], reference_tz: Union[pytz.BaseTzInfo, None]
    ) -> Union[pd.Timestamp, None]:
        """Adjust `ts` its timezone to the `reference_tz`."""
        if ts is None:
            return None
        elif reference_tz is not None:
            if ts.tz is not None:
                # compare if these two have the same timezone / offset
                try:
                    assert ts.tz.__str__() == reference_tz.__str__()
                except AssertionError:
                    assert ts.utcoffset() == reference_tz.utcoffset(ts.tz_convert(None))
                return ts
            else:  # localize -> time remains the same
                return ts.tz_localize(reference_tz)
        elif reference_tz is None and ts.tz is not None:
            return ts.tz_localize(None)
        return ts

    @staticmethod
    def get_start_end_indices(hf_trace_data, axis_type, start, end) -> Tuple[int, int]:
        """Get the start & end indices of the high-frequency data."""
        # Base case: no hf data, or both start & end are None
        if not len(hf_trace_data["x"]):
            return 0, 0
        elif start is None and end is None:
            return 0, len(hf_trace_data["x"])

        # NOTE: as we use bisect right for the end index, we do not need to add a
        #      small epsilon to the end value
        start = hf_trace_data["x"][0] if start is None else start
        end = hf_trace_data["x"][-1] if end is None else end

        # NOTE: we must verify this before check if the x is a range-index
        if axis_type == "log":
            start, end = 10**start, 10**end

        # We can compute the start & end indices directly when it is a RangeIndex
        if isinstance(hf_trace_data["x"], pd.RangeIndex):
            x_start = hf_trace_data["x"].start
            x_step = hf_trace_data["x"].step
            start_idx = int(max((start - x_start) // x_step, 0))
            end_idx = int((end - x_start) // x_step)
            return start_idx, end_idx
        # TODO: this can be performed as-well for a fixed frequency range-index w/ freq

        if axis_type == "date":
            start, end = pd.to_datetime(start), pd.to_datetime(end)
            # convert start & end to the same timezone
            if isinstance(hf_trace_data["x"], pd.DatetimeIndex):
                tz = hf_trace_data["x"].tz
                try:
                    assert start.tz.__str__() == end.tz.__str__()
                except (TypeError, AssertionError):
                    # This fix is needed for DST (when the timezone is not fixed)
                    assert start.tz_localize(None) == start.tz_convert(tz).tz_localize(
                        None
                    )
                    assert end.tz_localize(None) == end.tz_convert(tz).tz_localize(None)

                start = PlotlyAggregatorParser.to_same_tz(start, tz)
                end = PlotlyAggregatorParser.to_same_tz(end, tz)

        # Search the index-positions
        start_idx = bisect.bisect_left(hf_trace_data["x"], start)
        end_idx = bisect.bisect_right(hf_trace_data["x"], end)
        return start_idx, end_idx

    @staticmethod
    def _handle_gaps(
        hf_trace_data: dict,
        hf_x: np.ndarray,
        agg_x: np.ndarray,
        agg_y: np.ndarray,
        indices: np.ndarray,
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Handle the gaps in the aggregated data.

        Returns:
            - agg_x: the aggregated x-values
            - agg_y: the aggregated y-values
            - indices: the indices of the hf_data data that were aggregated

        """
        gap_handler: AbstractGapHandler = hf_trace_data["gap_handler"]
        downsampler = hf_trace_data["downsampler"]

        # TODO check for trace mode (markers, lines, etc.) and only perform the
        # gap insertion methodology when the mode is lines.
        # if trace.get("connectgaps") != True and
        if (
            isinstance(gap_handler, NoGapHandler)
            # rangeIndex | datetimeIndex with freq -> equally spaced x; so no gaps
            or isinstance(hf_trace_data["x"], pd.RangeIndex)
            or (
                isinstance(hf_trace_data["x"], pd.DatetimeIndex)
                and hf_trace_data["x"].freq is not None
            )
        ):
            return agg_x, agg_y, indices

        # Interleave the gaps
        # View the data as an int64 when we have a DatetimeIndex
        # We only want to detect gaps, so we only want to compare values.
        agg_x_parsed = PlotlyAggregatorParser.parse_hf_data(agg_x)
        xdt = agg_x_parsed.dtype
        if np.issubdtype(xdt, np.timedelta64) or np.issubdtype(xdt, np.datetime64):
            agg_x_parsed = agg_x_parsed.view("int64")

        agg_y, indices = gap_handler.insert_fill_value_between_gaps(
            agg_x_parsed, agg_y, indices
        )
        if isinstance(downsampler, DataPointSelector):
            agg_x = hf_x[indices]
        elif isinstance(downsampler, DataAggregator):
            # The indices are in this case a repeat
            agg_x = agg_x[indices]

        return agg_x, agg_y, indices

    @staticmethod
    def aggregate(
        hf_trace_data: dict,
        start_idx: int,
        end_idx: int,
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Aggregate the data in `hf_trace_data` between `start_idx` and `end_idx`.

        Returns:
            - x: the aggregated x-values
            - y: the aggregated y-values
            - indices: the indices of the hf_data data that were aggregated

            These indices are useful to select the corresponding hf_data from
            non `x` and `y` data (e.g. `text`, `marker_size`, `marker_color`).

        """
        hf_x = hf_trace_data["x"][start_idx:end_idx]
        hf_y = hf_trace_data["y"][start_idx:end_idx]

        # No downsampling needed ; we show the raw data as is, but with gap-detection
        if (end_idx - start_idx) <= hf_trace_data["max_n_samples"]:
            indices = np.arange(len(hf_y))  # no downsampling - all values are selected
            if len(indices):
                return PlotlyAggregatorParser._handle_gaps(
                    hf_trace_data, hf_x=hf_x, agg_x=hf_x, agg_y=hf_y, indices=indices
                )
            else:
                return hf_x, hf_y, indices

        downsampler = hf_trace_data["downsampler"]

        hf_x_parsed = PlotlyAggregatorParser.parse_hf_data(hf_x)
        hf_y_parsed = PlotlyAggregatorParser.parse_hf_data(hf_y)

        if isinstance(downsampler, DataPointSelector):
            s_v = hf_y_parsed
            if isinstance(s_v, pd.Categorical):  # pd.Categorical (has no .values)
                s_v = s_v.codes
            indices = downsampler.arg_downsample(
                hf_x_parsed,
                s_v,
                n_out=hf_trace_data["max_n_samples"],
                **hf_trace_data.get("downsampler_kwargs", {}),
            )
            if isinstance(hf_trace_data["x"], pd.RangeIndex):
                # we avoid slicing the default pd.RangeIndex (as this is not an
                # in-memory array) - this proves to be faster than slicing the index.
                agg_x = (
                    start_idx
                    + hf_trace_data["x"].start
                    + indices.astype(hf_trace_data["x"].dtype) * hf_trace_data["x"].step
                )
            else:
                agg_x = hf_x[indices]
            agg_y = hf_y[indices]
        elif isinstance(downsampler, DataAggregator):
            agg_x, agg_y = downsampler.aggregate(
                hf_x_parsed,
                hf_y_parsed,
                n_out=hf_trace_data["max_n_samples"],
                **hf_trace_data.get("downsampler_kwargs", {}),
            )
            if isinstance(hf_trace_data["x"], pd.RangeIndex):
                # we avoid slicing the default pd.RangeIndex (as this is not an
                # in-memory array) - this proves to be faster than slicing the index.
                agg_x = (
                    start_idx
                    + hf_trace_data["x"].start
                    + agg_x * hf_trace_data["x"].step
                )
            # The indices are just the range of the aggregated data
            indices = np.arange(len(agg_x))
        else:
            raise ValueError(
                "Invalid downsampler instance, must be either a "
                + f"DataAggregator or a DataPointSelector, got {type(downsampler)}"
            )

        return PlotlyAggregatorParser._handle_gaps(
            hf_trace_data, hf_x=hf_x, agg_x=agg_x, agg_y=agg_y, indices=indices
        )



================================================
FILE: plotly_resampler/figure_resampler/__init__.py
================================================
# -*- coding: utf-8 -*-
"""
Module withholding wrappers for the plotly ``go.Figure`` and ``go.FigureWidget`` class 
which allows bookkeeping and back-end based resampling of high-frequency sequential
data.

!!! tip

    The term `high-frequency` actually refers very large amounts of sequential data.

"""

from .figure_resampler import ASSETS_FOLDER, FigureResampler
from .figurewidget_resampler import FigureWidgetResampler

__all__ = [
    "FigureResampler",
    "ASSETS_FOLDER",
    "FigureWidgetResampler",
]



================================================
FILE: plotly_resampler/figure_resampler/figure_resampler.py
================================================
# -*- coding: utf-8 -*-
"""
``FigureResampler`` wrapper around the plotly ``go.Figure`` class.

Creates a web-application and uses ``dash`` callbacks to enable dynamic resampling.

"""

from __future__ import annotations

__author__ = "Jonas Van Der Donckt, Jeroen Van Der Donckt, Emiel Deprost"

import os
import warnings
from pathlib import Path
from typing import List, Optional, Tuple, Union

import dash
import plotly.graph_objects as go
from plotly.basedatatypes import BaseFigure

from ..aggregation import (
    AbstractAggregator,
    AbstractGapHandler,
    MedDiffGapHandler,
    MinMaxLTTB,
)
from .figure_resampler_interface import AbstractFigureAggregator
from .utils import is_figure, is_fr

# Default arguments for the Figure overview
ASSETS_FOLDER = Path(__file__).parent.joinpath("assets").absolute().__str__()
_DEFAULT_OVERVIEW_LAYOUT_KWARGS = {
    "showlegend": False,
    "height": 120,
    "activeselection": dict(fillcolor="#96C291", opacity=0.3),
    "margin": {"t": 0, "b": 0},
}


class FigureResampler(AbstractFigureAggregator, go.Figure):
    """Data aggregation functionality for ``go.Figures``."""

    def __init__(
        self,
        figure: BaseFigure | dict = None,
        convert_existing_traces: bool = True,
        default_n_shown_samples: int = 1000,
        default_downsampler: AbstractAggregator = MinMaxLTTB(),
        default_gap_handler: AbstractGapHandler = MedDiffGapHandler(),
        resampled_trace_prefix_suffix: Tuple[str, str] = (
            '<b style="color:sandybrown">[R]</b> ',
            "",
        ),
        show_mean_aggregation_size: bool = True,
        convert_traces_kwargs: dict | None = None,
        create_overview: bool = False,
        overview_row_idxs: list = None,
        overview_kwargs: dict = {},
        verbose: bool = False,
        show_dash_kwargs: dict | None = None,
    ):
        """Initialize a dynamic aggregation data mirror using a dash web app.

        Parameters
        ----------
        figure: BaseFigure
            The figure that will be decorated. Can be either an empty figure
            (e.g., ``go.Figure()``, ``make_subplots()``, ``go.FigureWidget``) or an
            existing figure.
        convert_existing_traces: bool
            A bool indicating whether the high-frequency traces of the passed ``figure``
            should be resampled, by default True. Hence, when set to False, the
            high-frequency traces of the passed ``figure`` will not be resampled.
        default_n_shown_samples: int, optional
            The default number of samples that will be shown for each trace,
            by default 1000.\n
            !!! note
                - This can be overridden within the [`add_trace`][figure_resampler.figure_resampler_interface.AbstractFigureAggregator.add_trace] method.
                - If a trace withholds fewer datapoints than this parameter,
                  the data will *not* be aggregated.
        default_downsampler: AbstractAggregator, optional
            An instance which implements the AbstractAggregator interface and
            will be used as default downsampler, by default ``MinMaxLTTB`` with
            ``MinMaxLTTB`` is a heuristic to the LTTB algorithm that uses pre-selection
            of min-max values (default 4 per bin) to speed up LTTB (as now only 4 values
            per bin are considered by LTTB). This min-max ratio of 4 can be changed by
            initializing ``MinMaxLTTB`` with a different value for the ``minmax_ratio``
            parameter. \n
            !!! note
                This can be overridden within the [`add_trace`][figure_resampler.figure_resampler_interface.AbstractFigureAggregator.add_trace] method.
        default_gap_handler: AbstractGapHandler, optional
            An instance which implements the AbstractGapHandler interface and
            will be used as default gap handler, by default ``MedDiffGapHandler``.
            ``MedDiffGapHandler`` will determine gaps by first calculating the median
            aggregated x difference and then thresholding the aggregated x delta on a
            multiple of this median difference.  \n
            !!! note
                This can be overridden within the [`add_trace`][figure_resampler.figure_resampler_interface.AbstractFigureAggregator.add_trace] method.
        resampled_trace_prefix_suffix: str, optional
            A tuple which contains the ``prefix`` and ``suffix``, respectively, which
            will be added to the trace its legend-name when a resampled version of the
            trace is shown. By default a bold, orange ``[R]`` is shown as prefix
            (no suffix is shown).
        show_mean_aggregation_size: bool, optional
            Whether the mean aggregation bin size will be added as a suffix to the trace
            its legend-name, by default True.
        convert_traces_kwargs: dict, optional
            A dict of kwargs that will be passed to the [`add_trace`][figure_resampler.figure_resampler_interface.AbstractFigureAggregator.add_trace] method and
            will be used to convert the existing traces. \n
            !!! note
                This argument is only used when the passed ``figure`` contains data and
                ``convert_existing_traces`` is set to True.
        create_overview: bool, optional
            Whether an overview will be added to the figure (also known as rangeslider),
            by default False. An overview is a bidirectionally linked figure that is
            placed below the FigureResampler figure and shows a coarse version on which
            the current view of the FigureResampler figure is highlighted. The overview
            can be used to quickly navigate through the data by dragging the selection
            box.
            !!! note
                - In the case of subplots, the overview will be created for each subplot
                  column. Only a single subplot row can be captured in the overview,
                  this is by default the first row. If you want to customize this
                  behavior, you can use the `overview_row_idxs` argument.
                - This functionality is not yet extensively validated. Please report any
                  issues you encounter on GitHub.
        overview_row_idxs: list, optional
            A list of integers corresponding to the row indices (START AT 0) of the
            subplots columns that should be linked with the column its corresponding
            overview. By default None, which will result in the first row being utilized
            for each column.
        overview_kwargs: dict, optional
            A dict of kwargs that will be passed to the `update_layout` method of the
            overview figure, by default {}, which will result in utilizing the
            [`default`][_DEFAULT_OVERVIEW_LAYOUT_KWARGS] overview layout kwargs.
        verbose: bool, optional
            Whether some verbose messages will be printed or not, by default False.
        show_dash_kwargs: dict, optional
            A dict that will be used as default kwargs for the [`show_dash`][figure_resampler.figure_resampler.FigureResampler.show_dash] method.
            !!! note
                The passed kwargs to the [`show_dash`][figure_resampler.figure_resampler.FigureResampler.show_dash] method will take precedence over these defaults.

        """
        # Parse the figure input before calling `super`
        if is_figure(figure) and not is_fr(figure):
            # A go.Figure
            # => base case: the figure does not need to be adjusted
            f = figure
        else:
            # Create a new figure object and make sure that the trace uid will not get
            # adjusted when they are added.
            f = self._get_figure_class(go.Figure)()
            f._data_validator.set_uid = False

            if isinstance(figure, BaseFigure):
                # A base figure object, can be;
                # - a go.FigureWidget
                # - a plotly-resampler figure: subclass of AbstractFigureAggregator
                # => we first copy the layout, grid_str and grid ref
                f.layout = figure.layout
                f._grid_str = figure._grid_str
                f._grid_ref = figure._grid_ref
                f.add_traces(figure.data)
            elif isinstance(figure, dict) and (
                "data" in figure or "layout" in figure  # or "frames" in figure  # TODO
            ):
                # A figure as a dict, can be;
                # - a plotly figure as a dict (after calling `fig.to_dict()`)
                # - a pickled (plotly-resampler) figure (after loading a pickled figure)
                # => we first copy the layout, grid_str and grid ref
                f.layout = figure.get("layout")
                f._grid_str = figure.get("_grid_str")
                f._grid_ref = figure.get("_grid_ref")
                f.add_traces(figure.get("data"))
                # `pr_props` is not None when loading a pickled plotly-resampler figure
                f._pr_props = figure.get("pr_props")
                # `f._pr_props`` is an attribute to store properties of a
                # plotly-resampler figure. This attribute is only used to pass
                # information to the super() constructor. Once the super constructor is
                # called, the attribute is removed.

                # f.add_frames(figure.get("frames")) TODO
            elif isinstance(figure, (dict, list)):
                # A single trace dict or a list of traces
                f.add_traces(figure)

        self._show_dash_kwargs = (
            show_dash_kwargs if show_dash_kwargs is not None else {}
        )

        super().__init__(
            f,
            convert_existing_traces,
            default_n_shown_samples,
            default_downsampler,
            default_gap_handler,
            resampled_trace_prefix_suffix,
            show_mean_aggregation_size,
            convert_traces_kwargs,
            verbose,
        )

        if isinstance(figure, AbstractFigureAggregator):
            # Copy the `_hf_data` if the previous figure was an AbstractFigureAggregator
            # and adjust the default `max_n_samples` and `downsampler`
            self._hf_data.update(
                self._copy_hf_data(figure._hf_data, adjust_default_values=True)
            )

            # Note: This hack ensures that the this figure object initially uses
            # data of the whole view. More concretely; we create a dict
            # serialization figure and adjust the hf-traces to the whole view
            # with the check-update method (by passing no range / filter args)
            with self.batch_update():
                graph_dict: dict = self._get_current_graph()
                update_indices = self._check_update_figure_dict(graph_dict)
                for idx in update_indices:
                    self.data[idx].update(graph_dict["data"][idx])

        self._create_overview = create_overview
        # update the overview layout
        overview_layout_kwargs = _DEFAULT_OVERVIEW_LAYOUT_KWARGS.copy()
        overview_layout_kwargs.update(overview_kwargs)
        self._overview_layout_kwargs = overview_layout_kwargs

        # array representing the row indices per column (START AT 0) of the subplot
        # that should be linked with the columns corresponding overview.
        # By default, the first row (i.e. index 0) will be utilized for each column
        self._overview_row_idxs = self._parse_subplot_row_indices(overview_row_idxs)

        # The FigureResampler needs a dash app
        self._app: dash.Dash | None = None
        self._port: int | None = None
        self._host: str | None = None
        # Certain functions will be different when using persistent inline
        # (namely `show_dash` and `stop_callback`)

    def _get_subplot_rows_and_cols_from_grid(self) -> Tuple[int, int]:
        """Get the number of rows and columns of the figure's grid.

        Returns
        -------
        Tuple[int, int]
            The number of rows and columns of the figure's grid, respectively.
        """
        if self._grid_ref is None:  # case: go.Figure (no subplots)
            return (1, 1)
        # TODO: not 100% sure whether this is correct
        return (len(self._grid_ref), len(self._grid_ref[0]))

    def _parse_subplot_row_indices(self, row_indices: list = None) -> List[int]:
        """Verify whether the passed row indices are valid.

        Parameters
        ----------
        row_indices: list, optional
            A list of integers representing the row indices for which the overview
            should be created. The length of the list should be equal to the number of
            columns of the figure. Each element of the list should be smaller than the
            number of rows of the figure (thus note that the row indices start at 0). By
            default None, which will result in the first row being utilized for each
            column.
            !!! note
                When you do not want to use an overview of a certain column (because
                a certain subplot spans more than 1 column), you can specify this by
                setting that respecive row_index value to `None`.

                For instance, the sbuplot on row 2, col 1 spans two coloms. So when you
                intend to utilize that subplot within the overview, you want to specify
                the row_indices as: `[1, None, ...]`

        Returns
        -------
        List[int]
            A list of integers representing the row indices per subplot column.

        """
        n_rows, n_cols = self._get_subplot_rows_and_cols_from_grid()

        # By default, the first row is utilized to set the row indices
        if row_indices is None:
            return [0] * n_cols

        # perform some checks on the row indices
        assert isinstance(row_indices, list), "row indices must be a list"
        assert (
            len(row_indices) == n_cols
        ), "the number of row indices must be equal to the number of columns"
        assert all(
            [(li is None) or (0 <= li < n_rows) for li in row_indices]
        ), "row indices must be smaller than the number of rows"

        return row_indices

    # determines which subplot data to take from main and put into coarse
    def _remove_other_axes_for_coarse(self) -> go.Figure:
        # base case: no rows and cols to filter
        if self._grid_ref is None:  # case: go.Figure (no subplots)
            return self

        # Create the grid specification for the overview figure (in `reduced_grid_ref`)
        # The trace_list and the 2 axis lists are 1D arrays holding track of the traces
        # and axes to track.
        reduced_grid_ref = [[]]

        # Store the xaxis keys (e.g., x2) of the traces to keep
        trace_list = []
        # Store the xaxis and yaxis layout keys of the traces to keep (e.g., xaxis2)
        layout_xaxis_list, layout_yaxis_list = [], []
        for col_idx, row_idx in enumerate(self._overview_row_idxs):
            if row_idx is None:  # skip None value
                continue

            overview_grid_ref = self._grid_ref[row_idx][col_idx]
            reduced_grid_ref[0].append(overview_grid_ref)  # [0] bc 1 row in overview
            for subplot in overview_grid_ref:
                trace_list.append(subplot.trace_kwargs["xaxis"])

                # store the layout keys so that we can retain the exact layout
                xaxis_key, yaxis_key = subplot.layout_keys
                layout_yaxis_list.append(yaxis_key)
                layout_xaxis_list.append(xaxis_key)
        # print("layout_list", l_xaxis_list, l_yaxis_list)
        # print("trace_list", trace_list)

        fig_dict = self._get_current_graph()  # a copy of the current graph

        # copy the data from the relevant overview subplots
        reduced_fig_dict = {
            "data": [],
            "layout": {"template": fig_dict["layout"]["template"]},
        }
        # NOTE: we enumerate over the data of the full figure so that we can utilize the
        # trace index to mimic the colorway.
        for i, trace in enumerate(fig_dict["data"]):
            # NOTE: the interplay between line_color and marker_color seems to work in
            # this implementation - a more thorough investigation might be needed
            if trace.get("xaxis", "x") in trace_list:
                if "line" not in trace:
                    trace["line"] = {}
                # Ensure that the same color is utilized
                trace["line"]["color"] = (
                    self._layout_obj.template.layout.colorway[i]
                    if self.data[i].line.color is None
                    else self.data[i].line.color
                )
                # add the trace to the reduced figure
                reduced_fig_dict["data"].append(trace)

        # Add the relevant layout keys to the reduced figure
        for k, v in fig_dict["layout"].items():
            if k in layout_xaxis_list:
                reduced_fig_dict["layout"][k] = v
            elif k in layout_yaxis_list:
                v = v.copy()
                # set the domain to [0, 1] to ensure that the overview figure has the
                # global y-axis range
                v.update({"domain": [0, 1]})
                reduced_fig_dict["layout"][k] = v

        # Create a figure object using the reduced figure dict
        reduced_fig = go.Figure(layout=reduced_fig_dict["layout"])
        reduced_fig._grid_ref = reduced_grid_ref
        # Ensure that the trace uid is not adjusted, this must be set prior to adding
        # the trace data. Otherwise, data aggregation will not work.
        reduced_fig._data_validator.set_uid = False
        reduced_fig.add_traces(reduced_fig_dict["data"])
        return reduced_fig

    def _create_overview_figure(self) -> go.Figure:
        # create a new coarse fig
        reduced_fig = self._remove_other_axes_for_coarse()

        # Resample the coarse figure using 3x the default aggregation size to ensure
        # that it contains sufficient details
        coarse_fig_hf = FigureResampler(
            reduced_fig,
            default_n_shown_samples=3 * self._global_n_shown_samples,
        )

        # NOTE: this way we can alter props without altering the original hf data
        # NOTE: this also copies the default aggregation functionality to the coarse figure
        coarse_fig_hf._hf_data = {uid: trc.copy() for uid, trc in self._hf_data.items()}
        for trace in coarse_fig_hf.hf_data:
            trace["max_n_samples"] *= 3

        coarse_fig_dict = coarse_fig_hf._get_current_graph()
        # add the 3x max_n_samples coarse figure data to the coarse_fig_dict
        coarse_fig_hf._check_update_figure_dict(coarse_fig_dict)
        del coarse_fig_hf

        coarse_fig = go.Figure(layout=coarse_fig_dict["layout"])
        coarse_fig._grid_ref = reduced_fig._grid_ref
        coarse_fig._data_validator.set_uid = False
        coarse_fig.add_traces(coarse_fig_dict["data"])
        # remove any update menus for the coarse figure
        coarse_fig.layout.pop("updatemenus", None)
        # remove the `rangeselector` options for all 'axis' keys in the layout of the
        # coarse figure
        for k, v in coarse_fig.layout._props.items():
            if "axis" in k:
                v.pop("rangeselector", None)

        # height of the overview scales with the height of the dynamic view
        coarse_fig.update_layout(
            **self._overview_layout_kwargs,
            hovermode=False,
            clickmode="event+select",
            dragmode="select",
        )
        # Hide the grid
        hide_kwrgs = dict(
            showgrid=False,
            showticklabels=False,
            zeroline=False,
            title_text=None,
            mirror=True,
            ticks="",
            showline=False,
            linecolor="black",
        )
        coarse_fig.update_yaxes(**hide_kwrgs)
        coarse_fig.update_xaxes(**hide_kwrgs)

        vrect_props = dict(
            **dict(line_width=0, x0=0, x1=1),
            **dict(fillcolor="lightblue", opacity=0.25, layer="above"),
        )

        if self._grid_ref is None:  # case: go.Figure (no subplots)
            # set the fixed range to True
            coarse_fig["layout"]["xaxis"]["fixedrange"] = True
            coarse_fig["layout"]["yaxis"]["fixedrange"] = True

            # add a shading to the overview
            coarse_fig.add_vrect(xref="x domain", **vrect_props)
            return coarse_fig

        col_idx_overview = 0
        for col_idx, row_idx in enumerate(self._overview_row_idxs):
            if row_idx is None:  # skip the None value
                continue

            # we will only use the first grid-ref (as we will otherwise have multiple
            # overlapping selection boxes)
            for subplot in self._grid_ref[row_idx][col_idx][:1]:
                xaxis_key, yaxis_key = subplot.layout_keys

                # set the fixed range to True
                coarse_fig["layout"][xaxis_key]["fixedrange"] = True
                coarse_fig["layout"][yaxis_key]["fixedrange"] = True

                # add a shading to the overview
                coarse_fig.add_vrect(
                    col=col_idx_overview + 1,
                    xref=f"{subplot.trace_kwargs['xaxis']} domain",
                    **vrect_props,
                )

            col_idx_overview += 1  # only increase the index when not None

        return coarse_fig

    def show_dash(
        self,
        mode=None,
        config: dict | None = None,
        init_dash_kwargs: dict | None = None,
        graph_properties: dict | None = None,
        **kwargs,
    ):
        """Registers the `update_graph` callback & show the figure in a dash app.

        Parameters
        ----------
        mode: str, optional
            Display mode. One of:\n
              * ``"external"``: The URL of the app will be displayed in the notebook
                output cell. Clicking this URL will open the app in the default
                web browser.
              * ``"inline"``: The app will be displayed inline in the notebook output
                cell in an iframe.
              * ``"inline_persistent"``: The app will be displayed inline in the
                notebook output cell in an iframe, if the app is not reachable a static
                image of the figure is shown. Hence this is a persistent version of the
                ``"inline"`` mode, allowing users to see a static figure in other
                environments, browsers, etc.

                !!! note

                    This mode requires the ``kaleido`` and ``flask_cors`` package.
                    Install them : ``pip install plotly_resampler[inline_persistent]``
                    or ``pip install kaleido flask_cors``.

              * ``"jupyterlab"``: The app will be displayed in a dedicated tab in the
                JupyterLab interface. Requires JupyterLab and the ``jupyterlab-dash``
                extension.
            By default None, which will result in the same behavior as ``"external"``.
        config: dict, optional
            The configuration options for displaying this figure, by default None.
            This ``config`` parameter is the same as the dict that you would pass as
            ``config`` argument to the `show` method.
            See more [https://plotly.com/python/configuration-options/](https://plotly.com/python/configuration-options/)
        init_dash_kwargs: dict, optional
            Keyword arguments for the Dash app constructor.
            !!! note
                This variable is of special interest when working in a jupyterhub +
                kubernetes environment. In this case, user notebook servers are spawned
                as separate pods and user access to those servers are proxied via
                jupyterhub. Dash requires the `requests_pathname_prefix` to be set on
                __init__ - which can be done via this `init_dash_kwargs` argument.
                Note that you should also pass the `jupyter_server_url` to the
                `show_dash` method.
                More details: https://github.com/predict-idlab/plotly-resampler/issues/265
        graph_properties: dict, optional
            Dictionary of (keyword, value) for the properties that should be passed to
            the dcc.Graph, by default None.
            e.g.: `{"style": {"width": "50%"}}`
            Note: "config" is not allowed as key in this dict, as there is a distinct
            ``config`` parameter for this property in this method.
            See more [https://dash.plotly.com/dash-core-components/graph](https://dash.plotly.com/dash-core-components/graph)
        **kwargs: dict
            kwargs for the ``app.run_server()`` method, e.g., port=8037.
            !!! note
                These kwargs take precedence over the ones that are passed to the
                constructor via the ``show_dash_kwargs`` argument.

        """
        available_modes = list(dash._jupyter.JupyterDisplayMode.__args__) + [
            "inline_persistent"
        ]
        assert (
            mode is None or mode in available_modes
        ), f"mode must be one of {available_modes}"
        graph_properties = {} if graph_properties is None else graph_properties
        assert "config" not in graph_properties  # There is a param for config
        if self["layout"]["autosize"] is True and self["layout"]["height"] is None:
            graph_properties.setdefault("style", {}).update({"height": "100%"})

        # 0. Check if the traces need to be updated when there is a xrange set
        # This will be the case when the users has set a xrange (via the `update_layout`
        # or `update_xaxes` methods`)
        relayout_dict = {}
        for xaxis_str in self._xaxis_list:
            x_range = self.layout[xaxis_str].range
            if x_range:  # when not None
                relayout_dict[f"{xaxis_str}.range[0]"] = x_range[0]
                relayout_dict[f"{xaxis_str}.range[1]"] = x_range[1]
        if relayout_dict:  # when not empty
            update_data = self._construct_update_data(relayout_dict)

            if not self._is_no_update(update_data):  # when there is an update
                with self.batch_update():
                    # First update the layout (first item of update_data)
                    self.layout.update(self._parse_relayout(update_data[0]))

                    # Then update the data
                    for updated_trace in update_data[1:]:
                        trace_idx = updated_trace.pop("index")
                        self.data[trace_idx].update(updated_trace)

        # 1. Construct the Dash app layout
        init_dash_kwargs = {} if init_dash_kwargs is None else init_dash_kwargs
        if self._create_overview:
            # fmt: off
            # Add the assets folder to the init_dash_kwargs
            init_dash_kwargs["assets_folder"] = os.path.relpath(ASSETS_FOLDER, os.getcwd())
            # Also include the lodash script, as the client-side callbacks uses this
            init_dash_kwargs["external_scripts"] = ["https://cdn.jsdelivr.net/npm/lodash/lodash.min.js" ]
            # fmt: on

        # fmt: off
        div = dash.html.Div(
            children=[
                dash.dcc.Graph(
                    id="resample-figure", figure=self, config=config, **graph_properties
                )
            ],
            style={
                "display": "flex", "flex-flow": "column",
                "height": "95vh", "width": "100%",
            },
        )
        # fmt: on
        if self._create_overview:
            overview_config = config.copy() if config is not None else {}
            overview_config["displayModeBar"] = False
            coarse_fig = self._create_overview_figure()
            div.children += [
                dash.dcc.Graph(
                    id="overview-figure",
                    figure=coarse_fig,
                    config=overview_config,
                    **graph_properties,
                ),
            ]

        # Create the app, populate the layout and register the resample callback
        app = dash.Dash("local_app", **init_dash_kwargs)
        app.layout = div
        self.register_update_graph_callback(
            app,
            "resample-figure",
            "overview-figure" if self._create_overview else None,
        )

        # 2. Run the app
        height_param = "height" if mode == "inline_persistent" else "jupyter_height"
        if "inline" in mode and height_param not in kwargs:
            # If app height is not specified -> re-use figure height for inline dash app
            #  Note: default layout height is 450 (whereas default app height is 650)
            #  See: https://plotly.com/python/reference/layout/#layout-height
            fig_height = self.layout.height if self.layout.height is not None else 450
            kwargs[height_param] = fig_height + 18

        # kwargs take precedence over the show_dash_kwargs
        kwargs = {**self._show_dash_kwargs, **kwargs}

        # Store the app information, so it can be killed
        self._app = app
        self._host = kwargs.get("host", "127.0.0.1")
        self._port = kwargs.get("port", "8050")

        # function signatures are slightly different for the (Jupyter)Dash and the
        # JupyterDashInlinePersistent implementations
        if mode == "inline_persistent":
            from .jupyter_dash_persistent_inline_output import (
                JupyterDashPersistentInlineOutput,
            )

            jpi = JupyterDashPersistentInlineOutput(self)
            jpi.run_app(app=app, **kwargs)
        else:
            app.run(jupyter_mode=mode, **kwargs)

    def stop_server(self, warn: bool = True):
        """Stop the running dash-app.

        Parameters
        ----------
        warn: bool
            Whether a warning message will be shown or  not, by default True.

        !!! warning

            This only works if the dash-app was started with [`show_dash`][figure_resampler.figure_resampler.FigureResampler.show_dash].
        """
        if self._app is not None:
            servers_dict = dash.jupyter_dash._servers
            old_server = servers_dict.get((self._host, self._port))
            if old_server:
                old_server.shutdown()
            del servers_dict[(self._host, self._port)]
        elif warn:
            warnings.warn(
                "Could not stop the server, either the \n"
                + "\t- 'show-dash' method was not called, or \n"
                + "\t- the dash-server wasn't started with 'show_dash'"
            )

    def construct_update_data_patch(
        self, relayout_data: dict
    ) -> Union[dash.Patch, dash.no_update]:
        """Construct the Patch of the to-be-updated front-end data, based on the layout
        change.

        Attention
        ---------
        This method is tightly coupled with Dash app callbacks. It takes the front-end
        figure its ``relayoutData`` as input and returns the ``dash.Patch`` which needs
        to be sent to the ``figure`` property for the corresponding ``dcc.Graph``.

        Parameters
        ----------
        relayout_data: dict
            A dict containing the ``relayoutData`` (i.e., the changed layout data) of
            the corresponding front-end graph.

        Returns
        -------
        dash.Patch:
            The Patch object containing the figure updates which needs to be sent to
            the front-end.

        """
        update_data = self._construct_update_data(relayout_data)
        if not isinstance(update_data, list) or len(update_data) <= 1:
            return dash.no_update

        patched_figure = dash.Patch()  # create patch
        for trace in update_data[1:]:  # skip first item as it contains the relayout
            trace_index = trace.pop("index")  # the index of the corresponding trace
            # All the other items are the trace properties which needs to be updated
            for k, v in trace.items():
                # NOTE: we need to use the `patched_figure` as a dict, and not
                # `patched_figure.data` as the latter will replace **all** the
                # data for the corresponding trace, and we just want to update the
                # specific trace its properties.
                patched_figure["data"][trace_index][k] = v
        return patched_figure

    def register_update_graph_callback(
        self,
        app: dash.Dash,
        graph_id: str,
        coarse_graph_id: Optional[str] = None,
    ):
        """Register the [`construct_update_data_patch`][figure_resampler.figure_resampler_interface.AbstractFigureAggregator.construct_update_data_patch]
        method as callback function to the passed dash-app.

        Parameters
        ----------
        app: Union[dash.Dash, JupyterDash]
            The app in which the callback will be registered.
        graph_id:
            The id of the ``dcc.Graph``-component which withholds the to-be resampled
            Figure.
        coarse_graph_id: str, optional
            The id of the ``dcc.Graph``-component which withholds the coarse overview
            Figure, by default None.

        """
        # As we use the figure again as output, we need to set: allow_duplicate=True

        if coarse_graph_id is not None:
            # update pr graph range with overview selection
            app.clientside_callback(
                dash.ClientsideFunction(
                    namespace="clientside", function_name="coarse_to_main"
                ),
                dash.Output(graph_id, "id", allow_duplicate=True),
                dash.Input(coarse_graph_id, "selectedData"),
                dash.State(graph_id, "id"),
                dash.State(coarse_graph_id, "id"),
                prevent_initial_call=True,
            )

            # update selectbox with clientside callback
            app.clientside_callback(
                dash.ClientsideFunction(
                    namespace="clientside", function_name="main_to_coarse"
                ),
                dash.Output(coarse_graph_id, "id", allow_duplicate=True),
                dash.Input(graph_id, "relayoutData"),
                dash.State(coarse_graph_id, "id"),
                dash.State(graph_id, "id"),
                prevent_initial_call=True,
            )

        app.callback(
            dash.Output(graph_id, "figure", allow_duplicate=True),
            dash.Input(graph_id, "relayoutData"),
            prevent_initial_call=True,
        )(self.construct_update_data_patch)

    def _get_pr_props_keys(self) -> List[str]:
        # Add the additional plotly-resampler properties of this class
        return super()._get_pr_props_keys() + ["_show_dash_kwargs"]

    def _ipython_display_(self):
        # To display the figure inline as a dash app
        self.show_dash(mode="inline")



================================================
FILE: plotly_resampler/figure_resampler/figurewidget_resampler.py
================================================
# -*- coding: utf-8 -*-
"""
``FigureWidgetResampler`` wrapper around the plotly ``go.FigureWidget`` class.

Utilizes the ``fig.layout.on_change`` method to enable dynamic resampling.

"""

from __future__ import annotations

__author__ = "Jonas Van Der Donckt, Jeroen Van Der Donckt, Emiel Deprost"

from typing import Tuple

import plotly.graph_objects as go
from plotly.basedatatypes import BaseFigure

from ..aggregation import (
    AbstractAggregator,
    AbstractGapHandler,
    MedDiffGapHandler,
    MinMaxLTTB,
)
from .figure_resampler_interface import AbstractFigureAggregator


class _FigureWidgetResamplerM(type(AbstractFigureAggregator), type(go.FigureWidget)):
    # MetaClass for the FigureWidgetResampler
    pass


class FigureWidgetResampler(
    AbstractFigureAggregator, go.FigureWidget, metaclass=_FigureWidgetResamplerM
):
    """Data aggregation functionality wrapper for ``go.FigureWidgets``.

    !!! warning

        * This wrapper only works within ``jupyter``-based environments.
        * The ``.show()`` method returns a **static figure** on which the
          **dynamic resampling cannot be performed**. To allow dynamic resampling,
          you should just output the ``FigureWidgetResampler`` object in a cell.

    """

    def __init__(
        self,
        figure: BaseFigure | dict = None,
        convert_existing_traces: bool = True,
        default_n_shown_samples: int = 1000,
        default_downsampler: AbstractAggregator = MinMaxLTTB(),
        default_gap_handler: AbstractGapHandler = MedDiffGapHandler(),
        resampled_trace_prefix_suffix: Tuple[str, str] = (
            '<b style="color:sandybrown">[R]</b> ',
            "",
        ),
        show_mean_aggregation_size: bool = True,
        convert_traces_kwargs: dict | None = None,
        verbose: bool = False,
    ):
        # Parse the figure input before calling `super`
        f = self._get_figure_class(go.FigureWidget)()
        f._data_validator.set_uid = False

        if isinstance(figure, BaseFigure):
            # A base figure object, can be;
            # - a base plotly figure: go.Figure or go.FigureWidget
            # - a plotly-resampler figure: subclass of AbstractFigureAggregator
            # => we first copy the layout, grid_str and grid ref
            f.layout = figure.layout
            f._grid_str = figure._grid_str
            f._grid_ref = figure._grid_ref
            f.add_traces(figure.data)
        elif isinstance(figure, dict) and (
            "data" in figure or "layout" in figure  # or "frames" in figure  # TODO
        ):
            # A figure as a dict, can be;
            # - a plotly figure as a dict (after calling `fig.to_dict()`)
            # - a pickled (plotly-resampler) figure (after loading a pickled figure)
            f.layout = figure.get("layout")
            f._grid_str = figure.get("_grid_str")
            f._grid_ref = figure.get("_grid_ref")
            f.add_traces(figure.get("data"))
            # `pr_props` is not None when loading a pickled plotly-resampler figure
            f._pr_props = figure.get("pr_props")
            # `f._pr_props`` is an attribute to store properties of a plotly-resampler
            # figure. This attribute is only used to pass information to the super()
            # constructor. Once the super constructor is called, the attribute is
            # removed.

            # f.add_frames(figure.get("frames")) TODO
        elif isinstance(figure, (dict, list)):
            # A single trace dict or a list of traces
            f.add_traces(figure)

        super().__init__(
            f,
            convert_existing_traces,
            default_n_shown_samples,
            default_downsampler,
            default_gap_handler,
            resampled_trace_prefix_suffix,
            show_mean_aggregation_size,
            convert_traces_kwargs,
            verbose,
        )

        if isinstance(figure, AbstractFigureAggregator):
            # Copy the `_hf_data` if the previous figure was an AbstractFigureAggregator
            # And adjust the default max_n_samples and
            self._hf_data.update(
                self._copy_hf_data(figure._hf_data, adjust_default_values=True)
            )

            # Note: This hack ensures that the this figure object initially uses
            # data of the whole view. More concretely; we create a dict
            # serialization figure and adjust the hf-traces to the whole view
            # with the check-update method (by passing no range / filter args)
            with self.batch_update():
                graph_dict: dict = self._get_current_graph()
                update_indices = self._check_update_figure_dict(graph_dict)
                for idx in update_indices:
                    self.data[idx].update(graph_dict["data"][idx])

        self._prev_layout = None  # Contains the previous xaxis layout configuration

        # used for logging purposes to save a history of layout changes
        self._relayout_hist = []

        # Assign the the update-methods to the corresponding classes
        showspike_keys = [f"{xaxis}.showspikes" for xaxis in self._xaxis_list]
        self.layout.on_change(self._update_spike_ranges, *showspike_keys)

        x_relayout_keys = [f"{xaxis}.range" for xaxis in self._xaxis_list]
        self.layout.on_change(self._update_x_ranges, *x_relayout_keys)

    def _update_x_ranges(self, layout, *x_ranges, force_update: bool = False):
        """Update the the go.Figure data based on changed x-ranges.

        Parameters
        ----------
        layout : go.Layout
            The figure's (i.e, self) layout object. Remark that this is a reference,
            so if we change self.layout (same object reference), this object will
            change.
        *x_ranges: iterable
            A iterable list of current x-ranges, where each x-range is a tuple of two
            items, indicating the current/new (if changed) left-right x-range,
            respectively.
        fore_update: bool
            Whether an update of all traces will be forced, by default False.
        """
        relayout_dict = {}  # variable in which we aim to reconstruct the relayout
        # serialize the layout in a new dict object
        layout = {
            xaxis_str: layout[xaxis_str].to_plotly_json()
            for xaxis_str in self._xaxis_list
        }
        if self._prev_layout is None:
            self._prev_layout = layout

        for xaxis_str, x_range in zip(self._xaxis_list, x_ranges):
            # We also check whether "range" is within the xaxis its layout otherwise
            # It is most-likely an autorange check
            if (
                "range" in layout[xaxis_str]
                and self._prev_layout[xaxis_str].get("range", []) != x_range
                or (force_update and x_range is not None)
            ):
                # a change took place -> add to the relayout dict
                relayout_dict[f"{xaxis_str}.range[0]"] = x_range[0]
                relayout_dict[f"{xaxis_str}.range[1]"] = x_range[1]

                # An update will take place for that trace
                # -> save current xaxis range to _prev_layout
                self._prev_layout[xaxis_str]["range"] = x_range

        if relayout_dict:  # when not empty
            # Construct the update data
            update_data = self._construct_update_data(relayout_dict)

            if self._is_no_update(update_data):
                # Return when no data update
                return

            if self._print_verbose:
                self._relayout_hist.append(dict(zip(self._xaxis_list, x_ranges)))
                self._relayout_hist.append(layout)
                self._relayout_hist.append(["xaxis-range-update", len(update_data) - 1])
                self._relayout_hist.append("-" * 30)

            with self.batch_update():
                # First update the layout (first item of update_data)
                self.layout.update(self._parse_relayout(update_data[0]))

                for xaxis_str in self._xaxis_list:
                    if "showspikes" in layout[xaxis_str]:
                        self.layout[xaxis_str].pop("showspikes")

                # Then update the data
                for updated_trace in update_data[1:]:
                    trace_idx = updated_trace.pop("index")
                    self.data[trace_idx].update(updated_trace)

    def _update_spike_ranges(self, layout, *showspikes, force_update=False):
        """Update the go.Figure based on the changed spike-ranges.

        Parameters
        ----------
        layout : go.Layout
            The figure's (i.e, self) layout object. Remark that this is a reference,
            so if we change self.layout (same object reference), this object will
            change.
        *showspikes: iterable
            A iterable where each item is a bool, indicating  whether showspikes is set
            to true/false for the corresponding xaxis in ``self._xaxis_list``.
        force_update: bool
            Bool indicating whether the range updates need to take place. This is
            especially useful when you have recently updated the figure its data (with
            the hf_data property) and want to perform an autoscale, independent from
            the current figure-layout.
        """
        relayout_dict = {}  # variable in which we aim to reconstruct the relayout
        # serialize the layout in a new dict object
        layout = {
            xaxis_str: layout[xaxis_str].to_plotly_json()
            for xaxis_str in self._xaxis_list
        }

        if self._prev_layout is None:
            self._prev_layout = layout

        for xaxis_str, showspike in zip(self._xaxis_list, showspikes):
            if (
                force_update
                or
                # autorange key must be set to True
                (
                    layout[xaxis_str].get("autorange", False)
                    # we only perform updates for traces which have 'range' property,
                    # as we do need to reconstruct the update-data for these traces
                    and self._prev_layout[xaxis_str].get("range", None) is not None
                )
            ):
                relayout_dict[f"{xaxis_str}.autorange"] = True
                relayout_dict[f"{xaxis_str}.showspikes"] = showspike
                # autorange -> we pop the xaxis range
                if "range" in layout[xaxis_str]:
                    del layout[xaxis_str]["range"]

        if len(relayout_dict):
            # An update will take place, save current layout to _prev_layout
            self._prev_layout = layout

            # Construct the update data
            update_data = self._construct_update_data(relayout_dict)
            if not self._is_no_update(update_data):
                if self._print_verbose:
                    self._relayout_hist.append(layout)
                    self._relayout_hist.append(
                        ["showspikes-update", len(update_data) - 1]
                    )
                    self._relayout_hist.append("-" * 30)

                with self.batch_update():
                    # First update the layout (first item of update_data)
                    if not force_update:
                        self.layout.update(self._parse_relayout(update_data[0]))

                    # Also: Remove the showspikes from the layout, otherwise the autorange
                    # will not work as intended (it will not be triggered again)
                    # Note: this removal causes a second trigger of this method
                    # which will go in the "else" part below.
                    for xaxis_str in self._xaxis_list:
                        self.layout[xaxis_str].pop("showspikes")

                    # Then, update the data
                    for updated_trace in update_data[1:]:
                        trace_idx = updated_trace.pop("index")
                        self.data[trace_idx].update(updated_trace)
        elif self._print_verbose:
            self._relayout_hist.append(["showspikes", "initial call or showspikes"])
            self._relayout_hist.append("-" * 40)

    def reset_axes(self):
        """Reset the axes of the FigureWidgetResampler.

        This is useful when adjusting the `hf_data` properties of the
        ``FigureWidgetResampler``.
        """
        self._update_spike_ranges(
            self.layout, *[False] * len(self._xaxis_list), force_update=True
        )
        # Reset the layout
        self.update_layout(
            {
                axis: {"autorange": None, "range": None}
                for axis in self._xaxis_list + self._yaxis_list
            }
        )

    def reload_data(self):
        """Reload all the data of FigureWidgetResampler for the current range-view.

        This is useful when adjusting the `hf_data` properties of the
        ``FigureWidgetResampler``.
        """
        if all(
            self.layout[xaxis].autorange
            or (
                self.layout[xaxis].autorange is None
                and self.layout[xaxis].range is None
            )
            for xaxis in self._xaxis_list
        ):
            self._update_spike_ranges(
                self.layout, *[False] * len(self._xaxis_list), force_update=True
            )
        else:
            # Resample the data for the current range-view
            self._update_x_ranges(
                self.layout,
                # Pass the current view to trigger a resample operation
                *[self.layout[xaxis_str]["range"] for xaxis_str in self._xaxis_list],
                force_update=True,
            )
            # TODO: when we know which traces have changed we can use
            # a new -> `update_xaxis_str` argument.

    def __reduce__(self):
        # Needed for pickling
        # Specifically set the class name, as the metaclass is not easily picklable
        return FigureWidgetResampler, *list(super().__reduce__())[1:]



================================================
FILE: plotly_resampler/figure_resampler/jupyter_dash_persistent_inline_output.py
================================================
import base64
import contextlib
import logging
import os
import queue
import threading
import uuid
import warnings

import requests

try:
    from IPython.display import HTML, display
except ImportError:
    raise ImportError(
        "The `jupyter_dash_persistent_inline_output` requirements are not installed.\n"
        "Please install them with:\n"
        "pip install plotly_resampler[inline_persistent]"
    )

from dash._jupyter import JupyterDash, _jupyter_config, make_server
from plotly.graph_objects import Figure
from retrying import retry


class JupyterDashPersistentInlineOutput:
    """Extension of the JupyterDash class to support the custom inline output for
    ``FigureResampler`` figures.

    Specifically we embed a div in the notebook to display the figure inline.

     - In this div the figure is shown as an iframe when the server (of the dash app)
       is alive.
     - In this div the figure is shown as an image when the server (of the dash app)
       is dead.

    As the HTML & javascript code is embedded in the notebook output, which is loaded
    each time you open the notebook, the figure is always displayed (either as iframe
    or just an image).
    Hence, this extension enables to maintain always an output in the notebook.

    .. Note::
        This subclass is only used when the mode is set to ``"inline_persistent"`` in
        the :func:`FigureResampler.show_dash <plotly_resampler.figure_resampler.FigureResampler.show_dash>`
        method. However, the mode should be passed as ``"inline"`` since this subclass
        overwrites the inline behavior.

    .. Note::
        This subclass utilizes the optional ``flask_cors`` package to detect whether the
        server is alive or not.

    """

    def __init__(self, fig: Figure) -> None:
        super().__init__()
        self.fig = fig

        # The unique id of this app
        # This id is used to couple the output in the notebook with this app
        # A fetch request is performed to the _is_alive_{uid} endpoint to check if the
        # app is still alive.
        self.uid = str(uuid.uuid4())

    def _display_inline_output(self, dashboard_url, width, height):
        """Display the dash app persistent inline in the notebook.

        The figure is displayed as an iframe in the notebook if the server is reachable,
        otherwise as an image.
        """
        # TODO: check whether an error gets logged in case of crash
        # TODO: add option to opt out of this
        from IPython.display import display

        try:
            import flask_cors  # noqa: F401
        except (ImportError, ModuleNotFoundError):
            warnings.warn(
                "'flask_cors' is not installed. The persistent inline output will "
                + " not be able to detect whether the server is alive or not."
            )

        # Get the image from the dashboard and encode it as base64
        fig = self.fig  # is stored in the show_dash method
        f_width = 1000 if fig.layout.width is None else fig.layout.width
        fig_base64 = base64.b64encode(
            fig.to_image(format="png", width=f_width, scale=1, height=fig.layout.height)
        ).decode("utf8")

        # The html (& javascript) code to display the app / figure
        uid = self.uid
        display(
            {
                "text/html": f"""
                <div id='PR_div__{uid}'></div>
                <script type='text/javascript'>
                """
                + """

                function setOutput(timeout) {
                    """
                +
                # Variables should be in local scope (in the closure)
                f"""
                    var pr_div = document.getElementById('PR_div__{uid}');
                    var url = '{dashboard_url}';
                    var pr_img_src = 'data:image/png;base64, {fig_base64}';
                    var is_alive_suffix = '_is_alive_{uid}';
                    """
                + """

                    if (pr_div.firstChild) return  // return if already loaded

                    const controller = new AbortController();
                    const signal = controller.signal;

                    return fetch(url + is_alive_suffix, {method: 'GET', signal: signal})
                        .then(response => response.text())
                        .then(data =>
                            {
                                if (data == "Alive") {
                                    console.log("Server is alive");
                                    iframeOutput(pr_div, url);
                                } else {
                                    // I think this case will never occur because of CORS
                                    console.log("Server is dead");
                                    imageOutput(pr_div, pr_img_src);
                                }
                            }
                        )
                        .catch(error => {
                            console.log("Server is unreachable");
                            imageOutput(pr_div, pr_img_src);
                        })
                }

                setOutput(350);

                function imageOutput(element, pr_img_src) {
                    console.log('Setting image');
                    var pr_img = document.createElement("img");
                    pr_img.setAttribute("src", pr_img_src)
                    pr_img.setAttribute("alt", 'Server unreachable - using image instead');
                    """
                + f"""
                    pr_img.setAttribute("max-width", '{width}');
                    pr_img.setAttribute("max-height", '{height}');
                    pr_img.setAttribute("width", 'auto');
                    pr_img.setAttribute("height", 'auto');
                    """
                + """
                    element.appendChild(pr_img);
                }

                function iframeOutput(element, url) {
                    console.log('Setting iframe');
                    var pr_iframe = document.createElement("iframe");
                    pr_iframe.setAttribute("src", url);
                    pr_iframe.setAttribute("frameborder", '0');
                    pr_iframe.setAttribute("allowfullscreen", '');
                    """
                + f"""
                    pr_iframe.setAttribute("width", '{width}');
                    pr_iframe.setAttribute("height", '{height}');
                    """
                + """
                    element.appendChild(pr_iframe);
                }
                </script>
                """
            },
            raw=True,
            clear=True,
            display_id=uid,
        )

    # NOTE: Minimally adatped version from dash._jupyter.JupyterDash.run_server
    def run_app(
        self,
        app,
        width="100%",
        height=650,
        host="127.0.0.1",
        port=8050,
        server_url=None,
    ):
        """Run the inline persistent dash app in the notebook.

        Parameters
        ----------
        app : dash.Dash
            A Dash application instance
        width : str, optional
            Width of app when displayed using mode="inline", by default "100%"
        height : int, optional
            Height of app when displayed using mode="inline", by default 650
        host : str, optional
            Host of the server, by default "127.0.0.1"
        port : int, optional
            Port used by the server, by default 8050
        server_url : str, optional
            Use if a custom url is required to display the app, by default None

        """
        # Terminate any existing server using this port
        old_server = JupyterDash._servers.get((host, port))
        if old_server:
            old_server.shutdown()
            del JupyterDash._servers[(host, port)]

        # Configure pathname prefix
        if "base_subpath" in _jupyter_config:
            requests_pathname_prefix = (
                _jupyter_config["base_subpath"].rstrip("/") + "/proxy/{port}/"
            )
        else:
            requests_pathname_prefix = app.config.get("requests_pathname_prefix", None)

        if requests_pathname_prefix is not None:
            requests_pathname_prefix = requests_pathname_prefix.format(port=port)
        else:
            requests_pathname_prefix = "/"

        # FIXME Move config initialization to main dash __init__
        # low-level setter to circumvent Dash's config locking
        # normally it's unsafe to alter requests_pathname_prefix this late, but
        # Jupyter needs some unusual behavior.
        dict.__setitem__(
            app.config, "requests_pathname_prefix", requests_pathname_prefix
        )

        # # Compute server_url url
        if server_url is None:
            if "server_url" in _jupyter_config:
                server_url = _jupyter_config["server_url"].rstrip("/")
            else:
                domain_base = os.environ.get("DASH_DOMAIN_BASE", None)
                if domain_base:
                    # Dash Enterprise sets DASH_DOMAIN_BASE environment variable
                    server_url = "https://" + domain_base
                else:
                    server_url = f"http://{host}:{port}"
        else:
            server_url = server_url.rstrip("/")

        # server_url = "http://{host}:{port}".format(host=host, port=port)

        dashboard_url = f"{server_url}{requests_pathname_prefix}"

        # prevent partial import of orjson when it's installed and mode=jupyterlab
        # TODO: why do we need this? Why only in this mode? Importing here in
        # all modes anyway, in case there's a way it can pop up in another mode
        try:
            # pylint: disable=C0415,W0611
            import orjson  # noqa: F401
        except ImportError:
            pass

        err_q = queue.Queue()

        server = make_server(host, port, app.server, threaded=True, processes=0)
        logging.getLogger("werkzeug").setLevel(logging.ERROR)

        # ---------------------------------------------------------------------
        # NOTE: added this code to mimic the _alive_{token} endpoint but with cors
        with contextlib.suppress(ImportWarning, ModuleNotFoundError):
            from flask_cors import cross_origin

            @app.server.route(f"/_is_alive_{self.uid}", methods=["GET"])
            @cross_origin(origins=["*"], allow_headers=["Content-Type"])
            def broadcast_alive():
                return "Alive"

        # ---------------------------------------------------------------------

        @retry(
            stop_max_attempt_number=15,
            wait_exponential_multiplier=100,
            wait_exponential_max=1000,
        )
        def run():
            try:
                server.serve_forever()
            except SystemExit:
                pass
            except Exception as error:
                err_q.put(error)
                raise error

        thread = threading.Thread(target=run)
        thread.daemon = True
        thread.start()

        JupyterDash._servers[(host, port)] = server

        # Wait for server to start up
        alive_url = f"http://{host}:{port}/_alive_{JupyterDash.alive_token}"

        def _get_error():
            try:
                err = err_q.get_nowait()
                if err:
                    raise err
            except queue.Empty:
                pass

        # Wait for app to respond to _alive endpoint
        @retry(
            stop_max_attempt_number=15,
            wait_exponential_multiplier=10,
            wait_exponential_max=1000,
        )
        def wait_for_app():
            _get_error()
            try:
                req = requests.get(alive_url)
                res = req.content.decode()
                if req.status_code != 200:
                    raise Exception(res)

                if res != "Alive":
                    url = f"http://{host}:{port}"
                    raise OSError(
                        f"Address '{url}' already in use.\n"
                        "    Try passing a different port to run_server."
                    )
            except requests.ConnectionError as err:
                _get_error()
                raise err

        try:
            wait_for_app()
            self._display_inline_output(dashboard_url, width=width, height=height)

        except Exception as final_error:  # pylint: disable=broad-except
            msg = str(final_error)
            if msg.startswith("<!"):
                display(HTML(msg))
            else:
                raise final_error



================================================
FILE: plotly_resampler/figure_resampler/utils.py
================================================
"""Utility functions for the figure_resampler submodule."""

import math

import pandas as pd
from plotly.basedatatypes import BaseFigure

try:  # Fails when IPywidgets is not installed
    from plotly.basewidget import BaseFigureWidget
except (ImportError, ModuleNotFoundError):
    BaseFigureWidget = type(None)

from typing import Any

### Checks for the figure type


def is_figure(figure: Any) -> bool:
    """Check if the figure is a plotly go.Figure or a FigureResampler.

    !!! note

        This method does not use isinstance(figure, go.Figure) as this will not work
        when go.Figure is decorated (after executing the
        ``register_plotly_resampler`` function).

    Parameters
    ----------
    figure : Any
        The figure to check.

    Returns
    -------
    bool
        True if the figure is a plotly go.Figure or a FigureResampler.
    """
    return isinstance(figure, BaseFigure) and (not isinstance(figure, BaseFigureWidget))


def is_figurewidget(figure: Any):
    """Check if the figure is a plotly go.FigureWidget or a FigureWidgetResampler.

    !!! note

        This method does not use isinstance(figure, go.FigureWidget) as this will not
        work when go.FigureWidget is decorated (after executing the
        ``register_plotly_resampler`` function).

    Parameters
    ----------
    figure : Any
        The figure to check.

    Returns
    -------
    bool
        True if the figure is a plotly go.FigureWidget or a FigureWidgetResampler.
    """
    return isinstance(figure, BaseFigureWidget)


def is_fr(figure: Any) -> bool:
    """Check if the figure is a FigureResampler.

    !!! note

        This method will not return True if the figure is a plotly go.Figure.

    Parameters
    ----------
    figure : Any
        The figure to check.

    Returns
    -------
    bool
        True if the figure is a FigureResampler.
    """
    from plotly_resampler import FigureResampler

    return isinstance(figure, FigureResampler)


def is_fwr(figure: Any) -> bool:
    """Check if the figure is a FigureWidgetResampler.

    !!! note

        This method will not return True if the figure is a plotly go.FigureWidget.

    Parameters
    ----------
    figure : Any
        The figure to check.

    Returns
    -------
    bool
        True if the figure is a FigureWidgetResampler.
    """
    from plotly_resampler import FigureWidgetResampler

    return isinstance(figure, FigureWidgetResampler)


### Rounding functions for bin size


def timedelta_to_str(td: pd.Timedelta) -> str:
    """Construct a tight string representation for the given timedelta arg.

    Parameters
    ----------
    td: pd.Timedelta
        The timedelta for which the string representation is constructed

    Returns
    -------
    str:
        The tight string bounds of format '$d-$h$m$s.$ms'.
        If the timedelta is negative, the string starts with 'NEG'.

    """
    out_str = ""

    # Edge case if we deal with negative
    if td < pd.Timedelta(seconds=0):
        td *= -1
        out_str += "NEG"

    # Note: this must happen after the *= -1
    c = td.components
    if c.days > 0:
        out_str += f"{c.days}D"
    if c.hours > 0 or c.minutes > 0 or c.seconds > 0 or c.milliseconds > 0:
        out_str += "_" if out_str else ""  # add seperator if non-empty

    if c.hours > 0:
        out_str += f"{c.hours}h"
    if c.minutes > 0:
        out_str += f"{c.minutes}m"
    if c.seconds > 0:
        if c.milliseconds:
            out_str += (
                f"{c.seconds}.{str(c.milliseconds / 1000).split('.')[-1].rstrip('0')}s"
            )
        else:
            out_str += f"{c.seconds}s"
    elif c.milliseconds > 0:
        out_str += f"{c.milliseconds}ms"
    if c.microseconds > 0:
        out_str += f"{c.microseconds}us"
    if c.nanoseconds > 0:
        out_str += f"{c.nanoseconds}ns"
    return out_str


def round_td_str(td: pd.Timedelta) -> str:
    """Round a timedelta to the nearest unit and convert to a string.

    Parameters
    ----------
    td : pd.Timedelta
        The timedelta to round.

    Returns
    -------
    str
        The rounded timedelta as a string.
        If the timedelta is == 0, None is returned.

    !!! info "See Also"
        [`timedelta_to_str`][figure_resampler.utils.timedelta_to_str]

    """
    for t_s in ("D", "h", "min", "s", "ms", "us", "ns"):
        if td > 0.95 * pd.Timedelta(f"1{t_s}"):
            return timedelta_to_str(td.round(t_s))


def round_number_str(number: float) -> str:
    """Round a number to the nearest unit and convert to a string.

    Parameters
    ----------
    number : float
        The number to round.

    Returns
    -------
    str
        The rounded number as a string.
        If the number is == 0, None is returned.

    """
    sign = "-" if number < 0 else ""
    number = abs(number)
    if number > 0.95:
        for unit, scaling in [
            ("T", int(1e12)),  # Trillion
            ("B", int(1e9)),  # Billion
            ("M", int(1e6)),  # Million
            ("k", int(1e3)),  # Thousand
        ]:
            if number / scaling > 0.95:
                return f"{round(number / scaling)}{unit}"
        return sign + str(round(number))
    if number > 0:  # avoid log10(0)
        # we have a number between 0-0.95 -> round till nearest non-zero digit
        return sign + str(round(number, 1 + abs(int(math.log10(number)))))



================================================
FILE: plotly_resampler/figure_resampler/assets/coarse_fine.js
================================================
function getGraphDiv(gdID) {
    let graphDiv = document?.querySelectorAll('div[id*="' + gdID + '"][class*="dash-graph"]');
    graphDiv = graphDiv?.[0]?.getElementsByClassName("js-plotly-plot")?.[0];
    if (!_.isElement(graphDiv)) {
        throw new Error(`Invalid gdID '${gdID}'`);
    }
    return graphDiv;
}

/**
 *
 * @param {object} data The data of the graphDiv
 * @returns {Array} An array containing all the unique axis keys of the graphDiv data
 *                  [{x: x[ID], y: y[ID]}, {x: x[ID], y: y[ID]}]
 */
const getXYAxisKeys = (data) => {
    return _.chain(data)
        .map((obj) => ({ x: obj.xaxis || "x", y: obj.yaxis || "y" }))
        .uniqWith(_.isEqual)
        .value();
};

const getAnchorT = (keys, anchor) => {
    const obj_index = anchor.slice(0, 1);
    const anchorT = _.chain(keys)
        .filter((obj) => obj[obj_index] == anchor)
        .value()[0][{ x: "y", y: "x" }[obj_index]];

    return anchorT;
};

/**
 * Get the corresponding axis name of the anchors
 *
 * @param {object} layout the layout of the graphDiv
 * @returns {object} An object containing the anchor and its orthogonal axis name e.g.
 *                  {x[ID]: yaxis[ID], y[ID]: xaxis[ID]}
 */
const getLayoutAxisAnchors = (layout) => {
    var layout_axis_anchors = Object.assign(
        {},
        ..._.chain(layout)
            .map((value, key) => {
                if (key.includes("axis")) return { [value.anchor]: key };
            })
            .without(undefined)
            .value()
    );
    // Edge case for non "make_subplot" figures; i.e. figures constructed with
    // go.Figure
    if (_.size(layout_axis_anchors) == 1 && _.has(layout_axis_anchors, undefined)) {
        return { x: "yaxis", y: "xaxis" };
    }
    return layout_axis_anchors;
};

/**
 * Compare the equality of two arrays with a certain decimal point presiction
 * @param {*} objValueArr An array with numeric values
 * @param {*} othValueArr An array with numeray values
 * @returns {boolean} true when all values are equal (to 5 decimal points)
 */
function rangeCustomizer(objValueArr, othValueArr) {
    return _.every(
        _.zipWith(objValueArr, othValueArr, (objValue, othValue) => {
            if (_.isNumber(objValue) && _.isNumber(othValue)) {
                objValue = _.round(objValue, 5);
                othValue = _.round(othValue, 5);
                return objValue === othValue;
            } else {
                alert(`not a number  ${objValue} type:${typeof objValue} | ${othValue} type:${typeof othValue}`);
            }
        })
    );
}

window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        coarse_to_main: function (selectedData, mainFigID, coarseFigID) {
            // Base case
            if (!selectedData.range) {
                return mainFigID;
            }

            main_graphDiv = getGraphDiv(mainFigID);
            coarse_graphDiv = getGraphDiv(coarseFigID);

            const coarse_xy_axiskeys = getXYAxisKeys(coarse_graphDiv.data);
            const main_xy_axiskeys = getXYAxisKeys(main_graphDiv.data);
            const layout_axis_anchors = getLayoutAxisAnchors(main_graphDiv.layout);

            // Use the maingraphDiv its layout to obtain a list of a list of all shared (x)axis names
            // in practice, these are the xaxis names that are linked to each other (i.e. the inner list is the
            // xaxis names of the subplot columns)
            // e.g.: [ [xaxis1, xaxis2],  [xaxis3, xaxis4] ]
            let shared_axes_list = _.chain(main_graphDiv.layout)
                .map((value, key) => {
                    if (value.matches) return { anchor: value.matches, match: [key] };
                })
                .without(undefined)
                // groupby same anchor and concat the match arrays
                .groupBy("anchor")
                .map(
                    _.spread((...values) => {
                        return _.mergeWith(...values, (objValue, srcValue) => {
                            if (_.isArray(objValue)) return objValue.concat(srcValue);
                        });
                    })
                )
                // add the axis string to the match array and return the match array
                .map((m_obj) => {
                    const anchorT = getAnchorT(main_xy_axiskeys, m_obj.anchor);
                    let axis_str = layout_axis_anchors[anchorT];
                    m_obj.match.push(axis_str);
                    return m_obj.match;
                })
                .value();
            // console.log("shared axes list", shared_axes_list);

            const relayout = {};

            // Quick inline function to set the relayout range values
            const setRelayoutRangeValues = (axisStr, values) => {
                for (let rangeIdx = 0; rangeIdx < 2; rangeIdx++) {
                    relayout[axisStr + `.range[${rangeIdx}]`] = values[rangeIdx];
                }
            };

            // iterate over the selected data range
            // console.log("selected data range", selectedData.range);
            for (const anchor_key in selectedData.range) {
                const selected_range = selectedData.range[anchor_key];
                // Obtain the anchor key of the orthogonal axis (x or y), based on the coarse graphdiv anchor pairs
                const anchorT = getAnchorT(coarse_xy_axiskeys, anchor_key);
                const axisStr = layout_axis_anchors[anchorT];
                const mainLayoutRange = main_graphDiv.layout[axisStr].range;
                const coarseFigRange = coarse_graphDiv.layout[axisStr].range;

                if (!_.isEqual(selected_range, mainLayoutRange)) {
                    const shared_axis_match = _.chain(shared_axes_list)
                        .filter((arr) => arr.includes(axisStr))
                        .value()[0];
                    if (axisStr.includes("yaxis") && _.isEqualWith(selected_range, coarseFigRange, rangeCustomizer)) {
                        continue;
                    }

                    if (shared_axis_match) {
                        shared_axis_match.forEach((axisMStr) => {
                            setRelayoutRangeValues(axisMStr, selected_range);
                        });
                    } else {
                        setRelayoutRangeValues(axisStr, selected_range);
                    }
                }
            }

            Object.keys(relayout).length > 0 ? Plotly.relayout(main_graphDiv, relayout) : null;
            return mainFigID;
        },

        main_to_coarse: function (mainRelayout, coarseFigID, mainFigID) {
            const coarse_graphDiv = getGraphDiv(coarseFigID);
            const main_graphDiv = getGraphDiv(mainFigID);

            const coarse_xy_axiskeys = getXYAxisKeys(coarse_graphDiv.data);
            const layout_axis_anchors = getLayoutAxisAnchors(coarse_graphDiv.layout);

            const currentSelections = coarse_graphDiv.layout.selections;
            const update = { selections: currentSelections || [] };

            const getUpdateObj = (xy_pair, x_range, y_range) => {
                return {
                    type: "rect",
                    xref: xy_pair.x,
                    yref: xy_pair.y,
                    line: { width: 1, color: "#352F44", dash: "solid" },
                    x0: x_range[0],
                    x1: x_range[1],
                    y0: y_range[0],
                    y1: y_range[1],
                };
            };

            // Base case; no selections yet on the coarse graph
            if (!currentSelections) {
                // if current selections is None
                coarse_xy_axiskeys.forEach((xy_pair) => {
                    // console.log("xy pair", xy_pair);
                    const x_axis_key = _.has(layout_axis_anchors, xy_pair.y) ? layout_axis_anchors[xy_pair.y] : "xaxis";
                    const y_axis_key = _.has(layout_axis_anchors, xy_pair.x) ? layout_axis_anchors[xy_pair.x] : "yaxis";
                    // console.log('xaxis key', x_axis_key, main_graphDiv.layout[x_axis_key]);
                    const x_range = main_graphDiv.layout[x_axis_key].range;
                    const y_range = main_graphDiv.layout[y_axis_key].range;

                    update["selections"].push(getUpdateObj(xy_pair, x_range, y_range));
                });
                Plotly.relayout(coarse_graphDiv, update);
                return coarseFigID;
            }

            // Alter the selections based on the relayout
            let performed_update = false;

            for (let i = 0; i < coarse_xy_axiskeys.length; i++) {
                const xy_pair = coarse_xy_axiskeys[i];
                // If else handles the edge case of a figure without subplots
                const x_axis_key = _.has(layout_axis_anchors, xy_pair.y) ? layout_axis_anchors[xy_pair.y] : "xaxis";
                const y_axis_key = _.has(layout_axis_anchors, xy_pair.x) ? layout_axis_anchors[xy_pair.x] : "yaxis";
                // console.log('xaxis key', x_axis_key, main_graphDiv.layout[x_axis_key]);

                let x_range = main_graphDiv.layout[x_axis_key].range;
                let y_range = main_graphDiv.layout[y_axis_key].range;
                // If the y-axis autorange is true, we alter the y-range to the coarse graphdiv its y-range
                // console.log('mainrelayout', mainRelayout);
                if (main_graphDiv.layout[y_axis_key]["autorange"] === true) {
                    y_range = coarse_graphDiv.layout[y_axis_key].range;
                }
                if (
                    mainRelayout[x_axis_key + ".autorange"] === true &&
                    mainRelayout[y_axis_key + ".autorange"] === true
                ) {
                    performed_update = true;
                    if (
                        // NOTE: for some reason, showspikes info is only available for the xaxis & yaxis keys
                        _.has(mainRelayout, "xaxis.showspikes") &&
                        _.has(mainRelayout, "yaxis.showspikes")
                    ) {
                        // reset axis -> we use the coarse graphDiv layout
                        x_range = coarse_graphDiv.layout[x_axis_key].range;
                    }
                } else if (mainRelayout[x_axis_key + ".range[0]"] || mainRelayout[y_axis_key + ".range[0]"]) {
                    // a specific range is set
                    performed_update = true;
                }

                update["selections"][i] = getUpdateObj(xy_pair, x_range, y_range);
            }
            performed_update ? Plotly.relayout(coarse_graphDiv, update) : null;
            return coarseFigID;
        },
    },
});



================================================
FILE: tests/__init__.py
================================================
[Empty file]


================================================
FILE: tests/conftest.py
================================================
"""Fixtures and helper functions for testing"""

import os
from typing import Union

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import pytest
from plotly.subplots import make_subplots

from plotly_resampler import (
    LTTB,
    EveryNthPoint,
    FigureResampler,
    unregister_plotly_resampler,
)

# hyperparameters
_nb_samples = 10_000
data_dir = "examples/data/"
headless = True
TESTING_LOCAL = False  # SET THIS TO TRUE IF YOU ARE TESTING LOCALLY


@pytest.fixture
def registering_cleanup():
    # Cleans up the registering before and after each test
    unregister_plotly_resampler()
    yield
    unregister_plotly_resampler()


def _remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


@pytest.fixture
def pickle_figure():
    FIG_PATH = "fig.pkl"
    _remove_file(FIG_PATH)
    yield FIG_PATH
    _remove_file(FIG_PATH)


@pytest.fixture
def driver():
    import time

    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    from seleniumwire import webdriver

    time.sleep(1)

    options = Options()
    d = DesiredCapabilities.CHROME
    d["goog:loggingPrefs"] = {"browser": "ALL"}
    if not TESTING_LOCAL:
        if headless:
            options.add_argument("--headless")
        # options.add_argument("--no=sandbox")
        driver = webdriver.Chrome(
            options=options,
            desired_capabilities=d,
        )
    else:
        options.add_argument("--remote-debugging-port=9222")
        driver = webdriver.Chrome(
            options=options,
            # executable_path="/home/jeroen/chromedriver",
            # executable_path="/home/jonas/Documents/chromedriver-linux64/chromedriver",
            desired_capabilities=d,
        )
        # driver = webdriver.Firefox(executable_path='/home/jonas/git/gIDLaB/plotly-dynamic-resampling/geckodriver')
    return driver


@pytest.fixture
def float_series() -> pd.Series:
    x = np.arange(_nb_samples).astype(np.uint32)
    y = np.sin(x / 50).astype(np.float32) + np.random.randn(_nb_samples) / 5
    return pd.Series(index=x, data=y, name="float_series")


@pytest.fixture
def cat_series() -> pd.Series:
    cats_list = ["a", "a", "a", "a"] * 2000
    for i in np.random.randint(0, len(cats_list), 3):
        cats_list[i] = "b"
    for i in np.random.randint(0, len(cats_list), 3):
        cats_list[i] = "c"
    return pd.Series(
        cats_list * (_nb_samples // len(cats_list) + 1),
        dtype="category",
        name="cat_series",
    )[:_nb_samples]


@pytest.fixture
def bool_series() -> pd.Series:
    bool_list = [True, False, True, True, True, True] + [True] * 1000
    return pd.Series(
        bool_list * (_nb_samples // len(bool_list) + 1),
        dtype="bool",
        name="bool_series",
    )[:_nb_samples]


@pytest.fixture
def example_figure() -> FigureResampler:
    df_gusb = pd.read_parquet(f"{data_dir}df_gusb.parquet")
    df_data_pc = pd.read_parquet(f"{data_dir}df_pc_test.parquet")

    n = 110_000  # _000
    np_series = np.array(
        (3 + np.sin(np.arange(n) / 200_000) + np.random.randn(n) / 10)
        * np.arange(n)
        / 100_000,
        dtype=np.float32,
    )
    x = np.arange(len(np_series))

    fig = FigureResampler(
        make_subplots(
            rows=2,
            cols=2,
            specs=[[{}, {}], [{"colspan": 2}, None]],
            subplot_titles=(
                "GUSB swimming pool",
                "Generated sine",
                "Power consumption",
            ),
            vertical_spacing=0.12,
        ),
        default_n_shown_samples=1_000,
        verbose=False,
    )

    # ------------ swimming pool data -----------
    df_gusb_pool = df_gusb["zwembad"].last("4D").dropna()
    fig.add_trace(
        go.Scattergl(
            x=df_gusb_pool.index,
            y=df_gusb_pool.astype("uint16"),
            mode="markers",
            marker_size=5,
            name="occupancy",
            showlegend=True,
        ),
        hf_hovertext="mean last hour: "
        + df_gusb_pool.rolling("1h").mean().astype(int).astype(str),
        downsampler=EveryNthPoint(),
        row=1,
        col=1,
    )
    fig.update_yaxes(title_text="Occupancy", row=1, col=1)

    # ----------------- generated sine -----------
    fig.add_trace(
        go.Scattergl(name="sin", line_color="#26b2e0"),
        hf_x=x,
        hf_y=np_series,
        row=1,
        col=2,
    )

    # ------------- Power consumption data -------------
    df_data_pc = df_data_pc.last("190D")
    for i, c in enumerate(df_data_pc.columns):
        fig.add_trace(
            go.Scattergl(
                name=f"room {i+1}",
            ),
            hf_x=df_data_pc.index,
            hf_y=df_data_pc[c].astype(np.float32),
            row=2,
            col=1,
            downsampler=LTTB(),
        )

    fig.update_layout(height=600)
    fig.update_yaxes(title_text="Watt/hour", row=2, col=1)
    fig.update_layout(
        title="<b>Plotly-Resampler demo</b>",
        title_x=0.5,
        legend_traceorder="normal",
    )
    return fig


@pytest.fixture
def example_figure_fig() -> go.Figure:
    df_gusb = pd.read_parquet(f"{data_dir}df_gusb.parquet")
    df_data_pc = pd.read_parquet(f"{data_dir}df_pc_test.parquet")

    n = 110_000  # _000
    np_series = np.array(
        (3 + np.sin(np.arange(n) / 200_000) + np.random.randn(n) / 10)
        * np.arange(n)
        / 100_000,
        dtype=np.float32,
    )
    x = np.arange(len(np_series))

    # construct a normal figure object instead of a figureResample object
    fig = make_subplots(
        rows=2,
        cols=2,
        specs=[[{}, {}], [{"colspan": 2}, None]],
        subplot_titles=("GUSB swimming pool", "Generated sine", "Power consumption"),
        vertical_spacing=0.12,
    )

    # ------------ swimming pool data -----------
    df_gusb_pool = df_gusb["zwembad"].last("4D").dropna()
    fig.add_trace(
        go.Scattergl(
            x=df_gusb_pool.index,
            y=df_gusb_pool,  # .astype("uint16"),
            mode="markers",
            marker_size=5,
            name="occupancy",
            showlegend=True,
            hovertext="mean last hour: "
            + df_gusb_pool.rolling("1h").mean().astype(int).astype(str),
        ),
        # downsampler=EveryNthPoint(),
        row=1,
        col=1,
    )
    fig.update_yaxes(title_text="Occupancy", row=1, col=1)

    # ----------------- generated sine -----------
    fig.add_trace(
        go.Scattergl(name="sin", line_color="#26b2e0", x=x, y=np_series),
        row=1,
        col=2,
    )

    # ------------- Power consumption data -------------
    df_data_pc = df_data_pc.last("190D")
    for i, c in enumerate(df_data_pc.columns):
        fig.add_trace(
            go.Scattergl(
                name=f"room {i+1}",
                x=df_data_pc.index,
                y=df_data_pc[c].astype(np.float32),
            ),
            row=2,
            col=1,
        )

    fig.update_layout(height=600)
    fig.update_yaxes(title_text="Watt/hour", row=2, col=1)
    fig.update_layout(
        title="<b>Plotly-Resampler demo - fig base</b>",
        title_x=0.5,
        legend_traceorder="normal",
    )
    return fig


@pytest.fixture
def gsr_figure() -> FigureResampler:
    def groupby_consecutive(
        df: Union[pd.Series, pd.DataFrame], col_name: str = None
    ) -> pd.DataFrame:
        """Merges consecutive `column_name` values in a single dataframe.

        This is especially useful if you want to represent sparse data in a more
        compact format.

        Parameters
        ----------
        df : Union[pd.Series, pd.DataFrame]
            Must be time-indexed!
        col_name : str, optional
            If a dataFrame is passed, you will need to specify the `col_name` on which
            the consecutive-grouping will need to take plase.

        Returns
        -------
        pd.DataFrame
            A new `DataFrame` view, with columns:
            [`start`, `end`, `n_consecutive`, `col_name`], representing the
            start- and endtime of the consecutive range, the number of consecutive samples,
            and the col_name's consecutive values.
        """
        if type(df) == pd.Series:
            col_name = df.name
            df = df.to_frame()

        assert col_name in df.columns

        df_cum = (
            (df[col_name].diff(1) != 0)
            .astype("int")
            .cumsum()
            .rename("value_grp")
            .to_frame()
        )
        df_cum["sequence_idx"] = df.index
        df_cum[col_name] = df[col_name]

        df_grouped = pd.DataFrame(
            {
                "start": df_cum.groupby("value_grp")["sequence_idx"].first(),
                "end": df_cum.groupby("value_grp")["sequence_idx"].last(),
                "n_consecutive": df_cum.groupby("value_grp").size(),
                col_name: df_cum.groupby("value_grp")[col_name].first(),
            }
        ).reset_index(drop=True)
        df_grouped["next_start"] = df_grouped.start.shift(-1).fillna(df_grouped["end"])
        return df_grouped

    df_gsr = pd.read_parquet(f"{data_dir}processed_gsr.parquet")

    fig = FigureResampler(
        make_subplots(
            rows=2,
            cols=1,
            specs=[[{"secondary_y": True}], [{}]],
            shared_xaxes=True,
        ),
        default_n_shown_samples=1_000,
        resampled_trace_prefix_suffix=(
            '<b style="color:blue">[R]</b> ',
            ' <b style="color:red">[R]</b>',
        ),
        verbose=False,
        show_mean_aggregation_size=True,
    )
    fig.update_layout(height=700)

    for c in ["EDA", "EDA_lf_cleaned", "EDA_lf_cleaned_tonic"]:
        fig.add_trace(
            go.Scattergl(name=c), hf_x=df_gsr.index, hf_y=df_gsr[c], row=1, col=1
        )

    df_peaks = df_gsr[df_gsr["SCR_Peaks_neurokit_reduced_acc"] == 1]
    fig.add_trace(
        trace=go.Scattergl(
            x=df_peaks.index,
            y=df_peaks["EDA_lf_cleaned"],
            visible="legendonly",
            mode="markers",
            marker_symbol="cross",
            marker_size=15,
            marker_color="red",
            name="SCR peaks",
        ),
        limit_to_view=True,
    )

    df_grouped = groupby_consecutive(df_gsr["EDA_SQI"])
    df_grouped["EDA_SQI"] = df_grouped["EDA_SQI"].map(bool)
    df_grouped["good_sqi"] = df_grouped["EDA_SQI"].map(int)
    df_grouped["bad_sqi"] = (~df_grouped["EDA_SQI"]).map(int)
    for sqi_col, col_or in [
        ("good_sqi", "#2ca02c"),
        ("bad_sqi", "#d62728"),
    ]:
        fig.add_trace(
            go.Scattergl(
                x=df_grouped["start"],
                y=df_grouped[sqi_col],
                mode="lines",
                line_width=0,
                fill="tozeroy",
                fillcolor=col_or,
                opacity=0.1 if "good" in sqi_col else 0.2,
                line_shape="hv",
                name=sqi_col,
                showlegend=False,
            ),
            max_n_samples=len(df_grouped) + 1,
            downsampler=EveryNthPoint(),
            limit_to_view=True,
            secondary_y=True,
        )

    fig.add_trace(
        go.Scattergl(name="EDA_Phasic", visible="legendonly"),
        hf_x=df_gsr.index,
        hf_y=df_gsr["EDA_Phasic"],
        row=2,
        col=1,
    )

    return fig


@pytest.fixture
def multiple_tz_figure() -> FigureResampler:
    n = 5_050

    dr = pd.date_range("2022-02-14", freq="s", periods=n, tz="UTC")
    dr_v = np.random.randn(n)

    cs = [
        dr,
        dr.tz_localize(None).tz_localize("Europe/Amsterdam"),
        dr.tz_convert("Europe/Brussels"),
        dr.tz_convert("Australia/Perth"),
        dr.tz_convert("Australia/Canberra"),
    ]

    fr_fig = FigureResampler(
        make_subplots(rows=len(cs), cols=1, shared_xaxes=True),
        default_n_shown_samples=500,
        convert_existing_traces=False,
        verbose=True,
        show_mean_aggregation_size=False,
    )
    fr_fig.update_layout(height=min(700, 250 * len(cs)))

    for i, date_range in enumerate(cs, 1):
        fr_fig.add_trace(
            go.Scattergl(name=date_range.dtype.name.split(", ")[-1]),
            hf_x=date_range,
            hf_y=dr_v,
            row=i,
            col=1,
        )
    return fr_fig


@pytest.fixture
def cat_series_box_hist_figure() -> FigureResampler:
    # Create a categorical series, with mostly a's, but a few sparse b's and c's
    cats_list = np.array(list("aaaaaaaaaa" * 1000))
    cats_list[np.random.choice(len(cats_list), 100, replace=False)] = "b"
    cats_list[np.random.choice(len(cats_list), 50, replace=False)] = "c"
    cat_series = pd.Series(cats_list, dtype="category")

    x = np.arange(_nb_samples).astype(np.uint32)
    y = np.sin(x / 300).astype(np.float32) + np.random.randn(_nb_samples) / 5
    float_series = pd.Series(index=x, data=y)

    base_fig = make_subplots(
        rows=2,
        cols=2,
        specs=[[{}, {}], [{"colspan": 2}, None]],
    )
    fig = FigureResampler(base_fig, default_n_shown_samples=1000, verbose=True)

    fig.add_trace(
        go.Scattergl(name="cat_series", x=cat_series.index, y=cat_series),
        row=1,
        col=1,
        hf_hovertext="text",
    )

    fig.add_trace(go.Box(x=float_series.values, name="float_series"), row=1, col=2)
    fig.add_trace(
        go.Box(x=float_series.values**2, name="float_series**2"), row=1, col=2
    )

    # add a not hf-trace
    fig.add_trace(
        go.Histogram(
            x=float_series,
            name="float_series",
        ),
        row=2,
        col=1,
    )
    return fig


@pytest.fixture
def shared_hover_figure() -> FigureResampler:
    fig = FigureResampler(make_subplots(rows=3, cols=1, shared_xaxes=True), verbose=1)

    x = np.array(range(100_000))
    y = np.sin(x / 120) + np.random.random(len(x)) / 10

    for i in range(1, 4):
        fig.add_trace(go.Scatter(x=[], y=[]), hf_x=x, hf_y=y, row=i, col=1)

    fig.update_layout(template="plotly_white", height=900)
    fig.update_traces(xaxis="x3")
    fig.update_xaxes(spikemode="across", showspikes=True)

    return fig


@pytest.fixture
def multi_trace_go_figure() -> FigureResampler:
    fig = FigureResampler(go.Figure())

    n = 500_000  # nb points per sensor
    x = np.arange(n)
    y = np.sin(x / 20) + np.random.random(len(x)) / 10

    for i in range(30):  # 30 sensors
        fig.add_trace(
            go.Scattergl(name=str(i)),
            hf_x=x,
            hf_y=y + i,
        )
    fig.update_layout(height=800)
    return fig



================================================
FILE: tests/fr_selenium.py
================================================
# -*- coding: utf-8 -*-
"""
Selenium wrapper class withholding methods for testing the plolty-figureResampler.

.. note::
    Headless mode is enabled by default.

"""

from __future__ import annotations

__author__ = "Jonas Van Der Donckt, Jeroen Van Der Donckt"

import json
import time
from typing import List, Union

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire import webdriver
from seleniumwire.request import Request

# Note: this will be used to add more waiting time to windows & mac os tests as
# - on these OS's serialization of the figure is necessary (to start the dash app in a
#    multiprocessing.Process)
#    https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods
# - on linux, the browser (i.e., sending & getting requests) goes a lot faster
from .utils import not_on_linux

# https://www.blazemeter.com/blog/improve-your-selenium-webdriver-tests-with-pytest
# and create a parameterized driver.get method


class RequestParser:
    @staticmethod
    def filter_callback_requests(requests: List[Request]) -> List[Request]:
        valid_requests = []
        for r in requests:
            if r.method.upper() != "POST":
                # note; the `_reload_hash` GET request will thus be filtered out
                continue

            if not r.url.endswith("_dash-update-component"):
                continue

            valid_requests.append(r)
        return valid_requests

    def assert_fetch_data_request(
        data_request: Request, relayout_keys: List[str], n_updated_traces: int
    ):
        """Withholds checks for the relayout-data fetch request

        Parameters
        ----------
        data_request : Request
            The relayout data fetch request, with
            * Request body: the relayout changes
            * Response body: a list of dicts with first tiem
        relayout_keys : List[str]
            The expected keys to be found in the relayout command
        n_updated_traces : int
            The expected amount of traces which will be updated.

        """
        fetch_data_body = json.loads(data_request.body)
        assert "inputs" in fetch_data_body and len(fetch_data_body["inputs"]) == 1
        # verify that the request is triggered by the relayoutData
        figure_id = "resample-figure"
        assert fetch_data_body["inputs"][0]["id"] == figure_id
        assert fetch_data_body["inputs"][0]["property"] == "relayoutData"
        assert all(k in fetch_data_body["inputs"][0]["value"] for k in relayout_keys)
        # verify that the response is a list of dicts
        fetch_data_response_body = json.loads(data_request.response.body)["response"]
        # convert the updateData to a list of dicts
        updateData = fetch_data_response_body[figure_id]["figure"]["operations"]
        updated_traces = list(set(d["location"][1] for d in updateData))

        updated_x_keys = set(
            map(
                lambda d: d["location"][1],
                (filter(lambda x: x["location"][-1] == "x", updateData)),
            )
        )
        updated_y_keys = set(
            map(
                lambda d: d["location"][1],
                (filter(lambda x: x["location"][-1] == "y", updateData)),
            )
        )

        assert n_updated_traces == len(updated_traces)

        # verify that there are x and y updates for each trace
        assert len(updated_x_keys) == len(updated_y_keys) == n_updated_traces

    def assert_front_end_relayout_request(relayout_request: Request):
        relayout_body = json.loads(relayout_request.body)
        assert "inputs" in relayout_body and len(relayout_body["inputs"]) == 1
        assert relayout_body["inputs"][0]["id"] == "resample-figure"
        assert relayout_body["inputs"][0]["property"] == "relayoutData"
        assert all(
            k in relayout_body["inputs"][0]["value"]
            for k in ["annotations", "template", "title", "legend", "xaxis", "yaxis"]
        )

        relayout_response_body = json.loads(relayout_request.response.body)["response"]
        # the relayout response its updateData should be an empty dict
        # { "response": { "trace-updater": { "updateData": [ {} ] } } }
        updateData = relayout_response_body["trace-updater"]["updateData"]
        assert len(updateData) == 1
        assert updateData[0] == {}

    def browser_independent_single_callback_request_assert(
        fr: FigureResamplerGUITests, relayout_keys: List[str], n_updated_traces: int
    ):
        """Verifies the callback requests on a browser-independent manner

        fr: FigureResamplerGUITests
            used for determining the browser-type.
        requests: List[Request]
            The captured requests of a SINGLE INTERACTION CALLBACK
        relayout_keys : List[str]
            The expected keys to be found in the relayout command
        n_updated_traces : int
            The expected amount of traces which will be updated.

        """
        # First, filter the requests to only retain the relevant ones
        requests = RequestParser.filter_callback_requests(fr.get_requests())

        browser_name = fr.driver.capabilities["browserName"]
        if "firefox" in browser_name:
            # There are 2 requests which are send
            # 1. first: changed-layout to server -> new data to back-end request
            # 2. the front-end relayout request
            assert len(requests) >= 1, f"len(requests) = {len(requests)}"
            if len(requests) == 2:
                fetch_data_request, relayout_request = requests
                # RequestParser.assert_front_end_relayout_request(relayout_request)
            else:
                fetch_data_request = requests[0]

        elif "chrome" in browser_name:
            # for some, yet unknown reason, chrome does not seem to capture the
            # second front-end request.
            assert len(requests) == 1, f"len(requests) = {len(requests)}"
            fetch_data_request = requests[0]
        else:
            raise ValueError(f"invalid browser name {browser_name}")

        # Validate the update-data-callback request
        RequestParser.assert_fetch_data_request(
            fetch_data_request,
            relayout_keys=relayout_keys,
            n_updated_traces=n_updated_traces,
        )


class FigureResamplerGUITests:
    """Wrapper for performing figure-resampler GUI."""

    def __init__(self, driver: webdriver, port: int):
        """Construct an instance of A firefox selenium driver to fetch wearable data.

        Parameters
        ----------
        username : str
            The e4connect login username.
        password : str
            The e4connect password.
        save_dir : str
            The directory in which the data elements will be saved.
        headless: bool, default: True
            If set to `True` the driver will be ran in a headless mode.

        """
        self.port = port
        self.driver: Union[webdriver.Firefox, webdriver.Chrome] = driver
        self.on_page = False

    def go_to_page(self):
        """Navigate to FigureResampler page."""
        time.sleep(1)
        self.driver.get("http://localhost:{}".format(self.port))
        self.on_page = True
        if not_on_linux():
            time.sleep(7)  # bcs serialization of multiprocessing
        max_nb_tries = 3
        for _ in range(max_nb_tries):
            try:
                self.driver.find_element_by_id("resample-figure")
                break
            except Exception:
                time.sleep(5)

    def clear_requests(self, sleep_time_s=1):
        time.sleep(sleep_time_s)
        del self.driver.requests

    def get_requests(self, delete: bool = True):
        if not_on_linux():
            time.sleep(2)  # bcs slower browser
        requests = self.driver.requests
        if delete:
            self.clear_requests()

        return requests

    def drag_and_zoom(self, div_classname, x0=0.25, x1=0.5, y0=0.25, y1=0.5):
        """
        Drags and zooms the div with the given classname.

        Parameters
        ----------
        div_classname : str
            The classname of the div to be dragged and zoomed.
        x0 : float, default: 0.5
            The relative x-coordinate of the upper left corner of the div.
        x1 : float, default: 0.5
            The relative x-coordinate of the lower right corner of the div.
        y0 : float, default: 0.5
            The relative y-coordinate of the upper left corner of the div.
        y1 : float, default: 0.5
            The relative y-coordinate of the lower right corner of the div.

        """
        if not self.on_page:
            self.go_to_page()

        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, div_classname))
        )

        subplot = self.driver.find_element(By.CLASS_NAME, div_classname)
        size = subplot.size
        w, h = size["width"], size["height"]

        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(subplot, xoffset=w * x0, yoffset=h * y0)
        actions.click_and_hold()
        actions.pause(0.2)
        actions.move_by_offset(xoffset=w * (x1 - x0), yoffset=h * (y1 - y0))
        actions.pause(0.2)
        actions.release()
        actions.pause(0.2)
        actions.perform()

    def _get_modebar_btns(self):
        if not self.on_page:
            self.go_to_page()

        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, "modebar-group"))
        )
        return self.driver.find_elements(By.CLASS_NAME, "modebar-btn")

    def autoscale(self):
        for btn in self._get_modebar_btns():
            data_title = btn.get_attribute("data-title")
            if data_title == "Autoscale":
                ActionChains(self.driver).move_to_element(btn).click().perform()
                return

    def reset_axes(self):
        for btn in self._get_modebar_btns():
            data_title = btn.get_attribute("data-title")
            if data_title == "Reset axes":
                ActionChains(self.driver).move_to_element(btn).click().perform()
                return

    def click_legend_item(self, legend_name):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, "modebar-group"))
        )
        for legend_item in self.driver.find_elements(By.CLASS_NAME, "legendtext"):
            if legend_name in legend_item.get_attribute("data-unformatted"):
                # move to the center of the item and click it
                (
                    ActionChains(self.driver)
                    .move_to_element(legend_item)
                    .pause(0.1)
                    .click()
                    .perform()
                )
                return

    # ------------------------------ DATA MODEL METHODS  ------------------------------
    def __del__(self):
        self.driver.close()



================================================
FILE: tests/test_aggregators.py
================================================
import numpy as np
import pandas as pd
import pytest
from pytest_lazyfixture import lazy_fixture as lf

from plotly_resampler.aggregation import (
    LTTB,
    EveryNthPoint,
    FuncAggregator,
    MedDiffGapHandler,
    MinMaxAggregator,
    MinMaxLTTB,
    MinMaxOverlapAggregator,
    NoGapHandler,
)

from .utils import construct_index, wrap_aggregate


# ------------------------------- DatapointSelector ----------------------------------
@pytest.mark.parametrize(
    "downsampler",
    [
        # NOTE:-> the current LTTB based aggregators need an `x`
        # LTTB,  MinMaxLTTB,
        EveryNthPoint,
        MinMaxAggregator,
        MinMaxOverlapAggregator,
    ],
)
# NOTE: -> categorical series it's values is not of dtype array; but the
# PlotlyAggregatorParser is able to deal with this
@pytest.mark.parametrize("series", [lf("float_series"), lf("bool_series")])
def test_arg_downsample_no_x(series, downsampler):
    for n in np.random.randint(100, len(series), 6):
        # make sure n is even (required for MinMax downsampler)
        n = n - (n % 2)
        indices = downsampler().arg_downsample(series.values, n_out=n)
        assert len(indices) <= n + (n % 2)


@pytest.mark.parametrize(
    "downsampler",
    [
        LTTB,
        MinMaxLTTB,
        EveryNthPoint,
        MinMaxAggregator,
        MinMaxOverlapAggregator,
    ],
)
@pytest.mark.parametrize("series", [lf("float_series"), lf("bool_series")])
@pytest.mark.parametrize(
    "index_type", ["range", "datetime", "timedelta", "float", "int"]
)
def test_arg_downsample_x(series, downsampler, index_type):
    series = series.copy()
    series.index = construct_index(series, index_type)
    for n_out in np.random.randint(100, len(series), 6):
        # make sure n is even (required for MinMax downsampler)
        n_out = n_out - (n_out % 2)
        indices = downsampler().arg_downsample(
            series.index.values, series.values, n_out=n_out
        )
        assert len(indices) <= n_out + (n_out % 2)


@pytest.mark.parametrize(
    "downsampler",
    [EveryNthPoint, LTTB, MinMaxAggregator, MinMaxLTTB, MinMaxOverlapAggregator],
)
@pytest.mark.parametrize("series", [lf("float_series"), lf("bool_series")])
@pytest.mark.parametrize(
    "index_type", ["range", "datetime", "timedelta", "float", "int"]
)
def test_arg_downsample_empty_series(downsampler, series, index_type):
    series = series.copy()
    series.index = construct_index(series, index_type)
    empty_series = series.iloc[0:0]
    idxs = downsampler().arg_downsample(
        empty_series.index.values, empty_series.values, n_out=1_000
    )
    assert len(idxs) == 0


@pytest.mark.parametrize(
    "downsampler",
    [EveryNthPoint, MinMaxAggregator, MinMaxLTTB, MinMaxOverlapAggregator],
)
@pytest.mark.parametrize("series", [lf("float_series"), lf("bool_series")])
def test_arg_downsample_no_x_empty_series(downsampler, series):
    empty_series = series.iloc[0:0]
    idxs = downsampler().arg_downsample(empty_series.values, n_out=1_000)
    assert len(idxs) == 0


@pytest.mark.parametrize(
    "downsampler",
    [EveryNthPoint, LTTB, MinMaxAggregator, MinMaxLTTB, MinMaxOverlapAggregator],
)
@pytest.mark.parametrize("gap_handler", [MedDiffGapHandler, NoGapHandler])
@pytest.mark.parametrize(
    "series",
    [lf("float_series"), lf("cat_series"), lf("bool_series")],
)
@pytest.mark.parametrize(
    "index_type", ["range", "datetime", "timedelta", "float", "int"]
)
def test_wrap_aggregate(downsampler, gap_handler, series, index_type):
    series = series.copy()
    series.index = construct_index(series, index_type)
    np.random.seed(42)
    for n in np.random.randint(100, len(series) // 2, 6):
        # make sure n is even (required for MinMax downsampler)
        n = n - (n % 2)
        x_agg, y_agg, indices = wrap_aggregate(
            hf_x=series.index,
            hf_y=series.values,
            downsampler=downsampler(),
            gap_handler=gap_handler(),
            n_out=n,
        )
        assert not pd.Series(y_agg).isna().any()
        assert len(x_agg) == len(y_agg) == len(indices)
        assert len(y_agg) <= n + (n % 2)


@pytest.mark.parametrize(
    "downsampler",
    [EveryNthPoint, LTTB, MinMaxAggregator, MinMaxLTTB, MinMaxOverlapAggregator],
)
@pytest.mark.parametrize("gap_handler", [MedDiffGapHandler, NoGapHandler])
@pytest.mark.parametrize("series", [lf("float_series"), lf("bool_series")])
@pytest.mark.parametrize(
    "index_type", ["range", "datetime", "timedelta", "float", "int"]
)
def test_wrap_aggregate_empty_series(downsampler, gap_handler, series, index_type):
    empty_series = series.copy()
    empty_series.index = construct_index(empty_series, index_type)
    empty_series = empty_series.iloc[0:0]
    x_agg, y_agg, indices = wrap_aggregate(
        hf_x=empty_series.index,
        hf_y=empty_series.values,
        downsampler=downsampler(),
        gap_handler=gap_handler(),
        n_out=1000,
    )
    assert len(x_agg) == len(y_agg) == len(indices) == 0


@pytest.mark.parametrize(
    "downsampler",
    [EveryNthPoint, LTTB, MinMaxAggregator, MinMaxLTTB, MinMaxOverlapAggregator],
)
@pytest.mark.parametrize(
    "series", [lf("float_series"), lf("bool_series"), lf("cat_series")]
)
def test_wrap_aggregate_x_gaps(downsampler, series):
    series = series.copy()
    # Create a range-index with some gaps in it
    idx = np.arange(len(series))
    idx[1000:] += 1000
    idx[2000:] += 1500
    idx[8000:] += 2500
    series.index = idx

    x_agg, y_agg, indices = wrap_aggregate(
        hf_x=series.index,
        hf_y=series.values,
        downsampler=downsampler(),
        gap_handler=MedDiffGapHandler(),
        n_out=100,
    )
    assert len(x_agg) == len(y_agg) == len(indices)
    assert pd.Series(y_agg).isna().sum() >= 3


@pytest.mark.parametrize(
    "downsampler",
    [EveryNthPoint, LTTB, MinMaxAggregator, MinMaxLTTB, MinMaxOverlapAggregator],
)
@pytest.mark.parametrize("series", [lf("float_series")])
def test_wrap_aggregate_x_gaps_float_fill_value(downsampler, series):
    idx = np.arange(len(series))
    idx[1000:] += 1000
    idx[2000:] += 1500
    idx[8000:] += 2500
    series.index = idx
    # 1. test with the default fill value (i.e., None)
    x_agg, y_agg, indices = wrap_aggregate(
        hf_x=series.index,
        # add a constant to the series to ensure that the fill value is not used
        hf_y=series.values + 1000,
        downsampler=downsampler(),
        gap_handler=MedDiffGapHandler(),
        n_out=100,
    )
    assert len(x_agg) == len(y_agg) == len(indices)
    assert pd.Series(y_agg).isnull().sum() == 3
    # 2. test with a custom default fill value (i.e., 0)
    x_agg, y_agg, indices = wrap_aggregate(
        hf_x=series.index,
        # add a constant to the series to ensure that the fill value is not used
        hf_y=series.values + 1000,
        downsampler=downsampler(),
        gap_handler=MedDiffGapHandler(fill_value=0),
        n_out=100,
    )
    assert len(x_agg) == len(y_agg) == len(indices)
    assert pd.Series(y_agg == 0).sum() == 3


@pytest.mark.parametrize(
    "downsampler", [EveryNthPoint, LTTB, MinMaxLTTB, MinMaxOverlapAggregator]
)
@pytest.mark.parametrize("gap_handler", [MedDiffGapHandler, NoGapHandler])
@pytest.mark.parametrize(
    "series", [lf("float_series"), lf("bool_series"), lf("cat_series")]
)
def test_wrap_aggregate_range_index_data_point_selection(
    downsampler, gap_handler, series
):
    series = series.copy()
    series.index = pd.RangeIndex(start=-20_000, stop=-20_000 + len(series))
    x_agg, y_agg, indices = wrap_aggregate(
        hf_x=series.index,
        hf_y=series.values,
        downsampler=downsampler(),
        gap_handler=gap_handler(),
        n_out=100,
    )
    assert len(x_agg) == len(y_agg) == len(indices)
    assert x_agg[0] == -20_000


# ------------------------------- NAN handling -------------------------------
@pytest.mark.parametrize("downsampler", [MinMaxLTTB, MinMaxAggregator])
@pytest.mark.parametrize("series", [lf("float_series")])
def test_nan_behavior(series, downsampler):
    series = series.copy()
    series.iloc[1 + np.random.choice(len(series) - 2, 100, replace=False)] = np.nan

    # OMIT -> no NaNs in the output
    for n in np.random.randint(100, len(series), 6):
        x_agg, y_agg, indices = wrap_aggregate(
            hf_x=series.index,
            hf_y=series.values,
            downsampler=downsampler(nan_policy="omit"),
            gap_handler=NoGapHandler(),
            n_out=100,
        )
        assert not pd.Series(y_agg).isna().any()
        assert len(x_agg) == len(y_agg) == len(indices)
        assert len(y_agg) <= n + (n % 2)

    # KEEP -> NaN will be returned in the output
    for n in np.random.randint(100, len(series), 6):
        x_agg, y_agg, indices = wrap_aggregate(
            hf_x=series.index,
            hf_y=series.values,
            downsampler=downsampler(nan_policy="keep"),
            gap_handler=NoGapHandler(),
            n_out=100,
        )
        assert pd.Series(y_agg).isna().any()
        assert len(x_agg) == len(y_agg) == len(indices)
        assert len(y_agg) <= n + (n % 2)

    ## INVALID nan_policy -> should raise a ValueError
    with pytest.raises(ValueError):
        wrap_aggregate(
            hf_x=series.index,
            hf_y=series.values,
            downsampler=downsampler(nan_policy="invalid"),
            gap_handler=NoGapHandler(),
            n_out=100,
        )


# # ------------------------------- DataAggregator -------------------------------
@pytest.mark.parametrize("agg_func", [np.mean])  # np.median, sum])
@pytest.mark.parametrize("series", [lf("float_series"), lf("bool_series"