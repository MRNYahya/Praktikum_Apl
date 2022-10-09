import os

hargacan = [85000, 65000, 50000, 35000, 30000]
hargabr = [8000, 7500, 8000, 6000, 6500, 7500, 9000, 50000]
hargasketch = [22000, 17500]
hargasketch1 = [129000, 70000]
hargapalet = [11000, 7000]
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def keluar():
    clear_screen()
    print("+====================================================+")
    print("|       Terima Kasih telah membuka program ini       |")
    print("+====================================================+")
    input("                   Tekan enter")
    exit()

def keluar_menu():
    clear_screen()
    print("+=========================================================+")
    print("|       Terima kasih sudah menggunakan program ini        |")
    print("|                   Have a Good Day !                     |")
    print("+=========================================================+")
    input("                     Tekan enter")
    exit()


def menu_login():
    clear_screen()
    print("+====================================================+")
    print("|     Mode manakah yang ingin Anda gunakan untuk     |")
    print("|               mengakses program ini?               |")
    print("|                                                    |")
    print("|  [A] Customer                                      |")
    print("|  [B] Admin                                         |")
    print("|  [C] Keluar                                        |")
    print("+====================================================+")
    Login = str(input("|  Mode : "))

    if (Login == "A" or Login == "a"):
        menu_akun()
    elif (Login == "B" or Login == "b"):
        print("|        Masukkan Username dan Password Anda         |")
        print("+====================================================+")
        k = 3 
        while k > 0:
            Username = str(input("| Username : "))
            Password = str(input("| Password : "))
            if (Username == "Choco" and Password == "late"):
                menu_admin()
            else:
                k -= 1
                print("| Usename dan Password Salah | Sisa kesempatan :", k)
                if k == 0:
                    print("|            Kesempatan Anda telah habis             |") 
                    print("|        Silahkan menebak ulang passwordnya :)       |")
                    print("+====================================================+")
                    input("                  Tekan Enter")
                    menu_login()

    elif (Login == "C"):
        keluar()
    else:
        print("|       Inputan Anda salah, silahkan coba lagi       |")
        print("|                     Tekan enter                    |")
        print("+====================================================+")
        input("")
        menu_login()

def menu_admin():
    clear_screen()
    print("+=====================================================+")
    print("|           Anda telah login sebagai Admin            |")
    print("|                      (O w O)                        |")
    print("|       Perintah mana yang ingin Anda jalankan ?      |")
    print("|  [1] Lihat Data                                     |")
    print("|  [2] Cari Data                                      |")
    print("|  [3] Update Data                                    |")
    print("|  [4] Delete Data                                    |")
    print("|  [5] Log out                                        |")
    print("|  [0] Exit                                           |")
    print("+=====================================================+")
    admin = str(input("| Pilihan : "))

    if (admin == "1"):
        lihat_data()
    elif (admin == "2"):
        def linearSearch(array,n,x):
            for i in range(0,n):
                if(array[i] == x):
                    return i
            return -1

        clear_screen()
        print("+=============================================+")
        print("|            Cari Data Pengunjung             |")
        print("+=============================================+")
        x = input("| Masukkan data : ")
        n = len(pengunjung["orang"][0])

        for i in range(n):
            result = linearSearch(pengunjung["orang"][i], n, x)
            if result != -1:
                print(f"\n| Data berada pada identitas ke-{i+1}, indeks ke-{result}")
                break
        if result == -1:
            print("Element Not found")

        print("+=============================================+")
        print("|          Tekan Enter untuk Kembali          |")
        input("+=============================================+")
        menu_admin()
    elif (admin == "3"):
        update_data()
    elif (admin == "4"):
        delete_data()
    elif (admin == "5"):
        menu_login()
    elif (admin == "0"):
        keluar_menu()
    else:
        print("Anda menginput pilihan yang salah, silahkan coba kembali...")
        input("                   Tekan enter             ")
        menu_admin()

def lihat_data():
    clear_screen()
    print("+=============================================+")
    print("|               Data Pengunjung               |")
    print("+=============================================+")
    for i in range (len(pengunjung["orang"])):
       print("| Nama : ",(pengunjung["orang"][i][0]))
       print("| Umur : ",(pengunjung["orang"][i][1]))
       print("| Alamat : ",(pengunjung["orang"][i][2]))
       print("| Email : ",(pengunjung["orang"][i][3]),"\n")

    print()
    input("             Tekan Untuk Kembali")
    menu_admin()

def update_data():
    clear_screen()
    print("+===================================================+")
    print("|                   Update Data                     |")
    print("+===================================================+")
    y = int(input("| Input Indeks Data Yang Ingin Di Update :"))
    
    print("| Masukkan Data Yang Akan diUpdate                  |")
    nama = str(input("| Nama : "))
    umur = str(input("| Umur : "))
    alamat = str(input("| Alamat : "))
    email = str(input("| Email : "))
    pengunjung["orang"][y] = [nama, umur, alamat, email]
    
    for i in pengunjung["orang"]:
        print(i)   
        
    input("  Data telah diupdate, tekan Enter Untuk Kembali")
    menu_admin()

def delete_data():
    clear_screen()
    print("+=============================================+")
    print("|                 Delete Data                 |")
    print("+=============================================+")
    for i in range (len(pengunjung["orang"])):
        print("| Nama : ",(pengunjung["orang"][i][0]))
        print("| Umur : ",(pengunjung["orang"][i][1]))
        print("| Alamat : ",(pengunjung["orang"][i][2]))
        print("| Email : ",(pengunjung["orang"][i][3]),"\n")

    y = int(input("Hapus indeks ke : "))
    del pengunjung["orang"][y]
    print("+=============================================+")
    input("          Tekan Enter untuk kembali           ")
    menu_admin()

pengunjung = {"orang":[]}
def menu_akun():
    clear_screen()
    print("+==================================================+")
    print("|           Silahkan masukkan akun Anda            |")
    print("|                                                  |")
    nama = str(input("| Nama : "))
    umur = str(input("| Umur : "))
    alamat = str(input("| Alamat : "))
    email = str(input("| Email : "))

    pengunjung["orang"].append([nama, umur, alamat, email])

    for k in pengunjung["orang"]:
        print(k)
    
    print("|             Akun Anda telah terbuat             |")
    print("|          Tekan Enter Untuk Melanjutkan          |")
    print("+=================================================+")
    input(" ")
    menu_customer()
      
def menu_customer():
    clear_screen()
    print("+==================================================+")
    print("|             Welcome to Cia Art Suply             |")
    print("|                    ( > o <)                      |")
    print("|   Kami menyediakan berbagai macam perlengkapan,  |")
    print("|  dan keperluan untuk membuat karya seni lainnya. |")
    print("+==================================================+")
    print("|               Silahkan berbelanja !              |")
    print("|  Berikut daftar - daftar barang yang tersedia :  |")
    print("|  [1] Paint                                       |")
    print("|  [2] Brush                                       |")
    print("|  [3] Canvas                                      |")
    print("|  [4] Books (for art)                             |")
    print("|  [5] Pallet                                      |")
    print("|  [6] List harga barang - barang                  |")
    print("|  [7] Kembali                                     |")
    print("|  [0] Keluar                                      |")
    print("+==================================================+")
    barang = str(input("=  Pilihan : "))
    
    if (barang == "1"):
        menu_paint()
    elif (barang == "2"):
        menu_brush()
    elif (barang == "3"):
        menu_canvas()
    elif (barang == "4"):
        menu_books()
    elif (barang == "5"):
        menu_palet()
    elif (barang == "6"):
        list_harga()
    elif (barang == "7"):
        menu_login()
    elif (barang == "0"):
        keluar()
    else:
        print("Inputan Anda salah, silahkan coba lagi ya (O w O)")
        input("                Tekan enter...")
        menu_customer()

