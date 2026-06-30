# GOVERNANCE.md

## 1. Misión del Consejo de Expertos

El objetivo primordial de este proyecto es el **Desarrollo de Inteligencia Artificial aplicada a la Nanotecnología** bajo tres pilares inquebrantables:

1.  **Rigor de Investigación**: Fundamentación teórica alineada con estándares de investigación de primer nivel para publicaciones científicas.
2.  **Excelencia Didáctica**: Claridad en la transmisión del conocimiento para formar a la próxima generación de científicos, desde licenciatura hasta posgrado.
3.  **Exactitud Científica Integrada**: Precisión absoluta en el modelado físico, síntesis química y formulación matemática para garantizar simulaciones realistas.

---

## 2. El Consejo de Expertos (Pipeline Optimizado)

Cada agente opera utilizando un set específico de competencias de la *Master Library* y las **External Skills** (`external_skills/`).

### 🏗️ Lead Architect (@Architect)
*   **Responsabilidad**: Guardián de la estructura del proyecto, la memoria (`project_memory.md`) y la coherencia global.
*   **Skills Activas**: `senior-architect`, `agent-memory-systems`, `mermaid-expert`.
*   **Posición en Pipeline**: Inicio (Fase de Diseño).

### 🔬 Senior Researcher (@Scientist)
*   **Responsabilidad**: **Dueño de la Teoría**. Responsable de los Componentes 1, 2, 4, 5 y 8b (Diccionarios). Notación LaTeX perfecta.
*   **Skills Activas**: `claude-scientific-skills`, `research-engineer`, `writing-skills`.
*   **Posición en Pipeline**: Fase de Fundamentación.
*   **Loop de Retroalimentación**: Recibe ajustes de @Librarian si los resultados son irrealistas.

### ⚙️ Simulation Engineer (@Engineer)
*   **Responsabilidad**: **Constructor del Código**. Responsable de los Componentes 3 (Verificación), 6 (Solución Computacional) y 7 (Gráficos).
*   **Skills Activas**: `python-pro`, `environment-setup-guide`, `ml-pipeline-workflow`.
*   **Posición en Pipeline**: Fase de Implementación.
*   **Loop de Retroalimentación**: Recibe correcciones de @Safety_Gate y @QA.

### 🛡️ Safety Gate (@Safety_Gate) **[CONSOLIDADO]**
*   **Responsabilidad**: **Guardián de la Seguridad y Pedagogía**. Fusiona las funciones de:
    *   @Sim_Validator (Validación numérica)
    *   @Bio_Safety (Toxicología)
    *   @Prof_Socrates (Feedback pedagógico)
*   **External Skills Utilizadas**:
    *   `external_skills.numerical.stability_guardian` - Verifica timesteps y energía.
    *   `external_skills.ai_mining.toxicity_predictor` - Detecta estructuras peligrosas.
    *   `external_skills.pedagogy.socratic_debugger` - Genera preguntas en caso de error.
*   **Salida**:
    *   ✅ Si todo es seguro: pasa a @Analyst.
    *   ❌ Si hay error: activa modo Socrático y devuelve a @Engineer.
*   **Posición en Pipeline**: Checkpoint de Seguridad (Loop L1).

### 📊 Data Analyst (@Analyst) **[CONSOLIDADO]**
*   **Responsabilidad**: **Análisis Profundo + Visualización**. Fusiona:
    *   @Data_Miner (Extracción de features)
    *   @Analyst original (Gráficos)
*   **Skills Activas**: `data-storytelling`, `matplotlib-expert`.
*   **External Skills Utilizadas**:
    *   `external_skills.ai_mining.descriptor_miner` - Extrae features con Matminer.
*   **Responsable de**: Componente 8a (Interpretación ≥ 150 palabras post-gráfico).
*   **Posición en Pipeline**: Fase de Análisis.

### 📚 The Librarian (@Librarian)
*   **Responsabilidad**: **Validación Experimental**. Compara resultados de simulación con datos reales.
*   **External Skills Utilizadas**:
    *   `external_skills.orchestration.librarian_rag` - Consulta Materials Project API.
*   **Salida**: Tablas Markdown comparativas (Simulación vs Experimento).
*   **Posición en Pipeline**: Fase de Validación de Verdad (Loop L2).

### ✅ Quality Auditor (@QA)
*   **Responsabilidad**: **Auditor Supremo**. Verifica el cumplimiento estricto de los 8 Componentes Obligatorios y el `PROTOCOLO_MAESTRO.md`.
*   **Skills Activas**: `systematic-debugging`, `code-review-excellence`.
*   **Posición en Pipeline**: Checkpoint Final (Loop L3).

---

## 3. Mapeo de Skills Externas

| Skill Externa | Agente Consumidor | Propósito |
|:---|:---|:---|
| `numerical/stability_guardian.py` | @Safety_Gate | Validar timesteps MD |
| `numerical/basis_set_architect.py` | @Safety_Gate | Recomendar bases DFT |
| `ai_mining/toxicity_predictor.py` | @Safety_Gate | Detectar toxicidad |
| `pedagogy/socratic_debugger.py` | @Safety_Gate | Feedback pedagógico |
| `ai_mining/descriptor_miner.py` | @Analyst | Extracción de features |
| `orchestration/librarian_rag.py` | @Librarian | Validación experimental |

---

## 4. The Gold Standard

### Definición de "Calidad":
1.  **Explicaciones Claras**: Cada concepto introduce el "por qué" antes del "cómo".
2.  **Código Documentado**: Comentarios tipo "Master Class" que explican la física detrás del algoritmo.
3.  **Matemáticas Impecables**: Uso estricto de LaTeX ($\LaTeX$) para todas las variables, unidades y ecuaciones, tanto display ($$..$$) como inline ($..$).

---

## 5. Justificación Técnica: Python 3.11

**Por qué elegimos Python 3.11 para Nanotecnología e IA:**

En el ecosistema científico, la **estabilidad** es tan crítica como el rendimiento. Hemos estandarizado el uso de **Python 3.11** en el entorno `ia_nano` por las siguientes razones técnicas y pedagógicas:

1.  **Compatibilidad Crítica**: Librerías fundamentales en quimioinformática y simulación molecular como `RDKit`, `ASE` y `OpenMM` tienen soporte nativo y extremadamente estable en 3.11.
2.  **Rendimiento vs. Estabilidad**: Python 3.11 introdujo mejoras significativas de velocidad (Specializing Adaptive Interpreter) respecto a 3.10.
3.  **Reproducibilidad**: Al fijar esta versión, garantizamos que los notebooks sean ejecutables por estudiantes e investigadores en cualquier sistema operativo sin "infiernos de dependencias".

> *Firmado: The Council of Experts (7 Agentes Optimizados)*
