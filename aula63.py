import random
import sys


for _ in range(100):
    nove_digitos = ''

    for i in range(9):
        nove_digitos += str(random.randint(0, 9))


    contador_regressivo = 10
    resultado = 0 
    for digito in nove_digitos:
        resultado += int(digito) * contador_regressivo
        contador_regressivo -= 1
        
    digito_1 = ((resultado * 10) % 11)
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo2 = 11
    resultado2 = 0
    for digitos in dez_digitos:
        resultado2 += int(digitos) * contador_regressivo2
        contador_regressivo2 -= 1
    digito_2 = ((resultado2 * 10) % 11) 
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'  

    print(cpf_gerado)


    