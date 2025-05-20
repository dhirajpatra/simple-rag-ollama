#!/bin/bash

# Start Ollama server in background
ollama serve &
OLLAMA_PID=$!

# Model names
EMBED_MODEL="hf.co/CompendiumLabs/bge-base-en-v1.5-gguf"
LANG_MODEL="hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF"

# Function to pull model if not already present
pull_if_missing() {
  local model="$1"
  if ! ollama list | grep -q "$model"; then
    echo "Pulling model: $model"
    ollama pull "$model"
  else
    echo "Model already present: $model"
  fi
}

# Wait until Ollama is available
echo "Waiting for Ollama server to be available..."
until curl -s http://localhost:11434 > /dev/null; do
  echo "Still waiting for Ollama..."
  sleep 2
done
echo "Ollama server is running."

# Pull required models
pull_if_missing "$EMBED_MODEL"
pull_if_missing "$LANG_MODEL"

# Wait for Ollama process
wait $OLLAMA_PID
