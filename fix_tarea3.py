import json

path = r'c:\Users\yesiz\OneDrive\Documentos\Modelado IA\Antigravity-Nano-Research-Multiagentic-Core-main\Tarea 1.ipynb'

with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f"Celdas antes: {len(nb['cells'])}")

# The Tarea 3 header marker
tarea3_marker = "Tarea 3: Investigacion"

# Find first occurrence of a Tarea 3 cell
first_t3 = None
for i, cell in enumerate(nb['cells']):
    src = ''.join(cell['source'])
    if tarea3_marker in src:
        first_t3 = i
        break

if first_t3 is None:
    print("No se encontro Tarea 3. Nada que hacer.")
else:
    # Keep only cells up to and including the 4 Tarea 3 cells starting at first_t3
    nb['cells'] = nb['cells'][:first_t3 + 4]
    print(f"Celdas despues (recortado hasta celda {first_t3 + 3}): {len(nb['cells'])}")

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=4)
    print("OK: Duplicados eliminados.")
