# Preamble
import numpy as np
from itertools import permutations
from D_A_Storage import e_2
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

# Matrix Lambda for Task2.py
A_2 = np.diag(e_2)

# Combine coordinate data into big lists:

# Eigenvectors: [4.30788144, 1.2769152, 3.51255544]
# x-data:
x = x_2 + x_3 + x_4 + x_5 + x_6 + x_7 + x_8 + x_9 + x_10 + x_11
# y-data:
y = y_2 + y_3 + y_4 + y_5 + y_6 + y_7 + y_8 + y_9 + y_10 + y_11
# z-data:
z = z_2 + z_3 + z_4 + z_5 + z_6 + z_7 + z_8 + z_9 + z_10 + z_11

# Permute order of the vectors
x_new = list()
y_new = list()
z_new = list()
l_1 = list(permutations((x, y, z)))
for i_1 in range(len(x)):
    for i_2 in range(len(l_1)):
        x_new.append(l_1[i_2][0][i_1])
        y_new.append(l_1[i_2][1][i_1])
        z_new.append(l_1[i_2][2][i_1])