def list_harga():
    clear_screen()
    print("+=========================================================+")
    print("|       Silahkan pilih barang yang ingin Anda list        |")
    print("|                        ( > w < )                        |")
    print("|  [1] Paint                                              |")
    print("|  [2] Brush                                              |")
    print("|  [3] Canvas                                             |")
    print("|  [4] Books (for art)                                    |")
    print("|  [5] Pallet                                             |")
    print("|  [6] Kembali                                            |")
    print("|  [0] Keluar                                             |")
    print("+=========================================================+")
    menu = str(input("=  Barang : "))

    if (menu == "1"):
        mm_paint()
    elif (menu == "2"):
        mm_brush()
    elif (menu == "3"):
        mm_canvas()
    elif (menu == "4"):
        mm_books()
    elif (menu == "5"):
        mm_palet()
    elif (menu == "6"):
        menu_customer()
    elif (menu == "0"):
        print("|       Terima kasih telah menggunakan program ini        |")
        print("|                    Have a good day !                    |")
        print("+=========================================================+")
        input("                      Tekan Enter...")
        exit()
    else:
        print("|          Inputan Anda salah, mohon input ulang          |")
        print("|                         (x _ x)                         |")
        print("+=========================================================+")
        input("                       Tekan Enter...")
        list_harga()

def mm_paint():
    clear_screen()
    print("+=============================================================+")
    print("|                                                             |")
    print("|   Untuk menu paint, semua warna memiliki harga yang sama    |")
    print("|         sesuai dengan jenis catnya masing - masing          |")
    print("|                                                             |")
    print("|              Cat Minyak   = Rp 18000 / 1 pcs                |")
    print("|              Cat Air      = Rp 7000 / 1 pcs                 |")
    print("|              Cat Akrilik  = Rp 10000 / 1 pcs                |")
    print("|              Cat Poster   = Rp 16000 / 1 pcs                |")
    print("+=============================================================+")
    input("               Tekan Enter untuk kembali...")
    list_harga()

def partitionAscending(array, rendah, tinggi):
    pivot = array[tinggi]
    i = rendah - 1
    
    for j in range(rendah, tinggi):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[tinggi]) = (array[tinggi], array[i + 1])
    return i + 1

def quickSortAscending(array, rendah, tinggi):
    if rendah < tinggi:
        pi = partitionAscending(array, rendah, tinggi)
        quickSortAscending(array, rendah, pi - 1)
        quickSortAscending(array, pi + 1, tinggi)

def partitionDescending(array, rendah, tinggi):
    pivot = array[tinggi]
    i = rendah - 1
    
    for j in range(rendah, tinggi):
        if array[j] >= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[tinggi]) = (array[tinggi], array[i + 1])
    return i + 1

def quickSortDescending(array, rendah, tinggi):
    if rendah < tinggi:
        pi = partitionDescending(array, rendah, tinggi)
        quickSortDescending(array, rendah, pi - 1)
        quickSortDescending(array, pi + 1, tinggi)

def mm_brush():
    clear_screen()
    print("+=============================================================+")
    print("|            List manakah yang ingin Anda pilih ?             |")
    print("|                                                             |")
    print("|  [1] Ascending                                              |")
    print("|  [2] Descending                                             |")
    print("|  [3] Kembali                                                |")
    print("|  [0] Keluar                                                 |")
    print("+=============================================================+")
    lalalala = str(input("|  Jenis list : "))

    if (lalalala == "1"):
        mm_brushAsc()
    elif (lalalala == "2"):
        mm_brushDesc()
    elif (lalalala == "3"):
        list_harga()
    elif (lalalala == "0"):
        print("|        Terima kasih telah menggunakan program ini !         |")
        print("|                       Tekan Enter...                        |")
        print("+=============================================================+")
        input("   ")
        exit()
    else:
        print("       Input Anda salah, tekan enter untuk coba ulang")
        print("                          <===>")
        input("                            ")
        mm_brush()

def mm_brushAsc():
    clear_screen()
    size = len(hargabr)
    quickSortAscending(hargabr, 0, size - 1)
    print("+=============================================================+")
    print("|                       < Menu Brush >                        |")
    print("|                                                             |")
    print("|              List Harga Brush secara Ascending :            |")
    print("|      ",hargabr ,"    |")
    print("|                                                             |")
    print("+=============================================================+")
    print("                   Tekan Enter untuk kembali")
    input("  ")
    list_harga()

def mm_brushDesc():
    clear_screen()
    size = len(hargabr)
    quickSortDescending(hargabr, 0, size - 1)
    print("+=============================================================+")
    print("|                       < Menu Brush >                        |")
    print("|                                                             |")
    print("|              List Harga Brush secara Descending :           |")
    print("|      ",hargabr ,"    |")
    print("|                                                             |")
    print("+=============================================================+")
    print("                   Tekan Enter untuk kembali")
    input("  ")
    list_harga()

def mm_canvas():
    clear_screen()
    print("+=============================================================+")
    print("|            List manakah yang ingin Anda pilih ?             |")
    print("|                                                             |")
    print("|  [1] Ascending                                              |")
    print("|  [2] Descending                                             |")
    print("|  [3] Kembali                                                |")
    print("|  [0] Keluar                                                 |")
    print("+=============================================================+")
    lalalala = str(input("|  Jenis list : "))

    if (lalalala == "1"):
        mm_canvasAsc()
    elif (lalalala == "2"):
        mm_brushDesc()
    elif (lalalala == "3"):
        list_harga()
    elif (lalalala == "0"):
        print("|        Terima kasih telah menggunakan program ini !         |")
        print("|                       Tekan Enter...                        |")
        print("+=============================================================+")
        input("   ")
        exit()
    else:
        print("       Input Anda salah, tekan enter untuk coba ulang")
        print("                          <===>")
        input("                            ")
        mm_canvas()


def mm_canvasAsc():
    clear_screen()
    size = len(hargacan)
    quickSortAscending(hargacan, 0, size - 1)
    print("+=============================================================+")
    print("|                       < Menu Canvas >                       |")
    print("|                                                             |")
    print("|              List Harga Canvas Secara Ascending :           |")
    print("|             ", hargacan,"           |")
    print("|                                                             |")
    print("+=============================================================+")
    print("                   Tekan Enter untuk kembali")
    input("  ")
    list_harga()

def mm_canvasDesc():
    clear_screen()
    size = len(hargacan)
    quickSortDescending(hargacan, 0, size - 1)
    print("+=============================================================+")
    print("|                       < Menu Canvas >                       |")
    print("|                                                             |")
    print("|              List Harga Canvas Secara Descending :          |")
    print("|             ", hargacan,"           |")
    print("|                                                             |")
    print("+=============================================================+")
    print("                   Tekan Enter untuk kembali")
    input("  ")
    list_harga()

