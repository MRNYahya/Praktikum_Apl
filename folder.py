# menulis w (write)
f = open("test.txt",mode="w")

# membaca r (read)
f = open("test.txt", mode="r")
# menambahkan a ke file (add)
f = open("test.txt",mode="a")

f = open("contoh.txt","r",encoding ="utf-8")
a=f.read(4)
print(a)

# manggil semuanya
a=f.read()
print(a)

f.tell()
f.seek()

f.readlines()
"abcdefg"