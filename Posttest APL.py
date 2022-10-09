#Nama: Muhamad Rizky Nilzamyahya
#NIM: 2009106029
#Kelas Informatika A 2020
#Tema/Judul: Penjualan Minuman

import os
import time

listM=[]
listH=[]
pembeli={"data":[]} #Nampung data pembeli yang menggunakan aplikasi

def reset():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_awal():
    try:
        reset()
        listM.clear()
        listH.clear()
        print("----------------------------------------------------")
        print("           Anda ingin masuk sebagai apa?            ")
        print("----------------------------------------------------")
        print("1. Customer                                         ")
        print("2. Admin                                            ")
        print("3. Keluar                                           ")
        print("----------------------------------------------------")
        Login = int(input("Pilih : "))

        if (Login ==1):
            login()
        elif (Login == 2):
            x = 5
            while x > 0:
                reset()
                print("----------------------------------------------------")
                print("          Masukkan Username dan Password            ")
                print("----------------------------------------------------")
                User = str(input("Username : "))
                Password = str(input("Password : "))
                
                if (User == "admin" and Password == "2009106029"):
                    print("----------------------------------------------------")
                    print("                 Berhasil Masuk !!!                 ")
                    print("----------------------------------------------------")
                    input("                   < Tekan Enter >                  ")
                    admin()
                else:
                    x -= 1
                    if (User == "admin" and Password != "2009106029"):
                        print("\nError: Password yang anda masukkan salah !!!\nKesempatan :[", x,"]")
                        print("----------------------------------------------------")
                        time.sleep(3)

                    elif (User != "admin" and Password == "2009106029"):
                        print("\nError: Username yang dimasukkan tidak terdata !!!\nKesempatan :[", x,"]")
                        print("----------------------------------------------------")
                        time.sleep(3)

                    else:
                        print("\nError: Username yang dimasukkan tidak terdata !!! \nKesempatan :[", x,"]")
                        print("----------------------------------------------------")
                        time.sleep(3)

                    if x == 0:
                        print("            Kesempatan Anda telah habis             ") 
                        print("               Kembali Ke Menu Awal?                 ")
                        print("----------------------------------------------------")
                        input("                  < Tekan Enter >")
                        menu_awal()

        elif (Login == 3):
            keluar()
            
        else:
            print("\nError: Masukkan angka 1 sampai 3 !!               ")
            print("----------------------------------------------------")
            menu_awal()
    
    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        time.sleep(2)

def login():
    try:
        reset()
        print("----------------------------------------------------")
        print("                 Masukkan data Anda                 ")
        print("----------------------------------------------------")
        name = str(input("Nama   : "))
        age = str(input("Umur   : "))
        alamat = str(input("Alamat : "))
        email = str(input("Email  : "))

        pembeli["data"].append([name, age, alamat, email])

        print("----------------------------------------------------")
        print("              Akun berhasil di buat !!!             ")
        print("----------------------------------------------------")
        input("                   < Tekan Enter >                  ")
        menu()

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        time.sleep(2)

def admin():
    try:
        reset()
        print("----------------------------------------------------")
        print("                     Menu Admin                     ")
        print("----------------------------------------------------")
        print("1. Lihat Data Pengunjung                            ")
        print("2. Mengubah Data Pengunjung                         ")
        print("3. Menghapus Data Pengunjung                        ")
        print("4. Mencari Data                                     ")
        print("5. Log out                                          ")
        print("----------------------------------------------------")
        pilih = int(input("Pilih : "))

        if (pilih == 1):
            monitor()
        elif (pilih == 2):
            update()
        elif (pilih == 3):
            delete()
        elif (pilih == 4):
            try:
                def linearSearch(array,n,x):
                    for i in range(0,n):
                        if(array[i] == x):
                            return i
                    return -1

                x = input("Masukkan data yang di cari: ")
                n = 4

                for i in range(n):
                    result = linearSearch(pembeli["data"][i], n, x)
                    if result != -1:
                        print(f"\nData berada pada indeks ke-{i}\nidentitas ke-{result+1}")
                        break
                if result == -1:
                    print("Data yang anda cari tidak ada!!!")

                print("----------------------------------------------------")
                input("              < Kembali: Tekan Enter >              ")
                admin()

            except IndexError:
                print("\n----------------------------------------------------")
                print("           Data yang anda cari tidak ada!!!         ")
                print("----------------------------------------------------")
                input("              < Kembali: Tekan Enter >              ")

        elif (pilih == 5):
            menu_awal()

        else:
            print("\nError: Masukkan angka 1 sampai 5 !!!")
            print("----------------------------------------------------")
            time.sleep(2)
            admin()
        
    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        time.sleep(2)
        admin()

