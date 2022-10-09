import pandas as pds
import matplotlib.pyplot as mpp
import numpy as np
from scipy import stats
import math
import os

#Deklarasi variabel global untuk menampung dataframe
dataframe = pds.read_csv("C:/Users/User/OneDrive/Documents/CS/Phyton/Probas Grafik/StudentsPerformance.csv")

#Deklarasi fungsi mencari tipe data
def tipe_data():
    reset()
    print('+','-'*50,'+')
    print('              Tipe Data Pada Dataframe')
    print('+','-'*50,'+')
    desc = dataframe.dtypes
    print(desc.to_string())
    print('+',"-"*50,'+')
    print("")
    stop()

#Deklarasi fungsi distribusi frekuensi untuk writing_score
def DisFrek_writing():
    reset()
    DataFrame_writing = (sorted(dataframe['writing_score']))
    nilai_min = min(dataframe['writing_score']) # Dapat digunakan sebagai nilai bawah kelas
    nilai_max = max(dataframe['writing_score'])
    nilai_total = dataframe['writing_score'].count()

    print('+',"-"*33,'+')
    print("Berikut tabel distribusi untuk\nwriting_score")
    print('+',"-"*33,'+')
    print ("| Nilai"," Frekuensi\t   |",sep='\t\t|')
    print('+',"-"*33,'+')
    frekuensi = 0
    for nilai_min in range (nilai_min, nilai_max, 10):
        nilai_atas_kelas = nilai_min + 10 - 1
        nilai_bawah_kelas = nilai_min
        for nilai_min in range (nilai_min, nilai_atas_kelas + 1, 1):
            data_pada_interval = DataFrame_writing.count(nilai_min)
            frekuensi = frekuensi + data_pada_interval
            if nilai_min == nilai_atas_kelas:
                print ("|", nilai_bawah_kelas, " - ", nilai_atas_kelas , "\t |", frekuensi, "\t\t   |")
                frekuensi = 0
    print('+',"-"*33,'+')
    print("|\tTotal    |    ", nilai_total, "\t   |")
    print('+',"-"*33,'+')
    print("")
    stop()

#Deklarasi fungsi distribusi frekuensi untuk reading_score
def DisFrek_reading():
    reset()
    DataFrame_reading = (sorted(dataframe['reading_score']))
    nilai_min = min(dataframe['reading_score']) #Dapat digunakan sebagai nilai bawah kelas
    nilai_max = max(dataframe['reading_score'])
    nilai_total = dataframe['reading_score'].count()

    print('+',"-"*33,'+')
    print("Berikut tabel distribusi untuk\nreading_score")
    print('+',"-"*33,'+')
    print ("| Nilai"," Frekuensi\t   |",sep='\t\t|')
    print('+',"-"*33,'+')
    frekuensi = 0
    for nilai_min in range (nilai_min, nilai_max, 10):
        nilai_atas_kelas = nilai_min + 10 - 1
        nilai_bawah_kelas = nilai_min
        for nilai_min in range (nilai_min, nilai_atas_kelas + 1, 1):
            data_pada_interval = DataFrame_reading.count(nilai_min)
            frekuensi = frekuensi + data_pada_interval
            if nilai_min == nilai_atas_kelas:
                print ("|", nilai_bawah_kelas, " - ", nilai_atas_kelas , "\t |", frekuensi, "\t\t   |")
                frekuensi = 0
    print('+',"-"*33,'+')
    print("|\tTotal    |    ", nilai_total, "\t   |")
    print('+',"-"*33,'+')
    print("")
    stop()

#Deklarasi fungsi menu untuk menampilkan tabel distribusi frekuensi
def menu_DisFrek():
    reset()
    print('+',"-"*50,'+')
    print('              Menu Distribusi Frekuensi')
    print('+',"-"*50,'+')
    print('\t1) Distribusi Frekuensi Writing_score')
    print('\t2) Distribusi Frekuensi Reading_score')
    print('\t0) Kembali')
    print('+',"-"*50,'+')
    choice = int(input('Pilih : '))
    if choice == 1:
        DisFrek_writing()
    elif choice == 2:
        DisFrek_reading()
    elif choice == 0:
        menu_utama()
    else:
        print('\nMasukkan angka yang ada !!!')
        stop()

