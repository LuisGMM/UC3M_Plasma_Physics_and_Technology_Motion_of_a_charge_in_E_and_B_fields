from typing import Literal
import numpy as np


def solve(
    inc_t: float,
    t_final: float,
    r0: np.ndarray,
    v0: np.ndarray,
    B1_B0: float,
    Ex_B0: float,
    w: float,
    gamma_qB: float,
    sgn: Literal[-1, 1],
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    r_current = r0
    v_current = v0

    r = np.ones((int(t_final / inc_t), 3))
    v = np.ones((int(t_final / inc_t), 3))
    t = np.arange(0, t_final, inc_t)

    for i, t_i in enumerate(t):
        r[i] = r_current
        v[i] = v_current
        ex_b0 = Ex_B0 * np.cos(2 * np.pi * w * t_i)

        v_mid = v_current + 0.5 * inc_t * np.array(
            (
                sgn * (1 + B1_B0 * r_current[0]) * v_current[1]
                + sgn * ex_b0
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
                + sgn * ex_b0
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

    return r, v, t


def energy(v, mass_e=1):
    return 0.5 * np.linalg.norm(v, axis=1) ** 2 * mass_e
