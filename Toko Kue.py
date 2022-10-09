import os
import time

def reset():
    os.system('cls' if os.name == 'nt' else 'clear')

def menuawal():
    try:
        reset()
        kuecoklat=35
        kuekeju=25
        if kuecoklat <= 0:
            print("Kue Coklat Habis")
            exit(0)
        elif kuekeju <= 0:
            print("Kue keju habis")
            exit(0)
        

        print("")
        print("==== Selamat datang di Toko Kue Yahya ====\n")
        print("================ Daftar Menu =================\n")
        print("Kue Keju: 6000/pcs\n  -Beli 4-15 kue mendapatkan diskon 7%\n  -Beli 16-25 kue mendapatkan diskon 12%")
        print("   (Ready Stock 25/hari)\n")
        print("Kue Coklat: 3500/pcs\n  -Beli 5-20 kue mendapatkan diskon 10%\n  -Beli 21-35 kue mendapatkan diskon 15%")
        print("   (Ready Stock 35/hari)\n")
        print("===============================================\n")
        print("1. keju\n2. coklat\n")
        menu = int(input("Pilih rasa: "))
        print("")
        if menu==1:
            keju()
        elif menu==2:
            coklat()
        elif menu==3:
            keluar()

    except ValueError:
        print("Masukkan angka!!")
    

def keju():
    try:
        print("===============================================\n")
        harga = 6000
        jumlah = (int(input("Pesan berapa kue keju: ")))
        total = harga * jumlah
        if (1<= jumlah <= 3):
            print("Harga           : Rp.", int(total))
            uangku = int(input("Uang Anda       : Rp. "))
            harga_total = uangku - total
            if (total <= uangku):
                print("Kembalian       : Rp.", int(uangku), "- Rp.", int(total))
                print("                : Rp.", int(harga_total))
                print("")
                print("==== Terima Kasih Telah Membeli Produk Kami ====")
            else:
                print("Uang Anda Kurang: Rp.", int(harga_total))

        elif (4 <= jumlah <= 15):
            diskon = total * 7 / 100
            print("Harga           : Rp.", int(total))
            print("Potongan harga  : Rp.", int(diskon))
            harga_total = total - diskon
            print("Total Harga     : Rp.", int(total), "- Rp. ", int(diskon))
            print("                : Rp.",int(harga_total))
            uangku = int(input("Uang Anda       : Rp. "))
            kembalian = uangku - harga_total
            if (harga_total <= uangku):
                print("Kembalian       : Rp.", int(uangku), "- Rp.", int(harga_total))
                print("                : Rp.", int(kembalian))
                print("")
                print("==== Terima Kasih Telah Membeli Produk Kami ====")
            else:
                print("Uang Anda Kurang: Rp.", int(kembalian))
        
        elif (16 <= jumlah <= 25):
            diskon = total * 12 / 100
            print("Harga           : Rp.", int(total))
            print("Potongan harga  : Rp.", int(diskon))
            harga_total = total - diskon
            print("Total Harga     : Rp.", int(total), "- Rp. ", int(diskon))
            print("                : Rp.",int(harga_total))
            uangku = int(input("Uang Anda       : Rp. "))
            kembalian = uangku - harga_total
            if (harga_total <= uangku):
                print("Kembalian       : Rp.", int(uangku), "- Rp.", int(harga_total))
                print("                : Rp.", int(kembalian))
                print("")
                print("==== Terima Kasih Telah Membeli Produk Kami ====")
            else:
                print("Uang Anda Kurang: Rp.", int(kembalian))
        else:
            print("Stok Hanya terbatas 25 Kue/Hari")
            
    except ValueError:
        print("Masukkan angka!!")

while True:
    menuawal()