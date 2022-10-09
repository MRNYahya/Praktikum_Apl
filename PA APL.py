import pandas as pd
import csv
import datetime
import os
import matplotlib.pyplot as plt
import numpy as np

atasan_pria = ["Kaos","Kemeja","Jaket","Hoodie","Sweater"]
harga_atasanpria = [20000,40000,75000,50000,80000]

bawahan_pria = ["Formal","Chino","Cargo","Jeans"]
harga_bawahanpria = [60000,80000,70000,75000]

sepatu_pria = ["Sneakers","Slip on"]
harga_sepatupria = [40000,63000]

aksesoris_pria = ["Topi","Ikat Pinggang","Sarung Tangan","Scarf","Dasi"]
harga_aksesorispria = [7500,15000,30000,37000,30000]

atasan_wanita = ["Kemeja","Kaos","Blouse","Tank Top","Blazer","Cardigan","Sweater","Hoodie"]
harga_atasanwanita = [42000,24000,34000,15000,65000,40000,80000,52000]

bawahan_wanita = ["Jeans","Legging","Flare Pants","A-line Skirt","Rok Semi skirt"]
harga_bawahanwanita = [170000,50000,70000,90000,150000]

sepatu_wanita = ["Sneakers","Boots","Heels"]
harga_sepatuwanita = [210000,200000,240000]

aksesoris_wanita = ["Kain Hijab","Kacamata","Anting","Gelang","Kalung","Topi"]
harga_aksesoriswanita = [35000,42000,9000,14000,80000,7500]



def grafik():
    labels = ['Baju', 'Celana', 'Sepatu', 'Aksesoris']

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, penjualan_pria, width, label='Pria')
    rects2 = ax.bar(x + width / 2, penjualan_wanita, width, label='Wanita')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Penjualan')
    ax.set_title('Grafik Penjualan')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()

def isidata(nama,umur,alamat,email):
    riwayat.append(nama)
    riwayat.append(umur)
    riwayat.append(alamat)
    riwayat.append(email)
    m = open('DataCustomer.csv', 'a', newline='')
    w = csv.writer(m)
    w.writerow(riwayat)

def datapembelian(Nama,product,Jumlahbarang,Harga,Waktubeli):
        pembelian.append(Nama)
        pembelian.append(product)
        pembelian.append(Jumlahbarang)
        pembelian.append(Harga)
        pembelian.append(Waktu)
        m = open('DataPembelian.csv', 'a', newline='')
        w = csv.writer(m)
        w.writerow(pembelian)
        pembelian.clear()


def pembayaran():
    print("                      Keranjang Belanja                      ")
    for i in range(len(keranjang_belanja["data"])):
        n = len(keranjang_belanja["data"])
        quickSortAsc(keranjang_belanja["data"], 0, n - 1)
        print("Produk      : ", (keranjang_belanja["data"][i][0]))
        print("Jumlah      : ", (keranjang_belanja["data"][i][1]))
        print("Total Harga : ", (keranjang_belanja["data"][i][2]))
        print("\n-----------------------------------------------------")
    print("Total Harga   : Rp.", sum(total_harga))
    print("------------------------------------------------------")


def checkout():
    pembayaran()
    harga = sum(total_harga)
    bayar = int(input("Masukkan Jumlah Pembayaran: "))
    if (bayar >= harga):
        print("------------------------------------------------------")
        print("Jumlah Pembayaran : Rp.",bayar)
        print("Total Harga       : Rp.",harga)
        print("Kembalian         : Rp.",bayar-harga)
        print("                Terima Kasih Telah Bebelanja          ")

def fashion():
    try:
        print("----------------------------------------------------")
        print("                      Fashion                       ")
        print("----------------------------------------------------")
        print("1. Pria")
        print("2. Wanita")
        print("3. Keranjang Belanja")
        print("4. Check-Out")
        gender = int(input("\nPilih: "))

        if (gender == 1):
            menupria()
        elif (gender == 2):
            menuwanita()
        elif (gender == 3):
            pembayaran()
        elif (gender == 4):
            checkout()
        else:
            print("\nError: Masukkan angka 1 sampai 2 !!!")
            print("----------------------------------------------------")
            input("              < Kembali: Tekan Enter >              ")

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")

