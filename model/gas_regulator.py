# Simple one zone gas regulator used as the baseline model

from scipy.integrate import solve_ivp

def sfr(M_g, tau_dep):
    return M_g / tau_dep

def derivatives(t, state, params):
    M_g, M_star, M_Z = state
    Mdot_in, R, eta, tau_dep, y, Z_in = params["Mdot_in"], params["R"], params["eta"], params["tau_dep"], params["y"], params["Z_in"]
    Z_g = M_Z / M_g
    Mdot_star = sfr(M_g, tau_dep)
    dM_g = Mdot_in - (1 - R + eta) * Mdot_star
    dM_star = (1 - R) * Mdot_star
    dM_Z = Z_in * Mdot_in - Z_g * (1 - R + eta) * Mdot_star + y * (1 - R) * Mdot_star
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
    Mdot_star = sfr(M_g, params["tau_dep"])
    return {"Z_g": Z_g, "Mdot_star": Mdot_star, "Mdot_out": params["eta"] * Mdot_star}

def equilibrium_values(params):
    R, eta = params["R"], params["eta"]
    Mdot_star = params["Mdot_in"] / (1 - R + eta)
    return {"M_g": params["tau_dep"] * Mdot_star, "Mdot_star": Mdot_star, "Z_g": params["Z_in"] + params["y"] * (1 - R) / (1 - R + eta)}