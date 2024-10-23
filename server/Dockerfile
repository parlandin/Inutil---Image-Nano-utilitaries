# Etapa 1: Imagem base do Python
FROM python:3.10-slim AS base


WORKDIR /app

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 8000


CMD ["fastapi", "run", "src/main.py", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
