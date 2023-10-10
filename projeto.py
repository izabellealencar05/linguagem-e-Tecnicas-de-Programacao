import matplotlib.pyplot as plt

precoMercadorias = {}  
vendas = {} 
def lerPrecos():
    while True:  
        mercadoria = int(input("Digite o número da mercadoria: "))  
        preco = float(input(f"Digite o preço da mercadoria {mercadoria}: "))  
        precoMercadorias[mercadoria] = preco  
        adicionarPrecos = input("Deseja adicionar mais preços? (S/N): ").strip().lower()  
        if adicionarPrecos != 's':
            break  

def calcularFaturamento(vendas):
    faturamento = 0  
    for mercadoria, quantidade in vendas.items():  
        preco = precoMercadorias.get(int(mercadoria), 0)  
        faturamento += quantidade * preco  
    return faturamento  

def imprimirFaturamento(faturamento):
    print("------------Faturamento------------")
    for mercadoria, quantidade in vendas.items():  
        preco = precoMercadorias.get(int(mercadoria), 0) 
        subtotal = quantidade * preco  
        print(f"Mercadoria {mercadoria}: {quantidade} unidades de R${preco:.2f}")
        print(f"Total: R${subtotal:.2f})")
    print(f"Faturamento: R${faturamento:.2f}")
    print("-----------------------------------")

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
    for mercadoria in mercadoriasCalculo: 
        quantidade = int(input(f"Digite a quantidade vendida da mercadoria {mercadoria}: "))  
        vendas[mercadoria] = quantidade  

def salvarDados(nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write("Mercadoria\tQuantidade\tPreço\n")
        for mercadoria, quantidade in vendas.items():
            preco = precoMercadorias.get(mercadoria, 0)
            arquivo.write(f"{mercadoria}\t{quantidade}\t{preco}\n")

def menu():
    print("===================MENU===================")
    print("|    1 - adicionar preço                 |")
    print("|    2 - fazer o calculo do faturamento  |")
    print("|    3 - mostrar o faturamento           |")
    print("|    4 - percentual de vendas            |")
    print("|    5 - sair                            |")
    print("==========================================")
    faturamento = 0 
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
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    menu()
    nome_arquivo = "dados_vendas.txt"
    salvarDados(nome_arquivo)

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

if __name__ == "__main__":
    main()  
