from lab.solver import solve, energy
from lab.constants import inc_t, t_final, r0, v0, B1_B0, Ex_B0, w, gamma_qB
import matplotlib.pyplot as plt


def plot1(ri, re):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
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
        re[:, 0],
        re[:, 1],
        re[:, 2],
        label="q = -1",
        linestyle="-",
        color="b",
        linewidth=2.5,
    )
    plt.legend()
    plt.show()


# 1. Plot the 3D trajectory or, at least, its 2D projection on the XY plane for a positive
# and negative charge for a run using the parameters in Table 1. The result
# should look like Fig. 2.

ri, vi, ti = solve(inc_t, t_final, r0, v0, B1_B0, Ex_B0, w, gamma_qB, 1)
re, ve, te = solve(inc_t, t_final, r0, v0, B1_B0, Ex_B0, w, gamma_qB, -1)
plot1(ri, re)


# Why do the charges rotate with different orientations?
# Why is the radius of the projected trajectories for the two charges rL = 1?
# What is the radius (or distances in general, for that matter) normalized to?
# Which parameters can be changed in the code to obtain a different radius?
# How would you modify the code to be able see differences for different charge and mass values?


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
