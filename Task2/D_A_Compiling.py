# Preamble
from itertools import permutations
from math import log10

from D_A_Storage import x_2
from D_A_Storage import x_3
from D_A_Storage import x_4
from D_A_Storage import x_5
from D_A_Storage import x_6
from D_A_Storage import x_7
from D_A_Storage import x_8
from D_A_Storage import x_9
from D_A_Storage import x_10
from D_A_Storage import x_11
from D_A_Storage import x_12
from D_A_Storage import x_13
from D_A_Storage import x_mystery_1
from D_A_Storage import x_primes_1
from D_A_Storage import x_primes_2
from D_A_Storage import x_primes_3
from D_A_Storage import x_tri2_1
from D_A_Storage import x_tri2_2
from D_A_Storage import x_tri2_3
from D_A_Storage import x_test_1
from D_A_Storage import x_test_2
from D_A_Storage import x_hexagon_1
from D_A_Storage import x_test_1_det

from D_A_Storage import y_2
from D_A_Storage import y_3
from D_A_Storage import y_4
from D_A_Storage import y_5
from D_A_Storage import y_6
from D_A_Storage import y_7
from D_A_Storage import y_8
from D_A_Storage import y_9
from D_A_Storage import y_10
from D_A_Storage import y_11
from D_A_Storage import y_12
from D_A_Storage import y_13
from D_A_Storage import y_mystery_1
from D_A_Storage import y_primes_1
from D_A_Storage import y_primes_2
from D_A_Storage import y_primes_3
from D_A_Storage import y_tri2_1
from D_A_Storage import y_tri2_2
from D_A_Storage import y_tri2_3
from D_A_Storage import y_test_1
from D_A_Storage import y_test_2
from D_A_Storage import y_hexagon_1
from D_A_Storage import y_test_1_det

from D_A_Storage import z_2
from D_A_Storage import z_3
from D_A_Storage import z_4
from D_A_Storage import z_5
from D_A_Storage import z_6
from D_A_Storage import z_7
from D_A_Storage import z_8
from D_A_Storage import z_9
from D_A_Storage import z_10
from D_A_Storage import z_11
from D_A_Storage import z_12
from D_A_Storage import z_13
from D_A_Storage import z_mystery_1
from D_A_Storage import z_primes_1
from D_A_Storage import z_primes_2
from D_A_Storage import z_primes_3
from D_A_Storage import z_tri2_1
from D_A_Storage import z_tri2_2
from D_A_Storage import z_tri2_3
from D_A_Storage import z_test_1
from D_A_Storage import z_test_2
from D_A_Storage import z_hexagon_1
from D_A_Storage import z_test_1_det


# Combine coordinate data into big lists:

# eigenvalues: [4.30788144, 1.2769152, 3.51255544]
x_eigenvalues_triangle = [log10(4.30788144), log10(4.30788144), log10(1.2769152), log10(1.2769152),
                           log10(3.51255544), log10(3.51255544)]
y_eigenvalues_triangle = [log10(1.2769152), log10(3.51255544), log10(4.30788144), log10(3.51255544),
                           log10(4.30788144), log10(1.2769152)]
z_eigenvalues_triangle = [log10(3.51255544), log10(1.2769152), log10(3.51255544), log10(4.30788144),
                           log10(1.2769152), log10(4.30788144)]
# x-data:
x_triangle = x_2 + x_3 + x_4 + x_5 + x_6 + x_7 + x_8 + x_9 + x_10 + x_11
# y-data:
y_triangle = y_2 + y_3 + y_4 + y_5 + y_6 + y_7 + y_8 + y_9 + y_10 + y_11
# z-data:
z_triangle = z_2 + z_3 + z_4 + z_5 + z_6 + z_7 + z_8 + z_9 + z_10 + z_11

# Permute order of the vectors
x_triangle_permuted = list()
y_triangle_permuted = list()
z_triangle_permuted = list()
l_1 = list(permutations((x_triangle, y_triangle, z_triangle)))
for i_1 in range(len(x_triangle)):
    for i_2 in range(len(l_1)):
        x_triangle_permuted.append(l_1[i_2][0][i_1])
        y_triangle_permuted.append(l_1[i_2][1][i_1])
        z_triangle_permuted.append(l_1[i_2][2][i_1])

# eigenvalues:
e_shield = [2.55061337, 4.77928811, 1.50907569]
x_eigenvalues_shield = list()
y_eigenvalues_shield = list()
z_eigenvalues_shield = list()
l_e_shield = list(permutations(e_shield))
for i_1 in range(0, 3):
    for i_2 in range(len(l_e_shield)):
        x_eigenvalues_shield.append(log10(l_e_shield[i_2][0]))
        y_eigenvalues_shield.append(log10(l_e_shield[i_2][1]))
        z_eigenvalues_shield.append(log10(l_e_shield[i_2][2]))

x_shield = x_12 + x_13
y_shield = y_12 + y_13
z_shield = z_12 + z_13

# Permute order of the vectors
x_shield_permuted = list()
y_shield_permuted = list()
z_shield_permuted = list()
l_2 = list(permutations((x_shield, y_shield, z_shield)))
for i_1 in range(len(x_shield)):
    for i_2 in range(len(l_2)):
        x_shield_permuted.append(l_2[i_2][0][i_1])
        y_shield_permuted.append(l_2[i_2][1][i_1])
        z_shield_permuted.append(l_2[i_2][2][i_1])


# eigenvalues: [5.1926814, 13.67366029, 8.92714867]
x_mystery = x_mystery_1
y_mystery = y_mystery_1
z_mystery = z_mystery_1

