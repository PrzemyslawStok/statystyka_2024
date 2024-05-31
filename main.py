import numpy as np
from matplotlib import pyplot as plot

if __name__ == '__main__':
    fig, ax = plot.subplots(2, 2, figsize=(10, 10), dpi=200)

    ax = ax.ravel()

    linspace_dim = [5, 10, 20, 100, 200, 500]

    for i, dim in enumerate(linspace_dim):
        x = np.linspace(-np.pi, np.pi, dim)
        y = np.sin(x)

        ax[0].plot(x, y, label=fr"$y=sin(x), dim={dim}$")

    ax[0].set_xlabel('x')
    ax[0].set_ylabel('y')
    ax[0].legend()

    plot.show()
