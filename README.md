# Testing the Effect of Inflow Metallicity on Molecular Gas and Star Formation in a One-Zone Gas-Regulator Model

## Overview

This project studies whether the metallicity of gas entering a galaxy can affect its later molecular-gas content and star-formation history.

A simple one-zone gas-regulator model is used. The project first constructs a metallicity-independent baseline model that acts as a control. A second model then includes the metallicity-dependent molecular-gas and star-formation prescription of Krumholz, McKee and Tumlinson (KMT).

The main controlled variable is the inflow metallicity,

$$Z_{\rm in}$$

The purpose of the project is not to reproduce the detailed evolution of a specific observed galaxy. Instead, it tests whether changing inflow metallicity can produce a measurable dynamical response under simple and controlled assumptions.

---

## Research Question

Does changing the metallicity of gas inflowing into a one-zone galaxy model produce a measurable change in its molecular-gas content and star-formation history?

A secondary question is whether such a response appears only after a metallicity-dependent molecular-gas prescription is included.

---

## Hypotheses

### Null hypothesis

Changing the inflow metallicity mainly changes the chemical evolution of the galaxy and does not significantly affect gas consumption or star formation when the star-formation prescription is independent of metallicity.

### Alternative hypothesis

When a metallicity-dependent molecular-gas prescription is included, changing the inflow metallicity produces a measurable change in the molecular fraction and star-formation history.

The experiment does not assume beforehand that higher metallicity must produce a higher final star-formation rate.

---

## Model Structure

Two related models are used.

### 1. Baseline gas regulator

The baseline model follows:

- gas mass $M_g$
- stellar mass $M_\star$
- gas metal mass $M_Z$
- gas metallicity $Z_g=M_Z/M_g$

The baseline star-formation law is

$$\dot M_{\star,\mathrm{SF}}=\frac{M_g}{\tau_{\rm dep}}$$

Metallicity does not enter this star-formation law. The baseline model therefore acts as a control experiment.

### 2. KMT regulator

The KMT model keeps the same mass and metal conservation framework but replaces the baseline star-formation prescription with a metallicity- and surface-density-dependent molecular-gas prescription.

The main causal pathway is

$$Z_{\rm in} \rightarrow Z_g \rightarrow Z' \rightarrow f_{\rm H_2} \rightarrow \dot M_{\star,\mathrm{SF}}, $$

where

$$Z' = \frac{Z_g}{Z_\odot}$$

---

## Main Equations

The gas mass evolves as

$$\frac{dM_g}{dt} = \dot M_{\rm in} - (1-R+\eta)\dot M_{\star,\mathrm{SF}}$$

The long-lived stellar mass evolves as

$$\frac{dM_\star}{dt} = (1-R)\dot M_{\star,\mathrm{SF}}$$

The gas metal mass evolves as

$$\frac{dM_Z}{dt} = Z_{\rm in}\dot M_{\rm in} - Z_g(1-R+\eta)\dot M_{\star,\mathrm{SF}} + y(1-R)\dot M_{\star,\mathrm{SF}}$$

The analytical equilibrium star-formation rate is

$$\dot M_{\star,\mathrm{SF,eq}} = \frac{\dot M_{\rm in}} {1-R+\eta}$$

The analytical equilibrium metallicity is

$$Z_{\rm eq} = Z_{\rm in} + \frac{y(1-R)}{1-R+\eta}$$

A complete mathematical description is given in `MODEL_SPECIFICATION.md`.

---

## Final Model Parameters

The final model uses:

- $Z_\odot=0.0134$
- $M_{g,0}=5\times10^9\,M_\odot$
- $M_{\star,0}=5\times10^{10}\,M_\odot$
- $Z_{g,0}=0.5Z_\odot$
- $R=0.4$
- $\eta=0.5$
- $y=0.016$
- $\tau_{\rm dep}=2.35$ Gyr for the baseline model
- $R_{\rm gas}=10$ kpc for the KMT model
- clumping factor $c=5$

The inflow rate is defined from the baseline equilibrium condition,

$$\dot M_{\rm in} = (1-R+\eta) \frac{M_{g,0}}{\tau_{\rm dep}}$$

giving approximately

$$ \dot M_{\rm in} = 2.34\,M_\odot\,{\rm yr}^{-1}$$

The full origin, status and justification of each value are listed in `PARAMETER_PROVENANCE.md`.

---

## Controlled Inflow-Metallicity Grid

The final experiment varies

$$ \frac{Z_{\rm in}}{Z_\odot} = [0,\ 0.05,\ 0.10,\ 0.30,\ 0.50,\ 1.00]$$

All other parameters and initial conditions are kept fixed.

---

## Main Result

The baseline model behaves as expected: changing inflow metallicity changes the chemical evolution but does not change the gas-mass or star-formation histories.

The KMT model gives a different result.

Higher inflow metallicity increases the evolving ISM metallicity and molecular fraction, which produces a measurable transient difference in star formation.

For the adopted parameter set, the largest point-by-point SFR difference relative to the pristine-inflow KMT run is approximately

$$14.4\%.$$

This occurs for

$$Z_{\rm in}=Z_\odot.$$

The different KMT runs still approach nearly the same late-time star-formation rate because the equilibrium mass flow remains constrained by the fixed inflow rate, return fraction and mass-loading factor.

The gas reservoir instead adjusts. More metal-rich runs require less total gas to maintain approximately the same equilibrium SFR.

The exact size of the transient response depends on model assumptions such as gas radius and clumping factor. The $14.4\%$ result should therefore be interpreted as a result of this specific model setup, not as a universal prediction for real galaxies.

---

## Numerical Validation

The baseline and KMT models were checked before the final experiment.

The tests include:

- analytical equilibrium comparison
- gas-mass convergence toward equilibrium
- metallicity convergence toward equilibrium
- total mass conservation
- molecular-fraction bounds
- qualitative KMT behaviour with metallicity and surface density
- KMT regulator equilibrium behaviour

The final numerical mass-budget residuals are very small compared with the total system mass.

---

## Project Structure

```text
Part I - Gas Regulator/
│
├── README.md
├── requirements.txt
├── PARAMETER_PROVENANCE.md
├── MODEL_SPECIFICATION.md
│
├── model/
│   ├── parameters.py
│   ├── gas_regulator.py
│   └── kmt_regulator.py
│
├── notebooks/
│   ├── 01_model_framework.ipynb
│   ├── 02_baseline_validation.ipynb
│   ├── 03_kmt_validation.ipynb
│   └── 04_inflow_metallicity_experiments.ipynb
│
└── output/
    ├── figures/
    └── tables/
