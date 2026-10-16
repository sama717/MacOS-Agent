from pathlib import Path
from planner import build_plan

DRY_RUN = True
desktop = Path.home() / "Desktop"

plan = build_plan(desktop)

for item, step in enumerate(plan, 1):
    print(item, step["item"].name, "->", step["folder"])

answer = input("Numbers to skip (like 6, 232), or Enter to approve all: ")
skip = { int(n) for n in answer.split(",") if n.strip() }
