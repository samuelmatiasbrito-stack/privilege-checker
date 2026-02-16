import csv

class RolesValidator():
    
    def __init__(self, caminho_roles, caminho_prvrestritos):

        self.roles = self.LerArquivo(caminho_roles)
        self.privileges = self.LerArquivo(caminho_prvrestritos)   

    def LerArquivo(self, caminho):
        with open(caminho, newline='', encoding='utf-8') as arquivo:
            newarquivo = list(csv.reader(arquivo, delimiter=';'))
        return newarquivo
    
    def ListarRoles(self):
        coluna_roles = []
        for i, linha in enumerate(self.LerArquivo(self.roles), start= 1):
            coluna_roles.append(f'{i} - {linha[0]}')
        return coluna_roles
    
    def ObterRoleEspecifica(self, entrada):
        if entrada.isdigit():
            numero = int(entrada)
            try:
                role = self.LerArquivo(self.roles)[numero - 1]
                print(f"{role[0]} possui os privilegios: {', '.join(role[1:])}")
            except IndexError:
                print("selecione um numero válido")
            
    def ObterPrvRestritoRoleEspecifica(self,entrada):
        if entrada.isdigit() and int(entrada) <= len(self.ListarRoles()):
            indice_role = int(entrada) - 1
            encontrados = []
            for privilegio in self.LerArquivo(self.roles)[indice_role][1:]:
                for restrito in self.LerArquivo(self.privileges):
                    if privilegio == restrito[0]:
                        encontrados.append(f"{privilegio}: {restrito[1]}")
            if encontrados:
                return f"{self.LerArquivo(self.roles)[indice_role][0]} possui {' | '.join(encontrados)}"
            else:
                return f"{self.LerArquivo(self.roles)[indice_role][0]} não possui privilegios restritos"
        else:
            print(f'Aceito apenas números entre 1 - {len(self.ListarRoles(self.roles))}')



