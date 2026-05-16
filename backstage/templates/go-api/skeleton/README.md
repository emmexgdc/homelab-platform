# ${{ values.appName }}

Go API service generated from the homelab platform template.

## Run locally

```bash

go run ./cmd/api

GET /
GET /healthz
GET /metrics

docker build -t ${{ values.appName }}:local .
docker run --rm -p 8080:8080 ${{ values.appName }}:local

