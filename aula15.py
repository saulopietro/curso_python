nome = input('Qual o seu nome?')
idade = input('Qual a sua idade?')
altura = float(input('Qual a sua altura?'))
peso = float(input('Qual o seu peso?'))
imc = peso / altura ** 2

print(f'O seu imc e {imc:.2f}')