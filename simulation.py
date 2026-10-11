import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1. Define the Ophthalmic Drug Clearance Math (ODE)
# dC/dt = -k * C  (The rate of drug change depends on concentration and clearance rate)
def drug_clearance(t, C, k):
    return -k * C

# 2. Set Clinical Variables
C0 = [10.0]       # Initial concentration of Ranibizumab injected (mg/L)
t_span = (0, 60)  # Track the drug levels over 60 days
t_eval = np.linspace(0, 60, 300) # Smooth time intervals for plotting
k_clearance = 0.075 # Elimination rate constant based on vitreous half-life (~9 days)

# 3. Solve the Differential Equation Numerically
solution = solve_ivp(drug_clearance, t_span, C0, args=(k_clearance,), t_eval=t_eval)

# 4. Generate the Simulation Plot
plt.figure(figsize=(8, 5))
plt.plot(solution.t, solution.y, label='Ranibizumab Concentration', color='teal', linewidth=2)
plt.title('Mathematical Ophthalmology: Vitreous Anti-VEGF Drug Clearance Kinetics')
plt.xlabel('Time (Days)')
plt.ylabel('Concentration in Vitreous Humor (mg/L)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(y=1.0, color='r', linestyle=':', label='Minimum Therapeutic Threshold')
plt.legend()

# Display the final graph
plt.show()