def mm_books():
    clear_screen()
    print("+=============================================================+")
    print("|            Buku manakah yang Anda ingin pilih ?             |")
    print("|                                                             |")
    print("|  [1] Sketchbook                                             |")
    print("|  [2] Watercolor Book                                        |")
    print("|  [3] Kembali                                                |")
    print("|  [0] Keluar                                                 |")
    print("+=============================================================+")
    lalalala = str(input("=  Tipe buku : "))

    if (lalalala == "1"):
        Sketchbook_1()
    elif (lalalala == "2"):
        watercolor_1()
    elif (lalalala == "3"):
        list_harga()
    elif (lalalala == "0"):
        print("|        Terima kasih telah menggunakan program ini !         |")
        print("|                       Tekan Enter...                        |")
        print("+=============================================================+")
        input("   ")
        exit()
    else:
        print("       Input Anda salah, tekan enter untuk coba ulang")
        print("                          <===>")
        input("                            ")
        mm_books()

def Sketchbook_1():
    clear_screen()
    print("+=============================================================+")
    print("|            List manakah yang ingin Anda pilih ?             |")
    print("|                                                             |")
    print("|  [1] Ascending                                              |")
    print("|  [2] Descending                                             |")
    print("|  [3] Kembali                                                |")
    print("|  [0] Keluar                                                 |")
    print("+=============================================================+")
    lalalala = str(input("|  Jenis list : "))

    if (lalalala == "1"):
        sketchAsc()
    elif (lalalala == "2"):
        sketchDesc()
    elif (lalalala == "3"):
        mm_books()
    elif (lalalala == "0"):
        print("|        Terima kasih telah menggunakan program ini !         |")
        print("|                       Tekan Enter...                        |")
        print("+=============================================================+")
        input("   ")
        exit()
    else:
        print("       Input Anda salah, tekan enter untuk coba ulang")
        print("                          <===>")
        input("                            ")
        Sketchbook_1()

def sketchAsc():
    clear_screen()
    size = len(hargasketch)
    quickSortAscending(hargasketch, 0, size - 1)
    print("+=============================================================+")
    print("|                      < Menu Sketchbook >                    |")
    print("|                                                             |")
    print("|                 List Harga Secara Ascending :               |")
    print("|                        ",hargasketch , "                     |")
    print("|                                                             |")
    print("+=============================================================+")
    print("                   Tekan Enter untuk kembali")
    input("  ")
    list_harga()

def sketchDesc():
    clear_screen()
    size = len(hargasketch)
    quickSortDescending(hargasketch, 0, size - 1)
    print("+=============================================================+")
    print("|                      < Menu Sketchbook >                    |")
    print("|                                                             |")
    print("|                List Harga Secara Descending :               |")
    print("|                        ",hargasketch , "                     |")
    print("|                                                             |")
    print("+=============================================================+")
    print("                   Tekan Enter untuk kembali")
    input("  ")
    list_harga()

def watercolor_1():
    clear_screen()
    print("+=============================================================+")
    print("|            List manakah yang ingin Anda pilih ?             |")
    print("|                                                             |")
    print("|  [1] Ascending                                              |")
    print("|  [2] Descending                                             |")
    print("|  [3] Kembali                                                |")
    print("|  [0] Keluar                                                 |")
    print("+=============================================================+")
    lalalala = str(input("|  Jenis list : "))

    if (lalalala == "1"):
        waterAsc()
    elif (lalalala == "2"):
        sketchDesc()
    elif (lalalala == "3"):
        mm_books()
    elif (lalalala == "0"):
        print("|        Terima kasih telah menggunakan program ini !         |")
        print("|                       Tekan Enter...                        |")
        print("+=============================================================+")
        input("   ")
        exit()
    else:
        print("       Input Anda salah, tekan enter untuk coba ulang")
        print("                          <===>")
        input("                            ")
        watercolor_1()

def waterAsc():
    clear_screen()
    size = len(hargasketch1)
    quickSortAscending(hargasketch1, 0, size - 1)
    print("+=============================================================+")
    print("|                   < Menu Watercolor book >                  |")
    print("|                                                             |")
    print("|        List Harga Watercolor Book Secara Ascending :        |")
    print("|                     ", hargasketch1,"                       |")
    print("|                                                             |")
    print("+=============================================================+")
    print("                   Tekan Enter untuk kembali")
    input("  ")
    list_harga()

def waterDesc():
    clear_screen()
    size = len(hargasketch1)
    quickSortDescending(hargasketch1, 0, size - 1)
    print("+=============================================================+")
    print("|                   < Menu Watercolor book >                  |")
    print("|                                                             |")
    print("|        List Harga Watercolor Book Secara Descending :       |")
    print("|                     ", hargasketch1,"                       |")
    print("|                                                             |")
    print("+=============================================================+")
    print("                   Tekan Enter untuk kembali")
    input("  ")
    list_harga()

def mm_palet():
    clear_screen()
    print("+=============================================================+")
    print("|            List manakah yang ingin Anda pilih ?             |")
    print("|                                                             |")
    print("|  [1] Ascending                                              |")
    print("|  [2] Descending                                             |")
    print("|  [3] Kembali                                                |")
    print("|  [0] Keluar                                                 |")
    print("+=============================================================+")
    lalalala = str(input("|  Jenis list : "))

    if (lalalala == "1"):
        paletAsc()
    elif (lalalala == "2"):
        paletDesc()
    elif (lalalala == "3"):
        list_harga()
    elif (lalalala == "0"):
        print("|        Terima kasih telah menggunakan program ini !         |")
        print("|                       Tekan Enter...                        |")
        print("+=============================================================+")
        input("   ")
        exit()
    else:
        print("       Input Anda salah, tekan enter untuk coba ulang")
        print("                          <===>")
        input("                            ")
        mm_palet()

def paletAsc():
    clear_screen()
    size = len(hargapalet)
    quickSortAscending(hargapalet, 0, size - 1)
    print("+=============================================================+")
    print("|                        < Menu Palet >                       |")
    print("|                                                             |")
    print("|            List Harga Palet Secara Ascending :              |")
    print("|                      ", hargapalet,"                        |")
    print("|                                                             |")
    print("+=============================================================+")
    print("                   Tekan Enter untuk kembali")
    input("  ")
    list_harga()

def paletDesc():
    clear_screen()
    size = len(hargapalet)
    quickSortDescending(hargapalet, 0, size - 1)
    print("+=============================================================+")
    print("|                        < Menu Palet >                       |")
    print("|                                                             |")
    print("|            List Harga Palet Secara Descending :             |")
    print("|                      ", hargapalet,"                        |")
    print("|                                                             |")
    print("+=============================================================+")
    print("                   Tekan Enter untuk kembali")
    input("  ")
    list_harga()

