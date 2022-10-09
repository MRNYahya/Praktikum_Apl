print ("Program konversi Desimal, Binary, Octal, Hexadecimal")
print ("Angka Binary diawali 0b, Hexa diawali 0x, Oktal diawali 0o")
print ("Pilih [1] untuk Desimal ke Binary")
print ("Pilih [2] untuk Desimal ke Hexa")
print ("Pilih [3] untuk Desimal ke Octal")
print ("Pilih [4] untuk Binary ke Desimal")
print ("Pilih [5] untuk Binary ke Hexa")
print ("Pilih [6] untuk Binary ke Oktal")
print ("Pilih [7] untuk Hexa ke Binary")
print ("Pilih [8] untuk Hexa ke Desimal")
print ("Pilih [9] untuk Hexa ke Octal")
print ("Pilih [10] untuk octal ke Binary")
print ("Pilih [11] untuk octal ke Desimal")
print ("Pilih [12] untuk octal ke Hexa")
 
i = int(input("Masukkan pilihan anda: "))
if i == 1:
    x = int(input("masukkan angka Desimal: "))
    y=chr(bin(x))
    print (y)
    
elif i == 2:
    x = int(input("masukkan angka Desimal: "))
    print (hex(x))
elif i == 3:
    x = int(input("masukkan angka Desimal: "))
    print (oct(x))
elif i == 4:
    x = int(input("masukkan angka Binary: "),2)
    print (x)
elif i == 5:
    x = int(input("masukkan angka Binary: "),2)
    print (hex(x))
elif i == 6:
    x = int(input("masukkan angka Binary: "),2)
    print (oct(x))
elif i == 7:
    x = int(input("masukkan angka Hexa: "),16)
    print (bin(x))
elif i == 8:
    x = int(input("masukkan angka Hexa: "),16)
    print (x)
elif i == 9:
    x = int(input("masukkan angka Hexa: "),16)
    print (oct(x))
elif i == 10:
    x = int(input("masukkan angka Octal: "),8)
    print (bin(x))
elif i == 11:
    x = int(input("masukkan angka Octal: "),8)
    print (x)
elif i == 12:
    x = int(input("masukkan angka Octal: "),8)
    print (hex(x))
else:
    print("Pilihan anda salah")

#---------------------------------------------------------------------------

def ubah(i):
    angka = ['','satu','dua','tiga','empat','lima','enam','tujuh','delapan','sembilan','sepuluh','sebelas']
    i = int(i)
    result = ''
    if i >= 0 and i <=11:
        result += f'{angka[i]}'
    elif i<20:
        result += f'{ubah(i % 10)} belas'
    elif i <100:
        result += f'{ubah(i / 10)} puluh {ubah(i % 10)}'
    elif i<200:
        result += f'seratus {ubah(i - 100)}'
    elif i < 1000:
        result += f'{ubah( i / 100)} ratus {ubah(i %100)}'
    elif i < 2000:
        result += f'seribu {ubah(i - 1000)}'
    elif i<1000000:
        result += f'{ubah(i / 1000)} ribu {ubah(i % 1000)}'
    elif i<1000000000:
        result += f'{ubah(i / 1000000)} juta {ubah(i % 1000000)}'
    else:
        result += f'{ubah(i / 1000000000)} milyar {ubah(i % 1000000000)}'
    return result

n = int(input("\nmasukan bilangan : "))
print(ubah(n))


