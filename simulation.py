import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# --- Parameters ---
mu_max = 0.4    # max specific growth rate (h⁻¹)
Ks     = 0.1    # half-saturation constant (g/L)
Y      = 0.5    # yield coefficient (g biomass / g substrate)
D      = 0.2    # dilution rate (h⁻¹)
S0     = 10.0   # feed substrate concentration (g/L)

X0     = 0.5    # initial biomass (g/L)
S_init = 5.0    # initial substrate (g/L)

t_span = (0, 50)        # simulation time in hours
t_eval = np.linspace(0, 50, 500)

# --- Model equations ---
def bioreactor(t, y):
    X, S = y
    mu = mu_max * S / (Ks + S)
    dX_dt = (mu - D) * X
    dS_dt = D * (S0 - S) - (mu * X / Y)
    return [dX_dt, dS_dt]

# --- Solve ---
solution = solve_ivp(
    bioreactor,
    t_span,
    [X0, S_init],
    t_eval=t_eval,
    method='RK45'
)

X = solution.y[0]
S = solution.y[1]
t = solution.t

# --- Plot ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

ax1.plot(t, X, color='steelblue', linewidth=2)
ax1.set_ylabel('Biomass X (g/L)')
ax1.set_title('CSTR Bioreactor Simulation — Monod Kinetics')
ax1.grid(True, alpha=0.3)

ax2.plot(t, S, color='coral', linewidth=2)
ax2.set_ylabel('Substrate S (g/L)')
ax2.set_xlabel('Time (h)')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('output_plot.png', dpi=150)
plt.show()
