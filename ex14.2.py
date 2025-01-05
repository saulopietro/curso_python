quest = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
i = 0
while True:
    for pergunta in quest:
        print('Pergunta: ', pergunta['Pergunta'])
        print()
        
        for i, opcao in enumerate(pergunta['Opções']):
            print(f'{i})', opcao)
        print()
        
        escolha = input('Escolha uma opcao: ')
        print()
        if escolha == pergunta['Resposta']:
            print('Parabens, voce acertou')
            print()
            i += 0
        else:
            print('Voce errou!')
            print()
    break
    

print(f'Voce acertou {i} perguntas')    