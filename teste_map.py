def multiplica_por_3(produto):
    return {**produto, 'preco': round(produto['preco'] * 3, 2)}
def aumentar_porcentam(valor, porcentagem):
    return valor * porcentagem
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

lista = map(
    multiplica_por_3,
    produtos
    )

print_iter(lista)

print(__name__)