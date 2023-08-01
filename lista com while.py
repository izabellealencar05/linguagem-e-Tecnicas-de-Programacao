lista = [1, 2, 3, 4, 5, 6, 7, 8]
max_valor = lista[0]
min_valor = lista[0]
total = 0
valor = 0
while valor < len(lista):
    if lista[valor] > max_valor:
        max_valor = lista[valor]
    if lista[valor] < min_valor:
        min_valor = lista[valor]
    total = total + lista[valor]
    lista = valor + 1

print('o total da lista é: ', total)
print('maior valor: ', max_valor)
print('o menor valor é: ', min_valor)