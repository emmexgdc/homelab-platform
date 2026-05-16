from fastapi import FastAPI, Response
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

app = FastAPI(title="${{ values.appName }}")


@app.get("/")
def root():
    return {
        "app": "${{ values.appName }}",
        "status": "ok"
    }


@app.get("/healthz")
def healthz():
    return {
        "status": "healthy"
    }


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
