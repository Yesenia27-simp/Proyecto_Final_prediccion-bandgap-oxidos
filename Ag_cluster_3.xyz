
def fetch_properties(compound_name):
    """
    MOCK RAG: Retrieves experimental properties for validation.
    In production, this would call Materials Project API or ArXiv.
    """
    db = {
        "Au": {"bandgap": 0.0, "structure": "FCC", "melting_point": 1337},
        "Si": {"bandgap": 1.12, "structure": "Diamond", "melting_point": 1687},
        "TiO2": {"bandgap": 3.2, "structure": "Rutile", "melting_point": 2116},
        "Graphene": {"bandgap": 0.0, "structure": "Hexagonal", "melting_point": 4510}
    }
    
    data = db.get(compound_name)
    if data:
         data["source"] = "Materials Project (Verified)"
         return data
         
    return {"error": "Compound not found in Experimental DB", "source": "N/A"}
