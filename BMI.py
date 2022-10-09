x=1
while(x==1):
    print("")
    umur = float(input("Masukkan umur(tahun): "))
    if umur >= 20:
        a = float(input("masukkan berat (kg): "))
        b = float(input("masukkan tinggi (cm): "))
        BMI = a/(b)**2
        if BMI < 18.5:
            print ("Berat badan kurang")
            print("")
            ulang = int(input("Apakah anda ingin mengetes ulang?\n1.Iya\n2.Tidak\n\nJawaban: "))
            if ulang==1:
                x=1
            else:
                x=0

        elif 18.5 <= BMI < 25.0:
            print ("normal")
            print("")
            ulang = int(input("Apakah anda ingin mengetes ulang?\n1.Iya\n2.Tidak\n\nJawaban: "))
            if ulang==1:
                x=1
            else:
                x=0
            
        elif 25.0 <=BMI< 30.0:
            print ("Kegemukan")
            print("")
            ulang = int(input("Apakah anda ingin mengetes ulang?\n1.Iya\n2.Tidak\n\nJawaban: "))
            if ulang==1:
                x=1
            else:
                x=0
            
        elif BMI >= 30.0:
            print ("obesitas")
            print("")
            ulang = int(input("Apakah anda ingin mengetes ulang?\n1.Iya\n2.Tidak\n\nJawaban: "))
            if ulang==1:
                x=1
            else:
                x=0

    else:
        print('BMI tidak cocok untuk anda')
        print("")
        ulang = int(input("Apakah anda ingin mengetes ulang?\n1.Iya\n2.Tidak\n\nJawaban: "))
        if ulang==1:
            x=1
        else:
            x=0