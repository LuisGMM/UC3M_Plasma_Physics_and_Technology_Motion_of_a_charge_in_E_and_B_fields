from lab.solver import solve
from lab.constants import inc_t, t_final, r0, v0, Ex_B0, gamma_qB
import matplotlib.pyplot as plt
import numpy as np


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
        label="w = 0.2",
        linestyle="-",
        color="r",
        linewidth=2.5,
    )
    ax.plot(
        ri[:, 0],
        ri[:, 1],
        np.zeros_like(ri[:, 2]),
        linestyle="-",
        color="r",
        linewidth=1.5,
    )

    ax.plot(
        re[:, 0],
        re[:, 1],
        re[:, 2],
        label="w = 2",
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


# Repeat the first simulation only for a positive charge using E1/B0 = 0.2. Do it
# first with ω = 0.2 and then with ω = 2. The 3D trajectories, or at least their 2D
# projections on the XY plane, should look like Fig. 5.

r1, v1, t1 = solve(inc_t, t_final, r0, v0, 0.2, Ex_B0, 0.2, gamma_qB, 1)
r2, v2, t2 = solve(inc_t, t_final, r0, v0, 0.2, Ex_B0, 2, gamma_qB, 1)
plot1(r1, r2)


# Can you discuss the results?
# What happens with the trajectories? And the energy of the charge?
# Can you predict, for an arbitrary frequency ω, the type of behaviour that will be observed?
