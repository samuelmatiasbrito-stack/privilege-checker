import csv
from classroles import Arq


with open('roles.csv', newline='', encoding='utf-8') as Roles_Arq:
    Roles = list(csv.reader(Roles_Arq, delimiter=';'))
    with open('restricted_privileges.csv', newline='', encoding='utf-8') as Privileges_Arq:
        Privileges = list(csv.reader(Privileges_Arq, delimiter=';'))
        for Privilege in Privileges:
            for Role in Roles:
                if Privilege[0] in Role:
                    print(f'Apenas {Role[0]} possui o privilégio {Privilege[0]} ({Privilege[1]})')


arquivo = Arq()

print(arquivo.caminho_arq('roles.csv'))
