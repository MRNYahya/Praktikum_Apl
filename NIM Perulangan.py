#Materi Perulangan
import os 
import time

# Muhamad Rizky Nilzamyahya
# NIM 2009106029
while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        #input NIM + 10 = 29 + 10 = 39
        NIM = int(input("Masukkan NIM: "))
        y = 1
        a = 1

        while (y <= NIM):
            print(a)
            a += 1
            if (a == 10):
                a -= 9
            y += 1
        break

    except ValueError:
        print ("Masukkan Angka woyy")
        time.sleep(2)