import os 
import time

def reset():
    os.system('cls' if os.name == 'nt' else 'clear')


reset()
print("")
print("=== Selamat datang di Toko DONAT Kelompok 9 ===")
print("")
print("================= Daftar Menu ================= ")
print("")
print("1. Donat Keju: 4000/pcs")
print("2. Donat Coklat: 3000/pcs")
print("3. Donat Gula: 2000/pcs")
print("")
print("=================== [PROMO] ===================")
print("")
print("- beli 5 donat diskon 10%")
print("- beli 10 donat diskon 15%")
print("")
print("=================== [PAKET] ===================")
print("")
print("1. Beli 1 rasa:\n  - keju\n  - coklat\n  - gula")
print("2. Beli 2 rasa:\n  - keju coklat\n  - keju gula\n  - coklat gula")
print("3. Beli 3 rasa:\n  - keju coklat gula")
print("")
print("===============================================")
print("")
paket = int(input("Paket: "))
x = 1
while(x==1):
    print("")
    if (paket==1):
        reset()
        print("")
        print("Ket:\n-tekan 1 untuk memilih rasa Keju\n-tekan 2 untuk memilih rasa Coklat\n-tekan 3 untuk memilih rasa Gula")
        print("")
        print("===============================================")
        print("")
        menu = int(input("Rasa: "))
        print("")

        if (menu == 1):
            harga1 = 4000
            jumlah1 = (int(input("Pesan berapa Donat keju: ")))
            total1 = harga1 * jumlah1
            if (jumlah1 >=10):
                diskon = total1 * 15 / 100
                print("Harga           : Rp.", int(total1))
                print("Potongan harga  : Rp.", int(diskon))
                htot1 = total1 - diskon
                print("Total Harga     : Rp.", int(total1), "- Rp. ", int(diskon))
                print("                : Rp.",int(htot1))
                uangku = int(input("Uang Anda       : Rp. "))
                kembalian = uangku - htot1
                if (htot1 <= uangku):
                    print("Kembalian       : Rp.", int(uangku), "- Rp.", int(htot1))
                    print("                : Rp.", int(kembalian))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    time.sleep(10)
                    
                    x=0
                else:
                    print("Uang Anda Kurang: Rp.", int(kembalian))
                    print("")
                    x=0
                    time.sleep(10)
        
            elif jumlah1>=5:
                diskon = total1 * 10 / 100
                print("Harga           : Rp.", int(total1))
                print("Potongan harga  : Rp.", int(diskon))
                htot1 = total1 - diskon
                print("Total Harga     : Rp.", int(total1), "- Rp. ", int(diskon))
                print("                : Rp.",int(htot1))
                uangku = int(input("Uang Anda       : Rp. "))
                kembalian = uangku - htot1
                if (htot1 <= uangku):
                    print("Kembalian       : Rp.", int(uangku), "- Rp.", int(htot1))
                    print("                : Rp.", int(kembalian))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    x=0
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(kembalian))
                    print("")
                    x=0
                    time.sleep(10)
            else:
                print("Harga           : Rp.", int(total1))
                uangku = int(input("Uang Anda       : Rp. "))
                htot1 = uangku - total1
                if (total1 <= uangku):
                    print("Kembalian       : Rp.", int(uangku), "- Rp.", int(total1))
                    print("                : Rp.", int(htot1))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    x=0
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(htot1))
                    print("")
                    x=0
                    time.sleep(10)

        if (menu == 2):
            harga2 = 3000
            jumlah2 = (int(input("Pesan berapa Donat Coklat: ")))
            total2 = harga2 * jumlah2
            if (jumlah2 >=10):
                diskon = total2 * 15 / 100
                print("Harga           : Rp.", int(total2))
                print("Potongan harga  : Rp.", int(diskon))
                htot2 = total2 - diskon
                print("Total Harga     : Rp.", int(total2), "- Rp. ", int(diskon))
                print("                : Rp.",int(htot2))
                uangku = int(input("Uang Anda       : Rp. "))
                kembalian = uangku - htot2
                if (htot2 <= uangku):
                    print("Kembalian       : Rp.", int(uangku), "- Rp.", int(htot2))
                    print("                : Rp.", int(kembalian))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    x=0
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(kembalian))
                    print("")
                    x=0
                    time.sleep(10)
        
            elif (jumlah2>=5):
                diskon = total2 * 10 / 100
                print("Harga           : Rp.", int(total2))
                print("Potongan harga  : Rp.", int(diskon))
                htot2 = total2 - diskon
                print("Total Harga     : Rp.", int(total2), "- Rp. ", int(diskon))
                print("                : Rp.",int(htot2))
                uangku = int(input("Uang Anda       : Rp. "))
                kembalian = uangku - htot2
                if (htot2 <= uangku):
                    print("Kembalian       : Rp.", int(uangku), "- Rp.", int(htot2))
                    print("                : Rp.", int(kembalian))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    x=0
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(kembalian))
                    print("")
                    x=0
                    time.sleep(10)
            else:
                print("Harga           : Rp.", int(total2))
                uangku = int(input("Uang Anda       : Rp. "))
                htot2 = uangku - total2
                if (total2 <= uangku):
                    print("Kembalian       : Rp.", int(uangku), "- Rp.", int(total2))
                    print("                : Rp.", int(htot2))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    x=0
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(htot2))
                    print("")
                    x=0
                    time.sleep(10)

        if (menu == 3):
            harga3 = 2000
            jumlah3 = (int(input("Pesan berapa Donat Gula: ")))
            total3 = harga3 * jumlah3
            if (jumlah3 >=10):
                diskon = total3 * 15 / 100
                print("Harga           : Rp.", int(total3))
                print("Potongan harga  : Rp.", int(diskon))
                htot3 = total3 - diskon
                print("Total Harga     : Rp.", int(total3), "- Rp. ", int(diskon))
                print("                : Rp.",int(htot3))
                uangku = int(input("Uang Anda       : Rp. "))
                kembalian = uangku - htot3
                if (htot3 <= uangku):
                    print("Kembalian       : Rp.", int(uangku), "- Rp.", int(htot3))
                    print("                : Rp.", int(kembalian))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    x=0
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(kembalian))
                    print("")
                    x=0
                    time.sleep(10)
        
            elif (jumlah3>=5):
                diskon = total3 * 10 / 100
                print("Harga           : Rp.", int(total3))
                print("Potongan harga  : Rp.", int(diskon))
                htot3 = total3 - diskon
                print("Total Harga     : Rp.", int(total3), "- Rp. ", int(diskon))
                print("                : Rp.",int(htot3))
                uangku = int(input("Uang Anda       : Rp. "))
                kembalian = uangku - htot3
                if (htot3 <= uangku):
                    print("Kembalian       : Rp.", int(uangku), "- Rp.", int(htot3))
                    print("                : Rp.", int(kembalian))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    x=0
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(kembalian))
                    print("")
                    x=0
                    time.sleep(10)
            else:
                print("Harga           : Rp.", int(total3))
                uangku = int(input("Uang Anda       : Rp. "))
                htot3 = uangku - total3
                if (total3 <= uangku):
                    print("Kembalian       : Rp.", int(uangku), "- Rp.", int(total3))
                    print("                : Rp.", int(htot3))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    x=0
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(htot3))
                    print("")
                    x=0
                    time.sleep(10)

    if (paket==2):
        reset()
        print("")
        print("Ket:\n-tekan 1 untuk memilih rasa Keju Coklat\n-tekan 2 untuk memilih rasa Keju Gula\n-tekan 3 untuk memilih rasa Coklat Gula")
        print("")
        print("===============================================")
        print("")
        rasa = (int(input("Rasa: ")))
        print("")

        if(rasa==1):
            harga1 = 4000
            jumlah1 = (int(input("Pesan berapa Donat keju: ")))
            print("")
            total1 = harga1 * jumlah1
            print("")
            if (jumlah1 >= 10):
                diskon = total1 * 15 / 100
                print("Harga           : Rp.", int(total1))
                print("Potongan harga  : Rp.", int(diskon))
                htot1 = total1 - diskon
                print("Total Harga     : Rp.", int(total1), "- Rp. ", int(diskon))
                print("                : Rp.",int(htot1))
                print("")
            
            elif (jumlah1 >= 5):
                diskon = total1 * 10 / 100
                print("Harga           : Rp.", int(total1))
                print("Potongan harga  : Rp.", int(diskon))
                htot1 = total1 - diskon
                print("Total Harga     : Rp.", int(total1), "- Rp. ", int(diskon))
                print("                : Rp.",int(htot1))
                print("")

            else:
                print("Harga           : Rp.", int(total1))
                print("")

            harga2 = 3000
            jumlah2 = (int(input("Pesan berapa Donat Coklat: ")))
            print("")
            total2 = harga2 * jumlah2
            if (jumlah2 >=10):
                diskon = total2 * 15 / 100
                print("Harga           : Rp.", int(total2))
                print("Potongan harga  : Rp.", int(diskon))
                htot2 = total2 - diskon
                print("Total Harga     : Rp.", int(total2), "- Rp. ", int(diskon))
                print("                : Rp.",int(htot2))
                print("")
                x=0

            elif (jumlah2>=5):
                diskon = total2 * 10 / 100
                print("Harga           : Rp.", int(total2))
                print("Potongan harga  : Rp.", int(diskon))
                htot2 = total2 - diskon
                print("Total Harga     : Rp.", int(total2), "- Rp. ", int(diskon))
                print("                : Rp.",int(htot2))
                print("")
                x=0
            
            else:
                print("Harga           : Rp.", int(total2))
                print("")
                x=0

            listpesan=[]
            listbayar=[]

            if (jumlah1>=5 and jumlah2>=5):
                listpesan.append(jumlah1)
                listpesan.append(jumlah2)
                listbayar.append(htot1)
                listbayar.append(htot2)

                print("===============================================")
                print("")
                print("List daftar harga yang di pesan:")
                print(int(listpesan[0]), "Donat Keju   :", "Rp.", int(listbayar[0]))
                print(int(listpesan[1]), "Donat Coklat :", "Rp.", int(listbayar[1]))
                print("--------------------------")
                harga_total = htot1 + htot2
                print("Total           :", "Rp.", int(harga_total))
                uangku = int(input("Uang Anda       : Rp. "))
                kembalian = uangku - harga_total
                if (harga_total <= uangku):
                    print("Kembalian       : Rp.", int(uangku), "- Rp.", int(harga_total))
                    print("                : Rp.", int(kembalian))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(kembalian))
                    print("")
                    time.sleep(10)

            elif (jumlah1>=5 and 1<=jumlah2<=4):
                listpesan.append(jumlah1)
                listpesan.append(jumlah2)
                listbayar.append(htot1)
                listbayar.append(total2)

                print("===============================================")
                print("")
                print("List daftar harga yang di pesan:")
                print(int(listpesan[0]), "Donat Keju   :", "Rp.", int(listbayar[0]))
                print(int(listpesan[1]), "Donat Coklat  :", "Rp.", int(listbayar[1]))
                print("--------------------------")
                harga_total = htot1 + total2
                print("Total           :", "Rp.", int(harga_total))
                uangku = int(input("Uang Anda       : Rp. "))
                kembalian = uangku - harga_total
                if (harga_total <= uangku):
                    print("Kembalian       : Rp.", int(uangku), "- Rp.", int(harga_total))
                    print("                : Rp.", int(kembalian))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(kembalian))
                    print("")
                    time.sleep(10)

            elif (1<=jumlah1<=4 and jumlah2>=5):
                listpesan.append(jumlah1)
                listpesan.append(jumlah2)
                listbayar.append(total1)
                listbayar.append(htot2)

                print("===============================================")
                print("")
                print("List daftar harga yang di pesan:")
                print(int(listpesan[0]), "Donat Keju    :", "Rp.", int(listbayar[0]))
                print(int(listpesan[1]), "Donat Coklat :", "Rp.", int(listbayar[1]))
                print("--------------------------")
                harga_total = total1 + htot2
                print("Total           :", "Rp.", int(harga_total))
                uangku = int(input("Uang Anda       : Rp. "))
                kembalian = uangku - harga_total
                if (harga_total <= uangku):
                    print("Kembalian       : Rp.", int(uangku), "- Rp.", int(harga_total))
                    print("                : Rp.", int(kembalian))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(kembalian))
                    print("")
                    time.sleep(10)

            else:
                listpesan.append(jumlah1)
                listpesan.append(jumlah2)
                listbayar.append(total1)
                listbayar.append(total2)

                print("===============================================")
                print("")
                print("List daftar harga yang di pesan:")
                print(int(listpesan[0]), "Donat Keju    :", "Rp.", int(listbayar[0]))
                print(int(listpesan[1]), "Donat Coklat  :", "Rp.", int(listbayar[1]))
                print("--------------------------")
                harga_total = total1 + total2
                print("Total           :", "Rp.", int(harga_total))
                uangku = int(input("Uang Anda       : Rp. "))
                kembalian = uangku - harga_total
                if (harga_total <= uangku):
                    print("Kembalian       : Rp.", int(uangku), "- Rp.", int(harga_total))
                    print("                : Rp.", int(kembalian))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(kembalian))
                    print("")
                    time.sleep(10)
        
        if(rasa==2):
            harga1 = 4000
            jumlah1 = (int(input("Pesan berapa Donat keju: ")))
            total1 = harga1 * jumlah1
            print("")
            if (jumlah1 >= 10):
                diskon = total1 * 15 / 100
                print("Harga           : Rp.", int(total1))
                print("Potongan harga  : Rp.", int(diskon))
                htot1 = total1 - diskon
                print("Total Harga     : Rp.", int(total1), "- Rp. ", int(diskon))
                print("                : Rp.",int(htot1))
                print("")
            
            elif (jumlah1 >= 5):
                diskon = total1 * 10 / 100
                print("Harga           : Rp.", int(total1))
                print("Potongan harga  : Rp.", int(diskon))
                htot1 = total1 - diskon
                print("Total Harga     : Rp.", int(total1), "- Rp. ", int(diskon))
                print("                : Rp.",int(htot1))
                print("")

            else:
                print("Harga           : Rp.", int(total1))
                print("")

            harga3 = 2000
            jumlah3 = (int(input("Pesan berapa Donat Gula: ")))
            print("")
            total3 = harga3 * jumlah3
            if (jumlah3 >=10):
                diskon = total3 * 15 / 100
                print("Harga           : Rp.", int(total3))
                print("Potongan harga  : Rp.", int(diskon))
                htot3 = total3 - diskon
                print("Total Harga     : Rp.", int(total3), "- Rp. ", int(diskon))
                print("                : Rp.",int(htot3))
                print("")
                x=0

            elif (jumlah3>=5):
                diskon = total3 * 10 / 100
                print("Harga           : Rp.", int(total3))
                print("Potongan harga  : Rp.", int(diskon))
                htot3 = total3 - diskon
                print("Total Harga     : Rp.", int(total3), "- Rp. ", int(diskon))
                print("                : Rp.",int(htot3))
                print("")
                x=0
            
            else:
                print("Harga           : Rp.", int(total3))
                print("")
                x=0

            listpesan=[]
            listbayar=[]

            if (jumlah1>=5 and jumlah3>=5):
                listpesan.append(jumlah1)
                listpesan.append(jumlah3)
                listbayar.append(htot1)
                listbayar.append(htot3)

                print("===============================================")
                print("")
                print("List daftar harga yang di pesan:")
                print(int(listpesan[0]), "Donat Keju   :", "Rp.", int(listbayar[0]))
                print(int(listpesan[1]), "Donat Gula   :", "Rp.", int(listbayar[1]))
                print("--------------------------")
                harga_total = htot1 + htot3
                print("Total           :", "Rp.", int(harga_total))
                uangku = int(input("Uang Anda       : Rp. "))
                kembalian = uangku - harga_total
                if (harga_total <= uangku):
                    print("Kembalian       : Rp.", int(uangku), "- Rp.", int(harga_total))
                    print("                : Rp.", int(kembalian))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(kembalian))
                    print("")
                    time.sleep(10)
                
            elif (jumlah1>=5 and 1<=jumlah3<=4):
                listpesan.append(jumlah1)
                listpesan.append(jumlah3)
                listbayar.append(htot1)
                listbayar.append(total3)

                print("===============================================")
                print("")
                print("List daftar harga yang di pesan:")
                print(int(listpesan[0]), "Donat Keju   :", "Rp.", int(listbayar[0]))
                print(int(listpesan[1]), "Donat Gula    :", "Rp.", int(listbayar[1]))
                print("--------------------------")
                harga_total = htot1 + total3
                print("Total            :", "Rp.", int(harga_total))
                uangku = int(input("Uang Anda        : Rp. "))
                kembalian = uangku - harga_total
                if (harga_total <= uangku):
                    print("Kembalian        : Rp.", int(uangku), "- Rp.", int(harga_total))
                    print("                 : Rp.", int(kembalian))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(kembalian))
                    print("")
                    time.sleep(10)

            elif (1<=jumlah1<=4 and jumlah3>=5):
                listpesan.append(jumlah1)
                listpesan.append(jumlah3)
                listbayar.append(total1)
                listbayar.append(htot3)

                print("===============================================")
                print("")
                print("List daftar harga yang di pesan:")
                print(int(listpesan[0]), "Donat Keju    :", "Rp.", int(listbayar[0]))
                print(int(listpesan[1]), "Donat Gula   :", "Rp.", int(listbayar[1]))
                print("--------------------------")
                harga_total = total1 + htot3
                print("Total           :", "Rp.", int(harga_total))
                uangku = int(input("Uang Anda       : Rp. "))
                kembalian = uangku - harga_total
                if (harga_total <= uangku):
                    print("Kembalian       : Rp.", int(uangku), "- Rp.", int(harga_total))
                    print("                : Rp.", int(kembalian))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(kembalian))
                    print("")
                    time.sleep(10)
            else:
                listpesan.append(jumlah1)
                listpesan.append(jumlah3)
                listbayar.append(total1)
                listbayar.append(total3)

                print("===============================================")
                print("")
                print("List daftar harga yang di pesan:")
                print(int(listpesan[0]), "Donat Keju    :", "Rp.", int(listbayar[0]))
                print(int(listpesan[1]), "Donat Gula    :", "Rp.", int(listbayar[1]))
                print("--------------------------")
                harga_total = total1 + total3
                print("Total           :", "Rp.", int(harga_total))
                uangku = int(input("Uang Anda       : Rp. "))
                kembalian = uangku - harga_total
                if (harga_total <= uangku):
                    print("Kembalian       : Rp.", int(uangku), "- Rp.", int(harga_total))
                    print("                : Rp.", int(kembalian))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(kembalian))
                    print("")
                    time.sleep(10)
        
        if(rasa==3):
            harga2 = 3000
            jumlah2 = (int(input("Pesan berapa Donat Coklat: ")))
            total2 = harga2 * jumlah2
            print("")
            if (jumlah2 >= 10):
                diskon = total2 * 15 / 100
                print("Harga           : Rp.", int(total2))
                print("Potongan harga  : Rp.", int(diskon))
                htot2 = total2 - diskon
                print("Total Harga     : Rp.", int(total2), "- Rp. ", int(diskon))
                print("                : Rp.",int(htot2))
                print("")
            
            elif (jumlah2 >= 5):
                diskon = total2 * 10 / 100
                print("Harga           : Rp.", int(total2))
                print("Potongan harga  : Rp.", int(diskon))
                htot2 = total2 - diskon
                print("Total Harga     : Rp.", int(total2), "- Rp. ", int(diskon))
                print("                : Rp.",int(htot2))
                print("")

            else:
                print("Harga           : Rp.", int(total2))
                print("")

            harga3 = 2000
            jumlah3 = (int(input("Pesan berapa Donat Gula: ")))
            print("")
            total3 = harga3 * jumlah3
            if (jumlah3 >=10):
                diskon = total3 * 15 / 100
                print("Harga           : Rp.", int(total3))
                print("Potongan harga  : Rp.", int(diskon))
                htot3 = total3 - diskon
                print("Total Harga     : Rp.", int(total3), "- Rp. ", int(diskon))
                print("                : Rp.",int(htot3))
                print("")
                x=0

            elif (jumlah3>=5):
                diskon = total3 * 10 / 100
                print("Harga           : Rp.", int(total3))
                print("Potongan harga  : Rp.", int(diskon))
                htot3 = total3 - diskon
                print("Total Harga     : Rp.", int(total3), "- Rp. ", int(diskon))
                print("                : Rp.",int(htot3))
                print("")
                x=0
            
            else:
                print("Harga           : Rp.", int(total3))
                print("")
                x=0

            listpesan=[]
            listbayar=[]

            if (jumlah2>=5 and jumlah3>=5):
                listpesan.append(jumlah2)
                listpesan.append(jumlah3)
                listbayar.append(htot2)
                listbayar.append(htot3)

                print("===============================================")
                print("")
                print("List daftar harga yang di pesan:")
                print(int(listpesan[0]), "Donat Coklat :", "Rp.", int(listbayar[0]))
                print(int(listpesan[1]), "Donat Gula   :", "Rp.", int(listbayar[1]))
                print("--------------------------")
                harga_total = htot2 + htot3
                print("Total           :", "Rp.", int(harga_total))
                uangku = int(input("Uang Anda       : Rp. "))
                kembalian = uangku - harga_total
                if (harga_total <= uangku):
                    print("Kembalian       : Rp.", int(uangku), "- Rp.", int(harga_total))
                    print("                : Rp.", int(kembalian))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(kembalian))
                    print("")
                    time.sleep(10)

            elif (jumlah2>=5 and 1<=jumlah3<=4):
                listpesan.append(jumlah2)
                listpesan.append(jumlah3)
                listbayar.append(htot2)
                listbayar.append(total3)
                
                print("===============================================")
                print("")
                print("List daftar harga yang di pesan:")
                print(int(listpesan[0]), "Donat Coklat :", "Rp.", int(listbayar[0]))
                print(int(listpesan[1]), "Donat Gula    :", "Rp.", int(listbayar[1]))
                print("--------------------------")
                harga_total = htot2 + total3
                print("Total          :", "Rp.", int(harga_total))
                uangku = int(input("Uang Anda      : Rp. "))
                kembalian = uangku - harga_total
                if (harga_total <= uangku):
                    print("Kembalian      : Rp.", int(uangku), "- Rp.", int(harga_total))
                    print("               : Rp.", int(kembalian))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(kembalian))
                    print("")
                    time.sleep(10)

            elif (1<=jumlah2<=4 and jumlah3>=5):
                listpesan.append(jumlah2)
                listpesan.append(jumlah3)
                listbayar.append(total2)
                listbayar.append(htot3)

                print("===============================================")
                print("")
                print("List daftar harga yang di pesan:")
                print(int(listpesan[0]), "Donat Coklat   :", "Rp.", int(listbayar[0]))
                print(int(listpesan[1]), "Donat Gula    :", "Rp.", int(listbayar[1]))
                print("--------------------------")
                harga_total = total2 + htot3
                print("Total          :", "Rp.", int(harga_total))
                uangku = int(input("Uang Anda      : Rp. "))
                kembalian = uangku - harga_total
                if (harga_total <= uangku):
                    print("Kembalian      : Rp.", int(uangku), "- Rp.", int(harga_total))
                    print("               : Rp.", int(kembalian))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(kembalian))
                    print("")
                    time.sleep(10)

            else:
                listpesan.append(jumlah2)
                listpesan.append(jumlah3)
                listbayar.append(total2)
                listbayar.append(total3)

                print("===============================================")
                print("")
                print("List daftar harga yang di pesan:")
                print(int(listpesan[0]), "Donat Coklat :", "Rp.", int(listbayar[0]))
                print(int(listpesan[1]), "Donat Gula   :", "Rp.", int(listbayar[1]))
                print("--------------------------")
                harga_total = total2 + total3
                print("Total          :", "Rp.", int(harga_total))
                uangku = int(input("Uang Anda      : Rp. "))
                kembalian = uangku - harga_total
                if (harga_total <= uangku):
                    print("Kembalian      : Rp.", int(uangku), "- Rp.", int(harga_total))
                    print("               : Rp.", int(kembalian))
                    print("")
                    print("==== Terima Kasih Telah Membeli Produk Kami ====")
                    time.sleep(10)
                else:
                    print("Uang Anda Kurang: Rp.", int(kembalian))
                    print("")
                    time.sleep(10)

    if (paket==3):
        reset()
        harga1 = 4000
        jumlah1 = (int(input("Pesan berapa Donat keju: ")))
        total1 = harga1 * jumlah1
        print("")
        if (jumlah1 >= 10):
            diskon = total1 * 15 / 100
            print("Harga           : Rp.", int(total1))
            print("Potongan harga  : Rp.", int(diskon))
            htot1 = total1 - diskon
            print("Total Harga     : Rp.", int(total1), "- Rp. ", int(diskon))
            print("                : Rp.",int(htot1))
            print("")
            
        elif (jumlah1 >= 5):
            diskon = total1 * 10 / 100
            print("Harga           : Rp.", int(total1))
            print("Potongan harga  : Rp.", int(diskon))
            htot1 = total1 - diskon
            print("Total Harga     : Rp.", int(total1), "- Rp. ", int(diskon))
            print("                : Rp.",int(htot1))
            print("")

        else:
            print("Harga           : Rp.", int(total1))
            print("")

        harga2 = 3000
        jumlah2 = (int(input("Pesan berapa Donat Coklat: ")))
        total2 = harga2 * jumlah2
        print("")
        if (jumlah2 >= 10):
            diskon = total2 * 15 / 100
            print("Harga           : Rp.", int(total2))
            print("Potongan harga  : Rp.", int(diskon))
            htot2 = total2 - diskon
            print("Total Harga     : Rp.", int(total2), "- Rp. ", int(diskon))
            print("                : Rp.",int(htot2))
            print("")
        
        elif (jumlah2 >= 5):
            diskon = total2 * 10 / 100
            print("Harga           : Rp.", int(total2))
            print("Potongan harga  : Rp.", int(diskon))
            htot2 = total2 - diskon
            print("Total Harga     : Rp.", int(total2), "- Rp. ", int(diskon))
            print("                : Rp.",int(htot2))
            print("")

        else:
            print("Harga           : Rp.", int(total2))
            print("")

        harga3 = 2000
        jumlah3 = (int(input("Pesan berapa Donat Gula: ")))
        print("")
        total3 = harga3 * jumlah3
        if (jumlah3 >=10):
            diskon = total3 * 15 / 100
            print("Harga           : Rp.", int(total3))
            print("Potongan harga  : Rp.", int(diskon))
            htot3 = total3 - diskon
            print("Total Harga     : Rp.", int(total3), "- Rp. ", int(diskon))
            print("                : Rp.", int(htot3))
            print("")
            x=0

        elif (jumlah3>=5):
            diskon = total3 * 10 / 100
            print("Harga           : Rp.", int(total3))
            print("Potongan harga  : Rp.", int(diskon))
            htot3 = total3 - diskon
            print("Total Harga     : Rp.", int(total3), "- Rp. ", int(diskon))
            print("                : Rp.", int(htot3))
            print("")
            x=0
            
        else:
            print("Harga           : Rp.", int(total3))
            print("")
            x=0

        listpesan=[]
        listbayar=[]

        if (jumlah1>=5 and jumlah2>=5 and jumlah3>=5):
            listpesan.append(jumlah1)
            listpesan.append(jumlah2)
            listpesan.append(jumlah3)
            listbayar.append(htot1)
            listbayar.append(htot2)
            listbayar.append(htot3)

            print("===============================================")
            print("")
            print("List daftar harga yang di pesan:")
            print(int(listpesan[0]), "Donat Keju    :", "Rp.", int(listbayar[0]))
            print(int(listpesan[1]), "Donat Coklat  :", "Rp.", int(listbayar[1]))
            print(int(listpesan[2]), "Donat Gula    :", "Rp.", int(listbayar[2]))
            print("-----------------------------")
            harga_total = htot1 + htot2 + htot3
            print("Total            :", "Rp.", int(harga_total))
            uangku = int(input("Uang Anda        : Rp. "))
            kembalian = uangku - harga_total
            if (harga_total <= uangku):
                print("Kembalian        : Rp.", int(uangku), "- Rp.", int(harga_total))
                print("                 : Rp.", int(kembalian))
                print("")
                print("==== Terima Kasih Telah Membeli Produk Kami ====")
                time.sleep(10)
            else:
                print("Uang Anda Kurang: Rp.", int(kembalian))
                print("")
                time.sleep(10)


        elif (jumlah1>=5 and jumlah2>=5 and 1<=jumlah3<=4):
            listpesan.append(jumlah1)
            listpesan.append(jumlah2)
            listpesan.append(jumlah3)
            listbayar.append(htot1)
            listbayar.append(htot2)
            listbayar.append(total3)

            print("===============================================")
            print("")
            print("List daftar harga yang di pesan:")
            print(int(listpesan[0]), "Donat Keju   :", "Rp.", int(listbayar[0]))
            print(int(listpesan[1]), "Donat Coklat  :", "Rp.", int(listbayar[1]))
            print(int(listpesan[2]), "Donat Gula    :", "Rp.", int(listbayar[2]))
            print("-----------------------------")
            harga_total = htot1 + htot2 + total3
            print("Total           :", "Rp.", int(harga_total))
            uangku = int(input("Uang Anda       : Rp. "))
            kembalian = uangku - harga_total
            if (harga_total <= uangku):
                print("Kembalian       : Rp.", int(uangku), "- Rp.", int(harga_total))
                print("                : Rp.", int(kembalian))
                print("")
                print("==== Terima Kasih Telah Membeli Produk Kami ====")
                time.sleep(10)
            else:
                print("Uang Anda Kurang: Rp.", int(kembalian))
                print("")
                time.sleep(10)

        elif (1<=jumlah1<=4 and jumlah2>=5 and jumlah3>=5):
            listpesan.append(jumlah1)
            listpesan.append(jumlah2)
            listpesan.append(jumlah3)
            listbayar.append(total1)
            listbayar.append(htot2)
            listbayar.append(htot3)

            print("===============================================")
            print("")
            print("List daftar harga yang di pesan:")
            print(int(listpesan[0]), "Donat Keju    :", "Rp.", int(listbayar[0]))
            print(int(listpesan[1]), "Donat Coklat :", "Rp.", int(listbayar[1]))
            print(int(listpesan[2]), "Donat Gula   :", "Rp.", int(listbayar[2]))
            print("-----------------------------")
            harga_total = total1 + htot2 + htot3
            print("Total           :", "Rp.", int(harga_total))
            uangku = int(input("Uang Anda       : Rp. "))
            kembalian = uangku - harga_total
            if (harga_total <= uangku):
                print("Kembalian       : Rp.", int(uangku), "- Rp.", int(harga_total))
                print("                : Rp.", int(kembalian))
                print("")
                print("==== Terima Kasih Telah Membeli Produk Kami ====")
                time.sleep(10)
            else:
                print("Uang Anda Kurang: Rp.", int(kembalian))
                print("")
                time.sleep(10)

        elif (jumlah1>=5 and 1<=jumlah2<=4 and jumlah3>=5):
            listpesan.append(jumlah1)
            listpesan.append(jumlah2)
            listpesan.append(jumlah3)
            listbayar.append(htot1)
            listbayar.append(total2)
            listbayar.append(htot3)

            print("===============================================")
            print("")
            print("List daftar harga yang di pesan:")
            print(int(listpesan[0]), "Donat Keju   :", "Rp.", int(listbayar[0]))
            print(int(listpesan[1]), "Donat Coklat  :", "Rp.", int(listbayar[1]))
            print(int(listpesan[2]), "Donat Gula   :", "Rp.", int(listbayar[2]))
            print("-----------------------------")
            harga_total = htot1 + total2 + htot3
            print("Total           :", "Rp.", int(harga_total))
            uangku = int(input("Uang Anda       : Rp. "))
            kembalian = uangku - harga_total
            if (harga_total <= uangku):
                print("Kembalian       : Rp.", int(uangku), "- Rp.", int(harga_total))
                print("                : Rp.", int(kembalian))
                print("")
                print("==== Terima Kasih Telah Membeli Produk Kami ====")
                time.sleep(10)
            else:
                print("Uang Anda Kurang: Rp.", int(kembalian))
                print("")
                time.sleep(10)

        elif (jumlah1>=5 and 1<=jumlah2<=4 and 1<=jumlah3<=4):
            listpesan.append(jumlah1)
            listpesan.append(jumlah2)
            listpesan.append(jumlah3)
            listbayar.append(htot1)
            listbayar.append(total2)
            listbayar.append(total3)

            print("===============================================")
            print("")
            print("List daftar harga yang di pesan:")
            print(int(listpesan[0]), "Donat Keju   :", "Rp.", int(listbayar[0]))
            print(int(listpesan[1]), "Donat Coklat  :", "Rp.", int(listbayar[1]))
            print(int(listpesan[2]), "Donat Gula    :", "Rp.", int(listbayar[2]))
            print("-----------------------------")
            harga_total = htot1 + total2 + total3
            print("Total           :", "Rp.", int(harga_total))
            uangku = int(input("Uang Anda       : Rp. "))
            kembalian = uangku - harga_total
            if (harga_total <= uangku):
                print("Kembalian       : Rp.", int(uangku), "- Rp.", int(harga_total))
                print("                : Rp.", int(kembalian))
                print("")
                print("==== Terima Kasih Telah Membeli Produk Kami ====")
                time.sleep(10)
            else:
                print("Uang Anda Kurang: Rp.", int(kembalian))
                print("")
                time.sleep(10)

        elif (1<=jumlah1<=4 and jumlah2>=5 and 1<=jumlah3<=4):
            listpesan.append(jumlah1)
            listpesan.append(jumlah2)
            listpesan.append(jumlah3)
            listbayar.append(total1)
            listbayar.append(htot2)
            listbayar.append(total3)

            print("===============================================")
            print("")
            print("List daftar harga yang di pesan:")
            print(int(listpesan[0]), "Donat Keju    :", "Rp.", int(listbayar[0]))
            print(int(listpesan[1]), "Donat Coklat :", "Rp.", int(listbayar[1]))
            print(int(listpesan[2]), "Donat Gula    :", "Rp.", int(listbayar[2]))
            print("-----------------------------")
            harga_total = total1 + htot2 + total3
            print("Total           :", "Rp.", int(harga_total))
            uangku = int(input("Uang Anda       : Rp. "))
            kembalian = uangku - harga_total
            if (harga_total <= uangku):
                print("Kembalian       : Rp.", int(uangku), "- Rp.", int(harga_total))
                print("                : Rp.", int(kembalian))
                print("")
                print("==== Terima Kasih Telah Membeli Produk Kami ====")
                time.sleep(10)
            else:
                print("Uang Anda Kurang: Rp.", int(kembalian))
                print("")
                time.sleep(10)

        elif (1<=jumlah1<=4 and 1<=jumlah2<=4 and jumlah3>=5):
            listpesan.append(jumlah1)
            listpesan.append(jumlah2)
            listpesan.append(jumlah3)
            listbayar.append(total1)
            listbayar.append(total2)
            listbayar.append(htot3)

            print("===============================================")
            print("")
            print("List daftar harga yang di pesan:")
            print(int(listpesan[0]), "Donat Keju    :", "Rp.", int(listbayar[0]))
            print(int(listpesan[1]), "Donat Coklat  :", "Rp.", int(listbayar[1]))
            print(int(listpesan[2]), "Donat Gula   :", "Rp.", int(listbayar[2]))
            print("-----------------------------")
            harga_total = total1 + total2 + htot3
            print("Total           :", "Rp.", int(harga_total))
            uangku = int(input("Uang Anda       : Rp. "))
            kembalian = uangku - harga_total
            if (harga_total <= uangku):
                print("Kembalian       : Rp.", int(uangku), "- Rp.", int(harga_total))
                print("                : Rp.", int(kembalian))
                print("")
                print("==== Terima Kasih Telah Membeli Produk Kami ====")
                time.sleep(10)
            else:
                print("Uang Anda Kurang: Rp.", int(kembalian))
                print("")
                time.sleep(10)

        else:
            listpesan.append(jumlah1)
            listpesan.append(jumlah2)
            listpesan.append(jumlah3)
            listbayar.append(total1)
            listbayar.append(total2)
            listbayar.append(total3)

            print("===============================================")
            print("")
            print("List daftar harga yang di pesan:")
            print(int(listpesan[0]), "Donat Keju    :", "Rp.", int(listbayar[0]))
            print(int(listpesan[1]), "Donat Coklat  :", "Rp.", int(listbayar[1]))
            print(int(listpesan[2]), "Donat Gula    :", "Rp.", int(listbayar[2]))
            print("-----------------------------")
            harga_total = total1 + total2 + total3
            print("Total           :", "Rp.", int(harga_total))
            uangku = int(input("Uang Anda       : Rp. "))
            kembalian = uangku - harga_total
            if (harga_total <= uangku):
                print("Kembalian       : Rp.", int(uangku), "- Rp.", int(harga_total))
                print("                : Rp.", int(kembalian))
                print("")
                print("==== Terima Kasih Telah Membeli Produk Kami ====")
                time.sleep(10)
            else:
                print("Uang Anda Kurang: Rp.", int(kembalian))
                print("")
                time.sleep(10)