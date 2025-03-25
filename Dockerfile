# This Dockerfile is used to deploy a simple single-container Reflex app instance.
FROM python:3.12


# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /app
COPY . .

ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python3.12 -m venv $VIRTUAL_ENV 

# Install app requirements and reflex in the container
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Deploy templates and prepare app
RUN reflex init

# Needed until Reflex properly passes SIGTERM on backend.
STOPSIGNAL SIGKILL

# Always apply migrations before starting the backend.
#CMD [ -d alembic ] && reflex db migrate;\
#   exec reflex run --env prod --backend-only

#CMD ["bash", "-c", "if [ -d alembic ]; then reflex db migrate;"]
# CMD [ -d alembic ] && reflex db migrate; 
# ENTRYPOINT ["reflex", "run", "--env", "prod", "--backend-only", "--loglevel", "debug" ]  
# Copia start.sh al contenedor
COPY start.sh /app/start.sh

# Asegúrate de que sea ejecutable
RUN chmod +x /app/start.sh

# Configura el script como el comando principal
CMD ["bash", "/app/start.sh"]  