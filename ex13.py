while True:
    def criar_multiplicador(multiplicador):
        def multiplicar(n):
            return n * multiplicador
        return multiplicar


    duplicado = criar_multiplicador(2)
    triplicado = criar_multiplicador(3)
    quadruplilicado = criar_multiplicador(4)

    n1 = input('Digite um numero: ')
    mult =input('Voce deseja [T]riplicar [D]uplicar ou [Q]uadruplicar :')
    
    
    if mult == 'd' or 't' or 'q':
        if mult == 'd':
            print(duplicado(int(n1)))
        if mult == 't':
            print(triplicado(int(n1)))
        if mult == 'q':  
            print(quadruplilicado(int(n1)))
    else:
        print('Por favor, digite uma opçao valida.')
        continue




