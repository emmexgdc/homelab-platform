# ${{ values.appName }}
TypeScript Node.js API generated from the homelab IDP starter template.
## Run locally
```bash
npm install
npm run dev

Build

npm run build

Start

npm start

Endpoints

GET /
GET /healthz
GET /metrics

Docker

docker build -t ${{ values.appName }}:local .
docker run --rm -p 8080:8080 ${{ values.appName }}:local