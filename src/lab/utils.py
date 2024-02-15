import numpy as np
import matplotlib.pyplot as plt

from matplotlib.figure import Figure


def plot3d(vec: np.ndarray, fig: Figure | None):
    fig_ = plt.figure() if fig is None else fig
    ax = fig_.add_subplot(111, projection="3d")
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.plot(vec[:, 0], vec[:, 1], vec[:, 2])


def plot2d(vec1: np.ndarray, vec2: np.ndarray, fig: Figure | None):
    fig_ = plt.figure() if fig is None else fig
    ax = fig_.add_subplot(111)
    ax.plot(vec1, vec2)
