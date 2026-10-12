# Vitreous Drug Clearance Kinetics

A compact, reproducible Python model for simulating drug transport and clearance in a simplified vitreous-like compartment. The project is designed as a transparent, minimal computational prototype for exploratory analysis, education, and future extension.

## Overview

This repository implements a one-dimensional diffusion-clearance model using an explicit finite-difference scheme. The model evolves a concentration field over time and illustrates how local transport and elimination processes can be represented in a simple numerical framework.

The code is intentionally readable and lightweight, with a small dependency footprint and no hidden infrastructure. It is suitable for:

- teaching numerical methods,
- prototyping transport models,
- parameter sensitivity exploration,
- building a baseline for more detailed ocular pharmacokinetic studies.

## Why this project exists

Many scientific code repositories are difficult to run, reproduce, or extend because the implementation is opaque or overengineered. This project takes the opposite approach: a minimal yet credible simulation that is easy to inspect, modify, and adapt.

The goal is not to claim a clinically validated physiological model. Instead, it provides a clean computational foundation for studying the interplay between:

- spatial diffusion,
- boundary conditions,
- local clearance dynamics,
- temporal evolution of concentration profiles.

## Scientific formulation

The model tracks the concentration field $C(x, t)$ in a 1D domain and updates it with a finite-difference approximation of a diffusion-clearance equation:

$$
\frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2} - k_{\mathrm{clear}} C
$$

where:

- $C(x, t)$ is the concentration at position $x$ and time $t$
- $D$ is the effective diffusion coefficient
- $k_{\mathrm{clear}}$ is the first-order clearance rate

The numerical update is implemented explicitly as:

$$
C_i^{n+1} = C_i^n + \Delta t \left(D\frac{C_{i+1}^n - 2C_i^n + C_{i-1}^n}{\Delta x^2} - k_{\mathrm{clear}} C_i^n\right)
$$

This is a standard, easy-to-interpret finite-difference scheme suitable for a compact baseline model.

## Repository structure

- `simulation.py` — main numerical solver and plotting routine
- `requirements.txt` — dependency list
- `LICENSE` — MIT license
- `.gitignore` — standard Python exclusions

## Installation

This project requires Python 3.9+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the simulation

From the repository root:

```bash
python simulation.py
```

The script runs the model and writes a plot to:

```text
vitreous_clearance_profile.png
```

You can also customize the simulation via command-line options:

```bash
python simulation.py --nx 300 --dt 0.05 --steps 3000 --output profile.png
```

## Model assumptions

This implementation is deliberately simplified. It is intended as a transparent prototype rather than a clinical or anatomically detailed model. Current assumptions include:

- one-dimensional spatial domain,
- homogeneous effective transport properties,
- simple boundary conditions,
- constant diffusion and clearance parameters,
- no coupled physiological feedback or compartmental structure.

These choices make the model interpretable and easy to extend.

## Parameter defaults

The default configuration is designed to behave stably and produce a smooth concentration profile:

| Parameter | Value | Meaning |
| --- | ---: | --- |
| `length` | 0.025 cm | domain length |
| `nx` | 200 | number of grid points |
| `diffusion_coefficient` | 2.0e-5 | effective diffusion coefficient |
| `clearance_rate` | 1.2e-4 | first-order local clearance |
| `source_value` | 6.5e-5 | concentration at the source boundary |
| `dt` | 0.1 | explicit time step |
| `steps` | 2000 | number of time steps |

## Example output

The script produces a spatial concentration profile showing the evolution from a boundary-driven source toward a smoother, lower concentration distribution over time.

This output is useful for:

- checking numerical stability,
- visualizing spatial gradients,
- comparing parameter choices,
- developing more advanced transport models.

## Extending the project

This code is structured to make future improvements straightforward, such as:

- parameter sweeps,
- alternative boundary conditions,
- nonlinear clearance terms,
- multi-compartment formulations,
- validation against experimental data,
- more advanced finite-difference or finite-volume methods.

## Contributing

Contributions are welcome. If you are improving the numerical method, adding validation, or extending the model, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
