# Inicio Rápido

## Requisitos

- Python 3.11
- Conda o Miniconda
- Git

## Instalación

=== "Windows"

    ```batch
    git clone https://github.com/Multiagent-AI-Lab/Antigravity-Nano-Research-Multiagentic-Core.git
    cd Antigravity-Nano-Research-Multiagentic-Core
    setup.bat
    ```

=== "Linux / macOS"

    ```bash
    git clone https://github.com/Multiagent-AI-Lab/Antigravity-Nano-Research-Multiagentic-Core.git
    cd Antigravity-Nano-Research-Multiagentic-Core
    chmod +x setup.sh
    ./setup.sh
    ```

El script de setup automáticamente:

- Crea el ambiente conda `ia_nano` (Python 3.11)
- Instala todas las dependencias científicas (ASE, RDKit, OpenMM)
- Registra el kernel de Jupyter
- Verifica la instalación

## Iniciar Jupyter

```bash
conda activate ia_nano
jupyter lab
```

## Claves API (opcional)

Para las unidades que usan LLMs, crea un archivo `.env` en la raíz:

```bash
GOOGLE_API_KEY=tu_clave_aqui
OPENROUTER_API_KEY=tu_clave_aqui
```

!!! note "Free Tier"
    Todos los notebooks incluyen fallbacks locales cuando las cuotas de API se agotan. El curso funciona sin claves de API de pago.

## Verificar Instalación

```bash
conda activate ia_nano
python verify_installation.py
```
