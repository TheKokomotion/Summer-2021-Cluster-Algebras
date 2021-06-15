# Preamble
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from MutationFunction import mutation
from MutationFunction import A
from MutationFunction import C


# List of good mutations distance k from the seed


def list_maker(k):
    mutation_list = list()
    r = range(1, 7)
    for i in range(1, k + 1):
        if i == 1:
            for q in r:
                m_i = q
                mutation_list.append(m_i)
        else:
            for q in r:
                m_i = q
                for k in range(6 * 5 ** (i - 2)):
                    if m_i != int(str(mutation_list[k])[i - 2]):
                        a = int(str(mutation_list[k]) + str(m_i))
                        mutation_list.append(a)
            for n in range(6 * 5 ** (i - 2)):
                del mutation_list[0]
    return mutation_list


# Mutations Distance k from seed
def mutation_collection(cluster, array, k):
    mutation_list = list()
    for i in range(6 * (5 ** (k - 1))):
        for n in range(k):
            a = int(str(list_maker(k)[i])[n])
            if n == 0:
                (x, y) = mutation(cluster, array, a)
            else:
                (x, y) = mutation(x, y, a)
        mutation_list.append(x)
    return mutation_list


# 3D Scatter Plot
fig_1 = pyplot.figure()
ax_1 = Axes3D(fig_1)

# Axis Labels
ax_1.set_xlabel('X-axis')
ax_1.set_ylabel('Y-axis')
ax_1.set_zlabel('Z-axis')


# Plotting Weight Vectors
def plot(cluster, array, k):
    x = list()
    y = list()
    z = list()
    m = mutation_collection(cluster, array, k)
    for i in range(6 * (5 ** (k - 1))):
        for j in range(9):
            x.append(m[i][j][0])
            y.append(m[i][j][1])
            z.append(m[i][j][2])
    return [x, y, z]


# Make Plot
p = plot(C, A, 4)
ax_1.scatter(p[0], p[1], p[2])
pyplot.show()
