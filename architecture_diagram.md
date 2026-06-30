# Unidad 2 — Simulacion Molecular Avanzada

**Curso:** IA Aplicada a Investigacion Cientifica y Tecnologica  
**Repositorio:** [Multiagent-AI-Lab/Antigravity-Nano-Research-Multiagentic-Core](https://github.com/Multiagent-AI-Lab/Antigravity-Nano-Research-Multiagentic-Core)

---

## Proposito

Esta unidad profundiza en las herramientas de simulacion computacional de mayor uso en investigacion:
Dinamica Molecular (MD) y Teoria del Funcional de la Densidad (DFT). El estudiante simula el
comportamiento de sistemas atomicos en el tiempo, calcula propiedades electronicas y disenha
nanoestructuras computacionalmente.

---

## Notebooks

| Archivo | Contenido principal |
|---------|---------------------|
| `UNIDAD_2_SIMULACION_MOLECULAR.ipynb` | Dinamica Molecular: potenciales, ensembles NVE/NVT/NPT, analisis de trayectorias, propiedades de transporte |
| `UNIDAD_2_PARTE2_DFT_NANOFABRICACION.ipynb` | DFT: bases Gaussianas, pseudopotenciales, propiedades electronicas, disenho de nanoestructuras |

---

## Temas cubiertos

**Parte 1 — Dinamica Molecular:**
- Fundamentos de MD: ecuaciones de movimiento, integracion temporal (Verlet, Velocity-Verlet)
- Potenciales interatomicos: Lennard-Jones, EAM, Tersoff
- Ensembles termodinamicos: NVE (microcanonino), NVT (canonico), NPT (isobarico-isotermico)
- Termostatos y barostatos: Nose-Hoover, Berendsen, Parrinello-Rahman
- Analisis de trayectorias: RMSD, MSD, coeficiente de difusion, funciones de correlacion
- Propiedades de transporte: viscosidad, conductividad termica

**Parte 2 — DFT y Nanofabricacion:**
- Teoria del Funcional de la Densidad (DFT): principios, funcionales de intercambio-correlacion
- Bases Gaussianas (STO-3G, 6-31G*, cc-pVDZ) vs. ondas planas
- Pseudopotenciales: PAW, norm-conserving
- Optimizacion de estructuras con DFT
- Calculo de propiedades electronicas: band gap, densidad de estados (DOS), cargas de Mulliken
- Disenho computacional de nanoestructuras: heterojunctions, nanowires, quantum dots

---

## Stack tecnologico

| Herramienta | Uso |
|-------------|-----|
| ASE | Simulaciones MD y DFT, manejo de trayectorias |
| NumPy / SciPy | Analisis numerico y estadistico |
| Matplotlib | Visualizacion de trayectorias, DOS, RDF |
| NGLView | Visualizacion 3D de trayectorias moleculares |

---

## Prerrequisitos

- **Unidad 1** completada (ASE, estructuras atomicas, optimizacion geometrica)
- Mecanica clasica y estadistica (basico)
- Mecanica cuantica: ecuacion de Schrodinger (basico)
- Nivel: licenciatura avanzada / posgrado
- Duracion estimada: 6-10 horas (2 notebooks)

---

## Instalacion

```bash
git clone https://github.com/Multiagent-AI-Lab/Antigravity-Nano-Research-Multiagentic-Core
cd Antigravity-Nano-Research-Multiagentic-Core
conda env create -f environment.yml
conda activate ia_nano
jupyter lab educational_content/unit_02_molecular_simulation/
```

---

## Archivos generados durante la ejecucion

- `.traj` — trayectorias de MD (excluidas via `.gitignore`)
- `.npz` — datos de simulacion comprimidos

---

## Relacion con otras unidades

- **Unidad 1** (prerequisito) -> estructuras estaticas
- **Unidad 2** (esta) -> estructuras dinamicas, propiedades electronicas
- **Unidad 3** -> ML predictivo usando datos generados en U1 y U2

---

*Ultima actualizacion: abril 2026*  
*Antigravity-Nano-Research — Unit 02 Molecular Simulation*
