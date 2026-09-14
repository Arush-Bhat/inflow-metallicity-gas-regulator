# Shared parameters and initial conditions for both regulator models
# Masses use Msun time uses Gyr radius uses kpc and metallicity is a mass fraction

import numpy as np

Z_SUN = 0.0134
M_G0 = 5e9
M_STAR0 = 5e10
Z_G0 = 0.5 * Z_SUN
R = 0.4
ETA = 0.5
Y = 0.016
TAU_DEP = 2.35 # Gyr; adopted one-zone depletion timescale
MDOT_IN = (1 - R + ETA) * M_G0 / TAU_DEP

BASE_PARAMS = {"Mdot_in": MDOT_IN, "R": R, "eta": ETA, "tau_dep": TAU_DEP, "y": Y, "Z_in": 0.1 * Z_SUN}
KMT_PARAMS = {
    "Mdot_in": MDOT_IN,
    "R": R,
    "eta": ETA,
    "y": Y,
    "Z_in": 0.1 * Z_SUN,
    "Z_sun": Z_SUN,

    # One-zone geometric / unresolved-structure assumptions
    "R_gas": 10.0,
    "clumping_factor": 5.0
}
INITIAL = {"M_g": M_G0, "M_star": M_STAR0, "Z_g": Z_G0}
Z_IN_VALUES = Z_SUN * np.array([0.0, 0.05, 0.10, 0.30, 0.50, 1.00])
TIME = np.linspace(0.0, 10.0, 1001)