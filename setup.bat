@echo off
REM ============================================================================
REM Antigravity Nano Research Multiagentic Core - Setup Script (Windows)
REM ============================================================================
REM This script automates the installation of the ia_nano environment
REM ============================================================================

echo.
echo ========================================================================
echo  Antigravity Nano Research Multiagentic Core - Setup
echo ========================================================================
echo.

REM --- Step 1: Verify Conda ---
echo [1/5] Verificando Conda...
where conda >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo.
    echo [ERROR] Conda no encontrado en el PATH
    echo.
    echo Por favor instala Anaconda o Miniconda:
    echo   - Anaconda: https://www.anaconda.com/download
    echo   - Miniconda: https://docs.conda.io/en/latest/miniconda.html
    echo.
    echo Despues de instalar, reinicia esta terminal y ejecuta setup.bat nuevamente.
    pause
    exit /b 1
)
echo [OK] Conda encontrado
echo.

REM --- Step 2: Create Environment ---
echo [2/5] Creando ambiente ia_nano (Python 3.11)...
echo Esto puede tomar varios minutos...
echo.
conda env create -f environment.yml
if %ERRORLEVEL% neq 0 (
    echo.
    echo [WARNING] El ambiente ya existe o hubo un error.
    echo Intentando actualizar el ambiente existente...
    conda env update -f environment.yml --prune
    if %ERRORLEVEL% neq 0 (
        echo [ERROR] No se pudo crear/actualizar el ambiente
        pause
        exit /b 1
    )
)
echo [OK] Ambiente ia_nano creado/actualizado
echo.

REM --- Step 3: Activate and Install Pip Dependencies ---
echo [3/5] Instalando dependencias adicionales con pip...
call conda activate ia_nano
if %ERRORLEVEL% neq 0 (
    echo [ERROR] No se pudo activar el ambiente ia_nano
    pause
    exit /b 1
)

pip install -r requirements.txt --quiet
if %ERRORLEVEL% neq 0 (
    echo [WARNING] Algunas dependencias pip fallaron, pero continuando...
)
echo [OK] Dependencias pip instaladas
echo.

REM --- Step 4: Register Jupyter Kernel ---
echo [4/5] Registrando kernel Jupyter...
python -m ipykernel install --user --name=ia_nano --display-name="Python 3.11 (ia_nano)"
if %ERRORLEVEL% neq 0 (
    echo [ERROR] No se pudo registrar el kernel Jupyter
    pause
    exit /b 1
)
echo [OK] Kernel Jupyter registrado
echo.

REM --- Step 5: Verify Installation ---
echo [5/5] Verificando instalacion...
python verify_installation.py
if %ERRORLEVEL% neq 0 (
    echo.
    echo [WARNING] La verificacion reporto algunos problemas
    echo Revisa los mensajes arriba para mas detalles
    echo.
) else (
    echo [OK] Verificacion completa
    echo.
)

REM --- Success Message ---
echo ========================================================================
echo  INSTALACION COMPLETA
echo ========================================================================
echo.
echo Proximos pasos:
echo   1. Activar el ambiente:
echo      conda activate ia_nano
echo.
echo   2. Iniciar Jupyter Lab:
echo      jupyter lab
echo.
echo   3. En Jupyter, selecciona el kernel "Python 3.11 (ia_nano)"
echo.
echo Documentacion:
echo   - README.md          : Guia rapida
echo   - GOVERNANCE.md      : Roles de los agentes
echo   - INSTALL.md         : Troubleshooting detallado
echo.
echo ========================================================================
pause
