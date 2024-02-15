import matplotlib.pyplot as plt
from lab.solver import solve, enery


ri, vi, ti = solve(inc_t, t_final, r0, v0, B1_B0, Ex_B0, w, gamma_qB, 1)
re, ve, te = solve(inc_t, t_final, r0, v0, B1_B0, Ex_B0, w, gamma_qB, -1)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.plot(ri[:, 0], ri[:, 1], ri[:, 2])
ax.plot(re[:, 0], re[:, 1], re[:, 2])
plt.show()


# plot the energy over time

fig, ax = plt.subplots()
ax.plot(ti, enery(vi), label="positive")
ax.plot(te, enery(ve), label="negative")
ax.legend()
plt.show()
