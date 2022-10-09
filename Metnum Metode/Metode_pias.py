import os

def reset():
    os.system('cls' if os.name == 'nt' else 'clear')

def trapint(f,a,b,trapezoids):
    
    cumulative_area=0

    a=float(a)
    b=float(b)
    trapezoids=float(trapezoids)

    i=(b-a)/trapezoids

    trailing_x=a
    leading_x=a+i

    while (a<=leading_x<=b) or (a>=leading_x>=b):
        area=(f(trailing_x)+f(leading_x))*i/2
        cumulative_area+=area

        leading_x+=i
        trailing_x+=i

    return cumulative_area

reset()
f = lambda x: x**2-2*x+3
selang = input("Selang :")
splitSelang = selang.split(",")
jumlahPias = int(input("Jumlah pias: "))
print(trapint(f, int(splitSelang[0]), int(splitSelang[1]), jumlahPias))
