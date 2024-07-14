# %%

# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal: 
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
if consumo <= 10:
    print ("O plano ideal para o seu consumo de", consumo, "é o Plano Essencial Fibra - 50Mbps")

elif consumo <=20:
    print("O plano ideal para o seu consumo de", consumo, "é o Plano Prata Fibra - 100Mbps")

else:
    print("O plano ideal para o seu consumo de", consumo, "é o Plano Premium Fibra - 300Mbps")


# %%

def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB."
    elif 10 < consumo <= 20:
        return "Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB."
    else:
        return "Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB."

def main():
    while True:
        try:
            consumo_mensal = float(input("Por favor, insira o seu consumo médio mensal de dados em GB: "))
            if consumo_mensal < 0:
                print("O consumo de dados deve ser um valor positivo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    plano_recomendado = recomendar_plano(consumo_mensal)
    print(plano_recomendado)

if __name__ == "__main__":
    main()
# %%
