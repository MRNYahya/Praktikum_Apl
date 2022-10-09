#sequential search
def linearSearch(array,n,x):
    found = False
    for i in range(0,n):
        if(array[i]==x):
            print("",i)
            found = True
    if not(found==True):
        return 1
    return -1

array = [21,13,16,14,21,76,21]
x=21

print("Linear Search\n",array)
print("\nangka",x,"Ditemukan pada index:")
result = linearSearch(array, len(array), x)
if result==False:
    print("Element Not found")

#interpolation searh
#harus terurut dulu, ga support string
def interpolationSearch(arr,lo,hi,x):
    if (lo <= hi and x>= arr[lo]and x<=arr[hi]):
        pos = lo +((hi - lo)//(arr[hi]-arr[lo])*(x-arr[lo]))
        if arr[pos]==x:
            return pos
        if arr[pos]<x:
            return interpolationSearch(arr,pos+1,hi,x)
        if arr[pos]>x:
            return interpolationSearch(arr,pos-1,hi,x)
        return -1

arr = [10,12,13,16,18,19,20,22,29,30,33,35,42]
arr2= ["a","b","c","d"]

n = len(arr)
x=22
indeks = interpolationSearch(arr,0,n-1,x)

if indeks != -1:
    print("\nInterpolaton Search\n",array)
    print("\nangka",x,"Ditemukan pada index: \n",indeks)
else:
    print("\nElement not found")
            
#Binary search
#harus terurut
def binary(array,x,low,high):
    while low<= high:
        ditemukan = False
        mid = low +(high-low)//2
        if array[mid]== x:
            array[mid]=update
            ditemukan = True
        elif array[mid]<x:
            low = mid +1
        elif array[mid]>x:
            high = mid-1
    if ditemukan == False:
        return -1
    return mid
array = [3,4,5,6,7,7,8,9]
x=7
update = 10
result = binary(array,x,0,len(array)-1)

#merubah isi list bersamaan menggunakan search
print(array)
if result != -1:
    print("element is present at index: "+ str(result))
    print("array: ",array)



pengunjung ={"orang":["a","b","c","d"]}

#cia punya
def linearSearch(array,n,x):
    for i in range(0,n):
        if(array[i] == x):
            return i
    return -1

    x = input("| Masukkan data : ")
    n = len(pengunjung["orang"][0])

    for i in range(n):
        result = linearSearch(pengunjung["orang"][i], n, x)
        if result != -1:
            print(f"\nData berada pada identitas ke-{i+1}, indeks ke-{result}")
            break
    if result == -1:
        print("Element Not found")