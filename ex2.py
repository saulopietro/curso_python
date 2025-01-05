nome = 'Saulo Pietro'
altura = 1.72
peso = 72
imc =  peso / altura ** 2                   # peso em quilos dividido por sua altura ao quadrado

linha_1 = f'{nome} tem {altura} de altura'
linha_2 = f'pesa {peso} quilos, e seu imc e'
linha_3 = f'{imc:.1f}'
print(linha_1)
print(linha_2)
print(linha_3)