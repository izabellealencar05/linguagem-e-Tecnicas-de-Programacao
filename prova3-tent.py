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
        self.historico = Historico()
        self.total_depositado = 0  # Nova variável para armazenar o total depositado
        self.total_sacado = 0  # Nova variável para armazenar o total sacado

    def depositar(self, valor):
        if self.saldo + valor <= self.limite:
            self.saldo += valor
            self.historico.adicionar_transacao(f'Depósito: +{valor}', self.saldo, self.limite)
            self.cliente.saldo = self.saldo
            self.total_depositado += valor  # Atualiza o total depositado
            print("Valor depositado com sucesso!")
        else:
            print("Erro! Limite de saldo e menor")

    def sacar(self, valor):
        if self.saldo - valor >= -self.limite:
            self.saldo -= valor
            self.historico.adicionar_transacao(f'Saque: -{valor}', self.saldo, self.limite)
            self.cliente.saldo = self.saldo
            self.total_sacado += valor  # Atualiza o total sacado
            print("Valor sacado com sucesso!")
        else:
            print("Erro! Limite de saque excedido.")
class Historico:
    def __init__(self):
        self.transacoes = []
        self.saldo_antigo = 0

    def adicionar_transacao(self, transacao, novo_saldo, limite):
        self.transacoes.append({
            'transacao': transacao,
            'saldo_antigo': self.saldo_antigo,
            'saldo_atual': novo_saldo,
            'limite': limite
        })
        self.saldo_antigo = novo_saldo

    def gerar_csv_informacoes(self, nome_arquivo, cliente, conta):
        nome_arquivo = "conta.csv"
        with open(nome_arquivo, 'w', newline='') as arquivo_csv:
            colunas = ['Nome', 'Número da Conta', 'Saldo Antigo', 'Saldo Atual', 'Limite', 'Depósito', 'Saque']
            escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)

            escritor.writeheader()
            for transacao in self.transacoes:
                escritor.writerow({
                    'Nome': cliente.nome,
                    'Número da Conta': conta.numero,
                    'Saldo Antigo': transacao['saldo_antigo'],
                    'Saldo Atual': transacao['saldo_atual'],
                    'Limite': transacao['limite'],
                    'Depósito': transacao['transacao'],
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
    print(f"Número da conta: {conta.numero}, Saldo: {conta.saldo}, Limite: {conta.limite}")
    print(f"Total Depositado: {conta.total_depositado}")
    print(f"Total Sacado: {conta.total_sacado}")

    saldo_antigo = conta.saldo - Historico().transacoes[-1] if Historico().transacoes else 0
    print(f"Saldo Antigo: {saldo_antigo}")

    nome_arquivo = f"informacoes_conta_{conta.numero}.csv"
    conteudo = f"Informações do Cliente:\nNome: {cliente.nome}, CPF: {cliente.cpf}, Saldo Atual: {cliente.saldo}\n"
    conteudo += f"Informações da Conta:\nNúmero da Conta: {conta.numero}, Saldo: {conta.saldo}, Limite: {conta.limite}\n"
    conteudo += f"Total Depositado: {conta.total_depositado}\nTotal Sacado: {conta.total_sacado}\n"
    conteudo += f"Saldo Antigo: {conta.saldo}"
    Historico().salvar_em_arquivo(nome_arquivo, conteudo)
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
historico_global = Historico()

def menu():
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
            else:
                print("Conta não encontrada.")
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
                imprimir_historico(conta)
            else:
                print("Conta não encontrada.")
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida ou nenhuma conta cadastrada. Tente novamente.")


def main():
    menu()

if __name__ == "__main__":
    main()
