# Overview

The aim of the Polaris project is to analyze satellite telemetry in
order to understand links and dependencies among different subsystems,
and between the spacecraft and its context.

It produces a data-driven analysis that should be able to demonstrate
understanding of the links between the different behaviour changes
of each telemetry within a satellite, or within a set of external
sources of information (mission plan, solar aspect angles,
ephemerides, etc.).

Machine learning is used to learn the dependencies and correlations
happening within a spacecraft.  The acquired knowledge is stored in a
dependency graph (e.g. Bayesian network) -- both for analysis, and to
allow operators to examine future changes by comparison against older
versions of the graph.

Polaris is split into the following parts based on function:

- `polaris fetch` will download and normalize satellite telemetry from
  the SatNOGS network (or you can import your own).

- `polaris learn` will analyze the telemetry, produce a model of the
  connections between telemetry components, and save a dependency
  graph for visualization.

- `polaris convert` will convert graph output from `polaris learn` to
  another file format (like `.gexf`).

- `polaris behave` will detect anomalies in telemetry data and produce
  a json report of all the data and any detected anomalies.

- `polaris report` is an interactive, browser-based report of the data
  produced by `polaris behave`.
