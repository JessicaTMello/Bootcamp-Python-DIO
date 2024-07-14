# %%
arquivo = open(
    r"C:\Users\Jessica\OneDrive - maferreira94.shop\Área de Trabalho\PYTHON-DIO\trilha-python-dio\05 - Manipulação de arquivos/teste.txt", "w"
)
arquivo.write("Escrevendo dados em um novo arquivo - jessica.")
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])
arquivo.close()

# %%
