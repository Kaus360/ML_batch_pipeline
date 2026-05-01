# ML Batch Pipeline

A minimal MLOps-style batch processing pipeline that computes a rolling mean signal on OHLCV market data. Built for reproducibility, observability, and deployment readiness.

## Overview

- Loads configuration from YAML (seed, window, version)
- Reads a 10,000-row OHLCV dataset
- Computes a rolling mean on the close price
- Generates a binary signal based on close vs rolling mean
- Outputs structured metrics as JSON
- Logs all processing steps to a log file
- Fully Dockerized for one-command execution

## Project Structure
ML_batch_pipeline/
├── run.py            # main pipeline script
├── config.yaml       # pipeline configuration
├── data.csv          # 10,000-row OHLCV dataset
├── requirements.txt  # python dependencies
├── Dockerfile        # container definition
├── metrics.json      # sample output from successful run
├── run.log           # sample log from successful run
└── README.md

## Requirements

- Python 3.9+
- Docker (for containerized run)

## Local Setup

```bash
pip install -r requirements.txt

python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
```

## Docker Setup

```bash
docker build -t mlops-task .

docker run --rm mlops-task
```

## Configuration

Edit `config.yaml` to adjust pipeline behavior:

```yaml
seed: 42
window: 5
version: "v1"
```

- `seed` — random seed for reproducibility
- `window` — rolling mean window size
- `version` — pipeline version tag included in output

## Output

On success, `metrics.json` contains:

```json
{
  "version": "v1",
  "rows_processed": 10000,
  "metric": "signal_rate",
  "value": 0.4881952781112445,
  "latency_ms": 19,
  "seed": 42,
  "status": "success"
}
```

On failure:

```json
{
  "version": "v1",
  "status": "error",
  "error_message": "description of what went wrong"
}
```

## Reproducibility

All runs with the same `config.yaml` and `data.csv` produce identical outputs. Seed is set via `numpy.random.seed` at startup and is recorded in the metrics output.