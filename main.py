import csv

with open('roles.csv', newline= '', encoding= 'utf-8') as direitos_arq:
    direitos = csv.reader(direitos_arq, delimiter=';')
    with open('restricted_privileges.csv', newline= '', encoding= 'utf-8') as privilegios_arq:
        privilegios = csv.reader(privilegios_arq, delimiter=';')
        ## parei na criação do for
            
            
