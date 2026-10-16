import json
from pathlib import Path

rules = json.loads(Path("rules.json").read_text())

def decide_folder(item):
    for prefix, folder in rules["name_starts_with"].items():
        if item.name.startswith(prefix):
            return folder
    return rules["extensions"].get(item.suffix.lower(), rules["fallback"])