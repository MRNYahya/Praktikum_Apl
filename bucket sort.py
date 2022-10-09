def main():
    input_list = []
    banyak=int(input("Mau masukkan berapa banyak data: "))
    for i in range(banyak):
        angka=(int((input("Masukkan angka: "))))
        input_list.extend([angka])
    print('\nORIGINAL LIST:')
    print(input_list)
    sorted_list = bucket_sort(input_list)
    print('SORTED LIST ASCENDING:')
    print(sorted_list)

def bucket_sort(input_list):
    # Temukan nilai maksimum dalam daftar dan gunakan panjang daftar untuk menentukan nilai mana dalam daftar yang masuk ke ember mana 
    max_value = max(input_list)
    size = max_value/len(input_list)

    # Buat n ember kosong di mana n sama dengan panjang daftar input
    buckets_list= []
    for x in range(len(input_list)):
        buckets_list.append([]) 

    # Masukkan elemen daftar ke dalam ember yang berbeda berdasarkan ukurannya
    for i in range(len(input_list)):
        j = int (input_list[i] / size)
        if j != len (input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    # Urutkan elemen di dalam bucket menggunakan Insertion Sort
    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])
            
    # Gabungkan ember dengan elemen yang diurutkan ke dalam satu daftar
    final_output = []
    for x in range(len (input_list)):
        final_output = final_output + buckets_list[x]
    return final_output


def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var

main()