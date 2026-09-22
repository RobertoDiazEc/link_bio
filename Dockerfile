# Multi-stage Dockerfile for Railway deployment
# Uses uv for fast, reproducible builds from uv.lock

# ---------- Builder stage ----------
FROM python:3.12-slim AS builder

ENV UV_VERSION=0.5.7
ENV PATH="/root/.local/bin/uv:$PATH"

# Install uv
RUN pip install "uv==${UV_VERSION}"

# Create venv
RUN uv venv /app/.venv

# Copy lockfile and pyproject.toml first (better caching)
COPY uv.lock pyproject.toml /app/

# Install dependencies (frozen lockfile, no dev dependencies)
RUN uv sync --frozen --no-dev

# Copy source code
COPY . /app/

# Prepare Reflex (init is needed to validate the app structure)
RUN /app/.venv/bin/reflex init

# Export app for production
RUN /app/.venv/bin/reflex export --backend-only --no-zip

# ---------- Production stage ----------
FROM python:3.12-slim AS production

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /app/.venv /app/.venv

# Copy source code
COPY --from=builder /app /app

# Copy exported frontend (from reflex export)
COPY --from=builder /app/.web /app/.web

# Create required directories
RUN mkdir -p /app/data /app/uploaded_files

# Expose backend port (Railway sets PORT env var)
EXPOSE 8000

# Let Reflex handle shutdown gracefully
STOPSIGNAL SIGTERM

# Run migrations if alembic is set up
CMD ["sh", "-c", "cd /app && (if [ -d alembic ]; then reflex db migrate; fi) && exec reflex run --env prod --backend-only --backend-port ${PORT:-8000} --host 0.0.0.0"]
