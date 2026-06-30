# .gitignore for Antigravity Nano Research Multiagentic Core

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual Environments
ia_nano/
venv/
ENV/
env/
.venv
.conda/

# Jupyter Notebook
.ipynb_checkpoints
*.ipynb_checkpoints/

# Environment variables
.env
.env.local
*.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# Data files (large datasets should not be in repo)
*.h5
*.hdf5
*.nc
*.cdf
data/raw/*
!data/raw/.gitkeep

# Temporary files
*.tmp
*.temp
*.log
*.bak

# OS specific
Thumbs.db
.DS_Store
*.lnk

# Materials Project API keys
.mp_api_key
mp_config.json

# Simulation outputs (large files)
*.xyz
*.pdb
*.traj
*.dump
