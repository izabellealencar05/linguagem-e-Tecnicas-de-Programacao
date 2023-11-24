import csv
from datetime import datetime


class Cliente:
    def __init__(self, nome, cpf, saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo


class Conta:
    def __init__(self, cliente, numero, saldo=0, limite=0):
        self.cliente = cliente
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
        self.total_depositado = 0
        self.total_sacado = 0
        self.data_abertura = datetime.now()

    def depositar(self, valor):
        self.saldo += valor
        self.historico.adicionar_transacao(
            f'Depósito: +{valor}', self.saldo, self.limite, datetime.now()
        )
        self.cliente.saldo = self.saldo
        self.total_depositado += valor
        print("Valor depositado com sucesso!")

    def sacar(self, valor):
        if self.saldo - valor >= -self.limite:
            self.saldo -= valor
            self.historico.adicionar_transacao(
                f'Saque: -{valor}', self.saldo, self.limite, datetime.now()
            )
            self.cliente.saldo = self.saldo
            self.total_sacado += valor
            print("Valor sacado com sucesso!")
        else:
            print("Erro! Limite de saque excedido.")


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao, novo_saldo, limite, data):
        self.transacoes.append({
            'transacao': transacao,
            'saldo_atual': novo_saldo,
            'limite': limite,
            'data': data  # Added transaction date
        })

    def __str__(self):
        return '\n'.join(str(transacao) for transacao in self.transacoes)

    def gerar_csv_informacoes(self, nome_arquivo, cliente, conta):
        with open(nome_arquivo, 'w', newline='') as arquivo_csv:
            colunas = ['Nome', 'Número da Conta', 'Saldo Atual', 'Limite', 'Transacao', 'Data']
            escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)

            escritor.writeheader()
            for transacao in self.transacoes:
                escritor.writerow({
                    'Nome': cliente.nome,
                    'Número da Conta': conta.numero,
                    'Saldo Atual': transacao['saldo_atual'],
                    'Limite': transacao['limite'],
                    'Transacao': transacao['transacao'],
                    'Data': transacao['data']  # Added line for transaction date
                })

    def salvar_em_arquivo(self, nome_arquivo, conteudo):
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(conteudo)



def cadastrar_conta():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    saldo = float(input("Digite o saldo inicial do cliente: "))
    numero_conta = int(input("Digite o número da conta: "))
    limite_conta = float(input("Digite o limite da conta: "))
    cliente = Cliente(nome, cpf, saldo)
    conta = Conta(cliente, numero_conta, saldo, limite=limite_conta)
    return conta


def imprimir_informacoes(cliente, conta):
    print("\nInformações do Cliente:")
    print(f"Nome: {cliente.nome}, CPF: {cliente.cpf}")
    print(f"Numero da conta: {conta.numero}")
    print(f"Saldo: {conta.saldo}")
    print(f"Limite: {conta.limite}")
    print(f"Total Depositado: {conta.total_depositado}")
    print(f"Total Sacado: {conta.total_sacado}")

def cadastrar_conta(contas):
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    numero_conta = int(input("Digite o número da conta: "))
    saldo = float(input("Digite o saldo do cliente: "))
    limite_conta = float(input("Digite o limite da conta: "))
    cliente = Cliente(nome, cpf, saldo)
    conta = Conta(cliente, numero_conta, saldo, limite=limite_conta)
    contas.append(conta)
def gerar_arquivo_contas(contas):
    with open("infoContas", 'w', newline='') as arquivo_csv:
        colunas = ['Nome', 'Número da Conta', 'Saldo', 'Limite']
        escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)

        escritor.writeheader()
        for conta in contas:
            escritor.writerow({
                'Nome': conta.cliente.nome,
                'Número da Conta': conta.numero,
                'Saldo': conta.saldo,
                'Limite': conta.limite
            })

def gerar_arquivo_transacoes(contas):
    nome_arquivo = "transacoes_todas_contas.csv"
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        colunas = ['Nome', 'Número da Conta', 'Saldo Atual', 'Limite', 'Transacao', 'Data']
        escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)
        escritor.writeheader()

        for conta in contas:
            for transacao in conta.historico.transacoes:
                escritor.writerow({
                    'Nome': conta.cliente.nome,
                    'Número da Conta': conta.numero,
                    'Saldo Atual': transacao['saldo_atual'],
                    'Limite': transacao['limite'],
                    'Transacao': transacao['transacao'],
                    'Data': transacao['data']
                })
def imprimir_informacoes_cliente(contas):
    with open("informacoes_clientes.csv", 'w', newline='') as arquivo_csv:
        colunas = ['Nome', 'CPF', 'Saldo']
        escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)

        escritor.writeheader()
        for conta in contas:
            escritor.writerow({
                'Nome': conta.cliente.nome,
                'CPF': conta.cliente.cpf,
                'Saldo': conta.cliente.saldo
            })


contas = []
historico_global = Historico()

while True:
    print('================MENU===============')
    print("|  1 - Cadastrar conta            |")
    print("|  2 - Deposito                   |")
    print("|  3 - Saque                      |")
    print("|  4 - Imprimir dados da conta    |")
    print("|  5 - Sair do programa           |")
    print("===================================")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_conta(contas)
        print("Dados cadastrados com sucesso!")
    elif opcao == "2" and contas:
        while True:
            numero_conta = int(input("Digite o número da conta para depósito: "))
            conta = next((c for c in contas if c.numero == numero_conta), None)
            if conta:
                valor = float(input("Digite o valor a ser depositado: "))
                conta.depositar(valor)
                break
            else:
                print("Conta não encontrada. Por favor, digite um número de conta válido.")
    elif opcao == "3" and contas:
        numero_conta = int(input("Digite o número da conta para saque: "))
        valor = float(input("Digite o valor a ser sacado: "))
        conta = next((c for c in contas if c.numero == numero_conta), None)
        if conta:
            conta.sacar(valor)
        else:
            print("Conta não encontrada.")
    elif opcao == "4" and contas:
        numero_conta = int(input("Digite o número da conta para imprimir informações: "))
        conta = next((c for c in contas if c.numero == numero_conta), None)
        if conta:
            imprimir_informacoes(conta.cliente, conta)

        else:
            print("Conta não encontrada.")
    elif opcao == "5":
        gerar_arquivo_contas(contas)
        gerar_arquivo_transacoes(contas)
        imprimir_informacoes_cliente(contas)
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida ou nenhuma conta cadastrada. Tente novamente.")