#Deklarasi fungsi tabel histogram
def histogram():
    dataframe.hist(figsize=(10,10), bins=10)
    mpp.tight_layout()
    mpp.show()

#Deklarasi fungsi nilai tendensi sentral
def tendensi_sentral():
    reset()
    #Mencari nilai mean
    WritScor_mean = dataframe['writing_score'].mean()
    ReadScor_mean = dataframe['reading_score'].mean()
    #Mencari nilai median
    WritScor_median = dataframe['writing_score'].median()
    ReadScor_median = dataframe['reading_score'].median()
    #Mencari nilai modus
    WritScor_modus = stats.mode(dataframe['writing_score'])
    ReadScor_modus = stats.mode(dataframe['reading_score'])
    #Mencari nilai minimum
    WritScor_min = dataframe['writing_score'].min()
    ReadScor_min = dataframe['reading_score'].min()
    #Mencari nilai maksimum
    WritScor_max = dataframe['writing_score'].max()
    ReadScor_max = dataframe['reading_score'].max()

    print('+',"-"*50,'+')
    print('         Nilai tendensi sentral writing_score')
    print('+',"-"*50,'+')
    print('\tNilai Mean\t: ', WritScor_mean)
    print('\tNilai Median\t: ', WritScor_median)
    print('\tNilai Modus\t: ', WritScor_modus[0][0])
    print('\tNilai Min\t: ',WritScor_min)
    print('\tNilai Max\t: ',WritScor_max)
    print('+',"-"*50,'+')
    print("")
    print('+',"-"*50,'+')
    print('         Nilai tendensi sentral reading_score')
    print('+',"-"*50,'+')
    print('\tNilai Mean\t: ', ReadScor_mean)
    print('\tNilai Median\t: ', ReadScor_median)
    print('\tNilai Modus\t: ', ReadScor_modus[0][0])
    print('\tNilai Min\t: ', ReadScor_min)
    print('\tNilai Max\t: ',ReadScor_max)
    print('+',"-"*50,'+')
    print("")
    stop()

#Mencari nilai variansi untuk writing_score
def WritScor_variansi():
    reset()
    #Mencari nilai standar deviasi untuk writing_score
    WritScor_StanV = dataframe['writing_score'].std()
    #Mencari nilai range dari writing_score
    q1 = dataframe['writing_score'].min()
    q3 = dataframe['writing_score'].max()
    r = q3 - q1
    #Mencari nilai interkuartil dari writing_score
    WritScor_IntQuar = dataframe['writing_score'].quantile()
    #Mencari nilai variansi untuk writing_score
    WritScor_mean = dataframe['writing_score'].mean()
    WritScor_kv = (WritScor_StanV/WritScor_mean) * 100/100

    print('+',"-"*50,'+')
    print('         Nilai Variansi writing_score')
    print('+',"-"*50,'+')
    print('Nilai standar deviasi writing_score\n-> ', WritScor_StanV)
    print('+',"-"*50,'+')
    print('Nilai range writing_score\n-> ', r)
    print('+',"-"*50,'+')
    print('Nilai interkuartil writing_score\n-> ', WritScor_IntQuar)
    print('+',"-"*50,'+')
    print('Rata-rata writing_score\n-> ', WritScor_mean)
    print('Standar deviasi writing_score\n-> ', WritScor_StanV)
    print('Nilai variansi writing_score\n-> ', WritScor_kv)
    print('+',"-"*50,'+')
    print("")
    stop()

