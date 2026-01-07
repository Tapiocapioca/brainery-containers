# Brainery Containers

Container Docker per il sistema RAG Brainery.

[🇬🇧 English](README.md) | [🇨🇳 中文](README.zh.md)

## Container

| Container | Porta | Scopo |
|-----------|-------|-------|
| **crawl4ai** | 9100 | Web scraping |
| **yt-dlp-server** | 9101 | Trascrizioni YouTube |
| **whisper-server** | 9102 | Trascrizione audio |
| **anythingllm** | 9103 | Database RAG |

**Range porte 9100-9103** ordinato per workflow e usa spazio IANA non assegnato per minimizzare conflitti. Le porte predefinite funzionano out-of-box; override opzionale tramite `.env` disponibile.

## Avvio Rapido

```bash
docker-compose up -d
```

Verifica che i container siano attivi:
```bash
curl http://localhost:9100/health   # crawl4ai
curl http://localhost:9101/health   # yt-dlp-server
curl http://localhost:9102/health   # whisper-server
curl http://localhost:9103/api/ping # anythingllm
```

## Gestione Dati

Brainery usa una **strategia mista** per ottimizzare performance e persistenza:

### 📁 Dati Persistenti (disco host)
- **anythingllm-storage**: Database RAG con documenti ed embeddings
- **whisper-models**: Modelli Whisper pre-scaricati (~150MB)

Location:
- Windows: `C:\ProgramData\Docker\volumes\`
- Linux: `/var/lib/docker/volumes/`

### 💾 Cache Temporanee (RAM)
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

Le porte predefinite (9100-9103) funzionano per la maggior parte degli utenti.

Se hai un conflitto, crea un file `.env`:

```bash
cp .env.example .env
# Modifica le porte nel file .env
docker-compose up -d
```

## Immagini Disponibili

Tutte le immagini sono pubblicate su Docker Hub:
- `tapiocapioca/crawl4ai:latest`
- `tapiocapioca/yt-dlp-server:latest`
- `tapiocapioca/whisper-server:latest`
- `tapiocapioca/anythingllm:latest`

## Documentazione

- **[Guida Installazione](docs/it/installation.md)** - Setup passo-passo
- **[Esempi d'Uso](docs/it/usage.md)** - Esempi pratici

## Versioning

Usa Semantic Versioning: `v1.0.0`, `v1.1.0`, ecc.

## Struttura Repository

- **brainery-containers**: Questo repository (container Docker)
- **brainery**: Skill principale per Claude Code

## Licenza

MIT
