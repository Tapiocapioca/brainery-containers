# Brainery Containers

Brainery RAG 系统的 Docker 容器。

[🇬🇧 English](README.md) | [🇮🇹 Italiano](README.it.md)

## 容器

| 容器 | 端口 | 用途 |
|------|------|------|
| **crawl4ai** | 9100 | 网页抓取 |
| **yt-dlp-server** | 9101 | YouTube 字幕 |
| **whisper-server** | 9102 | 音频转录 |
| **anythingllm** | 9103 | RAG 数据库 |

**端口范围 9100-9103** 按工作流排序，使用 IANA 未分配空间以减少冲突。默认端口开箱即用；可通过 `.env` 文件覆盖。

## 快速开始

```bash
docker-compose up -d
```

验证容器运行状态：
```bash
curl http://localhost:9100/health   # crawl4ai
curl http://localhost:9101/health   # yt-dlp-server
curl http://localhost:9102/health   # whisper-server
curl http://localhost:9103/api/ping # anythingllm
```

## 数据管理

Brainery 使用**混合策略**来优化性能和持久性：

### 📁 持久化数据（主机磁盘）
- **anythingllm-storage**：包含文档和向量的 RAG 数据库
- **whisper-models**：预下载的 Whisper 模型（~150MB）

位置：
- Windows: `C:\ProgramData\Docker\volumes\`
- Linux: `/var/lib/docker/volumes/`

### 💾 临时缓存（RAM）
- **crawl4ai**：网页抓取缓存（512MB tmpfs）
- **yt-dlp-server**：临时视频缓存（1GB tmpfs）

**优势：**
- ✅ 高性能（RAM）
- ✅ 缓存无磁盘 I/O
- ✅ 重启后保留 RAG 数据库
- ✅ Whisper 模型无需重新下载

**RAM 要求：** 约 1.5GB 用于缓存 + 运行中的模型

---

## 端口自定义

默认端口（9100-9103）适用于大多数用户。

如有冲突，创建 `.env` 文件：

```bash
cp .env.example .env
# 在 .env 文件中编辑端口
docker-compose up -d
```

## 可用镜像

所有镜像已发布到 Docker Hub：
- `tapiocapioca/crawl4ai:latest`
- `tapiocapioca/yt-dlp-server:latest`
- `tapiocapioca/whisper-server:latest`
- `tapiocapioca/anythingllm:latest`

## 文档

- **[安装指南](docs/zh/installation.md)** - 分步设置
- **[使用示例](docs/zh/usage.md)** - 实用示例

## 版本控制

使用语义化版本：`v1.0.0`、`v1.1.0` 等。

## 仓库结构

- **brainery-containers**：此仓库（Docker 容器）
- **brainery**：主要的 Claude Code 技能

## 许可证

MIT
