primeiro_valor = input('Digite um numero:')
segundo_valor = input('Digite outro numero:')

if primeiro_valor > segundo_valor:
    print(f'O numero {primeiro_valor} e maior que o numero {segundo_valor}')
elif segundo_valor > primeiro_valor:
    print(f'O numero {segundo_valor} e maior que o numero {primeiro_valor}')
elif primeiro_valor == segundo_valor:
    print(f'O numero {primeiro_valor} e igual ao numero {segundo_valor}')