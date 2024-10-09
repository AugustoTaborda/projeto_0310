from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulação de Banco de Dados
usuarios = []

@app.route('/usuarios', methods=['GET', 'POST'])
def gerenciar_usuarios():
    if request.method == 'GET':
        return jsonify(usuarios), 200 
    elif request.method == 'POST':
        novo_usuario = request.get_json()
        if 'nome' not in novo_usuario or 'email' not in novo_usuario:
            return {"erro": "Nome e E-email são obrigatorio."}, 400
        
        novo_usuario['id'] = len(usuarios) + 1 
        usuarios.append(novo_usuario)
        return jsonify(novo_usuario), 201
    
@app.route('/usuarios/<int:id>', methods=['GET', 'POST', 'DELETE'])
def usuario_por_id(id):
    usuario = next((u for u in usuarios if u ['id']  == id), None)
    
    if request.method == 'GET':
        if usuario:
            return jsonify(usuario), 200
        return {"mensagem": "Usuario não encontrado"}, 404
    
    elif request.method == 'POST':
        if usuario:
            dados =request.get_json()
            if 'nome' in dados:
                usuario['nome'] = dados['nome']
            if 'email' in dados:
                usuario['email'] = dados['email']
            
            return jsonify(usuario), 200
        return {"mensagem": "Usuario não encontrado"}, 404
    
    elif request.method == 'DELETE':
        if usuario:
            pass
    
if __name__ == "__main__":
    app.run(debug=True)