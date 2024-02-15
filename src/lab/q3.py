from lab.solver import solve, energy
from lab.constants import inc_t, t_final, r0, v0, B1_B0, Ex_B0, w, gamma_qB
import matplotlib.pyplot as plt
import numpy as np


def plot1(ri, re):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_xlim(-2, 2)
    ax.set_ylim(-8, 2)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.plot(
        ri[:, 0],
        ri[:, 1],
        ri[:, 2],
        label="q = +1",
        linestyle="-",
        color="r",
        linewidth=2.5,
    )
    ax.plot(
        ri[:, 0],
        ri[:, 1],
        np.zeros_like(ri[:, 2]),
        label="q = +1",
        linestyle="-",
        color="r",
        linewidth=1.5,
    )

    ax.plot(
        re[:, 0],
        re[:, 1],
        re[:, 2],
        linestyle="-",
        color="b",
        linewidth=2.5,
    )
    ax.plot(
        re[:, 0],
        re[:, 1],
        np.zeros_like(re[:, 2]),
        linestyle="-",
        color="b",
        linewidth=1.5,
    )
    plt.legend()
    plt.show()


# Repeat the first simulation for positive and negative charges setting B1/B0 = 0.2.
# The 3D trajectories or, at least their 2D projections on the XY plane, should look like Fig. 4.

ri, vi, ti = solve(inc_t, t_final, r0, v0, 0.2, Ex_B0, w, gamma_qB, 1)
re, ve, te = solve(inc_t, t_final, r0, v0, 0.2, Ex_B0, w, gamma_qB, -1)
plot1(ri, re)


# Plot the variation with time of x and y for both particles

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(ti, ri[:, 0], label="x+")
ax.plot(ti, ri[:, 1], label="y+")
ax.plot(te, re[:, 0], label="x-")
ax.plot(te, re[:, 1], label="y-")
ax.set_xlabel("Time [s]")
ax.set_ylabel("Position [m]")
ax.legend()
plt.show()

# Why do electrons and ions drift in the opposite directions?
# Why is this direction along Y ?

# From the plot of y(t), can you estimate the velocity of the drift?
# What is it normalized to (or any velocity, for that matter)?
# Which parameter value should be varied in the code to make this drift change?


# Plot the kinetic energy of the charges as a function of t.

fig, ax = plt.subplots()
ax.plot(ti, energy(vi), label="positive")
ax.plot(te, energy(ve), label="negative")
ax.set_xlabel("Time [s]")
ax.set_ylabel("Kinetic Energy [V]")
ax.legend()
plt.show()

# Does it change with time? Why?


# Do another run with γ/B0 = 0.2. How do things change? And the energy?

ri, vi, ti = solve(inc_t, t_final, r0, v0, B1_B0, Ex_B0, w, 0.2, 1)
re, ve, te = solve(inc_t, t_final, r0, v0, B1_B0, Ex_B0, w, 0.2, -1)
plot1(ri, re)
