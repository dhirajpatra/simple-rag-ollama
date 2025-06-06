@echo off
REM This batch file stops, prunes, and restarts Docker Compose services.

echo Stopping and removing docker-compose services...
docker-compose down

echo Removing dangling images...
docker image prune -f

echo Removing dangling containers...
docker container prune -f

echo Starting docker-compose services...
docker-compose up --build --remove-orphans

echo Waiting for Ollama service to become healthy...
timeout /t 60 /nobreak
echo Server is up and running.

pause
