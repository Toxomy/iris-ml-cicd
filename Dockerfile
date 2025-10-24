# Use official Python runtime as base image
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .
COPY test_app.py .

# Run tests during build to ensure quality
RUN python -m pytest test_app.py -v

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "app.py"]