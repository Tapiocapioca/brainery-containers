from fastapi import FastAPI
import yt_dlp

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok", "service": "yt-dlp-server"}

@app.post("/transcript")
async def get_transcript(url: str):
    # TODO: Implement transcript extraction
    # Will be completed in API endpoints section
    return {"status": "not_implemented"}