def menupria():
    try:
        print("----------------------------------------------------")
        print("                        Pria                        ")
        print("----------------------------------------------------")
        print("1. Baju")
        print("2. Celana")
        print("3. Sepatu")
        print("4. Aksesoris")
        pilih = int(input("\nPilih: "))

        if (pilih == 1):
            baju_pria()
        elif (pilih == 2):
            celanapria()
        elif (pilih == 3):
            sepatupria()
        elif (pilih == 4):
            aksesorispria()
        else:
            print("\nError: Masukkan angka 1 sampai 3 !!!")
            print("----------------------------------------------------")
            input("              < Kembali: Tekan Enter >              ")

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")

def menuwanita():
    try:
        print("----------------------------------------------------")
        print("                        Wanita                      ")
        print("----------------------------------------------------")
        print("1. Baju")
        print("2. Celana")
        print("3. Sepatu")
        print("4. Aksesoris")
        pilih = int(input("\nPilih: "))

        if (pilih == 1):
            baju_wanita()
        elif (pilih == 2):
            celana_wanita()
        elif (pilih == 3):
            sepatuwanita()
        elif (pilih == 4):
            aksesoriswanita()
        else:
            print("\nError: Masukkan angka 1 sampai 4 !!!")
            print("----------------------------------------------------")
            input("              < Kembali: Tekan Enter >              ")

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")

def baju_pria():
    BajuPria = 0
    try:
        print("----------------------------------------------------")
        print("                     Baju Pria                      ")
        print("----------------------------------------------------")
        print("Pilih Salah Satu")
        for i in range(len(atasan_pria)):
            print([i + 1], atasan_pria[i], '\t''\t','\t', '|', "Rp.",harga_atasanpria[i], '|')
        pilih = int(input("\nPilih: "))
        if (pilih == 1):
            Produk = atasan_pria[0] + " Pria"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_atasanpria[0]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            BajuPria += Jumlah
            print("Total Harga adalah :Rp.",Harga)
            print("----------------------------------------------------")


        if (pilih==2):
            Produk = atasan_pria[1] + " Pria"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_atasanpria[1]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            BajuPria += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

        if (pilih==3):
            Produk = atasan_pria[2] + " Pria"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_atasanpria[2]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            BajuPria += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

        if (pilih==4):
            Produk = atasan_pria[3] + " Pria"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_atasanpria[3]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            BajuPria += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

        if (pilih==5):
            Produk = atasan_pria[4] + " Pria"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_atasanpria[4]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            BajuPria += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")
    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")
    penjualan_pria[0] = BajuPria

def celanapria():
    CelanaPria = 0
    try:
        print("----------------------------------------------------")
        print("                   Celana Pria                      ")
        print("----------------------------------------------------")
        print("Pilih Salah Satu")
        for i in range(len(bawahan_pria)):
            print([i + 1], bawahan_pria[i], '\t''\t','\t', '|', "Rp.",harga_bawahanpria[i], '|')
        pilih = int(input("\nPilih: "))
        if (pilih == 1):
            Produk = bawahan_pria[0] + " Pria"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_bawahanpria[0]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            CelanaPria += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

        if (pilih == 2):
            Produk = bawahan_pria[1] + " Pria"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_bawahanpria[1]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            CelanaPria += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

        if (pilih == 3):
            Produk = bawahan_pria[2] + " Pria"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_bawahanpria[2]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            CelanaPria += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

        if (pilih == 4):
            Produk = bawahan_pria[3] + " Pria"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_bawahanpria[3]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            CelanaPria += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")
    penjualan_pria[1] = CelanaPria

def sepatupria():
    SepatuPria = 0
    try:
        print("----------------------------------------------------")
        print("                   Sepatu Pria                      ")
        print("----------------------------------------------------")
        print("Pilih Salah Satu")
        for i in range(len(sepatu_pria)):
            print([i + 1], sepatu_pria[i], '\t''\t','\t', '|', "Rp.",harga_sepatupria[i], '|')
        pilih = int(input("\nPilih: "))
        if (pilih == 1):
            Produk = sepatu_pria[0] + " Pria"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_sepatupria[0]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            SepatuPria += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

        if (pilih == 2):
            Produk = sepatu_pria[1] + " Pria"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_sepatupria[1]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            SepatuPria += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

        if (pilih == 3):
            Produk = sepatu_pria[2] + " Pria"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_sepatupria[2]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            SepatuPria += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")
    penjualan_pria[2] = SepatuPria

