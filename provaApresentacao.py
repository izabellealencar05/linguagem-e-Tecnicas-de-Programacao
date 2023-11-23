import csv #importando CSV para conseguir criar um arquivo nesse formato (pra criar tabelas)
class Cliente: #criando uma classe pra cliente
    def __init__(self, nome, cpf, saldo = 0): #inicializando a construcao da classe com os parametros 'self', 'nome', 'cpf' e 'saldo' (com valor inicial de 0)
        self.nome = nome #declarando que self.nome é 'nome', self se refere a instacia do objeto CLiente
        self.cpf = cpf #declando cpf
        self.saldo = saldo #atribui ao parametro saldo ao atributo saldo


class Conta: #criando outra classe, agr para Conta
    def __init__(self, cliente, numero, saldo = 0, limite = 0): #inicializando a construcao da classe com os parametros:self, cliente, numero, saldo (com valor inicial de 0) e limite (com valor inicial de 0), sao os parametros principais para criar uma conta bancaria, por isso tiveram q ser colocados como parametros
        self.cliente = cliente # Atribui o objeto cliente ao atributo cliente. Isso estabelece uma relação entre a classe conta e a classe cliente
        self.numero = numero #atribui o valor do parametro numero ao atributo de numero
        self.saldo = saldo #atribui o valor do parametro saldo ao atributo de saldo, tendo como valor inicial 0
        self.limite = limite #atribui o valor do parametro limite ao atributo de limite, valor inicial 0
        self.historico = Historico() #cria uma instancia da classe Historico e a atribui ao atributo historico, nao precisa ser colocado como parametro da classe Conta, pq tem um valor padrao ja, que eh a propria classe Historico sendo atribuida
        self.total_depositado = 0 #inicializa o atributo com valor 0, nao tem eh necessario para a criacao de uma conta bancaria, ent n precisa ser colocado como parametro da classe Conta
        self.total_sacado = 0 #inicializa o atributo com valor 0

    def depositar(self, valor): #criando o metodo Depositar com os parametros: self e valor (valor a ser depositado), self smp deve ser o primeiro parametro na utilizacao de um metodo, que eh uma referencia a instancia da classe na qual o metodo esta sendo chamado
        if self.saldo + valor <= self.limite: #se o valor do saldo mais o valor a ser deositado eh menor ou igual ao limite
            self.saldo += valor #se a for menor ou igual ao limite, eh adicionado o valor a ser depositado ao saldo
            self.historico.adicionar_transacao(f'Depósito: +{valor}', self.saldo, self.limite) #o metodo 'historico.adicionar_trasnsacao' adiciona uma transacao ao historico, indicando um depósito com o valor depositado, o novo saldo após o depósito e o limite atual
            self.cliente.saldo = self.saldo #atualiza o saldo do cliente com o novo saldo apos o deposito
            self.total_depositado += valor #atribui ao atributo 'total_depositado' com o valor depositado
            print("Valor depositado com sucesso!") #imprime na tela essa frase
        else: #se a condicao acima for 'errada' ele imprime na tela essa frase
            print("Erro! Limite de saldo é menor") #frase impressa na tela caso a condicao nao seja verdadeira

    def sacar(self, valor): #inicializa outro metodo chamado 'sacar' com os parametros "self" (instancia da classe) e 'valor' (valor a ser sacado)
        if self.saldo - valor >= -self.limite: #se o saldo menos o valor a ser sacado  for maior que o limite inferior
            self.saldo -= valor #se a condicao for verdadeira ele retira do saldo o valor a ser sacado
            self.historico.adicionar_transacao(f'Saque: -{valor}', self.saldo, self.limite) #chama o metodo do objeto 'historico', adiciona a transacao ao historico,printando o valor sacado, o saldo e o limite
            self.cliente.saldo = self.saldo #atualiza o saldo do cliente com o novo saldo
            self.total_sacado += valor #incrementa o atributo 'total_sacado' da conta com o valor sacado
            print("Valor sacado com sucesso!") #printa na tela essa frase
        else: #caso a condicao nao seja verdadeira
            print("Erro! Limite de saque excedido.") #printa na tela essa frase


