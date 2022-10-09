import numpy as np
print('Input Matriks')
z = float(input('Masukkan angka untuk baris 1 kolom 1 : '))
y = float(input('Masukkan angka untuk baris 1 kolom 2 : '))
x = float(input('Masukkan angka untuk baris 1 kolom 3 : '))
w = float(input('Masukkan angka untuk baris 2 kolom 1 : '))
v = float(input('Masukkan angka untuk baris 2 kolom 2 : '))
u = float(input('Masukkan angka untuk baris 2 kolom 3 : '))
t = float(input('Masukkan angka untuk baris 3 kolom 1 : '))
s = float(input('Masukkan angka untuk baris 3 kolom 2 : '))
r = float(input('Masukkan angka untuk baris 3 kolom 3 : '))
print('Input Vektor')
q = float(input('Masukkan angka untuk baris 1 : '))
p = float(input('Masukkan angka untuk baris 2 : '))
o = float(input('Masukkan angka untuk baris 3 : '))

A = np.array([[z,y,x], [w,v,u], [t,s,r]])
n = len(A)
print('.'*30)
print('Matriks Augmentasi : ')
print(A)
B = np.array([[q],[p],[o]])
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