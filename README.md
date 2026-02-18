# AI Service (FastAPI + Docker)

一个最简单的 AI API 服务示例，展示如何将本地模型（如 Ollama）封装成可部署的 Docker 服务。

## 功能

- `/ping`：健康检查
- `/chat`：调用本地模型生成回复

## 运行方式

### 1. 构建镜像

```bash
docker build -t ai-service .