class Historico:  # cria a classe Historico
    def __init__(self):  # iniciando a construção da classe com apenas o parâmetro 'self'
        self.transacoes = []  # criando uma lista vazia para o atributo 'transacoes', para armazenar as transacoes

    def adicionar_transacao(self, transacao, novo_saldo, limite):  # criando um método com os parâmetros: self, transacao, novo_saldo, limite
        self.transacoes.append({  # criando um dicionário na lista 'transacoes' com os valores:
            'transacao': transacao,  # transacao
            'saldo_atual': novo_saldo,  # saldo após a transacao
            'limite': limite  # limite da transacao
        })

    def __str__(self):  # criando um método para retornar em string, com o parametro 'self' como referencia a instancia da classe
        return '\n'.join(str(transacao) for transacao in self.transacoes) #Define o método especial __str__ para a classe Historico, retornando uma representação em string do histórico, mostrando cada transação em uma nova linha.

    def gerar_csv_informacoes(self, nome_arquivo, cliente, conta): #cria um metodo com os parametros: self, nome_arquivo, cliente, conta
        with open(nome_arquivo, 'w', newline='') as arquivo_csv: #abre um arquivo CSV
            colunas = ['Nome', 'Número da Conta', 'Saldo Atual', 'Limite', 'Transacao'] #formatando as colunas
            escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)

            escritor.writeheader() #escreve a linha do cabecalho
            for transacao in self.transacoes:
                #escreve em cada linha:
                escritor.writerow({
                    'Nome': cliente.nome,
                    'Número da Conta': conta.numero,
                    'Saldo Atual': transacao['saldo_atual'],
                    'Limite': transacao['limite'],
                    'Transacao': transacao['transacao']
                })

    def salvar_em_arquivo(self, nome_arquivo, conteudo): #cria o metodo com os parametros: self, nome_arquivo, conteudo
        with open(nome_arquivo, 'w') as arquivo: #abre o arquivo, na formato para escrever, ent permite escrever dentro do arquivo
            arquivo.write(conteudo) #escreve o conteudo do arquivo




def cadastrar_conta(): #cria uma funcao sem parametros
    nome = input("Digite o nome do cliente: ") #pede ao usuario para informar o nome
    cpf = input("Digite o CPF do cliente: ") #pede o cpf
    saldo = float(input("Digite o saldo inicial do cliente: ")) #pede o saldo
    numero_conta = int(input("Digite o número da conta: ")) #pede o numero da conta
    limite_conta = float(input("Digite o limite da conta: ")) #pede o limite da conta
    cliente = Cliente(nome, cpf, saldo) #xcria um objeto da classe Cliente com as informacoes fornecidads pelo usario
    conta = Conta(cliente, numero_conta, saldo, limite=limite_conta) #cria um objeto  Conta associado a esse cliente
    return conta #retorna o objeto conta


def imprimir_informacoes(cliente, conta): #cria a funcao com os parametros cliente e conta que sao objetos das classes Clientes e Conta
    print("\nInformações do Cliente:") #printa na tela a frase
    print(f"Nome: {cliente.nome}, CPF: {cliente.cpf}") #printa na tela o nome e o cpf o cliente
    print(f"Numero da conta: {conta.numero}") #printa na tela o numero da conta
    print(f"Saldo: {conta.saldo}") #printa na tela o saldo
    print(f"Limite: {conta.limite}") #printa na tela o limite
    print(f"Total Depositado: {conta.total_depositado}") #printa na tela o total depositado
    print(f"Total Sacado: {conta.total_sacado}") #printa na tela o total sacado

def cadastrar_conta(contas): #cria a funcao como parametro a lista de contas
    nome = input("Digite o nome do cliente: ") #pede ao usuario que informe o nome
    cpf = input("Digite o CPF do cliente: ") #pede ao usuario que informe o cpf
    numero_conta = int(input("Digite o número da conta: ")) #pede ao usuario que informe o numero da conta
    saldo = float(input("Digite o saldo do cliente: ")) #pede ao usuario que informe o saldo
    limite_conta = float(input("Digite o limite da conta: ")) #pede ao usuario que informe o limite
    cliente = Cliente(nome, cpf, saldo) #cria um objeto da classe com as infos que o usuario digitou
    conta = Conta(cliente, numero_conta, saldo, limite=limite_conta) #cria um objeto da classe Conta com as infos fornecidas pelo usuario
    contas.append(conta) #adiciona a conta à lista de contas
def gerar_arquivo_contas(contas): #cria a funcao como parametro a lista contas
    with open("infoContas", 'w', newline='') as arquivo_csv: #abre o arquivo
        #formatando o arquivo
        colunas = ['Nome', 'Número da Conta', 'Saldo', 'Limite']
        escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)

        escritor.writeheader() #escreve o cabecalho
        for conta in contas: #inicia o loop
            #para cada conta escreve uma linha no arquivo
            escritor.writerow({
                'Nome': conta.cliente.nome,
                'Número da Conta': conta.numero,
                'Saldo': conta.saldo,
                'Limite': conta.limite
            })

