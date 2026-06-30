"""
Script auxiliar: agrega las celdas del ejercicio de Ciberseguridad al notebook
U5_01_FUNDAMENTOS_AGENTES_MODERNOS.ipynb usando nbformat.

El codigo de la celda se lee desde _cyber_cell_source.py para evitar
problemas de escape con comillas triples en strings multilínea.

Ejecutar desde el directorio del notebook:
    python _add_cyber_cell.py
"""
import nbformat
from pathlib import Path

HERE          = Path(__file__).parent
NOTEBOOK_PATH = HERE / "U5_01_FUNDAMENTOS_AGENTES_MODERNOS.ipynb"
SOURCE_PATH   = HERE / "_cyber_cell_source.py"

# ── Celda Markdown ────────────────────────────────────────────────────────────
MARKDOWN_SOURCE = """\
---
## Ejercicio de Extensión — Solución Propuesta
### Dominio: **Ciberseguridad y Respuesta a Incidentes** 🛡️

**Dominio elegido:** Analista de Seguridad Informática especializado en clasificación de
vulnerabilidades (CVE), cálculo de severidad CVSS y análisis de Indicadores de Compromiso (IoC).

Este dominio es **diferente** a los ejemplos del notebook (nanociencia y finanzas cuantitativas):
- No requiere cálculos continuos sino clasificación categórica y validación en bases de datos de amenazas
- El foco es **determinismo y precisión** — una respuesta incorrecta puede dejar sistemas expuestos
- Los hiperparámetros priorizan reproducibilidad forense y lenguaje técnico preciso sobre creatividad
"""

# ── Código de la celda — leído desde archivo independiente ────────────────────
print(f"Leyendo código fuente desde: {SOURCE_PATH}")
with open(SOURCE_PATH, encoding="utf-8") as f:
    CODE_SOURCE = f.read()

# ── Leer el notebook ──────────────────────────────────────────────────────────
print(f"Leyendo notebook: {NOTEBOOK_PATH}")
with open(NOTEBOOK_PATH, encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

print(f"Celdas actuales: {len(nb.cells)}")

# ── Comprobar idempotencia ────────────────────────────────────────────────────
for cell in nb.cells:
    if "cybersecurity_ir" in cell.source and "EJERCICIO DE EXTENSIÓN" in cell.source:
        print("AVISO: Las celdas de Ciberseguridad ya existen en el notebook.")
        raise SystemExit(0)

# ── Crear nuevas celdas ───────────────────────────────────────────────────────
md_cell   = nbformat.v4.new_markdown_cell(source=MARKDOWN_SOURCE)
code_cell = nbformat.v4.new_code_cell(source=CODE_SOURCE)
md_cell.id   = "f2a8d3b1"
code_cell.id = "c9e7f501"

# ── Agregar al final ──────────────────────────────────────────────────────────
nb.cells.append(md_cell)
nb.cells.append(code_cell)

# ── Guardar ───────────────────────────────────────────────────────────────────
with open(NOTEBOOK_PATH, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"\nNotebook actualizado correctamente.")
print(f"  Celdas totales: {len(nb.cells)}")
print(f"  Nuevas celdas: 2 (markdown + codigo)")
print(f"  Dominio nuevo: cybersecurity_ir")
