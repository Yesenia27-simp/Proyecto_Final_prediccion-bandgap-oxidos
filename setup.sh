#!/bin/bash
# ============================================================================
# Antigravity Nano Research Multiagentic Core - Setup Script (Linux/macOS)
# ============================================================================
# This script automates the installation of the ia_nano environment
# ============================================================================

set -e  # Exit on error

echo ""
echo "========================================================================"
echo " Antigravity Nano Research Multiagentic Core - Setup"
echo "========================================================================"
echo ""

# --- Step 1: Verify Conda ---
echo "[1/5] Verificando Conda..."
if ! command -v conda &> /dev/null; then
    echo ""
    echo "[ERROR] Conda no encontrado en el PATH"
    echo ""
    echo "Por favor instala Anaconda o Miniconda:"
    echo "  - Anaconda: https://www.anaconda.com/download"
    echo "  - Miniconda: https://docs.conda.io/en/latest/miniconda.html"
    echo ""
    echo "Después de instalar, reinicia esta terminal y ejecuta ./setup.sh nuevamente."
    exit 1
fi
echo "[OK] Conda encontrado"
echo ""

# --- Step 2: Create Environment ---
echo "[2/5] Creando ambiente ia_nano (Python 3.11)..."
echo "Esto puede tomar varios minutos..."
echo ""

if conda env create -f environment.yml 2>/dev/null; then
    echo "[OK] Ambiente ia_nano creado"
else
    echo "[WARNING] El ambiente ya existe o hubo un error."
    echo "Intentando actualizar el ambiente existente..."
    conda env update -f environment.yml --prune
    echo "[OK] Ambiente ia_nano actualizado"
fi
echo ""

# --- Step 3: Activate and Install Pip Dependencies ---
echo "[3/5] Instalando dependencias adicionales con pip..."

# Initialize conda for bash
eval "$(conda shell.bash hook)"
conda activate ia_nano

pip install -r requirements.txt --quiet || echo "[WARNING] Algunas dependencias pip fallaron, pero continuando..."
echo "[OK] Dependencias pip instaladas"
echo ""

# --- Step 4: Register Jupyter Kernel ---
echo "[4/5] Registrando kernel Jupyter..."
python -m ipykernel install --user --name=ia_nano --display-name="Python 3.11 (ia_nano)"
echo "[OK] Kernel Jupyter registrado"
echo ""

# --- Step 5: Verify Installation ---
echo "[5/5] Verificando instalación..."
if python verify_installation.py; then
    echo "[OK] Verificación completa"
else
    echo "[WARNING] La verificación reportó algunos problemas"
    echo "Revisa los mensajes arriba para más detalles"
fi
echo ""

# --- Success Message ---
echo "========================================================================"
echo " INSTALACIÓN COMPLETA"
echo "========================================================================"
echo ""
echo "Próximos pasos:"
echo "  1. Activar el ambiente:"
echo "     conda activate ia_nano"
echo ""
echo "  2. Iniciar Jupyter Lab:"
echo "     jupyter lab"
echo ""
echo "  3. En Jupyter, selecciona el kernel 'Python 3.11 (ia_nano)'"
echo ""
echo "Documentación:"
echo "  - README.md          : Guía rápida"
echo "  - GOVERNANCE.md      : Roles de los agentes"
echo "  - INSTALL.md         : Troubleshooting detallado"
echo ""
echo "========================================================================"
