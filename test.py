import os, random, sys
from sympy import sympify, Symbol, Derivative
from math import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def error():
    print('Usage : Main.py')
    print(' Main.py <"Persamaan"> ')
    print('Contoh Inputan : Main.py "x**2 + 9"')
    print("Contoh pangkat 2 => (**2)")

#menu
def method(p):
    clear_screen()
    print("Persamaan: %s"%(pers))
    print("\nPilih metode:")
    print("1. Bagi Dua")
    print("2. Regula Falsi")
    print("3. Teknik Pias")
    print("4. Newton Cotes (Simpson 1/3)")
    pil = int(input("Masukkan Pilihan : "))
    pil = 4
    if(pil == 1):
        bagidua(pers)
    elif(pil == 2):
        Regulafalsi(pers)
    elif(pil == 3):
        Teknikpias()
    elif(pil == 4):
        Newtoncotes1_3()
    else:
        print("Inputan salah")
        exit()
    return 0

#input persamaan dan perulangan
if name == 'main':
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
            print("****")
            print("-------SEVINA AFI AMALIA------")
            print("----------2009106042----------")
            print("****")
            print("\n\n========================================")
            print("\t\tSOLUTION NON LINEAR")
            print("=======================================\n")
            print("Contoh inputan : y = x**2 + 1")
            print("Contoh pangkat 2 => (**2)")
            pers = str(input("Masukkan Persamaan : "))
            pers = pers.lower()
            print()
            method(pers)
        print()
        pil2 = input("Ulang ? (y/n) : ")
        if (pil2 =='y' or pil2 == 'Y'):
            pil3 = input("Ulang dengan Persamaan yang sama ? (y/n) : ")
            clear_screen()
        else:
            exit()
  

    
def f(x,p):
    return (eval(p))

def persamaan(pers):
    x = Symbol('x')
    y=sympify(input('\nMasukkan Ulang Persamaannya : '))
    return pers

def persamaan1(pers): #Alternative
    n = 1
    while((pers.find("^")) == 1):
        n = n + 1
        q = n - 1
        pers = pers.replace("^%d"%(n),("*x"*q))
    return pers

def turunan(pers):
    x= Symbol('x')
    deriv= Derivative(pers, x)
    return str(deriv.doit())

def bagidua(pers):
    clear_screen()
    n = 0
    p = persamaan(pers)
    print("Metode Numerik")
    print("Persamaan, %s"%(pers))
    print()
    print("(Berapa angka dibelakang koma. Masukkan 2 jika tidak yakin)")
    rou = int(input("Pembulatan : "))
    print("(Ingin mendekati nilai berapa. Masukkan 0 jika tidak yakin)")
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
            print("Syarat sudah ok. f(%d)*f(%d) < 0 || %5.2f < 0"%(x1,x2,check))
            break
        else:
            print("Syarat belum ok f(%d)*f(%d) >= 0 || %5.2f >= 0"%(x1,x2,check))

    print()
    #Mempersiapkan output berupa tabel
    print("X1 = %d , X2 = %d , Error = %.6f"% (x1,x2,err))
    print("_______")
    print(" n x f(x) error ")
    print("_______")
    
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
            print("__")
            print("Akar Persamaan, %.36f"%(x3))
            print("Atau ~ %.4f"%(round(x3,4)))
            print("Error, %.4f"%(round(fx3,4)))
            print()
            print("Note!")
            print("Saat Melakukan perhitungan pastikan gunakan pembulatan")
            print("agar mendapatkan jawaban yang sesuai dengan taraf error")
            break
        if f(x1,p) * f(x3,p) > 0:
            x1 = x3
        else :
            x2 = x3
            
        cektemp = abs(fx3)
        #Agar memudahkan pembacaan iterasi. setiap 10 iterasi di stop.
        if n%10 == 0:
            input("Lanjut? Tekan enter.")

