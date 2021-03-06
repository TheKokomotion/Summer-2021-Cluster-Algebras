import numpy as np
from math import comb
import scipy.linalg as la
import random
from math import log10


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
    b = sample_floats(5, 15, size)
    for i in range(size):
        a[i][i] = b[i]
    return a


# Matrix C for conjugation
def matrix_c(size):
    check = True
    while check:
        c = np.random.uniform(-100, 101, (size, size))
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


# TP generator
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
            print(f'Checked {n} matrices')
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
            n = n + 1
            print(f'Checked {n} matrices')
            return cac_
        else:
            # This way tells how many candidates were checked
            n = n + 1
            # This way gives some info on how "close" each candidate was to being TNN
            # print(tnn_test(cac_))


# TP test
def close_to_0_test(matrix, i=0, j=0):
    c = 0
    for i_1 in range(len(matrix)):
        for j_1 in range(len(matrix)):
            m = min(i_1, j_1)
            rows = list()
            columns = list()
            for n in range(m + 1):
                rows.insert(0, (i_1 - n))
                columns.insert(0, (j_1 - n))
            a = matrix[np.ix_(rows, columns)]
            if (i_1 == i) and (j_1 == j):
                if np.linalg.det(a) > 0:
                    if np.linalg.det(a) <= .0001:
                        c = c + 1
            else:
                if np.linalg.det(a) > 0:
                    c = c + 1
    if c == len(matrix) ** 2:
        return -1


# Note: returns -1 if desired minor is close to 0


# TP generator
def close_to_0(eigenvalue_matrix, size=1, i=1, j=2):
    n = 0
    a = eigenvalue_matrix
    check = True
    while check:
        c = matrix_c(size)
        c_ = np.linalg.inv(c)
        cac_ = np.matmul(np.matmul(c, a), c_)
        if close_to_0_test(cac_, i, j) == -1:
            n = n + 1
            print(f'Checked {n} matrices')
            return cac_
        else:
            # This way tells how many candidates were checked
            n = n + 1
            # This way gives some info on how "close" each candidate was to being TNN
            # print(tp_test(cac_))


# LDU
def ldu(matrix):
    lu = la.lu(matrix)
    x = lu[1]
    u = lu[2]
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


# d(A) generator in which diagonal matrix doesn't need to have increasing entries - faster
def d_a_fast(tp_or_tnn, lambda_matrix=np.array(0), size=1, number=1):
    x = list()
    y = list()
    z = list()
    if np.all(lambda_matrix == 0):
        lambda_matrix = matrix_a(size)
    print(lambda_matrix)
    for i in range(number):
        print(f'Entry {i + 1}')
        check = True
        while check:
            if tp_or_tnn == 'no_restriction':
                c = matrix_c(size)
                c_ = np.linalg.inv(c)
                a = c.dot(lambda_matrix).dot(c_)
            else:
                a = tp_or_tnn(lambda_matrix, size)
            b = ldu(a)
            if all(g >= 0 for g in np.diag(b[1])):
                d = [log10(x) for x in np.diag(b[1])]
                d.sort()
                x.append(d[0])
                y.append(d[1])
                z.append(d[2])
                check = False
    return [x, y, z, lambda_matrix]


# Store D(A)
Matrix_Lambda = np.array([[1.2, 0, 0], [0, .5, 0], [0, 0, 1.1]])
k = 3
Number_Of_Vectors = 3
index = 'test_1_det'
bottom = -100
top = 100
dlist = d_a_fast(close_to_0, Matrix_Lambda, k, Number_Of_Vectors)
with open("D_A_Storage.py", "a") as out:
    out.write('\n')
    out.write('# Matrix Lambda:' + '\n')
    out.write(f'# A = np.array({dlist[3]})' + '\n')
    out.write(f'# Number of Vectors: {Number_Of_Vectors}' + '\n')
    out.write(f'# C values in [{bottom}, {top}]' + '\n')
    out.write('# x-values:' + '\n')
    out.write(f'x_{index} = {dlist[0]}' + '\n')
    out.write('# y-values:' + '\n')
    out.write(f'y_{index} = {dlist[1]}' + '\n')
    out.write('# z-values:' + '\n')
    out.write(f'z_{index} = {dlist[2]}' + '\n')
