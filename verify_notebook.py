
import numpy as np
from ase.build import fcc100
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import os

print("✅ Librerías importadas correctamente.")

# 1. Construcción del Nanohilo
nanowire = fcc100('Au', size=(4, 4, 6), vacuum=2.0)
nanowire.center(vacuum=5.0, axis=(0, 1))
print(f"Nanohilo creado con {len(nanowire)} átomos.")

# 2. Optimización (Limpio)
nanowire.calc = EMT()
e_initial = nanowire.get_potential_energy()
print(f"Energía Inicial: {e_initial:.3f} eV")

# Usar un archivo temporal para log para no ensuciar
dyn = BFGS(nanowire, trajectory='temp_opt.traj', logfile='temp_opt.log')
dyn.run(fmax=0.05)
e_clean = nanowire.get_potential_energy()
print(f"✅ Energía Total (Limpio): {e_clean:.3f} eV")

# 3. Defecto
nanowire_defect = nanowire.copy()
center = nanowire_defect.get_center_of_mass()
distances = nanowire_defect.get_distances(np.arange(len(nanowire_defect)), center, mic=True)
atom_to_remove_index = np.argmin(distances)
del nanowire_defect[atom_to_remove_index]
print(f"Átomo eliminado. Restantes: {len(nanowire_defect)}")

# 4. Optimización Defecto
nanowire_defect.calc = EMT()
dyn_def = BFGS(nanowire_defect, trajectory='temp_opt_def.traj', logfile='temp_opt_def.log')
dyn_def.run(fmax=0.05)
e_defect = nanowire_defect.get_potential_energy()
print(f"✅ Energía Total (Defecto): {e_defect:.3f} eV")

# 5. Análisis
N_clean = len(nanowire)
mu_Au = e_clean / N_clean
e_formation = e_defect - (e_clean - mu_Au)

print(f"Resultados Finales:")
print(f"  Energía Formación: {e_formation:.3f} eV")

# Limpieza
for f in ['temp_opt.traj', 'temp_opt.log', 'temp_opt_def.traj', 'temp_opt_def.log']:
    if os.path.exists(f):
        os.remove(f)
