lista = []
while True:
    
    letra = input('Selecione uma opção\n[i]nserir [a]pagar [l]istar: ')

    lista_solo = []
    
    if letra == 'i':
        item = input('Item: ')
        lista.append(item)
        lista_solo.append(item)
        print(f'Voce adicionou {item} na sua lista')
        lista_solo.clear
    if letra == 'l':
        lista_enumerada = enumerate(lista)
        for item2 in lista_enumerada:
            a, b = item2
            print(a, b)
    if letra == 'a' and len(lista) > 0 :
        try:
            indice = input('Qual o indice voce deseja retirar?: ')
            indice_int = int(indice)
            del lista[indice_int]
        except ValueError:
            print('Por favor, digite um numero valido')
        except IndexError:
            print('Digite um indice valido')
           


    
        
        
    
