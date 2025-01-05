#divisao
n1 = input('Digite um numero: ')
n2 = input('Digite outro numero: ')
n1_float = float(n1)
n2_float = float(n2)
def divisor_nao_pode_ser_0(d):
    if d == 0:
        raise ZeroDivisionError('Voce esta tentado dividir por 0')

def tem_que_ser_int_ou_float(n):
    if not isinstance(n, (float, int)):
        raise TypeError('Digite um int ou float')


def dividir(n, d):
    divisor_nao_pode_ser_0(d)
    tem_que_ser_int_ou_float(n)
    tem_que_ser_int_ou_float(d)
    return n / d

print(dividir(n1_float, n2_float))