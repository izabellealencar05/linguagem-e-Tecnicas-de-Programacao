import os
import time


def menu():
    while True:

        os.system('cls')
        print("           M E N U ")
        print('1. CRIAR UMA LISTA DE INTEIRO E INSERIR n ELEMENTOS')
        print('2. INVERTER A LISTA DE INTEROS')
        print('3. RETORNAR O PRODUTO DOS ELEMENTOS DA LISTA CRIADA(recursiva)')
        print('4. IMPRIMIR A LISTA')
        print('5- CRIAR UM DICIONARIO DE n ALUNOS COM AS RESPECTIVAS NOTAS')
        print('6. IMPRIRMIR OS ALUNOS COM SUAS NOTAS')
        print('7. ALTERAR A NOTA DE UM ALUNO DO DICIONARIO')
        print('8. RETORNAR UMA LISTA DOS ELEMENTOS REPETIDOS DE DUAS LISTAS - (OBTER AS DUAS LISTAS')
        print('TECLAR <zero> ou <sair> PARA ABANDONAR O PROGRAMA')
        op = input("digite a opção: ")

        if op == 'sair' or op == '0':
            break
        if int(op) == 1:
            l = crialista()
            print(l)
        if int(op) == 2:
            l = inverteLista(l)
            time.sleep(1)
            print(l)

        if int(op) == 3:
            print('O produto da lista é: ', produtoLista(l))
            time.sleep(2)
        if int(op) == 4:
            imprimeLista(l)
            time.sleep(1)

        if int(op) == 5:
            d = alunodic()
            imprimeDic(d)

        if int(op) == 6:
            imprimeDic(d)

        if int(op) == 7:
            al = alteranota(d)
            imprimeDic(al)

        if int(op) == 8:
            lst = terceiraLista()
            for i in lst:
                print(i)
            time.sleep(5)
            print('A lista 3 é :', retornaRepete(lst))
            time.sleep(2)


def crialista():
    l = []
    x = int(input('Função cria Lista. Quantos elementos pra lista  '))
    while x > 0:
        i = int(input('Digite o elemento: '))
        l.append(i)
        x = x - 1
    return l



def inverteLista(l):
    l.reverse()
    return l


def imprimeLista(lst):
    print('A lista a ser impressa é: ', lst)


def produtoLista(l):
    if l == []:
        return 1
    else:
        return l[0] * produtoLista(l[1:])


def alunodic():
    aluno = {}
    x = int(input('Função cria Dicionario. Quantos elementos pra dicionáro  '))
    while x > 0:
        nome = input('Digite o nome do aluno: ')
        nota = float(input('Digite a nota: '))
        aluno.get(nome)
        aluno[nome] = nota
        x = x - 1
    return aluno


def alteranota(aluno):
    nome = input('Digite o nome do aluno: ')
    nota = float(input('Digite a nota: '))
    aluno[nome] = nota
    return aluno


def imprimeDic(aluno):
    print(aluno)
    time.sleep(5)


def terceiraLista():
    l = []
    l1 = []
    x = int(input('Quantos elementos pra lista 1 ? '))
    while x > 0:
        i = int(input('Digite o {} elemento pra lista 1: '.format(x)))
        l.append(i)
        x = x - 1
    x = int(input('Quantos elementos para lista 2 ?'))
    while x > 0:
        i = int(input('Digite o {} elemento pra lista 2: '.format(x)))
        l1.append(i)
        x = x - 1
    return (l, l1)


def retornaRepete(lst):
    l1 = lst[0]
    l2 = lst[1]
    print(l1)
    print(l2)
    time.sleep(3)
    l3 = []
    i = 0
    while i < len(l2):
        j = 0
        while j < len(l1):
            if l1[j] == l2[i]:
                l3.append(l2[i])
                break
            j = j + 1
        i = i + 1
    return (l3)
menu()
