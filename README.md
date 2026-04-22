# 🚀 Enterprise DevOps Platform

## 📌 Overview
This project demonstrates a real-world DevOps pipeline by building, containerizing, and deploying a microservice using Docker, Kubernetes, and AWS.

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
Client → Flask App → Docker → Kubernetes → AWS ECR

---

## 📂 Project Structure
enterprise-devops-platform/
├── app/
├── k8s/
├── cicd/
├── terraform/
├── monitoring/

---

## ⚙️ Features
- Flask API
- Dockerized app
- Kubernetes deployment
- AWS ECR integration

---

## 🚀 How to Run

### Run app
```bash
cd app/transaction-service
python app.py
```

### Build Docker
```bash
docker build -t transaction-service .
```

### Push to ECR
```bash
docker tag transaction-service:latest 494459347674.dkr.ecr.us-east-1.amazonaws.com/transaction-service
docker push 494459347674.dkr.ecr.us-east-1.amazonaws.com/transaction-service
```

### Deploy
```bash
kubectl apply -f k8s/
kubectl port-forward svc/transaction-service 8080:80
```

---

## ✅ Output
http://127.0.0.1:8080/health → {"status":"ok"}

---

## 🚀 Next
- CI/CD
- Terraform
- Monitoring
- EKS

