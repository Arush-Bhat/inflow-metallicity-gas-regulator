# References

This file lists the main physical and observational references used in the project.

The references are grouped by their role in the model.

---

## Gas-Regulator Framework

### Lilly et al. (2013)

Lilly, S. J., Carollo, C. M., Pipino, A., Renzini, A., & Peng, Y. (2013).

**Gas Regulation of Galaxies: The Evolution of the Cosmic Specific Star Formation Rate, the Metallicity--Mass--Star-formation Rate Relation, and the Stellar Content of Halos.**

*The Astrophysical Journal*, **772**, 119.

Used in this project for:

- the gas-regulator framework;
- gas-mass conservation;
- metal-mass conservation;
- the instantaneous-recycling treatment;
- the definition of the stellar yield;
- the adopted return fraction $R=0.4$;
- comparison with regulator depletion times.

---

## Atomic-to-Molecular Transition

### Krumholz, McKee & Tumlinson (2008)

Krumholz, M. R., McKee, C. F., & Tumlinson, J. (2008).

**The Atomic-to-Molecular Transition in Galaxies. I. An Analytic Approximation for Photodissociation Fronts in Finite Clouds.**

*The Astrophysical Journal*, **689**, 865--882.

Used as part of the theoretical basis for the Krumholz--McKee--Tumlinson treatment of the atomic-to-molecular transition.

---

### Krumholz, McKee & Tumlinson (2009)

Krumholz, M. R., McKee, C. F., & Tumlinson, J. (2009).

**The Atomic-to-Molecular Transition in Galaxies. II. H I and H2 Column Densities.**

*The Astrophysical Journal*, **693**, 216--235.

Used in this project for the metallicity- and surface-density-dependent molecular-gas framework.

The molecular fraction depends mainly on gas surface density and secondarily on metallicity.

---

## Molecular-Gas Star-Formation Law

### Krumholz, McKee & Tumlinson (2009)

Krumholz, M. R., McKee, C. F., & Tumlinson, J. (2009).

**The Star Formation Law in Atomic and Molecular Gas.**

*The Astrophysical Journal*, **699**, 850--856.

This is the main reference for the KMT implementation used in the project.

It provides the adopted approximations for:

- the molecular fraction $f_{\rm H_2}$;
- the metallicity variable $Z'=Z_g/Z_\odot$;
- the unresolved clumping-factor treatment;
- the molecular-gas-dependent star-formation law;
- the surface-density dependence of the star-formation prescription.

The project adopts a clumping factor

$$
c=5,
$$

motivated by the unresolved-galaxy treatment discussed in this work.

The KMT approximation is also treated cautiously at very low metallicity, approximately below

$$
Z' \sim 0.05.
$$

---

## Solar Metallicity

### Asplund et al. (2009)

Asplund, M., Grevesse, N., Sauval, A. J., & Scott, P. (2009).

**The Chemical Composition of the Sun.**

*Annual Review of Astronomy and Astrophysics*, **47**, 481--522.

Used for the adopted solar metal mass fraction

$$
Z_\odot = 0.0134.
$$

---

## Molecular-Gas Depletion Time

### Bigiel et al. (2011)

Bigiel, F., Leroy, A. K., Walter, F., Brinks, E., de Blok, W. J. G.,
Kramer, C., Rix, H.-W., Schruba, A., Schuster, K.-F.,
Usero, A., & Wiesemeyer, H. W. (2011).

**A Constant Molecular Gas Depletion Time in Nearby Disk Galaxies.**

*The Astrophysical Journal Letters*, **730**, L13.

Used as the observational motivation for the adopted depletion time

$$
\tau_{\rm dep}=2.35\ {\rm Gyr}.
$$

In the baseline one-zone model, this molecular-gas depletion time is applied to the total gas reservoir as a modelling assumption rather than as a direct observational measurement of the modeled system.

---

# Reference Roles in the Model

| Reference | Main use in this project |
|---|---|
| Lilly et al. (2013) | Gas-regulator equations, recycling, yield convention, return fraction |
| Krumholz et al. (2008) | Physical basis of the atomic-to-molecular transition |
| Krumholz et al. (2009), ApJ 693 | Molecular fraction and metallicity dependence |
| Krumholz et al. (2009), ApJ 699 | KMT molecular fraction and star-formation law |
| Asplund et al. (2009) | Solar metallicity $Z_\odot=0.0134$ |
| Bigiel et al. (2011) | Motivation for $\tau_{\rm dep}=2.35$ Gyr |

---

# Notes

These papers provide the physical and observational basis for the model, but not every parameter in the project is directly measured or taken from the literature.

Some quantities, including the mass-loading factor, effective gas radius, initial conditions and controlled inflow-metallicity grid, are adopted modelling choices.

The status and justification of every model parameter are documented separately in:

`PARAMETER_PROVENANCE.md`

The complete mathematical implementation is documented in:

`MODEL_SPECIFICATION.md`
