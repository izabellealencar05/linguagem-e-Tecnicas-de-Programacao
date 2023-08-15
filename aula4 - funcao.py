nota = []
nome = []

def lenomenota():
    x = int(input("digite a qntd de aluno: "))
    for i in range(x):
        print("aluno {}".format(i))
        m = input("digite o nome do aluno: ")
        n = float(input("digite a nota do aluno: "))

        nota.append(n)
        nome.append(m)

def avalianota():
    for i in range(len(nome)):
        if nota[i] >= 9.0 and nota[i] <= 10:
            print('o aluno {} tem o conceito A e a nota {}'. format(nome[i], nota[i]))
        if nota[i] < 9.0 and nota[i] >= 8.0:
            print("o aluno {} tem o conceito B e nota {}". format(nome[i], nota[i]))
        if nota[i] >= 7.0 and nota[i] < 8.0:
            print("o aluno {} tem o conceito C e nota {}".format(nome[i], nota[i]))
        if nota[i] < 7.0 and nota[i] >= 0.0:
            print("o aluno {} tem o conceito F e nota {}".format(nome[i], nota[i]))

print("INICIO DO PROGRAMA")
lenomenota()
print("MEIO DO PROGRAMA")
avalianota()
print("FIM DO PROGRAMA")