def aksesorispria():
    AksesorisPria = 0
    try:
        print("----------------------------------------------------")
        print("                  Aksesoris Pria                    ")
        print("----------------------------------------------------")
        print("Pilih Salah Satu")
        for i in range(len(aksesoris_pria)):
            print([i + 1], aksesoris_pria[i], '\t''\t', '\t', '|', "Rp.", aksesoris_pria[i], '|')
        pilih = int(input("\nPilih: "))
        if (pilih == 1):
            Produk = aksesoris_pria[0]
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_aksesorispria[0]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            AksesorisPria += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

        if (pilih == 2):
            Produk = aksesoris_pria[1]
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_aksesorispria[1]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            AksesorisPria += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

        if (pilih == 3):
            Produk = aksesoris_pria[2]
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_aksesorispria[2]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            AksesorisPria += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

        if (pilih == 4):
            Produk = aksesoris_pria[3]
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_aksesorispria[3]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            AksesorisPria += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

        if (pilih == 5):
            Produk = aksesoris_pria[3]
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_aksesorispria[3]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            AksesorisPria += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")
    penjualan_pria[3] = AksesorisPria

def baju_wanita():
    BajuWanita = 0
    try:
        print("----------------------------------------------------")
        print("                     Baju Wanita                    ")
        print("----------------------------------------------------")
        print("Pilih Salah Satu")
        for i in range(len(atasan_wanita)):
            print([i + 1], atasan_wanita[i], '\t''\t','\t', '|', "Rp.",harga_atasanwanita[i], '|')
        pilih = int(input("\nPilih: "))
        if (pilih == 1):
            Produk = atasan_wanita[0] + " Wanita"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_atasanwanita[0]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            BajuWanita += Jumlah
            print("Total Harga adalah :Rp.",Harga)
            print("----------------------------------------------------")

        if (pilih == 2):
            Produk = atasan_wanita[1] + " Wanita"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_atasanwanita[1]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            BajuWanita += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

        if (pilih == 3):
            Produk = atasan_wanita[2]
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_atasanwanita[2]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            BajuWanita += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

        if (pilih == 4):
            Produk = atasan_wanita[3] + " Wanita"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_atasanwanita[3]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            BajuWanita += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

        if (pilih == 5):
            Produk = atasan_wanita[4] + " Wanita"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_atasanwanita[4]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            BajuWanita += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

        if (pilih == 6):
            Produk = atasan_wanita[5] + " Wanita"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_atasanwanita[5]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            BajuWanita += Jumlah
            print("Total Harga adalah :Rp.",Harga)
            print("----------------------------------------------------")

        if (pilih == 7):
            Produk = atasan_wanita[6] + " Wanita"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_atasanwanita[6]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            BajuWanita += Jumlah
            print("Total Harga adalah :Rp.",Harga)
            print("----------------------------------------------------")

        if (pilih == 8):
            Produk = atasan_wanita[7] + " Wanita"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_atasanwanita[7]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            BajuWanita += Jumlah
            print("Total Harga adalah :Rp.",Harga)
            print("----------------------------------------------------")
    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")
    penjualan_wanita[0] = BajuWanita

def celana_wanita():
    CelanaWanita = 0
    try:
        print("----------------------------------------------------")
        print("                     Celana Wanita                  ")
        print("----------------------------------------------------")
        print("Pilih Salah Satu")
        for i in range(len(bawahan_wanita)):
            print([i + 1], bawahan_wanita[i], '\t''\t','\t', '|', "Rp.",harga_bawahanwanita[i], '|')
        pilih = int(input("\nPilih: "))
        if (pilih == 1):
            Produk = bawahan_wanita[0] + " Wanita"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_bawahanwanita[0]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            CelanaWanita += Jumlah
            print("Total Harga adalah :Rp.",Harga)
            print("----------------------------------------------------")
        if (pilih == 2):
            Produk = bawahan_wanita[1] + " Wanita"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_bawahanwanita[1]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            CelanaWanita += Jumlah
            print("Total Harga adalah :Rp.",Harga)
            print("----------------------------------------------------")
        if (pilih == 3):
            Produk = bawahan_wanita[2]
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_bawahanwanita[2]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            CelanaWanita += Jumlah
            print("Total Harga adalah :Rp.",Harga)
            print("----------------------------------------------------")
        if (pilih == 4):
            Produk = bawahan_wanita[3]
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_bawahanwanita[3]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            CelanaWanita += Jumlah
            print("Total Harga adalah :Rp.",Harga)
            print("----------------------------------------------------")
        if (pilih == 5):
            Produk = bawahan_wanita[4]
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_bawahanwanita[4]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            CelanaWanita += Jumlah
            print("Total Harga adalah :Rp.",Harga)
            print("----------------------------------------------------")


    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")

