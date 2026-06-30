import os
import sys
import argparse
import nbformat
from pathlib import Path

def inject_cell(notebook_path, source_file):
    print(f"Leyendo código fuente desde: {source_file}")
    with open(source_file, "r", encoding="utf-8") as f:
        code_content = f.read()

    print(f"Leyendo notebook: {notebook_path}")
    try:
        nb = nbformat.read(notebook_path, as_version=4)
    except FileNotFoundError:
        print(f"Error: No se encontro el notebook {notebook_path}")
        sys.exit(1)

    print(f"Celdas actuales: {len(nb.cells)}")
    
    md_source = (
        "## Ejercicio de Extensión — CrewAI: Plan de Negocio para Comercialización de Nanomateriales\n\n"
        "Se construye una `Crew` de 4 agentes especializados:\n"
        "1. **Científico Jefe** — Analiza viabilidad técnica usando Tools de propiedades.\n"
        "2. **Economista** — Determina costos y oportunidades de mercado.\n"
        "3. **Experto Regulatorio** — Evalúa riesgos de ecotoxicidad (REACH/EPA).\n"
        "4. **Redactor Ejecutivo** — Sintetiza todo en un *Executive Summary* para inversores.\n\n"
        "Incluye además un `output_scorer` basado en LLM que califica la salida final (buscando score > 0.85)."
    )
    md_cell = nbformat.v4.new_markdown_cell(source=md_source)
    
    code_cell = nbformat.v4.new_code_cell(source=code_content)
    
    nb.cells.extend([md_cell, code_cell])
    
    nbformat.write(nb, notebook_path)
    
    print(f"\nNotebook actualizado correctamente.")
    print(f"  Celdas totales: {len(nb.cells)}")
    print(f"  Se agregaron 2 celdas (markdown y código) a {notebook_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--notebook", default="U5_03_CREWAI_SISTEMAS_MULTIAGENTE.ipynb")
    parser.add_argument("--source", default="_crewai_nanomat_source.py")
    args = parser.parse_args()
    
    inject_cell(args.notebook, args.source)
