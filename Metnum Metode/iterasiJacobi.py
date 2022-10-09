import numpy as np
import os

os.system('cls')

print("------------------------------------------")
print("-- 2009106029 Muhamad Rizky Nilzamyahya --")
print("------------------------------------------\n")

limit_iterasi = 30

A = np.array ([[1.0, 2.0, 3.0, -1.0], 
               [2.0, 5.0, 4.0, 8.0],
               [4.0, 2.0, 2.0, 1.0],
               [6.0, 4.0, -1.0 ,-2.0]])

b = np.array ([10.0, 8.0, -2.0, 4.0])

print ("Iterasi Jacobi")
for i in range (A.shape[0]):
    row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    print(" + ".join(row), "=", b[i])
    print()

x = np.zeros_like(b)
for hitung in range (limit_iterasi):
    
    x_baru = np.zeros_like(x)

    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_baru[i] = (b[i] - s1 - s2)/ A[i,i]
    
    if np.allclose(x, x_baru, atol=1e-10,rtol=0.):
        break

x = x_baru

print("Solusi")
print(x)
error = np.dot(A, x)-b
print("Error:")
print(error)