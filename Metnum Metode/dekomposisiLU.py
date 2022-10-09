print('Input Matriks')
import numpy as np

# Mengiputkan nilai matrix
a = float(input('Masukkan angka untuk baris 1 kolom 1 : '))
b = float(input('Masukkan angka untuk baris 1 kolom 2 : '))
c = float(input('Masukkan angka untuk baris 1 kolom 3 : '))
d = float(input('Masukkan angka untuk baris 2 kolom 1 : '))
e = float(input('Masukkan angka untuk baris 2 kolom 2 : '))
f = float(input('Masukkan angka untuk baris 2 kolom 3 : '))
g = float(input('Masukkan angka untuk baris 3 kolom 1 : '))
h = float(input('Masukkan angka untuk baris 3 kolom 2 : '))
i = float(input('Masukkan angka untuk baris 3 kolom 3 : '))

# menginputkan nilai vektor
print('Input Vektor')
j = float(input('Masukkan angka untuk baris 1 : '))
k = float(input('Masukkan angka untuk baris 2 : '))
l = float(input('Masukkan angka untuk baris 3 : '))

# memasukkan nilai variabel yang sudah di inputkan menjadi sebuah array
A = np.array([[a,b,c], [d,e,f], [g,h,i]])
print('.'*30)
print('Matriks augmentasi : ')
print(A)
B = np.array([[j],[k],[l]])
print('Vektor : ')
print(B)

det = np.linalg.det(A)
if det == 0:
    print('Elemen diagonal pertama bernilai 0, proses hitung tidak bisa dilanjutkan')
    print('.'*30)
else:
    x = np.linalg.solve(A,B)
    print('Solusi untuk metode dekomposisi LU : ')
    print(x)