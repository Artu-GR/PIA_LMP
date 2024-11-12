# Use the official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /PIA_LMP

# Install system dependencies required for mysqlclient
RUN dnf update && \
    dnf install -y --no-install-recommends \
    gcc \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    default-mysql-client && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose the port
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
