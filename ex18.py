
# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte', 'Teresina']
l2 = ['BA', 'SP', 'MG', 'PI']

def zipper(lista1, lista2):
    intervalo = max(len(lista1), len(lista2))
    lista_final = [
        [lista1[i], lista2[i]] for i in range(intervalo)
    ]
    return lista_final

print(*zipper(l1, l2), sep='\n')