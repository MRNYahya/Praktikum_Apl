import os
os.system('cls')
def partisiAsc(data,start,akhir):
    i = (start-1)
    pivot=data[akhir]

    for j in range(start, akhir):
        if data[j] <= pivot:
            i = i+1
            data[i], data[j] = data[j], data[i]
    data[i+1], data[akhir] = data[akhir], data[i+1]
    return (i+1)

def quickSortAsc(data, start, akhir):
    if len(data) == 1:
        return data
    if start< akhir:
        pa = partisiAsc(data, start, akhir)
        quickSortAsc(data, start, pa-1)
        quickSortAsc(data, pa+1, akhir)

def partisiDesc(data, start, akhir):
    i = (start-1)
    pivot = data[akhir]
    for j in range(start, akhir):
        if data[j] >= pivot:
            i = i+1
            data[i], data[j] = data[j], data[i]
    data[i+1], data[akhir] = data[akhir], data[i+1]
    return (i+1)

def quickSortDesc(data, start, akhir):
    if len(data) == 1:
        return data
    if start < akhir:
        pa = partisiDesc(data, start, akhir)
        quickSortDesc(data, start, pa-1)
        quickSortDesc(data, pa+1, akhir)

data = ["AYAM","Monyet","Bebek"]
n = len(data)

print('Urutan kalimat sebelum diurutkan      : ', end="")
for i in range(len(data)):
    print(data[i], end=" ")

print('Urutan kalimat setelah diurutkan secara ascending : ')
quickSortAsc(data, 0, n-1)
for i in range(len(data)):
    print(data[i], end=" ")

print('Urutan kalimat setelah diurutkan secara descending : ')
quickSortDesc(data, 0, n-1)
for i in range(len(data)):
    print(data[i], end=" ")