class Caneta():
    def __init__(self, cor):
        self.cor_TINTA = cor
    @property
    def cor(self):
        print('Voce chamou o property')
        return self.cor_TINTA

caneta = Caneta('Azul')
print(caneta.cor)




