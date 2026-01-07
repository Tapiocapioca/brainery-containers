from fastapi import FastAPI
from faster_whisper import WhisperModel

app = FastAPI()

# Carica modello Whisper all'avvio (CPU, ottimizzato)
model = WhisperModel("base", device="cpu", compute_type="int8")

@app.get("/health")
async def health():
    return {"status": "ok", "service": "whisper-server"}

@app.post("/transcribe")
async def transcribe_audio(audio_url: str):
    # TODO: Implement audio transcription
    # Will be completed in API endpoints section
    return {"status": "not_implemented"}
