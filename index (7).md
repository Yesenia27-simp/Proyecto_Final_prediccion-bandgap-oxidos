# Unidad 5 — Sistemas Multi-Agente

## Descripción General

Diseño y orquestación de sistemas multi-agente para investigación científica, desde LangChain hasta Google ADK 1.0 con protocolo A2A.

## Temas

### Frameworks Cubiertos

| Framework | Enfoque |
|-----------|---------|
| LangChain | Chains, tools, LCEL |
| LangGraph | Grafos con estado, ciclos |
| CrewAI | Colaboración por roles |
| Google ADK 1.0 | Agentes listos para producción |
| SmolaAgents | Agentes ligeros (HF) |

### Temas Avanzados

- **Protocolo A2A** (Agent-to-Agent) — Estándar de comunicación cross-framework
- **RAG y GraphRAG** — Generación Aumentada por Recuperación con grafos
- **Mem0 + ChromaDB** — Memoria persistente de agentes
- **Producción**: FastAPI, OpenTelemetry, model routing

## Notebooks Clave

| Notebook | Tema |
|----------|------|
| U5_01 | Fundamentos LangChain |
| U5_02 | Agentes con estado LangGraph |
| U5_03 | Equipos multi-rol CrewAI |
| **U5_04** | **Google ADK 1.0 + A2A + Gemma4** |
| U5_05 | RAG y GraphRAG |
| U5_06 | Memoria persistente (Mem0) |
| U5_07 | Producción: FastAPI + observabilidad |
| U5_08 | Model routing multi-proveedor |
| U5_09 | SmolaAgents (HuggingFace) |

## Destacado U5_04 — Google ADK + A2A

El notebook más avanzado de la unidad cubre:

- `LlmAgent`, `SequentialAgent`, `ParallelAgent`, `LoopAgent`
- `BuiltInCodeExecutor` — Ejecución de código en sandbox seguro
- `BaseTool` con tipado estricto Pydantic
- Checkpoints de sesión y recuperación
- **AgentCard** y protocolo de descubrimiento A2A
- Cliente cross-framework con autenticación Bearer
- Fallbacks locales para cuotas de API agotadas

[Abrir Unidad 5 en GitHub](https://github.com/Multiagent-AI-Lab/Antigravity-Nano-Research-Multiagentic-Core/tree/main/educational_content/unit_05_multi_agent_sys){ .md-button }
