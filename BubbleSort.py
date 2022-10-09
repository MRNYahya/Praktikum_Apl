import os

# Creating a bubble sort function  
def bubble_sort(list1):  
    # Outer loop for traverse the entire list  
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1
  
list1 = ["a","b","z","c"]
os.system('cls')
banyak=int(input("Mau masukkan berapa banyak data: "))
for i in range(banyak):
    angka=(str((input("Masukkan angka: "))))
    list1.extend([angka])
    print("= ",list1,"\n")

print("The unsorted list is: ", list1)  
# Calling the bubble sort function  
print("The sorted list is: ", bubble_sort(list1))  