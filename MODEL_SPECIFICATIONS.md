# Model Specification

## 1. Purpose

This document gives the mathematical specification of the two models used in Project I:

1. the baseline one-zone gas regulator;
2. the metallicity-dependent KMT gas regulator.

The two models use the same gas and metal conservation framework. Their main difference is the adopted star-formation prescription.

---

# 2. Units

The internal model units are:

| Quantity | Unit |
|---|---|
| Gas mass | \(M_\odot\) |
| Stellar mass | \(M_\odot\) |
| Metal mass | \(M_\odot\) |
| Time | Gyr |
| Mass flow rate | \(M_\odot\,\mathrm{Gyr}^{-1}\) |
| Radius | kpc |
| Surface density | \(M_\odot\,\mathrm{pc}^{-2}\) |
| Metallicity | dimensionless mass fraction |

Star-formation rates are divided by \(10^9\) when displayed in

\[
M_\odot\,\mathrm{yr}^{-1}.
\]

---

# 3. State Variables

Both regulator models integrate three state variables:

\[
\mathbf{x}(t)
=
\left[
M_g(t),
M_\star(t),
M_Z(t)
\right].
\]

Here:

\[
M_g
\]

is the total gas mass of the one-zone ISM reservoir,

\[
M_\star
\]

is the mass locked into long-lived stars and stellar remnants, and

\[
M_Z
\]

is the mass of metals contained in the gas reservoir.

The gas metallicity is derived from

\[
Z_g
=
\frac{M_Z}{M_g}.
\]

---

# 4. Common Regulator Physics

## 4.1 Stellar mass return

The instantaneous recycling approximation is used.

If the instantaneous star-formation rate is

\[
\dot M_{\star,\mathrm{SF}},
\]

a fraction \(R\) is immediately returned to the gas reservoir.

The rate of long-lived stellar-mass growth is therefore

\[
\frac{dM_\star}{dt}
=
(1-R)
\dot M_{\star,\mathrm{SF}}.
\]

The quantity \(\dot M_{\star,\mathrm{SF}}\) is therefore not equal to \(dM_\star/dt\).

---

## 4.2 Galactic outflow

The gas outflow rate is proportional to the star-formation rate:

\[
\dot M_{\rm out}
=
\eta
\dot M_{\star,\mathrm{SF}},
\]

where \(\eta\) is the mass-loading factor.

The outflow is assumed to be well mixed with the ISM:

\[
Z_{\rm out}=Z_g.
\]

No outflow recycling is included in Project I.

---

## 4.3 Gas conservation

The gas mass evolves according to

\[
\boxed{
\frac{dM_g}{dt}
=
\dot M_{\rm in}
-
(1-R+\eta)
\dot M_{\star,\mathrm{SF}}
}.
\]

The first term adds gas through inflow.

The second term accounts for:

\[
(1-R)\dot M_{\star,\mathrm{SF}}
\]

being permanently locked into long-lived stars, and

\[
\eta\dot M_{\star,\mathrm{SF}}
\]

being removed by galactic outflow.

---

## 4.4 Metal conservation

The metal mass in the gas evolves according to

\[
\boxed{
\frac{dM_Z}{dt}
=
Z_{\rm in}\dot M_{\rm in}
-
Z_g(1-R+\eta)\dot M_{\star,\mathrm{SF}}
+
y(1-R)\dot M_{\star,\mathrm{SF}}
}.
\]

The terms represent:

1. metals entering with inflowing gas;
2. existing ISM metals removed by stellar locking and outflow;
3. newly produced metals returned by stars.

The yield \(y\) is defined as the newly produced metal mass returned to the ISM per unit mass locked into long-lived stars.

This is the yield convention used in Lilly et al. (2013).

---

# 5. Baseline Star-Formation Model

The baseline regulator uses

\[
\boxed{
\dot M_{\star,\mathrm{SF}}
=
\frac{M_g}{\tau_{\rm dep}}
}.
\]

The depletion time \(\tau_{\rm dep}\) is constant.

Metallicity does not appear in this relation.

Therefore, in the baseline model,

\[
Z_{\rm in}
\]

can affect

\[
M_Z
\quad\text{and}\quad
Z_g,
\]

but cannot directly affect

\[
M_g
\quad\text{or}\quad
\dot M_{\star,\mathrm{SF}}.
\]

This is why the baseline model is used as the control case.

---

# 6. Baseline Analytical Equilibrium

Gas equilibrium requires

\[
\frac{dM_g}{dt}=0.
\]

Therefore

