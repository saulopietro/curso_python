
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()



produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos_multiplicador_por_2 = [{**n, 'preco': n['preco'] * 2} for n in produtos]


    

print(*produtos_multiplicador_por_2, sep='\n')