def monitor():
    reset()
    print("----------------------------------------------------")
    print("                  Data Pengunjung                   ")
    for i in range (len(pembeli["data"])):
        n = len(pembeli["data"])
        quickSortDesc(pembeli["data"], 0, n-1)
        print("----------------------------------------------------")
        print("                   Indeks [",i,"]                   ")
        print("----------------------------------------------------")
        print("Nama   : ",(pembeli["data"][i][0]))
        print("Umur   : ",(pembeli["data"][i][1]))
        print("Alamat : ",(pembeli["data"][i][2]))
        print("Email  : ",(pembeli["data"][i][3]))

    print("----------------------------------------------------")
    input("              < Kembali: Tekan Enter >              ")
    admin()

def update():
    try:
        reset()
        print("----------------------------------------------------")
        print("                    Update Data                     ")
        print("----------------------------------------------------")
        for i in range (len(pembeli["data"])):
            n = len(pembeli["data"])
            quickSortDesc(pembeli["data"], 0, n-1)
            print("                   Indeks [",i,"]                   ")
            print("----------------------------------------------------")
            print("Nama   : ",(pembeli["data"][i][0]))
            print("Umur   : ",(pembeli["data"][i][1]))
            print("Alamat : ",(pembeli["data"][i][2]))
            print("Email  : ",(pembeli["data"][i][3]))
            print("----------------------------------------------------")

        y = int(input("Mengubah data indeks ke : "))
        reset()
        print("----------------------------------------------------")
        print("                 Masukkan Data Baru                 ")
        print("----------------------------------------------------")
        name = str(input("Nama   : "))
        age = str(input("Umur   : "))
        alamat = str(input("Alamat : "))
        email = str(input("Email  : "))
        pembeli["data"][y] = [name, age, alamat, email]
            
        print("----------------------------------------------------")
        print("               Data berhasil disimpan               ")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")
        admin()

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        time.sleep(2)
        update()

    except IndexError:
        print("----------------------------------------------------")
        print("          Data yang anda inginkan tidak ada         ")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")
        admin()

def delete():
    try:
        reset()
        print("----------------------------------------------------")
        print("                    Hapus Data                      ")
        print("----------------------------------------------------")
        for i in range (len(pembeli["data"])):
            n = len(pembeli["data"])
            quickSortDesc(pembeli["data"], 0, n-1)
            print("                   Indeks [",i,"]                   ")
            print("----------------------------------------------------")
            print("Nama   : ",(pembeli["data"][i][0]))
            print("Umur   : ",(pembeli["data"][i][1]))
            print("Alamat : ",(pembeli["data"][i][2]))
            print("Email  : ",(pembeli["data"][i][3]))
            print("----------------------------------------------------")

        y = int(input("Hapus indeks ke : "))
        del pembeli["data"][y]
        print("----------------------------------------------------")
        print("               Data berhasil dihapus                ")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")
        admin()

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        time.sleep(2)
        delete()

    except IndexError:
        print("----------------------------------------------------")
        print("          Data yang anda inginkan tidak ada         ")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")
        admin()

def partisiAsc(data, depan, belakang):
    i = (depan-1)
    pivot=data[belakang]
    for j in range(depan, belakang):
        if data[j] <= pivot:
            i = i+1
            data[i], data[j] = data[j], data[i]
    data[i+1], data[belakang] = data[belakang], data[i+1]
    return (i+1)

def quickSortAsc(data, depan, belakang):
    if len(data) == 1:
        return data
    if depan < belakang:
        pa = partisiAsc(data, depan, belakang)
        quickSortAsc(data, depan, pa-1)
        quickSortAsc(data, pa+1, belakang)
        
def partisiDesc(data, depan, belakang):
    i = (depan-1)
    pivot = data[belakang]
    for j in range(depan, belakang):
        if data[j] >= pivot:
            i = i+1
            data[i], data[j] = data[j], data[i]
    data[i+1], data[belakang] = data[belakang], data[i+1]
    return (i+1)