def menu_paint():
    clear_screen()
    print("+=========================================================+")
    print("|           Cat tipe apa yang Anda butuhkan ?             |")
    print("|                        (^__^)                           |")
    print("|  [1] Cat Minyak                                         |")
    print("|  [2] Cat Air                                            |")
    print("|  [3] Cat Akrilik                                        |")
    print("|  [4] Cat Poster                                         |")
    print("|  [5] Kembali                                            |")
    print("|  [0] Keluar                                             |")
    print("+=========================================================+")
    paint = str(input("=  Tipe Cat : "))

    if (paint == "1"):
        cat_minyak()
    elif (paint == "2"):
        cat_air()
    elif (paint == "3"):
        cat_akrilik()
    elif (paint == "4"):
        cat_poster()
    elif (paint == "5"):
        menu_customer()
    elif (paint == "0"):
        keluar_menu()
    else:
        print("         Mohon maaf, inputan Anda salah...          ")
        input("               === Tekan Enter ===                  ")
        menu_paint()


ho = [18000,190000]
def cat_minyak():
    clear_screen()
    print("+=========================================================+")
    print("|           Warna apa saja yang Anda butuhkan ?           |")
    print("|              Semua cat ini berukuran 50 ml              |")
    print("|                                                         |")
    print("|  [1] White : Rp", ho[0],"                                  |")
    print("|  [2] Yellow : Rp", ho[0],"                                 |")
    print("|  [3] Light Sand : Rp", ho[0],"                             |")
    print("|  [4] Orange : Rp", ho[0],"                                 |")
    print("|  [5] Red : Rp", ho[0],"                                    |")
    print("|  [6] Light Green : Rp", ho[0],"                            |")
    print("|  [7] Green : Rp", ho[0],"                                  |")
    print("|  [8] Light Blue : Rp", ho[0],"                             |")
    print("|  [9] Blue : Rp", ho[0],"                                   |")
    print("|  [10] Brown : Rp", ho[0],"                                 |")
    print("|  [11] Black : Rp", ho[0],"                                 |")
    print("|  [12] Paket warna isi 11 + 1 kuas : Rp", ho[1],"          |")
    print("|  [13] Kembali                                           |")
    print("|  [0] Keluar                                             |")
    print("+=========================================================+")
    minyak = str(input("=  Warna Cat : "))

    if (minyak == "1"):
        minyak_putih()
    elif (minyak == "2"):
        minyak_kuning()
    elif (minyak == "3"):
        minyak_lightsand()
    elif (minyak == "4"):
        minyak_orange()
    elif (minyak == "5"):
        minyak_red()
    elif (minyak == "6"):
        minyak_lightgreen()
    elif (minyak == "7"):
        minyak_green()
    elif (minyak == "8"):
        minyak_lightblue()
    elif (minyak == "9"):
        minyak_blue()
    elif (minyak == "10"):
        minyak_brown()
    elif (minyak == "11"):
        minyak_black()
    elif (minyak == "12"):
        paket_minyak()
    elif (minyak == "13"):
        menu_paint()
    elif (minyak == "0"):
        keluar_menu()
    else:
        print("         Mohon maaf, inputan Anda salah...          ")
        input("               === Tekan Enter ===                  ")
        cat_minyak()

