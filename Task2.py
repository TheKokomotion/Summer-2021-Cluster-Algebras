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


# Evidently CAC_ is totally non-negative iff all n^2 initial minors are non-negative (minors of consecutive rows/columns
# that border the top left or right of matrix), so we'll just check these.


def tnn_test(matrix):
    c = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            m = min(i, j)
            rows = list()
            columns = list()
            for n in range(m + 1):
                rows.insert(0, (i - n))
                columns.insert(0, (j - n))
            a = matrix[np.ix_(rows, columns)]
            if np.linalg.det(a) >= 0:
                c = c + 1
    if c == (len(matrix) + 1) ** 2:
        return 1
    else:
        return 0
# Note: returns 1 if tnn, else returns 0


k = 3
A = matrix_a(k)
C = matrix_c(k)
C_ = np.linalg.inv(C)
CAC_ = np.matmul(C, A, C_)
print(CAC_)
print(tnn_test(CAC_))