#Mencari nilai variansi untuk reading_score
def ReadScor_variansi():
    reset()
    #Mencari nilai standar deviasi untuk reading_score
    ReadScor_StanV = dataframe['reading_score'].std()
    #Mencari nilai range dari reading_score
    q1 = dataframe['reading_score'].min()
    q3 = dataframe['reading_score'].max()
    r = q3 - q1
    #Mencari nilai interkuartil dari reading_score
    ReadScor_IntQuar = dataframe['reading_score'].quantile()
    #Mencari nilai variansi untuk reading_score
    ReadScor_mean = dataframe['reading_score'].mean()
    ReadScor_kv = (ReadScor_StanV/ReadScor_mean) * 100/100

    print('+',"-"*50,'+')
    print('         Nilai Variansi reading_score')
    print('+',"-"*50,'+')
    print('Nilai standar deviasi reading_score\n-> ', ReadScor_StanV)
    print('+',"-"*50,'+')
    print('Nilai range reading_score\n-> ', r)
    print('+',"-"*50,'+')
    print('Nilai interkuartil reading_score\n-> ', ReadScor_IntQuar)
    print('+',"-"*50,'+')
    print('Rata-rata reading_score\n-> ', ReadScor_mean)
    print('Standar deviasi reading_score\n-> ', ReadScor_StanV)
    print('Nilai variansi reading_score\n-> ', ReadScor_kv)
    print('+',"-"*50,'+')
    print("")
    stop()

#Deklarasi fungsi menu mencari nilai variansi
def menu_variansi():
    reset()
    print('+',"-"*50,'+')
    print('              Menu Tampil Variansi')
    print('+',"-"*50,'+')
    print('\t1) Nilai variansi writing_score')
    print('\t2) Nilai variansi reading_score')
    print('\t0) Kembali')
    print('+',"-"*50,'+')
    choice = int(input('Pilih : '))
    if choice == 1:
        WritScor_variansi()
    elif choice == 2:
        ReadScor_variansi()
    elif choice == 0:
        menu_utama()
    else:
        print('\nMasukkan angka yang ada !!!')
        stop()

#Deklarasi fungsi tampil box plot
def box_plot():
    dataframe.boxplot()
    mpp.tight_layout()
    mpp.show()

#Deklarasi fungsi tampil scatter plot
def scatter_plot():
    fig, ax = mpp.subplots()
    _ = ax.scatter(dataframe['reading_score'], dataframe['writing_score'])
    _ = ax.set_title('Score Dataset')
    _ = ax.set_xlabel('reading_score')
    _ = ax.set_ylabel('writing_score')
    mpp.show()

#Mencari nilai skewness dan kurtosis untuk writing_score
def WritScor_skewkurto():
    reset()
    #Mencari nilai mean, modus, dan standar deviasi
    WritScor_mean = dataframe['writing_score'].mean()
    WritScor_modus = stats.mode(dataframe['writing_score'])
    WritScor_StanV = dataframe['writing_score'].std()
    #Mencari nilai skewness dari variabel di atas
    WritScor_skew = (WritScor_mean - WritScor_modus[0][0]) / WritScor_StanV
    #Mencari nilai Q1, Q3, P10, dan P90
    q1 = dataframe['writing_score'].min()
    q3 = dataframe['writing_score'].max()
    p10 = np.percentile(dataframe['writing_score'], 10)
    p90 = np.percentile(dataframe['writing_score'], 90)
    #Mencari nilai kurtosis dari variabel di atas
    WritScor_kurt = ((q3 - q1) / 2) / p90 - p10

    print('+',"-"*50,'+')
    print('           Nilai Skewness writing_score')
    print('+',"-"*50,'+')
    print('Nilai rata-rata\t\t\t: ', WritScor_mean)
    print('Nilai modus\t\t\t: ', WritScor_modus[0][0])
    print('Nilai standar deviasi\t\t: ', WritScor_StanV)
    print('Nilai skewness writing_score\n-> ', WritScor_skew)
    print('+',"-"*50,'+')
    print("")
    print('+',"-"*50,'+')
    print('           Nilai Kurtosis writing_score')
    print('+',"-"*50,'+')
    print('Q1\t\t\t\t: ', q1)
    print('Q3\t\t\t\t: ', q3)
    print('P10\t\t\t\t: ', p10)
    print('P90\t\t\t\t: ', p90)
    print('Nilai kurtosis writing_score\n-> ', WritScor_kurt)
    print('+',"-"*50,'+')
    print("")
    stop()

