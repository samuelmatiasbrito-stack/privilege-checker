from classroles import RolesValidator
Validador = RolesValidator('roles.csv', 'restricted_privileges.csv')

while True:
    question = input('Sistema carregado, qual consulta você deseja realizar? \n\
1- Consultar todos os privilegios de uma Role espécifica \n\
2- Consultar todos os privilegios restritos de uma Role espécifica \n\
3- Consultar todos os privilegios restritos de todas as Roles \n\
Opcao: ')
    if question == '1':
        print('Qual Role você quer consultar?: ')
        print(Validador.ListarRoles())
        entrada = input('Digite o numero correspondente da Role: ')
        print(Validador.RoleEspecifica(entrada))
    elif question == '2':
        print('Qual Role você quer consultar?: ')
        print(Validador.ListarRoles())
        entrada = input('Digite o numero correspondente da Role: ')
        print(Validador.PrvUnicaRole(entrada))

        
    elif question == '3':
        for Privilege in Validador.Arquivo(Validador.caminho_prvrestritos):
            for Role in Validador.roles:
                if Privilege[0] in Role:
                    print(f'{Role[0]} possui {Privilege[0]}({Privilege[1]})')

                