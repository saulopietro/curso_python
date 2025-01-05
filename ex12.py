def multi(*args):
    total = 1 
    for n in args:
        total *= n
    
    return total


print(multi(1,2,3,4,5,6,7,8,9,10))


def p_or_i(x):
    if int(x) % 2 == 0:
        return 'par'
    return 'Impar'
    
n = input('Digite um numero: ')

print(f'O Numero {n} é ',p_or_i(n))


