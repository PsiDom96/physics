import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from vibr.geometry.primitives import create_thin_plate
from vibr.geometry.meshing import generate_mesh


# Plate and simulation parameters
radius = 0.1  # meters
dx = 0.002    # grid resolution
dt = 1e-5     # time step
c = 100.0     # wave speed in m/s
T = 0.01      # total simulation time

# Create geometry and mesh
X, Y, mask = create_thin_plate(radius, dx)
coords, indices = generate_mesh(X, Y, mask)

Nx, Ny = X.shape
Nt = int(T / dt)

# Initialize wavefield arrays
u = np.zeros((Nx, Ny))      # current displacement
u_prev = np.zeros_like(u)   # previous timestep
u_next = np.zeros_like(u)   # next timestep

# Initial condition: pulse at center
center_i, center_j = Nx // 2, Ny // 2
u[center_i, center_j] = 1.0

# Store results for animation
frames = []
frames.append(u.copy())

# Finite difference wave simulation
for n in range(1, Nt):
    for i, j in indices:
        if 1 <= i < Nx - 1 and 1 <= j < Ny - 1:
            u_next[i, j] = (2 * u[i, j] - u_prev[i, j] + 
                             (c * dt / dx) ** 2 * 
                             (u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1] - 4 * u[i, j]))
    u_prev[:, :] = u[:, :]
    u[:, :] = u_next[:, :]
    if n % 20 == 0:
        frames.append(u.copy())

# Animation
fig, ax = plt.subplots()
cax = ax.imshow(frames[0], cmap='viridis', origin='lower', extent=[-radius, radius, -radius, radius])
fig.colorbar(cax)

def animate(n):
    cax.set_data(frames[n])
    ax.set_title(f"Time = {n * dt * 20:.5f} s")
    return [cax]

ani = FuncAnimation(fig, animate, frames=len(frames), interval=50)
plt.show()
