# Preamble
from matplotlib import pyplot
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
from D_A_Storage import x_2
from D_A_Storage import y_2
from D_A_Storage import z_2
from D_A_Storage import x_3
from D_A_Storage import y_3
from D_A_Storage import z_3
from D_A_Storage import x_4
from D_A_Storage import y_4
from D_A_Storage import z_4


# 3D Scatter Plot
fig = pyplot.figure()
ax_1 = fig.add_subplot(111, projection='3d')

# Axis Labels
ax_1.set_xlabel('X-axis')
ax_1.set_ylabel('Y-axis')
ax_1.set_zlabel('Z-axis')

# Make Plot
ax_1.scatter(x_2, y_2, z_2, color='Red')
ax_1.scatter(x_3, y_3, z_3, color='Red')
ax_1.scatter(x_4, y_4, z_4, color='Red')
pyplot.show()
