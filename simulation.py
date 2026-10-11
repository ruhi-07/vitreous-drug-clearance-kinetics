import numpy as np
import matplotlib.pyplot as plt

# 1. Physical and Biological Parameters (Retinal Layer Dynamics)
L = 0.025            # Total thickness of retina slice (cm) - approx 250 microns
Nx = 50              # Number of spatial steps (grid resolution)
dx = L / (Nx - 1)    # Spatial step size
x = np.linspace(0, L, Nx)

D = 2.0e-5           # Diffusion coefficient of oxygen in tissue (cm^2/s)
Vmax = 1.2e-4        # Max metabolic oxygen consumption rate (mL O2 / mL tissue / s)
Km = 1.0e-6          # Michaelis constant (concentration at half-max consumption)

# 2. Time Stepping Setup (Explicit Finite Difference Method)
dt = 0.1             # Time step (seconds) - must satisfy stability criteria: dt < (dx^2)/(2D)
Nt = 2000            # Total number of time iterations

# 3. Boundary & Initial Conditions
# Oxygen concentration (C) initialized to baseline everywhere
C = np.ones(Nx) * 5.0e-5  
C_choroid = 6.5e-5   # Fixed oxygen concentration at choroid border (x = 0)

# 4. Numerical Solver for the Reaction-Diffusion PDE
# ∂C/∂t = D*(∂²C/∂x²) - (Vmax*C)/(Km + C)
for t in range(Nt):
    C_new = C.copy()
    
    # Apply Finite Difference approximation for the inner tissue layers
    for i in range(1, Nx - 1):
        diffusion = D * (C[i+1] - 2*C[i] + C[i-1]) / (dx**2)
        consumption = (Vmax * C[i]) / (Km + C[i])
        C_new[i] = C[i] + dt * (diffusion - consumption)
        
    # Enforce Ocular Anatomy Boundaries
    C_new[0] = C_choroid              # Choroid supply boundary condition
    C_new[-1] = C_new[-2]             # Inner retinal boundary (zero-flux mirror condition)
    
    C = C_new

# 5. Plot the Spatial Calculus Output
plt.figure(figsize=(9, 5))
plt.plot(x * 10000, C * 1e5, color='crimson', linewidth=2.5, label='Steady-State Oxygen Profile')
plt.title('Mathematical Ophthalmology: 1D Retinal Oxygenation PDE Model', fontsize=12, fontweight='bold')
plt.xlabel('Retinal Depth from Choroid Base (Microns / μm)')
plt.ylabel('Oxygen Concentration (Arbitrary Partial Pressure Units)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.axvspan(180, 250, color='gray', alpha=0.15, label='Inner Retinal Layer (Hypoxia Vulnerability)')
plt.legend(loc='upper right')

plt.show()
