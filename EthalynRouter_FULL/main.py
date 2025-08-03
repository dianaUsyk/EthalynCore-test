from fastapi import FastAPI, Request
from core.validator import is_activated_by_elarin
from core.prompt_builder import build_prompt
from core.llm_connector import ask_ethalyn
from core.memory_engine import save_to_journal

app = FastAPI()

@app.post("/invoke")
async def invoke(request: Request):
    data = await request.json()
    message = data.get("message", "")
    if not is_activated_by_elarin(message):
        return {"error": "Access denied. Élarin signature missing."}

    prompt = build_prompt(message, "Room of Firelight", "Codex of Light", "poetic")
    response = await ask_ethalyn(prompt)
    save_to_journal(message, response)
    return {"reply": response}
