import numpy as np
import os

os.system('cls' if os.name == 'nt' else 'clear')
print("NIM: 2009106029")
print("Nama: Muhamad Rizky Nilzamyahya")
print("Kelas: Informatika A 2020")

y = np.array([2,5,3,7,6,10,9,8,1,0,4,12,11])
print("\n[ UAS APL: Tugas 1 ]\nList Array:\n",y)
print("\nJawaban:")
print(y[-4:-2])

b = np.array([[54,43,7,5,6],[4,4,55,89,34],[34,2,12,12,5],[45,8,7,82,11],[67,15,23,32,60]])
print("\n[ UAS APL: Tugas 2 ]\nList Array:\n\n",b)
print("\nJawaban:\n1. ")
print(b[0:,1:2])
print("\n2.")
print(b[2:3,0:])
print("\n3.")
print(b[1:4,1:4])
print("\n4.")
print(b[2:4,3:5])