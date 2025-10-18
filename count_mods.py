import os

# Change this to your own path
ROOT = r"c:\Users\borgo\AppData\Roaming\eden\load\0100F43008C44000"

cheat_mods = []
exefs_mods = []
other_mods = []

for entry in os.scandir(ROOT):
    if not entry.is_dir():
        continue

    cheats_path = os.path.join(entry.path, "cheats")
    exefs_path = os.path.join(entry.path, "exefs")

    if os.path.isdir(cheats_path):
        cheat_mods.append(entry.name)
    elif os.path.isdir(exefs_path):
        exefs_mods.append(entry.name)
    else:
        other_mods.append(entry.name)

# === Output summary ===
total = len(cheat_mods) + len(exefs_mods) + len(other_mods)

print(f"=== Mod Count for {ROOT} ===")
print(f"Total mods found: {total}")
print(f" - Cheats mods: {len(cheat_mods)}")
print(f" - Exefs mods:  {len(exefs_mods)}")
print(f" - Other dirs:  {len(other_mods)}\n")

if cheat_mods:
    print("Cheat-based mods:")
    for name in cheat_mods:
        print(f"  • {name}")

if exefs_mods:
    print("\nExefs-based mods:")
    for name in exefs_mods:
        print(f"  • {name}")

if other_mods:
    print("\nOther folders (not recognized as mods):")
    for name in other_mods:
        print(f"  • {name}")