def minyak_putih():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|                                                         |")
    hargao1 = int(input("|   Jumlah cat : "))

    putih = ho[0]*hargao1
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", ho[0], "*", hargao1, "= Rp", putih, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def minyak_kuning():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|                                                         |")
    hargao2 = int(input("|   Jumlah cat : "))

    kuning = ho[0]*hargao2
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", ho[0], "*", hargao2, "= Rp", kuning, "                              |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def minyak_lightsand():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|                                                         |")
    hargao3 = int(input("|   Jumlah cat : "))

    lightsand = ho[0]*hargao3
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", ho[0], "*", hargao3, "= Rp", lightsand, "                              |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def minyak_orange():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|                                                         |")
    hargao4 = int(input("|   Jumlah cat : "))

    orange = ho[0]*hargao4
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", ho[0], "*", hargao4, "= Rp", orange, "                              |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def minyak_red():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|                                                         |")
    hargao5 = int(input("|   Jumlah cat : "))

    red = ho[0]*hargao5
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", ho[0], "*", hargao5, "= Rp", red, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def minyak_lightgreen():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|                                                         |")
    hargao6 = int(input("|   Jumlah cat : "))

    lightgreen = ho[0]*hargao6
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", ho[0], "*", hargao6, "= Rp", lightgreen, "                            |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def minyak_green():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|                                                         |")
    hargao7 = int(input("|   Jumlah cat : "))

    green = ho[0]*hargao7
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", ho[0], "*", hargao7, "= Rp", green, "                                  |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def minyak_lightblue():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|                                                         |")
    hargao8 = int(input("|   Jumlah cat : "))

    lightblue = ho[0]*hargao8
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", ho[0], "*", hargao8, "= Rp", lightblue, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def minyak_blue():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|                                                         |")
    hargao9 = int(input("|   Jumlah cat : "))

    blue = ho[0]*hargao9
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", ho[0], "*", hargao9, "= Rp", blue, "                                 |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def minyak_brown():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|                                                         |")
    hargao10 = int(input("|   Jumlah cat : "))

    brown = ho[0]*hargao10
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", ho[0], "*", hargao10, "= Rp", brown, "                                 |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def minyak_black():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|                                                         |")
    hargao11 = int(input("|   Jumlah cat : "))

    black = ho[0]*hargao11
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("| Rp", ho[0], "*", hargao11, "= Rp", black, "                                   |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def paket_minyak():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|   Paket warna isi 11 + 1 kuas : Rp", ho[1], "              |")
    print("|                                                         |")
    hargao12 = int(input("|   Jumlah cat : "))

    paket = ho[1]*hargao12
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("| Rp", ho[1], "*", hargao12, "= Rp", paket, "                              |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

air = ["White", "Yellow", "Light Sand", "Orange", "Red", "Light Green", "Green", "Light Blue", "Blue", "Brown", "Black"]
hargaair = [7000, 75000]
def cat_air():
    clear_screen()
    print("+=========================================================+")
    print("|           Warna apa saja yang Anda butuhkan ?           |")
    print("|              Semua cat ini berukuran 12 ml              |")
    print("|                                                         |")
    print("|  [1]", air[0]," : Rp", hargaair[0],"                                  |")
    print("|  [2]", air[1]," : Rp", hargaair[0],"                                 |")
    print("|  [3]", air[2]," : Rp", hargaair[0],"                             |")
    print("|  [4]", air[3]," : Rp", hargaair[0],"                                 |")
    print("|  [5]", air[4]," : Rp", hargaair[0],"                                    |")
    print("|  [6]", air[5]," : Rp", hargaair[0],"                            |")
    print("|  [7]", air[6]," : Rp", hargaair[0],"                                  |")
    print("|  [8]", air[7]," : Rp", hargaair[0],"                             |")
    print("|  [9]", air[8]," : Rp", hargaair[0],"                                   |")
    print("|  [10]", air[9], ": Rp", hargaair[0],"                                  |")
    print("|  [11]", air[10]," : Rp", hargaair[0],"                                 |")
    print("|  [12] Paket warna isi 11 + 1 kuas : Rp", hargaair[1],"           |")
    print("|  [13] Kembali                                           |")
    print("|  [0] Keluar                                             |")
    print("+=========================================================+")
    water = str(input("=  Warna Cat : "))

    if (water == "1"):
        air_putih()
    elif (water == "2"):
        air_kuning()
    elif (water == "3"):
        air_lightsand()
    elif (water == "4"):
        air_orange()
    elif (water == "5"):
        air_red()
    elif (water == "6"):
        air_lightgreen()
    elif (water == "7"):
        air_green()
    elif (water == "8"):
        air_lightblue()
    elif (water == "9"):
        air_blue()
    elif (water == "10"):
        air_brown()
    elif (water == "11"):
        air_black()
    elif (water == "12"):
        paket_air()
    elif (water == "13"):
        menu_paint()
    elif (water == "0"):
        keluar_menu()
    else:
        print("Input yang Anda masukkan salah, silahkan coba ulang")
        input("                   Tekan enter")
        cat_air()

def air_putih():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       ", air[0],"   Rp", hargaair[0], "                                |")
    print("|                                                         |")
    hargawater1 = int(input("|   Jumlah cat : "))

    putih1 = hargaair[0]*hargawater1
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargaair[0], "*", hargawater1, "= Rp", putih1, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def air_kuning():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       ", air[1],"   Rp", hargaair[0], "                               |")
    print("|                                                         |")
    hargawater2 = int(input("|   Jumlah cat : "))

    kuning2 = hargaair[0]*hargawater2
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargaair[0], "*", hargawater2, "= Rp", kuning2, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def air_lightsand():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       ", air[2],"   Rp", hargaair[0], "                           |")
    print("|                                                         |")
    hargawater3= int(input("|   Jumlah cat : "))

    lightsand1 = hargaair[0]*hargawater3
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargaair[0], "*", hargawater3, "= Rp", lightsand1, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def air_orange():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       ", air[3],"   Rp", hargaair[0], "                               |")
    print("|                                                         |")
    hargawater4 = int(input("|   Jumlah cat : "))

    orange1 = hargaair[0]*hargawater4
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargaair[0], "*", hargawater4, "= Rp", orange1, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def air_red():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       ", air[4],"   Rp", hargaair[0], "                                  |")
    print("|                                                         |")
    hargawater5 = int(input("|   Jumlah cat : "))

    merah1 = hargaair[0]*hargawater5
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargaair[0], "*", hargawater5, "= Rp", merah1, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def air_lightgreen():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       ", air[5],"   Rp", hargaair[0], "                          |")
    print("|                                                         |")
    hargawater6 = int(input("|   Jumlah cat : "))

    lightgreen1 = hargaair[0]*hargawater6
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargaair[0], "*", hargawater6, "= Rp", lightgreen1, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def air_green():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       ", air[6],"   Rp", hargaair[0], "                                |")
    print("|                                                         |")
    hargawater7 = int(input("|   Jumlah cat : "))

    hijau1 = hargaair[0]*hargawater7
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargaair[0], "*", hargawater7, "= Rp", hijau1, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def air_lightblue():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       ", air[7],"   Rp", hargaair[0], "                           |")
    print("|                                                         |")
    hargawater8 = int(input("|   Jumlah cat : "))

    lightgreen1 = hargaair[0]*hargawater8
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargaair[0], "*", hargawater8, "= Rp", lightgreen1, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def air_blue():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       ", air[8],"   Rp", hargaair[0], "                                 |")
    print("|                                                         |")
    hargawater9 = int(input("|   Jumlah cat : "))

    blue1 = hargaair[0]*hargawater9
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargaair[0], "*", hargawater9, "= Rp", blue1, "                                |")
    print("|                                                         |") 
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def air_brown():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       ", air[9],"   Rp", hargaair[0], "                                |")
    print("|                                                         |")
    hargawater10 = int(input("|   Jumlah cat : "))

    brown1 = hargaair[0]*hargawater10
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargaair[0], "*", hargawater10, "= Rp", brown1, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def air_black():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       ", air[10],"   Rp", hargaair[0], "                                |")
    print("|                                                         |")
    hargawater11 = int(input("|   Jumlah cat : "))

    black1 = hargaair[0]*hargawater11
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargaair[0], "*", hargawater11 ,"= Rp", black1, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def paket_air():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|   Paket warna isi 11 + 1 kuas : Rp", hargaair[1], "               |")
    print("|                                                         |")
    hargawater12 = int(input("|   Jumlah cat : "))

    paketair = hargaair[1]*hargawater12
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("| ", hargaair[1], "*", hargawater12, "=", paketair, "                                    |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

akr = ["Hitam", "Putih", "Merah", "Hijau", "Biru", "Kuning", "Coklat Tua", "Ungu"]
hrgakr = [10000,75000]
def cat_akrilik():
    clear_screen()
    print("+=========================================================+")
    print("|           Warna apa saja yang Anda butuhkan ?           |")
    print("|              Semua cat ini berukuran 30 ml              |")
    print("|                                                         |")
    print("|  [1]", akr[0]," : Rp", hrgakr[0],"                                 |")
    print("|  [2]", akr[1]," : Rp", hrgakr[0],"                                 |")
    print("|  [3]", akr[2]," : Rp", hrgakr[0],"                                 |")
    print("|  [4]", akr[3]," : Rp", hrgakr[0],"                                 |")
    print("|  [5]", akr[4]," : Rp", hrgakr[0],"                                  |")
    print("|  [6]", akr[5]," : Rp", hrgakr[0],"                                |")
    print("|  [7]", akr[6]," : Rp", hrgakr[0],"                            |")
    print("|  [8]", akr[7]," : Rp", hrgakr[0],"                                  |")
    print("|  [9] Paket 8 warna+ 1 kuas : Rp", hrgakr[1],"                  |")
    print("|  [10] Kembali                                           |")
    print("|  [0] Keluar                                             |")
    print("+=========================================================+")
    water = str(input("=  Warna Cat : "))

    if (water == "1"):
        akr_hitam()
    elif (water == "2"):
        akr_putih()
    elif (water == "3"):
        akr_merah()
    elif (water == "4"):
        akr_hijau()
    elif (water == "5"):
        akr_biru()
    elif (water == "6"):
        akr_kuning()
    elif (water == "7"):
        akr_Coklat()
    elif (water == "8"):
        akr_Ungu()
    elif (water == "9"):
        paket_akr()
    elif (water == "10"):
        menu_paint()
    elif (water == "0"):
        keluar_menu()
    else:
        print("Input yang Anda masukkan salah, silahkan coba ulang")
        print("                   Tekan enter")
        input(" ")
        cat_akrilik()

def akr_hitam():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", akr[0],"   Rp", hrgakr[0], "                              |")
    print("|                                                         |")
    hargaqq = int(input("|   Jumlah cat : "))

    blackqq = hrgakr[0]*hargaqq
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hrgakr[0], "*", hargaqq ,"= Rp", blackqq, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def akr_putih():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", akr[1],"   Rp", hrgakr[0], "                              |")
    print("|                                                         |")
    harga62 = int(input("|   Jumlah cat : "))

    putih61 = hrgakr[0]*harga62
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hrgakr[0], "*", harga62 ,"= Rp", putih61, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def akr_merah():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", akr[2],"   Rp", hrgakr[0], "                              |")
    print("|                                                         |")
    hargavv = int(input("|   Jumlah cat : "))

    warnavv = hrgakr[0]*hargavv
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hrgakr[0], "*", hargavv ,"= Rp", warnavv, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def akr_hijau():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", akr[3],"   Rp", hrgakr[0], "                              |")
    print("|                                                         |")
    hargacc = int(input("|   Jumlah cat : "))

    warnacc = hrgakr[0]*hargacc
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hrgakr[0], "*", hargacc ,"= Rp", warnacc, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def akr_biru():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", akr[4],"   Rp", hrgakr[0], "                               |")
    print("|                                                         |")
    hargax = int(input("|   Jumlah cat : "))

    warnax = hrgakr[0]*hargax
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hrgakr[0], "*", hargax ,"= Rp", warnax, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def akr_kuning():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", akr[5],"   Rp", hrgakr[0], "                             |")
    print("|                                                         |")
    hargazz = int(input("|   Jumlah cat : "))

    warnazz = hrgakr[0]*hargazz
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hrgakr[0], "*", hargazz ,"= Rp", warnazz, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def akr_Coklat():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", akr[6],"   Rp", hrgakr[0], "                         |")
    print("|                                                         |")
    hargauu = int(input("|   Jumlah cat : "))

    warnauu = hrgakr[0]*hargauu
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hrgakr[0], "*", hargauu ,"= Rp", warnauu, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def akr_Ungu():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", akr[7],"   Rp", hrgakr[0], "                               |")
    print("|                                                         |")
    hargall = int(input("|   Jumlah cat : "))

    warnall = hrgakr[0]*hargall
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hrgakr[0], "*", hargall ,"= Rp", warnall, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def paket_akr():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       Paket 8 warna + 1 kuas : Rp", hrgakr[1], "                 |")
    print("|                                                         |")
    hargakk = int(input("|   Jumlah cat : "))

    warnakk = hrgakr[1]*hargakk
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hrgakr[1], "*", hargakk ,"= Rp", warnakk, "                              |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

pos = ["White", "Black", "Yellow", "Chrome Yellow", "Burnt Sienna", "Vermilion Hue", "Carmine", "Purple", "Yellow Green", "Green", "Cobalt Blue", "Prussian Blue"]
hargapos = [16000, 190000]
def cat_poster():
    clear_screen()
    print("+=========================================================+")
    print("|           Warna apa saja yang Anda butuhkan ?           |")
    print("|              Semua cat ini berukuran 30 ml              |")
    print("|                                                         |")
    print("|  [1]", pos[0]," : Rp", hargapos[0],"                                 |")
    print("|  [2]", pos[1]," : Rp", hargapos[0],"                                 |")
    print("|  [3]", pos[2]," : Rp", hargapos[0],"                                |")
    print("|  [4]", pos[3]," : Rp", hargapos[0],"                         |")
    print("|  [5]", pos[4]," : Rp", hargapos[0],"                          |")
    print("|  [6]", pos[5]," : Rp", hargapos[0],"                         |")
    print("|  [7]", pos[6]," : Rp", hargapos[0],"                               |")
    print("|  [8]", pos[7]," : Rp", hargapos[0],"                                |")
    print("|  [9]", pos[8]," : Rp", hargapos[0],"                          |")
    print("|  [10]", pos[9]," : Rp", hargapos[0],"                                |")
    print("|  [11]", pos[10]," : Rp", hargapos[0],"                          |")
    print("|  [12]", pos[11]," : Rp", hargapos[0],"                        |")
    print("|  [13] Paket 12 warna : Rp", hargapos[1],"                       |")
    print("|  [14] Kembali                                           |")
    print("|  [0] Keluar                                             |")
    print("+=========================================================+")
    catpos1 = str(input("=  Warna Cat : "))

    if (catpos1 == "1"):
        pos_1()
    elif (catpos1 == "2"):
        pos_2()
    elif (catpos1 == "3"):
        pos_3()
    elif (catpos1 == "4"):
        pos_4()
    elif (catpos1 == "5"):
        pos_5()
    elif (catpos1 == "6"):
        pos_6()
    elif (catpos1 == "7"):
        pos_7()
    elif (catpos1 == "8"):
        pos_8()
    elif (catpos1 == "9"):
        pos_9()
    elif (catpos1 == "10"):
        pos_10()
    elif (catpos1 == "11"):
        pos_11()
    elif (catpos1 == "12"):
        pos_12()
    elif (catpos1 == "13"):
        pos_paket()
    elif (catpos1 == "14"):
        menu_paint()
    elif (catpos1 == "0"):
        keluar_menu()
    else:
        print("Input yang Anda masukkan salah, silahkan coba ulang")
        print("                   Tekan enter")
        input(" ")
        cat_akrilik()

def pos_1():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", pos[0],"   Rp", hargapos[0], "                              |")
    print("|                                                         |")
    harga74 = int(input("|   Jumlah cat : "))

    warna74 = hargapos[0]*harga74
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargapos[0], "*", harga74 ,"= Rp", warna74, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def pos_2():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", pos[1],"   Rp", hargapos[0], "                              |")
    print("|                                                         |")
    harga58 = int(input("|   Jumlah cat : "))

    warna58 = hargapos[0]*harga58
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargapos[0], "*", harga58 ,"= Rp", warna58, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def pos_3():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", pos[2],"   Rp", hargapos[0], "                             |")
    print("|                                                         |")
    harga25 = int(input("|   Jumlah cat : "))

    warna25 = hargapos[0]*harga25
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargapos[0], "*", harga25 ,"= Rp", warna25, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def pos_4():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", pos[3],"   Rp", hargapos[0], "                      |")
    print("|                                                         |")
    harga90 = int(input("|   Jumlah cat : "))

    warna90 = hargapos[0]*harga90
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargapos[0], "*", harga90 ,"= Rp", warna90, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def pos_5():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", pos[4],"   Rp", hargapos[0], "                       |")
    print("|                                                         |")
    harga56 = int(input("|   Jumlah cat : "))

    warna56 = hargapos[0]*harga56
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargapos[0], "*", harga56 ,"= Rp", warna56, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def pos_6():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", pos[5],"   Rp", hargapos[0], "                      |")
    print("|                                                         |")
    hargadc = int(input("|   Jumlah cat : "))

    warnadc = hargapos[0]*hargadc
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargapos[0], "*", hargadc ,"= Rp", warnadc, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def pos_7():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", pos[6],"   Rp", hargapos[0], "                            |")
    print("|                                                         |")
    hargaac = int(input("|   Jumlah cat : "))

    warnaac = hargapos[0]*hargaac
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargapos[0], "*", hargaac ,"= Rp", warnaac, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def pos_8():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", pos[7],"   Rp", hargapos[0], "                             |")
    print("|                                                         |")
    hargaop = int(input("|   Jumlah cat : "))

    warnaop = hargapos[0]*hargaop
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargapos[0], "*", hargaop ,"= Rp", warnaop, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def pos_9():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", pos[8],"   Rp", hargapos[0], "                       |")
    print("|                                                         |")
    hargauuu = int(input("|   Jumlah cat : "))

    warnauuu = hargapos[0]*hargauuu
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargapos[0], "*", hargauuu ,"= Rp", warnauuu, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def pos_10():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", pos[9],"   Rp", hargapos[0], "                              |")
    print("|                                                         |")
    harganee = int(input("|   Jumlah cat : "))

    warnanee = hargapos[0]*harganee
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargapos[0], "*", harganee ,"= Rp", warnanee, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def pos_11():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", pos[10],"   Rp", hargapos[0], "                        |")
    print("|                                                         |")
    harga77 = int(input("|   Jumlah cat : "))

    warna77 = hargapos[0]*harga77
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargapos[0], "*", harga77 ,"= Rp", warna77, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def pos_12():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", pos[11],"   Rp", hargapos[0], "                      |")
    print("|                                                         |")
    hargaoo = int(input("|   Jumlah cat : "))

    warnaoo = hargapos[0]*hargaoo
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargapos[0], "*", hargaoo ,"= Rp", warnaoo, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def pos_paket():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       Paket 12 warna : Rp", hargapos[1], "                       |")
    print("|                                                         |")
    hargawee = int(input("|   Jumlah cat : "))

    warnawee = hargapos[1]*hargawee
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargapos[1], "*", hargawee ,"= Rp", warnawee, "                             |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()


brush = ["Round Brush", "Flat Brush", "Fan Brush", "Rigger Brush", "Angle Brush", "Bright Brush", "Mop Brush"]
def menu_brush():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan pilih brush tipe apa yang Anda butuhkan :     |")
    print("|                                                         |")
    print("|  [1]", brush[0]," : Rp", hargabr[0],"                            |")
    print("|  [2]", brush[1]," : Rp", hargabr[1],"                             |")
    print("|  [3]", brush[2]," : Rp", hargabr[2],"                              |")
    print("|  [4]", brush[3]," : Rp", hargabr[3],"                           |")
    print("|  [5]", brush[4]," : Rp", hargabr[4],"                            |")
    print("|  [6]", brush[5]," : Rp", hargabr[5],"                           |")
    print("|  [7]", brush[6]," : Rp", hargabr[6],"                              |")
    print("|  [8] Paket 7 kuas : Rp ", hargabr[7],"                          |")
    print("|  [9] Kembali                                            |")
    print("|  [0] Keuar                                              |")
    print("+=========================================================+")
    belibr = str(input("|  Tipe Brush : "))

    if (belibr == "1"):
        Round_brush()
    elif (belibr == "2"):
        Flat_brush()
    elif (belibr == "3"):
        Fan_brush()
    elif (belibr == "4"):
        Rigger_brush()
    elif (belibr == "5"):
        Angle_brush()
    elif (belibr == "6"):
        Bright_brush()
    elif (belibr == "7"):
        Mop_brush()
    elif (belibr == "8"):
        paket_br()
    elif (belibr == "9"):
        menu_customer()
    elif (belibr == "0"):
        keluar_menu()
    else:
        print("         Mohon maaf, inputan Anda salah...          ")
        input("               === Tekan Enter ===                  ")
        menu_brush()

def paket_br():
    clear_screen()
    print("+=================================================================+")
    print("|     Silahkan inputkan jumlah brush pack yang ingin di beli      |")
    print("|                                                                 |")
    hargabr1 = int(input("|   Jumlah pack : "))

    bulat = hargabr[7]*hargabr1
    print("+=================================================================+")
    print("|  Total harga :                                                  |")
    print("|  Rp", hargabr[7], "*", hargabr1, "= Rp", bulat, "                                        |")
    print("|                                                                 |")
    print("|                Terima kasih telah berbelanja !                  |")
    print("|              Silahkan tekan enter untuk kembali                 |")
    print("+=================================================================+")
    input(" ")
    menu_customer()


def Round_brush():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    
    print("|       ", brush[0],"   Rp", hargabr[0], "                          |")
    print("|                                                         |")
    hargabr1 = int(input("|   Jumlah kuas : "))

    bulat = hargabr[0]*hargabr1
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargabr[0], "*", hargabr1, "= Rp", bulat, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def Flat_brush():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       ", brush[1],"   Rp", hargabr[1], "                           |")
    print("|                                                         |")
    hargabr2 = int(input("|   Jumlah kuas : "))

    lurus = hargabr[1]*hargabr2
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargabr[1], "*", hargabr2, "= Rp", lurus, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def Fan_brush():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       ", brush[2],"   Rp", hargabr[2], "                            |")
    print("|                                                         |")
    hargabr3 = int(input("|   Jumlah kuas : "))

    kipas = hargabr[2]*hargabr3
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargabr[2], "*", hargabr3, "= Rp", kipas, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def Rigger_brush():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       ", brush[3],"   Rp", hargabr[3], "                         |")
    print("|                                                         |")
    hargabr4 = int(input("|   Jumlah kuas : "))

    ombak = hargabr[3]*hargabr4
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargabr[3], "*", hargabr4, "= Rp", ombak, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def Angle_brush():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       ", brush[4],"   Rp", hargabr[4], "                          |")
    print("|                                                         |")
    hargabr5 = int(input("|   Jumlah kuas : "))

    sudut = hargabr[4]*hargabr5
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("| ", hargabr[4], "*", hargabr5, "=", sudut, "                                      |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def Bright_brush():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       ", brush[5],"   Rp", hargabr[5], "                         |")
    print("|                                                         |")
    hargabr6 = int(input("|   Jumlah kuas : "))

    terang = hargabr[5]*hargabr6
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargabr[5], "*", hargabr6, "= Rp", terang, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def Mop_brush():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|       ", brush[6],"   Rp", hargabr[6], "                            |")
    print("|                                                         |")
    hargabr7 = int(input("|   Jumlah kuas : "))

    mop = hargabr[6]*hargabr7
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargabr[6], "*", hargabr7, "= Rp", mop, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()


canvas = ["60 x 90 cm", "60 x 80 cm", "50 x 70 cm", "50 x 50 cm", "40 x 50 cm"]
def menu_canvas():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan pilih ukuran kanvas yang Anda butuhkan :      |")
    print("|                                                         |")
    print("|  [1]", canvas[0]," : Rp", hargacan[0],"                            |")
    print("|  [2]", canvas[1]," : Rp", hargacan[1],"                            |")
    print("|  [3]", canvas[2]," : Rp", hargacan[2],"                            |")
    print("|  [4]", canvas[3]," : Rp", hargacan[3],"                            |")
    print("|  [5]", canvas[4]," : Rp", hargacan[4],"                            |")
    print("|  [6] Kembali                                            |")
    print("|  [0] Keluar                                             |")
    print("+=========================================================+")
    belican = str(input("|  Ukuran Canvas : "))

    if (belican == "1"):
        canvas_1()
    elif (belican == "2"):
        canvas_2()
    elif (belican == "3"):
        canvas_3()
    elif (belican == "4"):
        canvas_4()
    elif (belican == "5"):
        canvas_5()
    elif (belican == "6"):
        menu_customer()
    elif (belican == "0"):
        keluar_menu()
    else:
        print("        Inputan yang Anda masukkan salah")
        print("       silahkan coba ulang dan tekan enter")
        input(" ")
        menu_canvas()

def canvas_1():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", canvas[0],"   Rp", hargacan[0], "                         |")
    print("|                                                         |")
    hargagg = int(input("|   Jumlah cat : "))

    warnagg = hargacan[0]*hargagg
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargacan[0], "*", hargagg ,"= Rp", warnagg, "                              |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def canvas_2():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", canvas[1],"   Rp", hargacan[1], "                         |")
    print("|                                                         |")
    hargaree = int(input("|   Jumlah canvas : "))

    warnaree = hargacan[1]*hargaree
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargacan[1], "*", hargaree ,"= Rp", warnaree, "                              |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def canvas_3():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", canvas[2],"   Rp", hargacan[2], "                         |")
    print("|                                                         |")
    hargaen = int(input("|   Jumlah canvas : "))

    warnaen = hargacan[2]*hargaen
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargacan[2], "*", hargaen ,"= Rp", warnaen, "                              |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def canvas_4():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", canvas[3],"   Rp", hargacan[3], "                         |")
    print("|                                                         |")
    hargaaa = int(input("|   Jumlah canvas : "))

    warnaaa = hargacan[3]*hargaaa
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargacan[3], "*", hargaaa ,"= Rp", warnaaa, "                              |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def canvas_5():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|        ", canvas[4],"   Rp", hargacan[4], "                         |")
    print("|                                                         |")
    hargawee = int(input("|   Jumlah canvas : "))

    warnawee = hargacan[4]*hargawee
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargacan[4], "*", hargawee ,"= Rp", warnawee, "                              |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()


