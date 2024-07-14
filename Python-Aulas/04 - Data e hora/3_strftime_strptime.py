# %%

from datetime import datetime

#Formatando data e hora 17/06/2024 11:26

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))

# %%
