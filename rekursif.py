#algoritma yang melakukan pemanggilan terhadap dirinya sendiri

def faktorial(x):
    if x == 1:
        return 1
    else:
        return(x * faktorial(x-1))
        
num = int(input("Masukkan Nilai yang ingin di Faktorial: "))
print("Faktorial dari", num,"adalah",faktorial(num))

def coba():
    x = int(input("Masukkan Angka: "))
    if 1 <= x <= 5:
        print("Angka 1 sampai 5")
    
    else:
        print("Coba Lagi !!!")
        coba()

#indirect rekursif, hubungan timbal balik
def foo1():
    foo2()

def foo2():
    foo1()

coba()