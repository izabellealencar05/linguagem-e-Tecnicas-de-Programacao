a = {1, 2, 3, 4, 5, 6}
b = {2, 4, 6}
print('conjunto a', a)
print('conjunto b', b)
print(b.issubset(a)) #b e subconjunto de A
print(a.difference(b)) #numeros q tem em A mas n tem em B
print(a.isdisjoint(b))
print(b)
print("a - b= ", a - b)
print('')
print("a uniao B ", a | b)
print("")
print("a intersecao B", a & b)
print("")
print('diferenca simetrica', b ^ a)
print('B pertence a', b in a)
print("")
print("2 pertence a", 2 in a)