def menu_books():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan pilih jenis Art Book yang Anda butuhkan :     |")
    print("|                                                         |")
    print("|  [1] Sketchbook                                         |")
    print("|  [2] Watercolour Book                                   |")
    print("|  [3] Kembali                                            |")
    print("|  [0] Keluar                                             |")
    print("+=========================================================+")
    Books = str(input("|  Jenis buku : "))

    if (Books == "1"):
        book_1()
    elif (Books == "2"):
        book_2()
    elif (Books == "3"):
        menu_customer()
    elif (Books == "0"):
        keluar_menu()
    else:
        print("              Maaf, inputan Anda salah")
        print("       Silahkan tekan enter untuk mengulang")
        input(" ")
        menu_books()

sketch = ["Sketchbook A5", "Sketchbook A4"]
sketch1 = ["Watercolor Book A4", "Watercolor Book A3"]
def book_1():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan pilih SketchBook yang Anda butuhkan :         |")
    print("|                                                         |")
    print("|  [1]", sketch[0], ": Rp", hargasketch[0],"                          |")
    print("|  [2]", sketch[1], ": Rp", hargasketch[1],"                          |")
    print("|  [3] Kembali                                            |")
    print("|  [0] Keluar                                             |")
    print("+=========================================================+")
    sketch1 = str(input("|  Sketchbook : "))

    if (sketch1 == "1"):
        kertas_a5()
    elif (sketch1 == "2"):
        kertas_a4()
    elif (sketch1 == "3"):
        menu_books()
    elif (sketch1 == "0"):
        keluar_menu()
    else:
        print("              Maaf, inputan Anda salah")
        print("       Silahkan tekan enter untuk mengulang")
        input(" ")
        book_1()

