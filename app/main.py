import os
from huggingface_hub import login
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

hf_token = os.getenv("HUGGINGFACE_HUB_TOKEN")
if hf_token:
    login(token=hf_token)

app = FastAPI()

MODEL_NAME = "meta-llama/Meta-Llama-3-70B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_auth_token=True)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto", torch_dtype="auto", use_auth_token=True)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Serve a simple chat UI at "/"
@app.get("/", response_class=HTMLResponse)
async def chat_ui():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>LLM Chat</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 30px; background: #f4f4f4;}
            #chat { width: 100%; max-width: 600px; margin: auto; background: #fff; padding: 20px; border-radius: 8px; }
            .msg { margin-bottom: 10px; }
            .user { color: #0b5394; }
            .bot { color: #38761d; }
            #input { width: 80%; padding: 8px; }
            #send { padding: 8px 14px; }
        </style>
    </head>
    <body>
        <div id="chat">
            <h2>LLM Chat</h2>
            <div id="messages"></div>
            <input id="input" type="text" placeholder="Type your message..." autocomplete="off"/>
            <button id="send">Send</button>
        </div>
        <script>
        const input = document.getElementById('input');
        const send = document.getElementById('send');
        const messages = document.getElementById('messages');
        function addMsg(role, text) {
            const div = document.createElement('div');
            div.className = 'msg ' + role;
            div.innerHTML = '<strong>' + role + ':</strong> ' + text;
            messages.appendChild(div);
            messages.scrollTop = messages.scrollHeight;
        }
        send.onclick = async function() {
            const prompt = input.value.trim();
            if (!prompt) return;
            addMsg('user', prompt);
            input.value = '';
            addMsg('bot', '<em>Thinking...</em>');
            const resp = await fetch('/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ prompt })
            });
            const data = await resp.json();
            messages.lastChild.innerHTML = '<strong>bot:</strong> ' + data.response;
        };
        input.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') send.onclick();
        });
        </script>
    </body>
    </html>
    """

@app.post("/generate")
async def generate_text(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    output = generator(prompt, max_new_tokens=100)
    return JSONResponse({"response": output[0]["generated_text"]})