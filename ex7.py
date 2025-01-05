frase = "o rato roeu a roupa do rei de roma "
i = 0

while i < len(frase):
    letra_atual = frase[i]
    qtsvzsapareceu = frase.count(letra_atual)
   
    if letra_atual == " ":
        i += 1
        continue    
    print(f'Letra:{letra_atual} apareceu:{qtsvzsapareceu} vezes')
    
    i += 1 