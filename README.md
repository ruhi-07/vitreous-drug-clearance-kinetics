# Retinal Oxygenation Model

A reduced-order mathematical model for oxygen transport and metabolic consumption in retinal tissue. The system is formulated as a 1D reaction-diffusion equation and solved numerically using a finite-difference scheme.

The model is designed to represent the interaction between:

- oxygen diffusion through retinal tissue,
- oxygen delivery from the choroidal boundary,
- cellular metabolic consumption,
- spatial gradients in oxygen tension across the retinal depth.

## Why this project exists

Retinal tissue is metabolically active and highly sensitive to local oxygen supply and consumption imbalance. This model provides a mechanistic description of oxygen dynamics in a simplified retinal domain.

Rather than relying on empirical fitting alone, the framework is based on a physically motivated system in which:

- oxygen diffuses through the tissue,
- oxygen is consumed by metabolic activity,
- anatomical boundary conditions represent the supply and geometric constraints of the retina.

This makes the model a useful baseline for investigating oxygenation patterns, hypoxic risk, and the effect of parameter variation on spatial oxygen profiles.

## Governing equation

The oxygen concentration field $C(x,t)$ is modeled using a nonlinear reaction-diffusion equation:

$$
\frac{\partial C}{\partial t}
= D \frac{\partial^2 C}{\partial x^2}
- \frac{V_{\max} C}{K_m + C}
$$

where:

- $C(x,t)$ is the local oxygen concentration,
- $D$ is the diffusion coefficient,
- $V_{\max}$ is the maximum oxygen consumption rate,
- $K_m$ is the Michaelis constant for oxygen-dependent consumption.

### Interpretation of the terms

- $\frac{\partial C}{\partial t}$: local temporal change in oxygen concentration,
- $D \frac{\partial^2 C}{\partial x^2}$: diffusion-driven redistribution of oxygen,
- $\frac{V_{\max} C}{K_m + C}$: nonlinear oxygen consumption due to retinal metabolic activity.

## Boundary conditions

The model imposes the following boundary conditions on the retinal domain:

1. Choroidal boundary at $x=0$

   Oxygen is supplied from the choroid:

   $$
   C(0,t) = C_{\text{choroid}}
   $$

2. Inner retinal boundary at $x=L$

   A zero-flux condition is imposed to represent a no-net-flow internal boundary:

   $$
   \left.\frac{\partial C}{\partial x}\right|_{x=L} = 0
   $$

These conditions describe a biologically motivated setup in which oxygen enters from the outer supply boundary and is consumed within the tissue.

## Numerical method

The simulation uses an explicit finite-difference method on a 1D spatial grid.

The time step is constrained by the diffusion stability criterion:

$$
\Delta t \le \frac{(\Delta x)^2}{2D}
$$

This ensures that the explicit scheme remains numerically stable for the diffusion term.

At each time step, the implementation:

- computes diffusion at internal grid points,
- evaluates the nonlinear metabolic consumption term,
- advances the concentration field in time,
- enforces the boundary values at each iteration.

## Repository contents

This repository currently contains the core simulation logic in:

- `simulation.py` — numerical solver, parameter setup, and visualization

## Getting started

### Requirements

This project requires:

- Python 3.x
- NumPy
- Matplotlib

Install the dependencies with:

```bash
pip install numpy matplotlib
```

## Run the simulation

From the repository root:

```bash
python simulation.py
```

This generates a spatial oxygen profile across retinal depth after the model approaches a steady state.

## Model parameters

The current implementation uses a representative retinal slice with parameters such as:

- domain length: $L = 0.025\,\text{cm}$
- diffusion coefficient: $D = 2.0 \times 10^{-5}\,\text{cm}^2/\text{s}$
- maximum consumption rate: $V_{\max} = 1.2 \times 10^{-4}$
- Michaelis constant: $K_m = 1.0 \times 10^{-6}$
- oxygen supply at the choroid: $C_{\text{choroid}} = 6.5 \times 10^{-5}$

These values are intended as a biologically motivated baseline for exploring oxygen transport dynamics.

## Example output

The script produces a spatial concentration profile with:

- x-axis: retinal depth from the choroid,
- y-axis: oxygen concentration,
- highlighted region: oxygen-sensitive inner retinal layer.

This visualization is useful for qualitative inspection of:

- oxygen gradients,
- consumption-driven depletion,
- relative hypoxia risk across retinal depth.

## Assumptions and limitations

This is a simplified mechanistic model intended as a conceptual and numerical framework rather than a clinical or anatomically complete simulation. Current assumptions include:

- 1D geometry only,
- homogeneous tissue properties,
- simplified retinal architecture,
- fixed boundary oxygen concentration,
- no vascular remodeling or dynamic blood flow effects.

These simplifications make the model interpretable and computationally efficient while leaving room for future extensions.

## Potential extensions

Possible future improvements include:

- 2D or 3D retinal geometry,
- time-varying oxygen supply,
- vascular regulation feedback,
- multi-layer retinal compartments,
- parameter sensitivity analysis,
- comparison against experimental oxygen data.

## Summary

This project implements a compact mechanistic model of retinal oxygen dynamics governed by a nonlinear reaction-diffusion equation. It combines biological intuition, mathematical modeling, and numerical simulation in a form suitable for studying retinal physiology and oxygen transport behavior.

The repository is a strong starting point for:

- simulation-based retinal physiology studies,
- educational demonstrations of PDE modeling,
- computational biology prototyping,
- future extension toward more clinically realistic tissue models.

## License

This project does not currently specify a license. If you plan to share or publish this code more broadly, consider adding an open-source license such as MIT or Apache 2.0.
