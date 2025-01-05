tarefas = []

tarefas_refazer = []

comandos = ['listar', 'desfazer','refazer']

i = -1
while True:
    print('Comandos: listar, desfazer, refazer')
    
    comando = input('Digite uma tarefa ou comando: ')

    if comando not in comandos:
        tarefas.append(comando)
        tarefas_refazer.append(comando)
        print()
        print('TAREFAS: ')
        print()
        print(*tarefas, sep='\n')
        print()
        continue

    if comando == 'listar':
        print()
        print('TAREFAS: ')
        print()
        print(*tarefas, sep='\n')
        print()
        continue

    if comando == 'desfazer':
        tarefas.pop(-1)
        print()
        print('TAREFAS: ')
        print()
        print(*tarefas, sep='\n')
        print()
        continue
    if comando == 'refazer':
        ultima_tarefa = tarefas_refazer(i)
        i += 1
        tarefas.append(ultima_tarefa)
        print()
        print('TAREFAS: ')
        print()
        print(*tarefas, sep='\n')
        print()
