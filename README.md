# MLflow LLM Demo 🚀

A production-grade deployment example of an LLM-powered FastAPI application, built with CI/CD and deployed on GPU-based infrastructure.

## 🔧 Features

- **FastAPI** + **Transformers** (e.g., Mistral 7B)
- **PyTorch 2.7.1** + **CUDA 12.8** runtime
- **MLflow** logging and tracking
- GitHub Actions pipeline:
  - Builds Docker image
  - Pushes to GHCR
  - (Optional) Deploys via Helm
- Custom RunPod pod template used for GPU inference

## 🔧 Features

- **FastAPI** + **Transformers** (e.g., Mistral 7B)
- **PyTorch 2.7.1** + **CUDA 12.8** runtime
- **MLflow** logging and tracking
- GitHub Actions pipeline:
  - Builds Docker image
  - Pushes to GHCR
  - (Optional) Deploys via Helm
- Custom RunPod pod template used for GPU inference

## 📁 Repo Structure

```
mlflow-llm-demo/
├── Dockerfile
├── requirements.txt
├── app/
│ └── main.py # FastAPI + LLM inference endpoint
├── helm/
│ └── chart/ # Helm chart for Kubernetes deployment
│ ├── templates/
│ │ ├── deployment.yaml
│ │ └── service.yaml
│ └── values.yaml
└── .github/
└── workflows/
└── deploy.yml # CI: build → push → deploy
```


## 🚪 Quick Start

### 1. Set GitHub Secrets

Add these secrets to your GitHub repo (`Settings → Secrets`):

| Name                | Description                                       |
|---------------------|---------------------------------------------------|
| `GHCR_TOKEN`        | GitHub PAT with `write:packages` permission       |
| `HUGGINGFACE_TOKEN` | (Optional) Token for gated HF model access        |

### 2. Update `app/main.py`

Verify that `app/main.py` correctly loads and uses your intended model (e.g., `"mistralai/Mistral-7B-Instruct-v0.2"`), with HF token support baked in.

### 3. Trigger CI/CD

Any push to `main` triggers a build pipeline:

- Builds the Docker image using `pytorch/pytorch:2.7.1-cuda12.8-cudnn9-runtime`
- Pushes the image to GHCR with tag `latest`
- (Optional) Deploys via Helm if configured

Check progress under **Actions → Deploy to RunPod**.

### 4. Deploy on RunPod

Use the following as your **RunPod pod template**:

- **Image**: `ghcr.io/<your_user>/mlflow-llm-demo:latest`
- **GPU**: RTX 4090 / L40S / equivalent
- **Ports**: expose `8080` (FastAPI endpoint)
- **Payload**: includes GPU runtime, hf token already baked in

Once the pod launches:
```bash
curl http://<pod-id>.runpod.dev:8080/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explain AI infrastructure in simple terms."}'
```

---

### 🧩 Section 5: Development Flow

```markdown
## 🚦 Development Flow

1. Edit code or model in `app/main.py`
2. Push code to `main`
3. GitHub Actions builds and pushes updated Docker image
4. Redeploy or restart RunPod pod to pull the new image

You can automate redeployments via:
- A bootstrap script
- RunPod API script inside the pod

## 🛠️ Optional Enhancements

- Deploy Helm chart on k3s inside RunPod (multi-service, ingress, volumes)
- Integrate **MLflow server** inside the container
- Add **logging & metrics** (Prometheus, Grafana, MLflow metrics)
- Add **Swagger UI** via FastAPI metadata

## 👤 Credits

Built and maintained by [@nishaero](https://github.com/nishaero)  
Designed for DevOps/ML engineers as a pathway to **AI‑infra architect** roles
