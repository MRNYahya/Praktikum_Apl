mhs=0
print("------------ Nilai rata-rata Mahasiwa ------------")
orang=(int(input("Jumlah mahasiswa: ")))

while mhs<orang:
    quis=(float(input("Nilai Quis: ")))
    tugas=(float(input("Nilai Tugas: ")))
    UTS=(float(input("Nilai UTS: ")))
    rata_rata = (0.3 * quis) + (0.2 * tugas) + (0.5 * UTS)
    mhs = mhs+1
    print("\nMahasiswa ke-",mhs,"memiliki rata-rata: ",rata_rata)
    print("-"*50)