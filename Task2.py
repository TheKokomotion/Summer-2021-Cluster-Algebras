import numpy as np


# Random diagonal matrix with distinct eigenvalues
def matrix_a(size):
    a = np.zeros((size, size), dtype=int)
    b = np.random.permutation(100)[:size]
    for i in range(size):
        a[i][i] = b[i]
    return a


# Matrix C for conjugation
def matrix_c(size):
    c = 2 * np.random.rand(size, size) - 1
    if np.linalg.det(c) != 0:
        return c


k = 3
A = matrix_a(k)
C = matrix_c(k)
print(A)
print(C)

