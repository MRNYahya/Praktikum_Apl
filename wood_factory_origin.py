hargaPlywood = 150000
hargaMeubel = 500000
hargaPapan = 100000
hargaBalok = 120000

def sekb():
    angka = ''
    for huruf in b:
        if ord(huruf) >= 48 and ord(huruf) <= 57:
            angka += str(huruf)
    return angka

def madmin():
    print ('  ______________________________')
    print (' /       /             \        \ ')
    print ('/_______/_______________\________\ ')
    print ('|________________________________|')
    print ('|       Admin Wood Factory       |')
    print ('|________________________________|')
    print ('| Pilih Salah Satu Menu Berikut. |')
    print ('| 1. Produksi                    |')
    print ('| 2. Riwayat Penjualan           |')
    print ('| 3. Stok dan Modal              |')
    print ('|                                |')
    print ('| 9. Kembali                     |')
    print ('| 0. Keluar                      |')
    print ('|________________________________|')

def produksi():
    print ('  ______________________________')
    print (' /       /             \        \ ')
    print ('/_______/_______________\________\ ')
    print ('|________________________________|')
    print ('|        Bagian Produksi         |')
    print ('|________________________________|')
    print ('| Output Yang Akan Dihasilkan :  |')
    print ('|                                |')
    print ('| 1. Besar Modal Yang Digunakan  |')
    print ('| 2. Total Hasil Produksi        |')
    print ('|________________________________|')
    print ('|________________________________|')
    print ('|     Pilihan Hasil Produksi     |')
    print ('|________________________________|')
    print ('| 1. Plywood                     |')
    print ('| 2. Meubel                      |')
    print ('| 3. Papan dan Balok             |')
    print ('|________________________________|')
    
def penjualan ():
    print ('  ______________________________                       @@')
    print (' /       /             \        \                   __@@_')
    print ('/_______/_______________\________\                  |  _|')
    print ('|_________________________________\                 |  |')
    print ('|        Bagian Penjualan        |__________________|  |_____')
    print ('|________________________________|___________________________\_')
    print ('| Hal-hal yang perlu diperhatikan|_____________________________\_')
    print ('| 1. Inputkan (9) Untuk Kembali  |_______________________________\ ')
    print ('| 2. Inputkan (0) Untuk Keluar   |')
    print ('| 3. Harap Sesuaikan Input       | Stok Plywood :',THP1,'Unit')
    print ('|________________________________| Stok Meubel  :',THP2,'Unit')
    print ('|________________________________| Stok Papan   :',THP3,'Unit')
    print ('|      Daftar Diskon Produk      | Stok Balok   :',THP4,'Unit')
    print ('|________________________________|________________________________')
    print ('| 1. Plywood                     | 2. Meubel                     |')
    print ('| - <=100   : Harga Normal       | - <=50    : Harga Normal      |')
    print ('| - 101-300 : 5%                 | - 51-100  : 5%                |')
    print ('| - 301-500 : 15%                | - 101-200 : 15%               |')
    print ('| - >500    : 30%                | - >200    : 30%               |')
    print ('| Harga Per Unit : Rp.150.000,-  | Harga Per Unit : Rp.500.000,- |')
    print ('|________________________________|_______________________________|')
    print ('| 3. Papan                       | 4. Balok                      |')
    print ('| - <=100   : Harga Normal       | - <=10  : Harga Normal        |')
    print ('| - 101-300  : 5%                | - 11-30 : 5%                  |')
    print ('| - 301-500 : 15%                | - 31-50 : 15%                 |')
    print ('| - >500    : 30%                | - >50   : 30%                 |')
    print ('| Harga Per Unit : Rp.100.000,-  | Harga Per Unit : Rp.120.000,- |')
    print ('|________________________________|_______________________________|')

def dplywood():
    if plywood <= 100:
        harga1 = plywood * hargaPlywood
    elif plywood > 100 and plywood <= 300:
        harga1 = (plywood * hargaPlywood)-((plywood * hargaPlywood)*0.05)
    elif plywood > 300 and plywood <= 500:
        harga1 = (plywood * hargaPlywood)-((plywood * hargaPlywood)*0.15)
    elif plywood > 500:
        harga1 = (plywood * hargaPlywood)-((plywood * hargaPlywood)*0.3)
    else:
        harga1 = 0
    return harga1

