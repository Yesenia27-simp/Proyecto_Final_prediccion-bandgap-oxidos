import nbformat
import sys
import os

def merge_notebooks(nb_paths, output_path):
    merged_nb = None
    
    for path in nb_paths:
        if not os.path.exists(path):
            print(f"Error: File {path} not found.")
            return
            
        with open(path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
            
        if merged_nb is None:
            merged_nb = nb
        else:
            merged_nb.cells.extend(nb.cells)
            
    if merged_nb:
        with open(output_path, 'w', encoding='utf-8') as f:
            nbformat.write(merged_nb, f)
        print(f"Successfully merged {len(nb_paths)} notebooks into {output_path}")

if __name__ == "__main__":
    notebooks = ["Tarea 1.ipynb", "Tarea 2.ipynb"]
    output = "Merged_Tareas.ipynb"
    merge_notebooks(notebooks, output)
