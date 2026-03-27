# 🚀 Enterprise DevOps Platform

## 📌 Overview
This project demonstrates a real-world DevOps pipeline by building, containerizing, and deploying a microservice using Docker, Kubernetes, and AWS.

It simulates a production-ready workflow including image management with AWS ECR and secure deployment using Kubernetes.

---

## 🛠 Tech Stack
- Python (Flask)
- Docker
- Kubernetes
- AWS ECR
- GitHub
- Linux (WSL)

---

## 🏗 Architecture
Client → Flask App → Docker Container → Kubernetes Deployment → Service → AWS ECR

---

## 📂 Project Structure
enterprise-devops-platform/
├── app/transaction-service
├── k8s/
├── cicd/
├── terraform/
├── monitoring/
└── README.md


---

## ⚙️ Features
- Flask-based transaction service
- Dockerized application
- Kubernetes deployment with replicas
- Service exposure using port-forwarding
- AWS ECR integration for private image storage
- Kubernetes imagePullSecrets for secure image pulling

---

## 🚀 How to Run

### Run Locally
```bash
cd app/transaction-service
python app.py