def sepatuwanita():
    SepatuWanita = 0
    try:
        print("----------------------------------------------------")
        print("                     Sepatu Wanita                  ")
        print("----------------------------------------------------")
        print("Pilih Salah Satu")
        for i in range(len(sepatu_wanita)):
            print([i + 1], sepatu_wanita[i], '\t''\t','\t', '|', "Rp.",harga_sepatuwanita[i], '|')
        pilih = int(input("\nPilih: "))
        if (pilih == 1):
            Produk = sepatu_wanita[0] + "Wanita"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_sepatuwanitaa[0]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            SepatuWanita += Jumlah
            print("Total Harga adalah :Rp.",Harga)
            print("----------------------------------------------------")
        if (pilih == 2):
            Produk = sepatu_wanita[1] + "Wanita"
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_sepatuwanitaa[1]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            SepatuWanita += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")

        if (pilih == 3):
            Produk = sepatu_wanita[2]
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_aksesoriswanita[2]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            SepatuWanita += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")


    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")

    penjualan_wanita[2] = SepatuWanita

def aksesoriswanita():
    AksesorisWanita = 0
    try:
        print("----------------------------------------------------")
        print("                     Aksesoris Wanita               ")
        print("----------------------------------------------------")
        print("Pilih Salah Satu")
        for i in range(len(aksesoris_wanita)):
            print([i + 1], aksesoris_wanita[i], '\t''\t','\t', '|', "Rp.",harga_aksesoriswanita[i], '|')
        pilih = int(input("\nPilih: "))
        if (pilih == 1):
            Produk = aksesoris_wanita[0]
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_aksesoriswanita[0]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            AksesorisWanita += Jumlah
            print("Total Harga adalah :Rp.",Harga)
            print("----------------------------------------------------")
        if (pilih == 2):
            Produk = aksesoris_wanita[1]
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_aksesoriswanita[1]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            AksesorisWanita += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")
        if (pilih == 3):
            Produk = aksesoris_wanita[2]
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_aksesoriswanita[2]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            AksesorisWanita += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")
        if (pilih == 4):
            Produk = aksesoris_wanita[3]
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_aksesoriswanita[3]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            AksesorisWanita += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")
        if (pilih == 5):
            Produk = aksesoris_wanita[4]
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_aksesoriswanita[4]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            AksesorisWanita += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")
        if (pilih == 6):
            Produk = aksesoris_wanita[5]
            Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
            Harga = Jumlah * harga_aksesoriswanita[5]
            total_harga.append(Harga)
            keranjang_belanja["data"].append([Produk, Jumlah, Harga])
            datapembelian(name, Produk, Jumlah, Harga, Waktu)
            AksesorisWanita += Jumlah
            print("Total Harga adalah :Rp.", Harga)
            print("----------------------------------------------------")


    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")

    penjualan_wanita[3] = AksesorisWanita

def admin():
    print("----------------------------------------------------")
    print("                     Menu Admin                     ")
    print("----------------------------------------------------")
    print("1. Lihat Data Pengunjung                            ")
    print("2. Lihat Riwayat Pembelian                          ")
    print("3. Update Data Barang                               ")
    print("4. Hapus Data Barang                                ")
    print("5. Grafik Penjualan                                 ")
    pilih = int(input("Pilih Salah Satu: "))
    if (pilih == 1):
        datapengunjung()
    elif (pilih == 2):
        riwayatpembelian()
    elif (pilih == 3):
        updatebarang()
    elif (pilih == 4):
        hapusbarang()
    elif (pilih == 5):
        grafik()



def datapengunjung():
    df = pd.read_csv("DataCustomer.csv")
    print(df)


def riwayatpembelian():
    df = pd.read_csv("DataPembelian.csv")
    print(df)

