# Enterprise DevOps Platform

## Overview
A production-style DevOps project that demonstrates containerization, Kubernetes orchestration, AWS ECR integration, and deployment workflows for a Flask-based transaction service.

## Tech Stack
- Python / Flask
- Docker
- Kubernetes
- AWS ECR
- GitHub Actions
- Terraform
- Prometheus / Grafana

## Project Structure
- app/transaction-service
- k8s/
- cicd/
- terraform/
- monitoring/

## Features
- Flask transaction service
- Dockerized application
- Kubernetes deployment with replicas
- Service exposure and port forwarding
- AWS ECR image push and pull
- Kubernetes imagePullSecrets for private ECR access

## Local Setup
### Run app locally
```bash
cd app/transaction-service
source venv/bin/activate
python app.py
