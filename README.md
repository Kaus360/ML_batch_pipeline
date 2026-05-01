# ML Batch Pipeline

A batch processing pipeline for machine learning signals.

## Prerequisites

- python 3.9+
- docker (optional, for containerized run)
- dependencies in `requirements.txt`

## Local Run

To run the pipeline locally, use the following command:

```bash
pip install -r requirements.txt
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
```

## Docker Build

To build the docker image:

```bash
docker build -t ml-batch-pipeline .
```

## Docker Run

To run the pipeline using docker and output the metrics to stdout:

```bash
docker run --rm ml-batch-pipeline
```

## Example Output

The pipeline outputs a `metrics.json` file. Example:

```json
{
  "version": "v1",
  "status": "success",
  "rows_processed": 10000,
  "signal_rate": 0.4925,
  "latency_ms": 125.43
}
```

## Reproducibility

The pipeline ensures deterministic output by accepting a `seed` parameter in the `config.yaml` file. Running the same input data with the same configuration will yield identical metrics on every run.
