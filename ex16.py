
from dados import produtos
import copy

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
print(*produtos, sep='\n')
print()


novos_produtos = [{**produtos, 'preco': round(produtos['preco'] * 1.1, 2)}
for produtos in copy.deepcopy(produtos)]

print(*novos_produtos, sep='\n')
print()


produtos_ordenados_por_nome = sorted(produtos,
key=lambda p: p['nome'],
reverse = True)
print(*produtos_ordenados_por_nome, sep='\n')
print()


produtos_ordenados_por_preco = sorted(produtos, key=lambda p: p['preco'])
print(*produtos_ordenados_por_preco, sep='\n')



