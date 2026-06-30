# Installation Guide

Guía detallada de instalación y troubleshooting para **Antigravity Nano Research Multiagentic Core**.

---

## 📋 Requisitos Previos

### Obligatorios

1. **Antigravity** - [Instalación](https://github.com/google-deepmind/antigravity)
2. **Conda o Miniconda** - [Descargar](https://docs.conda.io/en/latest/miniconda.html)
3. **Git** - [Descargar](https://git-scm.com/downloads)
4. **Python 3.11** (se instalará vía conda)

### Opcionales

- **Node.js** (v18+) - Para MCP servers
- **CUDA Toolkit** - Para aceleración GPU en OpenMM

---

## 🚀 Instalación Rápida

### Método A: Setup Automático (Recomendado)

**Windows**:
```batch
git clone https://github.com/ljyudico/Antigravity-Nano-Research-Multiagentic-Core.git
cd Antigravity-Nano-Research-Multiagentic-Core
setup.bat
```

**Linux/macOS**:
```bash
git clone https://github.com/ljyudico/Antigravity-Nano-Research-Multiagentic-Core.git
cd Antigravity-Nano-Research-Multiagentic-Core
chmod +x setup.sh
./setup.sh
```

### Método B: Instalación Manual

Si el setup automático falla, sigue estos pasos:

#### 1. Crear Ambiente Conda

```bash
conda env create -f environment.yml
```

#### 2. Activar Ambiente

```bash
conda activate ia_nano
```

#### 3. Instalar Dependencias Pip

```bash
pip install -r requirements.txt
```

#### 4. Registrar Kernel Jupyter

```bash
python -m ipykernel install --user --name=ia_nano --display-name="Python 3.11 (ia_nano)"
```

#### 5. Verificar Instalación

```bash
python verify_installation.py
```

---

## 🔧 Troubleshooting

### Error: "Conda command not found"

**Causa**: Conda no está en el PATH del sistema.

**Solución Windows**:
1. Busca "Anaconda Prompt" en el menú inicio
2. Ejecuta el setup desde Anaconda Prompt en lugar de CMD
3. O añade Conda al PATH:
   - Panel de Control → Sistema → Variables de entorno
   - Añade `C:\Users\TU_USUARIO\miniconda3\Scripts` al PATH

**Solución Linux/macOS**:
```bash
# Añade a ~/.bashrc o ~/.zshrc
export PATH="$HOME/miniconda3/bin:$PATH"
source ~/.bashrc
```

---

### Error: "Solving environment: failed"

**Causa**: Conflictos de dependencias o canales de conda.

**Solución**:
```bash
# Limpiar caché de conda
conda clean --all

# Actualizar conda
conda update -n base conda

# Intentar de nuevo
conda env create -f environment.yml
```

Si persiste, instala manualmente:
```bash
conda create -n ia_nano python=3.11
conda activate ia_nano
conda install -c conda-forge ase rdkit openmm mendeleev jupyterlab
pip install -r requirements.txt
```

---

### Error: "ImportError: No module named 'rdkit'"

**Causa**: RDKit no se instaló correctamente.

**Solución**:
```bash
conda activate ia_nano
conda install -c conda-forge rdkit
```

**Verificar**:
```python
python -c "from rdkit import Chem; print('RDKit OK')"
```

---

### Error: "Kernel 'ia_nano' not found"

**Causa**: El kernel Jupyter no está registrado.

**Solución**:
```bash
conda activate ia_nano
python -m ipykernel install --user --name=ia_nano
```

**Verificar kernels disponibles**:
```bash
jupyter kernelspec list
```

---

### Error: "External skills not found"

**Causa**: El directorio `external_skills` no está en el PYTHONPATH.

**Solución**:

**Opción 1 (Temporal)**:
```python
# En tu notebook
import sys
sys.path.append('/ruta/absoluta/a/Antigravity-Nano-Research-Multiagentic-Core')
```

**Opción 2 (Permanente)**:
```bash
# Crear archivo .pth en site-packages
conda activate ia_nano
python -c "import site; print(site.getsitepackages()[0])"
# Anota la ruta, luego:
echo "/ruta/a/Antigravity-Nano-Research-Multiagentic-Core" > /ruta/site-packages/nano_research.pth
```

---

### Problemas con OpenMM en Windows

**Síntoma**: `ImportError: DLL load failed`

**Causa**: Falta Visual C++ Redistributable.

**Solución**:
1. Descarga [Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)
2. Instala y reinicia
3. Reinstala OpenMM:
   ```bash
   conda install -c conda-forge openmm --force-reinstall
   ```

---

### Problemas con CUDA (GPU)

**Verificar CUDA**:
```bash
nvidia-smi
```

**Instalar OpenMM con soporte CUDA**:
```bash
conda install -c conda-forge openmm cudatoolkit=11.8
```

**Verificar GPU en OpenMM**:
```python
from openmm import Platform
print(Platform.getPluginLoadFailures())
print([Platform.getPlatform(i).getName() for i in range(Platform.getNumPlatforms())])
```

Deberías ver `['Reference', 'CPU', 'CUDA', 'OpenCL']`.

---

## 🍎 Instalación en macOS (Apple Silicon M1/M2)

### Consideraciones Especiales

RDKit y OpenMM tienen soporte nativo para ARM64, pero requiere configuración especial:

```bash
# Usar miniforge en lugar de miniconda
brew install miniforge
conda init zsh  # o bash

# Crear ambiente
conda env create -f environment.yml

# Si RDKit falla, instalar desde conda-forge
conda install -c conda-forge rdkit
```

### Verificar Arquitectura

```bash
python -c "import platform; print(platform.machine())"
# Debería mostrar: arm64
```

---

## 🐧 Instalación en Linux

### Dependencias del Sistema

**Ubuntu/Debian**:
```bash
sudo apt-get update
sudo apt-get install build-essential libssl-dev libffi-dev python3-dev
```

**Fedora/RHEL**:
```bash
sudo dnf install gcc gcc-c++ make openssl-devel libffi-devel python3-devel
```

---

## ✅ Verificación Completa

Ejecuta el script de verificación:

```bash
conda activate ia_nano
python verify_installation.py
```

**Salida esperada**:
```
======================================================================
 Verificación de Instalación - Antigravity Nano Research
======================================================================

🐍 Verificando versión de Python...
   ✓ Python 3.11.x (Correcto)

📦 Verificando dependencias críticas...
   ✓ NumPy
   ✓ Pandas
   ✓ SciPy
   ✓ Matplotlib
   ✓ ASE (Atomic Simulation Environment)
   ✓ RDKit
   ✓ Mendeleev
   ✓ SymPy

🛠️  Verificando External Skills...
   ✓ Stability Guardian
   ✓ Basis Set Architect
   ✓ Toxicity Predictor
   ✓ Socratic Debugger
   ✓ Librarian RAG

📓 Verificando kernel Jupyter...
   ✓ Kernel 'ia_nano' registrado

======================================================================
 ✅ VERIFICACIÓN COMPLETA - Todo está correctamente instalado
======================================================================
```

---

## 🔄 Actualizar el Ambiente

Si hay actualizaciones en `environment.yml`:

```bash
conda activate ia_nano
conda env update -f environment.yml --prune
```

---

## 🗑️ Desinstalar

```bash
# Eliminar ambiente
conda deactivate
conda env remove -n ia_nano

# Eliminar kernel Jupyter
jupyter kernelspec uninstall ia_nano

# Eliminar repositorio
rm -rf Antigravity-Nano-Research-Multiagentic-Core
```

---

## 📞 Soporte

Si ninguna solución funciona:

1. Revisa [Issues existentes](https://github.com/ljyudico/Antigravity-Nano-Research-Multiagentic-Core/issues)
2. Abre un nuevo Issue con:
   - Output completo de `python verify_installation.py`
   - Output de `conda list`
   - Tu sistema operativo y versión
   - Logs de error completos

---

## 📚 Recursos Adicionales

- [Conda Cheat Sheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
- [ASE Documentation](https://wiki.fysik.dtu.dk/ase/)
- [RDKit Getting Started](https://www.rdkit.org/docs/GettingStartedInPython.html)
- [OpenMM User Guide](http://docs.openmm.org/latest/userguide/)

---

<div align="center">
  <sub>¿Instalación exitosa? ¡Ahora lee <a href="README.md">README.md</a> para comenzar! 🚀</sub>
</div>