def kertas_a5():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|  Keterangan : Isi 30 lembar, GSM 160                    |")
    print("|      ", sketch[0],"   Rp", hargasketch[0], "                        |")
    print("|                                                         |")
    harga = int(input("|   Jumlah buku : "))

    warna1 = hargasketch[0]*harga
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargasketch[0], "*", harga ,"= Rp", warna1, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def kertas_a4():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|  Keterangan : Isi 50 lembar                             |")
    print("|      ", sketch[1],"   Rp", hargasketch[1], "                        |")
    print("|                                                         |")
    harga = int(input("|   Jumlah buku : "))

    warna1 = hargasketch[1]*harga
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargasketch[1], "*", harga ,"= Rp", warna1, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def book_2():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan pilih SketchBook yang Anda butuhkan :         |")
    print("|                                                         |")
    print("|  [1]", sketch1[0], ": Rp", hargasketch1[0],"                    |")
    print("|  [2]", sketch1[1], ": Rp", hargasketch1[1],"                     |")
    print("|  [3] Kembali                                            |")
    print("|  [0] Keluar                                             |")
    print("+=========================================================+")
    sketch2 = str(input("|  Sketchbook : "))

    if (sketch2 == "1"):
        water_book1()
    elif (sketch2 == "2"):
        water_book2()
    elif (sketch2 == "3"):
        menu_books()
    elif (sketch2 == "0"):
        keluar_menu()
    else:
        print("              Maaf, inputan Anda salah")
        print("       Silahkan tekan enter untuk mengulang")
        input(" ")
        book_2()

