import numpy as np

print('Input Matriks')  # Mengiputkan nilai matrix
z = float(input('Masukkan angka untuk baris 1 kolom 1 : '))
y = float(input('Masukkan angka untuk baris 1 kolom 2 : '))
x = float(input('Masukkan angka untuk baris 1 kolom 3 : '))
w = float(input('Masukkan angka untuk baris 2 kolom 1 : '))
v = float(input('Masukkan angka untuk baris 2 kolom 2 : '))
u = float(input('Masukkan angka untuk baris 2 kolom 3 : '))
t = float(input('Masukkan angka untuk baris 3 kolom 1 : '))
s = float(input('Masukkan angka untuk baris 3 kolom 2 : '))
r = float(input('Masukkan angka untuk baris 3 kolom 3 : '))
print('Input Vektor')# menginputkan nilai vektor
q = float(input('Masukkan angka untuk baris 1 : '))
p = float(input('Masukkan angka untuk baris 2 : '))
o = float(input('Masukkan angka untuk baris 3 : '))

# memasukkan nilai variabel yang sudah di inputkan menjadi sebuah array
matriks = np.array([[z,y,x], [w,v,u], [t,s,r]])
vektor = np.array([[q],[p],[o]])
det = np.linalg.det(matriks)
if det == 0:
    print('Matriks ini tidak memiliki invers')
    print(matriks)
else:
    print('.'*30)
    print('Matriks augmentasi :')
    print(matriks)

    print('Vektor : ')
    print(vektor)

    invers = np.linalg.inv(matriks)
    np.set_printoptions(precision=3)
    print('Matriks invers : ')
    print(invers)

    print('Solusi untuk metode matriks balikan : ')
    hasil = np.dot(invers, vektor)
    np.set_printoptions(suppress=True)
    print(hasil)