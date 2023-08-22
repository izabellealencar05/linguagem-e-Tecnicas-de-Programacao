def ledados():
    x = int(input('digite o valor da base: '))
    y = int(input('digite o valot do expoente: '))
    return(x , y)

def pot(x, y):
    p = 1
    for _ in range(y):
        p = p * x
    return(p)
def imprime(k):
        print("o resultado da potencia de y sobre x e ", k)

s, w = ledados()
z = pot(s, w)
imprime(z)
