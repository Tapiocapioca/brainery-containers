# Brainery Containers

Docker containers for the Brainery RAG system.

[🇮🇹 Italiano](README.it.md) | [🇨🇳 中文](README.zh.md)

## Containers

| Container | Port | Purpose |
|-----------|------|---------|
| **crawl4ai** | 9100 | Web scraping |
| **yt-dlp-server** | 9101 | YouTube transcripts |
| **whisper-server** | 9102 | Audio transcription |
| **anythingllm** | 9103 | RAG database |

**Port range 9100-9103** is workflow-ordered and uses IANA unassigned space to minimize conflicts. Default ports work out-of-box; optional `.env` override available.

## Quick Start

```bash
docker-compose up -d
```

Verify containers are running:
```bash
curl http://localhost:9100/health   # crawl4ai
curl http://localhost:9101/health   # yt-dlp-server
curl http://localhost:9102/health   # whisper-server
curl http://localhost:9103/api/ping # anythingllm
```

## Data Management

Brainery uses a **mixed strategy** to optimize performance and persistence:

### 📁 Persistent Data (host disk)
- **anythingllm-storage**: RAG database with documents and embeddings
- **whisper-models**: Pre-downloaded Whisper models (~150MB)

Location:
- Windows: `C:\ProgramData\Docker\volumes\`
- Linux: `/var/lib/docker/volumes/`

### 💾 Temporary Caches (RAM)
- **crawl4ai**: Web scraping cache (512MB tmpfs)
- **yt-dlp-server**: Temporary video cache (1GB tmpfs)

**Advantages:**
- ✅ High performance (RAM)
- ✅ No disk I/O for caches
- ✅ RAG database preserved across restarts
- ✅ Whisper models not re-downloaded

**RAM requirements:** ~1.5GB dedicated for caches + models in execution

---

## Port Customization

Default ports (9100-9103) work for most users.

If you have a conflict, create a `.env` file:

```bash
cp .env.example .env
# Edit ports in .env file
docker-compose up -d
```

## Available Images

All images are published on Docker Hub:
- `tapiocapioca/crawl4ai:latest`
- `tapiocapioca/yt-dlp-server:latest`
- `tapiocapioca/whisper-server:latest`
- `tapiocapioca/anythingllm:latest`

## Documentation

- **[Installation Guide](docs/en/installation.md)** - Step-by-step setup
- **[Usage Examples](docs/en/usage.md)** - Practical examples

## Versioning

Uses Semantic Versioning: `v1.0.0`, `v1.1.0`, etc.

## Repository Structure

- **brainery-containers**: This repository (Docker containers)
- **brainery**: Main Claude Code skill

## License

MIT
