class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def grava(self):
        gravar = input("Deseja salvar os dados no arquivo 'cliente.txt' (s/n)? ")
        if gravar.lower() == 's': #transformar para minuscula
            with open('cliente.txt', 'a') as f:
                linhas = "{:<20} {:<20} {:<20}\n".format("Nome", "Sobrenome", "CPF")  # formatando a tabela, dentro das chaves esta o tamanho do espaco de cada coluna
                f.write(linhas)
                linhas = "{:<20} {:<20} {:<20}\n".format(self.nome, self.sobrenome, str(self.cpf))
                f.write(linhas)
                print("Os dados foram salvos no arquivo 'cliente.txt'!")
        elif gravar.lower() == 'n':
            print("Os dados não foram salvos no arquivo!")

    def ler(self):
        with open("cliente.txt", 'r') as f:
            l = f.read()
            print(l)
            for i in f:
                print(i)



class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def grava(self):
        gravar = input("Deseja salvar os dados no arquivo 'conta.txt' (s/n)? ")
        while True:
            if gravar.lower() == 's': #transformar letra pra minuscula
                with open('conta.txt', 'a') as f:  #o 'write' so funciona com elementos em string, ent deve transformar todos os 'int' ou 'float' em str
                    linhas = "{:<20} {:<20} {:<20} {:<20}\n".format("Numero da Conta", "Nome do Cliente", "Saldo", "Limite") #formatando a tabela, dentro das chaves esta o tamanho do espaco de cada coluna
                    f.write(linhas)
                    linhas = "{:<20} {:<20} {:<20} {:<20}\n".format(str(self.numero), self.cliente, str(self.saldo), str(self.limite))
                    f.write(linhas)
                print("Os dados foram salvos!")
                break
            elif gravar.lower() == 'n':
                print('Os dados não serão salvos!')
                break
            else:
                print("Opção inválida. Tente novamente")
                continue

    def ler(self):
        with open("conta.txt", 'r') as f:
            for i in f:
                print(i)
        
def menu():
    while True:
        print('================MENU===============')
        print('|  1 - inserir dados do cliente   |')
        print("|  2 - inserir dados da conta     |")
        print("|  3 - imprimir dados do cliente  |")
        print("|  4 - imprimir dados da conta    |")
        print("|  5 - sair do programa           |")
        print("===================================")

        op = int(input("Digite uma opcao: "))
        if op == 1:
            nome = input("Digite o nome: ")
            sobrenome = input("Digite o sobrenome: ")
            cpf = float(input("Digite o CPF: "))
            cliente = Cliente(nome, sobrenome, cpf)
            cliente.grava()
        if op == 2:
            numero = int(input('Qual o numero da conta? '))
            cliente_nome = input("Qual o nome do cliente? ")
            saldo = float(input("Qual o saldo? "))
            limite = float(input('Qual o limite? '))
            conta = Conta(numero, cliente_nome, saldo, limite)
            conta.grava()
        if op == 3:
            cliente.ler()
        if op == 4:
            conta.ler()

menu()
