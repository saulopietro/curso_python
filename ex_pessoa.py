class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def crescer(self, anos:int):
        self.altura = self.altura + anos * 0.5
        print(f'{self.nome} agora tem {self.idade} anos.')
        print(f'{self.nome} agora tem {self.altura} metros.')
   
    def envelhecer(self, anos : int):
        if self.idade <= 21:
            self.idade = self.idade + anos
            
            return self.crescer(anos)        
        self.idade = self.idade + anos
        print(f'{self.nome} agora tem {self.idade} anos.')
    
    def engordar(self, q_quilos):
        self.peso = self.peso + q_quilos
        print(f'{self.nome} agora tem {self.peso} quilos.')
        
    

p1 = Pessoa('Saulo', 13, 78, 1.40)
print(p1.idade)
print(p1.altura)
p1.envelhecer(5)
