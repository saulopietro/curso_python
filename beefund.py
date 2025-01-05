def annerichards(valor, tempo):
    while True:
        const_preço = 1.46
        if valor < 20 or valor > 100:
            print()
            print('Escolha um valor entre 20 e 100 dolares.')
            print()
            break

        aportes = tempo / 15

        if aportes  == 1:
            novo_valor = valor * const_preço
            print()
            print('Você terá: ', novo_valor,'dolares')
            print()
            break

        if aportes > 1:
            valores = []
            novo_valor = valor * const_preço
            valores.append(novo_valor)
            while (aportes - 1) > 0:
                valores.append(valores[-1] * 1.47)
                aportes -= 1
            print()
            print('Você terá: ', round(valores[-1], 2),'dolares')
            print()
            break


operadores = [
    'Anne Richards',
    'PEPPERSTONE',
    'Sabrina Gan'
]


while True:
    for i, n in enumerate(operadores):
        print(f'{i}: {n}')
    print()
    escolha = input('Escolha um operador: ')

    valor = int(input('Digite o valor em dolares: '))

    tempo = int(input('Quantos dias? "em múltiplos de 15": '))

    if escolha == '0':
        annerichards(valor, tempo)
        break