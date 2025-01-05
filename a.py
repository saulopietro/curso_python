def pedido(*itens, **informações):
    print('Itens do pedido: ')
    for item in itens:
        print(f'-- {item}')
        print()
    
    print('Informações adicionais: ')
    for chave, valor in informações.items():
        print (f'{chave}: {valor}')

pedidos = input('Quais sao os itens?: ')

pedido(pedidos, nome='João', mesa=5, )
