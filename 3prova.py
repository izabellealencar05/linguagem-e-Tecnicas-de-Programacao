class Cliente():
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def grava(c):
        f = open ('cliente.txt', 'a') #"a" serve para abrir um arquivo, se ele ja estiver criado ele abrirá em modo de edicoa
        f.write(c.nome)
        f.write(c.sobrenome)
        f.write(c.cpf)
        f.close()

    def ler(r): #o "r" serve para abrir um arquivo e apenas le-lo, e nao fazer nenhuma modificacao
        f = open ("cliente.txt", 'r')
        l = f.read
        print(l)
        for i in f:
            print(i)

    def imprimir(self):
        print(f"Nome: {self.nome} ")
        print(f"Sobrenome: {self.sobrenome}")
        print(f"CPF: {self.cpf}")

class Conta():
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def grava(c):
        f = open('conta.txt', 'a')
        f.write(c.cliente)
        f.write(c.numero)
        f.write(c.saldo)
        f.write(c.limite)
        f.close()



    def ler(c):
        f = open('conta.txt', 'r')
        for i in f:
            print(i)


def menu():
    print('================MENU===============')
    print('|  1 - inserir dados do cliente   |')
    print("|  2 - inserir dados da conta     |")
    print("|  3 - imprimir dados do cliente  |")
    print("|  4 - imprimir dados da conta    |")
    print("===================================")

menu()
op = int(input("digite uma opcao: "))
if op == 1:
   Cliente.imprimir()



