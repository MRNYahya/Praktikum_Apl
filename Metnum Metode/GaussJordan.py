import numpy as np
def gssjrdn(a,b):
    a = np.array(a, float)
    b = np.array(b, float)
    n = len(b)
    #Looping
    for k in range(n):
        #Pivot parsial
        if np.fabs(a[k,k]) < 1.0e-12:
            for i in range(k+1,n):
                if np.fabs(a[i,k]) > np.fabs(a[k,k]):
                    for j in range(k,n):
                        a[k,j],a[i,j] = a[i,j],a[k,j]
                    b[k],b[i] = b[i],b[k]
                    break
        #Pembagian baris pivot
        pivot = a[k,k]
        for j in range(k,n):
            a[k,j] /= pivot
        b[k] /= pivot
        #Eliminasi
        for i in range(n):
            if i == k or a[i,k] ==0: continue
            factor = a[i,k]
            for j in range(k,n):
                a[i,j] -= factor * a[k,j]
            b[i] -= factor * b[k]
    return b,a

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
a = np.array([[z,y,x], [w,v,u], [t,s,r]])
b = np.array([[q],[p],[o]])
print('.'*30)
print('Matriks augmentasi :')
print(a)
print('Vektor : ')
print(b)

# A menjadi matriks idenntitas
X, A = gssjrdn(a,b)
print('Solusi untuk metode gauss-jordan : ')
print(X)