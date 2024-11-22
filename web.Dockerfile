FROM python:3.12 AS builder

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt
RUN reflex export --backend-only --no-zip

