# Brainery Containers

Docker containers per il sistema RAG Brainery.

## Containers

| Container | Porta | Scopo |
|-----------|-------|-------|
| **crawl4ai** | 9100 | Web scraping |
| **yt-dlp-server** | 9101 | YouTube transcripts |
| **whisper-server** | 9102 | Audio transcription |
| **anythingllm** | 9103 | RAG database |

## Quick Start

```bash
docker-compose up -d
```

Verifica che tutto funzioni:
```bash
curl http://localhost:9100/health   # crawl4ai
curl http://localhost:9101/health   # yt-dlp-server
curl http://localhost:9102/health   # whisper-server
curl http://localhost:9103/api/ping # anythingllm
```

## Gestione Dati e Volumi

Brainery usa una **strategia mista** per ottimizzare performance e persistenza:

### 📁 Dati Persistenti (su disco host)
- **anythingllm-storage**: Database RAG con documenti e embeddings
- **whisper-models**: Modelli Whisper pre-scaricati (~150MB)

Location:
- Windows: `C:\ProgramData\Docker\volumes\`
- Linux: `/var/lib/docker/volumes/`

### 💾 Cache Temporanee (in RAM)
- **crawl4ai**: Cache web scraping (512MB tmpfs)
- **yt-dlp-server**: Cache video temporanei (1GB tmpfs)

**Vantaggi:**
- ✅ Performance elevate (RAM)
- ✅ Nessun I/O su disco per cache
- ✅ Database RAG preservato tra restart
- ✅ Modelli Whisper non riscaricati

**Requisiti RAM:** ~1.5GB dedicati a cache + modelli in esecuzione

---

## Personalizzazione Porte

Le porte di default (9100-9103) funzionano per la maggior parte degli utenti.

Se hai un conflitto, crea un file `.env`:

```bash
cp .env.example .env
# Modifica le porte nel file .env
docker-compose up -d
```

## Immagini Disponibili

Tutte le immagini sono su Docker Hub:
- `tapiocapioca/crawl4ai:latest`
- `tapiocapioca/yt-dlp-server:latest`
- `tapiocapioca/whisper-server:latest`
- `tapiocapioca/anythingllm:latest`

## Versioning

Usa Semantic Versioning: `v1.0.0`, `v1.1.0`, ecc.

## Repository

- **brainery-containers**: Questo repository (Docker containers)
- **brainery**: Claude Code skill principale

## License

MIT
