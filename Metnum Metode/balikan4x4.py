import numpy as np
import os

os.system('cls')

print("------------------------------------------")
print("-- 2009106029 Muhamad Rizky Nilzamyahya --")
print("------------------------------------------\n")

matriks = np.array ([[1.0, 2.0, 3.0, -1.0], 
               [2.0, 5.0, 4.0, 8.0],
               [4.0, 2.0, 2.0, 1.0],
               [6.0, 4.0, -1.0 ,-2.0]])

vektor = np.array ([10.0, 8.0, -2.0, 4.0])

det = np.linalg.det(matriks)
if det == 0:
    print('Matriks ini tidak memiliki invers')
    print(matriks)
else:
    print('Matriks augmentasi :')
    print(matriks)

    print('\nVektor : ')
    print(vektor)

    invers = np.linalg.inv(matriks)
    np.set_printoptions(precision=3)
    print('\nMatriks invers : ')
    print(invers)

    print('\nSolusi untuk metode matriks balikan : ')
    hasil = np.dot(invers, vektor)
    np.set_printoptions(suppress=True)
    print(hasil)
    print("")