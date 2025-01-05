primeiro_valor = input('Digite um numero:')
segundo_valor = input('Digite outro numero:')

condicao0 = primeiro_valor > segundo_valor
condicao1 = segundo_valor > primeiro_valor  
condicao2 = primeiro_valor == segundo_valor

if condicao0:
    print(f'O numero {primeiro_valor} e maior que o numero {segundo_valor}')
elif condicao1:
    print(f'O numero {segundo_valor} e maior que o numero {primeiro_valor}')
elif condicao2:
    print(f'O numero {primeiro_valor} e igual que o numero {segundo_valor}')
