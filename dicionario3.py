notas = {
    'joao': 9,
    'maria' : 10,
    'jose' : 4
}
notas.popitem() #elimina o ultimo elemento
print(notas)
print(notas)
print(" a nota de maria é: ", notas.get('maria'))
notas['maria'] = 9
print("a nova nota de maria é: ", notas.get('maria'))

print('antigo dicionario--------', notas)
nome = 'pedro'
nota = 9.0
notas[nome] = nota
print(notas)
del notas['maria']
print('delecao de maria', notas)
