import numpy as np
from matplotlib import pyplot as plot


def multiplot():
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

    height = np.random.randint(160, 200, 100)
    height = np.append(height, np.random.randint(170, 175, 200))
    np.random.shuffle(height)
    x = np.arange(0, len(height))

    ax[1].plot(x, height, label=fr"$wzrost$")
    ax[2].hist(height, bins=20)

    plot.show()


def simple():
    x = np.linspace(0, 5, 100)
    y = x * x
    print(x)
    print(y)
    plot.plot(x, y)
    plot.show()


if __name__ == '__main__':
    # multiplot()
    simple()
