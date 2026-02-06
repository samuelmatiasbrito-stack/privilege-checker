import csv

class RolesValidator():
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
            
    def PrvUnicaRole(self,entrada, roles, prvrestritos):
        if entrada.isdigit():
            idx = int(entrada) - 1
            if 0 <= idx < len(self.Arquivo(roles)):
                role_nome = self.Arquivo(roles)[idx][0]
            else:
                print("numero invalido")
        else:
            role_nome = entrada
        for Privilege in self.Arquivo(prvrestritos):
            if Privilege[0].lower() == role_nome.lower():
                print(f"{role_nome} possui {Privilege[0]} ({Privilege[1]})")