def updatebarang():
    try:
        print("----------------------------------------------------")
        print("                    Update Barang                   ")
        print("----------------------------------------------------")
        a = int(input("[1]Pria\n[2]Wanita\nPilih: "))
        print("----------------------------------------------------")
        if (a == 1):
            b= int(input("[1]Baju\n[2]Celana\n[3]Sepatu\n[4]Aksesoris\nPilih: "))
            print("----------------------------------------------------")
            if (b==1):
                for i in range(len(atasan_pria)):
                    print([i], atasan_pria[i], '\t''\t', '\t', '|', "Rp.", harga_atasanpria[i], '|')
                print("----------------------------------------------------")
                y = int(input("Mengubah data indeks ke : "))
                NamaBarang = input("Masukkan Nama Barang: ")
                HargaBarang = input("Masukkan Harga Barang: ")
                atasan_pria[y] = NamaBarang
                harga_atasanpria[y] = HargaBarang
                print("Barang Telah Diupdate")
            if (b==2):
                for i in range(len(bawahan_pria)):
                    print([i], bawahan_pria[i], '\t''\t', '\t', '|', "Rp.", harga_bawahanwanita[i], '|')
                print("----------------------------------------------------")
                y = int(input("Mengubah data indeks ke : "))
                NamaBarang = input("Masukkan Nama Barang: ")
                HargaBarang = input("Masukkan Harga Barang: ")
                bawahan_pria[y] = NamaBarang
                harga_bawahanpria[y] = HargaBarang
                print("Barang Telah Diupdate")

            if (b==3):
                for i in range(len(sepatu_pria)):
                    print([i], sepatu_pria[i], '\t''\t', '\t', '|', "Rp.", harga_sepatupria[i], '|')
                print("----------------------------------------------------")
                y = int(input("Mengubah data indeks ke : "))
                NamaBarang = input("Masukkan Nama Barang: ")
                HargaBarang = input("Masukkan Harga Barang: ")
                sepatu_pria[y] = NamaBarang
                harga_sepatupria[y] = HargaBarang
                print("Barang Telah Diupdate")

            if (b==4):
                for i in range(len(aksesoris_pria)):
                    print([i], aksesoris_pria[i], '\t''\t', '\t', '|', "Rp.", harga_aksesorispria[i], '|')
                print("----------------------------------------------------")
                y = int(input("Mengubah data indeks ke : "))
                NamaBarang = input("Masukkan Nama Barang: ")
                HargaBarang = input("Masukkan Harga Barang: ")
                aksesoris_pria[y] = NamaBarang
                harga_aksesorispria[y] = HargaBarang
                print("Barang Telah Diupdate")

        if (a==2):
            b = int(input("[1]Baju\n[2]Celana\n[3]Sepatu\n[4]Aksesoris\nPilih: "))
            print("----------------------------------------------------")
            if (b == 1):
                for i in range(len(atasan_pria)):
                    print([i], atasan_pria[i], '\t''\t', '\t', '|', "Rp.", harga_atasanpria[i], '|')
                print("----------------------------------------------------")
                y = int(input("Mengubah data indeks ke : "))
                NamaBarang = input("Masukkan Nama Barang: ")
                HargaBarang = input("Masukkan Harga Barang: ")
                atasan_pria[y] = NamaBarang
                harga_atasanpria[y] = HargaBarang
                print("Barang Telah Diupdate")
            if (b == 2):
                for i in range(len(bawahan_wanita)):
                    print([i], bawahan_pria[i], '\t''\t', '\t', '|', "Rp.", harga_bawahanwanita[i], '|')
                print("----------------------------------------------------")
                y = int(input("Mengubah data indeks ke : "))
                NamaBarang = input("Masukkan Nama Barang: ")
                HargaBarang = input("Masukkan Harga Barang: ")
                bawahan_wanita[y] = NamaBarang
                harga_bawahanwanita[y] = HargaBarang
                print("Barang Telah Diupdate")

            if (b == 3):
                for i in range(len(sepatu_wanita)):
                    print([i], sepatu_wanita[i], '\t''\t', '\t', '|', "Rp.", harga_sepatuwanita[i], '|')
                print("----------------------------------------------------")
                y = int(input("Mengubah data indeks ke : "))
                NamaBarang = input("Masukkan Nama Barang: ")
                HargaBarang = input("Masukkan Harga Barang: ")
                sepatu_wanita[y] = NamaBarang
                harga_sepatuwanita[y] = HargaBarang
                print("Barang Telah Diupdate")

            if (b == 4):
                for i in range(len(aksesoris_wanita)):
                    print([i], aksesoris_wanita[i], '\t''\t', '\t', '|', "Rp.", harga_aksesoriswanita[i], '|')
                print("----------------------------------------------------")
                y = int(input("Mengubah data indeks ke : "))
                NamaBarang = input("Masukkan Nama Barang: ")
                HargaBarang = input("Masukkan Harga Barang: ")
                aksesoris_wanita[y] = NamaBarang
                harga_aksesoriswanita[y] = HargaBarang
                print("Barang Telah Diupdate")

    except ValueError:
        print("Input Salah!!")

