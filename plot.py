import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
    X = np.linspace(0, 1, 10)
    Y = X*X
    print(X)
    print(Y)
    plt.plot(X, Y)
    plt.show()
