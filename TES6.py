import pandas as pd
import csv
import datetime
import os
import matplotlib.pyplot as plt
import numpy as np

riwayat = []
pembelian = []
keranjang_belanja = {"data": []}
total_harga = []
penjualan_pria = [0,0,0,0]
penjualan_wanita = [0,0,0,0]
Data = []

def reset():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    elif depan < belakang:
        pa = partisiAsc(data, depan, belakang)
        quickSortAsc(data, depan, pa - 1)
        quickSortAsc(data, pa + 1, belakang)

def datapembelian(Nama, product, Jumlahbarang, Harga, Waktubeli):
    pembelian.append(Nama)
    pembelian.append(product)
    pembelian.append(Jumlahbarang)
    pembelian.append(Harga)
    pembelian.append(Waktu)
    m = open('DataPembelian.csv', 'a', newline='')
    w = csv.writer(m)
    w.writerow(pembelian)
    pembelian.clear()

def isidata(nama,umur,alamat,email):
    riwayat.append(nama)
    riwayat.append(umur)
    riwayat.append(alamat)
    riwayat.append(email)
    m = open('DataCustomer.csv', 'a', newline='')
    w = csv.writer(m)
    w.writerow(riwayat)

def fashion():
    try:
        reset()
        print("----------------------------------------------------")
        print("                      Fashion                       ")
        print("----------------------------------------------------")
        print("[1] Fashion Pria")
        print("[2] Fashion Wanita")
        print("[3] Keranjang Belanja")
        print("[4] Check-Out")
        print("[0] Kembali")
        gender = int(input("\nPilih: "))
        if (gender == 1):
            menupria()
        elif (gender == 2):
            menuwanita()
        elif (gender == 3):
            pembayaran()
        elif (gender == 4):
            checkout()
        elif (gender == 0):
            print("----------------------------------------------------")
            print("              < Kembali: Tekan Enter >              ")
            input("                          ")
        else:
            print("\nError: Masukkan angka yang ada !!!")
            print("----------------------------------------------------")
            print("              < Kembali: Tekan Enter >              ")
            input("                          ")
            fashion()

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                          ")
        fashion()

def admin():
    try:
        reset()
        print("----------------------------------------------------")
        print("                     Menu Admin                     ")
        print("----------------------------------------------------")
        print("[1] Lihat Data Pengunjung                           ")
        print("[2] Lihat Riwayat Pembelian                         ")
        print("[3] Tambah Data Barang                              ")
        print("[4] Update Data Barang                              ")
        print("[5] Hapus Data Barang                               ")
        print("[6] Grafik Penjualan                                ")
        print("[0] Kembali")
        pilih = int(input("\nPilih Salah Satu: "))
        if (pilih == 1):
            datapengunjung()
        elif (pilih == 2):
            riwayatpembelian()
        elif (pilih == 3):
            tambah_barang()
        elif (pilih == 4):
            updatebarang()
        elif (pilih == 5):
            hapusbarang()
        elif (pilih == 6):
            grafik()
        elif (pilih == 0):
            print("----------------------------------------------------")
            print("              < Kembali: Tekan Enter >              ")
            input("                          ")
        else:
            print("\nError: Masukkan angka yang ada !!!")
            print("----------------------------------------------------")
            print("              < Kembali: Tekan Enter >              ")
            input("                            ")
            admin()

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        admin()

def menupria():
    try:
        reset()
        print("----------------------------------------------------")
        print("                        Pria                        ")
        print("----------------------------------------------------")
        print("[1] Baju")
        print("[2] Celana")
        print("[3] Sepatu")
        print("[4] Aksesoris")
        print("[0] Kembali")
        pilih = int(input("\nPilih: "))
        if (pilih == 1):
            baju_pria()
        elif (pilih == 2):
            celanapria()
        elif (pilih == 3):
            sepatupria()
        elif (pilih == 4):
            aksesorispria()
        elif (pilih == 0):
            fashion()
        else:
            print("\nError: Masukkan angka yang ada !!!")
            print("----------------------------------------------------")
            print("              < Kembali: Tekan Enter >              ")
            input("                          ")
            menupria()

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        menupria()

