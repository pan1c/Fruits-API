###############################################
# Stage 1 – base image with runtime deps only #
###############################################
FROM python:3.13-slim AS base

# Set working directory
WORKDIR /code
ENV PYTHONUNBUFFERED=1

# Install runtime dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Optional: non-root user (used only in prod)
RUN adduser --disabled-password --no-create-home --gecos '' appuser

###############################################
# Stage 2 – test / dev image (extends base)   #
###############################################
FROM base AS test

# Set working directory
ENV PYTHONPATH=/code
# Install dev/test dependencies
COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copy source and tests
COPY app ./app
COPY tests ./tests
COPY setup.cfg .

# Set test entrypoint
CMD ["pytest", "-q"]

###############################################
# Stage 3 – final production image            #
###############################################
FROM base AS prod


COPY app ./app
# Switch to non-root user
USER appuser

EXPOSE 8000

# Run FastAPI via Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
