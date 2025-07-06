from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"  # change later if you like

print("[LLM] loading model – first run may take a while …")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto",
    device_map="auto"
)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate(prompt: str, max_new_tokens: int = 128):
    res = generator(
        prompt,
        do_sample=False,
        max_new_tokens=max_new_tokens,
        pad_token_id=tokenizer.eos_token_id,
    )
    return res[0]["generated_text"][len(prompt) :]
