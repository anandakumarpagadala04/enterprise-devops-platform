## Enterprise DevOps Platform

## Overview

This project showcases a production-grade Enterprise DevOps Platform built using AWS, Terraform, Docker, Kubernetes, Jenkins, GitHub Actions, Prometheus, and Grafana.

The platform demonstrates complete end-to-end DevOps implementation—from infrastructure provisioning and application containerization to CI/CD automation, Kubernetes deployment, and real-time monitoring.

The core application is a Python-based Transaction Microservice that exposes REST APIs for transaction processing and health monitoring. The application is deployed on AWS infrastructure using Docker containers and Kubernetes, with automated deployment pipelines and observability integrated for production-style operations.

---

## Key Implementations

### Infrastructure as Code (Terraform)

* Provisioned AWS VPC, Subnet, Route Tables, Internet Gateway, and Security Groups
* Created and managed EC2 instances using Terraform
* Configured AWS ECR repository for container image storage
* Verified infrastructure state using `terraform plan` and `terraform apply`

### Containerization (Docker)

* Built Docker image for Python Flask Transaction Service
* Managed container lifecycle using Docker
* Exposed application securely using EC2 public IP and custom ports
* Validated deployment using live API requests

### CI/CD Automation (GitHub Actions + Jenkins)

* Implemented GitHub Actions workflows for automated build and deployment
* Configured Jenkins pipelines for deployment automation
* Automated Docker image build and push to container registry
* Reduced manual deployment effort and improved release consistency

### Kubernetes Deployment (K8s / EKS / KIND)

* Deployed application using Kubernetes Deployment and Service manifests
* Configured multiple running pods for high availability
* Implemented NodePort and Port Forwarding for service exposure
* Validated Kubernetes deployment using live GET and POST API requests

### Monitoring & Observability (Prometheus + Grafana)

* Integrated Prometheus for metrics collection
* Configured Node Exporter for infrastructure monitoring
* Built Grafana dashboards for CPU, Memory, Network, and Disk visualization
* Improved operational visibility and incident monitoring

---

## Tech Stack

* AWS (EC2, ECR, VPC, Security Groups)
* Terraform
* Docker
* Kubernetes (EKS / KIND)
* Jenkins
* GitHub Actions
* Prometheus
* Grafana
* Python (Flask)
* Linux (Ubuntu / WSL)
* Git & GitHub
* REST APIs

---

## Architecture Flow

Developer → Git Push → GitHub Actions → Jenkins Pipeline → Docker Build → Container Registry → Kubernetes Deployment → AWS EC2 / Cluster → Prometheus Monitoring → Grafana Dashboard

This architecture simulates a real-world enterprise DevOps workflow used in production environments.

---

## Project Structure

```text
enterprise-devops-platform/
│
├── .github/workflows/        # GitHub Actions CI/CD workflows
├── app/transaction-service/  # Python Flask microservice
├── k8s/                      # Kubernetes deployment and service manifests
├── terraform/                # Infrastructure provisioning using Terraform
├── monitoring/               # Prometheus + Grafana monitoring setup
├── README.md
└── .gitignore
```

---

## Application Features

* Transaction creation using REST APIs
* Health check endpoint for service validation
* Dockerized microservice deployment
* Kubernetes-based scalable deployment
* CI/CD automation for build and deployment
* Real-time monitoring and dashboard visualization
* Infrastructure provisioning using Terraform

---

## Deployment Validation

### GET Request

```bash
GET /transactions
```

### POST Request

```bash
POST /transactions
{
  "amount": 200,
  "type": "debit"
}
```

### Health Check

```bash
GET /health
```

### Sample Output

```json
{
  "message": "Transaction Service Running"
}
```

This confirms successful end-to-end deployment across infrastructure, containers, Kubernetes, and monitoring layers.

---

## Monitoring Dashboard

Grafana dashboards provide visibility into:

* CPU Utilization
* Memory Usage
* Disk Usage
* Network Traffic
* Node Health
* System Uptime

Prometheus continuously collects infrastructure and application metrics for operational monitoring.

---

## Real-World Challenges Solved

* Docker port conflicts during deployment
* GitHub Actions deployment workflow failures
* Jenkins deployment automation issues
* IAM permission troubleshooting during infrastructure setup
* Kubernetes service exposure and networking issues
* Monitoring stack integration and Prometheus datasource validation
* Production debugging and deployment troubleshooting

These challenges provided strong hands-on experience similar to real production DevOps environments.

---

## Business Impact

This project demonstrates how DevOps improves:

* Deployment speed
* Infrastructure reliability
* Release consistency
* Monitoring and incident response
* Production visibility
* Automation efficiency
* System scalability and operational excellence

This reflects the same principles used in enterprise-scale DevOps and Site Reliability Engineering (SRE) teams.

---

## Future Enhancements

* ArgoCD GitOps deployment
* Blue-Green / Canary deployment strategies
* HashiCorp Vault for secrets management
* ELK Stack for centralized logging
* AWS CloudWatch integration
* Auto-scaling and production-grade SRE improvements

---

## Author

Ananda Kumar Pagadala
DevOps Engineer | AWS Cloud | SRE | Platform Engineering

Focused on building scalable, reliable, and production-ready cloud infrastructure.
