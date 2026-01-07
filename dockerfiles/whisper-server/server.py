from fastapi import FastAPI
import whisper

app = FastAPI()

# Carica modello Whisper all'avvio
model = whisper.load_model("base")

@app.get("/health")
async def health():
    return {"status": "ok", "service": "whisper-server"}

@app.post("/transcribe")
async def transcribe_audio(audio_url: str):
    # TODO: Implement audio transcription
    # Will be completed in API endpoints section
    return {"status": "not_implemented"}
