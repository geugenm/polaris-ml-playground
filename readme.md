# Polaris

![Polaris logo](img/polaris_logo_small.png "Polaris")

Python3 tool to analyze a satellite set of telemetry to understand links/dependencies among different subsystems. The telemetry is currently retrieved from the [SatNOGS Network](https://network.satnogs.org/).

If you want to **know more**:

- read the [project wiki](https://gitlab.com/librespacefoundation/polaris/polaris/wikis/Home)

- read the blog post [Analyzing Lightsail-2 Telemetry with Polaris](https://blog.crespum.eu/analyzing-lightsail-2-telemetry-with-polaris/)

## Project structure

``` BASH
contrib/               - code that is not directly dependent on Polaris, but is used in the project
docs/                  - Some documentation on the project (though more is in the wiki)
polaris/               - Project source code
    anomaly/           - modules to detect anomaly in telemetry
    batch/             - Module to perform batch operations
    common/            - Modules common to all of Polaris
    convert/           - Module to convert graph output from learn to other file formats
    fetch/             - Module to fetch and prepare data for the analysis
    learn/             - Module to generate the dependency graph
    reports/           - Module to visualize the anomaly detection
    polaris.py         - Polaris entry point
```

## Installation

```bash
pip3 install .
```

We recommend to install it inside a Python virtual environment:

```bash
# Create the virtual env
$ python3 -m venv .venv

# Activate it
$ source .venv/bin/activate

# Upgrade Pip before installing Polaris
$ (.venv) pip install --upgrade pip

# Install Polaris from Pypi
$ (.venv) pip install polaris-ml
```

**Note:** If you run into problems installing Polaris via pip, **make
sure you've upgraded pip itself** and are using a clean, new, separate
virtual environment -- this solves most problems.

## Running the code

```bash
$ (.venv) polaris --help
Usage: polaris [OPTIONS] COMMAND [ARGS]...

  Tool for analyzing satellite telemetry

Options:
  --version   Show the version and exit.
  --help      Show this message and exit.

Commands:
  batch     Run polaris commands in batch mode
  behave    Detect anomalies and output reports of it
  convert   Convert polaris graph file (supported formats: gexf)
  fetch     Download data set(s)
  learn     Analyze data
  report    Show interactive graphs generated from `polaris behave` command

# To fetch and decode data from the SatNOGS network and space weather sources, run:
$ (.venv) polaris fetch -s 2019-08-10 -e 2019-10-5 --cache_dir /tmp/LightSail_2 LightSail-2 /tmp/normalized_frames.json
# Note: this may take some time.

# If the normalizer for your satellite does not exist, you can run polaris fetch
# with the --skip_normalizer flag. The result with and without the normalizer
# (without/with --skip-normalizer) are bound to be slightly different.
# The normalizer is mainly present to give you, the satellite operator, an
# intuitive (SI) value for fields (instead of arbitrarily scaled/shifted
# values). It is easy to create and you can get started with the process using
# the snippet at https://gitlab.com/librespacefoundation/polaris/polaris/-/snippets/2006696
$ (.venv) polaris fetch -s 2019-08-10 -e 2019-10-5 --cache_dir /tmp/LightSail_2 --skip_normalizer LightSail-2 /tmp/normalized_frames.json

# Data will be saved at /tmp/normalized_frames.json
$ (.venv) head /tmp/normalized_frames.json
[
    {
        "time": "2019-09-12 08:14:42",
        "measurement": "",
        "tags": {
            "satellite": "",
            "decoder": "Lightsail2",
            "station": "",
            "observer": "",
            "source": "",
[...]


# To learn from that data, run:
$ (.venv) polaris learn -g /tmp/new_graph.json /tmp/normalized_frames.json
# Note: depending on your hardware, this may take some time.

# Note: `polaris learn` uses your dedicated (CUDA enabled) GPU by default
#       to suppress this behaviour, you can utilise the --force-cpu flag.
$ (.venv) polaris learn -g /tmp/new_graph.json /tmp/normalized_frames.json --force_cpu
```

## Configuring Polaris

It is possible to override the default parameters used in the ai processes of Polaris by your own using configuration files.

- configuration for Learn cross correlation process (generating graph) :

``` JSON
{
  "use_gridsearch": false,
  "random_state": 43,
  "test_size": 0.2,
  "gridsearch_scoring": "neg_mean_squared_error",
  "gridsearch_n_splits": 6,
  "dataset_cleaning_params": {
    "col_max_na_percentage": 100,
    "row_max_na_percentage": 100
    },
  "model_cpu_params": {
    "objective": "reg:squarederror",
    "n_estimators": 81,
    "learning_rate": 0.1,
    "n_jobs": 1,
    "predictor": "cpu_predictor",
    "tree_method": "auto",
    "max_depth": 8
    },
  "model_params": {
    "objective": "reg:squarederror",
    "n_estimators": 80,
    "learning_rate": 0.1,
    "n_jobs": 1,
    "max_depth": 8
    }
}
```

To use it, add the `-l` or `learn_config_file` command line parameter when calling learn:

```bash
$ polaris learn -g /tmp/graph.json /tmp/normalized_frames -l ../xcorr_cfg.json

- configuration for detect anomalies
  ```
  {
    "window_size": 2,
    "stride": 1,
    "optimizer": "adam",
    "loss": "mean_squared_error",
    "metrics": ["MSE"],
    "test_size_fraction": 0.2,
    "number_of_epochs": 20,
    "noise_margin_per": 50,
    "batch_size": 128,
    "network_dimensions": [64, 32],
    "activations": ["relu"],
    "dataset_cleaning_params": {
        "col_max_na_percentage": 100,
        "row_max_na_percentage": 100
    },
  }
  ```

## Batch operations

Batch operations allow automation of repeated steps.  For example:

- running `polaris fetch` so that it fetches the latest data for a particular satellite, then running `polaris learn` to update the model

- running `polaris fetch` and `polaris learn` as part of an integration test

The `polaris batch` command is controlled by a JSON configuration file; an example can be found at `polaris/common/polaris_config.json.EXAMPLE`.

```bash
$ (.venv) polaris batch --config_file polaris/common/polaris_config.json.EXAMPLE
```

## InfluxDB

With the addition of space weather recently, influxdb support has been added to Polaris. To create the required `docker-compose.yml` file and start and stop the docker container, run:

```bash
$ python
>>> from vinvelivaanilai.storage import common

# To create the path
>>> common.create_docker_compose("/path/to/docker-compose.yml", "/path/to/storage")

# To start influxdb
>>> common.start_docker_compose("/path/to/docker-compose.yml")

# To stop influxdb
>>> common.stop_docker_compose("/path/to/docker-compose.yml")
```

To store in and fetch from influxdb use the flags `--store_in_influxdb` and `--fetch_from_influxdb` respectively.

```bash
polaris fetch -s 2019-08-10 -e 2019-10-5 --cache_dir /tmp/LightSail_2 LightSail-2 /tmp/normalized_frames.json --store_in_influxdb
$ polaris fetch -s 2019-08-10 -e 2019-10-5 --cache_dir /tmp/LightSail_2 LightSail-2 /tmp/normalized_frames.json --fetch_from_influxdb
```

## MLflow

Installing Polaris will install MLflow as a dependency. At this time Polaris is using MLflow during the cross check dependencies process, and the database is stored in the current working directory under the mlruns folder.

To view the logs in MLflow, run this command in the directory that holds the `mlruns` folder (by default, this is the project root directory):

```bash
mlflow ui
```

This command will start the tracking ui server at <http://localhost:5000>.

### Working on documentation

Documentation is hosted on readthedocs.io.  We use the [Myst parser](https://myst-parser.readthedocs.io/en/latest/), and write documentation in Markdown.

To work on documentation, install the docs dependencies like so:

``` BASH
# Yes, with the square brackets:
pip install -e .[docs]
```

Documentation files are in the `docs/` directory.  To build the HTML files, run:

``` BASH
cd docs/
make html
```

Generated files will be in the `docs/_build` directory, and can be viewed with your favourite browser.
