while True:
    n1 = input('Digite um numero: ')
    n2 = input('Digite outro numero: ')
    op = input('Digite um operador (+-*/): ')

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        validar_numero = True
    except:
        validar_numero = None

        if validar_numero is None:
            print('Um ou ambos os elementos digitados sao invalidos')
            continue
    
    op_disp = ('+-/*')
    
    if op not in op_disp:
        print('O operador nao e valido')
        continue
    
    

    sair = input('Quer sair? [s]sim: ').startswith('s')
    break
print('Voce saiu!')