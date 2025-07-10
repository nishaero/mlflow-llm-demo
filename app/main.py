from fastapi import FastAPI, Request
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

app = FastAPI()

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_auth_token=True)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto", torch_dtype="auto", use_auth_token=True)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

@app.post("/generate")
async def generate_text(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    output = generator(prompt, max_new_tokens=100)
    return {"response": output[0]["generated_text"]}