def Regulafalsi(pers):
    clear_screen()
    n = 0
    p = persamaan(pers)
    #pil[0] berisi pilihan metode pil[1] berisi string metode
    print("Metode Numerik")
    print("Persamaan, %s"%(pers))
    print()
    print("(Berapa angka dibelakang koma. Masukkan 2 jika tidak yakin)")
    rou = int(input("Pembulatan : "))
    print("(Ingin mendekati nilai berapa. Masukkan 0 jika tidak yakin)")
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
            print("Syarat sudah ok. f(%d)*f(%d) < 0 || %5.2f < 0"%(x1,x2,check))
            break
        else:
            print("Syarat belum ok f(%d)*f(%d) >= 0 || %5.2f >= 0"%(x1,x2,check))
    print()
    
    #Mempersiapkan output berupa tabel
    print("X1 = %d , X2 = %d , Error = %.6f"% (x1,x2,err))
    print("_______")
    print(" n x f(x) error ")
    print("_______")
    
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
            print("Note!")
            print("Saat Melakukan perhitungan pastikan gunakan pembulatan")
            print("agar mendapatkan jawaban yang sesuai dengan taraf error")
            break
        if f(x1,p) * f(x3,p) > 0:
            x1 = x3
        else :
            x2 = x3
            
        cektemp = abs(fx3)
        
        #Agar memudahkan pembacaan iterasi. setiap 10 iterasi di stop.
        if n%10 == 0:
            input("Lanjut? Tekan enter.")
        
def Teknikpias():
    clear_screen()
    print("Metode Numerik")
    fungsi = input('input math function: ')
    f = lambda x: eval(fungsi)
    print()
    print("(Berapa angka dibelakang koma. Masukkan 2 jika tidak yakin)")
    rou = int(input("Pembulatan : "))
    
    while True:
        print()
        a = float(input("Masukkan batas bawah integral : "))
        b = float(input("Masukkan batas atas integral : "))
        fa = round(f(a),rou)
        fb = round(f(b),rou)
        print()
        print("Nilai dari, F(%d) = %f " % (a,fa))
        print("Nilai dari, F(%d) = %f " % (b,fb))
        print()
        break
        
    while True:
        #Counter Iterasi
        n = float(input('banyak iterasi: '))
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
    print("a = %d , b = %d"% (a,b))
    print("________")
    print(" n x f(a) f(b) ")
    print("________")
    
    #Hanya untuk initialisasi
    cektemp = random.randint(1,100)
 
    #Output Sesuai bentuk tabel
    print("%3d| %.6f %10.8f %12.10f" % (n,q,fa,fb))
 
    #Agar memudahkan pembacaan iterasi. setiap 10 iterasi di stop.
    if n%10 == 0:
        input("\nLanjut? Tekan enter.")

def Newtoncotes1_3():
    clear_screen()
    print("Metode Numerik")
    fungsi = input('input math function: ')
    f = lambda x: eval(fungsi)
    print()
    print("(Berapa angka dibelakang koma. Masukkan 2 jika tidak yakin)")
    rou = int(input("Pembulatan : "))
    
    while True:
        print()
        a = float(input("Masukkan batas bawah integral : "))
        b = float(input("Masukkan batas atas integral : "))
        fa = round(f(a),rou)
        fb = round(f(b),rou)
        print()
        print("Nilai dari, F(%d) = %f " % (a,fa))
        print("Nilai dari, F(%d) = %f " % (b,fb))
        print()
        break
    
    while True:
        #Counter Iterasi
        n = float(input('banyak iterasi: '))
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
    print("a = %d , b = %d"% (a,b))
    print("________")
    print(" n x f(a) f(b) ")
    print("________")
    
    #Hanya untuk initialisasi
    cektemp = random.randint(1,100)
 
    #Output Sesuai bentuk tabel
    print("%3d| %.6f %10.8f %12.10f" % (n,q,fa,fb))
 
 #Agar memudahkan pembacaan iterasi. setiap 10 iterasi di stop.
    if n%10 == 0:
        input("\nLanjut? Tekan enter.")