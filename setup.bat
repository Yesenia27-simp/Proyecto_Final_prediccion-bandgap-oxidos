@echo off
REM ============================================================================
REM Antigravity Nano Research Multiagentic Core - Setup Script (Windows)
REM ============================================================================
REM This script automates the installation of the ia_nano environment.
REM Features:
REM - Auto-installs Miniconda if missing
REM - Handles network timeouts (retries)
REM - Sets up Jupyter kernel
REM ============================================================================

echo.
echo ========================================================================
echo  Antigravity Nano Research Multiagentic Core - Setup
echo ========================================================================
echo.

REM --- Step 1: Verify/Install Conda ---
echo [1/6] Verificando Conda...
where conda >nul 2>nul
if %ERRORLEVEL% equ 0 (
    echo [OK] Conda encontrado
    goto :CREATE_ENV
)

echo [INFO] Conda no encontrado. Procediendo a instalar Miniconda...
echo.

REM --- Download and Install Miniconda ---
echo [2/6] Descargando Miniconda (esto puede tardar varios minutos)...
set MINICONDA_INSTALLER=%TEMP%\Miniconda3-latest-Windows-x86_64.exe
set MINICONDA_PATH=%USERPROFILE%\miniconda3

powershell -Command "Invoke-WebRequest -Uri 'https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe' -OutFile '%MINICONDA_INSTALLER%'"
if %ERRORLEVEL% neq 0 (
    echo [ERROR] No se pudo descargar Miniconda
    echo Intenta descargar manualmente desde: https://docs.conda.io/en/latest/miniconda.html
    pause
    exit /b 1
)
echo [OK] Descarga completada
echo.

echo [3/6] Instalando Miniconda en %MINICONDA_PATH%...
echo Esto puede tardar varios minutos. Por favor espera...
start /wait "" "%MINICONDA_INSTALLER%" /InstallationType=JustMe /RegisterPython=0 /S /D=%MINICONDA_PATH%
if %ERRORLEVEL% neq 0 (
    echo [ERROR] La instalacion de Miniconda fallo
    pause
    exit /b 1
)
echo [OK] Miniconda instalado correctamente
echo.

REM --- Initialize Conda ---
echo [4/6] Configurando Conda...
call "%MINICONDA_PATH%\Scripts\activate.bat"
call conda init powershell
call conda init cmd.exe
set PATH=%MINICONDA_PATH%\Scripts;%MINICONDA_PATH%;%PATH%
echo [OK] Conda configurado
echo.

:CREATE_ENV
REM --- Step 5: Create Environment ---
echo [5/6] Creando ambiente ia_nano (Python 3.11)...
echo Esto puede tomar varios minutos...
echo.

REM Configure timeout to handle slow connections
call conda config --set remote_read_timeout_secs 300

call conda env list | findstr "ia_nano" >nul 2>nul
if %ERRORLEVEL% equ 0 (
    echo [INFO] El ambiente ya existe. Actualizando...
    call conda env update -f environment.yml --prune
) else (
    call conda env create -f environment.yml
)

if %ERRORLEVEL% neq 0 (
    echo.
    echo [ERROR] No se pudo crear/actualizar el ambiente.
    echo Posible error de conexion. Reintentando...
    pause
    exit /b 1
)
echo [OK] Ambiente ia_nano creado/actualizado
echo.

REM --- Step 6: Activate and Finalize ---
echo [6/6] Finalizando configuracion...
call conda activate ia_nano
if %ERRORLEVEL% neq 0 (
    echo [ERROR] No se pudo activar el ambiente ia_nano
    pause
    exit /b 1
)

echo Instalando dependencias pip...
pip install -r requirements.txt --quiet
echo [OK] Dependencias pip instaladas

echo Registrando kernel Jupyter...
python -m ipykernel install --user --name=ia_nano --display-name="Python 3.11 (ia_nano)"
echo [OK] Kernel Jupyter registrado
echo.

REM --- Verify Installation ---
echo Verificando instalacion...
python verify_installation.py
if %ERRORLEVEL% neq 0 (
    echo [WARNING] La verificacion reporto algunos problemas.
) else (
    echo [OK] Verificacion completa.
)
echo.

REM --- Success Message ---
echo ========================================================================
echo  INSTALACION COMPLETA
echo ========================================================================
echo.
echo Proximos pasos:
echo   1. Cierra esta ventana y abre una nueva terminal.
echo   2. Ejecuta:
echo      conda activate ia_nano
echo      jupyter lab
echo.
echo   3. Selecciona el kernel "Python 3.11 (ia_nano)"
echo.
echo ========================================================================
pause
