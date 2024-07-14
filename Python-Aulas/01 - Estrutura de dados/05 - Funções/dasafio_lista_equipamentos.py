# %%
# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
# TODO: Crie um loop para solicita os itens ao usuário:
# TODO: Solicite o item e armazena na variável "item":
# TODO: Adicione o item à lista "itens":

equipamentos = []

for i in range(3):
    itens = input()
    equipamentos.append(itens)
    print()

# Exibe a lista de itens
print("\nLista de Equipamentos:")  
for item in equipamentos:
    print(f"- {item}")

# %%
