from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from llama_cpp import Llama

app = FastAPI()

llm = Llama(
    model_path="llama-3-32b.Q4_K_M.gguf",  # Downloaded GGUF file path
    n_ctx=4096,
    n_gpu_layers=-1   # All on GPU!
)

@app.get("/", response_class=HTMLResponse)
async def chat_ui():
    with open("app/chat_ui.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/generate")
async def generate_text(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    output = llm(prompt, max_tokens=256, stop=["</s>"])
    text = output["choices"][0]["text"]
    return JSONResponse({"response": text})
