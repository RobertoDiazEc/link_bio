# Multi-stage Dockerfile for Railway deployment
# Uses uv for fast, reproducible builds from uv.lock

# ---------- Builder stage ----------
FROM python:3.12-slim AS builder

ENV UV_VERSION=0.5.7
ENV PATH="/root/.local/bin/uv:$PATH"

# Install uv
RUN pip install "uv==${UV_VERSION}"

WORKDIR /app

# Create venv
RUN uv venv /app/.venv

# Copy all source first (uv sync needs src/ for editable install)
COPY . /app/

# Install dependencies (frozen lockfile, no dev dependencies)
RUN uv sync --frozen --no-dev

# ---------- Production stage ----------
FROM python:3.12-slim AS production

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

# Install system packages (unzip for bun, curl for downloads, ca-certificates for HTTPS)
RUN apt-get update && apt-get install -y --no-install-recommends \
    unzip \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy installed dependencies from builder
COPY --from=builder /app/.venv /app/.venv

# Copy source code
COPY --from=builder /app /app/

# Create required directories
RUN mkdir -p /app/data /app/uploaded_files

# Expose backend port
EXPOSE 8080

# Let Reflex handle shutdown gracefully
STOPSIGNAL SIGTERM

# Run Reflex backend on Railway default port
CMD ["reflex", "run", "--env", "prod", "--backend-only", "--backend-port", "8080"]