def hapusbarang():
    try:
        print("----------------------------------------------------")
        print("                    Hapus Barang                    ")
        print("----------------------------------------------------")
        a = int(input("[1]Pria\n[2]Wanita\nPilih: "))
        print("----------------------------------------------------")
        if (a == 1):
            b= int(input("[1]Baju\n[2]Celana\n[3]Sepatu\n[4]Aksesoris\nPilih: "))
            print("----------------------------------------------------")
            if (b==1):
                df1 = pd.ope
            if (b==2):
                for i in range(len(atasan_pria)):
                    print([i], bawahan_pria[i], '\t''\t', '\t', '|', "Rp.", harga_bawahanpria[i], '|')
                print("----------------------------------------------------")
                y = int(input("Hapus data indeks ke : "))
                del bawahan_pria[y]
                del harga_bawahanpria[y]
                print("Barang Telah Dihapus")
            if (b==3):
                for i in range(len(sepatu_pria)):
                    print([i], sepatu_pria[i], '\t''\t', '\t', '|', "Rp.", harga_sepatupria[i], '|')
                print("----------------------------------------------------")
                y = int(input("Hapus data indeks ke : "))
                del sepatu_pria[y]
                del harga_sepatupria[y]
                print("Barang Telah Dihapus")
            if (b==4):
                for i in range(len(aksesoris_pria)):
                    print([i], aksesoris_pria[i], '\t''\t', '\t', '|', "Rp.", harga_aksesorispria[i], '|')
                print("----------------------------------------------------")
                y = int(input("Hapus data indeks ke : "))
                del aksesoris_pria[y]
                del harga_aksesorispria[y]
                print("Barang Telah Dihapus")
        if (a==2):
            b = int(input("[1]Baju\n[2]Celana\n[3]Sepatu\n[4]Aksesoris\nPilih: "))
            print("----------------------------------------------------")
            if (b==1):
                for i in range(len(atasan_wanita)):
                    print([i], atasan_wanita[i], '\t''\t', '\t', '|', "Rp.", harga_atasanwanita[i], '|')
                print("----------------------------------------------------")
                y = int(input("Hapus data indeks ke : "))
                del atasan_wanita[y]
                del harga_atasanwanita[y]
                print("Barang Telah Dihapus")
            if (b==2):
                for i in range(len(bawahan_wanita)):
                    print([i], bawahan_wanita[i], '\t''\t', '\t', '|', "Rp.", harga_bawahanwanita[i], '|')
                print("----------------------------------------------------")
                y = int(input("Hapus data indeks ke : "))
                del bawahan_wanita[y]
                del harga_bawahanwanita[y]
                print("Barang Telah Dihapus")

            if (b==3):
                for i in range(len(sepatu_wanita)):
                    print([i], sepatu_wanita[i], '\t''\t', '\t', '|', "Rp.", harga_sepatuwanita[i], '|')
                print("----------------------------------------------------")
                y = int(input("Hapus data indeks ke : "))
                del sepatu_wanita[y]
                del harga_sepatuwanita[y]
                print("Barang Telah Dihapus")

            if (b==4):
                for i in range(len(aksesoris_wanita)):
                    print([i], aksesoris_wanita[i], '\t''\t', '\t', '|', "Rp.", harga_aksesoriswanita[i], '|')
                print("----------------------------------------------------")
                y = int(input("Hapus data indeks ke : "))
                del aksesoris_wanita[y]
                del harga_aksesoriswanita[y]
                print("Barang Telah Dihapus")


    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        input("              < Kembali: Tekan Enter >              ")




