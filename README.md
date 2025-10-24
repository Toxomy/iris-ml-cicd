# Iris ML Classification Project

A simple machine learning project for classifying Iris flowers using Random Forest.

## Features
- Train Random Forest classifier on Iris dataset
- Save/load trained model
- Make predictions
- Unit tests included

## Installation
```bash
pip install -r requirements.txt
```

## Usage

Train model and make prediction:
```bash
python app.py
```

Run tests:
```bash
python -m pytest test_app.py -v
```

## Docker

Build image:
```bash
docker build -t iris-ml-app .
```

Run container:
```bash
docker run iris-ml-app
```