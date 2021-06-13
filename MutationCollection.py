# Preamble
import numpy as np
from MutationFunction import mutation
from MutationFunction import A
from MutationFunction import C

# List of good mutations distance k from the seed
mutation_list = list()


def list_maker(k):
    r = list(range(1, 7))
    for i in range(1, k + 1):
        m_i = 0
        if i == 1:
            for l in r:
                m_i = l
                mutation_list.append(m_i)
        else:
            for l in r:
                m_i = l
                for k in range(6 * 5 ** (i-2)):
                    if m_i != int(str(mutation_list[k])[i-2]):
                        a = int(str(mutation_list[k]) + str(m_i))
                        mutation_list.append(a)
            for n in range(6 * 5 ** (i-2)):
                del mutation_list[0]
    return mutation_list


# Example
list_maker(8)
print(mutation_list)
print(len(mutation_list))

# Mutations Distance 1 from the initial seed (work in progress)
M_1 = (mutation(C, A, 1), mutation(C, A, 2), mutation(C, A, 3), mutation(C, A, 4), mutation(C, A, 5), mutation(C, A, 6))
