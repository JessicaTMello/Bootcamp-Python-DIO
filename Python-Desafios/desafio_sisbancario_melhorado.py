# %%

import textwrap

def menu():
    menu = """\n
    [1] \tDepositar
    [2] \tSacar
    [3] \tExtrato
    [4] \tNova conta
    [5] \tListar contas
    [6] \tNovo usuario
    [7] \tSair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("Deposito realizado com sucesso")
    else:
        print("Operação falhou! O valor informado é invalido.")

    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques > limite_saque

    if excedeu_saldo:
        print("Operação invalida! Você não possui saldo suficiente")

    elif excedeu_limite:
        print("Operação invalida! O valor do saque excede o limite")

    elif excedeu_saque:
        print("Operação invalida! Limite de saques excedidos")

    elif valor > 0:
        saldo -= valor
        extrato += f"saque:\t\tR$ {valor:.2f}\n"
        numero_saques +=1
        print("Saque realizado com sucesso!")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("informe o CPF(SOMENTE NUMEROS): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuarios:
        print("\n Já existe um usuario com esse CPF")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço(logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuario criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuario):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrato, fluxo de criação de conta encerrado")
    return None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            agencia:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

#DEPOSITO
# Essa função verifica se o deposito é maior que 0 e adiciona o valor ao saldo.
# Se for menor que 0 a função else apresenta a mensagem 

        if opcao == "1":
            valor = float(input("Informe o valor do seu deposito: "))
            saldo, extrato = depositar(saldo,valor,extrato)


# SAQUE
# Essa função verifica se o saque é maior que o valor do saldo
# Verifica também se o saque é maior que o limite por saque (nesse caso 500)
# E verifica se a quantidade de saque é maior que o limite de saque (nesse caso 3)

        elif opcao == "2":
            valor = float(input("Informe o valor do seu saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saque=LIMITE_SAQUES,
        )


# Essa função demonstra o extrato
        elif opcao == "3":
            exibir_extrato(saldo,extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            criar_usuario(usuarios)

# Essa função sai do loop
        elif opcao == "7":
            break

        else:
            print("Operação inválida, selecione novamente a operação desejada")

main()
       
# %%
