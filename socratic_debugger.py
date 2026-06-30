# External Skills - Antigravity Nano Research

Este directorio contiene **skills modulares** desarrolladas específicamente para el sistema multi-agente de IA aplicada a Nanotecnología.

---

## 📁 Estructura

```
external_skills/
├── __init__.py                 # Inicialización del paquete
├── numerical/                  # Skills de validación numérica
│   ├── stability_guardian.py   # Validador de timesteps MD
│   └── basis_set_architect.py  # Recomendador de bases DFT
├── ai_mining/                  # Skills de AI/ML
│   └── toxicity_predictor.py   # Predictor de toxicidad
├── pedagogy/                   # Skills pedagógicas
│   └── socratic_debugger.py    # Generador de feedback Socrático
└── orchestration/              # Skills de orquestación
    └── librarian_rag.py        # RAG para validación experimental
```

---

## 🎯 Propósito

Las skills son **módulos independientes** que extienden las capacidades de los agentes del Consejo de Expertos. Cada skill:

- ✅ Tiene una responsabilidad única y bien definida
- ✅ Puede ser usada por uno o más agentes
- ✅ Incluye docstrings completos (Google style)
- ✅ Es testeable de forma aislada

---

## 🔗 Mapeo Skill → Agente

| Skill | Agente Consumidor | Propósito |
|-------|-------------------|-----------|
| `stability_guardian` | @Safety_Gate | Validar timesteps MD |
| `basis_set_architect` | @Safety_Gate | Recomendar bases DFT |
| `toxicity_predictor` | @Safety_Gate | Detectar toxicidad |
| `socratic_debugger` | @Safety_Gate | Feedback pedagógico |
| `librarian_rag` | @Librarian | Validación experimental |

Ver [GOVERNANCE.md](../GOVERNANCE.md) para detalles del pipeline de agentes.

---

## 📖 Uso

### Importar una Skill

```python
from external_skills.numerical import stability_guardian

# Analizar timestep
result = stability_guardian.analyze_timestep(
    dt_fs=1.0,
    simulation_type="MD",
    bond_types=['C-H', 'O-H']
)

print(result['safe'])  # True/False
print(result['message'])
```

### Ejemplo Completo

```python
from external_skills.numerical import basis_set_architect
from external_skills.ai_mining import toxicity_predictor

# Recomendar base para oro
basis_info = basis_set_architect.select_basis('Au', accuracy_level='high_precision')
print(f"Usar: {basis_info['basis']}")
print(f"Razón: {basis_info['reason']}")

# Predecir toxicidad
tox = toxicity_predictor.predict_toxicity('HgCl2')
if tox['is_toxic']:
    print(f"⚠️ Tóxico: {tox['toxicity_score']:.2f}")
    print(f"Mecanismos: {', '.join(tox['mechanisms'])}")
```

---

## 🛠️ Crear una Nueva Skill

### 1. Elegir Categoría

Decide en qué subdirectorio va tu skill:
- `numerical/` - Validación numérica, optimización
- `ai_mining/` - Modelos ML, predictores
- `pedagogy/` - Herramientas educativas
- `orchestration/` - Integración con APIs externas

### 2. Crear Archivo

```python
# external_skills/numerical/mi_nueva_skill.py

def mi_funcion(param1, param2):
    """
    Brief description.
    
    Args:
        param1 (type): Description
        param2 (type): Description
        
    Returns:
        dict: {
            "resultado": value,
            "mensaje": str,
            "metadata": dict
        }
        
    Example:
        >>> result = mi_funcion(10, 20)
        >>> print(result['resultado'])
        30
    """
    # Implementación
    return {
        "resultado": param1 + param2,
        "mensaje": "Operación exitosa",
        "metadata": {}
    }
```

### 3. Añadir Tests

```python
# tests/test_mi_nueva_skill.py

from external_skills.numerical import mi_nueva_skill

def test_mi_funcion():
    result = mi_nueva_skill.mi_funcion(10, 20)
    assert result['resultado'] == 30
    assert 'mensaje' in result
```

### 4. Documentar

- Añade entrada en este README
- Actualiza [SKILLS_ATTRIBUTION.md](../SKILLS_ATTRIBUTION.md)
- Documenta qué agente la consumirá en [GOVERNANCE.md](../GOVERNANCE.md)

---

## 🧪 Testing

```bash
# Activar ambiente
conda activate ia_nano

# Ejecutar tests
python -m pytest tests/ -v

# Test específico
python -m pytest tests/test_stability_guardian.py -v
```

---

## 📚 Recursos

- [SKILLS_ATTRIBUTION.md](../SKILLS_ATTRIBUTION.md) - Origen y créditos
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Guía de contribución
- [GOVERNANCE.md](../GOVERNANCE.md) - Roles de agentes

---

## 🔮 Roadmap

### Próximas Skills

- [ ] `band_structure_analyzer` - Análisis de estructura de bandas
- [ ] `reaction_pathway_finder` - Búsqueda de caminos de reacción
- [ ] `ml_force_field_trainer` - Entrenamiento de campos de fuerza ML
- [ ] `crystal_structure_validator` - Validación de simetrías cristalinas

¿Tienes ideas? Abre un [Issue](https://github.com/ljyudico/Antigravity-Nano-Research-Multiagentic-Core/issues) con la etiqueta `skill-proposal`.

---

<div align="center">
  <sub>Skills desarrolladas para investigación científica rigurosa 🔬</sub>
</div>
