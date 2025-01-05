# Exercício - sistema de perguntas e respostas

while True:

perguntas = {'Pergunta': 'Quanto é 2+2?', 'Opções': [1, 2, 3, 4, 5], 'Resposta': '4' }


print(perguntas['Pergunta'],)
print('Opçoes:', '\n',
        'A)',perguntas['Opções'][0], '\n',
        'B)',perguntas['Opções'][1], '\n',
        'C)',perguntas['Opções'][2], '\n',
        'D)',perguntas['Opções'][3], '\n',
        'E)',perguntas['Opções'][4])
resp = input('Digite uma resposta: ')

if  resp.isnumeric():
    if resp == perguntas['Resposta']:
        print('Pabens, voce acertou!')
        break
    else:
        print('Resposta errada, tente novamente')
        continue
else:
    print('Por favor, digite um numero inteiro')
    continue

