import csv

class DireitoAcesso:
    def __init__(self, nome_direitodeacesso, nome_privilegios):
        self.nome = nome_direitodeacesso
        self.privilegios = nome_privilegios

with open('roles.csv', newline='', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo, delimiter= ';')
    for linha in leitor:
        if 'prvReadAccount' in linha:
            print(linha)