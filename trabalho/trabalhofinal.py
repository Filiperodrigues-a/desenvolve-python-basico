import csv

# Estrutura para carregar dados
usuarios = []
produtos = []

# Funções de gerência de arquivos
def carregar_usuarios(arquivo='usuarios.csv'):
    """Carrega usuários do arquivo CSV."""
    global usuarios
    with open(arquivo, 'r') as f:
        reader = csv.DictReader(f)
        usuarios = [linha for linha in reader]

def salvar_usuarios(arquivo='usuarios.csv'):
    """Salva usuários no arquivo CSV."""
    global usuarios
    with open(arquivo, 'w', newline='') as f:
        fieldnames = ['id', 'nome', 'tipo', 'senha']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(usuarios)

def carregar_produtos(arquivo='produtos.csv'):
    """Carrega produtos do arquivo CSV."""
    global produtos
    with open(arquivo, 'r') as f:
        reader = csv.DictReader(f)
        produtos = [linha for linha in reader]

def salvar_produtos(arquivo='produtos.csv'):
    """Salva produtos no arquivo CSV."""
    global produtos
    with open(arquivo, 'w', newline='') as f:
        fieldnames = ['codigo', 'nome', 'categoria', 'preco', 'quantidade']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(produtos)

# Funções CRUD
def criar_usuario():
    """Cadastra um novo usuário."""
    id = input("Digite o ID do usuário: ")
    nome = input("Digite o nome do usuário: ")
    tipo = input("Digite o tipo de usuário (gerente, funcionário, cliente): ")
    senha = input("Digite a senha: ")
    usuarios.append({'id': id, 'nome': nome, 'tipo': tipo, 'senha': senha})
    salvar_usuarios()

def listar_usuarios():
    """Lista todos os usuários (somente gerente)."""
    for user in usuarios:
        print(user)

def atualizar_usuario():
    """Atualiza informações de um usuário existente."""
    id = input("Digite o ID do usuário a ser atualizado: ")
    for user in usuarios:
        if user['id'] == id:
            user['nome'] = input(f"Novo nome ({user['nome']}): ") or user['nome']
            user['tipo'] = input(f"Novo tipo ({user['tipo']}): ") or user['tipo']
            salvar_usuarios()
            return
    print("Usuário não encontrado.")

def deletar_usuario():
    """Remove um usuário do sistema."""
    id = input("Digite o ID do usuário a ser removido: ")
    global usuarios
    usuarios = [user for user in usuarios if user['id'] != id]
    salvar_usuarios()

# Exemplo de inicialização
if __name__ == '__main__':
    carregar_usuarios()
    carregar_produtos()
    while True:
        print("\n1. Criar usuário\n2. Listar usuários\n3. Atualizar usuário\n4. Deletar usuário\n0. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            criar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            atualizar_usuario()
        elif opcao == '4':
            deletar_usuario()
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")
