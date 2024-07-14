# Crie uma classe UsuarioTelefone.
# Defina um método especial `__init__`, que é o construtor da classe.
# O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero' e `plano`.

# Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
# A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
# %%

class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo

    def verificar_saldo(self):
        if self.__saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.__saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
        
class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.__nome = nome
        self.__plano = plano
    
    def get_nome(self):
        return self.__nome
    
    def get_plano(self):
        return self.__plano
    
nome = input()
plano = input()
verificar_saldo = float(input())
    
usuario = UsuarioTelefone(nome, verificar_saldo)
plano_usuario = PlanoTelefone(nome, plano)

saldo_usuario, mensagem_usuario = verificar_saldo()
print(mensagem_usuario)

# %%
