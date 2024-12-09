# DevOps Case Study Project

## Project Overview
```markdown
This is a DevOps case study showcasing a complete CI/CD pipeline for a Python Flask-based web application. The project demonstrates:
- Containerization with Docker
- Kubernetes deployment using Helm
- Secrets management via External Secrets
- GitOps implementation with ArgoCD
- Automated testing and deployment workflows with GitHub Actions
```

## Prerequisites
```markdown
- Python 3.9+ (for local development)
- Docker (20.10+)
- Kubernetes (Minikube 1.29+ or Kind 0.17+)
- Helm (v3.12+)
- ArgoCD (v2.6+)
- A Kubernetes cluster with sufficient resources
- Vault or a compatible secrets management system for External Secrets
```

## Local Development Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/bdkamaci/devops-case-study.git
   cd devops-case-study

2. Create virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Set environment variables (optional for local testing):
    ```bash
    export APP_ENVIRONMENT=development
    export DB_HOST=localhost

5. Run the application:    
     ```bash
    python app/src/main.py

## Build and Push the Docker Image
    docker build -t ghcr.io/bdkamaci/devops-case-study:v1 .
    docker push ghcr.io/bdkamaci/devops-case-study:v1

## Kubernetes Deployment
1. Install Helm charts:
   ```bash
   helm install myapp helm/app-chart -n development --create-namespace
2. Apply Kubernetes manifests
    ```bash
    kubectl apply -f kubernetes/base
3. Configure ArgoCD
    ```bash
    kubectl apply -f argocd/myapp-application.yml

## CI/CD Pipeline
```markdown
The CI/CD pipeline includes:
- **GitHub Actions**: Automates build, testing, and container image push steps. The workflow is triggered on every commit to the `main` branch.
- **ArgoCD**: Automatically syncs Kubernetes manifests and Helm charts to the cluster, ensuring continuous deployment to staging and production environments.
```

## Testing
1. Run tests locally:
   ```bash
   pytest tests/
2. View coverage reports:
    ```bash
    pytest --cov=app tests/

## Troubleshooting
- **Application Pods Not Ready**:
  Check the logs for errors:
  ```bash
  kubectl logs deployment/myapp

## Notes
```markdown
- Uses External Secrets for credential management
- Implements health checks
- Supports environment-specific configurations
```