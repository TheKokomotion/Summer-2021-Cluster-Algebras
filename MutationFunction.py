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
    b = [0, 0, 0]
    for l in range(1, 10):
        if l == n:
            for j in range(1, 7):
                if array[l - 1][j - 1] > 0:
                    a = np.add([x * array[l - 1][j - 1] for x in cluster[j - 1]], a)
            for i in range(1, 7):
                if array[i - 1][l - 1] > 0:
                    b = np.add([x * array[i - 1][l - 1] for x in cluster[i - 1]], b)
            x[l - 1] = np.subtract(np.add(a, b), cluster[l - 1])
        else:
            x[l - 1] = cluster[l - 1]

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
