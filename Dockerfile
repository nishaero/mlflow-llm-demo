# CUDA runtime w/ PyTorch
FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
ENV PYTHONPATH=/app

EXPOSE 8080 5000

# Start MLflow UI on :5000 & FastAPI on :8080
CMD bash -c "mlflow ui --port 5000 --host 0.0.0.0 & \
             uvicorn app.main:app --host 0.0.0.0 --port 8080"
