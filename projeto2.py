import pandas as pd

class Funcionario:
    def __init__(self, nome, cargo, salario, horas_trabalhadas):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_desconto_ir(self):
        if self.salario <= 1500:
            return 0
        elif 1500 < self.salario <= 3000:
            return 0.15 * self.salario
        elif 3000 < self.salario <= 5000:
            return 0.20 * self.salario
        else:
            return 0.27 * self.salario

def cadastro(funcionarios):
    while True:
        nome = input("Nome do funcionário: ")
        cargo = input("Cargo: ")
        salario = float(input("Salário: "))
        horas_trabalhadas = int(input("Horas trabalhadas: "))
        funcionario = Funcionario(nome, cargo, salario, horas_trabalhadas)
        funcionarios.append(funcionario)
        adicionarmais = input("Deseja adicionar outro funcionário? (s/n): ").lower()
        if adicionarmais != 's':
            break

def exibir_cadastro(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        print("\nCADASTRO DE FUNCIONÁRIOS")
        for f in funcionarios:
            print(f"Nome: {f.nome}")
            print(f"Cargo: {f.cargo}")
            print(f"Salário: {f.salario}")
            print(f"Horas Trabalhadas: {f.horas_trabalhadas}")
            print("")
def calcular_folha_pagamento(funcionarios):
    total_desconto_ir = 0
    total_salario_bruto = 0
    total_salario_liquido = 0

    data = {"Nome": [], "Cargo": [], "Salário Bruto": [], "Desconto IR": [], "Salário Líquido": []}

    for f in funcionarios:
        desconto_ir = f.calcular_desconto_ir()
        salario_bruto = f.salario
        salario_liquido = salario_bruto - desconto_ir

        data["Nome"].append(f.nome)
        data["Cargo"].append(f.cargo)
        data["Salário Bruto"].append(salario_bruto)
        data["Desconto IR"].append(desconto_ir)
        data["Salário Líquido"].append(salario_liquido)

        total_desconto_ir += desconto_ir
        total_salario_bruto += salario_bruto
        total_salario_liquido += salario_liquido

    df = pd.DataFrame(data)

    print("\nRELATÓRIO")
    print(df)
    print("\nTotal de Desconto de IR: R${:.2f}".format(total_desconto_ir))
    print("Total de Salário Bruto: R${:.2f}".format(total_salario_bruto))
    print("Total de Salário Líquido: R${:.2f}".format(total_salario_liquido))

def salvar_folha_pagamento(funcionarios, arquivo):
    data = {"Nome": [], "Cargo": [], "Salário": [], "Horas Trabalhadas": []}

    for f in funcionarios:
        data["Nome"].append(f.nome)
        data["Cargo"].append(f.cargo)
        data["Salário"].append(f.salario)
        data["Horas Trabalhadas"].append(f.horas_trabalhadas)

    df = pd.DataFrame(data)
    df.to_csv(arquivo, index=False)

def carregar_folha_pagamento(arquivo):
    try:
        df = pd.read_csv(arquivo)
        funcionarios = []
        for _, row in df.iterrows():
            funcionario = Funcionario(row["Nome"], row["Cargo"], row["Salário"], row["Horas Trabalhadas"])
            funcionarios.append(funcionario)
        return funcionarios
    except FileNotFoundError:
        return []

cadastro_efetuado = False  

def menu():
    nome_arquivo = "folha_pagamento.csv"
    funcionarios = carregar_folha_pagamento(nome_arquivo)

    while True:
        print("=====================MENU======================")
        print("|    1 - Adicionar funcionário                |")
        print("|    2 - Exibir cadastro de funcionários      |")
        print("|    3 - Calcular descontos e gerar relatório |")
        print("|    4 - Salvar folha de pagamento            |")
        print("|    5 - Sair                                 |")
        print("===============================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro(funcionarios)
            cadastro_efetuado = True 
        elif opcao == "2":
            if not cadastro_efetuado:
                print("Nenhum funcionário cadastrado.")
            else:
                exibir_cadastro(funcionarios)
        elif opcao == "3":
            if not funcionarios:
                print("Nenhum funcionário cadastrado.")
            else:
                calcular_folha_pagamento(funcionarios)
        elif opcao == "4":
            salvar_folha_pagamento(funcionarios, nome_arquivo)
            print("Folha de pagamento salva com sucesso.")
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
