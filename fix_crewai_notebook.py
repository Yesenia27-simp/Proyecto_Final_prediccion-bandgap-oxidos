# Unidad 4 — IA Aplicada a Nanotecnologia y Datos Experimentales

**Curso:** IA Aplicada a Investigacion Cientifica y Tecnologica  
**Repositorio:** [Multiagent-AI-Lab/Antigravity-Nano-Research-Multiagentic-Core](https://github.com/Multiagent-AI-Lab/Antigravity-Nano-Research-Multiagentic-Core)

---

## Proposito

Esta unidad aplica **IA Generativa y modelos de lenguaje** directamente a problemas de investigacion
en nanotecnologia: analisis de datos experimentales (SEM, espectroscopia), consulta inteligente
a bases de datos de materiales, optimizacion con algoritmos evolutivos y bayesianos, y
preparacion para los sistemas multi-agente de la Unidad 5.

---

## Notebooks

| Archivo | Contenido principal |
|---------|---------------------|
| `UNIDAD_4_IA_APLICADA.ipynb` | LLMs para ciencia de materiales, Materials Project API, prompting cientifico, embeddings, RAG basico |
| `UNIDAD_4_PARTE2_DATOS_EXPERIMENTALES.ipynb` | Computer Vision SEM/TEM, analisis espectroscopico, series temporales, optimizacion bayesiana y genetica |

---

## Temas cubiertos

**Parte 1 — LLMs y Generative AI:**
- Fundamentos de LLMs: tokenizacion, atencion, in-context learning
- Prompting cientifico: zero-shot, few-shot, chain-of-thought para investigacion
- Materials Project API: consultas programaticas a la base de datos de materiales mas grande del mundo
- Embeddings y busqueda semantica: representacion vectorial de textos cientificos
- RAG basico: recuperacion aumentada por generacion para consulta de literatura

**Parte 2 — Datos Experimentales:**
- Computer Vision para microscopio SEM/TEM: deteccion y segmentacion de nanoparticulas (U-Net)
- Analisis espectroscopico: FTIR, Raman, XPS — extraccion de features con ML
- Series temporales: deteccion de anomalias en datos de sintesis
- Optimizacion bayesiana: busqueda eficiente del espacio de parametros de sintesis
- Algoritmos geneticos: optimizacion multiobjetivo (tamano, morfoligia, propiedades)
- Neural Network Potentials para screening de materiales a gran escala

---

## Stack tecnologico

| Herramienta | Uso |
|-------------|-----|
| mp_api | Acceso programatico a Materials Project |
| scikit-learn | Pipelines de analisis espectroscopico y series temporales |
| scikit-image | Segmentacion y analisis de imagenes SEM/TEM |
| PyTorch / torchvision | U-Net para Computer Vision, NNPs |
| OpenAI / OpenRouter | LLMs (via API) para prompting y embeddings |
| Optuna | Optimizacion bayesiana de hiperparametros y parametros de sintesis |

---

## Prerrequisitos

- **Unidad 3** completada (ML clasico y redes neuronales)
- Conocimiento basico de fisica experimental (espectroscopia, microscopia)
- Cuenta en Materials Project (gratuita): https://next-gen.materialsproject.org/
- API key de OpenRouter o Google Gemini (opcional — notebooks tienen fallback)
- Nivel: posgrado / investigacion
- Duracion estimada: 8-12 horas (2 notebooks grandes)

---

## Instalacion

```bash
git clone https://github.com/Multiagent-AI-Lab/Antigravity-Nano-Research-Multiagentic-Core
cd Antigravity-Nano-Research-Multiagentic-Core
conda env create -f environment.yml
conda activate ia_nano
# Variables de entorno (opcional para LLMs):
# MP_API_KEY=tu_key_de_materials_project
# OPENROUTER_API_KEY=tu_key_de_openrouter
jupyter lab educational_content/unit_04_applied_ai/
```

---

## Datasets incluidos

- `materials_project_oxides_20260330.csv` — oxidos descargados via Materials Project API
- `spectral_features.csv` — features extraidos de espectros de ejemplo
- Imagenes SEM generadas sinteticamente para Computer Vision

---

## Relacion con otras unidades

- **Unidad 3** (prerequisito) -> modelos ML y redes neuronales
- **Unidad 4** (esta) -> LLMs, Vision y optimizacion sobre datos reales
- **Unidad 5** -> sistemas multi-agente que orquestan las herramientas de U1-U4

---

*Ultima actualizacion: abril 2026*  
*Antigravity-Nano-Research — Unit 04 Applied AI*
