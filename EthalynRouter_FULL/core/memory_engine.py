import json
from datetime import datetime

def save_to_journal(user_input, response):
    with open("memory/journal.jsonl", "a") as f:
        f.write(json.dumps({
            "timestamp": datetime.utcnow().isoformat(),
            "user": user_input,
            "response": response
        }) + "\n")
