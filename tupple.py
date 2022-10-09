#tuple: tidak dapat berubah datanya

tuple1=(1,2,3,4,5)
tuple2=(4,5.0,"enam",[7,8])

#nested tuple
tuple3=(1,(2,3),(4,5))

#packing tuple
tuple4= 1,2,3,"empat"

#unpacking tuple
a,b,c,d = tuple4

tuple5=("nama","nim")

print("\n",tuple1)
print("\n",tuple2[1])

print("\n",a)
print(b)
print(c)
print(d)

set1={1,2,3}
set2={"a",2,3.0}

print("\n",set1)

#Set List
print("-"*50)#------------------------------
setlist=set([1,0,5,8,3,4,9])
print("\n",setlist)

#set Kosong
setkosong=set()
print("")
print(type(setkosong))

#crud
myset={1,"lima"}
print("\n",myset)

#add
myset.add(2)
print("\n",myset)
myset.update([1,2,"awe"])
print(myset)
myset.update([2,6],[7,6,"abc"])
print(myset)

#remove
myset.discard("abc")
print("\n",myset)

myset.remove(1)
print(myset)

#pop
ab=set("apa kabar")
ab.pop()
print("\n",ab)

#clear
ab.clear()
print("\n",ab)

print("-"*50)#------------------------------------

#diagram ven
a={2,4,6,3,7,8}
b={1,5,9,0,3,2}

#union
print("\n",a|b)#bisa juga b|a

#intersection
print("\n",a&b)#irisan

#difference
print("\n",a-b)#ada di a tidak ada di b

#symetric difference
print("\n",a^b)#menampilkan yang berbeda dari a dengan b

#create
mydict={}
print("\n",mydict)
print(type(mydict))

mydict={1:"nama","NIM":[1,2,3]}
print("\n",mydict)

mydict2=dict([(2,3),(3,"nama")])
print("\n",mydict2)

mydict3=dict({1:'apple',2:"halo"})
print("\n",mydict3)

#read
print("\n",mydict.get("apple"))

#update
mydict["ABCD"]=1
print("\n",mydict)

mydict.update({"nama":5})
print("\n",mydict)

#pop
squares={1:1,2:4,3:9,4:16,5:25}
squares.pop(4)#kalau tanpa print dia hanya menghapus tanpa mengembalikan nilai

print("\n",squares)

#clear
squares.clear()
print("\n",squares)

#del: dia bakal menghapus, dan tidak dapat di panggil lagi