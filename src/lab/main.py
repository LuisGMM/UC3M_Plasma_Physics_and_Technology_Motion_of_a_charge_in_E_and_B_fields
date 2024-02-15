import numpy as np
import matplotlib.pyplot as plt


inc_t = 0.1
t_final = 30
r0 = np.array((0, 0, 3))
v0 = np.array((1, 0, 2))
B1_B0 = 0
Ex_B0 = 0
w = 0
gamma_qB = 0

sgn = -1

r_current: np.ndarray
v_current: np.ndarray

r_next: np.ndarray
v_next: np.ndarray

r_mid: np.ndarray
v_mid: np.ndarray


def solve(
    inc_t: float,
    t_final: float,
    r0: np.ndarray,
    v0: np.ndarray,
    B1_B0: float,
    Ex_B0: float,
    w: float,
    gamma_qB: float,
) -> np.ndarray:
    del w

    r_current = r0
    v_current = v0

    r = np.ones((int(t_final / inc_t), 3))
    v = np.ones((int(t_final / inc_t), 3))

    for i, _ in enumerate(np.arange(0, t_final, inc_t)):
        r[i] = r_current
        v[i] = v_current

        v_mid = v_current + 0.5 * inc_t * np.array(
            (
                sgn * (1 + B1_B0 * r_current[0]) * v_current[1]
                + sgn * Ex_B0
                - gamma_qB * v_current[0],
                -sgn * (1 + B1_B0 * r_current[0]) * v_current[0]
                - gamma_qB * v_current[1],
                -gamma_qB * v_current[2],
            )
        )
        r_mid = r_current + 0.5 * inc_t * v_current

        v_next = v_current + inc_t * np.array(
            (
                sgn * (1 + B1_B0 * r_mid[0]) * v_mid[1]
                + sgn * Ex_B0
                - gamma_qB * v_mid[0],
                -sgn * (1 + B1_B0 * r_mid[0]) * v_mid[0] - gamma_qB * v_mid[1],
                -gamma_qB * v_mid[2],
            )
        )
        r_next = r_current + inc_t * v_mid

        if np.isclose(r_current, 0, 0.1).all():
            print(r_current)

        r_current = r_next
        v_current = v_next

    return r


# print(r)

# print(np.isclose(np.array([0.00000000, 0.00000000, 0.00000000]), 0).all())

r = solve(inc_t, t_final, r0, v0, B1_B0, Ex_B0, w, gamma_qB)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot(r[:, 0], r[:, 1], r[:, 2])
plt.show()
