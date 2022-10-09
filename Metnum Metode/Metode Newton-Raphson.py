import os

os.system('cls')

print("------------------------------------------")
print("-- 2009106029 Muhamad Rizky Nilzamyahya --")
print("------------------------------------------\n")

def newtons(f,df,x0):
  e = 10**-4 # batasan untuk memperkirakan apakah f(x) sudah mendekati 0
  N = 100 # batas maksismum iterasi

  # untuk perulangan menampilkan langkah langkah mencari jawaban, setelah menemukan jawabannya akan di hitung iterasi nya
  for i in range (0,N):
    print("%d   | %f    | %f    " %(i,x0,f(x0)))
    if abs(f(x0)) < e:
      return x0,i
    if df(x0) == 0:
      print("Zero derivative")
      return None
    x0 = x0 - f(x0)/df(x0)
  print("Maximum iteration")
  return x0, i

# f merupakan fungsi pada soal
# df merupakan turunan pertama dari fungsi f
# x0 merupakan tebakan awal nilai akar
f  = lambda x: x**3 + 2*x**2 + 10*x - 20
df = lambda x: 3*x**2 + 4*x + 10
x0 = 1

x_root, iteration = newtons(f,df,x0)
print('\nResult : ', x_root)
print('In %d iteration' %iteration)
print("")