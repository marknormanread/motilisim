import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

distances = np.linspace(1, 25, 100)  # in microns
time = np.linspace(1, 10, 100)  # minutes
extent = [min(distances), max(distances), min(time), max(time)]

def heat_eqn_solve(dist, dt, diffusion, quantity_secreted):
    """
    dist = distances in um
    dt = time since secretion event, in seconds
    diffusion = in um^2/s
    quantity_secreted = number of molecules
    """
    coeff = 1 / ( (4 * np.pi * diffusion * dt) ** 1.5 )  # 3d
    diff = np.exp(-(dist*dist) / (4 * diffusion * dt))
    return quantity_secreted * coeff * diff


X, Y = np.meshgrid(distances, time)
Z = heat_eqn_solve(X, Y * 60, 1e-3, 1e6)
print(Z)

norm = cm.colors.Normalize(vmax=abs(Z).max(), vmin=-abs(Z).max())
cmap = cm.PRGn

fig = plt.figure(figsize=(5, 5))
ax = fig.gca()
im = ax.imshow(Z, extent=extent, origin='lower', aspect='auto')
ax.contour(Z, extent=extent, origin='lower')
fig.colorbar(im)
ax.set_xlabel('Distance from secretion source(um)')
ax.set_ylabel('Time (min)')
fig.tight_layout()
plt.show()
