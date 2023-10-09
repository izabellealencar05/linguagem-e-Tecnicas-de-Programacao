import matplotlib.pyplot as plt
precoMercadorias = {}
vendas = {}

def lerPrecos():
    adicionarPrecos = input("Deseja adicionar preços para as mercadorias? (S/N): ").strip().lower()

    while adicionarPrecos == 's':
        mercadoria = int(input("Digite o número da mercadoria: "))
        preco = float(input(f"Digite o preço da mercadoria {mercadoria}: "))
        precoMercadorias[mercadoria] = preco
        adicionarPrecos = input("Deseja adicionar mais preços? (S/N): ").strip().lower()


def lerMercadorias():
    mercadoriasCalculo = input("Digite os números das mercadorias para o cálculo do faturamento (separados por espaço): ").split()
    mercadoriasCalculo = [int(mercadoria) for mercadoria in mercadoriasCalculo]

    for mercadoria in mercadoriasCalculo:
        quantidade = int(input(f"Digite a quantidade vendida da mercadoria {mercadoria}: "))
        vendas[mercadoria] = quantidade


def calcularFaturamento():
    faturamento = 0
    for mercadoria, quantidade in vendas.items():
        preco = precoMercadorias.get(mercadoria, 0)
        faturamento += quantidade * preco
    return faturamento


def imprimirFaturamento(faturamento):
    print("Faturamento Mensal:")
    for mercadoria, quantidade in vendas.items():
        preco = precoMercadorias.get(mercadoria, 0)
        subtotal = quantidade * preco
        print(f"Mercadoria {mercadoria}: {quantidade} unidades vendidas a R${preco:.2f} cada (Total: R${subtotal:.2f})")
    print(f"Faturamento Total: R${faturamento:.2f}")

def calcular_percentuais_faturamento(faturamento):
    percentuais = {}
    for mercadoria, quantidade in vendas.items():
        preco = precoMercadorias.get(mercadoria, 0)
        subtotal = quantidade * preco
        percentual = (subtotal / faturamento) * 100
        percentuais[mercadoria] = percentual
    return percentuais

def imprimir_percentuais(percentuais):
    print("Percentuais de vendas por mercadoria sobre o total faturado:")
    for mercadoria, percentual in percentuais.items():
        print(f"Mercadoria {mercadoria}: {percentual:.2f}%")



def salvar_dados_vendas_arquivo(nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write("Mercadoria\tQuantidade\tPreço\n")
        for mercadoria, quantidade in vendas.items():
            preco = precoMercadorias.get(mercadoria, 0)
            arquivo.write(f"{mercadoria}\t{quantidade}\t{preco}\n")


def main():
    lerPrecos()
    lerMercadorias()
    faturamento = calcularFaturamento()
    imprimirFaturamento(faturamento)
    percentuais = calcular_percentuais_faturamento(faturamento)
    imprimir_percentuais(percentuais)
    nome_arquivo = "dados_vendas.txt"
    salvar_dados_vendas_arquivo(nome_arquivo)

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
