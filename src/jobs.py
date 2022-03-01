from functools import lru_cache

# fazer o import do csv
import csv


@lru_cache
def read(path):
    # utilizar o with open(file) para abrir o arquivo
    with open(path) as file:
        # cria variavel csv_file  para acessar o arquivo csv
        csv_file = csv.DictReader(file)
        # retorna a lista do arquivo csv_file
        return list(csv_file)
