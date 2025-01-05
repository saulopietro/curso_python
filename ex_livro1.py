preços = [{'nome': 'maçã', 'preco': 1.98,},
        {'nome': 'abacate', 'preco': 8.25}, 
        {'nome': 'tomate', 'preco': 2.38},  
        {'nome': 'carne', 'preco': 18.00}]
print('preços antigos: ', *preços, sep='\n')
print()
print('preços ajustados: ')
preços_ajustados = [{**i, 'preco': round(i['preco'] * 1.10, 2) } for i in preços]
print(*preços_ajustados, sep='\n')

