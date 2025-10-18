import os
import re

# Paths
# Replace this with your own paths

SRC = r"c:\Users\borgo\AppData\Roaming\eden\load\0100F43008C44000\Misc Mods\cheats\7222E13ECF6ADB32.txt"
OUT_ROOT = r"c:\Users\borgo\AppData\Roaming\eden\load\0100F43008C44000"
OUT_BASENAME = os.path.basename(SRC)  # 7222E13ECF6ADB32.txt

def sanitize_name(name: str) -> str:
    """Make a clean folder name."""
    name = name.strip()
    # Remove surrounding brackets
    name = re.sub(r'^\[|\]$', '', name)
    # Remove leading symbols (#, numbers, etc.)
    name = re.sub(r'^[#\d.\-\s]+', '', name)
    # Replace bad path characters
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    # Trim and limit length
    return name.strip()[:120]

def write_mod(header: str, lines: list[str]):
    """Write one mod block into its folder."""
    modname = sanitize_name(header)
    folder = os.path.join(OUT_ROOT, modname)
    cheats_dir = os.path.join(folder, "cheats")
    os.makedirs(cheats_dir, exist_ok=True)
    out_path = os.path.join(cheats_dir, OUT_BASENAME)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(header + "\n")
        f.writelines(lines)
    print(f"Created: {modname}")

with open(SRC, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

current_header = None
current_lines = []
count = 0

for line in lines:
    if re.match(r'^\[.*\]$', line.strip()):
        # New section found -> write the previous one first
        if current_header:
            write_mod(current_header, current_lines)
            count += 1
        current_header = line.strip()
        current_lines = []
    else:
        current_lines.append(line)

# Write the last section
if current_header:
    write_mod(current_header, current_lines)
    count += 1

print(f"\nDone! {count} mods created in {OUT_ROOT}")
