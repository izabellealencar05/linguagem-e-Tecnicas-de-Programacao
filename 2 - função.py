def lista_numeros(lista, numero):
  return numero in lista
lista = [1, 2, 3, 5, 6, 7, 8, 9]
x = int(input('digite um numero: '))
esta_na_lista = lista_numeros (lista, x)
print(f'O número {x} está presente na lista? {esta_na_lista}') 
