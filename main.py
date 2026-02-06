from classroles import RolesValidator
Validador = RolesValidator()

while True:
    question = input('Sistema carregado, qual consulta você deseja realizar? \n\
1- Consultar todos os privilegios de uma Role espécifica \n\
2- Consultar todos os privilegios restritos de uma Role espécifica \n\
3- Consultar todos os privilegios restritos de todas as Roles \n\
Opcao: ')
    if question == '1':
        print('Qual Role você quer consultar?: ')
        print(Validador.ListarRoles('roles.csv'))
        entrada = input('Digite o numero correspondente da Role: ')
        print(Validador.RoleEspecifica(entrada,'roles.csv'))
    elif question == '2':
        print('Qual Role você quer consultar?: ')
        print(Validador.ListarRoles('roles.csv'))
        entrada = input('Digite o numero correspondente da Role: ')
        print(Validador.PrvUnicaRole(entrada, 'roles.csv', 'restricted_privileges.csv'))

        
    elif question == '3':
        for Privilege in Validador.Arquivo('restricted_privileges.csv'):
            for Role in Validador.Arquivo('roles.csv'):
                if Privilege[0] in Role:
                    print(f'{Role[0]} possui {Privilege[0]}({Privilege[1]})')
    
    
        

                