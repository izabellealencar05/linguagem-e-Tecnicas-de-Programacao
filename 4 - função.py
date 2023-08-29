def somadosnum(n):
  if n <= 0:
    return 0
  soma = 0
  for i in range(1, n + 1):
    soma += i
  return soma
n = int(input("digite um numero: "))
resultado = somadosnum(n)
print(f'a soma de todos os inteiros positivos ate {n} é {resultado}')
