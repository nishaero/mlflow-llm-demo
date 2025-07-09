import time, json
from fastapi import FastAPI
from pydantic import BaseModel
from .llm_runner import generate
from mlflow_utils import start_run
import mlflow

app = FastAPI()

class Prompt(BaseModel):
    prompt: str
    max_tokens: int = 128

@app.post("/query")
def query(body: Prompt):
    with start_run(tags={"model": "Mistral-7B"}) as run:
        t0 = time.time()
        answer = generate(body.prompt, body.max_tokens)
        latency_ms = int((time.time() - t0) * 1000)

        mlflow.log_param("prompt_len", len(body.prompt))
        mlflow.log_metric("latency_ms", latency_ms)
        mlflow.log_metric("answer_tokens", len(answer.split()))

        # save prompt & answer as artifacts
        mlflow.log_text(body.prompt, "prompt.txt")
        mlflow.log_text(answer, "answer.txt")

    return {"answer": answer, "run_id": run.info.run_id}
