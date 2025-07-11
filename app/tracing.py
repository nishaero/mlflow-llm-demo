# app/tracing.py
import mlflow

def init_tracing():
    mlflow.set_tracking_uri("http://localhost:5000")  # or remote URI
    mlflow.set_experiment("llm-observability")
    mlflow.openai.autolog()
