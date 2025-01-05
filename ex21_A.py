# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
CAMINHO_ARQUIVO = 'ex21.json'
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
p2 = Pessoa('Lustosa', 18, 90, 1.80)

dados = [p1.__dict__, p2.__dict__]






with open(CAMINHO_ARQUIVO, 'w', encoding='UTF8') as arquivo:
    json.dump(dados, arquivo, indent=2)
