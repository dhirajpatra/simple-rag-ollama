# Start from the official ollama image
FROM ollama/ollama:latest

# Install curl and any other dependencies
RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy your entrypoint script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Define the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
