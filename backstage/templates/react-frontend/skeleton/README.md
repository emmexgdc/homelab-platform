# ${{ values.appName }}

React frontend generated from the homelab platform template.

## Run locally

```bash

npm install

npm run dev

npm run build


docker build -t ${{ values.appName }}:local .
docker run --rm -p 8080:8080 ${{ values.appName }}:local

 GET /healthz