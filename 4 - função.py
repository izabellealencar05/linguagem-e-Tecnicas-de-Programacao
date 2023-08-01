def soma_inteiros(n):
    if n <= 0:
        return 0  

    soma = 0
    for i in range(1, n + 1):
        soma += i

    return soma

n = int(input("digite um numero: "))
resultado = soma_inteiros_positivos(n)
print(f'A soma de todos os inteiros positivos até {n} é: {resultado}')
