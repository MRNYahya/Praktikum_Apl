#Tema: Balok

import os

listLP=[]
listK=[]
listV=[]
Jawaban=[]
biner=[]

def reset():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    try:
        reset()
        print("Tentukan Nilai dari: \n1.Luas permukaan balok \n2.Keliling balok \n3.Volume Balok")
        print("\nBeserta nilai biner dari setiap hasil\n")
        pilih = int(input("Pilih: "))
        if pilih == 1:
            luas()
        elif pilih == 2:
            keliling()
        elif pilih == 3:
            volume()
        else:
            print("Masukkan ANgka 1 sampai 3!!")

    except ValueError:
        print("Error: Masukkan Angka!!")

#MENCARI NILAI LUAS PERMUKAAN DAN NILAI BINERNYA
def luas():
    try:
        reset()
        print("----------------------------------------------------")
        print("a.Luas Permukaan \n\nDiketahui:")
        p1 = int(input("p = "))
        l1 = int(input("l = "))
        t1 = float(input("t = "))
        print("----------------------------------------------------")
        print("Rumus:")
        print("L = 2 * ((p * l) + (p * t) + (l * t))")
        L = 2 * ((p1 * l1) + (p1 * t1) + (l1 * t1))
        print("Luas Permukaan Balok =", L)
        
        desimal = int(L)
        binerL = bin(desimal) .replace("b","")
        print("Nilai biner =", binerL)
        print("----------------------------------------------------")
        input("                   < Tekan Enter >                  ")
        print("----------------------------------------------------")

        listLP.append(p1)
        listLP.append(l1)
        listLP.append(t1)
        listLP.append(L)
        Jawaban.append(L)
        biner.append(binerL)

        list1()

    except ValueError:
        print("Error: Masukkan Angka!!")

#MENCARI NILAI KELILING DAN NILAI BINERNYA
def keliling():
    try:
        reset()
        print("----------------------------------------------------")
        print("b.Keliling \n\nDiketahui:")
        p2 = int(input("p = "))
        l2 = int(input("l = "))
        t2 = float(input("t = "))
        print("----------------------------------------------------")
        print("Rumus:")
        print("K = 4 * (p + l + t)")
        K = 4 * (p2 + l2 + t2)
        print("Keliling Balok = ", K)

        desimal = int(K)
        binerK = bin(desimal) .replace("b","")
        print("Nilai biner = ", binerK)
        print("----------------------------------------------------")
        input("                   < Tekan Enter >                  ")
        print("----------------------------------------------------")

        listK.append(p2)
        listK.append(l2)
        listK.append(t2)
        listK.append(K)
        Jawaban.append(K)
        biner.append(binerK)
        list2()

    except ValueError:
        print("Error: Masukkan Angka!!")

#MENCARI NILAI VOLUME SAMA NILAI BINERNYA
def volume():
    try:
        reset()
        print("----------------------------------------------------")
        print("c.Volume \n\nDiketahui:")
        p3 = int(input("p = "))
        l3 = int(input("l = "))
        t3 = float(input("t = "))
        print("----------------------------------------------------")
        print("Rumus:")
        print("V = p * l * t")
        V = p3 * l3 * t3
        print("Volume Balok = ", V)

        desimal = int(V)
        binerV = bin(desimal) .replace("b","")
        print("Nilai biner = ", binerV)
        print("----------------------------------------------------")
        input("                   < Tekan Enter >                  ")
        print("----------------------------------------------------")

        listV.append(p3)
        listV.append(l3)
        listV.append(t3)
        listV.append(V)
        Jawaban.append(V)    
        biner.append(binerV)
        list3()

    except ValueError:
        print("Error: Masukkan Angka!!")

#PRINT ISI LIST
def list1():
    print("List Luas Permukaan:")
    print("p =", listLP[0])
    print("l =", listLP[1])
    print("t =", listLP[2])
    print("Luas Permukaan =", listLP[3])
    print("L =", Jawaban[0])
    print("Biner L =", biner[0])
    print("----------------------------------------------------")
    input("                   < Tekan Enter >                  ")
    print("----------------------------------------------------")
    listLP.clear()

def list2():
    print("List Keliling:")
    print("p =", listK[0])
    print("l =", listK[1])
    print("t =", listK[2])
    print("Keliling =", listK[3])
    print("K =", Jawaban[0])
    print("Biner K =", biner[0])
    print("----------------------------------------------------")
    input("                   < Tekan Enter >                  ")
    print("----------------------------------------------------")
    listK.clear()

def list3():
    print("List Volume:")
    print("p =", listV[0])
    print("l =", listV[1])
    print("t =", listV[2])
    print("Volume =", listV[3])
    print("V =", Jawaban[0])
    print("Biner V =", biner[0])
    print("----------------------------------------------------")
    input("                   < Tekan Enter >                  ")
    print("----------------------------------------------------")
    listV.clear()   

menu()