def dmeubel():
    if meubel <= 50:
        harga2 = meubel * hargaMeubel
    elif meubel > 50 and meubel <= 100:
        harga2 = (meubel * hargaMeubel)-((meubel * hargaMeubel)*0.05)
    elif meubel > 100 and meubel <= 200:
        harga2 = (meubel * hargaMeubel)-((meubel * hargaMeubel)*0.15)
    elif meubel > 200:
        harga2 = (meubel * hargaMeubel)-((meubel * hargaMeubel)*0.3)
    else:
        harga2 = 0
    return harga2

def dpapan():
    if papan <= 100:
        harga3 = papan * hargaPapan
    elif papan > 100 and papan <= 300:
        harga3 = (papan * hargaPapan)-((papan * hargaPapan)*0.05)
    elif papan > 300 and papan <= 500:
        harga3 = (papan * hargaPapan)-((papan * hargaPapan)*0.15)
    elif papan > 500:
        harga3 = (papan * hargaPapan)-((papan * hargaPapan)*0.3)
    else:
        harga3 = 0
    return harga3

def dbalok():
    if balok <= 10:
        harga4 = balok * hargaBalok
    elif balok > 10 and balok <= 30:
        harga4 = (balok * hargaBalok)-((balok * hargaBalok)*0.05)
    elif balok > 30 and balok <= 50:
        harga4 = (balok * hargaBalok)-((balok * hargaBalok)*0.15)
    elif balok > 50:
        harga4 = (balok * hargaBalok)-((balok * hargaBalok)*0.3)
    else:
        harga4 = 0
    return harga4

def login():
    print ('_____________________')
    print ('| Pilih Menu Login  |')
    print ('|___________________|')
    print ('| 1. Admin          |')
    print ('| 2. User           |')
    print ('| 3. Keluar         |')
    print ('|___________________|')
    
def tidakcukup():
    print ('______________________')
    print ('| MODAL TIDAK CUKUP! |')
    print ('|____________________|')

def papan_kosong():
    print ('')
    print ('Stok Papan Tidak Cukup!')
    print ('')

def plywood_kosong():
    print ('')
    print ('Stok Plywood Tidak Cukup!')
    print ('')

def meubel_kosong():
    print ('')
    print ('Stok Meubel Tidak Cukup!')
    print ('')

def balok_kosong():
    print ('')
    print ('Stok Balok Tidak Cukup!')
    print ('')

def cetak():
    print ('_________________________________')
    print ('|________________________________\ ')
    print ('| _______________________________/')
    print ('| |Plywood : ',jplywood)
    print ('| |Meubel  : ',jmeubel)
    print ('| |Papan   : ',jpapan)
    print ('| |Balok   : ',jbalok)
    print ('| |Total   : ',total,'Juta')
    print ('| |_____________________________')
    print ('|_______________________________\ ')
    print ('|_______________________________/')

def appendr():
    riwayat.append(jplywood)
    riwayat.append(jmeubel)
    riwayat.append(jpapan)
    riwayat.append(jbalok)
    riwayat.append(total)

def appendp():
    produksi2.append(THP1)
    produksi2.append(THP2)
    produksi2.append(THP3)
    produksi2.append(THP4)
    produksi2.append(modal)

def akhir():
    print ('__________________________________')
    print ('|     Total Biaya Keseluruhan    |')
    cetak()
    appendp()
    appendr()
    d = open('data.csv', 'a', newline='')
    w = csv.writer(d)
    w.writerow(riwayat)
    d.close()
    m = open('modal.csv', 'w', newline='')
    w = csv.writer(m)
    w.writerow(('Plywood','Meubel','Papan','Balok','Modal'))
    w.writerow(produksi2)
    m.close()

