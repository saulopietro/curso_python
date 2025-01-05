 # Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)
def criar_funcao(funcao):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        print('Vou te decorar')
        resultado = funcao(*args, **kwargs)
        return resultado
    return interna

@criar_funcao
def inverte(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Por favor, digite uma string')


invertida = inverte('Saulo')
print(invertida)