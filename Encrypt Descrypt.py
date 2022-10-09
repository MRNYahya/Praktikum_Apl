import os
import time

def reset():
    os.system('cls' if os.name == 'nt' else 'clear')

x=1
while(x==1): # titik ulang menu awal
    reset()
    print("------------ TUGAS MATEMATIKA ------------")
    print("\nPilih salah satu:\n1.Encrypt\n2.Descrypt")
    menu=int(input("\nPilih: "))
    key=int(input("Jarak: "))

    if(menu == 1):
        # The Encryption Function
        def cipher_encrypt(plain_text):

            encrypted = ""
            
            for c in plain_text:

                if c.isupper(): #periksa apakah itu karakter huruf besar

                    c_index = ord(c) - ord('A')

                    # menggeser karakter saat ini dengan posisi kunci
                    c_shifted = (c_index + key) % 26 + ord('A')
                    c_new = chr(c_shifted)
                    encrypted += c_new

                elif c.islower(): # periksa apakah itu karakter huruf kecil

                    # kurangi unicode dari 'a' untuk mendapatkan indeks dalam rentang [0-25)
                    c_index = ord(c) - ord('a') 
                    c_shifted = (c_index + key) % 26 + ord('a')
                    c_new = chr(c_shifted)
                    encrypted += c_new

                elif c.isdigit():
                    # jika itu angka, geser nilai sebenarnya
                    c_new = (int(c) + key) % 10
                    encrypted += str(c_new)

                else:
                    # jika bukan berdasarkan abjad atau angka, biarkan saja seperti itu
                    encrypted += c

            return encrypted

        plain_text = input("Masukkan Kata: ")
        ciphertext = cipher_encrypt(plain_text)
        print("\nPlain text message     : ", plain_text)
        print("Encrypted ciphertext   : ", ciphertext)
        print("\n------------------------------------------")
        ulang=int(input("Kembali ke menu awal?\n1.Iya\n2.Tidak\n\nPilih: "))
        if (ulang==1):
            time.sleep(1)
            reset()
        elif (ulang==2):
            print("\n------------- PROGRAM SELESAI ------------")
            x=0

    elif (menu == 2):
        # The Decryption Function
        def cipher_decrypt(ciphertext):

            decrypted = ""

            for c in ciphertext:

                if c.isupper():

                    c_index = ord(c) - ord('A')
                    # menggeser karakter saat ini ke kiri dengan posisi kunci untuk mendapatkan posisi aslinya
                    c_og_pos = (c_index - key) % 26 + ord('A')
                    c_og = chr(c_og_pos)
                    decrypted += c_og

                elif c.islower():

                    c_index = ord(c) - ord('a')
                    c_og_pos = (c_index - key) % 26 + ord('a')
                    c_og = chr(c_og_pos)
                    decrypted += c_og

                elif c.isdigit():
                    # jika itu angka, geser nilai sebenarnya
                    c_og = (int(c) - key) % 10
                    decrypted += str(c_og)

                else:
                    # jika bukan berdasarkan abjad atau angka, biarkan saja seperti itu
                    decrypted += c

            return decrypted
        
        ciphertext = input("Masukkan Kata: ")
        decrypted_msg = cipher_decrypt(ciphertext)
        print("\nThe cipher text       : ", ciphertext)
        print("The decrypted message : ",decrypted_msg)
        print("\n------------------------------------------")
        ulang=int(input("Kembali ke menu awal?\n1.Iya\n2.Tidak\n\nPilih: "))
        if (ulang==1):
            time.sleep(1)
            reset()
        elif (ulang==2):
            print("\n------------- PROGRAM SELESAI ------------")
            x=0

    else:
        print("Eror: Masukkan Angka 1 atau 2!!!")
        time.sleep(2)
        reset()
        x=1