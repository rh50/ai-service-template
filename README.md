# ai-service-template
# AI Service Template (FastAPI + Docker)  一个可复用的 AI 服务模板，用于快速构建基于本地模型（如 Ollama）或云端模型（如 OpenAI API）的 API 服务。  适合作为： - AI 项目脚手架 - Docker 化服务模板 - 工程化能力展示项目 - 本地模型服务化示例  ---  ## 功能  - `/ping`：健康检查 - `/chat`：调用本地模型生成回复（默认使用 Ollama）  ---  ## 快速开始  ### 1. 构建镜像  ```bash docker build -t ai-service-template .
