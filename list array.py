#List Angka
list1 = [1, 2, 7, 4, 1, 2, 5]
#Menu
def menu():
    print("-"*39)
    print("List\n",list1)
    print("-"*39)
    print("Menu:")
    print("1. Tambahkan data")
    print("2. Menghapus data")
    print("3. Mengupdate data")
    print("4. Mengurutkan data")
    print("5. Mencari Min dan Max data")
    print("6. Menghitung banyak data dalam list")
    print("7. Membalikkan urutan list")
    print("8. Keluar\n")

    pilih = str(input("Pilih: "))
    print("-"*39)
    if (pilih == "1"):
        tambah()
    elif (pilih == "2"):
        hapus()
    elif (pilih == "3"):
        update()
    elif (pilih == "4"):
        urut()
    elif (pilih == "5"):
        minmax()
    elif (pilih == "6"):
        itung()
    elif (pilih == "7"):
        balik()
    elif (pilih == "8"):
        keluar()
    else:
        print("Error: Masukkan angka 1 sampai 8!!")

def tambah():
    try:
        print("Pilih Fungsi:\n1. apend\n2. insert\n3. extend")
        pilih = int(input("Pilih: "))
        if(pilih==1):
            print("\n  ", list1)
            list1.append(int(input("Tambahkan angka: ")))
            print("= ", list1)

        elif(pilih==2):
            print("\n  ", list1)
            indeks=int(input("Menambah di indeks ke-"))
            angka=int(input("Masukkan angka: "))
            list1.insert(indeks, angka)
            print("= ", list1)
    
        elif(pilih==3):
            print("\n  ", list1)
            banyak=int(input("Mau masukkan berapa banyak data: "))
            for i in range(banyak):
                angka=(int((input("Masukkan angka: "))))
                list1.extend([angka])
                print("= ",list1,"\n")

        else:
            print("\nError: masukkan angka 1 sampai 3!!")
    except ValueError:
        print("\nError: masukkan angka!!")

def hapus():
    try:
        print("Pilih Fungsi:\n1. delete\n2. remove\n3. pop\n4. clear")
        pilih = int(input("Pilih: "))
        if(pilih==1):
            print("\n  ", list1)
            hapus=int(input("Hapus indeks ke: "))
            del list1[hapus]
            print("= ", list1)
    
        elif(pilih==2):
            print("\n  ", list1)
            hapus=int(input("Hapus angka: "))
            list1.remove(hapus)
            print("= ", list1)

        elif(pilih==3):
            print("\n  ", list1)
            list1.pop()
            print("Menghapus indeks terakhir\n= ", list1)

        elif(pilih==4):
            print("\n  ", list1)
            list1.clear()
            print("Menghapus isi data\n= ", list1)

        else:
            print("Error: masukkan angka 1 sampai 4!!")
    except ValueError:
        print("\nError: masukkan angka!!")

def update():
    try:
        print("  ", list1)
        index=int(input("ubah indeks ke: "))
        ubah=int(input("ubah menjadi: "))
        list1[index]= ubah
        print("= ", list1)
    except ValueError:
        print("\nError: masukkan angka!!")

def urut():
    try:
        print("Pilih Fungsi:\n1. kecil ke besar\n2. besar ke kecil")
        pilih = int(input("Pilih: "))
        if(pilih==1):
            print("\n  ", list1)
            list1.sort()
            print("kecil ke besar\n= ",list1)
        elif(pilih==2):
            print("\n  ", list1)
            list1.sort()
            list1.reverse()
            print("besar ke kecil\n= ",list1)
        else:
            print("Error: masukkan angka 1 sampai 2!!")
    except ValueError:
        print("\nError: masukkan angka!!")

def minmax():
    print("Nilai Minimum : ",min(list1))
    print("Nilai Maksimum: ",max(list1))

def itung():
    print("Element yang ada di data berjumlah: ", len(list1))

def balik():
    print("Sebelum:\n", list1)
    list1.reverse()
    print("Sesudah:\n",list1)

def keluar():
    print("Terima Kasih...")
    exit(0)


while(True):
    menu()