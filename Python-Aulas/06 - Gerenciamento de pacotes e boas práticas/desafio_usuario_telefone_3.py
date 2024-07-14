# %%

class PlanoTelefone:
    def __init__(self, saldo):
        self.__saldo = saldo

    def deduzir_saldo(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        else:
            return False

    def obter_saldo(self):
        return self.__saldo

class UsuarioTelefone:
    CUSTO_POR_MINUTO = 0.10

    def __init__(self, nome, telefone, saldo):
        self.__nome = nome
        self.__telefone = telefone
        self.__plano = PlanoTelefone(saldo)

    def fazer_chamada(self, destinatario, duracao):
        custo = duracao * UsuarioTelefone.CUSTO_POR_MINUTO
        if self.__plano.deduzir_saldo(custo):
            saldo_restante = self.__plano.obter_saldo()
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${saldo_restante:.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

nome = input()
telefone = input()
saldo_inicial = float(input())

usuario = UsuarioTelefone(nome, telefone, saldo_inicial)

destinatario = input()
duracao = float(input())

print(usuario.fazer_chamada(destinatario, duracao))


# %%
