import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Physical parameters
L = 1.0             # Length of the plate (meters)
T = 1.0             # Tension or stiffness coefficient (arbitrary units)
rho = 1.0           # Linear density (arbitrary units)
c = np.sqrt(T / rho)  # Wave speed

# Simulation parameters
Nx = 100
dx = L / Nx
x = np.linspace(0, L, Nx)
dt = 0.001
Nt = 1000

# Stability condition
assert c * dt / dx < 1.0, "Stability condition violated!"

# Initial conditions
u = np.zeros((Nt, Nx))
u[0, :] = np.exp(-1000 * (x - 0.5)**2)  # Gaussian pluck
u[1, 1:-1] = u[0, 1:-1] + 0.5 * (c * dt / dx)**2 * (u[0, 2:] - 2*u[0, 1:-1] + u[0, :-2])

# Time stepping loop
for n in range(1, Nt - 1):
    u[n + 1, 1:-1] = (2 * u[n, 1:-1] - u[n - 1, 1:-1] +
                     (c * dt / dx)**2 * (u[n, 2:] - 2*u[n, 1:-1] + u[n, :-2]))

# Animation
fig, ax = plt.subplots()
line, = ax.plot(x, u[0])
ax.set_ylim(-1.1, 1.1)
ax.set_title("1D Plate Vibration")

def animate(n):
    line.set_ydata(u[n])
    return line,

ani = FuncAnimation(fig, animate, frames=range(0, Nt, 10), interval=30)
ani.save('../figures/plate_vibration.gif', writer='pillow', fps=20)
plt.show()
