# %%

from datetime import datetime

import pytz

oslo = datetime.now(pytz.timezone("Europe/Oslo"))
sao_paulo = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(oslo)
print(sao_paulo)

# %%
