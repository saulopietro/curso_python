def somar(x, y):
    return x + y
def multiplicacao(x, y):
    return x * y
def divisao(x, y):
    return x / y
def subtracao(x, y):
    return x - y


while True:
    print('Operações: ')
    
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplição')
    print('4 - Divisão')

    op = input('Escolha uma operação (1, 2, 3, 4): ')
    op_permitadas = ('1, 2, 3, 4')
    
    if op not in op_permitadas:
        print('Digite uma operação valida')
        continue
    
    else:    
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))

        if op == '1':
            print('O resultado é:',somar(n1, n2))
        if op == '2':
            print('O resultado é:',subtracao(n1, n2))
        if op == '3':
            print('O resultado é:',multiplicacao(n1, n2))
        if op == '4':
            print('O resultado é:', divisao(n1, n2))
    break

    