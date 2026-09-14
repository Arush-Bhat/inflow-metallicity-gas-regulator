# Part I Parameter Provenance and Assumption Audit

This document records the origin and modelling status of the quantities used
in the Part I one-zone gas-regulator and KMT models.

The classifications are:

- SOURCE: directly adopted from a literature source.
- ADOPTED ASSUMPTION: chosen for the present model, possibly with literature motivation.
- CONTROLLED VARIABLE: deliberately varied in the experiment.
- INITIAL CONDITION: specifies the starting state of a simulation.
- DERIVED: calculated from other model quantities.
- NUMERICAL SETTING: controls numerical integration rather than the physical model.


## Parameter provenance

| Quantity | Adopted value | Units | Status | Reason / source |
|---|---:|---|---|---|
| $Z_\odot$ | 0.0134 | dimensionless mass fraction | SOURCE | Present-day solar metal mass fraction from Asplund et al. (2009). |
| $M_{g,0}$ | $5\times10^9$ | $M_\odot$ | INITIAL CONDITION | Representative starting gas mass; not fitted to a particular observed galaxy. |
| $M_{\star,0}$ | $5\times10^{10}$ | $M_\odot$ | INITIAL CONDITION | Representative starting stellar mass; not fitted to a particular observed galaxy. |
| $Z_{g,0}$ | $0.5Z_\odot$ | dimensionless mass fraction | INITIAL CONDITION | Representative initial ISM metallicity. |
| $R$ | 0.4 | dimensionless | SOURCE | Instantaneous return fraction adopted in Lilly et al. (2013). |
| $y$ | 0.016 | dimensionless | SOURCE | Metal yield per unit mass locked into long-lived stars, consistent with the value discussed by Lilly et al. (2013). |
| $\eta$ | 0.5 | dimensionless | ADOPTED ASSUMPTION | Representative mass-loading factor. Literature-motivated but not independently calibrated in this project. |
| $\tau_{\rm dep}$ | 2.35 | Gyr | ADOPTED ASSUMPTION | Representative one-zone depletion timescale. Motivated by molecular-gas depletion times reported by Bigiel et al. (2011); applying it to the total one-zone reservoir is a modelling assumption. |
| $\dot M_{\rm in}$ | 2.34 | $M_\odot\,{\rm yr}^{-1}$ | DERIVED | Defined from $(1-R+\eta)M_{g,0}/\tau_{\rm dep}$ so that the baseline model begins in gas-mass equilibrium. |
| $R_{\rm gas}$ | 10 | kpc | ADOPTED ASSUMPTION | Effective fixed gas radius used to convert one-zone gas mass into mean surface density. |
| $c$ | 5 | dimensionless | ADOPTED ASSUMPTION | KMT-motivated clumping factor representing unresolved gas structure. KMT use approximately this value for unresolved THINGS data, but it is not measured for this model. |
| $Z_{\rm in}/Z_\odot$ | $[0,0.05,0.10,0.30,0.50,1.00]$ | dimensionless | CONTROLLED VARIABLE | Deliberately varied to test the effect of inflow metallicity. |
| Integration interval | 0--10 | Gyr | NUMERICAL SETTING | Chosen to follow transient evolution and approach toward quasi-equilibrium; not intended as a detailed reconstruction of a real galaxy history. |
| Number of time samples | 1001 | — | NUMERICAL SETTING | Output sampling for numerical integration and plotting. |


## Model assumptions

### Baseline regulator

1. The galaxy is represented by a single well-mixed gas reservoir.
2. The inflow rate is constant during each simulation.
3. The inflow metallicity is constant within each simulation.
4. Stellar mass return is treated using the instantaneous recycling approximation.
5. The return fraction $R$ is constant.
6. The stellar yield $y$ is constant.
7. Outflow is proportional to star formation:
   $$
   \dot M_{\rm out}=\eta\dot M_{\star,\rm SF}.
   $$
8. The mass-loading factor $\eta$ is constant.
9. Outflowing gas has the same metallicity as the well-mixed ISM:
   $$
   Z_{\rm out}=Z_g.
   $$
10. The baseline star-formation law is
    $$
    \dot M_{\star,\rm SF}=\frac{M_g}{\tau_{\rm dep}},
    $$
    with constant depletion time.
11. Outflowing material is removed from the model and is not recycled through an evolving CGM.
12. No explicit spatial structure, halo evolution, redshift evolution, or CGM reservoir is followed.


### KMT extension

1. The baseline mass and metal conservation equations are retained.
2. The baseline star-formation prescription is replaced by the KMT molecular-gas-dependent prescription.
3. The one-zone gas mass is converted to an effective mean surface density using
   $$
   \Sigma_g=\frac{M_g}{\pi R_{\rm gas}^2}.
   $$
4. The effective gas radius $R_{\rm gas}$ is fixed in time.
5. Unresolved gas structure is represented by
   $$
   \Sigma_{\rm comp}=c\Sigma_g,
   $$
   with constant clumping factor $c$.
6. The metallicity supplied to the KMT prescription is the evolving ISM metallicity
   $$
   Z'=\frac{Z_g}{Z_\odot},
   $$
   not the inflow metallicity directly.
7. Inflow metallicity affects star formation through the causal pathway
   $$
   Z_{\rm in}
   \rightarrow Z_g
   \rightarrow f_{\rm H_2}
   \rightarrow \dot M_{\star,\rm SF}.
   $$
8. The KMT approximation has reduced reliability below approximately
   $Z'\sim0.05$.## Parameter and assumption provenance

All physical parameters, initial conditions, controlled variables, derived
quantities, and numerical settings are documented separately in
`PARAMETER_PROVENANCE.md`.

This distinction is important because not every numerical value in the model
has the same evidential status. Some quantities are taken directly from the
literature, some are explicit modelling assumptions, some define the initial
state, and $Z_{\rm in}$ is the controlled experimental variable.
9. The model does not yet contain an evolving CGM, reaccretion, or baryon-cycle recycling. Those processes belong to the subsequent project.


## Experimental distinction

The independent variable is

$$
Z_{\rm in}.
$$

The main evolving response variables are

$$
Z_g(t),\quad
f_{\rm H_2}(t),\quad
\dot M_\star(t),\quad
M_g(t),\quad
M_\star(t).
$$

Therefore $Z_{\rm in}$ must not be confused with $Z_g$ or with
$Z'=Z_g/Z_\odot$.