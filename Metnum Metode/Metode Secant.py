import os

os.system('cls')

print("------------------------------------------")
print("-- 2009106029 Muhamad Rizky Nilzamyahya --")
print("------------------------------------------\n")

def secant(f,x0,x1,e = 10**-4,N=100):

# untuk perulangan tampilan
  for i in range (0,N):
    print("%d   | %f    | %f    " %(i,x1,f(x1)))
    if abs(f(x1)) < e:
      return x1,i
# untuk perulangan langkah" mencari jawaban
    x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
    x0 = x1
    x1 = x2
  print("Maximum iteration")
  return x1, i

# f merupakan fungsi pada soal
f  = lambda x: x**3 + 2*x**2 + 10*x - 20
x0 = 1
x1 = 2

# output mencari jawaban dan jumlah iterasi
x_root, iteration = secant(f,x0,x1)
print('\nResult : ', x_root)
print('In %d iteration' %iteration)
print("")