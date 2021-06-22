import numpy as np
from math import comb
import scipy.linalg as la
import random
from math import log10
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D


# Random, distinct real numbers generator (thanks to Raymond Hettinger on stackoverflow)
def sample_floats(low, high, j=1):
    """ Return a k-length list of unique random floats
        in the range of low <= x <= high
    """
    result = []
    seen = set()
    for i in range(j):
        x = random.uniform(low, high)
        while x in seen:
            x = random.uniform(low, high)
        seen.add(x)
        result.append(x)
    return result


# Random diagonal matrix with distinct eigenvalues
def matrix_a(size):
    a = np.zeros((size, size))
    # It seems that keeping the upper limit small helps the computer run through computations faster
    b = sample_floats(1, 5, size)
    for i in range(size):
        a[i][i] = b[i]
    return a


# Matrix C for conjugation
def matrix_c(size):
    check = True
    while check:
        c = np.random.uniform(-1, 2, (size, size))
        if np.linalg.det(c) != 0:
            return c


# A matrix is totally positive iff all n^2 initial minors are positive; I'm still digging to find efficient criteria
# for totally non-negative, but the linked paper seems promising: https://arxiv.org/abs/1207.3613. Until I can figure
# out a more efficient way, I'll stick to checking all minors

# TP test
def tp_test(matrix):
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
            if np.linalg.det(a) > 0:
                c = c + 1
    if c == (len(matrix)) ** 2:
        return -1
    else:
        return c
# Note: returns -1 if TP


# TP generator - unfortunately the way we're generating matrices, I don't think this will ever find a TP matrix
def tp(eigenvalue_matrix, size=1):
    n = 0
    a = eigenvalue_matrix
    check = True
    while check:
        c = matrix_c(size)
        c_ = np.linalg.inv(c)
        cac_ = np.matmul(np.matmul(c, a), c_)
        if tp_test(cac_) == -1:
            n = n + 1
            print(n)
            return cac_
        else:
            # This way tells how many candidates were checked
            n = n + 1
            # This way gives some info on how "close" each candidate was to being TNN
            # print(tp_test(cac_))


# TNN test
def tnn_test(matrix):
    c = 0
    # 1 x 1 minors
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            a = matrix[np.ix_([i], [j])]
            if np.linalg.det(a) >= 0:
                c = c + 1
    # 2 x 2 minors
    for i_1 in range(len(matrix) - 1):
        for i_2 in range(i_1 + 1, len(matrix)):
            for j_1 in range(len(matrix) - 1):
                for j_2 in range(j_1 + 1, len(matrix)):
                    a = matrix[np.ix_([i_1, i_2], [j_1, j_2])]
                    if np.linalg.det(a) >= 0:
                        c = c + 1
    # 3 x 3 minors
    for i_1 in range(len(matrix) - 2):
        for i_2 in range(i_1 + 1, len(matrix) - 1):
            for i_3 in range(i_2 + 1, len(matrix)):
                for j_1 in range(len(matrix) - 2):
                    for j_2 in range(j_1 + 1, len(matrix) - 1):
                        for j_3 in range(j_2 + 1, len(matrix)):
                            a = matrix[np.ix_([i_1, i_2], [j_1, j_2])]
                            if np.linalg.det(a) >= 0:
                                c = c + 1
    # Output
    if c == comb(2 * len(matrix), len(matrix)) - 1:
        return -1
    else:
        return c
# Note: returns -1 if TNN. Only will work for 3 x 3 matrices as of now.


# TNN generator
def tnn(eigenvalue_matrix, size=1):
    n = 0
    a = eigenvalue_matrix
    check = True
    while check:
        c = matrix_c(size)
        c_ = np.linalg.inv(c)
        cac_ = c.dot(a).dot(c_)
        if tnn_test(cac_) == -1:
            # Optional information on matrices
            n = n + 1
            print(n)
            # print(a)
            # print(c)
            # print(c_)
            return cac_
        else:
            # This way tells how many candidates were checked
            n = n + 1
            # This way gives some info on how "close" each candidate was to being TNN
            # print(tnn_test(cac_))


# LDU
def ldu(matrix):
    x = la.lu(matrix)[1]
    u = la.lu(matrix)[2]
    d = np.diag(np.diag(u))
    u /= np.diag(u)[:, None]
    return x, d, u


# d(A) generator that makes sure diagonal matrix has increasing entries - kinda slow
def d_a(tp_or_tnn, size=1, number=1):
    d_a_list = list()
    lambda_matrix = matrix_a(size)
    print(lambda_matrix)
    for i in range(number):
        check1 = True
        while check1:
            # Generating TNN matrix to test
            a = tp_or_tnn(lambda_matrix, size)
            b = ldu(a)
            for j in range(size - 1):
                print(j)
                if b[1][j][j] >= b[1][j + 1][j + 1]:
                    # Test failed, exiting loop
                    break
                if j == size - 2:
                    print(b[1])
                    d = [log10(x) for x in np.diag(b[1])]
                    d_a_list.append(d)
                    # Success! Adding to list.
                    check1 = False
    return d_a_list


# 3D Scatter Plot
fig_1 = pyplot.figure()
ax_1 = Axes3D(fig_1)

# Axis Labels
ax_1.set_xlabel('X-axis')
ax_1.set_ylabel('Y-axis')
ax_1.set_zlabel('Z-axis')


# d(A) generator in which diagonal matrix doesn't need to have increasing entries - faster
def d_a_fast(tp_or_tnn, size=1, number=1):
    x = list()
    y = list()
    z = list()
    lambda_matrix = matrix_a(size)
    print(lambda_matrix)
    for i in range(number):
        a = tp_or_tnn(lambda_matrix, size)
        b = ldu(a)
        if all(g >= 0 for g in np.diag(b[1])):
            print(np.diag(b[1]))
            d = [log10(x) for x in np.diag(b[1])]
            d.sort()
            x.append(d[0])
            y.append(d[1])
            z.append(d[2])
    return [x, y, z]


# Make Plot (set k to desired distance)
k = 3
p = d_a_fast(tp, k, 25)
ax_1.scatter(p[0], p[1], p[2])
pyplot.show()
