import matplotlib.pyplot as plt

precoMercadorias = {}
vendas = {}

def lerPrecos():
    while True:
        try:
            mercadoria = int(input("Digite o número da mercadoria: "))
            preco = float(input(f"Digite o preço da mercadoria {mercadoria}: "))
            precoMercadorias[mercadoria] = preco
            adicionarPrecos = input("Deseja adicionar mais preços? (S/N): ").strip().lower()
            if adicionarPrecos != 's':
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos para o número da mercadoria e o preço.")

def calcularFaturamento(vendas):
    faturamento = 0
    for mercadoria, quantidade in vendas.items():
        preco = precoMercadorias.get(int(mercadoria), 0)
        faturamento += quantidade * preco
    return faturamento

def imprimirFaturamento(faturamento):
    print("------------------------------------------------FATURAMENTO------------------------------------------------")
    for mercadoria, quantidade in vendas.items():
        preco = precoMercadorias.get(int(mercadoria), 0)
        subtotal = quantidade * preco
        print(f"Mercadoria {mercadoria}: {quantidade} unidades vendidas a R${preco:.2f} cada (Total: R${subtotal:.2f})")
    print(f"Faturamento Total: R${faturamento:.2f}")
    print("-----------------------------------------------------------------------------------------------------------")

def calcularPercentual(faturamento):
    percentuais = {}
    for mercadoria, quantidade in vendas.items():
        preco = precoMercadorias.get(mercadoria, 0)
        subtotal = quantidade * preco
        percentual = (subtotal / faturamento) * 100
        percentuais[mercadoria] = percentual
    return percentuais

def imprimirPercentuais(percentuais):
    print("Percentuais de vendas por mercadoria sobre o total faturado:")
    for mercadoria, percentual in percentuais.items():
        print(f"Mercadoria {mercadoria}: {percentual:.2f}%")

def lerMercadorias():
    faturamento = 0
    try:
        mercadoriasCalculo = input("Digite os números das mercadorias para o cálculo do faturamento (separados por espaço): ").split()
        for mercadoria in mercadoriasCalculo:
            quantidade = int(input(f"Digite a quantidade vendida da mercadoria {mercadoria}: "))
            vendas[mercadoria] = quantidade
            preco = precoMercadorias.get(mercadoria, 0)
            subtotal = quantidade * preco
            faturamento += subtotal
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")
    return faturamento

def salvarDados(nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write("Mercadoria\tQuantidade\tPreço\n")
            for mercadoria, quantidade in vendas.items():
                preco = precoMercadorias.get(mercadoria, 0)
                arquivo.write(f"{mercadoria}\t{quantidade}\t{preco:.2f}\n")
    except Exception as e:
        print(f"Erro ao salvar dados: {str(e)}")

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
    faturamento = 0
    while True:
        print("===================MENU===================")
        print("|    1 - Adicionar preços                |")
        print("|    2 - Calcular faturamento            |")
        print("|    3 - Mostrar faturamento             |")
        print("|    4 - Percentual de vendas            |")
        print("|    5 - Mostrar gráfico de vendas       |")
        print("|    6 - Sair do programa                |")
        print("==========================================")
        opcao = input("Digite uma opção: ")

        if opcao == '1':
            lerPrecos()
        elif opcao == '2':
            faturamento = calcularFaturamento(vendas)
            print("Cálculo de faturamento concluído.")
        elif opcao == '3':
            imprimirFaturamento(faturamento)
        elif opcao == '4':
            if faturamento > 0:
                percentuais = calcularPercentual(faturamento)
                imprimirPercentuais(percentuais)
            else:
                print("Antes de calcular o percentual, você precisa calcular o faturamento.")
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

if __name__ == "__main__":
    main()