def water_book1():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|  Keterangan : Isi 30 lembar, GSM 160                    |")
    print("|      ", sketch1[0],"   Rp", hargasketch1[0], "                  |")
    print("|                                                         |")
    harga = int(input("|   Jumlah buku : "))

    warna1 = hargasketch1[0]*harga
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargasketch1[0], "*", harga ,"= Rp", warna1, "                             |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def water_book2():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak barang yang Anda ingin beli   |")
    print("|  Keterangan : Isi 50 lembar                             |")
    print("|      ", sketch1[1],"   Rp", hargasketch1[1], "                   |")
    print("|                                                         |")
    harga = int(input("|   Jumlah buku : "))

    warna1 = hargasketch1[1]*harga
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargasketch1[1], "*", harga ,"= Rp", warna1, "                              |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

palet = ["Palet kayu", "Palet Plastik"]
def menu_palet():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan pilih palet warna yang Anda butuhkan :        |")
    print("|                                                         |")
    print("|  [1]", palet[0], ": Rp", hargapalet[0],"                             |")
    print("|  [2]", palet[1], ": Rp", hargapalet[1],"                           |")
    print("|  [3] Kembali                                            |")
    print("|  [0] Keluar                                             |")
    print("+=========================================================+")
    palet1 = str(input("|  Tipe palet : "))

    if (palet1 == "1"):
        palet_kayu()
    elif (palet1 == "2"):
        palet_plastik()
    elif (palet1 == "3"):
        menu_customer()
    elif (palet1 == "0"):
        keluar_menu()
    else:
        print("              Maaf, inputan Anda salah")
        print("       Silahkan tekan enter untuk mengulang")
        input(" ")
        menu_palet()

def palet_kayu():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak palet yang Anda ingin beli    |")
    print("|  Keterangan : Ukuran 29 x 21 cm                         |")
    print("|                                                         |")
    harga = int(input("|   Jumlah palet : "))

    warna1 = hargapalet[0]*harga
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargapalet[0], "*", harga ,"= Rp", warna1, "                               |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

def palet_plastik():
    clear_screen()
    print("+=========================================================+")
    print("|  Silahkan inputkan banyak palet yang Anda ingin beli    |")
    print("|  Keterangan : Ukuran 17 x 22 cm                         |")
    print("|                                                         |")
    harga = int(input("|   Jumlah palet : "))

    warna1 = hargapalet[1]*harga
    print("+=========================================================+")
    print("|  Total harga :                                          |")
    print("|  Rp", hargapalet[1], "*", harga ,"= Rp", warna1, "                                |")
    print("|                                                         |")
    print("|            Terima kasih telah berbelanja !              |")
    print("|          Silahkan tekan enter untuk kembali             |")
    print("+=========================================================+")
    input(" ")
    menu_customer()

menu_login()