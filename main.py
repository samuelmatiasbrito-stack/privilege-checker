import csv

with open('roles.csv', newline='', encoding='utf-8') as Roles_Arq:
    Roles = csv.reader(Roles_Arq, delimiter=';')
    with open('restricted_privileges.csv', newline='', encoding='utf-8') as Privileges_Arq:
        Privileges = csv.reader(Privileges_Arq, delimiter=';')
        for Privilege in Privileges:
            for Role in Roles:
                if Role[0] in Privilege:
                    print(f' Apenas {Role[0]} possui o privilégio {Privilege[0]} ({Privilege[1]})')

