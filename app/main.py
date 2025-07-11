import os
from huggingface_hub import login
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from torch import float16
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, BitsAndBytesConfig

# Authenticate with Hugging Face
hf_token = os.getenv("HUGGINGFACE_HUB_TOKEN")
if hf_token:
    login(token=hf_token)

app = FastAPI()

# Load tokenizer and model
# 🌟 Use smaller LLaMA 8B model with 4-bit quantization
MODEL_NAME = "meta-llama/Meta-Llama-3.1-8B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_auth_token=True)
quant_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype="auto")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=quant_config,
    device_map="auto",
    low_cpu_mem_usage=True,
    use_auth_token=True
    torch_dtype=float16,  # Use float16 for better performance
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
