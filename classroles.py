import csv 
class Arq:
    # def __init__(self, role, privilege):
    #     self.role = role
    #     self.privilege = privilege

    def caminho_arq(self, caminho):
        with open(caminho, newline='', encoding='utf-8') as arquivo:
            arquivo_list= list(csv.reader(arquivo, delimiter=';'))
            return arquivo_list

             

        