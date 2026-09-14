# KMT molecular star formation coupled to the one zone gas regulator

import numpy as np
from scipy.integrate import solve_ivp

def gas_surface_density(M_g, R_gas):
    return M_g / (np.pi * (R_gas * 1000.0)**2)

def molecular_fraction(Sigma_g, Z_prime, clumping_factor):
    Sigma_comp = clumping_factor * Sigma_g
    chi = 0.77 * (1.0 + 3.1 * Z_prime**0.365)
    s = np.log(1.0 + 0.6 * chi) / (0.04 * Sigma_comp * Z_prime)
    delta = 0.0712 * (0.1 / s + 0.675)**(-2.8)
    f_H2 = 1.0 - (1.0 + (0.75 * s / (1.0 + delta))**(-5.0))**(-0.2)
    return np.clip(f_H2, 0.0, 1.0)

def kmt_values(M_g, Z_g, params):
    Sigma_g = gas_surface_density(M_g, params["R_gas"])
    Z_prime = Z_g / params["Z_sun"]
    f_H2 = molecular_fraction(Sigma_g, Z_prime, params["clumping_factor"])
    correction = np.where(Sigma_g < 85.0, (Sigma_g / 85.0)**(-0.33), (Sigma_g / 85.0)**0.33)
    Mdot_star = f_H2 * M_g / 2.6 * correction
    return {"Z_prime": Z_prime, "Sigma_g": Sigma_g, "f_H2": f_H2, "M_H2": f_H2 * M_g, "Mdot_star": Mdot_star}

def derivatives(t, state, params):
    M_g, M_star, M_Z = state
    R, eta, y, Z_in = params["R"], params["eta"], params["y"], params["Z_in"]
    Z_g = M_Z / M_g
    Mdot_star = kmt_values(M_g, Z_g, params)["Mdot_star"]
    dM_g = params["Mdot_in"] - (1 - R + eta) * Mdot_star
    dM_star = (1 - R) * Mdot_star
    dM_Z = Z_in * params["Mdot_in"] - Z_g * (1 - R + eta) * Mdot_star + y * (1 - R) * Mdot_star
    return [dM_g, dM_star, dM_Z]

def run_model(params, initial, t):
    state0 = [initial["M_g"], initial["M_star"], initial["Z_g"] * initial["M_g"]]
    solution = solve_ivp(lambda time, state: derivatives(time, state, params), (t[0], t[-1]), state0, t_eval=t, rtol=1e-8)
    if not solution.success:
        raise RuntimeError(solution.message)
    return solution

def quantities(solution, params):
    M_g, M_Z = solution.y[0], solution.y[2]
    Z_g = M_Z / M_g
    values = kmt_values(M_g, Z_g, params)
    return {"Z_g": Z_g, **values, "Mdot_out": params["eta"] * values["Mdot_star"]}

def equilibrium_values(params):
    R, eta = params["R"], params["eta"]
    return {"Mdot_star": params["Mdot_in"] / (1 - R + eta), "Z_g": params["Z_in"] + params["y"] * (1 - R) / (1 - R + eta)}