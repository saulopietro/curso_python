class Vendedor:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0
    
    def vendeu(self, vendas):
        self.vendas = vendas
    
    def bateu_meta(self, meta):
        if self.vendas >= meta:
            print(f'O vendedor {self.nome} bateu as metas')
        else:
            print((f'O vendedor {self.nome} não bateu as metas'))

vendedor1 = Vendedor('Saulo')
vendedor1.vendeu(500)
vendedor1.bateu_meta(600)


vendedor2 = Vendedor('Lustosa')
vendedor2.vendeu(1000)
vendedor2.bateu_meta(700)

    