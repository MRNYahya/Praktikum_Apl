from math import *
import os, random, sys
from sympy import sympify, Symbol, Derivative


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
2
def persamaan(pers):
    x = Symbol('x')
    y = sympify(input('\nMasukkan Ulang Persamaannya : '))
    return pers

def persamaan1(pers): #Alternative
    n = 1
    while((pers.find("^")) == 1):
        n = n + 1
        q = n - 1
        pers = pers.replace("^%d"%(n),("*x"*q))
    return pers

def f(x,p):
    return (eval(p))

def turunan(pers):
    x= Symbol('x')
    deriv= Derivative(pers, x)
    return str(deriv.doit())

def error():
    print('Usage : Main.py')
    print(' Main.py <"Persamaan"> ')
    print('example : Main.py "x**2 + 6 ')
    print(" for pangkat => (**)")

#Main Menu dan Pemanggilan fungsi fungsi
def menu(p):
    clear_screen()
    print("Persamaan: %s"%(pers))
    print("\nPilih Metode : ")
    print("[1] Bagi dua")
    print("[2] Regula falsi")
    print("[3] Teknik pias)")
    print("[4] Newton cotes (Simpson 1/3")
    pilihan = int(input("Masukkan Pilihan : "))
    pilihan = 4
    
    if(pilihan == 1):
        Bagidua(pers)
    elif(pilihan == 2):
        Regulafalsi(pers)
    elif(pilihan == 3):
        teknikpias()
    elif(pilihan == 4):
        Newtoncotes()
    else:
        print("Inputan salah")
        exit()
    return 0

def Bagidua(pers):
    clear_screen()
    n = 0
    p = persamaan(pers)
    print("Persamaan: %s"%(pers))
    print()
    #Saat Melakukan perhitungan pastikan gunakan Angka pembulatan")agar mendapatkan jawaban yang sesuai dengan taraf error
    print("Masukkan banyak angka dibelakang koma: ")
    rou = int(input("Angka pembulatan : "))
    print("Masukkan nilai epsilon:")
    err = float(input("Masukkan Error : "))
    while True:
        print()
        x1 = float(input("Masukkan X1 : "))
        x2 = float(input("Masukkan X3 : "))
        fx1 = round(f(x1,p),rou)
        fx2 = round(f(x2,p),rou)
        print()
        print("Nilai dari, F(%d) = %f " % (x1,fx1))
        print("Nilai dari, F(%d) = %f " % (x2,fx2))
        print()
        check = fx1*fx2
        if check < 0:
            print("Syarat sudah terpenuhi f(%d)*f(%d) < 0 || %5.2f < 0"%(x1,x2,check))
            break
        else:
            print("Syarat belum terpenuhi f(%d)*f(%d) >= 0 || %5.2f >= 0"%(x1,x2,check))
    print()
    #Mempersiapkan output berupa tabel
    print("\nX1 = %d , X2 = %d , Error = %.6f"% (x1,x2,err))
    print("\nn x f(x) error ")
    
    #Hanya untuk initialisasi
    cektemp = random.randint(1,100)
    
    while True:
        #Counter Iterasi
        n = n + 1
        x3 = round(((x1 + x2)/2),rou)
        fx3 = round(f(x3,p),rou)
        
        #Output Sesuai bentuk tabel
        print("%3d| %.8f %10.8f %12.10f" % (n,x3,fx3,fx3))
        
        #Print Akar Persamaan
        if abs(fx3) <= err or abs(fx3) == cektemp :
            print("\n\nAkar Persamaan, %.36f"%(x3))
            print("Atau ~ %.4f"%(round(x3,4)))
            print("Error, %.4f"%(round(fx3,4)))
            print()
            print("Harus menggunakan pembulatan supaya dapat taraf error dan jawaban!!")
            break
        if f(x1,p) * f(x3,p) > 0:
            x1 = x3
        else :
            x2 = x3
            
        cektemp = abs(fx3)
        #Agar memudahkan pembacaan iterasi. setiap 10 iterasi di stop.
        if n%10 == 0:
            input("Tekan enter bila ingin melanjutkan")
   
def Regulafalsi(pers):
    clear_screen()
    n = 0
    p = persamaan(pers)
    #pil[0] berisi pilihan metode pil[1] berisi string metode
    print("Persamaan: %s"%(pers))
    print()
    print("Masukkan banyak angka dibelakang koma: ")
    rou = int(input("Angka pembulatan : "))
    print("Masukkan nilai epsilon:")
    err = float(input("Masukkan Error : "))
    
    while True:
        print()
        x1 = float(input("Masukkan X1 : "))
        x2 = float(input("Masukkan X2 : "))
        fx1 = round(f(x1,p),rou)
        fx2 = round(f(x2,p),rou)
        print()
        print("Nilai dari, F(%d) = %f " % (x1,fx1))
        print("Nilai dari, F(%d) = %f " % (x2,fx2))
        print()
        check = fx1*fx2
        if check < 0:
            print("Syarat sudah terpenuhi f(%d)*f(%d) < 0 || %5.2f < 0"%(x1,x2,check))
            break
        else:
            print("Syarat belum terpenuhi f(%d)*f(%d) >= 0 || %5.2f >= 0"%(x1,x2,check))
    print()
    
    #Mempersiapkan output berupa tabel
    print("\nX1 = %d , X2 = %d , Error = %.6f"% (x1,x2,err))
    print("\nn x f(x) error ")
    
    #Hanya untuk initialisasi
    cektemp = random.randint(1,100)
    while True:
        #Counter Iterasi
        n = n + 1
        x3 = round(((x1 * f(x2,p) - x2 * f(x1,p)) / (f(x2,p) - f(x1,p))),rou)
        fx3 = round(f(x3,p),rou)
        
        #Output Sesuai bentuk tabel
        print("%3d| %.8f %10.8f %12.10f" % (n,x3,fx3,fx3))
    
        #Print Akar Persamaan
        if abs(fx3) <= err or abs(fx3) == cektemp :
            print("__")
            print("Akar Persamaan, %.36f"%(x3))
            print("Atau ~ %.4f"%(round(x3,4)))
            print("Error, %.4f"%(round(fx3,4)))
            print()
            break
        if f(x1,p) * f(x3,p) > 0:
            x1 = x3
        else :
            x2 = x3
            
        cektemp = abs(fx3)
        
        #Agar memudahkan pembacaan iterasi. setiap 10 iterasi di stop.
        if n%10 == 0:
            input("Tekan enter bila ingin melanjutkan")
     
