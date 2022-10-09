import os
import datetime
import time
from playsound import playsound

def reset():
    os.system('cls' if os.name == 'nt' else 'clear')

reset()
x=1
while True :
    try:
        print("=================== Setel Alarm ===================")
        alarmH = int(input(" Jam: "))
        alarmM = int(input(" Menit: "))
        print("")
        break
    except:
        print("Masukkan Angka!")
        time.sleep(3)
        reset()
        x=0

while True :
    try:
        AmPm = str(input(" Am / Pm: "))
        print("")
        print("="*51)
        print("")
        print(" Ket:")
        print(" Alarm akan menyala pada pukul {}.{} {} ".format (alarmH, alarmM, AmPm))
        print("")
    except:
        print("Masukkan Am atau Pm!")
        time.sleep(3)
        reset()

    if (AmPm =="Am"or"am"or"AM"):
        alarmH = alarmH

    elif (AmPm == "Pm"or"pm"or"PM"):
        alarmH = alarmH + 12



    while(1 == 1):
        if(alarmH == datetime.datetime.now().hour and 
            alarmM == datetime.datetime.now().minute):
            print("="*51)
            print("               AYOK BANGUN GAES!!!")
            print("="*51)
            playsound('qwerty.mp3')
            break
    break