def encontrar_maior_elemento (lista, limite):
  for i,  numero in enumerate(lista):
    if numero > limite:
      return i
  return -1

lista = [1, 3, 5, 6, 7, 9]
limite = 5
maior = encontrar_maior_elemento(lista, limite)
print(f'O índice do primeiro número maior que {limite} é: {maior}')
      
