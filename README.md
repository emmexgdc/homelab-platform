# Homelab Platform

Internal developer platform playground built for learning platform engineering workflows.

## Features

- Multi-language starter templates

- GitOps manifest generation

- Interactive service scaffolding

- GitHub repository bootstrapping

- GitOps PR automation

- Kubernetes-ready application templates

- Monitoring and secrets integration

## Supported Templates

- typescript-node-api

- react-frontend

- python-fastapi

- golang-api

## Core Workflows

### Create starter only

```bash

make new-starter APP_NAME=my-app TEMPLATE=typescript-node-api

make new-app \
  APP_NAME=my-app \
  PORT=8080 \
  REGISTRY=ghcr.io/emmexgdc

Full platform workflow
./scripts/create-service.sh


Create GitOps PR
make gitops-pr APP_NAME=my-app

Goal

This repo exists to simulate and learn modern platform engineering and internal developer platform workflows using:

* Kubernetes
* ArgoCD
* GitOps
* Backstage
* Golden templates
* Self-service developer tooling