for Privilege in Privileges:
            for Role in Roles:
                if Role[0] in Privilege:
                    print(f' Apenas {Role[0]} possui o privilégio {Privilege[0]} ({Privilege[1]})')