def menuwanita():
    try:
        reset()
        print("----------------------------------------------------")
        print("                        Wanita                      ")
        print("----------------------------------------------------")
        print("[1] Baju")
        print("[2] Celana")
        print("[3] Sepatu")
        print("[4] Aksesoris")
        print("[0] Kembali")
        pilih = int(input("\nPilih: "))
        if (pilih == 1):
            baju_wanita()
        elif (pilih == 2):
            celana_wanita()
        elif (pilih == 3):
            sepatuwanita()
        elif (pilih == 4):
            aksesoriswanita()
        elif (pilih == 0):
            fashion()
        else:
            print("\nError: Masukkan angka yang ada !!!")
            print("----------------------------------------------------")
            print("              < Kembali: Tekan Enter >              ")
            input("                            ")
            menuwanita()

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        menuwanita()

def baju_pria():
    df = pd.read_csv("DataBajuPria.csv")
    BajuPria = 0
    try:
        print("----------------------------------------------------")
        print("                     Baju Pria                      ")
        print("----------------------------------------------------")
        print("Pilih Salah Satu")
        print(df)
        pilih = int(input("\nPilih: "))
        Produk = df["Barang"][pilih]
        Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
        Harga = Jumlah * df["Harga"][pilih]
        total_harga.append(Harga)
        keranjang_belanja["data"].append([Produk, Jumlah, Harga])
        datapembelian(name, Produk, Jumlah, Harga, Waktu)
        BajuPria += Jumlah
        print("Total Harga adalah :Rp.", Harga)
        print("----------------------------------------------------")
    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        baju_pria()
    except KeyError:
        print("\nError: Index yang anda input tidak tersedia !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        baju_pria()
    penjualan_pria[0] = BajuPria

def celanapria():
    df = pd.read_csv("DataCelanaPria.csv")
    CelanaPria = 0
    try:
        print("----------------------------------------------------")
        print("                   Celana Pria                      ")
        print("----------------------------------------------------")
        print("Pilih Salah Satu")
        print(df)
        pilih = int(input("\nPilih: "))
        Produk = df["Barang"][pilih]
        Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
        Harga = Jumlah * df["Harga"][pilih]
        total_harga.append(Harga)
        keranjang_belanja["data"].append([Produk, Jumlah, Harga])
        datapembelian(name, Produk, Jumlah, Harga, Waktu)
        CelanaPria += Jumlah
        print("Total Harga adalah :Rp.", Harga)
        print("----------------------------------------------------")

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        celanapria()
    except KeyError:
        print("\nError: Index yang anda input tidak tersedia !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        celanapria()
    penjualan_pria[1] = CelanaPria

def sepatupria():
    df = pd.read_csv("DataSepatuPria.csv")
    SepatuPria = 0
    try:
        print("----------------------------------------------------")
        print("                   Sepatu Pria                      ")
        print("----------------------------------------------------")
        print("Pilih Salah Satu")
        print(df)
        pilih = int(input("\nPilih: "))
        Produk = df["Barang"][pilih]
        Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
        Harga = Jumlah * df["Harga"][pilih]
        total_harga.append(Harga)
        keranjang_belanja["data"].append([Produk, Jumlah, Harga])
        datapembelian(name, Produk, Jumlah, Harga, Waktu)
        SepatuPria += Jumlah
        print("Total Harga adalah :Rp.", Harga)
        print("----------------------------------------------------")

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                             ")
        sepatupria()
    except KeyError:
        print("\nError: Index yang anda input tidak tersedia !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        sepatupria()
    penjualan_pria[2] = SepatuPria

def aksesorispria():
    df = pd.read_csv("DataAksesorisPria.csv")
    AksesorisPria = 0
    try:
        print("----------------------------------------------------")
        print("                  Aksesoris Pria                    ")
        print("----------------------------------------------------")
        print("Pilih Salah Satu")
        print(df)
        pilih = int(input("\nPilih: "))
        Produk = df["Barang"][pilih]
        Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
        Harga = Jumlah * df["Harga"][pilih]
        total_harga.append(Harga)
        keranjang_belanja["data"].append([Produk, Jumlah, Harga])
        datapembelian(name, Produk, Jumlah, Harga, Waktu)
        AksesorisPria += Jumlah
        print("Total Harga adalah :Rp.", Harga)
        print("----------------------------------------------------")

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        aksesorispria()
    except KeyError:
        print("\nError: Index yang anda input tidak tersedia !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        aksesorispria()
    penjualan_pria[3] = AksesorisPria

def baju_wanita():
    df = pd.read_csv("DataBajuWanita.csv")
    BajuWanita = 0
    try:
        print("----------------------------------------------------")
        print("                     Baju Wanita                    ")
        print("----------------------------------------------------")
        print("Pilih Salah Satu")
        print(df)
        pilih = int(input("\nPilih: "))
        Produk = df["Barang"][pilih]
        Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
        Harga = Jumlah * df["Harga"][pilih]
        total_harga.append(Harga)
        keranjang_belanja["data"].append([Produk, Jumlah, Harga])
        datapembelian(name, Produk, Jumlah, Harga, Waktu)
        BajuWanita += Jumlah
        print("Total Harga adalah :Rp.", Harga)
        print("----------------------------------------------------")

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        baju_wanita()
    except KeyError:
        print("\nError: Index yang anda input tidak tersedia !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        baju_wanita()
    penjualan_wanita[0] = BajuWanita

def celana_wanita():
    df = pd.read_csv("DataCelanaWanita.csv")
    CelanaWanita = 0
    try:
        print("----------------------------------------------------")
        print("                     Celana Wanita                  ")
        print("----------------------------------------------------")
        print("Pilih Salah Satu")
        print(df)
        pilih = int(input("\nPilih: "))
        Produk = df["Barang"][pilih]
        Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
        Harga = Jumlah * df["Harga"][pilih]
        total_harga.append(Harga)
        keranjang_belanja["data"].append([Produk, Jumlah, Harga])
        datapembelian(name, Produk, Jumlah, Harga, Waktu)
        CelanaWanita += Jumlah
        print("Total Harga adalah :Rp.", Harga)
        print("----------------------------------------------------")

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        celana_wanita()
    except KeyError:
        print("\nError: Index yang anda input tidak tersedia !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        celana_wanita()
    penjualan_wanita[1] = CelanaWanita

def sepatuwanita():
    df = pd.read_csv("DataSepatuWanita.csv")
    SepatuWanita = 0
    try:
        print("----------------------------------------------------")
        print("                     Sepatu Wanita                  ")
        print("----------------------------------------------------")
        print("Pilih Salah Satu")
        print(df)
        pilih = int(input("\nPilih: "))
        Produk = df["Barang"][pilih]
        Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
        Harga = Jumlah * df["Harga"][pilih]
        total_harga.append(Harga)
        keranjang_belanja["data"].append([Produk, Jumlah, Harga])
        datapembelian(name, Produk, Jumlah, Harga, Waktu)
        SepatuWanita += Jumlah
        print("Total Harga adalah :Rp.", Harga)
        print("----------------------------------------------------")

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        sepatuwanita()
    except KeyError:
        print("\nError: Index yang anda input tidak tersedia !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        sepatuwanita()
    penjualan_wanita[2] = SepatuWanita

def aksesoriswanita():
    df = pd.read_csv("DataAksesorisWanita.csv")
    AksesorisWanita = 0
    try:
        print("----------------------------------------------------")
        print("                     Aksesoris Wanita               ")
        print("----------------------------------------------------")
        print("Pilih Salah Satu")
        print(df)
        pilih = int(input("\nPilih: "))
        Produk = df["Barang"][pilih]
        Jumlah = int(input("Masukkan Jumlah yang ingin dibeli: "))
        Harga = Jumlah * df["Harga"][pilih]
        total_harga.append(Harga)
        keranjang_belanja["data"].append([Produk, Jumlah, Harga])
        datapembelian(name, Produk, Jumlah, Harga, Waktu)
        AksesorisWanita += Jumlah
        print("Total Harga adalah :Rp.", Harga)
        print("----------------------------------------------------")

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        aksesoriswanita()
    except KeyError:
        print("\nError: Index yang anda input tidak tersedia !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        aksesoriswanita()
    penjualan_wanita[3] = AksesorisWanita

def datapengunjung():
    df = pd.read_csv("DataCustomer.csv")
    print(df)
    print("----------------------------------------------------")
    print("              < Kembali: Tekan Enter >              ")
    input("                            ")
    admin()

def riwayatpembelian():
    df = pd.read_csv("DataPembelian.csv")
    print(df)
    print("----------------------------------------------------")
    print("              < Kembali: Tekan Enter >              ")
    input("                            ")
    admin()

def tambah_barang():
    try:
        print("----------------------------------------------------")
        print("                    Tambah Barang                   ")
        print("----------------------------------------------------")
        print("[1]Tambah Data Pria")
        print("[2]Tambah Data Wanita")
        print("[0]kembali")
        a = int(input("\nPilih: "))
        print("----------------------------------------------------")
        if (a == 1):
            print("[1]Baju")
            print("[2]Celana")
            print("[3]Sepatu")
            print("[4]Aksesoris")
            print("[0]kembali")
            b = int(input("\nPilih: "))
            print("----------------------------------------------------")
            if (b == 1):
                Barang = input("Masukkan Nama Barang : ")
                Harga = int(input("Masukkan Harga Barang : "))
                Data.append(Barang)
                Data.append(Harga)
                d = open('DataBajuPria.csv', 'a', newline='')
                w = csv.writer(d)
                w.writerow(Data)
                d.close()
                print("\nData Sudah Ditambah!!!")
                Data.clear()
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            elif (b == 2):
                Barang = input("Masukkan Nama Barang : ")
                Harga = int(input("Masukkan Harga Barang : "))
                Data.append(Barang)
                Data.append(Harga)
                d = open('DataCelanaPria.csv', 'a', newline='')
                w = csv.writer(d)
                w.writerow(Data)
                d.close()
                print("\nData Sudah Ditambah!!!")
                Data.clear()
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            elif (b == 3):
                Barang = input("Masukkan Nama Barang : ")
                Harga = int(input("Masukkan Harga Barang : "))
                Data.append(Barang)
                Data.append(Harga)
                d = open('DataSepatuPria.csv', 'a', newline='')
                w = csv.writer(d)
                w.writerow(Data)
                d.close()
                print("\nData Sudah Ditambah!!!")
                Data.clear()
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            elif (b == 4):
                Barang = input("Masukkan Nama Barang : ")
                Harga = int(input("Masukkan Harga Barang : "))
                Data.append(Barang)
                Data.append(Harga)
                d = open('DataAksesorisPria.csv', 'a', newline='')
                w = csv.writer(d)
                w.writerow(Data)
                d.close()
                print("\nData Sudah Ditambah!!!")
                Data.clear()
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            elif (b == 0):
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                tambah_barang()
            else:
                print("\nError: Masukkan angka yang ada !!!")
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                tambah_barang()
        elif (a == 2):
            print("[1]Baju")
            print("[2]Celana")
            print("[3]Sepatu")
            print("[4]Aksesoris")
            print("[0]kembali")
            b = int(input("\nPilih: "))
            print("----------------------------------------------------")
            if (b == 1):
                Barang = input("Masukkan Nama Barang : ")
                Harga = int(input("Masukkan Harga Barang : "))
                Data.append(Barang)
                Data.append(Harga)
                d = open('DataBajuWanita.csv', 'a', newline='')
                w = csv.writer(d)
                w.writerow(Data)
                d.close()
                print("\nData Sudah Ditambah!!!")
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            elif (b == 2):
                Barang = input("Masukkan Nama Barang : ")
                Harga = int(input("Masukkan Harga Barang : "))
                Data.append(Barang)
                Data.append(Harga)
                d = open('DataCelanaWanita.csv', 'a', newline='')
                w = csv.writer(d)
                w.writerow(Data)
                d.close()
                print("\nData Sudah Ditambah!!!")
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            elif (b == 3):
                Barang = input("Masukkan Nama Barang : ")
                Harga = int(input("Masukkan Harga Barang : "))
                Data.append(Barang)
                Data.append(Harga)
                d = open('DataSepatuWanita.csv', 'a', newline='')
                w = csv.writer(d)
                w.writerow(Data)
                d.close()
                print("\nData Sudah Ditambah!!!")
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            elif (b == 4):
                Barang = input("Masukkan Nama Barang : ")
                Harga = int(input("Masukkan Harga Barang : "))
                Data.append(Barang)
                Data.append(Harga)
                d = open('DataAksesorisWanita.csv', 'a', newline='')
                w = csv.writer(d)
                w.writerow(Data)
                d.close()
                print("\nData Sudah Ditambah!!!")
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            elif (b == 0):
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                tambah_barang()
            else:
                print("\nError: Masukkan angka yang ada !!!")
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                tambah_barang()
        elif (a == 0):
            print("              < Kembali: Tekan Enter >              ")
            input("                            ")
            admin()
        else:
            print("\nError: Masukkan angka yang ada !!!")
            print("----------------------------------------------------")
            print("              < Kembali: Tekan Enter >              ")
            input("                            ")
            tambah_barang()
    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        tambah_barang()

def updatebarang():
    try:
        print("----------------------------------------------------")
        print("                    Update Barang                   ")
        print("----------------------------------------------------")
        print("[1]Update Data Pria")
        print("[2]Update Data Wanita")
        print("[0]kembali")
        a = int(input("\nPilih: "))
        print("----------------------------------------------------")
        if (a == 1):
            print("[1]Baju")
            print("[2]Celana")
            print("[3]Sepatu")
            print("[4]Aksesoris")
            print("[0]kembali")
            b = int(input("\nPilih: "))
            print("----------------------------------------------------")
            if (b == 1):
                df1 = pd.read_csv("DataBajuPria.csv")
                print(df1)
                y = int(input("Mengubah data indeks ke : "))
                if (y == True):
                    df1.loc[y, 'Barang'] = input("Masukkan Nama Barang Baru: ")
                    df1.loc[y, 'Harga'] = int(input("Masukkan Harga Barang Baru: "))
                    df1.to_csv("DataBajuPria.csv", index=False)
                    print("\nData Sudah Diupdate!!!")
                    print("----------------------------------------------------")
                    print("              < Kembali: Tekan Enter >              ")
                    input("                            ")
                    admin()
                else:
                    print("\nError: Index yang anda input tidak tersedia !!!")
                    print("----------------------------------------------------")
                    print("              < Kembali: Tekan Enter >              ")
                    input("                            ")
                    updatebarang()
            elif (b == 2):
                df2 = pd.read_csv("DataCelanaPria.csv")
                print(df2)
                y = int(input("Mengubah data indeks ke : "))
                if (y == True):
                    df2.loc[y, 'Barang'] = input("Masukkan Nama Barang Baru: ")
                    df2.loc[y, 'Harga'] = int(input("Masukkan Harga Barang Baru: "))
                    df2.to_csv("DataCelanaPria.csv", index=False)
                    print("\nData Sudah Diupdate!!!")
                    print("----------------------------------------------------")
                    print("              < Kembali: Tekan Enter >              ")
                    input("                            ")
                    admin()
                else:
                    print("\nError: Index yang anda input tidak tersedia !!!")
                    print("----------------------------------------------------")
                    print("              < Kembali: Tekan Enter >              ")
                    input("                            ")
                    updatebarang()
            elif (b == 3):
                df3 = pd.read_csv("DataSepatuPria.csv")
                print(df3)
                y = int(input("Mengubah data indeks ke : "))
                if (y == True):
                    df3.loc[y, 'Barang'] = input("Masukkan Nama Barang Baru: ")
                    df3.loc[y, 'Harga'] = int(input("Masukkan Harga Barang Baru: "))
                    df3.to_csv("DataSepatuPria.csv", index=False)
                    print("\nData Sudah Diupdate!!!")
                    print("----------------------------------------------------")
                    print("              < Kembali: Tekan Enter >              ")
                    input("                            ")
                    admin()
                else:
                    print("\nError: Index yang anda input tidak tersedia !!!")
                    print("----------------------------------------------------")
                    print("              < Kembali: Tekan Enter >              ")
                    input("                            ")
                    updatebarang()
            elif (b == 4):
                df4 = pd.read_csv("DataAksesorisPria.csv")
                print(df4)
                y = int(input("Mengubah data indeks ke : "))
                if (y == True):
                    df4.loc[y, 'Barang'] = input("Masukkan Nama Barang Baru: ")
                    df4.loc[y, 'Harga'] = int(input("Masukkan Harga Barang Baru: "))
                    df4.to_csv("DataAksesorisPria.csv", index=False)
                    print("\nData Sudah Diupdate!!!")
                    print("----------------------------------------------------")
                    print("              < Kembali: Tekan Enter >              ")
                    input("                            ")
                    admin()
                else:
                    print("\nError: Index yang anda input tidak tersedia !!!")
                    print("----------------------------------------------------")
                    print("              < Kembali: Tekan Enter >              ")
                    input("                            ")
                    updatebarang()
            elif (b == 0):
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            else:
                print("\nError: Masukkan angka yang ada !!!")
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                updatebarang()

        elif (a == 2):
            print("[1]Baju")
            print("[2]Celana")
            print("[3]Sepatu")
            print("[4]Aksesoris")
            print("[0]kembali")
            b = int(input("\nPilih: "))
            print("----------------------------------------------------")
            if (b == 1):
                df1 = pd.read_csv("DataBajuWanita.csv")
                print(df1)
                y = int(input("Mengubah data indeks ke : "))
                if (y == True):
                    df1.loc[y, 'Barang'] = input("Masukkan Nama Barang Baru: ")
                    df1.loc[y, 'Harga'] = int(input("Masukkan Harga Barang Baru: "))
                    df1.to_csv("DataBajuWanita.csv", index=False)
                    print("\nData Sudah Diupdate!!!")
                    print("----------------------------------------------------")
                    print("              < Kembali: Tekan Enter >              ")
                    input("                            ")
                    admin()
                else:
                    print("\nError: Index yang anda input tidak tersedia !!!")
                    print("----------------------------------------------------")
                    print("              < Kembali: Tekan Enter >              ")
                    input("                            ")
                    updatebarang()
            elif (b == 2):
                df2 = pd.read_csv("DataCelanaWanita.csv")
                print(df2)
                y = int(input("Mengubah data indeks ke : "))
                if (y == True):
                    df2.loc[y, 'Barang'] = input("Masukkan Nama Barang Baru: ")
                    df2.loc[y, 'Harga'] = int(input("Masukkan Harga Barang Baru: "))
                    df2.to_csv("DataCelanaWanita.csv", index=False)
                    print("\nData Sudah Diupdate!!!")
                    print("----------------------------------------------------")
                    print("              < Kembali: Tekan Enter >              ")
                    input("                            ")
                    admin()
                else:
                    print("\nError: Index yang anda input tidak tersedia !!!")
                    print("----------------------------------------------------")
                    print("              < Kembali: Tekan Enter >              ")
                    input("                            ")
                    updatebarang()
            elif (b == 3):
                df2 = pd.read_csv("DataSepatuWanita.csv")
                print(df2)
                y = int(input("Mengubah data indeks ke : "))
                if (y == True):
                    df2.loc[y, 'Barang'] = input("Masukkan Nama Barang Baru: ")
                    df2.loc[y, 'Harga'] = int(input("Masukkan Harga Barang Baru: "))
                    df2.to_csv("DataSepatuWanita.csv", index=False)
                    print("\nData Sudah Diupdate!!!")
                    print("----------------------------------------------------")
                    print("              < Kembali: Tekan Enter >              ")
                    input("                            ")
                    admin()
                else:
                    print("\nError: Index yang anda input tidak tersedia !!!")
                    print("----------------------------------------------------")
                    print("              < Kembali: Tekan Enter >              ")
                    input("                            ")
                    updatebarang()
            elif (b == 4):
                df2 = pd.read_csv("DataAksesorisWanita.csv")
                print(df2)
                y = int(input("Mengubah data indeks ke : "))
                if (y == True):
                    df2.loc[y, 'Barang'] = input("Masukkan Nama Barang Baru: ")
                    df2.loc[y, 'Harga'] = int(input("Masukkan Harga Barang Baru: "))
                    df2.to_csv("DataAksesorisWanita.csv", index=False)
                    print("\nData Sudah Diupdate!!!")
                    print("----------------------------------------------------")
                    print("              < Kembali: Tekan Enter >              ")
                    input("                            ")
                    admin()
                else:
                    print("\nError: Index yang anda input tidak tersedia !!!")
                    print("----------------------------------------------------")
                    print("              < Kembali: Tekan Enter >              ")
                    input("                            ")
                    updatebarang()
            elif (b == 0):
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            else:
                print("\nError: Masukkan angka yang ada !!!")
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                updatebarang()
        elif (a == 0):
            print("              < Kembali: Tekan Enter >              ")
            input("                            ")
            admin()
        else:
            print("\nError: Masukkan angka yang ada !!!")
            print("----------------------------------------------------")
            print("              < Kembali: Tekan Enter >              ")
            input("                            ")
            updatebarang()
    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        updatebarang()

def hapusbarang():
    try:
        print("----------------------------------------------------")
        print("                    Hapus Barang                    ")
        print("----------------------------------------------------")
        print("[1]Hapus Data Pria")
        print("[2]Hapus Data Wanita")
        print("[0]kembali")
        a = int(input("\nPilih: "))
        print("----------------------------------------------------")
        if (a == 1):
            print("[1]Baju")
            print("[2]Celana")
            print("[3]Sepatu")
            print("[4]Aksesoris")
            print("[0]kembali")
            b = int(input("\nPilih: "))
            print("----------------------------------------------------")
            if (b == 1):
                df1 = pd.read_csv("DataBajuPria.csv")
                print(df1)
                A = int(input("Masukkan Index Barang Yang Ingin Dihapus: "))
                df1 = df1.drop(A)
                df1.to_csv("DataBajuPria.csv", index=False)
                print("\nData Sudah Dihapus!!!")
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            elif (b == 2):
                df2 = pd.read_csv("DataCelanaPria.csv")
                print(df2)
                A = int(input("Masukkan Index Barang Yang Ingin Dihapus: "))
                df2 = df2.drop(A)
                df2.to_csv("DataCelanaPria.csv", index=False)
                print("\nData Sudah Dihapus!!!")
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            elif (b == 3):
                df3 = pd.read_csv("DataSepatuPria.csv")
                print(df3)
                A = int(input("Masukkan Index Barang Yang Ingin Dihapus: "))
                df3 = df3.drop(A)
                df3.to_csv("DataSepatuPria.csv", index=False)
                print("\nData Sudah Diupdate!!!")
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            elif (b == 4):
                df4 = pd.read_csv("DataAksesorisPria.csv")
                print(df4)
                A = int(input("Masukkan Index Barang Yang Ingin Dihapus: "))
                df4 = df4.drop(A)
                df4.to_csv("DataAksesorisPria.csv", index=False)
                print("\nData Sudah Dihapus!!!")
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            elif (b == 0):
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            else:
                print("\nError: Masukkan angka yang ada !!!")
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                hapusbarang()

        elif (a == 2):
            print("[1]Baju")
            print("[2]Celana")
            print("[3]Sepatu")
            print("[4]Aksesoris")
            print("[0]kembali")
            b = int(input("\nPilih: "))
            print("----------------------------------------------------")
            if (b == 1):
                df1 = pd.read_csv("DataBajuWanita.csv")
                print(df1)
                A = int(input("Masukkan Index Barang Yang Ingin Dihapus: "))
                df1 = df1.drop(A)
                df1.to_csv("DataBajuWanita.csv", index=False)
                print("\nData Sudah Dihapus!!!")
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            elif (b == 2):
                df2 = pd.read_csv("DataCelanaWanita.csv")
                print(df2)
                A = int(input("Masukkan Index Barang Yang Ingin Dihapus: "))
                df2 = df2.drop(A)
                df2.to_csv("DataCelanaWanita.csv", index=False)
                print("\nData Sudah Dihapus!!!")
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            elif (b == 3):
                df2 = pd.read_csv("DataSepatuWanita.csv")
                print(df2)
                A = int(input("Masukkan Index Barang Yang Ingin Dihapus: "))
                df2 = df2.drop(A)
                df2.to_csv("DataSepatuWanita.csv", index=False)
                print("\nData Sudah Dihapus!!!")
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            elif (b == 4):
                df2 = pd.read_csv("DataAksesorisWanita.csv")
                print(df2)
                A = int(input("Masukkan Index Barang Yang Ingin Dihapus: "))
                df2 = df2.drop(A)
                df2.to_csv("DataAksesorisWanita.csv", index=False)
                print("\nData Sudah Dihapus!!!")
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            elif (b == 0):
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
            else:
                print("\nError: Masukkan angka yang ada !!!")
                print("----------------------------------------------------")
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                hapusbarang()
        elif (a == 0):
                print("              < Kembali: Tekan Enter >              ")
                input("                            ")
                admin()
        else:
            print("\nError: Masukkan angka yang ada !!!")
            print("----------------------------------------------------")
            print("              < Kembali: Tekan Enter >              ")
            input("                            ")
            hapusbarang()

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        hapusbarang()
    except KeyError:
        print("\nError: Index yang anda input tidak tersedia !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        hapusbarang()

def grafik():
    labels = ['Baju', 'Celana', 'Sepatu', 'Aksesoris']
    x = np.arange(len(labels))
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, penjualan_pria, width, label='Pria')
    rects2 = ax.bar(x + width / 2, penjualan_wanita, width, label='Wanita')

    ax.set_ylabel('Penjualan')
    ax.set_title('Grafik Penjualan')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    fig.tight_layout()
    plt.show()

    print("----------------------------------------------------")
    print("              < Kembali: Tekan Enter >              ")
    input("                            ")
    admin()

def datagrafik():
    m = open('DataPembelian.csv', 'a', newline='')
    w = csv.writer(m)
    w.writerow(penjualan_pria)

def pembayaran():
    print(" ____________________________________________________ ")
    print("|                                                    |")
    print("|                                                    |")
    print("|====================================================|")
    print("|                  Keranjang Belanja                 |")
    print("|                                                    |")
    for i in range(len(keranjang_belanja["data"])):
        n = len(keranjang_belanja["data"])
        quickSortAsc(keranjang_belanja["data"], 0, n - 1)
        print("|  Produk      : ", (keranjang_belanja["data"][i][0]))
        print("|  Jumlah      : ", (keranjang_belanja["data"][i][1]))
        print("|  Total Harga : ", (keranjang_belanja["data"][i][2]))
        print("\n------------------------------------------------------")
    print("Total Harga   : Rp.", sum(total_harga))
    print("------------------------------------------------------")

def checkout():
    try:
        pembayaran()
        harga = sum(total_harga)
        bayar = int(input("Masukkan Jumlah Pembayaran: "))
        if (bayar >= harga):
            print("----------------------------------------------- ----")
            print("Jumlah Pembayaran : Rp.",bayar)
            print("Total Harga       : Rp.",harga)
            print("Kembalian         : Rp.",bayar-harga)
            print("            Terima Kasih Telah Bebelanja            ")
            print("----------------------------------------------------")
            print("              < Kembali: Tekan Enter >              ")
            input("                          ")

        else:
            print("Error: Uang Pembayaran Tidak Mencukupi !!!")
            print("----------------------------------------------------")
            print("              < Kembali: Tekan Enter >              ")
            input("                          ")
            checkout()

    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                          ")
        checkout()

Start = True
while (Start):
    reset()
    print("----------------------------------------------------")
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

    print("           Anda ingin masuk sebagai apa?            ")
    print("----------------------------------------------------")
    print("[1] Customer                                         ")
    print("[2] Admin                                            ")
    print("[0] Keluar                                           ")
    print("----------------------------------------------------")

    try:
        Login = int(input("Pilih : "))
        Start2 = True
        if (Login == 1):
            Start = False
            print("           Masukkan Data Diri           ")
            name = str(input("Nama   : "))
            age = int(input("Umur   : "))
            alamat = str(input("Alamat : "))
            email = str(input("Email  : "))
            isidata(name, age, alamat, email)
            while (Start2):
                fashion()
                try:
                    a = int(input("Ingin Melanjutkan?\n1.Iya\n2.Tidak "))
                    if a == 1:
                        Start2=True
                    elif a == 2:
                        Start2 = False
                        checkout()
                        Start3 = True
                        while (Start3):
                            a = int(input("Ingin Melanjutkan?\n1.Iya\n2.Tidak "))
                            if a == 1:
                                keranjang_belanja["data"].clear()
                                total_harga.clear()
                                Start3 = False
                                Start2 = True
                            elif a == 2:
                                keranjang_belanja["data"].clear()
                                total_harga.clear()
                                Start3 = False
                                Start2 = False
                                Start = True
                            else:
                                print("\nError: Masukkan angka yang ada !!!")
                                print("----------------------------------------------------")
                                print("              < Kembali: Tekan Enter >              ")
                                input("                            ")
                    else:
                        print("\nError: Masukkan angka yang ada !!!")
                        print("----------------------------------------------------")
                        print("              < Kembali: Tekan Enter >              ")
                        input("                            ")

                except ValueError:
                    print("\nError: Masukkan angka !!!")
                    print("----------------------------------------------------")
                    print("              < Kembali: Tekan Enter >              ")
                    input("                            ")

        elif (Login == 2):
            Start = False
            while (Start2):
                x = 5
                while x > 0:
                    reset()
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

                    else:
                        x -= 1
                        if (User == "admin" and Password != "123"):
                            print("\nError: Password yang anda masukkan salah !!!\nKesempatan :[", x,"]")
                            print("----------------------------------------------------")

                        elif (User != "admin" and Password == "123"):
                            print("\nError: Username yang dimasukkan tidak terdata !!!\nKesempatan :[", x,"]")
                            print("----------------------------------------------------")

                        else:
                            print("\nError: Username yang dimasukkan tidak terdata !!! \nKesempatan :[", x,"]")
                            print("----------------------------------------------------")

                        if x == 0:
                            print("            Kesempatan Anda telah habis             ") 
                            print("               Kembali Ke Menu Awal?                 ")
                            print("----------------------------------------------------")
                            input("                  < Tekan Enter >")
                    try:
                        a = int(input("Ingin Melanjutkan?\n1.Iya\n2.Tidak "))
                        if a == 1:
                            Start2 = True
                        elif a == 2:
                            Start2 = False
                            Start = True
                        else:
                            print("\nError: Masukkan angka yang ada !!!")
                            print("----------------------------------------------------")
                            print("              < Kembali: Tekan Enter >              ")
                            input("                            ")
                    except ValueError:
                        print("\nError: Masukkan angka !!!")
                        print("----------------------------------------------------")
                        print("              < Kembali: Tekan Enter >              ")
                        input("                            ")
        elif (Login == 0):
            print("----------------------------------------------------")
            print("                 < Program Selesai >                ")
            input("                            ")
            exit(0)
        else:
            print("\nError: Masukkan angka yang ada !!!")
            print("----------------------------------------------------")
            print("              < Kembali: Tekan Enter >              ")
            input("                            ")
            Start = True
    except ValueError:
        print("\nError: Masukkan angka !!!")
        print("----------------------------------------------------")
        print("              < Kembali: Tekan Enter >              ")
        input("                            ")
        Start = True