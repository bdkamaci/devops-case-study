FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ .

# Expose application port
EXPOSE 5000

# Use gunicorn as production WSGI server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]