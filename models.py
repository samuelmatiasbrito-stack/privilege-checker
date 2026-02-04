class SecurityRole:
    def __init__(self, nome_da_role, lista_de_privilegios):
        """
        Construtor da classe. 
        nome_da_role: string (ex: 'executivo')
        lista_de_privilegios: list (ex: ['prvReadAccount', 'prvWriteAccount'])
        """
        self.nome = nome_da_role
        self.privilegios = lista_de_privilegios