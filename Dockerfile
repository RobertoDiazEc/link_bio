# This Dockerfile is used to deploy a simple single-container Reflex app instance.
FROM python:3.12


# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /app
COPY . .

ENV VIRTUAL_ENV=app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python3.12 -m venv $VIRTUAL_ENV 

# Install app requirements and reflex in the container
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Deploy templates and prepare app
CMD  [ -d alembic ] && reflex db migrate; \
redis-server --daemonize yes && \
exec reflex run --env prod --backend-only