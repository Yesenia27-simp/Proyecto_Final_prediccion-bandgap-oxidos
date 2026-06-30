# Installation Guide

## Prerequisites

| Tool | Version | Notes |
|------|---------|-------|
| Python | 3.11 | Via conda recommended |
| Conda | Latest | Miniconda or Anaconda |
| Git | Latest | |
| RAM | 8 GB min | 16 GB recommended for Unit 5 |
| Disk | 5 GB | For conda environment + notebooks |

## Automatic Installation

=== "Windows"

    ```batch
    setup.bat
    ```

=== "Linux / macOS"

    ```bash
    chmod +x setup.sh && ./setup.sh
    ```

## Manual Installation

```bash
conda create -n ia_nano python=3.11 -y
conda activate ia_nano
pip install -r requirements.txt
python -m ipykernel install --user --name ia_nano --display-name "Python (ia_nano)"
```

## Verify

```bash
python verify_installation.py
```

Expected output:
```
✓ ASE installed
✓ RDKit installed
✓ PyTorch installed
✓ Google ADK installed
✓ LangChain installed
✓ All checks passed
```

## Troubleshooting

### RDKit not found
```bash
conda install -c conda-forge rdkit
```

### OpenMM GPU issues
```bash
conda install -c conda-forge openmm cudatoolkit
```

### Google ADK import errors
```bash
pip install google-adk --upgrade
```

!!! tip
    See [INSTALL.md](https://github.com/Multiagent-AI-Lab/Antigravity-Nano-Research-Multiagentic-Core/blob/main/INSTALL.md) in the repository for the complete troubleshooting guide.
