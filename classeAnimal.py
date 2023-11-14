class Animal():
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'o {self.nome} esta falando')
        print(f'e tem {self.idade} de idade')
        print('de idade')

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def latir(self):
        print(f'o {self.nome} esta latindo')
        print(f'e tem {self.idade} de idade')

class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def miar(self):
        print(f'o {self.nome} esta miando')
        print(f'e tem {self.idade} de idade')

c = Cachorro("marley", 4, "xow xow")
print(c)
