FROM python:3.12-slim

# Installa dipendenze sistema
RUN apt-get update && \
    apt-get install -y ffmpeg curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Installa Whisper e FastAPI
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia server
COPY server.py .

# Directory per modelli (volume)
RUN mkdir -p /app/models

# Esponi porta
EXPOSE 8502

# Avvia server
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8502"]
