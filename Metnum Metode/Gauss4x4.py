from re import M
import numpy as np
print('Input Matriks')
a = float(input('Masukkan angka untuk baris 1 kolom 1 : '))
b = float(input('Masukkan angka untuk baris 1 kolom 2 : '))
c = float(input('Masukkan angka untuk baris 1 kolom 3 : '))
d = float(input('Masukkan angka untuk baris 1 kolom 4 : '))
e = float(input('Masukkan angka untuk baris 2 kolom 1 : '))
f = float(input('Masukkan angka untuk baris 2 kolom 2 : '))
g = float(input('Masukkan angka untuk baris 2 kolom 3 : '))
h = float(input('Masukkan angka untuk baris 2 kolom 4 : '))
i = float(input('Masukkan angka untuk baris 3 kolom 1 : '))
j = float(input('Masukkan angka untuk baris 3 kolom 2 : '))
k = float(input('Masukkan angka untuk baris 3 kolom 3 : '))
l = float(input('Masukkan angka untuk baris 3 kolom 4 : '))
m = float(input('Masukkan angka untuk baris 4 kolom 1 : '))
n = float(input('Masukkan angka untuk baris 4 kolom 2 : '))
o = float(input('Masukkan angka untuk baris 4 kolom 3 : '))
p = float(input('Masukkan angka untuk baris 4 kolom 4 : '))
print('Input Vektor')
q = float(input('Masukkan angka untuk baris 1 : '))
r = float(input('Masukkan angka untuk baris 2 : '))
s = float(input('Masukkan angka untuk baris 3 : '))
t = float(input('Masukkan angka untuk baris 4 : '))

A = np.array([[a,b,c,d], [e,f,g,h], [i,j,k,l],[m,n,o,p]])
n = len(A)
print('.'*30)
print('Matriks Augmentasi : ')
print(A)
B = np.array([[q],[r],[s],[t]])
print('Vektor :')
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

print('Solusi untuk metode gauss : ')
print(np.linalg.solve(A1, B1))