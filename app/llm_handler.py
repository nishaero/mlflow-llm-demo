# app/llm_handler.py
import openai
import mlflow
from app.tracing import init_tracing

init_tracing()

def get_llm_response(prompt: str) -> str:
    with mlflow.start_run(run_name="llm_inference"):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message["content"]
