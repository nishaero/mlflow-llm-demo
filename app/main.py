import os
from huggingface_hub import login
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, BitsAndBytesConfig

# Authenticate with Hugging Face
hf_token = os.getenv("HUGGINGFACE_HUB_TOKEN")
if hf_token:
    login(token=hf_token)

app = FastAPI()

# Load tokenizer and model
MODEL_NAME = "hugging-quants/Meta-Llama-3.1-70B-Instruct-GPTQ-INT4"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_auth_token=True)
quant_config = BitsAndBytesConfig(load_in_8bit=True)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    torch_dtype="auto",
    low_cpu_mem_usage=True,
    use_auth_token=True
)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Serve HTML UI
@app.get("/", response_class=HTMLResponse)
async def chat_ui():
    with open("app/chat_ui.html", "r", encoding="utf-8") as f:
        return f.read()

# Accept prompt and return model response
@app.post("/generate")
async def generate_text(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    output = generator(prompt, max_new_tokens=256)
    return JSONResponse({"response": output[0]["generated_text"]})
