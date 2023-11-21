import csv

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
        self.historico = []

    def depositar(self, valor):
        if self.saldo + valor <= self.limite:
            self.saldo += valor
            self.historico.append(f'Depósito: +{valor}')
            self.cliente.saldo = self.saldo  # Atualizar o saldo do cliente
            Historico().atualizar_saldo_antigo(self.saldo)  # Atualizar o saldo antigo no histórico
        else:
            print("Operação não permitida. Limite de saldo excedido.")

    def sacar(self, valor):
        if self.saldo - valor >= -self.limite:
            self.saldo -= valor
            self.historico.append(f'Saque: -{valor}')
            self.cliente.saldo = self.saldo  # Atualizar o saldo do cliente
        else:
            print("Operação não permitida. Limite de saque excedido.")

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def gerar_csv_informacoes(self, nome_arquivo, cliente, conta):
        with open(nome_arquivo, 'w', newline='') as arquivo_csv:
            colunas = ['Nome', 'Número da Conta', 'Saldo', 'Limite', 'Depósito', 'Saque']
            escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)

            escritor.writeheader()
            escritor.writerow({
                'Nome': cliente.nome,
                'Número da Conta': conta.numero,
                'Saldo': conta.saldo,
                'Limite': conta.limite,
                'Depósito': '',
                'Saque': ''
            })

    def salvar_em_arquivo(self, nome_arquivo, conteudo):
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(conteudo)

def imprimir_historico(conta):
    print(f"\nHistórico da Conta {conta.numero}:")
    for transacao in conta.historico:
        print(transacao)

    # Salvar em arquivo
    nome_arquivo = f"extrato_conta_{conta.numero}.csv"
    conteudo = f"Saldo Atual: {conta.saldo}\n\nHistórico da Conta {conta.numero}:\n"
    conteudo += '\n'.join(conta.historico)
    Historico().salvar_em_arquivo(nome_arquivo, conteudo)  # Ajuste aqui
    print(f"\nDados salvos em {nome_arquivo}")

def imprimir_informacoes(cliente, conta):
    print("\nInformações do Cliente:")
    print(f"Nome: {cliente.nome}, CPF: {cliente.cpf}, Saldo Atual: {cliente.saldo}")

    print("\nInformações da Conta:")
    print(f"Número: {conta.numero}, Saldo: {conta.saldo}, Limite: {conta.limite}")

    # Salvar em arquivo
    nome_arquivo = f"informacoes_conta_{conta.numero}.csv"
    conteudo = f"Informações do Cliente:\nNome: {cliente.nome}, CPF: {cliente.cpf}, Saldo Atual: {cliente.saldo}\n\nInformações da Conta:\nNúmero da Conta: {conta.numero}, Saldo: {conta.saldo}, Limite: {conta.limite}"
    Historico().salvar_em_arquivo(nome_arquivo, conteudo)  # Ajuste aqui
    print(f"\nInformações salvas em {nome_arquivo}")

def cadastrar_conta():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    saldo = float(input("Digite o saldo inicial do cliente: "))
    numero_conta = int(input("Digite o número da conta: "))
    limite_conta = float(input("Digite o limite da conta: "))
    cliente = Cliente(nome, cpf, saldo)
    conta = Conta(cliente, numero_conta, saldo, limite=limite_conta)
    return conta

contas = []

while True:
    print('================MENU===============')
    print("|  1 - Inserir dados da conta     |")
    print("|  2 - Deposito                   |")
    print("|  3 - Saque                      |")
    print("|  4 - Imprimir dados da conta    |")
    print("|  5 - Sair do programa           |")
    print("===================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        conta = cadastrar_conta()
        contas.append(conta)
        print("Dados cadastrados com sucesso!")
    elif opcao == "2" and contas:
        numero_conta = int(input("Digite o número da conta para depósito: "))
        valor = float(input("Digite o valor a ser depositado: "))
        conta = next((c for c in contas if c.numero == numero_conta), None)
        if conta:
            conta.depositar(valor)
            print("Valor depositado com sucesso!")
        else:
            print("Conta não encontrada.")
    elif opcao == "3" and contas:
        numero_conta = int(input("Digite o número da conta para saque: "))
        valor = float(input("Digite o valor a ser sacado: "))
        conta = next((c for c in contas if c.numero == numero_conta), None)
        if conta:
            conta.sacar(valor)
            print("Valor sacado!")
        else:
            print("Conta não encontrada.")
    elif opcao == "4" and contas:
        numero_conta = int(input("Digite o número da conta para imprimir informações: "))
        conta = next((c for c in contas if c.numero == numero_conta), None)
        if conta:
            imprimir_informacoes(conta.cliente, conta)
            imprimir_historico(conta)
        else:
            print("Conta não encontrada.")
    elif opcao == "5":
        break
    else:
        print("Opção inválida ou nenhuma conta cadastrada. Tente novamente.")
