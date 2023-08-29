def buscabin(l, x, inicio, fim):
    if inicio > fim:
        return 0
    meio = (inicio + fim) // 2
    if x == l[meio]:
        return meio
    elif x < l[meio]:
        return buscabin(l, x, inicio,  meio - 1)
    else:
        return buscabin(l, x, meio + 1, fim)
l = []

for i in range(100, 200):
    l.append(i)
print(l)

print('inicio do programa')
x = int(input('digite um valor para pesquisar na lista: '))

while x != 0:
    pos = buscabin(l, x, 0, len(l))
    if pos != 0:
        print('{0} esta na posicao {1} da lista'.format(x, pos))
    else:
        print('{0} nao esta na lista'.format(x))
    x = int(input("digite um valor para pesquisar na lista: "))
print("FIM")