def quickSortDesc(data, depan, belakang):
    if len(data) == 1:
        return data
    if depan < belakang:
        pd = partisiDesc(data, depan, belakang)
        quickSortDesc(data, depan, pd-1)
        quickSortDesc(data, pd+1, belakang)

def menu():
    try:
        reset()
        print("                    Menu Minuman                    ")
        print("----------------------------------------------------")
        print("1. Teh (Es/Hangat)        : Rp.3000")
        print("2. Jeruk (Es/Hangat)      : Rp.4000")
        print("3. Aneka Jus              : Rp.15000")
        print("4. Es Kelapa              : Rp.5000")
        print("5. Es Campur              : Rp.12000")
        print("6. Es Dawet               : Rp.7000")
        print("7. Air Putih (Es/Hangat)  : (Free)")
        print("8. Cari")
        print("9. Hapus Pesanan")
        print("10.Bayar")
        print("11.Log out")
        print("\nKeterangan:")
        print("!!! Jika anda Log out list pesanan akan dihapus !!!\n")

        print("----------------------------------------------------")
        print("                    List Pesanan                    ")
        print("----------------------------------------------------")

        n = len(listM)
        quickSortAsc(listM, 0, n-1)
        i=0
        for pesanan in listM:
            print ("[",i,"]",pesanan)
            i=i+1

        print("\n----------------------------------------------------")
        print("Total Harga   : Rp.", sum(listH))
        print("----------------------------------------------------")

        pilih = int(input("Pilih : "))
        print("----------------------------------------------------")
        if (pilih == 1):
            teh()
        elif (pilih == 2):
            jeruk()
        elif (pilih == 3):
            jus()
        elif (pilih == 4):
            kelapa()
        elif (pilih == 5):
            campur()
        elif (pilih == 6):
            dawet()
        elif (pilih == 7):
            air()
        elif (pilih == 8):
            try:
                def linearSearch(array,n,x):
                    for i in range(0,n):
                        if(array[i] == x):
                            return i
                    return -1

                x = input("Masukkan data yang di cari: ")
                n = len(listM)

                for i in range(n):
                    result = linearSearch(listM, n, x)
                    if result != -1:
                        print(f"\nData berada pada list ke-{result}")
                        break
                if result == -1:
                    print("\nNama pesanan tidak ditemukan!!")

                print("----------------------------------------------------")
                input("              < Kembali: Tekan Enter >              ")
                menu()

            except UnboundLocalError:
                print("\n----------------------------------------------------")
                print("           Belum ada menu yang di pesan!!           ")
                print("----------------------------------------------------")
                input("              < Kembali: Tekan Enter >              ")
                menu()
                
        
        elif (pilih == 9):
            hapus()
        elif (pilih == 10):
            bayar(0,0)
        elif (pilih == 11):
            menu_awal()
        else:
            print("\nError: Masukkan angka 1 sampai 11 !!!")
            print("----------------------------------------------------")
            time.sleep(2)
            menu()
    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        time.sleep(2)
        menu()

def teh():
    try:
        banyak=int(input("Berapa banyak teh: "))
        print("1. Es\n2. Hangat\n")
        for i in range(banyak):
            pilih = int(input("Pilih: "))
            if (pilih==1):
                listM.append('Es Teh')
                listH.append(3000)
            elif (pilih==2):
                listM.append("Teh Hangat")
                listH.append(3000)
            else:
                print("\nError: Masukkan angka 1 sampai 2 !!!")
                print("----------------------------------------------------")
                time.sleep(2)
                teh()
        menu()
    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        time.sleep(2)
        teh()

def jeruk():
    try:
        banyak=int(input("Berapa banyak jeruk: "))
        print("1. Es\n2. Hangat\n")
        for i in range(banyak):
            pilih = int(input("Pilih: "))
            if (pilih==1):
                listM.append('Es Jeruk')
                listH.append(4000)
            elif (pilih==2):
                listM.append("Jeruk Hangat")
                listH.append(4000)
            else:
                print("\nError: Masukkan angka 1 sampai 2 !!!")
                print("----------------------------------------------------")
                time.sleep(2)
                jeruk()
        menu()
    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        time.sleep(2)
        jeruk()

