class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'{self.nome} está falando')
        print(f'E tem {self.idade} anos de idade')

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def latir(self):
        print(f'{self.nome} está latindo')
        print(f'E tem {self.idade} anos de idade')
        print(f"a raca e {self.raca}")

class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def miar(self):
        print(f'{self.nome} está miando')
        print(f'E tem {self.idade} anos de idade')
        print(f'A raça é {self.raca}')

class Leao(Animal):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.cor = cor

    def rugir(self):
        print(f'{self.nome} esta rugindo')
        print(f'e tem {self.idade} anos')
        print(f'e tem uma juba da cor {self.cor}')

def main():
    nome = input("qual o seu nome: ")
    idade = int(input("qual a sua idade: "))
    pessoa = Animal(nome, idade)

    nomeC = input("qual o nome do cachorro? ")
    idadeC = int(input("qual a idade do cachorro? "))
    racaC = input("qual a raca do cachorro? ")
    cachorro = Cachorro(nomeC, idadeC, racaC)

    nomeG = input("qual o nome do gato? ")
    idadeG = int(input("qual a idade do gato: "))
    racaG = input("qual a raca do gato: ")
    gato = Gato(nomeG, idadeG, racaG)

    nomeL = input("qual o nome do leao: ")
    idadeL = int(input("qual a idade do leao: "))
    corL = input("qual a cor da juba do leao: ")
    leao = Leao(nomeL, idadeL, corL)

    pessoa.falar()
    cachorro.latir()
    gato.miar()
    leao.rugir()

if __name__ == "__main__":
    main()
