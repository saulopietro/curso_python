salarios = []
filhos = []
media_salarioss = []


    

i = 0

while True:
    def media_salario(salarios):
        return salarios / i 
    
    salario = int(input('Qual o seu salário?: '))
    if salario == 'i':
        break
    i += 1

    
    media_salarioss += salario
    
    
    nfilhos = input('Quantos filhos você possui?: ')
    filhos.append(nfilhos)
    
print(media_salario(media_salarioss))
    