import csv
import pandas as pd
awal = True
while (awal):
    import datetime
    x = datetime.datetime.now()
    a = x.hour
    if a >= 5 and a <= 11:
        print ('_____________________')
        print ('|    Selamat Pagi   |')
        print ('|___________________|')
    elif a > 11 and a <= 14:
        print ('_____________________')
        print ('|   Selamat Siang   |')
        print ('|___________________|')
    elif a > 14 and a <= 17:
        print ('_____________________')
        print ('|    Selamat Sore   |')
        print ('|___________________|')
    elif a > 17 or a < 5:
        print ('_____________________')
        print ('|   Selamat Malam   |')
        print ('|___________________|')
    login()
    awal1 = True
    while (awal1):
        datap = pd.read_csv('modal.csv')
        THP1 = (datap['Plywood'][0])
        THP2 = (datap['Meubel'][0])
        THP3 = (datap['Papan'][0])
        THP4 = (datap['Balok'][0])
        modal = (datap['Modal'][0])
        a=str(input('Masukkan Pilihan : '))
        if a == '1' or a == '2' or a == '3':
            awal = False
            awal1 = False
            if a == '1':
                admin = True
                while (admin):
                    id = str(input('ID Admin : '))
                    pw = str(input('Password : '))
                    if id == 'Admin' and pw == '12345':
                        awal3 = True
                        while (awal3):
                            madmin ()
                            admin = False
                            awal2 = True
                            while (awal2):
                                piladmin = str(input('Masukkan Pilihan : '))
                                if piladmin == '1' or piladmin == '2' or piladmin == '3' or piladmin == '9' or piladmin == '0':
                                    awal2 = False
                                    if piladmin == '1':
                                        produksi1 = []
                                        produksi ()
                                        luas = True
                                        while (luas):
                                            b = input('Luas Lahan Satuan Ha : ')
                                            if sekb() == b:
                                                b = int(sekb())
                                                if b >= 1:
                                                    luas = False
                                                    pilih2 = True
                                                    while (pilih2):
                                                        c= str(input('Pilih Hasil Produksi : '))
                                                        if c == '1' or c == '2' or c == '3':
                                                            pilih2 = False
                                                            if c == '1':
                                                                THP = 320*(100*b)
                                                                GPH = 800000000*b
                                                                BOLP = BSL = 500000000*b
                                                                Modal = BOLP + BSL + GPH
                                                                ModalM = Modal/1000000
                                                                if modal >= ModalM:
                                                                    print ('_____________________________________')
                                                                    print ('|  Hasil Dalam Kurun Waktu 1 Tahun  |')
                                                                    print ('|___________________________________|')
                                                                    print ('| Luas Lahan Hutan     :',b,'Ha')
                                                                    print ('| Jumlah Produksi Kayu :',100*b,'Pohon')
                                                                    print ('| Total Hasil Produksi :',THP,'Lembar')
                                                                    print ('| Modal Usaha          : Rp.',Modal/1000000000,'M')
                                                                    print ('|____________________________________')
                                                                    modal -= ModalM
                                                                    THP1 += THP
                                                                    produksi1.append (THP1)
                                                                    produksi1.append (THP2)
                                                                    produksi1.append (THP3)
                                                                    produksi1.append (THP4)
                                                                    produksi1.append (modal)
                                                                    f = open('D:\modal.csv', 'w', newline='')
                                                                    w = csv.writer(f)
                                                                    w.writerow (('Plywood','Meubel','Papan','Balok','Modal'))
                                                                    w.writerow (produksi1)
                                                                    f.close()
                                                                    lanjut_admin = str(input('Ingin Melanjutkan Menu Admin(y/n)? '))
                                                                    if lanjut_admin == 'y' or lanjut_admin == 'n':
                                                                        if lanjut_admin == 'n':
                                                                            awal = True
                                                                            awal3 = False
                                                                        else:
                                                                            print ('Input Tidak Valid!')
                                                                else:
                                                                    tidakcukup()
                                                                    lanjut_admin = str(input('Ingin Melanjutkan Menu Admin(y/n)? '))
                                                                    if lanjut_admin == 'y' or lanjut_admin == 'n':
                                                                        if lanjut_admin == 'n':
                                                                            awal3 = False
                                                                            awal = True
                                                                        else:
                                                                            print ('Input Tidak Valid!')
                                                            elif c == '2':
                                                                THP = 100*(100*b)
                                                                GPH = 800000000*b
                                                                BOLP = BSL = 500000000*b
                                                                Modal = BOLP + BSL + GPH
                                                                ModalM = Modal/1000000
                                                                if modal >= ModalM:
                                                                    print ('_____________________________________')
                                                                    print ('|  Hasil Dalam Kurun Waktu 1 Tahun  |')
                                                                    print ('|___________________________________|')
                                                                    print ('| Luas Lahan Hutan     :',b,'Ha')
                                                                    print ('| Jumlah Produksi Kayu :',100*b,'Pohon')
                                                                    print ('| Total Hasil Produksi :',THP,'Unit')
                                                                    print ('| Modal Usaha          : Rp.',Modal/1000000000,'M')
                                                                    print ('|____________________________________')
                                                                    modal -= ModalM
                                                                    THP2 += THP
                                                                    produksi1.append (THP1)
                                                                    produksi1.append (THP2)
                                                                    produksi1.append (THP3)
                                                                    produksi1.append (THP4)
                                                                    produksi1.append (modal)
                                                                    f = open('modal.csv', 'w', newline='')
                                                                    w = csv.writer(f)
                                                                    w.writerow (('Plywood','Meubel','Papan','Balok','Modal'))
                                                                    w.writerow (produksi1)
                                                                    f.close()
                                                                    lanjut_admin = str(input('Ingin Melanjutkan Menu Admin(y/n)? '))
                                                                    if lanjut_admin == 'y' or lanjut_admin == 'n':
                                                                        if lanjut_admin == 'n':
                                                                            awal3 = False
                                                                            awal = True
                                                                        else:
                                                                            print ('Input Tidak Valid!')
                                                                else:
                                                                    tidakcukup()
                                                                    lanjut_admin = str(input('Ingin Melanjutkan Menu Admin(y/n)? '))
                                                                    if lanjut_admin == 'y' or lanjut_admin == 'n':
                                                                        if lanjut_admin == 'n':
                                                                            awal3 = False
                                                                            awal = True
                                                                        else:
                                                                            print ('Input Tidak Valid!')
                                                            else:
                                                                THPp = 200*(100*b)
                                                                THPb = 20*(100*b)
                                                                GPH = 800000000*b
                                                                BOLP = BSL = 500000000*b
                                                                Modal = BOLP + BSL + GPH
                                                                ModalM = Modal/1000000
                                                                if modal >= ModalM:
                                                                    print ('_____________________________________')
                                                                    print ('|  Hasil Dalam Kurun Waktu 1 Tahun  |')
                                                                    print ('|___________________________________|')
                                                                    print ('| Luas Lahan Hutan     :',b,'Ha')
                                                                    print ('| Jumlah Produksi Kayu :',100*b,'Pohon')
                                                                    print ('| Total Hasil Produksi : ')
                                                                    print ('| Papan : ',THPp,'Lembar')
                                                                    print ('| Balok : ',THPb,'Bilah')
                                                                    print ('| Modal Usaha          : Rp.',Modal/1000000000,'M')
                                                                    print ('|____________________________________')
                                                                    modal -= ModalM
                                                                    THP3 += THPp
                                                                    THP4 += THPb
                                                                    produksi1.append (THP1)
                                                                    produksi1.append (THP2)
                                                                    produksi1.append (THP3)
                                                                    produksi1.append (THP4)
                                                                    produksi1.append (modal)
                                                                    f = open('modal.csv', 'w', newline='')
                                                                    w = csv.writer(f)
                                                                    w.writerow (('Plywood','Meubel','Papan','Balok','Modal'))
                                                                    w.writerow (produksi1)
                                                                    f.close()
                                                                    lanjut_admin = str(input('Ingin Melanjutkan Menu Admin(y/n)? '))
                                                                    if lanjut_admin == 'y' or lanjut_admin == 'n':
                                                                        if lanjut_admin == 'n':
                                                                            awal3 = False
                                                                            awal = True
                                                                        else:
                                                                            print ('Input Tidak Valid!')
                                                                else:
                                                                    tidakcukup()
                                                                    lanjut_admin = str(input('Ingin Melanjutkan Menu Admin(y/n)? '))
                                                                    if lanjut_admin == 'y' or lanjut_admin == 'n':
                                                                        if lanjut_admin == 'n':
                                                                            awal3 = False
                                                                            awal = True
                                                                        else:
                                                                            print ('Input Tidak Valid!')
                                                        else:
                                                            print ('Input Tidak Valid!')
                                                    else:
                                                        print ('Input Tidak Valid!')
                                                else:
                                                    print ('Input Tidak Valid!')
                                            else:
                                                print ('Input Tidak Valid!')
                                    elif piladmin == '2':
                                        data = pd.read_csv('data.csv')
                                        print ('_____________________________________________________')
                                        print (data)
                                        print ('_____________________________________________________')
                                        lanjut_admin = str(input('Ingin Melanjutkan Menu Admin(y/n)? '))
                                        if lanjut_admin == 'y' or lanjut_admin == 'n':
                                            if lanjut_admin == 'n':
                                                awal3 = False
                                                awal = True
                                            else:
                                                print ('Input Tidak Valid!')
                                    elif piladmin == '3':
                                        stok = pd.read_csv('modal.csv')
                                        print ('______________________________________________')
                                        print (stok)
                                        print ('______________________________________________')
                                        lanjut_admin = str(input('Ingin Melanjutkan Menu Admin(y/n)? '))
                                        if lanjut_admin == 'y' or lanjut_admin == 'n':
                                            if lanjut_admin == 'n':
                                                awal3 = False
                                                awal = True
                                            else:
                                                print ('Input Tidak Valid!')
                                    elif piladmin == '9':
                                        awal = True
                                        awal1 = False
                                        admin = False
                                        awal3 = False
                                        awal2 = False
                                    else:
                                        awal = False
                                        awal1 = False
                                        admin = False
                                        awal3 = False
                                        awal2 = False
                                else:
                                    print ('Input Tidak Valid!')                                
                    else:
                        print ('')
                        print ('ID atau Kode Salah!')
                        lanjut = str(input('Coba Lagi(y/n)? '))
                        if lanjut == 'y' or lanjut == 'n':
                            if lanjut == 'n':
                                admin = False
            elif a == '2':
                riwayat = []
                produksi2 = []
                nama = str(input('Nama Lengkap Anda : '))
                riwayat.append(nama)
                stat1 = True
                jplywood = 0
                jmeubel = 0
                jpapan = 0 
                jbalok = 0
                total = 0
                while (stat1):
                    penjualan()
                    pilih = str(input('Masukkan Pilihan : '))
                    if pilih == '1' or pilih == '2' or pilih == '3' or pilih == '4' or pilih == '9' or pilih == '0':
                        if pilih == '1':
                            splywood = True
                            while (splywood):
                                plywood = input('Jumlah Plywood Yang Ingin Dibeli : ')
                                b = plywood
                                sekb()
                                if sekb() == b:
                                    splywood = False
                                    plywood = int(sekb())
                                    if plywood > 0:
                                        if plywood <= THP1:
                                            dplywood()
                                            total += (dplywood()/1000000)
                                            THP1 -= plywood
                                            jplywood += plywood
                                            cetak()
                                            gas = True
                                            while (gas):
                                                lanjut_beli = str(input('Ingin Melanjutkan Pembelian(y/n)? '))
                                                if lanjut_beli == 'n' or lanjut_beli == 'y':
                                                    gas = False
                                                    if lanjut_beli == 'n':
                                                        stat1 = False
                                                        awal = True
                                                        modal += total
                                                        akhir()
                                                else:
                                                    print ('')
                                                    print ('Input Tidak Valid!')
                                        else:
                                            plywood_kosong()
                                            if total != 0:
                                                cetak()
                                            gas = True
                                            while (gas):
                                                lanjut_beli = str(input('Ingin Melanjutkan Pembelian(y/n)? '))
                                                if lanjut_beli == 'n' or lanjut_beli == 'y':
                                                    gas = False
                                                    if lanjut_beli == 'n':
                                                        stat1 = False
                                                        awal = True
                                                        modal += total
                                                        if total != 0:
                                                            akhir()
                                else:
                                    print ('')
                                    print ('Input Tidak Valid!')
                        elif pilih == '2':
                            smeubel = True
                            while (smeubel):
                                meubel = input('Jumlah Meubel Yang Ingin Dibeli : ')
                                b = meubel
                                sekb()
                                if sekb() == b:
                                    smeubel = False
                                    meubel = int(sekb())
                                    if meubel > 0:
                                        if meubel <= THP2:
                                            dmeubel()
                                            total += (dmeubel()/1000000)
                                            THP2 -= meubel
                                            jmeubel += meubel
                                            cetak()
                                            gas = True
                                            while (gas):
                                                lanjut_beli = str(input('Ingin Melanjutkan Pembelian(y/n)? '))
                                                if lanjut_beli == 'n' or lanjut_beli == 'y':
                                                    gas = False
                                                    if lanjut_beli == 'n':
                                                        stat1 = False
                                                        awal = True
                                                        modal += total
                                                        akhir()
                                                else:
                                                    print ('')
                                                    print ('Input Tidak Valid!')
                                        else:
                                            meubel_kosong()
                                            if total != 0:
                                                cetak()
                                            gas = True
                                            while (gas):
                                                lanjut_beli = str(input('Ingin Melanjutkan Pembelian(y/n)? '))
                                                if lanjut_beli == 'n' or lanjut_beli == 'y':
                                                    gas = False
                                                    if lanjut_beli == 'n':
                                                        stat1 = False
                                                        awal = True
                                                        modal += total
                                                        if total != 0:
                                                            akhir()
                                else:
                                    print ('')
                                    print ('Input Tidak Valid!')
                        elif pilih == '3':
                            spapan = True
                            while (spapan):
                                papan = input('Jumlah Papan Yang Ingin Dibeli : ')
                                b = papan
                                sekb()
                                if sekb() == b:
                                    spapan = False
                                    papan = int(sekb())
                                    if papan > 0:
                                        if papan <= THP3:
                                            dpapan()
                                            total += (dpapan()/1000000)
                                            THP3 -= papan
                                            jpapan += papan
                                            cetak()
                                            gas = True
                                            while (gas):
                                                lanjut_beli = str(input('Ingin Melanjutkan Pembelian(y/n)? '))
                                                if lanjut_beli == 'n' or lanjut_beli == 'y':
                                                    gas = False
                                                    if lanjut_beli == 'n':
                                                        stat1 = False
                                                        awal = True
                                                        modal += total
                                                        akhir()
                                                else:
                                                    print ('')
                                                    print ('Input Tidak Valid!')
                                        else:
                                            papan_kosong()
                                            if total != 0:
                                                cetak()
                                            gas = True
                                            while (gas):
                                                lanjut_beli = str(input('Ingin Melanjutkan Pembelian(y/n)? '))
                                                if lanjut_beli == 'n' or lanjut_beli == 'y':
                                                    gas = False
                                                    if lanjut_beli == 'n':
                                                        stat1 = False
                                                        awal = True
                                                        modal += total
                                                        if total != 0:
                                                            akhir()
                                else:
                                    print ('')
                                    print ('Input Tidak Valid!')
                        elif pilih == '4':
                            sbalok = True
                            while (sbalok):
                                balok = input('Jumlah Balok Yang Ingin Dibeli : ')
                                b = balok
                                sekb()
                                if sekb() == b:
                                    sbalok = False
                                    balok = int(sekb())
                                    if balok > 0:
                                        if balok <= THP4:
                                            dbalok()
                                            total += (dbalok()/1000000)
                                            THP4 -= balok
                                            jbalok += balok
                                            cetak()
                                            gas = True
                                            while (gas):
                                                lanjut_beli = str(input('Ingin Melanjutkan Pembelian(y/n)? '))
                                                if lanjut_beli == 'n' or lanjut_beli == 'y':
                                                    gas = False
                                                    if lanjut_beli == 'n':
                                                        stat1 = False
                                                        awal = True
                                                        modal += total
                                                        akhir()
                                                else:
                                                    print ('')
                                                    print ('Input Tidak Valid!')
                                        else:
                                            balok_kosong()
                                            if total != 0:
                                                cetak()
                                            gas = True
                                            while (gas):
                                                lanjut_beli = str(input('Ingin Melanjutkan Pembelian(y/n)? '))
                                                if lanjut_beli == 'n' or lanjut_beli == 'y':
                                                    gas = False
                                                    if lanjut_beli == 'n':
                                                        stat1 = False
                                                        awal = True
                                                        modal += total
                                                        if total != 0:
                                                            akhir()
                                else:
                                    print ('')
                                    print ('Input Tidak Valid!')
                        elif pilih == '9':
                            stat1 = False
                            awal = True
                        else:
                            stat1 = False
                    else:
                        print ('')
                        print ('Input Tidak Valid!')
            else:
                awal = False
        else:
            print ('Input Tidak Valid!')