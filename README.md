# Advanced Mechanistic Ophthalmology: Retinal Tissue Oxygenation Model

A computational framework utilizing a **Partial Differential Equation (PDE)** to simulate spatial-temporal oxygen transport and metabolic consumption profiles within the physical layers of the human retina. 

This model transitions away from standard data-driven statistical models to implement physics-governed biomathematical systems—directly mapping tissue mechanics to clinical ischemic environments.

## The Advanced Calculus Framework

The spatial distribution and concentration decay of retinal oxygen ($C$) over space ($x$) and time ($t$) is modeled via a non-linear **Reaction-Diffusion Partial Differential Equation**:

$$ \frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2} - \frac{V_{max} C}{K_m + C} $$

### Breakdown of the Mathematical Logic:
* **$\frac{\partial C}{\partial t}$ (Temporal Derivative):** Calculates the localized rate of change of oxygen tension across time.
* **$D \frac{\partial^2 C}{\partial x^2}$ (The Spatial Diffusion Curvature):** Governed by Fick's Second Law, using a 1D Laplacian to map how oxygen naturally diffuses away from high-concentration capillary beds (the choroid matrix) down across the geometric layers of tissue.
* **$\frac{V_{max} C}{K_m + C}$ (Nonlinear Michaelis-Menten Kinetics):** Models the metabolic consumption mechanics of highly active outer-segment retinal photoreceptors.

## Anatomical Boundary Conditions Applied
To solve the PDE domain, explicit physical boundary constraints are defined to model retinal architecture:
1. **Choroidal Boundary ($x = 0$):** Fixed continuous blood supply concentration:  
   $$ C(0, t) = C_{choroid} $$
2. **Inner Retinal Boundary ($x = L$):** Zero-flux condition representing internal vascular equilibrium boundaries:  
   $$ \frac{\partial C}{\partial x} \Big|_{x=L} = 0 $$

## Implementation Architecture
The code applies an explicit finite-difference discretization model over space and time. It evaluates numerical stability limits according to the Courant-Friedrichs-Lewy condition:  
$$\Delta t \le \frac{\Delta x^2}{2D}$$
