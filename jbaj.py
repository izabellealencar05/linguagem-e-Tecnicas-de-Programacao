class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    def grava(c):
        f = open('cliente.txt', 'a')
        f.write(c.nome)
        f.write(c.sobrenome)
        f.write(c.cpf)
        f.close()
    def ler(c):
        f= open('cliente.txt', 'r')
        print('leitura de cliente')
        l = f.rand()
        print(l)

class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite

    def grava(c):
        f = open('conta.txt', 'a')
while True:
    print('1 - digite os dados')
    print('2 - ler arquivo e imprimir')
    print('3 - sair ')

    op = int (input("digite a opcao: "))
    if op == 3:
        break
    if op == 1:
        n = input("digite nome do cliente: ")
        s = int(input("digite o sobrenome do cliente: "))
        c = int(input("digite o cpf do cliente: "))
        num = int(input("digite o numero da conta: "))
        sld = int(input("digite o saldo da conta: "))
        lmt = int(input("digite o limite da conta: "))
    if op == 2:
        print(cliente.ler())
        print()