def teknikpias():
    clear_screen()
    fungsi = input('Masukkan persamaan: ')
    f = lambda x: eval(fungsi)
    print()
    print("Masukkan banyak angka dibelakang koma")
    rou = int(input("Angka pembulatan : "))
    
    while True:
        print()
        a = float(input("Masukkan nilai batas bawah integral : "))
        b = float(input("Masukkan nilai batas atas integral  : "))
        fa = round(f(a),rou)
        fb = round(f(b),rou)
        print()
        print("Nilai dari, F(%d) = %f " % (a,fa))
        print("Nilai dari, F(%d) = %f " % (b,fb))
        print()
        break
        
    while True:
        #Counter Iterasi
        n = float(input('Banyaknya iterasi: '))
        deltaX = (b-a)/n
        fs = 0
        ft = 0
        i = b
        while i <= a:
            fs += f(i)
            ft += f(i+deltaX)
            i += deltaX*2
        q = ((2*fa - (f(a) + f(b))) + (ft-f(b+deltaX)))*deltaX/2
        print("Hasil integral Teknik Pias: ", q)
        break
    
    print()
    
    #Mempersiapkan output berupa tabel
    print("\na = %d , b = %d"% (a,b))
    print("\nn x f(a) f(b) ")
    
    #Hanya untuk initialisasi
    cektemp = random.randint(1,100)
 
    #Output Sesuai bentuk tabel
    print("%3d| %.6f %10.8f %12.10f" % (n,q,fa,fb))
 
    #Agar memudahkan pembacaan iterasi. setiap 10 iterasi di stop.
    if n%10 == 0:
        input("\nTekan enter untuk melanjutkan....")
        
def Newtoncotes():
    clear_screen()
    fungsi = input('Masukkan persamaan : ')
    f = lambda x: eval(fungsi)
    print()
    print("Masukkan banyak angka dibelakang koma")
    rou = int(input("Angka pembulatan : "))
    
    while True:
        print()
        a = float(input("Masukkan nilai batas bawah integral : "))
        b = float(input("Masukkan nilai batas atas integral : "))
        fa = round(f(a),rou)
        fb = round(f(b),rou)
        print()
        print("Nilai dari F(%d) = %f " % (a,fa))
        print("Nilai dari F(%d) = %f " % (b,fb))
        print()
        break
    
    while True:
        #Counter Iterasi
        n = float(input('Banyaknya iterasi: '))
        deltaX = (b-a)/n
        fs = 0
        ft = 0
        i = b
        while i <= a:
            fs += f(i)
            ft += f(i+deltaX)
            i += deltaX*2
        q = ((2*fa - (f(a) + f(b))) + (ft-f(b+deltaX))*4)*deltaX/3
        print("Hasil integral simpson: ", q)
        break
    
    print()
    #Mempersiapkan output berupa tabel
    print("\na = %d , b = %d"% (a,b))
    print("\nn x f(a) f(b) ")
    
    #Hanya untuk initialisasi
    cektemp = random.randint(1,100)
 
    #Output Sesuai bentuk tabel
    print("%3d| %.6f %10.8f %12.10f" % (n,q,fa,fb))
 
 #Agar memudahkan pembacaan iterasi. setiap 10 iterasi di stop.
    if n%10 == 0:
        input("\nTekan enter bila ingin melanjutkan")

#--------------------------------------------------------------------------------#
# Input persamaan dan perulangan.
#--------------------------------------------------------------------------------#

if _name_ == 'main':
    #Inisialisasi Variable
    pil2 = 'y'
    
    if( (len(sys.argv)>2)): #Error Usage
        error()
        exit()
        
    elif(len(sys.argv)==2): #jika Menggnuakan Argument
        pil3 = 'y'
        pers = str(sys.argv[1])
        if((sys.argv[1].find('x')) == -1):
            error()
            print('\nNo Variable or using other than x')
            exit()
            
    else:
        pil3 = 'n'
        
    clear_screen()
    while(pil2 == 'y' or pil2 == 'Y'):
        if (pil3 == 'n' or pil3 == 'N'):
            print("\t\t************")
            print("\t\t*-------SEVINA AFI AMALIA------*")
            print("\t\t*----------2009106042----------*")
            print("\t\t************\n")
            print("Contoh inputan : y = x**2 + 1")
            print("Contoh pangkat 2 => (**2)")
            p = str(input("Masukkan Persamaan : "))
            p = p.lower()
            print()
            
            menu(pers)
        
        print()
        pil2 = input("Apakah anda ingin ulangi? (y/n) : ")
        if (pil2 =='y' or pil2 == 'Y'):
            pil3 = input("Apakah anda ingin ulangi? (y/n) : ")
            clear_screen()
        else:
            exit()