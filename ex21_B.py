import json
from ex21_A import CAMINHO_ARQUIVO, Pessoa

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)
    
    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])

print(p1.nome)

