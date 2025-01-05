# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#     a = x

#     def dentro():
#         # print(locals())

#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())
lista_de_letras = [n for n in range(100)]
def concatenar(string_inicial):
    valor_final = string_inicial
    def dentro(valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return dentro


while True:
    c = concatenar(1)
    for i, letra in enumerate(lista_de_letras):
        print(c(letra))
        
    break

        



