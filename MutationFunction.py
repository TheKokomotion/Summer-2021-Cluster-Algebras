import numpy as np

#Index Sets
I=[1,2,3,4,5,6,7,8,9]
J=[1,2,3,4,5,6]

#Extended Exchange Matrix
A = np.array([[0,-1,1,0,-1,1],[1,0,-1,0,-1,1],[-1,1,0,-1,0,-1],[0,0,1,0,-1,0],[1,1,0,1,0,-1],[-1,-1,1,0,1,0],[-1,1,0,0,0,0],[0,0,-1,1,0,0],[0,-1,0,-1,1,0]])
print(A)
print()

#Cluster and Frozen Variables
c_1=[2,1,3]
c_2=[2,3,3]
c_3=[1,1,2]
c_4=[1,2,0]
c_5=[3,3,4]
c_6=[1,2,2]
c_7=[3,3,3]
c_8=[2,2,2]
c_9=[4,4,4]


#Extended Cluster
C=[c_1,c_2,c_3,c_4,c_5,c_6,c_7,c_8,c_9]
print(C)
print()

#Mutation Function
def mutation(n):
    for l in I:
        if l==n:
            a = [0, 0, 0]
            b = [0, 0, 0]
            for j in J:
                if A[l-1][j-1] > 0:
                    a = np.add([x * A[l-1][j-1] for x in C[j-1]], a)
            for i in J:
                if A[i-1][l-1] > 0:
                    b = np.add([x * A[i-1][l-1] for x in C[i-1]], b)
            C[l-1] = np.subtract(np.add(a, b), C[l-1])
        else:
            C[l-1]=C[l-1]

    for i in I:
        for j in J:
            if i==n:
                A[i - 1][j - 1]=-A[i - 1][j - 1]
            elif j==n:
                A[i - 1][j - 1] =-A[i - 1][j - 1]
            elif A[i - 1][n - 1] > 0 and A[n - 1][j - 1] > 0:
                A[i - 1][j - 1] = A[i - 1][j - 1] + (A[i - 1][n - 1])*(A[n - 1][j - 1])
            elif A[i - 1][n - 1] < 0 and A[n - 1][j - 1] < 0:
                A[i - 1][j - 1] = A[i - 1][j - 1] - (A[i - 1][n - 1]) * (A[n - 1][j - 1])
            else:
                A[i - 1][j - 1] = A[i - 1][j - 1]
    print(A)
    print()
    print(C)



