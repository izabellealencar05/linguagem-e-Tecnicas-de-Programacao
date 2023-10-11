import matplotlib.pyplot as plt

precoMercadorias = {}  # Dicionário criado para armazenar os preços das mercadorias
vendas = {}  # Dicionário criado para armazenar as quantidades vendidas de mercadorias

def lerPrecos():
    while True:  # Loop infinito para ler os preços das mercadorias
        mercadoria = int(input("Digite o número da mercadoria: "))  # Solicita o número da mercadoria
        preco = float(input(f"Digite o preço da mercadoria {mercadoria}: "))  # Solicita o preço da mercadoria
        precoMercadorias[mercadoria] = preco  # Armazena o preço no dicionário
        adicionarPrecos = input("Deseja adicionar mais preços? (S/N): ").strip().lower()  # Pergunta se deseja adicionar mais preços
        if adicionarPrecos != 's':
            break  # Sai do loop se a resposta não for 's'

def calcularFaturamento(vendas):
    faturamento = 0  # Inicializa a variável Faturamento como 0
    for mercadoria, quantidade in vendas.items():  # Percorre as mercadorias vendidas
        preco = precoMercadorias.get(int(mercadoria), 0)  # Obtém o preço da mercadoria ou 0 se não existir
        faturamento += quantidade * preco  # Calcula o faturamento
    return faturamento  # Retorna o valor do faturamento

def imprimirFaturamento(faturamento):
    print("------------------------------------------------FATURAMENTO------------------------------------------------")
    for mercadoria, quantidade in vendas.items():  # Percorre as mercadorias vendidas
        preco = precoMercadorias.get(int(mercadoria), 0)  # Obtém o preço da mercadoria ou 0 se não existir
        subtotal = quantidade * preco  # Calcula o subtotal
        print(f"Mercadoria {mercadoria}: {quantidade} unidades vendidas a R${preco:.2f} cada (Total: R${subtotal:.2f})")
    print(f"Faturamento Total: R${faturamento:.2f}")
    print("-----------------------------------------------------------------------------------------------------------")
def calcularPercentual(faturamento):
    percentuais = {}
    for mercadoria, quantidade in vendas.items():
        preco = precoMercadorias.get(int(mercadoria), 0)
        subtotal = quantidade * preco
        percentual = (subtotal / faturamento) * 100
        percentuais[mercadoria] = percentual
    return percentuais

def imprimirPercentuais(percentuais):
    print("Percentuais de vendas por mercadoria sobre o total faturado:")
    for mercadoria, percentual in percentuais.items():
        print(f"Mercadoria {mercadoria}: {percentual:.2f}%")

def lerMercadorias():
    mercadoriasCalculo = input("Digite os números das mercadorias para o cálculo do faturamento (separados por espaço): ").split()
    for mercadoria in mercadoriasCalculo:  # Percorre as mercadorias informadas
        quantidade = int(input(f"Digite a quantidade vendida da mercadoria {mercadoria}: "))  # Solicita a quantidade vendida
        vendas[mercadoria] = quantidade  # Armazena a quantidade vendida no dicionário de vendas

def salvarDados(nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write("Mercadoria\tQuantidade\tPreço\n")
        for mercadoria, quantidade in vendas.items():
            preco = precoMercadorias.get(mercadoria, 0)
            arquivo.write(f"{mercadoria}\t{quantidade}\t{preco}\n")

def grafico():
    mercadorias_ordenadas = sorted(vendas.items(), key=lambda x: x[1], reverse=True)
    top_5_mercadorias = mercadorias_ordenadas[:5]
    mercadorias, quantidades = zip(*top_5_mercadorias)
    plt.figure(figsize=(10, 6))
    plt.bar(mercadorias, quantidades)
    plt.xlabel('Mercadorias')
    plt.ylabel('Quantidades Vendidas')
    plt.title('Top 5 Mercadorias Mais Vendidas no Mês')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def menu():
    print("===================MENU===================")
    print("|    1 - adicionar preço                 |")
    print("|    2 - fazer o calculo do faturamento  |")
    print("|    3 - mostrar o faturamento           |")
    print("|    4 - percentual de vendas            |")
    print("|    5 - mostrar o grafico de vendas     |")
    print("|    6 - sair do programa                |")
    print("==========================================")
    faturamento = 0  # Inicializa faturamento como 0
    while True:
        opcao = input("Digite uma opção: ")

        if opcao == '1':
            lerPrecos()
        elif opcao == '2':
            lerMercadorias()
            faturamento = calcularFaturamento(vendas)
        elif opcao  == '3':
            imprimirFaturamento(faturamento)
        elif opcao == '4':
            percentuais = calcularPercentual(faturamento)
            imprimirPercentuais(percentuais)
        elif opcao == '5':
            grafico()
        elif opcao == '6':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
def main():
    menu()
    nome_arquivo = "dados_vendas.txt"
    salvarDados(nome_arquivo)
    grafico()


if __name__ == "__main__":
    main() 
