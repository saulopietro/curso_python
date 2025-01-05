"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
n = input('Digite um numero inteiro:')
n: float
if n.isdigit():
    
    par_impar = n % 2 == 0
    if par_impar:
        print(f'O numero {n} e par')
    else:
        print (f'O numero {n} e impar')
else:
    print('O numero digitado nao e inteiro')
"""
Faça um programa que pergunte a h ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
h = input("Que horas sao?")
h: int
try:
    if h >= 0 and h <= 11:
        print('Bom dia')
    elif h >= 12 and h <= 17:
        print('Boa tarde')
    elif h >= 18 and h <= 23:
        print('Boa noite')
    else:
        print('Nao conheco essa hora')
except:
    print('Digite apenas numeros inteiros')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
n = input('Digite seu primeiro nome:')
qn = len(n)
if qn <= 4:
    print('Seu nome é curto')
elif qn >= 5 and qn <= 6:
    print('Seu nome é normal')
elif qn > 7:
    print("Seu nome é muito grande")
