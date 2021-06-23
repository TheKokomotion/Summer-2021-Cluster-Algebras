import numpy as np

# Extended Exchange Matrix
A = np.array(
    [[0, -1, 1, 0, -1, 1], [1, 0, -1, 0, -1, 1], [-1, 1, 0, -1, 0, -1], [0, 0, 1, 0, -1, 0], [1, 1, 0, 1, 0, -1],
     [-1, -1, 1, 0, 1, 0], [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, -1, 0, -1, 1, 0]])

# Cluster and Frozen Variables
c_1 = [2, 1, 3]
c_2 = [2, 3, 3]
c_3 = [1, 1, 2]
c_4 = [1, 2, 0]
c_5 = [3, 3, 4]
c_6 = [1, 2, 2]
c_7 = [3, 3, 3]
c_8 = [2, 2, 2]
c_9 = [4, 4, 4]

# Extended Cluster
C = [c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9]


# Mutation Function
def mutation(cluster, array, n):
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    y = np.array(
        [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    a = [0, 0, 0]
    for i_1 in range(1, 10):
        if i_1 == n:
            for i in range(1, 10):
                if array[i - 1][i_1 - 1] > 0:
                    a = np.add([x * array[i - 1][i_1 - 1] for x in cluster[i - 1]], a)
            x[i_1 - 1] = np.subtract(a, cluster[i_1 - 1])
        else:
            x[i_1 - 1] = cluster[i_1 - 1]

    for i in range(1, 10):
        for j in range(1, 7):
            if i == n:
                y[i - 1][j - 1] = -array[i - 1][j - 1]
            elif j == n:
                y[i - 1][j - 1] = -array[i - 1][j - 1]
            elif array[i - 1][n - 1] > 0 and array[n - 1][j - 1] > 0:
                y[i - 1][j - 1] = array[i - 1][j - 1] + (array[i - 1][n - 1]) * (array[n - 1][j - 1])
            elif array[i - 1][n - 1] < 0 and array[n - 1][j - 1] < 0:
                y[i - 1][j - 1] = array[i - 1][j - 1] - (array[i - 1][n - 1]) * (array[n - 1][j - 1])
            else:
                y[i - 1][j - 1] = array[i - 1][j - 1]

    x = np.array(x).tolist()

    return x, y

# I commented out all this stuff just so that the computer wouldn't run additional tasks

# 3D Scatter Plot
# from matplotlib import pyplot
# from mpl_toolkits.mplot3d import Axes3D

# fig = pyplot.figure()
# ax = Axes3D(fig)

# Plotting Weight Vectors
# xdata = [c_1[0], c_2[0], c_3[0], c_4[0], c_5[0], c_6[0], c_7[0], c_8[0], c_9[0]]
# ydata = [c_1[1], c_2[1], c_3[1], c_4[1], c_5[1], c_6[1], c_7[1], c_8[1], c_9[1]]
# zdata = [c_1[2], c_2[2], c_3[2], c_4[2], c_5[2], c_6[2], c_7[2], c_8[2], c_9[2]]

# Axis Labels
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')

# Make Plot
# ax.scatter(xdata, ydata, zdata)
# pyplot.show()

# Confirming that new version of mutation works correctly (I think it does!)
# print(C, A)
# m_1 = mutation(C, A, 1)
# print(m_1)
# m_11 = mutation(mutation(C, A, 1)[0], mutation(C, A, 1)[1], 1)
# print(m_11)
# if C == m_11[0]:
#    print('yay 1!')
# if numpy.array_equal(A, m_11[1]) == True:
#    print('yay 2!')

# This gave c_1[0] negative originally, doesn't anymore
# m_1 = mutation(C, A, 1)
# m_13 = mutation(m_1[0], m_1[1], 3)
# m_131 = mutation(m_13[0], m_13[1], 1)
# m_1313 = mutation(m_131[0], m_131[1], 3)
# m_13131 = mutation(m_1313[0], m_1313[1], 1)
# print(m_13131)