\[
\dot M_{\rm in}
=
(1-R+\eta)
\dot M_{\star,\mathrm{SF,eq}},
\]

which gives

\[
\boxed{
\dot M_{\star,\mathrm{SF,eq}}
=
\frac{\dot M_{\rm in}}
{1-R+\eta}
}.
\]

Using the baseline star-formation law,

\[
\boxed{
M_{g,\rm eq}
=
\tau_{\rm dep}
\dot M_{\star,\mathrm{SF,eq}}
}.
\]

For metal equilibrium,

\[
\frac{dM_Z}{dt}=0.
\]

Substituting the gas-equilibrium relation gives

\[
\boxed{
Z_{\rm eq}
=
Z_{\rm in}
+
\frac{y(1-R)}
{1-R+\eta}
}.
\]

The equilibrium metallicity therefore consists of the metallicity supplied by the inflow plus a stellar-enrichment term.

---

# 7. Baseline Gas Relaxation Timescale

Substituting

\[
\dot M_{\star,\mathrm{SF}}
=
\frac{M_g}{\tau_{\rm dep}}
\]

into the gas equation gives

\[
\frac{dM_g}{dt}
=
\dot M_{\rm in}
-
\frac{1-R+\eta}
{\tau_{\rm dep}}
M_g.
\]

The regulator timescale is therefore

\[
\boxed{
\tau_{\rm reg}
=
\frac{\tau_{\rm dep}}
{1-R+\eta}
}.
\]

For constant parameters, the analytical gas-mass solution is

\[
M_g(t)
=
M_{g,\rm eq}
+
\left[
M_g(0)-M_{g,\rm eq}
\right]
e^{-t/\tau_{\rm reg}}.
\]

This relation is used conceptually to understand the numerical approach toward equilibrium.

---

# 8. KMT Molecular-Gas Model

The KMT regulator keeps the same mass and metal conservation equations.

The baseline star-formation law is replaced with a metallicity- and surface-density-dependent prescription.

---

## 8.1 Effective gas surface density

The one-zone gas reservoir has no spatial resolution.

An effective mean surface density is therefore defined by

\[
\boxed{
\Sigma_g
=
\frac{M_g}
{\pi R_{\rm gas}^2}
}.
\]

The radius is converted from kpc to pc before calculating \(\Sigma_g\).

The adopted \(R_{\rm gas}\) is a model assumption and does not represent a resolved gas-density profile.

---

## 8.2 Clumping correction

KMT define the cloud-complex surface density as

\[
\boxed{
\Sigma_{\rm comp}
=
c\Sigma_g
},
\]

where \(c\) accounts for unresolved gas structure.

The project adopts

\[
c=5.
\]

This is motivated by the value used by KMT for unresolved observations, but it is treated as a modelling assumption for this one-zone system.

---

## 8.3 Metallicity supplied to KMT

The dimensionless KMT metallicity is

\[
\boxed{
Z'
=
\frac{Z_g}{Z_\odot}
}.
\]

This is the current metallicity of the model ISM.

It is not the same quantity as

\[
Z_{\rm in}.
\]

The causal sequence is

\[
Z_{\rm in}
\rightarrow
M_Z
\rightarrow
Z_g
\rightarrow
Z'.
\]

---

# 9. KMT Molecular Fraction

The molecular fraction is

\[
\boxed{
f_{\rm H_2}
=
1-
\left[
1+
\left(
\frac{3}{4}
\frac{s}{1+\delta}
\right)^{-5}
\right]^{-1/5}
}.
\]

The intermediate quantities are

\[
s
=
\frac{
\ln(1+0.6\chi)
}
{
0.04\Sigma_{\rm comp,0}Z'
},
\]

\[
\chi
=
0.77
\left(
1+3.1Z'^{0.365}
\right),
\]

and

\[
\delta
=
0.0712
\left(
0.1s^{-1}+0.675
\right)^{-2.8}.
\]

The normalized complex surface density is

\[
\Sigma_{\rm comp,0}
=
\frac{
\Sigma_{\rm comp}
}{
1\,M_\odot\,\mathrm{pc}^{-2}
}.
\]

The numerical implementation clips the final molecular fraction to

\[
0
\leq
f_{\rm H_2}
\leq
1.
\]

The KMT approximation becomes less reliable for approximately

\[
Z'<0.05.
\]

The production simulations used in this project remain above this ISM-metallicity regime.

---

# 10. Molecular Gas Mass

The molecular-gas mass is calculated from

\[
\boxed{
M_{\rm H_2}
=
f_{\rm H_2}M_g
}.
\]

