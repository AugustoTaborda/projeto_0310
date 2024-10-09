import requests
API_URL = "http://127.0.0.1:5000/usuarios"
def get_usuarios():
    response = requests.get(API_URL)
    if response.status_code == 200:
        usuarios = response.json()
        print("Usuários cadastrados:")
    for usuario in usuarios:
        print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, E-mail: {usuario['email']}")
    else:
        print("Erro ao buscar usuários.")
def get_usuario(id):
    response = requests.get(f"{API_URL}/{id}")
    if response.status_code == 200:
        usuario = response.json()
        print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, E-mail: {usuario['email']}")
    else:
        print("Usuário não encontrado.")
def criar_usuario(nome, email):
    usuario = {"nome": nome, "email": email}
    response = requests.post(API_URL, json=usuario)
    if response.status_code == 201:
        print("Usuário criado com sucesso:", response.json())
    else:
        print("Erro ao criar usuário:", response.status_code, response.text)
def atualizar_usuario(id, nome=None, email=None):
    dados = {}
    if nome:
        dados['nome'] = nome
    if email:
        dados['email'] = email
        response = requests.put(f"{API_URL}/{id}", json=dados)
    if response.status_code == 201:
        print("Usuário atualizado:", response.json())
    else:
        print("Erro ao atualizar usuário:", response.status_code, response.text)
        
def deletar_usuario(id):
    response = requests.delete(f"{API_URL}/{id}")
    if response.status_code == 200:
        print("Usuário excluído.")
    else:
        print("Erro ao excluir usuário:", response.status_code, response.text)
        

if __name__ == "__main__":
# Exemplo de uso:
    print("--- 1) LISTANDO USUÁRIOS ---")
    get_usuarios()
    
    print()
    
    print("--- CRIANDO USUÁRIOS ---")
    criar_usuario('Pedro', 'pedro@email.com')
    criar_usuario('Maria', 'maria@email.com')
    criar_usuario('Juca', 'juca@email.com')
    
    print()
    
    print("--- 2) LISTANDO USUÁRIOS ---")
    get_usuarios()
    
    print()
    
    print("--- ATUALIZANDO O USUÁRIO COM O ID = 2")
    atualizar_usuario(2, nome="Maria da Silva")
    
    print()
    
    print("--- 3) LISTANDO USUÁRIOS ---")
    get_usuarios()
    
    print()
    
    print('--- BUSCANDO O USUÁRIO COM O ID = 2 ---')
    get_usuario(2)
    
    print()
    
    print('--- EXCLUINDO O USUÁRIO COM ID = 3')
    deletar_usuario(3)
    
    print()
    
    print("--- 4) LISTANDO USUÁRIOS ---")
    get_usuarios()