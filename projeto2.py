import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    print("CADASTRO DE FUNCIONÁRIOS")
    for f in funcionarios:
        print(f"Nome: {f.nome}")
        print(f"Cargo: {f.cargo}")
        print(f"Salário: {f.salario}")
        print(f"Horas Trabalhadas: {f.horas_trabalhadas}")

def relatorio(funcionarios):
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

    print("\nRELATÓRIO")
    print("1 - Relatório Geral")
    for i, f in enumerate(funcionarios):
        print(f"{i + 2} - {f.nome}")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        df = pd.DataFrame(data)
        print(df)
    elif escolha.isnumeric() and 2 <= int(escolha) <= len(funcionarios) + 1:
        i = int(escolha) - 2
        nome_funcionario = funcionarios[i].nome
        data_funcionario = {
            "Nome": [data["Nome"][i]],
            "Cargo": [data["Cargo"][i]],
            "Salário Bruto": [data["Salário Bruto"][i]],
            "Desconto IR": [data["Desconto IR"][i]],
            "Salário Líquido": [data["Salário Líquido"][i]],
        }
        df = pd.DataFrame(data_funcionario)
        print(f"relatorio de {nome_funcionario}")
        print(df)
    else:
        print("Opção inválida.")

    print(f"Total de Desconto de IR: R${total_desconto_ir:.2f}")
    print(f"Total de Salário Bruto: R${total_salario_bruto:.2f}")
    print(f"Total de Salário Líquido: R${total_salario_liquido:.2f}")

    criar_grafico(data) 

def criar_grafico(data):
    plt.figure(figsize=(10, 6))
    plt.bar(data["Nome"], data["Salário Bruto"], label="Salário Bruto", color="blue")
    plt.bar(data["Nome"], data["Desconto IR"], label="Desconto IR", color="red", bottom=data["Salário Bruto"])
    plt.xlabel('Funcionários')
    plt.ylabel('Valores em R$')
    plt.title('Gráfico de Salário Bruto e Desconto de IR')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def menu():
    funcionarios = []

    while True:
        print("=====================MENU======================")
        print("|    1 - Adicionar funcionário                |")
        print("|    2 - Exibir cadastro de funcionários      |")
        print("|    3 - Calcular descontos e gerar relatório |")
        print("|    4 - Gráfico Geral                        |")
        print("|    5 - Sair                                 |")
        print("===============================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro(funcionarios)
        elif opcao == "2":
            exibir_cadastro(funcionarios)
        elif opcao == "3":
            relatorio(funcionarios)
        elif opcao == "4":
            criar_grafico(data)
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
