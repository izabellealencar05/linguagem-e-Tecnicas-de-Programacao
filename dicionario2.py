notas = {
    "joao" : 6,
    'maria' : 8,
    'iza' : 9
}

print('antigo dicionario')
print(notas)
nome = input("digite o nome do aluno: ")

if notas.get(nome):
    print('ja existe o aluno', nome)
else:
    nota = float(input("digite a nota do aluno: "))
    notas[nome] = nota
    print('-----novo dicionario-----')
    print(notas)

