import json
from datetime import datetime
from pathlib import Path

LOG = Path("logs.jsonl")

def log_move(item, dest, reason):
    entry = {
        "file": item.name,
        "from": str(item),
        "to": str(dest),
        "reason": reason,
        "time": datetime.now().isoformat(),
    }
    with LOG.open("a") as file:
        file.write(json.dumps(entry) + "\n")