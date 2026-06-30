"""
Verification Script for Antigravity Nano Research Multiagentic Core
====================================================================
This script verifies that all dependencies are correctly installed.
"""

import sys
import importlib

def check_python_version():
    """Verify Python version is 3.11.x"""
    print("\n🐍 Verificando versión de Python...")
    version = sys.version_info
    if version.major == 3 and version.minor == 11:
        print(f"   ✓ Python {version.major}.{version.minor}.{version.micro} (Correcto)")
        return True
    else:
        print(f"   ✗ Python {version.major}.{version.minor}.{version.micro}")
        print(f"   ⚠️  Se recomienda Python 3.11 para máxima compatibilidad")
        return False

def check_dependencies():
    """Verify critical dependencies can be imported"""
    print("\n📦 Verificando dependencias críticas...")
    
    critical_deps = {
        'numpy': 'NumPy',
        'pandas': 'Pandas',
        'scipy': 'SciPy',
        'matplotlib': 'Matplotlib',
        'ase': 'ASE (Atomic Simulation Environment)',
        'rdkit': 'RDKit',
        'mendeleev': 'Mendeleev',
        'sympy': 'SymPy',
    }
    
    all_ok = True
    for module_name, display_name in critical_deps.items():
        try:
            if module_name == 'rdkit':
                importlib.import_module('rdkit.Chem')
            else:
                importlib.import_module(module_name)
            print(f"   ✓ {display_name}")
        except ImportError as e:
            print(f"   ✗ {display_name} - NO ENCONTRADO")
            all_ok = False
    
    return all_ok

def check_external_skills():
    """Verify external skills can be imported"""
    print("\n🛠️  Verificando External Skills...")
    
    skills = [
        ('external_skills.numerical.stability_guardian', 'Stability Guardian'),
        ('external_skills.numerical.basis_set_architect', 'Basis Set Architect'),
        ('external_skills.ai_mining.toxicity_predictor', 'Toxicity Predictor'),
        ('external_skills.pedagogy.socratic_debugger', 'Socratic Debugger'),
        ('external_skills.orchestration.librarian_rag', 'Librarian RAG'),
    ]
    
    all_ok = True
    for module_path, display_name in skills:
        try:
            importlib.import_module(module_path)
            print(f"   ✓ {display_name}")
        except ImportError as e:
            print(f"   ✗ {display_name} - ERROR: {e}")
            all_ok = False
    
    return all_ok

def check_jupyter_kernel():
    """Check if Jupyter kernel is registered"""
    print("\n📓 Verificando kernel Jupyter...")
    try:
        import jupyter_client
        km = jupyter_client.kernelspec.KernelSpecManager()
        kernels = km.get_all_specs()
        
        if 'ia_nano' in kernels:
            print("   ✓ Kernel 'ia_nano' registrado")
            return True
        else:
            print("   ✗ Kernel 'ia_nano' NO encontrado")
            print("   ℹ️  Ejecuta: python -m ipykernel install --user --name=ia_nano")
            return False
    except Exception as e:
        print(f"   ⚠️  No se pudo verificar kernels: {e}")
        return False

def main():
    """Run all verification checks"""
    print("=" * 70)
    print(" Verificación de Instalación - Antigravity Nano Research")
    print("=" * 70)
    
    results = []
    results.append(check_python_version())
    results.append(check_dependencies())
    results.append(check_external_skills())
    results.append(check_jupyter_kernel())
    
    print("\n" + "=" * 70)
    if all(results):
        print(" ✅ VERIFICACIÓN COMPLETA - Todo está correctamente instalado")
        print("=" * 70)
        print("\n💡 Próximo paso:")
        print("   conda activate ia_nano")
        print("   jupyter lab")
        return 0
    else:
        print(" ⚠️  VERIFICACIÓN INCOMPLETA - Algunos componentes faltan")
        print("=" * 70)
        print("\n📖 Consulta INSTALL.md para troubleshooting")
        return 1

if __name__ == "__main__":
    sys.exit(main())
