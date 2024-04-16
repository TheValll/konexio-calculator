docker compose down
docker build pull --rm -f "dockerfile" -t "cours:latest" "."
docker compose up -d