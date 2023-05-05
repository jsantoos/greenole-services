# Imagem base
FROM python:3.9


ARG ENV_FILE
ENV ENV_FILE ${ENV_FILE:-.env}
RUN if [ -f "$ENV_FILE" ]; then set -o allexport && source "$ENV_FILE" && set +o allexport; fi


# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos necessários
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install uvicorn
#RUN pip install psycopg2
#RUN pip install psycopg2-binary
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/*


COPY app/ app/

# Definir variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POSTGRES_HOST=${POSTGRES_HOST} \
    POSTGRES_PORT=${POSTGRES_PORT} \
    POSTGRES_DB=${POSTGRES_DB} \
    POSTGRES_USER=${POSTGRES_USER} \
    POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
    DATABASE_URL=${DATABASE_URL} \
    DISCORD_WEBHOOK_URL=${DISCORD_WEBHOOK_URL}

# Define o arquivo .env
COPY ${ENV_FILE} .env


# Expor a porta do app
EXPOSE 5000

# Comando para executar o app
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=5000"]
