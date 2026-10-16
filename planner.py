from rules import decide_folder

def build_plan(folder):
    plan = []
    for item in folder.iterdir():
        if item.is_file() and not item.name.startswith('.'):
            plan.append({
                "item": item,
                "folder": decide_folder(item),
                "reason": "rule",
            })
    return plan