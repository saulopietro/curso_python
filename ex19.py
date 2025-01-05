l1 = [1, 2, 3, 4, 5, 6, 7,]
l2 = [1, 2, 3 , 4]

def somar_listas(lista1, lista2):
    return [x + y for x, y in zip(lista1, lista2)]

print(somar_listas(l1, l2))