import numpy as np
from matplotlib import pyplot as plot

if __name__ == '__main__':
    x = np.linspace(0, 10, 5)
    y = np.sin(x)

    plot.plot(x, y)
    plot.show()

    x = np.random.random(1000000)

    plot.hist(x, bins=100)
    plot.show()
