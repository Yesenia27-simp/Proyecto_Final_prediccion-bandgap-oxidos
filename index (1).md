# Quick Start

## Requirements

- Python 3.11
- Conda or Miniconda
- Git

## Installation

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

The setup script automatically:

- Creates the `ia_nano` conda environment (Python 3.11)
- Installs all scientific dependencies (ASE, RDKit, OpenMM)
- Registers the Jupyter kernel
- Verifies the installation

## Launch Jupyter

```bash
conda activate ia_nano
jupyter lab
```

## API Keys (optional)

For units that use LLMs, create a `.env` file in the root:

```bash
GOOGLE_API_KEY=your_key_here
OPENROUTER_API_KEY=your_key_here
```

!!! note "Free Tier"
    All notebooks include local fallbacks when API quotas are exhausted. The course works without paid API keys.

## Verify Installation

```bash
conda activate ia_nano
python verify_installation.py
```