def gerar_arquivo_transacoes(contas): #cria a funcao que recebe contas como parametrof
    for conta in contas: #inicia um loop que itera sobre cada conta na lista de contas
        nome_arquivo = f"transacoes_conta_{conta.numero}.csv" #variael com o nome do arquivo
        conta.historico.gerar_csv_informacoes(nome_arquivo, conta.cliente, conta) #chama o metodo

def imprimir_informacoes_cliente(contas): #criando uma funcao para imprimir infos dos clientes associados com a lista de contas como parametro
    with open("informacoes_clientes.csv", 'w', newline='') as arquivo_csv: #abrindo o arquivo CSV
        colunas = ['Nome', 'CPF', 'Saldo'] #cria uma lista que contem os nomes de cada coluna para ser escrito no arquivo csv
        escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)

        escritor.writeheader() #escreve a linha do cabecalho
        for conta in contas: #cria um loop que itera sobre cada conta na lista de contas
            #cada linha escreve:
            escritor.writerow({
                'Nome': conta.cliente.nome,
                'CPF': conta.cliente.cpf,
                'Saldo': conta.cliente.saldo
            })


contas = [] #cria uma lista vazia para armazenar contas
historico_global = Historico() #cria uma instancia da classe Historico para manter  um historico global de transacoes

while True: #iniciando o loop
    #criando o menu
    print('================MENU===============')
    print("|  1 - Cadastrar conta            |")
    print("|  2 - Deposito                   |")
    print("|  3 - Saque                      |")
    print("|  4 - Imprimir dados da conta    |")
    print("|  5 - Sair do programa           |")
    print("===================================")
    opcao = input("Escolha uma opção: ") #declarando a variavel 'opcao' para permitir o usuario escolher qual opcao do menu

    if opcao == "1": #se a opcao for igual a 1
        cadastrar_conta(contas) #chama a funcao 'cadastrar_conta' addicionando uma conta a lista de contas
        print("Dados cadastrados com sucesso!") #printar na tela essa frase

    elif opcao == "2" and contas: #se a opcao for igual a 2 e há constas cadastradas
        while True: #inicia um loop
            numero_conta = int(input("Digite o número da conta para depósito: ")) #delcara a variavel numero_conta para o usuario escrever o numero da conta que ele deseja fazer o deposito
            conta = next((c for c in contas if c.numero == numero_conta), None) #analisa se existe uma conta com o numero indicado
            if conta: #se a conta existe
                valor = float(input("Digite o valor a ser depositado: ")) #pede ao usuario para informar o valor a ser depositado na conta
                conta.depositar(valor) #chama o metodo 'depositar' da classe conta para realizar o deposito
                break #fecha o loop
            else: #se a conta nao existir
                print("Conta não encontrada. Por favor, digite um número de conta válido.") #printa na tela essa frase e retorna a perugnta inicial do loop

    elif opcao == "3" and contas: #se a opcao for igual a 3 e existir contas cadastradas
        numero_conta = int(input("Digite o número da conta para saque: ")) #declara a variavel numero_conta para o usuario poder digitar o numero da conta para o saque
        valor = float(input("Digite o valor a ser sacado: ")) #declara a variavel valor para o usuario digitar o valor que deseja sacar
        conta = next((c for c in contas if c.numero == numero_conta), None) #procura se a conta com o numero informado existe
        if conta: #se a conta existe
            conta.sacar(valor) #chama o metodo 'sacar' da classe Conta para realizar o saque
        else: #se a conta nao existe
            print("Conta não encontrada.") #printa na teka que a conta nao foi encontrada
    elif opcao == "4" and contas: #se a opcao for igual a 4 e existir contas cadastradas
        numero_conta = int(input("Digite o número da conta para imprimir informações: ")) #declara a variavel 'numero_conta' para o usuario indicar qual conta deseja ver as informacoes
        conta = next((c for c in contas if c.numero == numero_conta), None) #procura se existe a conta informada
        if conta: #se a conta existe
            imprimir_informacoes(conta.cliente, conta) #chama a funcao 'imprimir_informacoes' para mostrar as informacoes
        else: #senao
            print("Conta não encontrada.") #printa na tela que a conta nao foi encontrada
    elif opcao == "5": #se a opcao for igual a 5
        gerar_arquivo_contas(contas) #cria o aquivo referente as informacoes das contas criadas
        gerar_arquivo_transacoes(contas) #cria arquivo referente as transacoes das contas criadas
        imprimir_informacoes_cliente(contas) #imprime informacoes do cliente da classe conta
        print("Saindo do programa...") #printa na tela a frase
        break #fecha o lopp
    else: #senao
        print("Opção inválida ou nenhuma conta cadastrada. Tente novamente.") #printa na tela a frase, e volta para o menu
