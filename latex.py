import numpy as np
import array_to_latex as a2l

if __name__ == '__main__':
    A = np.random.random([10, 10])
    latex_code = a2l.to_ltx(A, frmt='{:6.2f}', arraytype='bmatrix', print_out=False)

    print(latex_code)
