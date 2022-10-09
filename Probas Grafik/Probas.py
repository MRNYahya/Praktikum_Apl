import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import csv

reading_score =[0]
writing_score =[0]

def reset():
    os.system('cls' if os.name == 'nt' else 'clear')

def dataGrafik():
    df = pd.read_csv("C:/Users/User/OneDrive/Documents/CS/Phyton/Probas Grafik/StudentsPerformance.csv")
    Data1 = (df['reading_score'][0])
    Data2 = (df['writing_score'][0])
    reading_score[0] = Data1
    writing_score[0] = Data2
    print(df.head())

def grafik():
    dataGrafik()
    labels = ['reading_score','writing_score']
    x = np.arange(len(labels))
    width = 0.10
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, reading_score, width, label='reading')
    rects2 = ax.bar(x + width / 2, writing_score, width, label='writing')

    ax.set_ylabel('Score')
    ax.set_title('Grafik Score')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    fig.tight_layout()
    plt.show()

    print("|==================================================|")
    print("              < Kembali: Tekan Enter >              ")
    input("                            ")


grafik()