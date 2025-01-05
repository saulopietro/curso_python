# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 20
    for numero in range(120)
]


produtos = [
    {'nome': 'p1', 'preço': 10},
    {'nome': 'p2', 'preço': 20},
    {'nome': 'p3', 'preço': 30}
]

novos_produtos = [
    {**item, 'preço': item['preço'] * 1.05}
    if item['preço'] > 20 else {**item}
    for item in produtos 
]


#p(novos_produtos)
lista = [n for n in range(10) if n < 7]
print(lista)























118,82
118,00
118,93
355,73


150,89
142,90
144,97

438,76