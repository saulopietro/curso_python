"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra = 'psicologico'
letra_certa = ''
while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Por favor, digite apenas um numero ')
        continue
    
    if letra in palavra:
        letra_certa += letra
    
    palavra_certa = ''
    
    for letras_secretas in palavra:
        if letras_secretas in letra_certa:
            palavra_certa += letras_secretas
        else:
            palavra_certa += '*'
           
        
    
    print(palavra_certa)

    if palavra_certa == palavra:
        print('Parabens, vôce ganhou!')