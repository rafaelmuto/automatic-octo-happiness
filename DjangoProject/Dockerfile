# Stage 1: Base builder image
# This stage sets up the base environment for building the application
# It uses a slim version of Python 3.10 to keep the image size small.
# It installs necessary build dependencies and sets up the working directory.
FROM python:3.10-slim AS builder

RUN mkdir /app
WORKDIR /app

# Set environment variables to optimize Python behavior
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


# Stage 2: Production image
# This stage creates the final production image by copying the built application
# from the builder stage. It uses a minimal base image to reduce size.
FROM python:3.10-slim

# Copy the Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# RUN useradd -m -r appuser && \
#     mkdir /app && \
#     chown -R appuser /app

RUN mkdir /app

WORKDIR /app

# Copy application code
# COPY --chown=appuser:appuser . .
COPY . .

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# USER appuser

EXPOSE 8000

# Make entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Start the application using Gunicorn
CMD ["/app/entrypoint.sh"]