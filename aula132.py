class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
        

    @property
    def get_cor(self):
        print('PROPERTY')
        return self.cor_tinta

def mostrar_cor(caneta):
    return caneta.cor

caneta_1 = Caneta('Azul')
mostrar_cor(caneta_1)