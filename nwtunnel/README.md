# Calculate the maximum flow of a tunnel system

A simple python program that calculates the maximum flow (capacity)
between two locations in a tunnel system.

## Prerequisites

python >= 2.7

## Run and test

To execute the CLI, run

`python -g <graph file> <start location> <end location>`

Example

```shell
python ./cli.py -g ./sample.json 'Immu Plains' 'Table Bay'
```

To run the unit tests and performance tests:

```shell
python ./test_nwtunnel.py
python ./perf_test.py
```
