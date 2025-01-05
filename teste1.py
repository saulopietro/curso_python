lista = [n for n in range(100)]
numero_certo = 73

while True:
    numero_escolhido = input('Escolha um número: ')
    numero_escolhido_int = int(numero_escolhido)
    
    if numero_escolhido_int > numero_certo:
        print('Numero alto')
        continue
    if numero_escolhido_int < numero_certo:
        print('chute baixo')
        continue
    if numero_escolhido_int == numero_certo:
        print('Voce achou o numero!')
        break

