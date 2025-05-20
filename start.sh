#!/bin/bash

echo "Stopping and removing docker-compose services..."
docker-compose down

echo "Removing dangling images..."
docker image prune -f

echo "Removing dangling containers..."
docker container prune -f

echo "Starting docker-compose services..."
docker-compose up --build --remove-orphans

echo "Waiting for Ollama service to become healthy..."

# Wait for Ollama container to be healthy (timeout 600s)
timeout=600
elapsed=0
while [ $elapsed -lt $timeout ]; do
  health_status=$(docker inspect --format='{{.State.Health.Status}}' $(docker-compose ps -q ollama))
  if [ "$health_status" == "healthy" ]; then
    echo "Ollama is healthy."
    exit 0
  fi
  echo "Waiting... ($elapsed/$timeout seconds)"
  sleep 30
  elapsed=$((elapsed+5))
done

echo "Error: Ollama service did not become healthy in time."
docker-compose logs ollama
docker-compose down
docker image prune -f
docker container prune -f
echo "Please check the logs for more details."
exit 1
