# NHS DevOps Data Pipeline — End-to-End Project

## Overview
This project demonstrates a full DevOps pipeline for a healthcare data processing dashboard using NHS prescription data. It includes data engineering, containerization, Kubernetes deployment, CI/CD with ArgoCD, and production deployment on AWS EKS.

---

## 🚀 Project Architecture

- **Data Source**: NHS PCA monthly prescription data (CSV)
- **Data Processing**: Python script using `pandas`
- **Containerization**: Docker
- **Kubernetes**: Deployment & Service manifests
- **CI/CD**: GitHub repo + ArgoCD
- **Infrastructure-as-Code**: Terraform to provision EKS
- **Visualization**: Streamlit dashboard deployed in Kubernetes

---

## 🧱 Tools Used

| Layer             | Tool / Service           |
|------------------|--------------------------|
| Data             | NHS PCA CSV              |
| ETL              | Python, pandas           |
| Containerization | Docker                   |
| Orchestration    | Kubernetes on AWS EKS    |
| IaC              | Terraform                |
| CI/CD            | ArgoCD                   |
| Dashboard        | Streamlit                |
| Cloud Provider   | AWS                      |

---

## 📂 Folder Structure
nhs-devops-pipeline/
├── argo/ # Kubernetes manifests
│ ├── deployment.yaml
│ └── service.yaml
├── dashboard/ # Streamlit app
│ └── streamlit_app.py
├── python/ # Data processing script
│ └── process_nhs_data.py
├── raw/ # Raw CSV files (gitignored)
├── terraform/ # IaC setup for EKS
│ ├── main.tf
│ ├── variables.tf
│ └── outputs.tf
├── Dockerfile
└── README.md


---

## 🧪 How to Run Locally

```bash
# 1. Build Docker image
docker build -t nhs-pipeline .

# 2. Run the container
docker run --rm nhs-pipeline
```

# ☁️ Kubernetes Deployment (via ArgoCD)
```bash
kubectl apply -f argo/deployment.yaml
kubectl apply -f argo/service.yaml
kubectl port-forward svc/argocd-server -n argocd 8080:443
```
# Key Learnings
Full EKS provisioning via Terraform

ArgoCD GitOps workflow setup

Streamlit dashboard containerised and deployed

Practical experience with AWS CLI, kubectl, and streamlit on Kubernetes

# Author
Oluwatobi Oni
DevOps & Cloud Enthusiast
