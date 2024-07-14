# Lembre-se de alterar o caminho do arquivo, para o caminho completo da sua máquina!
# %%
arquivo = open(
    r"C:\Users\Jessica\OneDrive - maferreira94.shop\Área de Trabalho\PYTHON-DIO\trilha-python-dio\05 - Manipulação de arquivos\lorem.txt", "r"
    )
print(arquivo.read()) #nesse caso lê todo o arquivo
arquivo.close()

# %%

arquivo = open(r"C:\Users\Jessica\OneDrive - maferreira94.shop\Área de Trabalho\PYTHON-DIO\trilha-python-dio\05 - Manipulação de arquivos\lorem.txt", "r")
print(arquivo.readline()) #nesse caso exibe uma linha por vez
arquivo.close()

# %%

arquivo = open(r"C:\Users\Jessica\OneDrive - maferreira94.shop\Área de Trabalho\PYTHON-DIO\trilha-python-dio\05 - Manipulação de arquivos\lorem.txt", "r")
print(arquivo.readlines()) #exibe todo o arquivo mas separa em uma lista
arquivo.close()

# %%
arquivo = open(r"C:\Users\Jessica\OneDrive - maferreira94.shop\Área de Trabalho\PYTHON-DIO\trilha-python-dio\05 - Manipulação de arquivos\lorem.txt", "r")
# tip
while len(linha := arquivo.readline()):
    print(linha)
arquivo.close()

# %%
