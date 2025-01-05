# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))
class Carro:
    def __init__(self, nome):
        self.nome = nome
    def acelerar(self):
        print(f'{self.nome} está acelerando...')
    def freiando(self):
        print(f'{self.nome} está freiando...')
fusca = Carro('fusca')

celta = Carro('celta')



fusca.freiando()