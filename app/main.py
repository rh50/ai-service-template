from fastapi import FastAPI
import requests

app = FastAPI()

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/chat")
def chat(prompt: str):
    payload = {
        "model": "qwen2.5:latest",
        "prompt": prompt,
        "stream": False
    }
    resp = requests.post(OLLAMA_URL, json=payload)
    return resp.json()