#Mencari nilai skewness dan kurtosis untuk reading_score
def ReadScor_skewkurto():
    reset()
    #Mencari nilai mean, modus, dan standar deviasi
    ReadScor_mean = dataframe['reading_score'].mean()
    ReadScor_modus = stats.mode(dataframe['reading_score'])
    ReadScor_StanV = dataframe['reading_score'].std()
    #Mencari nilai skewness dari variabel di atas
    ReadScor_skew = (ReadScor_mean - ReadScor_modus[0][0]) / ReadScor_StanV
    #Mencari nilai Q1, Q3, P10, dan P90
    q1 = dataframe['reading_score'].min()
    q3 = dataframe['reading_score'].max()
    p10 = np.percentile(dataframe['reading_score'], 10)
    p90 = np.percentile(dataframe['reading_score'], 90)
    #Mencari nilai kurtosis dari variabel di atas
    ReadScor_kurt = ((q3 - q1) / 2) / p90 - p10

    print('+',"-"*50,'+')
    print('           Nilai Skewness reading_score')
    print('+',"-"*50,'+')
    print('Nilai rata-rata\t\t\t: ', ReadScor_mean)
    print('Nilai modus\t\t\t: ', ReadScor_modus[0][0])
    print('Nilai standar deviasi\t\t: ', ReadScor_StanV)
    print('Nilai skewness reading_score\n-> ', ReadScor_skew)
    print('+',"-"*50,'+')
    print("")
    print('+',"-"*50,'+')
    print('           Nilai Kurtosis reading_score')
    print('+',"-"*50,'+')
    print('Q1\t\t\t\t: ', q1)
    print('Q3\t\t\t\t: ', q3)
    print('P10\t\t\t\t: ', p10)
    print('P90\t\t\t\t: ', p90)
    print('Nilai kurtosis reading_score\n-> ', ReadScor_kurt)
    print('+',"-"*50,'+')
    print("")
    stop()

#Deklarasi fungsi menu untuk mencari nilai skewness dan kurtosis
def menu_skewkurto():
    reset()
    print('+',"-"*50,'+')
    print('              Menu Tampil Variansi')
    print('+',"-"*50,'+')
    print('\t1) Skewness dan kurtosis writing_score')
    print('\t2) Skewness dan kurtosis reading_score')
    print('\t0) Kembali')
    print('+',"-"*50,'+')
    choice = int(input('Pilih : '))
    if choice == 1:
        WritScor_skewkurto()
    elif choice == 2:
        ReadScor_skewkurto()
    elif choice == 0:
        menu_utama()
    else:
        print('\nMasukkan angka yang ada !!!')
        stop()

#Deklarasi fungsi menu untuk box plot, scatter plot, dan nilai skewness dan kurtosis
def grafik():
    reset()
    print('+','-'*50,'+')
    print('              Menu Tampil Grafik Data')
    print('+','-'*50,'+')
    print('\t1) Tampilkan dalam bentuk box plot')
    print('\t2) Tampilkan dalam bentuk scatter plot')
    print('\t3) Tampilkan nilai skewness dan kurtosis')
    print('+','-'*50,'+')
    choice = int(input('Pilih : '))
    if choice == 1:
        box_plot()
    elif choice == 2:
        scatter_plot()
    elif choice == 3:
        menu_skewkurto()
    else:
        print('\nMasukkan angka yang ada !!!')
        stop()

def reset():
    os.system("cls")

def stop():
    os.system("pause")

def menu_utama():
    reset()
    print('+','-'*50,'+')
    print('              Menu Analisa Statistika')
    print('+','-'*50,'+')
    print('\t1) Tampilkan tipe data')
    print('\t2) Tampilkan tabel distribusi frekuensi')
    print('\t3) Tampilkan tabel histogram')
    print('\t4) Tampilkan nilai tendensi sentral')
    print('\t5) Tampilkan nilai variansi')
    print('\t6) Tampilkan grafik data')
    print('\t0) Keluar')
    print('+','-'*50,'+')

    choice = int(input('Pilih : '))
    if choice == 1:
        tipe_data()
    elif choice == 2:
        menu_DisFrek()
    elif choice == 3:
        histogram()
    elif choice == 4:
        tendensi_sentral()
    elif choice == 5:
        menu_variansi()
    elif choice == 6:
        grafik()
    elif choice == 0:
        exit(0)
    else:
        print('\nMasukkan angka yang ada !!!')
        stop()

if __name__ == ("__main__"):
    while(True):
        menu_utama()