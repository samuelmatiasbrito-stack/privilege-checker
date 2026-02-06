import csv

class RolesValidator():
    def __init__(self, caminho):
        self.caminho = caminho
    def Arquivo(self, caminho):
        with open(caminho, newline='', encoding='utf-8') as arquivo:
            newarquivo = list(csv.reader(arquivo, delimiter=';'))
        return newarquivo
    
    def ListarRoles(self,caminho):
        coluna_roles = []
        for i, linha in enumerate(self.Arquivo(caminho), start= 1):
            coluna_roles.append(f'{i} - {linha[0]}')
        return coluna_roles
        # opção reduzida = return [f'{i} - {linha[0]}'for i, linha in enumerate(self.Arquivo(caminho), start= 1) ]
    
    def RoleEspecifica(self, entrada, caminho):
        roles = self.Arquivo(caminho)
        if entrada.isdigit():
            numero = int(entrada)
            try:
                role = roles[numero - 1]
                print(f"{role[0]} possui os privilegios: {', '.join(role[1:])}")
                return
            except IndexError:
                print("Número inválido")
                return
            
    def PrvUnicaRole(self,entrada, caminho_roles, caminho_prvrestritos):
        if entrada.isdigit() and int(entrada) <= len(self.ListarRoles(caminho_roles)):
            indice_role = int(entrada) - 1
            encontrados = []
            for privilegio in self.Arquivo(caminho_roles)[indice_role][1:]:
                for restrito in self.Arquivo(caminho_prvrestritos):
                    if privilegio == restrito[0]:
                        encontrados.append(f"{privilegio}: {restrito[1]}")
            if encontrados:
                return f"{self.Arquivo(caminho_roles)[indice_role][0]} possui {' | '.join(encontrados)}"
            else:
                return f"{self.Arquivo(caminho_roles)[indice_role][0]} não possui privilegios restritos"
        else:
            print(f'Aceito apenas números entre 1 - {len(self.ListarRoles(caminho_roles))}')



