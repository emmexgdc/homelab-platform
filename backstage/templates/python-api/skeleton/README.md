# ${{ values.appName }}

Python FastAPI service generated from the homelab platform template.

## Run locally

```bash

pip install -r requirements.txt

uvicorn app.main:app --host 0.0.0.0 --port 8080

GET /

GET /healthz

GET /metrics

docker build -t ${{ values.appName }}:local .
docker run --rm -p 8080:8080 ${{ values.appName }}:local