# Unidad 5 — Sistemas Multi-Agente Modernos

**Curso:** IA Aplicada a Investigación Científica y Tecnológica  
**Repositorio:** [Multiagent-AI-Lab/Antigravity-Nano-Research-Multiagentic-Core](https://github.com/Multiagent-AI-Lab/Antigravity-Nano-Research-Multiagentic-Core)

---

## Propósito

Esta unidad construye **infraestructura de agentes reutilizable para cualquier dominio de investigación**: ciencias naturales, ingeniería, humanidades digitales, bioinformática, economía, entre otros.

Los ejemplos usan nanotecnología como dominio ilustrativo. La aplicación directa a nanotecnología está en la **Unidad 6**. Aquí el foco es el stack multi-agente en sí: cómo orquestar, enrutar, escalar y desplegar sistemas que un investigador puede adaptar a su propio dominio en horas.

---

## Notebooks

| Archivo | Sección | Contenido principal |
|---------|---------|---------------------|
| `U5_00_META_CONSTRUYENDO_CON_IA.ipynb` | 0 | Meta-notebook: cómo se construyó esta unidad con IA |
| `U5_01_FUNDAMENTOS_AGENTES_MODERNOS.ipynb` | 1–8.5 | ReAct, AgentExecutor, LCEL, 4 tipos de memoria, Smolagents CodeAgent, tests unitarios |
| `U5_02_LANGCHAIN_AVANZADO_LANGGRAPH.ipynb` | — | LangGraph StateGraph, ciclos, checkpoints, HITL |
| `U5_03_CREWAI_SISTEMAS_MULTIAGENTE.ipynb` | — | CrewAI: roles, tareas, memoria, human feedback |
| `U5_04_GOOGLE_ADK_A2A.ipynb` | — | Google ADK, protocolo A2A, MCP desde cero |
| `U5_05_RAG_MEMORIA_AVANZADA.ipynb` | — | RAG, ChromaDB, Mem0, 4 tipos de memoria persistente |
| `U5_06_GRAPH_RAG_MEMORIA.ipynb` | — | GraphRAG, Neo4j, grafos de conocimiento |
| `U5_07_MULTIMODAL_PRODUCCION.ipynb` | — | Multimodal, FastAPI async, observabilidad, model routing, lecciones de campo |
| `U5_08_PROYECTO_INTEGRADOR.ipynb` | — | Sistema multi-agente end-to-end + blueprint multi-proveedor |

---

## Stack tecnológico

| Capa | Tecnología | Versión |
|------|-----------|---------|
| Orquestación | LangChain / LangGraph | 0.3.25 / 0.2.56 |
| Multi-agente por roles | CrewAI | 0.80.0 |
| Agentes corporativos | Google ADK | 1.0.0 |
| Code agents | smolagents | 1.13.0 |
| Memoria vectorial | ChromaDB | 0.6.3 |
| Memoria persistente | Mem0 | latest |
| APIs de producción | FastAPI | 0.115.11 |
| Modelos (prioridad 1) | OpenRouter (Llama 4 Scout, Gemini 2.5, Kimi-K2.5, DeepSeek R1) | — |
| Modelos (fallback local) | Ollama llama3.2 | — |

---

## Modelo de routing (todos los notebooks)

```
OpenRouter → Gemini → OpenAI → Ollama (local, sin API key)
```

Funciona con GPU potente, con laptop económica, o sin internet. El investigador elige su nivel de recursos sin cambiar el código.

---

## Tabla de modelos (estado: marzo 2026)

| Caso de uso | Modelo | Costo/1M tok | Nota |
|------------|--------|-------------|------|
| FAQ, extracción | GPT-4o-mini / Gemini Flash | $0.10–0.15 | Rápido y económico |
| Razonamiento técnico | **Gemini 2.5 Flash** | $0.15 | Modo thinking integrado |
| Razonamiento profundo | **Gemini 2.5 Pro** | $1.25 | 1M tokens contexto |
| Multimodal + 10M ctx | **Llama 4 Scout** | $0.11 | Open weights, Meta abr 2026 |
| Cloud via Ollama, sin GPU | **Kimi-K2.5** | ~$0.15 | Tool calling mejorado |
| Alta privacidad | Ollama llama3.2 | $0 | 100% local |

---

## Prerrequisitos

- Python 3.11+
- Conda environment `ia_nano` (ver `environment.yml` en la raíz del repositorio)
- API keys opcionales — los notebooks funcionan con Ollama sin ninguna clave

---

## Instalación

```bash
git clone https://github.com/Multiagent-AI-Lab/Antigravity-Nano-Research-Multiagentic-Core
cd Antigravity-Nano-Research-Multiagentic-Core
conda env create -f environment.yml
conda activate ia_nano
pip install -r educational_content/unit_05_multi_agent_sys/requirements.txt
cp educational_content/unit_05_multi_agent_sys/.env.example .env
jupyter lab
```

---

## Adaptación a tu dominio de investigación

Cada notebook incluye un `DOMAIN_CONTEXTS` en la skill `context_loader` que puedes extender:

```python
DOMAIN_CONTEXTS["mi_dominio"] = {
    "description": "Tu descripción del dominio",
    "system_prompt_points": [
        "Punto 1 de expertise",
        "Punto 2 de metodología",
        ...
    ]
}
```

El agente ajusta automáticamente su comportamiento al dominio sin cambiar la arquitectura.

---

## Seguridad

- `eval()` **no se usa** en ningún notebook. Las expresiones aritméticas se evalúan con un parser AST que solo permite nodos `Constant`, `BinOp` y `UnaryOp`.
- Tests unitarios incluidos en U5_01 verifican el evaluador y las skills principales.

---

## Relación con otras unidades

- **Unidad 4** (ADK Fundamentals) → prerequisito recomendado
- **Unidad 5** (esta) → infraestructura multi-agente genérica
- **Unidad 6** → aplicación de esta infraestructura a nanotecnología computacional

---

*Última actualización: 30 de marzo de 2026*  
*Antigravity-Nano-Research — Unit 05 Multi-Agent Systems*
