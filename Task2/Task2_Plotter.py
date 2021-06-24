# Preamble
# import numpy as np
# from math import log10
from matplotlib import pyplot
# from D_A_Storage import e_2
from D_A_Compiling import x_shield_permuted
from D_A_Compiling import y_shield_permuted
from D_A_Compiling import z_shield_permuted
from D_A_Compiling import x_triangle_permuted
from D_A_Compiling import y_triangle_permuted
from D_A_Compiling import z_triangle_permuted


# 3D Scatter Plot
fig = pyplot.figure()
ax_1 = fig.add_subplot(111, projection='3d')

# Axis Labels
ax_1.set_xlabel('X-axis')
ax_1.set_ylabel('Y-axis')
ax_1.set_zlabel('Z-axis')

# Scatter Plot (without permutations)
# ax_1.scatter(x_shield, y_shield, z_shield, color='Red')

# Scatter Plot (with permutations)
# ax_1.scatter(x_triangle_permuted, y_triangle_permuted, z_triangle_permuted, color='Red')
ax_1.scatter(x_shield_permuted, y_shield_permuted, z_shield_permuted, color='Blue')

# Plane that triangle points lie in
# x = np.linspace(.1, .4, 5)
# y = np.linspace(.3, .6, 5)
# X, Y = np.meshgrid(x, y)
# Z = log10(e_2[0] * e_2[1] * e_2[2]) - X - Y
# ax_1.plot_surface(X, Y, Z)

# Show Plot
pyplot.show()
