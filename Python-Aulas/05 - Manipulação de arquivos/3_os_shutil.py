import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

os.mkdir(ROOT_PATH / "diretorio_jessica")

arquivo = open(ROOT_PATH / "jessica.txt", "w")
arquivo.close()

os.rename(ROOT_PATH / "jessica.txt", ROOT_PATH / "mello.txt")

os.remove(ROOT_PATH / "mello.txt")

shutil.move(ROOT_PATH / "jessica.txt", ROOT_PATH / "novo-diretorio" / "jessica.txt")
