import numpy as np

# Random diagonal matrix with distinct eigenvalues
def matrix(size):
    a = np.zeros((size, size), dtype=int)
    b = np.random.permutation(100)[:size]
    print(b)
    for i in range(size):
        a[i][i] = b[i]
    return a


print(matrix(3))
