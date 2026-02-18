# AI Service Template (FastAPI + Docker)

一个可复用的 AI 服务模板，用于快速构建基于本地模型（如 Ollama）或云端模型（如 OpenAI API）的 API 服务。

适合作为：
- AI 项目脚手架
- Docker 化服务模板
- 工程化能力展示项目
- 本地模型服务化示例

---

## ✨ 功能

- `/ping`：健康检查
- `/chat`：调用本地模型生成回复（默认使用 Ollama）

---

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/你的用户名/ai-service-template.git
cd ai-service-template
```

### 2. 构建镜像

```bash
docker build -t ai-service-template .
```

### 3. 启动服务

```bash
docker run -p 8000:8000 ai-service-template
```

### 4. 测试 API

```bash
curl http://localhost:8000/ping
curl -X POST "http://localhost:8000/chat?prompt=你好"
```

---

## 🐳 使用 docker-compose（可选）

```bash
docker-compose up --build
```

---

## 🧩 技术栈

- FastAPI
- Docker / Dockerfile
- Ollama（或 OpenAI API）
- docker-compose（可选）

---

## 📁 目录结构

```
ai-service-template/
├── app/
│   ├── main.py
│   ├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 📄 许可证

MIT
