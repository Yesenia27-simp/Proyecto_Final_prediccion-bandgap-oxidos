# Contributing to Antigravity Nano Research Multiagentic Core

¡Gracias por tu interés en contribuir! Este documento proporciona guías para contribuir al proyecto.

---

## 📋 Tabla de Contenidos

- [Código de Conducta](#código-de-conducta)
- [Cómo Contribuir](#cómo-contribuir)
- [Reportar Bugs](#reportar-bugs)
- [Proponer Features](#proponer-features)
- [Pull Requests](#pull-requests)
- [Estándares de Código](#estándares-de-código)
- [Estándares Científicos](#estándares-científicos)

---

## Código de Conducta

Este proyecto se adhiere a un código de conducta profesional y respetuoso. Al participar, te comprometes a:

- Ser respetuoso con todos los contribuyentes
- Aceptar críticas constructivas
- Enfocarte en lo mejor para la comunidad científica
- Mostrar empatía hacia otros miembros de la comunidad

---

## Cómo Contribuir

### 1. Fork del Repositorio

```bash
# Fork en GitHub, luego clona tu fork
git clone https://github.com/TU_USUARIO/Antigravity-Nano-Research-Multiagentic-Core.git
cd Antigravity-Nano-Research-Multiagentic-Core
```

### 2. Crear Rama de Feature

```bash
git checkout -b feature/nombre-descriptivo
# o para bugs:
git checkout -b fix/descripcion-del-bug
```

### 3. Hacer Cambios

- Sigue los [estándares de código](#estándares-de-código)
- Añade tests si es aplicable
- Actualiza documentación si es necesario

### 4. Commit

```bash
git add .
git commit -m "feat: descripción clara del cambio"
```

**Formato de commits** (Conventional Commits):
- `feat:` - Nueva funcionalidad
- `fix:` - Corrección de bug
- `docs:` - Cambios en documentación
- `style:` - Formato, sin cambios de código
- `refactor:` - Refactorización de código
- `test:` - Añadir tests
- `chore:` - Mantenimiento

### 5. Push y Pull Request

```bash
git push origin feature/nombre-descriptivo
```

Luego abre un Pull Request en GitHub con:
- Descripción clara de los cambios
- Referencia a issues relacionados
- Screenshots si aplica (para cambios visuales)

---

## Reportar Bugs

Usa el [template de bug report](.github/ISSUE_TEMPLATE/bug_report.md) e incluye:

- **Descripción**: Qué esperabas vs. qué obtuviste
- **Pasos para reproducir**: Lista numerada de pasos
- **Ambiente**:
  - OS (Windows/Linux/macOS)
  - Python version
  - Versión de dependencias críticas (ASE, RDKit)
- **Logs**: Copia completa del error
- **Contexto adicional**: Screenshots, archivos de entrada

---

## Proponer Features

Usa el [template de feature request](.github/ISSUE_TEMPLATE/feature_request.md) e incluye:

- **Problema que resuelve**: ¿Qué necesidad cubre?
- **Solución propuesta**: Descripción técnica
- **Alternativas consideradas**: Otros enfoques
- **Impacto**: ¿A quién beneficia?

---

## Pull Requests

### Checklist antes de enviar PR

- [ ] El código sigue los estándares de PEP 8
- [ ] Todos los tests pasan (`python -m pytest`)
- [ ] Añadiste docstrings a funciones nuevas
- [ ] Actualizaste README.md si es necesario
- [ ] Verificaste que no hay conflictos con `main`
- [ ] El commit message sigue Conventional Commits

### Proceso de Revisión

1. **Automated Checks**: GitHub Actions ejecutará tests automáticos
2. **Code Review**: Un mantenedor revisará tu código
3. **Feedback**: Responde a comentarios y haz cambios si es necesario
4. **Merge**: Una vez aprobado, se hará merge a `main`

---

## Estándares de Código

### Python (PEP 8)

```python
# ✅ Correcto
def calculate_energy(atoms, temperature=300.0):
    """
    Calculate total energy of atomic system.
    
    Args:
        atoms (ase.Atoms): Atomic structure
        temperature (float): Temperature in Kelvin
        
    Returns:
        float: Total energy in eV
    """
    kinetic = 0.5 * atoms.get_masses() * atoms.get_velocities()**2
    potential = atoms.get_potential_energy()
    return kinetic.sum() + potential

# ❌ Incorrecto (sin docstring, nombres poco claros)
def calc(a, t=300):
    k = 0.5 * a.get_masses() * a.get_velocities()**2
    p = a.get_potential_energy()
    return k.sum() + p
```

### Docstrings (Google Style)

```python
def my_function(param1, param2):
    """
    Brief description (one line).
    
    Longer description if needed. Explain the physics/chemistry
    behind the algorithm if relevant.
    
    Args:
        param1 (type): Description
        param2 (type): Description
        
    Returns:
        type: Description
        
    Raises:
        ValueError: When param1 is negative
        
    Example:
        >>> result = my_function(10, 20)
        >>> print(result)
        30
    """
    pass
```

### Imports

```python
# Orden de imports:
# 1. Standard library
import os
import sys

# 2. Third-party
import numpy as np
import pandas as pd
from ase import Atoms

# 3. Local
from external_skills.numerical import stability_guardian
```

---

## Estándares Científicos

### Ecuaciones en LaTeX

Todas las ecuaciones deben estar en LaTeX:

```markdown
La energía cinética se calcula como:

$$
K = \frac{1}{2} m v^2
$$

donde $m$ es la masa y $v$ la velocidad.
```

### Unidades

Siempre especifica unidades:

```python
# ✅ Correcto
timestep_fs = 1.0  # femtoseconds
energy_eV = atoms.get_potential_energy()  # eV

# ❌ Incorrecto (sin unidades)
timestep = 1.0
energy = atoms.get_potential_energy()
```

### Referencias

Si implementas un algoritmo de un paper, cita la fuente:

```python
def verlet_integration(atoms, dt):
    """
    Velocity Verlet integration algorithm.
    
    Reference:
        Swope et al., J. Chem. Phys. 76, 637 (1982)
        DOI: 10.1063/1.442716
    """
    pass
```

---

## Áreas de Contribución

### 🔬 Skills Científicas

Nuevas skills en `external_skills/`:
- Validadores numéricos
- Predictores ML
- Herramientas de análisis

### 📊 Visualización

Mejoras en gráficos y reportes:
- Nuevos tipos de plots
- Dashboards interactivos
- Exportación de figuras

### 📖 Documentación

- Tutoriales
- Ejemplos de uso
- Traducciones
- FAQ

### 🧪 Tests

- Tests unitarios
- Tests de integración
- Benchmarks de performance

---

## Preguntas

Si tienes dudas:

1. Revisa la [documentación](README.md)
2. Busca en [Issues existentes](https://github.com/ljyudico/Antigravity-Nano-Research-Multiagentic-Core/issues)
3. Abre un nuevo Issue con la etiqueta `question`

---

## Licencia

Al contribuir, aceptas que tus contribuciones estarán bajo la licencia Apache-2.0 del proyecto.

---

<div align="center">
  <sub>¡Gracias por hacer la ciencia más abierta y colaborativa! 🚀</sub>
</div>