# Permute order of the vectors
x_mystery_permuted = list()
y_mystery_permuted = list()
z_mystery_permuted = list()
l_3 = list(permutations((x_mystery, y_mystery, z_mystery)))
for i_1 in range(len(x_mystery)):
    for i_2 in range(len(l_3)):
        x_mystery_permuted.append(l_3[i_2][0][i_1])
        y_mystery_permuted.append(l_3[i_2][1][i_1])
        z_mystery_permuted.append(l_3[i_2][2][i_1])

# eigenvalues: [2, 3, 5]
x_primes = x_primes_1 + x_primes_2 + x_primes_3
y_primes = y_primes_1 + y_primes_2 + y_primes_3
z_primes = z_primes_1 + z_primes_2 + z_primes_3

# Permute order of the vectors
x_primes_permuted = list()
y_primes_permuted = list()
z_primes_permuted = list()
l_4 = list(permutations((x_primes, y_primes, z_primes)))
for i_1 in range(len(x_primes)):
    for i_2 in range(len(l_4)):
        x_primes_permuted.append(l_4[i_2][0][i_1])
        y_primes_permuted.append(l_4[i_2][1][i_1])
        z_primes_permuted.append(l_4[i_2][2][i_1])

# eigenvalues:
e_tri2 = [5.30788144, 1.2769152, 3.51255544]
x_eigenvalues_tri2 = list()
y_eigenvalues_tri2 = list()
z_eigenvalues_tri2 = list()
l_e_tri2 = list(permutations(e_tri2))
for i_1 in range(0, 3):
    for i_2 in range(len(l_e_tri2)):
        x_eigenvalues_tri2.append(log10(l_e_tri2[i_2][0]))
        y_eigenvalues_tri2.append(log10(l_e_tri2[i_2][1]))
        z_eigenvalues_tri2.append(log10(l_e_tri2[i_2][2]))

x_tri2 = x_tri2_1 + x_tri2_2 + x_tri2_3
y_tri2 = y_tri2_1 + y_tri2_2 + y_tri2_3
z_tri2 = z_tri2_1 + z_tri2_2 + z_tri2_3

# Permute order of the vectors
x_tri2_permuted = list()
y_tri2_permuted = list()
z_tri2_permuted = list()
l_tri2 = list(permutations((x_tri2, y_tri2, z_tri2)))
for i_1 in range(len(x_tri2)):
    for i_2 in range(len(l_tri2)):
        x_tri2_permuted.append(l_tri2[i_2][0][i_1])
        y_tri2_permuted.append(l_tri2[i_2][1][i_1])
        z_tri2_permuted.append(l_tri2[i_2][2][i_1])

# eigenvalue test:
e_test = [1.2, 0.5, 1.1]
x_eigenvalues_test = list()
y_eigenvalues_test = list()
z_eigenvalues_test = list()
l_e_test = list(permutations(e_test))
for i_1 in range(0, 3):
    for i_2 in range(len(l_e_test)):
        x_eigenvalues_test.append(log10(l_e_test[i_2][0]))
        y_eigenvalues_test.append(log10(l_e_test[i_2][1]))
        z_eigenvalues_test.append(log10(l_e_test[i_2][2]))

x_test = x_test_1 + x_test_2
y_test = y_test_1 + y_test_2
z_test = z_test_1 + z_test_2

# Permute order of the vectors
x_test_permuted = list()
y_test_permuted = list()
z_test_permuted = list()
l_test = list(permutations((x_test, y_test, z_test)))
for i_1 in range(len(x_test)):
    for i_2 in range(len(l_test)):
        x_test_permuted.append(l_test[i_2][0][i_1])
        y_test_permuted.append(l_test[i_2][1][i_1])
        z_test_permuted.append(l_test[i_2][2][i_1])

# One of 9 minors close to 0 Stuff
x_test_0_det_permuted = list()
y_test_0_det_permuted = list()
z_test_0_det_permuted = list()
l_test_0_det = list(permutations((x_test_1_det, y_test_1_det, z_test_1_det)))
for i_1 in range(len(x_test_1_det)):
    for i_2 in range(len(l_test_0_det)):
        x_test_0_det_permuted.append(l_test_0_det[i_2][0][i_1])
        y_test_0_det_permuted.append(l_test_0_det[i_2][1][i_1])
        z_test_0_det_permuted.append(l_test_0_det[i_2][2][i_1])

# Eigenvalues:
e_hexagon = [2.2, 0.5, 1.1]
x_eigenvalues_hexagon = list()
y_eigenvalues_hexagon = list()
z_eigenvalues_hexagon = list()
l_e_hexagon = list(permutations(e_hexagon))
for i_1 in range(0, 3):
    for i_2 in range(len(l_e_hexagon)):
        x_eigenvalues_hexagon.append(log10(l_e_hexagon[i_2][0]))
        y_eigenvalues_hexagon.append(log10(l_e_hexagon[i_2][1]))
        z_eigenvalues_hexagon.append(log10(l_e_hexagon[i_2][2]))

x_hexagon = x_hexagon_1
y_hexagon = y_hexagon_1
z_hexagon = z_hexagon_1

# Permute order of the vectors
x_hexagon_permuted = list()
y_hexagon_permuted = list()
z_hexagon_permuted = list()
l_hexagon = list(permutations((x_hexagon, y_hexagon, z_hexagon)))
for i_1 in range(len(x_hexagon)):
    for i_2 in range(len(l_hexagon)):
        x_hexagon_permuted.append(l_hexagon[i_2][0][i_1])
        y_hexagon_permuted.append(l_hexagon[i_2][1][i_1])
        z_hexagon_permuted.append(l_hexagon[i_2][2][i_1])
