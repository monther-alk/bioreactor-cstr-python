import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

mu_max = 0.4
Ks     = 0.1
Y      = 0.5
S0     = 10.0
X0     = 0.5
S_init = 5.0
t_span = (0, 100)
t_eval = np.linspace(0, 100, 1000)

dilution_rates = [0.1, 0.2, 0.3, 0.35]

plt.figure(figsize=(9, 5))

for D in dilution_rates:
    def bioreactor(t, y):
        X, S = y
        mu = mu_max * S / (Ks + S)
        dX_dt = (mu - D) * X
        dS_dt = D * (S0 - S) - (mu * X / Y)
        return [dX_dt, dS_dt]

    sol = solve_ivp(bioreactor, t_span, [X0, S_init], t_eval=t_eval)
    plt.plot(sol.t, sol.y[0], label=f'D = {D} h⁻¹', linewidth=2)

plt.xlabel('Time (h)')
plt.ylabel('Biomass X (g/L)')
plt.title('Effect of Dilution Rate on Biomass Concentration')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('parameter_sweep.png', dpi=150)
plt.show()