def menu_awal():
    try:
        print("           Anda ingin masuk sebagai apa?            ")
        print("----------------------------------------------------")
        print("1. Customer                                         ")
        print("2. Admin                                            ")
        print("3. Keluar                                           ")
        print("----------------------------------------------------")

    except ValueError:
        print("Salah")

def partisiAsc(data, depan, belakang):
    i = (depan - 1)
    pivot = data[belakang]
    for j in range(depan, belakang):
        if data[j] <= pivot:
            i = i + 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[belakang] = data[belakang], data[i + 1]
    return (i + 1)


def quickSortAsc(data, depan, belakang):
    if len(data) == 1:
        return data
    if depan < belakang:
        pa = partisiAsc(data, depan, belakang)
        quickSortAsc(data, depan, pa - 1)
        quickSortAsc(data, pa + 1, belakang)

riwayat = []
pembelian = []
keranjang_belanja = {"data": []}
total_harga = []
penjualan_pria = [0,0,0,0]
penjualan_wanita = [0,0,0,0]
Start = True
while (Start):
    Waktu = datetime.datetime.now()
    jam = Waktu.hour
    if jam >= 5 and jam <= 11:
        print("                   Selamat Pagi                     ")
    elif jam > 11 and jam <= 14:
        print("                   Selamat Siang                    ")
    elif jam > 14 and jam <= 18:
        print("                   Selamat Sore                     ")
    elif jam > 18 or jam < 5:
        print("                   Selamat Malam                    ")
    menu_awal()
    Login = int(input("Pilih : "))
    Start2 = True
    if (Login == 1):
        Start = False
        print("           Masukkan Data Diri           ")
        name = str(input("Nama   : "))
        age = str(input("Umur   : "))
        alamat = str(input("Alamat : "))
        email = str(input("Email  : "))
        isidata(name, age, alamat, email)
        while (Start2):
            fashion()
            try:
                a = str(input("Ingin Melanjutkan (y/n): "))
                if a == 'n' or a == 'N' :
                    Start2 = False
                    checkout()
                    Start3 = True
                    while (Start3):
                        a = str(input("Ingin Melanjutkan (y/n): "))
                        if a == 'y' or a == 'Y':
                            keranjang_belanja["data"].clear()
                            total_harga.clear()
                            Start3 = False
                            Start2 = True
                        if a == 'N' or a == 'n':
                            keranjang_belanja["data"].clear()
                            total_harga.clear()
                            Start3 = False
                            Start2 = False
                            Start = True

            except ValueError:
                print("Masukkan Huruf Y/N!!")

    if (Login == 2):
        Start = False
        Start2 = False
        x = 3
        while x > 0:
            print("----------------------------------------------------")
            print("          Masukkan Username dan Password            ")
            print("----------------------------------------------------")
            User = str(input("Username : "))
            Password = str(input("Password : "))

            if (User == "admin" and Password == "123"):
                print("----------------------------------------------------")
                print("                 Berhasil Masuk !!!                 ")
                print("----------------------------------------------------")
                input("                   < Tekan Enter >                  ")
                admin()
                try:
                    a = str(input("Ingin Melanjutkan (y/n): "))
                    if a == 'n' or a == 'N':
                        x = -1
                        Start = True

                    if a == 'Y' or a == 'y':
                        admin()

                except ValueError:
                    print("Masukkan Huruf Y/N!!")


            else:
                x -= 1
                if (User == "admin" and Password != "123"):
                    print("\nError: Password yang anda masukkan salah !!!\nKesempatan :[", x, "]")
                    print("----------------------------------------------------")
                    input("              < Kembali: Tekan Enter >              ")

                elif (User != "admin" and Password == "123"):
                    print("\nError: Username yang dimasukkan tidak terdata !!!\nKesempatan :[", x, "]")
                    print("----------------------------------------------------")
                    input("              < Kembali: Tekan Enter >              ")

                else:
                    print("\nError: Username yang dimasukkan tidak terdata !!! \nKesempatan :[", x, "]")
                    print("----------------------------------------------------")
                    input("              < Kembali: Tekan Enter >              ")

                if x == 0:
                    print("            Kesempatan Anda telah habis             ")
                    print("               Kembali Ke Menu Awal?                 ")
                    print("----------------------------------------------------")
                    input("              < Kembali: Tekan Enter >              ")
                    Start = True
















