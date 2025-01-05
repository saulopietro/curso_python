# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)


# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'Nome': 'Aline',
    'Sobrenome': 'Souza',
}
dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}




# print(pessoas_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def mostrar_argumentos_nomeados(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)


configurações = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}


mostrar_argumentos_nomeados(**configurações)