#Tema: Menghitung Luas dan Keliling Trapesium

print("")
print("Diketahui:")
AB = int(input("AB = "))
BC = int(input("BC = "))
CD = int(input("CD = "))
DA = int(input("DA = "))
t = int(input("t = "))

print("")
print("Menghitung Luas Trapesium")
print("Rumus: ")
print("L = 0.5 * (AB + CD) * t")
L = float(0.5) * (AB + CD) * t
print("Luas Trapesium: ", L)
print(" ")

print("Menghitung Keliling Trapesium")
print("Rumus:")
print("K = AB + BC + CD + DA")
K = AB + BC + CD + DA
print("Keliling Trapesium: ", K)