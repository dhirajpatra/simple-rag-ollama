# Dockerfile for Ollama server
# Use official Ollama image
FROM ollama/ollama:latest

# Install Python and dependencies
RUN apt-get update && apt-get install -y python3 python3-pip curl && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files from build context (./ollama_server)
COPY requirements.txt ollama_server.py entrypoint.sh /app/

# Ensure entrypoint script is executable
RUN chmod +x /app/entrypoint.sh

# Install Python dependencies
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Define entrypoint
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]


