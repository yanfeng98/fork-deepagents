# Ollama

[Ollama](https://ollama.com/) is the easiest way to get up and running with large language models such as gpt-oss, Gemma 3, DeepSeek-R1, Qwen3 and more.

## Install

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

```bash
pip install ollama
```

## Model

### [nomic-embed-text](https://ollama.com/library/nomic-embed-text)

```bash
ollama pull nomic-embed-text
```

**REST API**

```bash
curl http://localhost:11434/api/embeddings -d '{
  "model": "nomic-embed-text",
  "prompt": "The sky is blue because of Rayleigh scattering"
}'
```