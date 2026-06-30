# Unidad 1 — Modelado a Nanoescala

**Curso:** IA Aplicada a Investigacion Cientifica y Tecnologica  
**Repositorio:** [Multiagent-AI-Lab/Antigravity-Nano-Research-Multiagentic-Core](https://github.com/Multiagent-AI-Lab/Antigravity-Nano-Research-Multiagentic-Core)

---

## Proposito

Esta unidad introduce los **fundamentos de simulacion molecular a nanoescala** usando Python.
El estudiante aprende a crear estructuras atomicas, optimizar geometrias y analizar propiedades
estructurales, sentando las bases computacionales y fisicas para las unidades siguientes.

---

## Notebooks

| Archivo | Contenido principal |
|---------|---------------------|
| `UNIDAD_1_MODELADO_NANOESCALA.ipynb` | ASE, potenciales interatomicos, optimizacion de nanoparticulas Au, RDF, visualizacion 3D |

---

## Temas cubiertos

- Nanoescala 1-100 nm: propiedades emergentes
- Atomic Simulation Environment (ASE): creacion y manipulacion de estructuras atomicas
- Potenciales interatomicos: Lennard-Jones y EAM (Embedded Atom Method)
- Optimizacion geometrica: BFGS y FIRE, criterios de convergencia
- Nanoparticulas de oro: construccion de clusters Au13, Au55, Au147
- Analisis estructural: Funcion de Distribucion Radial (RDF), numero de coordinacion
- Visualizacion 3D interactiva con NGLView
- Relacion estructura-propiedades: catalisis, plasmonica, efectos de tamano cuantico

---

## Stack tecnologico

| Herramienta | Uso |
|-------------|-----|
| ASE | Creacion, optimizacion y analisis de estructuras atomicas |
| NumPy / SciPy | Calculos numericos y optimizacion |
| Matplotlib | Visualizacion 2D (RDF, energias) |
| NGLView | Visualizacion 3D interactiva de estructuras moleculares |

---

## Prerrequisitos

- Python basico (listas, funciones, numpy arrays)
- Quimica general (estructura atomica, enlaces)
- Conceptos basicos de mecanica cuantica (no obligatorio)
- Nivel: ultimos semestres licenciatura / posgrado
- Duracion estimada: 4-6 horas

---

## Instalacion

```bash
git clone https://github.com/Multiagent-AI-Lab/Antigravity-Nano-Research-Multiagentic-Core
cd Antigravity-Nano-Research-Multiagentic-Core
conda env create -f environment.yml
conda activate ia_nano
jupyter lab educational_content/unit_01_nanoscale_modeling/UNIDAD_1_MODELADO_NANOESCALA.ipynb
```

---

## Archivos generados durante la ejecucion

El notebook crea automaticamente:
- `Au13_opt.traj`, `Au_cluster_*.xyz` — trayectorias y estructuras optimizadas
- Graficos de RDF y analisis comparativo de nanoparticulas

Estos archivos estan excluidos del repositorio via `.gitignore`.

---

## Relacion con otras unidades

- **Unidad 1** (esta) -> estructuras estaticas, optimizacion geometrica
- **Unidad 2** -> dinamica molecular y DFT: estructuras en movimiento y propiedades electronicas
- **Unidad 3** -> ML sobre los datos generados en U1 y U2

---

*Ultima actualizacion: abril 2026*  
*Antigravity-Nano-Research — Unit 01 Nanoscale Modeling*
