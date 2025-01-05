import copy

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('Saulo', 17, 78, 1.72)

print()
