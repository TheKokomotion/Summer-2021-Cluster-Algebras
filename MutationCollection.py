# Preamble
from MutationFunction import mutation


# List of good mutations distance k from the seed


def list_maker(k):
    mutation_list = list()
    r = list(range(1, 7))
    for i in range(1, k + 1):
        if i == 1:
            for l in r:
                m_i = l
                mutation_list.append(m_i)
        else:
            for l in r:
                m_i = l
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
    for l in range(6 * (5 ** (k - 1))):
        for n in range(k):
            a = int(str(list_maker(k)[l])[n])
            if n == 0:
                (x, y) = mutation(cluster, array, a)
            else:
                (x, y) = mutation(x, y, a)
        mutation_list.append(x)
    return mutation_list
