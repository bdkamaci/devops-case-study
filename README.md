# DevOps Case Study Project

## Project Overview

This is a DevOps case study demonstrating a CI/CD pipeline for a Python Flask application deployed on Kubernetes.

## Prerequisites

- Python 3.9+
- Docker
- Kubernetes (Minikube/Kind)
- Helm
- ArgoCD

## Local Development Setup

1. Clone the repository
2. Create virtual environment

```python3 -m venv venv```

```source venv/bin/activate```

3. Install dependencies

```pip install -r requirements.txt```

4. Run application

```python app/src/main.py```


## Docker Build

```docker build -t yourusername/devops-case-study:v1 .```

## Kubernetes Deployment

1. Install Helm charts
2. Apply Kubernetes manifests
3. Configure ArgoCD

## CI/CD Pipeline

- GitHub Actions for CI
- ArgoCD for Continuous Deployment
- Supports staging and production environments

## Notes

- Uses External Secrets for credential management
- Implements health checks
- Supports environment-specific configurations#