import csv
with open('restricted_privileges.csv', newline= '', encoding= 'utf-8') as privilegios_arq:
    privilegios = list(csv.reader(privilegios_arq, delimiter=';'))
    with open('roles.csv', newline= '', encoding= 'utf-8') as direitos_arq:
        direitos = list(csv.reader(direitos_arq, delimiter=';'))
        for direito in direitos:
            for privilegio in privilegios:
                if privilegio[0] in direito:
                    print(f' Apenas {direito[0]} possui o privilégio {privilegio[0]} ({privilegio[1]})')
