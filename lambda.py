print("")
#greet bisa String
def greet (name):
    print("Hello "+name)
print("(greet bisa string)")
greet("Yahya")

print("")

#greet bisa int
def x (umur):
    print(umur)
print("(greet bisa int)")
x(18)

print("")

#fungsi lambda
print("(fungsi lambda)")
a=3
b=5
abc=(lambda x,y:x*y)(a,b)
print("Hasil: ",abc)

print("")

#perkalian list dengan list lain
print("(perkalian list dengan list lain)")
angka1=[1,5,4,0]
angka2=[3,4,5,6]
filter= map(lambda x,y: x*y, angka1,angka2)
print(list(filter))

print("")

#perkalian angka ke dalam list
print("(perkalian angka ke dalam list)")
angka=[1,5,4,7,8]
filter=map(lambda x:x*2,angka)
print(list(filter))

print("")

#tanpa global
def my_func():
    x=10
    print("(tanpa global)\nValue outside function: ",x)

x=20
my_func()
print("Value outside function: ",x)

print("")

#global
def my_fun(a,b):
    global x
    x = a+b

my_fun(1,2)
print("(global)\nx = ",x)

print("")

#Asterik
print("(Asterik)")
def greet (*names):
    for name in names:
        print("Hello", name)

greet("Sulis","Yahya","Agung","devi","ridho")