def jus():
    try:
        banyak=int(input("Berapa banyak Jus: "))
        print("1. Mangga\n2. Alpukat\n3. Buah naga")
        for i in range(banyak):
            pilih = int(input("Pilih: "))
            if (pilih==1):
                listM.append('Jus Mangga')
                listH.append(15000)
            elif (pilih==2):
                listM.append("Jus Alpukat")
                listH.append(15000)
            elif (pilih==3):
                listM.append("Jus Buah Naga")
                listH.append(15000)
            else:
                print("\nError: Masukkan angka 1 sampai 3 !!!")
                print("----------------------------------------------------")
                time.sleep(2)
                jus()
        menu()
    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        time.sleep(2)
        jus()

def kelapa():
    try:
        banyak=int(input("Berapa banyak Es Kelapa: "))
        for i in range(banyak):
            listM.append('Es Kelapa')
            listH.append(5000)
        menu()
    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        time.sleep(2)
        kelapa()

def campur():
    try:
        banyak=int(input("Berapa banyak Es Campur: "))
        for i in range(banyak):
            listM.append('Es Campur')
            listH.append(12000)
        menu()
    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        time.sleep(2)
        campur()

def dawet():
    try:
        banyak=int(input("Berapa banyak Es Dawet: "))
        for i in range(banyak):
            listM.append('Es Dawet')
            listH.append(7000)
        menu()
    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        time.sleep(2)
        dawet()
    
def air():
    try:
        banyak=int(input("Berapa banyak Air Putih: "))
        print("1. Es\n2. Hangat\n")
        for i in range(banyak):
            pilih = int(input("Pilih: "))
            if (pilih==1):
                listM.append('Air Es')
            elif (pilih==2):
                listM.append("Air hangat")
            else:
                print("\nError: Masukkan angka 1 sampai 2 !!!")
                print("----------------------------------------------------")
                time.sleep(2)
                air()
        menu()
    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        time.sleep(2)
        air()

def hapus():
    try:
        hapus=int(input("Hapus Pesanan ke: "))
        del listM[hapus]
        print("\n----------------------------------------------------")
        print("              Pesanan telah di hapus!!              ")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")
        menu()
    except ValueError:
        print("\nError: Masukkan angka !!!                         ")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")
        menu()
    except IndexError:
        print("\nError: Tidak ada menu pada Indeks tersebut!!!     ")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")
        menu()

def bayar(uang,x):
    try:
        reset()
        print("                    Menu Minuman                    ")
        print("----------------------------------------------------")
        print("1. Teh (Es/Hangat)        : Rp.3000")
        print("2. Jeruk (Es/Hangat)      : Rp.4000")
        print("3. Aneka Jus              : Rp.15000")
        print("4. Es Kelapa              : Rp.5000")
        print("5. Es Campur              : Rp.12000")
        print("6. Es Dawet               : Rp.7000")
        print("7. Air Putih (Es/Hangat)  : (Free)")
        print("8. Cari")
        print("9. Hapus Pesanan")
        print("10.Bayar")
        print("11.Log out")
        print("\nKeterangan:")
        print("!!! Jika anda Log out list pesanan akan dihapus !!!\n")

        print("----------------------------------------------------")
        print("                    List Pesanan                    ")
        print("----------------------------------------------------")

        n = len(listM)
        quickSortAsc(listM, 0, n-1)
        i=0
        for pesanan in listM:
            print ("[",i,"]",pesanan)
            i=i+1

        print("\n----------------------------------------------------")
        print("Total Harga   : Rp.", sum(listH))
        print("----------------------------------------------------")

        x=sum(listH)
        uang=int(input("Bayar         : Rp. "))
        total=uang-x
        if total>=0:
            print("Kembalian     : Rp.",uang,"-",sum(listH))
            print("              : Rp.",total)
            print("----------------------------------------------------")
            print("            Terima Kasih, Datang Kembali            ")
            print("----------------------------------------------------")
            input("              < Log out: Tekan Enter >              ")
            menu_awal()

        else:
            print("\nError: Uang anda kurang, Coba lagi!!")
            print("----------------------------------------------------")
            time.sleep(2)
            bayar(0,0)

        return total

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        time.sleep(2)
        bayar(uang,x)

def keluar():
    exit(0)

while True:
    menu_awal()