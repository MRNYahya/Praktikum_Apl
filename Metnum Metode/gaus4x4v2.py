from re import M
import numpy as np
import os

os.system('cls')

print("------------------------------------------")
print("-- 2009106029 Muhamad Rizky Nilzamyahya --")
print("------------------------------------------\n")

A = np.array ([[1.0, 2.0, 3.0, -1.0], 
               [2.0, 5.0, 4.0, 8.0],
               [4.0, 2.0, 2.0, 1.0],
               [6.0, 4.0, -1.0 ,-2.0]])

B = np.array ([10.0, 8.0, -2.0, 4.0])


n = len(A)
print('Matriks Augmentasi : ')
print(A)

print('\nVektor :')
print(B)

A1 = np.copy(A)
B1 = np.copy(B)

# Eliminasi baris
for k in range(0,n-1):
    for i in range(k+1,n):
        ratio = A[i,k]/A[k,k]
        for j in range(k, n-1):
            A[i,j] -= ratio*A[k,j]
        B[i] -= ratio*B[k]
# Substitusi mundur
x = np.zeros(n)
x[n-1] = B[n-1]/A[n-1, n-1]
for i in range(n-2,-1,-1):
    sum_j = 0
    for j in range(i+1,n):
        sum_j += A[i,j]*x[j]
    x[i] = (B[i] - sum_j)/A[i,i]

print('\nSolusi untuk metode gauss : ')
print(np.linalg.solve(A1, B1))
print("")