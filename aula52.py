lista = ['saulo', 'pietro', 'cr7']
lista_enumerada = list(enumerate(lista, start=1))

for nome in lista_enumerada:
    indice, palavra = nome
    print(indice, palavra) 