This distinction is important because an increasing molecular fraction does not necessarily imply an increasing absolute molecular mass if the total gas reservoir decreases.

---

# 11. KMT Star-Formation Law

The KMT star-formation surface density is

\[
\boxed{
\dot\Sigma_\star
=
f_{\rm H_2}
\frac{\Sigma_g}
{2.6\,\mathrm{Gyr}}
F(\Sigma_g)
},
\]

where

\[
F(\Sigma_g)
=
\begin{cases}
\left(
\dfrac{\Sigma_g}
{85\,M_\odot\,\mathrm{pc}^{-2}}
\right)^{-0.33},
&
\Sigma_g
<
85\,M_\odot\,\mathrm{pc}^{-2},
\\[10pt]
\left(
\dfrac{\Sigma_g}
{85\,M_\odot\,\mathrm{pc}^{-2}}
\right)^{0.33},
&
\Sigma_g
>
85\,M_\odot\,\mathrm{pc}^{-2}.
\end{cases}
\]

The global star-formation rate is obtained by multiplying by the model disk area:

\[
\boxed{
\dot M_{\star,\mathrm{SF}}
=
\dot\Sigma_\star
\pi R_{\rm gas}^2
}.
\]

The resulting units are

\[
M_\odot\,\mathrm{Gyr}^{-1}.
\]

---

# 12. KMT Regulator Coupling

The full KMT regulator contains the pathway

\[
\boxed{
Z_{\rm in}
\rightarrow
Z_g(t)
\rightarrow
Z'(t)
\rightarrow
f_{\rm H_2}(t)
\rightarrow
\dot M_{\star,\mathrm{SF}}(t)
}.
\]

Changing the SFR then changes:

\[
\frac{dM_g}{dt},
\]

\[
\frac{dM_\star}{dt},
\]

\[
\frac{dM_Z}{dt},
\]

and

\[
\dot M_{\rm out}.
\]

This creates an internal dynamical coupling.

It is not yet a complete baryon-cycle feedback loop because there is no evolving CGM reservoir or reaccretion.

---

# 13. KMT Equilibrium

Although the KMT star-formation law is nonlinear, the equilibrium mass-flow relation is unchanged.

Gas equilibrium still requires

\[
\boxed{
\dot M_{\star,\mathrm{SF,eq}}
=
\frac{\dot M_{\rm in}}
{1-R+\eta}
}.
\]

Metal equilibrium also remains

\[
\boxed{
Z_{\rm eq}
=
Z_{\rm in}
+
\frac{y(1-R)}
{1-R+\eta}
}.
\]

These relations depend on conservation rather than on the detailed form of the star-formation law.

However, the KMT equilibrium gas mass is no longer given by

\[
M_{g,\rm eq}
=
\tau_{\rm dep}
\dot M_{\star,\mathrm{SF,eq}}.
\]

Instead, the equilibrium gas mass must satisfy the nonlinear KMT star-formation relation.

---

# 14. Adopted Final Parameters

The production model uses

\[
Z_\odot=0.0134,
\]

\[
M_{g,0}
=
5\times10^9\,M_\odot,
\]

\[
M_{\star,0}
=
5\times10^{10}\,M_\odot,
\]

\[
Z_{g,0}
=
0.5Z_\odot,
\]

\[
R=0.4,
\]

\[
\eta=0.5,
\]

\[
y=0.016,
\]

and for the baseline model

\[
\tau_{\rm dep}
=
2.35\,\mathrm{Gyr}.
\]

The common inflow rate is defined by

\[
\dot M_{\rm in}
=
(1-R+\eta)
\frac{M_{g,0}}
{\tau_{\rm dep}},
\]

giving approximately

\[
\dot M_{\rm in}
=
2.34\,M_\odot\,\mathrm{yr}^{-1}.
\]

The KMT extension adopts

\[
R_{\rm gas}=10\,\mathrm{kpc}
\]

and

\[
c=5.
\]

The evidence status and justification of each value are documented separately in `PARAMETER_PROVENANCE.md`.

---

# 15. Controlled Experiment

The only deliberately varied model parameter in the final experiment is

\[
Z_{\rm in}.
\]

The adopted grid is

\[
\boxed{
\frac{Z_{\rm in}}{Z_\odot}
=
[
0,
0.05,
0.10,
0.30,
0.50,
1.00
]
}.
\]

Every run begins with the same initial conditions and uses the same values of all other parameters.

The baseline and KMT models are both run over this grid.

This allows the effect of adding metallicity-dependent molecular physics to be isolated.

---

# 16. Numerical Integration

The differential equations are integrated with

```text
scipy.integrate.solve_ivp