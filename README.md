# Advanced Mechanistic Ophthalmology: Retinal Oxygenation Model

A computational model for simulating oxygen transport and metabolic consumption in retinal tissue using a 1D reaction-diffusion framework. This project implements a finite-difference numerical solution to the time-dependent oxygen distribution field within a simplified retinal geometry.

The model is designed to capture the interaction between tissue diffusion, oxygen supply from the choroidal boundary, metabolic consumption by retinal cells, and spatial gradients in oxygen tension relevant to ischemic or hypoxic conditions.

## Why this project exists

Retinal tissue is highly metabolically active and extremely sensitive to oxygen supply and local consumption imbalance. This model provides a mechanistic description of oxygen dynamics in a simplified retinal slice, allowing analysis of how oxygen concentration changes over depth and time.

Rather than relying on purely statistical or empirical fits, this framework is based on a physics-informed system:

- oxygen diffuses through tissue
- oxygen is consumed by metabolic activity
- boundary conditions reflect anatomical supply and geometric constraints

This makes the model useful as a baseline for studying retinal oxygenation, hypoxia risk, and the influence of parameter changes on spatial oxygen profiles.

## Governing equation

The oxygen concentration field C(x, t) is modelled using a nonlinear reaction-diffusion equation:

\[
\frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2} - \frac{V_{max} C}{K_m + C}
\]

where:

- C(x, t) is the local oxygen concentration
- D is the diffusion coefficient
- Vmax is the maximum metabolic consumption rate
- Km is the Michaelis constant for oxygen-dependent consumption

### Interpretation of the terms

- dC/dt: local change in oxygen concentration over time
- D * d^2C/dx^2: diffusion-driven redistribution of oxygen
- (Vmax * C) / (Km + C): nonlinear oxygen consumption due to retinal metabolic activity

## Boundary conditions

To represent the anatomical structure of the retinal domain, the model applies the following boundary constraints:

1. Choroidal boundary at x = 0

   Oxygen is continuously supplied from the choroid:

   \[
   C(0, t) = C_{choroid}
   \]

2. Inner retinal boundary at x = L

   A zero-flux condition is imposed to represent a no-net-flow internal boundary:

   \[
   \left.\frac{\partial C}{\partial x}\right|_{x=L} = 0
   \]

These conditions create a biologically informed setup in which oxygen enters from the outer support boundary and is consumed within the tissue.

## Numerical method

The simulation uses an explicit finite-difference scheme in a 1D spatial domain.

The time step is constrained by the stability requirement:

\[
\Delta t \le \frac{\Delta x^2}{2D}
\]

This ensures the explicit method remains numerically stable for the diffusion term.

The implementation updates the concentration field iteratively:

- compute diffusion at each internal grid point
- compute nonlinear metabolic consumption
- advance the concentration in time
- enforce boundary values at each iteration

## Repository contents

This repository currently contains the core simulation logic in:

- simulation.py — numerical solver, parameter setup, and visualization

## Getting started

### Requirements

This project requires:

- Python 3.x
- NumPy
- Matplotlib

Install the dependencies using:

```bash
pip install numpy matplotlib
```

## Run the simulation

From the repository root:

```bash
python simulation.py
```

This will generate a plot of the spatial oxygen profile across the retinal depth after the model reaches steady-state behaviour.

## Model parameters

The current implementation uses a representative retinal slice with parameters such as:

- domain length: L = 0.025 cm
- diffusion coefficient: D = 2.0 x 10^-5 cm^2/s
- max consumption rate: Vmax = 1.2 x 10^-4
- Michaelis constant: Km = 1.0 x 10^-6
- oxygen supply at choroid: C_choroid = 6.5 x 10^-5

These values are intended as a biologically motivated baseline for exploring oxygen transport dynamics.

## Example output

The script produces a spatial concentration profile with:

- x-axis: retinal depth from the choroid
- y-axis: oxygen concentration
- highlighted region: oxygen-sensitive inner retinal layer

This visualization is useful for qualitative inspection of:

- oxygen gradients
- consumption-driven depletion
- relative hypoxia risk across the retinal depth

## Assumptions and limitations

This is a simplified mechanistic model and is intended as a conceptual and numerical framework, not a clinical or fully anatomical simulation. Current assumptions include:

- 1D geometry only
- homogeneous tissue properties
- simplified retinal architecture
- fixed boundary oxygen concentration
- no vascular remodeling or dynamic blood flow effects

These simplifications make the model interpretable and computationally efficient, while leaving room for future extensions.

## Potential extensions

Possible future improvements include:

- 2D/3D retinal geometry
- time-varying oxygen supply
- vascular regulation feedback
- multi-layer retinal compartments
- parameter sensitivity analysis
- comparison against experimental oxygen data

## Summary

This project implements a compact, mechanistic model of retinal oxygen dynamics governed by a nonlinear reaction-diffusion equation. It combines biological intuition, mathematical modeling, and numerical simulation to explore the spatial evolution of oxygen concentration within retinal tissue.

The current repo is a strong starting point for:

- simulation-based retinal physiology studies
- educational demonstrations of PDE modeling
- computational biology prototyping
- future extension into more clinically realistic tissue models

## License

This project does not currently specify a license. If you plan to share or publish this code more broadly, consider adding an open-source license such as MIT or Apache 2.0.
