class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    
    
    def filmar(self):
        if self.filmando:
            return print(f'A camera {self.nome} já está filmando...')
        self.filmando = True
        print(f'A camera {self.nome} está filmando...')
    
    
    def parar_filmar(self):
        if self.filmando is False:
            return print(f'A camera {self.nome} não está filmando...')
        self.filmando = False
        print(f'A camera {self.nome} está parando de filmar...')
    
    def fotografar(self):
        if self.filmando:
            return print('Não e possivel fotografar enquanto filma')
        return print(f'A camera {self.nome} está fotografando...')


c1 = Camera('Sony')
print(c1.nome)
c1.filmar()
c1.parar_filmar()
c1.fotografar()






c2 = Camera('Canon')
print(c2.nome)
c2.filmar()
c2.parar_filmar()
c2.fotografar()