import os
from huggingface_hub import login
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, BitsAndBytesConfig

hf_token = os.getenv("HUGGINGFACE_HUB_TOKEN")
if hf_token:
    login(token=hf_token)

app = FastAPI()

MODEL_NAME = "meta-llama/Meta-Llama-3-70B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_auth_token=True)
quant_config = BitsAndBytesConfig(load_in_8bit=True)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    torch_dtype="auto",
    quantization_config=quant_config,
    use_auth_token=True
)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

@app.get("/", response_class=HTMLResponse)
async def chat_ui():
    with open("app/chat_ui.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/generate")
async def generate_text(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    output = generator(prompt, max_new_tokens=256)
    return JSONResponse({"response": output[0]["generated_text"]})