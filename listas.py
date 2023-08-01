lista = [3, 4, 6, 7, 8]

max_valor = lista[0]
min_valor = lista[0]
total = 0
for valor in lista:
    if valor > max_valor:
        max_valor = valor
    if valor < min_valor:
        min_valor = valor
    total = total + valor
print('o maior valor da lista é', max_valor)
print('o menor valor da lista é', min_valor)
print('total da lista', total)
