
import numpy as np

def analyze_timestep(dt_fs, simulation_type="MD", bond_types=None):
    """
    Analyzes if a timestep is safe for a given Molecular Dynamics simulation.
    
    Args:
        dt_fs (float): Timestep in femtoseconds.
        simulation_type (str): Type of simulation ('MD', 'Langevin', 'Brownian').
        bond_types (list): List of bond types present e.g. ['C-H', 'O-H', 'Au-Au'].
    
    Returns:
        dict: {
            "safe": bool,
            "max_recommended_dt": float,
            "message": str,
            "risk_level": str ("LOW", "MEDIUM", "CRITICAL")
        }
    """
    if bond_types is None:
        bond_types = []
        
    crit_dt = 2.0 # Standard soft limit for generic MD
    message = "Timestep appears normal."
    risk = "LOW"
    
    # Hydrogen bonds vibrate fast (10fs period), requiring dt < 1.0fs usually (or 2fs with SHAKE)
    has_hydrogen = any('H' in b for b in bond_types)
    
    if has_hydrogen:
        crit_dt = 1.0
        if dt_fs > crit_dt:
            risk = "CRITICAL"
            message = f"Unstable! C-H/O-H bonds vibrate ~10fs. dt={dt_fs}fs will cause energy drift. Use SHAKE or reduce dt < {crit_dt}fs."
            return {"safe": False, "max_recommended_dt": crit_dt, "message": message, "risk_level": risk}
            
    if dt_fs > 2.0:
        risk = "MEDIUM"
        message = f"High timestep ({dt_fs}fs). Energy conservation not guaranteed for standard potentials."
        if dt_fs > 5.0:
            risk = "CRITICAL"
            message = f"Explosion Imminent! dt={dt_fs}fs is too large for atomic MD."
            return {"safe": False, "max_recommended_dt": 2.0, "message": message, "risk_level": risk}

    return {
        "safe": True,
        "max_recommended_dt": crit_dt,
        "message": "Timestep safe. Energy drift should be minimal.",
        "risk_level": risk
    }
