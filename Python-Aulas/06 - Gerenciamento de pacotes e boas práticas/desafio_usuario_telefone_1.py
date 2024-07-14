# Crie uma classe UsuarioTelefone.
# Defina um método especial `__init__`, que é o construtor da classe.
# O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero' e `plano`.

# Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
# A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
# %%
class UsuarioTelefone:
    def __init__(self, nome, numero_telefone, plano):
        self.__nome = nome
        self.__numero_telefone = numero_telefone
        self.__plano = plano
        print("Usuário", nome, "criado com sucesso.")
    
    def get_nome(self):
        return self.__nome

    def get_numero_telefone(self):
        return self.__numero_telefone
    
    def get_plano(self):
        return self.__plano

def validar_numero_telefone(numero_telefone):
    return len(numero_telefone) == 15 and numero_telefone[0] == '(' and numero_telefone[3] == ')' and numero_telefone[5] == '9' and numero_telefone[10] == '-'

def criar_usuario():
    nome = input()
    numero_telefone = input()
    plano = input()
    
    usuario = UsuarioTelefone(nome, numero_telefone, plano)

criar_usuario()
# %%
