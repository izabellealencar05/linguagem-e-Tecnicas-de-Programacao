qntd = int(input("quantos alunos? "))
for i in range(qntd):
    nome = str(input("qual o nome do aluno? "))
    nota = float(input("qual a nota do aluno? "))

    if 9 <= nota <= 10:
         print("sua nota é A")

    elif 8 <= nota <= 8.9:
        print("sua nota é B")

    elif 7 <= nota <= 7.9:
        print("sua nota é C")

    else:
        print("sua nota é F")

