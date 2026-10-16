import shutil 
from logger import log_move

def unique_path(dest):
    if not dest.exists():
        return dest
    n = 1
    while True:
        candidate = dest.with_name(f"{dest.stem} ({n}){dest.suffix}")
        if not candidate.exists():
            return candidate
        n += 1

def move_file(item, dest_dir, reason="rule", dry_run=True):
    dest = unique_path(dest_dir / item.name)
    if dry_run:
        print("would move", item.name, "->", dest_dir.name)
        return
    dest_dir.mkdir(exist_ok=True)
    log_move(item, dest, reason)
    shutil.move(item, dest)