FROM python:3.12-slim

# Installa yt-dlp e dipendenze
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    pip install --no-cache-dir yt-dlp fastapi uvicorn && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copia server
WORKDIR /app
COPY server.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Esponi porta
EXPOSE 8501

# Avvia server
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8501"]
