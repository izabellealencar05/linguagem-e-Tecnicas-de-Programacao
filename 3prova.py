import csv
import os

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def grava(self):
        gravar = input("Deseja salvar os dados no arquivo 'cliente.csv' (s/n)? ")
        if gravar.lower() == 's':
            with open('cliente.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Nome", "CPF"])
                writer.writerow([self.nome, str(self.cpf)])
            print("Os dados foram salvos no arquivo 'cliente.csv'!")
        elif gravar.lower() == 'n':
            print("Os dados não foram salvos no arquivo!")

    def ler(self):
        with open("cliente.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

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

    def ler(self):
        with open("conta.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

    def grava(self):
        gravar = input("Deseja salvar os dados no arquivo 'conta.csv' (s/n)? ")
        while True:
            if gravar.lower() == 's':
                with open('conta.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    if os.stat('conta.csv').st_size == 0:  # Verifica se o arquivo está vazio
                        writer.writerow(["Numero da Conta", "Nome do Cliente", "Saldo", "Limite"])
                    # Verifica se self.cliente é None e fornece um valor padrão se for o caso
                    nome_cliente = self.cliente.nome if self.cliente else "Cliente não associado"
                    writer.writerow([str(self.numero), nome_cliente, str(self.saldo), str(self.limite)])
                print("Os dados foram salvos!")
                break
            elif gravar.lower() == 'n':
                print('Os dados não serão salvos!')
                break
            else:
                print("Opção inválida. Tente novamente")
                continue

    def deposita(self, quantia):
        self.saldo += quantia
        self.historico.registrar_movimento(f"Depósito: +{quantia}")
        self.atualizar_arquivo("Deposito", quantia)

    def saca(self, quantia):
        if self.saldo - quantia >= 0:
            self.saldo -= quantia
            self.historico.registrar_movimento(f"Saque: -{quantia}")
            self.atualizar_arquivo("Saque", quantia)
            return True  # Retorna True se o saque for bem-sucedido
        else:
            print("Saldo insuficiente.")
            return False  # Retorna False se o saque não for possível

    class Conta:
        def __init__(self, numero, cliente, saldo, limite):
            self.numero = numero
            self.cliente = cliente
            self.saldo = saldo
            self.limite = limite
            self.historico = Historico()

        def associa_cliente(self, cliente):
            self.cliente = cliente

        def grava(self):
            gravar = input("Deseja salvar os dados no arquivo 'conta.csv' (s/n)? ")
            while True:
                if gravar.lower() == 's':
                    with open('conta.csv', 'a', newline='') as f:
                        writer = csv.writer(f)
                        if os.stat('conta.csv').st_size == 0:  # Verifica se o arquivo está vazio
                            writer.writerow(["Numero da Conta", "Nome do Cliente", "Saldo", "Limite"])
                        # Verifica se self.cliente é None e fornece um valor padrão se for o caso
                        nome_cliente = self.cliente.nome if self.cliente else "Cliente não associado"
                        writer.writerow([str(self.numero), nome_cliente, str(self.saldo), str(self.limite)])
                    print("Os dados foram salvos!")
                    break
                elif gravar.lower() == 'n':
                    print('Os dados não serão salvos!')
                    break
                else:
                    print("Opção inválida. Tente novamente")
                    continue

        def deposita(self, quantia, conta_destino=None):
            if conta_destino:
                conta_destino.saldo += quantia
                conta_destino.historico.registrar_movimento(f"Depósito recebido: +{quantia}")
                conta_destino.atualizar_arquivo("Deposito", quantia)

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
            # Leitura das linhas existentes
            linhas_existentes = []
            with open('conta.csv', 'r', newline='') as f:
                reader = csv.reader(f)
                linhas_existentes = list(reader)

            # Verifica se o arquivo está vazio e adiciona os rótulos das colunas
            if not linhas_existentes:
                linhas_existentes.append(["Numero da Conta", "Nome do Cliente", "Saldo", "Limite", "Deposito", "Saque"])

            # Procura a linha correspondente à conta atual
            for i, linha in enumerate(linhas_existentes[1:]):  # Pular o cabeçalho
                dados_conta = linha
                if dados_conta[0] == str(self.numero):
                    saldo_atual = float(dados_conta[2])
                    limite = float(dados_conta[3])
                    deposito = float(dados_conta[4])
                    saque = float(dados_conta[5])

                    if operacao == "Deposito":
                        deposito += quantia
                    elif operacao == "Saque":
                        saque += quantia

                    # Atualiza os valores na linha
                    linhas_existentes[i + 1] = [str(self.numero), self.cliente, str(saldo_atual), str(limite),
                                                str(deposito), str(saque)]
                    break
            else:
                # Se a conta não foi encontrada, adiciona uma nova linha
                nova_linha = [str(self.numero), self.cliente, str(self.saldo), str(self.limite), '0', '0']
                if operacao == "Deposito":
                    nova_linha[4] = str(quantia)
                elif operacao == "Saque":
                    nova_linha[5] = str(quantia)

                linhas_existentes.append(nova_linha)

            # Escreve todas as linhas de volta no arquivo
            with open('conta.csv', 'w', newline='') as f:
                writer = csv.writer(f, delimiter=',')
                writer.writerows(linhas_existentes)

            print(f"Os dados foram atualizados no arquivo 'conta.csv'!")

def menu():
    clientes = []
    contas = []

    if not os.path.isfile('conta.csv'):
        with open('conta.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Numero da Conta", "Nome do Cliente", "Saldo", "Limite"])

    # Carregar contas do arquivo
    with open("conta.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Pular cabeçalho
        for row in reader:
            numero = int(row[0])
            cliente_nome = row[1]
            saldo = float(row[2])
            limite = float(row[3])
            conta = Conta(numero, cliente_nome, saldo, limite)
            contas.append(conta)

    while True:
        print('==================MENU================')
        print('|  1 - Inserir dados do cliente      |')
        print("|  2 - Associar cliente a uma conta  |")
        print("|  3 - Imprimir dados do cliente     |")
        print("|  4 - Imprimir dados da conta       |")
        print("|  5 - Depositar                     |")
        print("|  6 - Sacar                         |")
        print("|  7 - Sair do programa              |")
        print("======================================")

        op = int(input("Digite uma opcao: "))
        if op == 1:
            nome = input("Digite o nome: ")
            cpf = input("Digite o CPF: ")
            cliente = Cliente(nome, cpf)
            clientes.append(cliente)
            cliente.grava()
        elif op == 2:
            numero = int(input('Qual o numero da conta? '))
            saldo = float(input("Qual o saldo? "))
            limite = float(input('Qual o limite? '))

            # Verificar se existem clientes para associar à conta
            if clientes:
                print("Clientes disponíveis:")
                for i, cliente in enumerate(clientes, 1):
                    print(f"{i}. {cliente.nome}")

                escolha_cliente = int(input("Escolha o número do cliente para associar à conta (ou 0 para nenhum): "))

                if escolha_cliente > 0 and escolha_cliente <= len(clientes):
                    cliente_associado = clientes[escolha_cliente - 1]
                    conta = Conta(numero, cliente_associado, saldo, limite)
                else:
                    conta = Conta(numero, None, saldo,
                                  limite)  # None indica que a conta não está associada a um cliente
            else:
                conta = Conta(numero, None, saldo, limite)  # None indica que a conta não está associada a um cliente

            contas.append(conta)
            conta.grava()
        elif op == 3:
            for cliente in clientes:
                cliente.ler()
        elif op == 4:
            for conta in contas:
                conta.ler()
        elif op == 5:
            numero_conta_destino = int(input('Digite o número da conta de destino: '))
            quantia = float(input('Digite a quantia a ser depositada: '))

            conta_destino = None

            # Encontrar a conta de destino
            for conta in contas:
                if conta.numero == numero_conta_destino:
                    conta_destino = conta

            if conta_destino:
                conta_destino.deposita(quantia, conta)
                print("Depósito realizado com sucesso.")
            else:
                print("Conta de destino não encontrada.")


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
