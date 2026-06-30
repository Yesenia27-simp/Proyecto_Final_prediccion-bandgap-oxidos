
def select_basis(element_symbol, accuracy_level="standard"):
    """
    Recommends a Gaussian Basis Set based on the element and desired accuracy.
    
    Args:
        element_symbol (str): e.g. 'H', 'C', 'Au'.
        accuracy_level (str): 'quick', 'standard', 'high_precision'.
        
    Returns:
        dict: {
            "basis": str,
            "reason": str,
            "description": str
        }
    """
    element = element_symbol.title()
    
    # Heavy metals need Relativistic ECPs
    heavy_metals = ['Au', 'Ag', 'Pt', 'Pd', 'Hg', 'Pb']
    
    if element in heavy_metals:
        return {
            "basis": "LANL2DZ",
            "reason": "Relativistic Effects",
            "description": f"{element} has core electrons moving near speed of light. LANL2DZ uses an Effective Core Potential (ECP) to handle this efficiently."
        }
        
    if accuracy_level == 'high_precision':
        return {
            "basis": "def2-TZVP",
            "reason": "Polarization & Diffuse Functions",
            "description": "Triple-zeta valence polarized. Extremely accurate for reaction energies but computationally expensive."
        }
        
    if accuracy_level == 'quick':
        return {
            "basis": "STO-3G",
            "reason": "Minimal Basis",
            "description": "Minimal basis set. Fast but qualitatively poor. Good for initial geometry debugging only."
        }
        
    # Standard default
    return {
        "basis": "6-31G(d)",
        "reason": "Standard Pople Basis",
        "description": "Split-valence with polarization on heavy atoms. The gold standard for organic molecules."
    }
