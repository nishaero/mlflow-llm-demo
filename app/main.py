import os
from huggingface_hub import login
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
from pydantic import BaseModel
from app.llm_handler import get_llm_response
import mlflow

# Login to Hugging Face
hf_token = os.getenv("HUGGINGFACE_HUB_TOKEN")
if hf_token:
    login(token=hf_token)

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("llm-inference")

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

@app.post("/inference")
def infer(payload: Prompt):
    result = get_llm_response(payload.prompt)
    return {"response": result}

MODEL_NAME = "meta-llama/Meta-Llama-3-8B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_auth_token=True)

# Force GPU and half precision
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True,
    use_auth_token=True
)
model.to("cuda")

generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)

@app.get("/", response_class=HTMLResponse)
async def chat_ui():
    with open("app/chat_ui.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/generate")
async def generate_text(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    output = generator(prompt, max_new_tokens=256)
    response = output[0]["generated_text"]

    with mlflow.start_run():
        mlflow.log_param("prompt", prompt)
        mlflow.log_metric("response_length", len(response))
        mlflow.log_text(response, "response.txt")

    return JSONResponse({"response": response})
