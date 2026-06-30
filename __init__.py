# External Skills - Antigravity Nano Research

Este directorio contiene **skills modulares** desarrolladas específicamente para el sistema multi-agente de IA aplicada a Nanotecnología.

---

## Estructura

```
external_skills/
├── __init__.py                      # Inicialización del paquete
├── registry.py                      # Registro central de skills (load_skill, discover_skills)
├── agent_warmup/
│   └── context_loader.py            # Inyecta contexto de dominio en agentes LLM
├── ai_mining/
│   └── toxicity_predictor.py        # Predictor de toxicidad de nanomateriales
├── apis/
│   ├── github_skill_loader.py       # Carga skills desde repositorios GitHub
│   └── token_budget_guard.py        # Control de presupuesto de tokens
├── evaluation/
│   └── output_scorer.py             # Evaluación de salidas de agentes
├── memory/
│   ├── episodic_retriever.py        # Recuperación de memoria episódica
│   └── graph_memory.py              # Memoria en grafo de conocimiento
├── numerical/
│   ├── stability_guardian.py        # Validador de timesteps MD
│   └── basis_set_architect.py       # Recomendador de bases DFT
├── observability/
│   └── trace_annotator.py           # Anotación de trazas de agentes
├── orchestration/
│   └── librarian_rag.py             # RAG para validación experimental
├── pedagogy/
│   └── socratic_debugger.py         # Generador de feedback socrático
└── routing/
    └── task_classifier.py           # Clasificador de tareas para routing
```

---

## Propósito

Las skills son **módulos independientes** que extienden las capacidades de los agentes del Consejo de Expertos. Cada skill:

- Tiene una responsabilidad única y bien definida
- Puede ser usada por uno o más agentes
- Incluye docstrings completos (Google style)
- Es testeable de forma aislada

---

## Mapeo Skill - Agente

| Skill | Agente Consumidor | Proposito |
|-------|-------------------|-----------|
| `context_loader` | todos los agentes | Inyectar contexto de dominio al inicio |
| `task_classifier` | @Orchestrator | Routing de tareas |
| `token_budget_guard` | @Orchestrator | Control de costos |
| `stability_guardian` | @Safety_Gate | Validar timesteps MD |
| `basis_set_architect` | @Safety_Gate | Recomendar bases DFT |
| `toxicity_predictor` | @Safety_Gate | Detectar toxicidad |
| `episodic_retriever` | @Librarian | Recuperar contexto previo |
| `graph_memory` | @Librarian | Consultar grafo de conocimiento |
| `librarian_rag` | @Librarian | Validación experimental |
| `output_scorer` | @Evaluator | Puntuar respuestas de agentes |
| `trace_annotator` | @Observability | Registrar trazas de ejecución |
| `socratic_debugger` | @Pedagogy | Feedback pedagogico |
| `github_skill_loader` | @Orchestrator | Cargar skills externas dinamicamente |

Ver [GOVERNANCE.md](../GOVERNANCE.md) para detalles del pipeline de agentes.

---

## Uso

### Usar el registry

```python
from external_skills.registry import load_skill, discover_skills

# Cargar skill por nombre (ultima version disponible)
retrieve = load_skill("episodic_retriever")
episodes = retrieve.retrieve(query="nanoparticles", user_id="user_1")

# Cargar version especifica
retrieve_v1 = load_skill("episodic_retriever@1.0.0")

# Ver todas las skills disponibles
discover_skills()
```

### Importar directamente

```python
from external_skills.numerical import stability_guardian

result = stability_guardian.analyze_timestep(
    dt_fs=1.0,
    simulation_type="MD",
    bond_types=['C-H', 'O-H']
)
print(result['safe'])   # True/False
print(result['message'])
```

---

## Crear una Nueva Skill

1. Crear el archivo `.py` en el subdirectorio correspondiente
2. Agregar la entrada en `registry.py` con version, modulo, descripcion y tags
3. Escribir tests en `tests/`
4. Actualizar este README y [SKILLS_ATTRIBUTION.md](../SKILLS_ATTRIBUTION.md)

---

## Testing

```bash
conda activate ia_nano
pytest tests/ -v
```

---

## Referencias

- [SKILLS_ATTRIBUTION.md](../SKILLS_ATTRIBUTION.md) - Origen y creditos
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Guia de contribucion
- [GOVERNANCE.md](../GOVERNANCE.md) - Roles de agentes
