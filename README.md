# Brainery Containers

Docker containers per il sistema RAG Brainery.

## Containers

- **crawl4ai**: Web scraping (porta 11235)
- **anythingllm**: RAG database (porta 3001)
- **yt-dlp-server**: YouTube transcripts (porta 8501)
- **whisper-server**: Audio transcription (porta 8502)

## Quick Start

```bash
docker-compose up -d
```

## Immagini Disponibili

Tutte le immagini sono su Docker Hub:
- `tapiocapioca/crawl4ai:latest`
- `tapiocapioca/anythingllm:latest`
- `tapiocapioca/yt-dlp-server:latest`
- `tapiocapioca/whisper-server:latest`

## Versioning

Usa Semantic Versioning: `v1.0.0`, `v1.1.0`, ecc.

## Repository

- **brainery-containers**: Questo repository (Docker containers)
- **brainery**: Claude Code skill principale

## License

MIT
