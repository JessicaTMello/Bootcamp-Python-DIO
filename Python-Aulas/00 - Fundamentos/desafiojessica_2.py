# %%

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

# Essa função verifica se o deposito é maior que 0 e adiciona o valor ao saldo.
# Se for menor que 0 a função else apresenta a mensagem 
    if opcao == "1":
        valor = float(input("Informe o valor do seu deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
    
        else: print("Operação falhou! O valor informado é inválido!")


# Essa função verifica se o saque é maior que o valor do saldo
# Verifica também se o saque é maior que o limite por saque (nesse caso 500)
# E verifica se a quantidade de saque é maior que o limite de saque (nesse caso 3)
    elif opcao == "2":
        valor = float(input("Informe o valor do seu saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_limite_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_limite_saque:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques

        else:
            print("Operação falhou! O valor informado é inválido.")


# Essa função demonstra o extrato
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")


# Essa função sai do loop
    elif opcao == "4":
        break
    else:
        print("Operação inválida, selecione novamente a operação desejada")


       
# %%
