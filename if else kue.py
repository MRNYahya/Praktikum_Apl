# Materi Percabangan
import os 

def reset():
    os.system('cls' if os.name == 'nt' else 'clear')

reset()
print("")
print("==== Selamat datang di Toko Kue kang Sule ====")
print("")
print("================ Daftar Menu ================= ")
print("")
print("1. Kue Keju: 6000/pcs\n  -Beli 4-15 kue mendapatkan diskon 7%\n  -Beli 16-25 kue mendapatkan diskon 12%")
print("   (Ready Stock 25/hari)")
print("")
print("2. Kue Coklat: 3500/pcs\n  -Beli 5-20 kue mendapatkan diskon 10%\n  -Beli 21-35 kue mendapatkan diskon 15%")
print("   (Ready Stock 35/hari)")
print("")
print("===============================================")
print("")
print("Ket:\n-tekan 1 untuk keju\n-tekan 2 untuk coklat")
print("")
menu = int(input("Pilih rasa keju/coklat: "))
print("")


if (menu == 1):
    harga = 6000
    jumlah = (int(input("Pesan berapa kue keju: ")))
    total = harga * jumlah
    if (4 <= jumlah <= 15):
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

if (menu == 2):
    harga = 3500
    jumlah = (int(input("Pesan berapa kue coklat: ")))
    total = harga * jumlah
    if (5 <= jumlah <= 20):
        diskon = total * 10 / 100
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
        
    elif (21 <= jumlah <= 35):
        diskon = total * 15 / 100
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