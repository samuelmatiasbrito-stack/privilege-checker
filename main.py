from classroles import Arq
arquivo = Arq()

for Privilege in arquivo.caminho_arq('restricted_privileges.csv'):
    for Role in arquivo.caminho_arq('roles.csv'):
        if Privilege[0] in Role:
            print(f'Apenas {Role[0]} possui o privilégio {Privilege[0]} ({Privilege[1]})')
