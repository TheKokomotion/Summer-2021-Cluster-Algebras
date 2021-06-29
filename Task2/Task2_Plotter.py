# Preamble
# import numpy as np
from math import log10
from itertools import permutations
from matplotlib import pyplot
# from D_A_Storage import e_2
from D_A_Compiling import x_shield_permuted
from D_A_Compiling import y_shield_permuted
from D_A_Compiling import z_shield_permuted
from D_A_Compiling import x_eigenvalues_shield
from D_A_Compiling import y_eigenvalues_shield
from D_A_Compiling import z_eigenvalues_shield
from D_A_Compiling import x_triangle_permuted
from D_A_Compiling import y_triangle_permuted
from D_A_Compiling import z_triangle_permuted
from D_A_Compiling import x_triangle
from D_A_Compiling import y_triangle
from D_A_Compiling import z_triangle
from D_A_Compiling import x_eigenvalues_triangle
from D_A_Compiling import y_eigenvalues_triangle
from D_A_Compiling import z_eigenvalues_triangle
from D_A_Compiling import x_mystery_permuted
from D_A_Compiling import y_mystery_permuted
from D_A_Compiling import z_mystery_permuted
from D_A_Compiling import x_primes_permuted
from D_A_Compiling import y_primes_permuted
from D_A_Compiling import z_primes_permuted
from D_A_Compiling import x_eigenvalues_tri2
from D_A_Compiling import y_eigenvalues_tri2
from D_A_Compiling import z_eigenvalues_tri2
from D_A_Compiling import x_tri2_permuted
from D_A_Compiling import y_tri2_permuted
from D_A_Compiling import z_tri2_permuted
from D_A_Compiling import x_eigenvalues_test
from D_A_Compiling import y_eigenvalues_test
from D_A_Compiling import z_eigenvalues_test
from D_A_Compiling import x_test_permuted
from D_A_Compiling import y_test_permuted
from D_A_Compiling import z_test_permuted
from D_A_Compiling import x_eigenvalues_hexagon
from D_A_Compiling import y_eigenvalues_hexagon
from D_A_Compiling import z_eigenvalues_hexagon
from D_A_Compiling import x_hexagon_permuted
from D_A_Compiling import y_hexagon_permuted
from D_A_Compiling import z_hexagon_permuted
from D_A_Compiling import x_hexagon
from D_A_Compiling import y_hexagon
from D_A_Compiling import z_hexagon
from D_A_Compiling import x_test_0_det_permuted
from D_A_Compiling import y_test_0_det_permuted
from D_A_Compiling import z_test_0_det_permuted

# 3D Scatter Plot
fig = pyplot.figure()
ax_1 = fig.add_subplot(111, projection='3d')

# Axis Labels
ax_1.set_xlabel('X-axis')
ax_1.set_ylabel('Y-axis')
ax_1.set_zlabel('Z-axis')

# Scatter Plot (add eigenvalues)
# ax_1.scatter(x_eigenvalues_triangle, y_eigenvalues_triangle, z_eigenvalues_triangle, color='Blue')
# ax_1.scatter(x_eigenvalues_shield, y_eigenvalues_shield, z_eigenvalues_shield, color='Orange')
# ax_1.scatter(x_eigenvalues_tri2, y_eigenvalues_tri2, z_eigenvalues_tri2, color='Blue')
# ax_1.scatter(x_eigenvalues_test, y_eigenvalues_test, z_eigenvalues_test, color='Blue')
# ax_1.scatter(x_eigenvalues_hexagon, y_eigenvalues_hexagon, z_eigenvalues_hexagon, color='Blue')

# Scatter Plot midpoint
# ax_1.scatter([log10(1.2 * 0.5 * 1.1) / 3], [log10(1.2 * 0.5 * 1.1) / 3], [log10(1.2 * 0.5 * 1.1) / 3], color ='Blue')

# Lines Connecting Eigenvalues
# permute_test = list(permutations(range(6)))
# x_temp = list()
# y_temp = list()
# z_temp = list()
# for i in range(20):
#     for j in range(6):
#         x_temp.append(x_eigenvalues_test[permute_test[i][j]])
#         y_temp.append(y_eigenvalues_test[permute_test[i][j]])
#         z_temp.append(z_eigenvalues_test[permute_test[i][j]])
#     ax_1.plot(x_temp, y_temp, z_temp, color='Blue')

# Scatter Plot (with permutations)
# ax_1.scatter(x_triangle, y_triangle, z_triangle, color='Red')
ax_1.scatter(x_hexagon, y_hexagon, z_hexagon, color='Orange')

# Scatter Plot (with permutations)
# ax_1.scatter(x_triangle_permuted, y_triangle_permuted, z_triangle_permuted, color='Red')
# ax_1.scatter(x_shield_permuted, y_shield_permuted, z_shield_permuted, color='Blue')
# ax_1.scatter(x_mystery_permuted, y_mystery_permuted, z_mystery_permuted, color='Green')
# ax_1.scatter(x_primes_permuted, y_primes_permuted, z_primes_permuted, color='Orange')
# ax_1.scatter(x_tri2_permuted, y_tri2_permuted, z_tri2_permuted, color='Orange')
# ax_1.scatter(x_test_permuted, y_test_permuted, z_test_permuted, color='Orange')
# ax_1.scatter(x_hexagon_permuted, y_hexagon_permuted, z_hexagon_permuted, color='Orange')
# ax_1.scatter(x_test_0_det_permuted, y_test_0_det_permuted, z_test_0_det_permuted, color='Red')

# Plane that triangle points lie in
# x = np.linspace(.1, .4, 5)
# y = np.linspace(.3, .6, 5)
# X, Y = np.meshgrid(x, y)
# Z = log10(e_2[0] * e_2[1] * e_2[2]) - X - Y
# ax_1.plot_surface(X, Y, Z)

# Show Plot
pyplot.show()
