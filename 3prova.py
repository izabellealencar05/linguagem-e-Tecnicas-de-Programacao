class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def grava(self):
        gravar = input("Deseja salvar os dados no arquivo 'cliente.txt' (s/n)? ")
        if gravar.lower() == 's':
            with open('cliente.txt', 'a') as f:
                linhas = "{:<20} {:<20}\n".format("Nome", "CPF")
                f.write(linhas)
                linhas = "{:<20} {:<20}\n".format(self.nome, str(self.cpf))
                f.write(linhas)
                print("Os dados foram salvos no arquivo 'cliente.txt'!")
        elif gravar.lower() == 'n':
            print("Os dados não foram salvos no arquivo!")

    def ler(self):
        with open("cliente.txt", 'r') as f:
            l = f.read()
            print(l)


class Historico:
    def __init__(self):
        self.movimentos = []

    def registrar_movimento(self, movimento):
        self.movimentos.append(movimento)

    def imprimir_extrato(self):
        print("Extrato do histórico da conta:")
        for movimento in self.movimentos:
            print(movimento)


class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def grava(self):
        gravar = input("Deseja salvar os dados no arquivo 'conta.txt' (s/n)? ")
        while True:
            if gravar.lower() == 's':
                with open('conta.txt', 'a') as f:
                    linhas = "{:<20} {:<20} {:<20} {:<20}\n".format("Numero da Conta", "Nome do Cliente", "Saldo", "Limite")
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

    def deposita(self, quantia):
        self.saldo += quantia
        self.historico.registrar_movimento(f"Depósito: +{quantia}")
        self.atualizar_arquivo("Deposito", quantia)

    def saca(self, quantia):
        if self.saldo - quantia >= 0:
            self.saldo -= quantia
            self.historico.registrar_movimento(f"Saque: -{quantia}")
            self.atualizar_arquivo("Saque", quantia)
            return True  
        else:
            print("Saldo insuficiente.")
            return False  

    def atualizar_arquivo(self, operacao, quantia):
        
        linhas_existentes = []
        with open('conta.txt', 'r') as f:
            linhas_existentes = f.readlines()

      
        if not linhas_existentes:
            linhas_existentes.append("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}\n".format(
                "Numero da Conta", "Nome do Cliente", "Saldo", "Limite", "Deposito", "Saque"))

        deposito = 0
        saque = 0

       
        for i, linha in enumerate(linhas_existentes):
            dados_conta = linha.split()
            if dados_conta[0] == str(self.numero):
                deposito = float(dados_conta[4])
                saque = float(dados_conta[5])
                # Substitui a linha existente
                linhas_existentes[i] = "{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}\n".format(
                    str(self.numero), self.cliente, str(self.saldo), str(self.limite), deposito, saque)
                break

      
        else:
            linhas_existentes.append("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}\n".format(
                str(self.numero), self.cliente, str(self.saldo), str(self.limite), deposito, saque))

      
        with open('conta.txt', 'w') as f:
            f.writelines(linhas_existentes)

        print(f"Os dados foram atualizados no arquivo 'conta.txt'!")
def menu():
    clientes = []
    contas = []

    while True:
        print('================MENU===============')
        print('|  1 - Inserir dados do cliente   |')
        print("|  2 - Inserir dados da conta     |")
        print("|  3 - Imprimir dados do cliente  |")
        print("|  4 - Imprimir dados da conta    |")
        print("|  5 - Depositar                  |")
        print("|  6 - Sacar                      |")
        print("|  7 - Sair do programa           |")
        print("===================================")

        op = int(input("Digite uma opcao: "))
        if op == 1:
            nome = input("Digite o nome: ")
            cpf = float(input("Digite o CPF: "))
            cliente = Cliente(nome, cpf)
            clientes.append(cliente)
            cliente.grava()
        elif op == 2:
            numero = int(input('Qual o numero da conta? '))
            cliente_nome = input("Qual o nome do cliente? ")
            saldo = float(input("Qual o saldo? "))
            limite = float(input('Qual o limite? '))
            conta = Conta(numero, cliente_nome, saldo, limite)
            contas.append(conta)
            conta.grava()
        elif op == 3:
            for cliente in clientes:
                cliente.ler()
        elif op == 4:
            for conta in contas:
                conta.ler()
        elif op == 5:
            numero_conta_origem = int(input('Digite o número da conta de origem: '))
            numero_conta_destino = int(input('Digite o número da conta de destino: '))

            conta_origem = None
            conta_destino = None

            for conta in contas:
                if conta.numero == numero_conta_origem:
                    conta_origem = conta
                elif conta.numero == numero_conta_destino:
                    conta_destino = conta

            if conta_origem is not None and conta_destino is not None:
                quantia = float(input('Digite a quantia a ser transferida: '))
                conta_origem.deposita(quantia, conta_destino)
            else:
                print("Conta de origem ou conta de destino não encontrada.")
        elif op == 6:
            numero_conta = int(input('Digite o número da conta para sacar: '))
            quantia = float(input('Digite a quantia a ser sacada: '))
            for conta in contas:
                if conta.numero == numero_conta:
                    if conta.saca(quantia):
                        print("Saque realizado com sucesso.")
                    else:
                        print("Saque não realizado.")
                    break
            else:
                print("Conta não encontrada.")
        elif op == 7:
            break

menu()
