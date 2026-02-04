from models import SecurityRole

def carregar_roles(caminho_arquivo):
    """
    Lê o CSV de roles e retorna uma lista de objetos SecurityRole.
    """
    lista_de_roles = []
    
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            # Remove espaços em branco e quebras de linha nas pontas
            linha_limpa = linha.strip()
            
            # Pula linhas vazias
            if not linha_limpa:
                continue
            
            # Divide a linha pelo separador ';'
            partes = linha_limpa.split(';')
            
            # O primeiro item é o nome da role
            nome_role = partes[0]
            # O restante da lista (do índice 1 em diante) são os privilégios
            privilegios = partes[1:]
            
            # Criamos a instância da classe (o objeto)
            nova_role = SecurityRole(nome_role, privilegios)
            
            # Guardamos o objeto na nossa lista
            lista_de_roles.append(nova_role)
            
    return lista_de_roles

def carregar_privilegios_restritos(caminho_arquivo):
    """
    Lê o CSV de restritos e retorna apenas a lista de nomes dos privilégios.
    """
    restritos = []
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        # Pular o cabeçalho (privilegio;descricao_risco)
        next(arquivo) 
        
        for linha in arquivo:
            partes = linha.strip().split(';')
            if partes:
                restritos.append(partes[0]) # Pega só o nome do privilégio
    return restritos

# --- Execução Principal ---
# 1. Carregamos os dados
minhas_roles = carregar_roles('roles.csv')
lista_negra = carregar_privilegios_restritos('restricted_privileges.csv')

print(f"Sistema carregado: {len(minhas_roles)} roles e {len(lista_negra)} privilégios críticos.\n")

# 2. Cenário 1 - Verificar todas as Roles
for role in minhas_roles:
    print(f"Analisando: {role.nome} ({len(role.privilegios)} privilégios)")
    for priv in role.privilegios:
        if priv in lista_negra:
            print(f"Role {role.nome} contém privilégio restrito {priv}")
            
# 3. Cenário 2 - Verificar uma Role
while True:
    roleName = input("\nDigite o nome da Role a ser verificada: ")
    for role in minhas_roles:
        if role.nome == roleName:
            privRestritosEncontrados = []
            for priv in role.privilegios:
                if priv in lista_negra:
                    privRestritosEncontrados.append(priv)
            if len(privRestritosEncontrados) > 0:
                print(f"Role {role.nome} contém privilégios restritos: {privRestritosEncontrados}")
            else:
                print(f"Role {role.nome} não contém privilegios restritos!")