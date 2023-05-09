'''API >> Lugar para disponibilizar recursos e ou funcionalidades

 Etapas
01 - Objetivo >> criar API que disponibiliza consulta, criação, edição e exclusão de livros 
02 - URL base >> localhost
03 - Endpoint
    - localhost/livros (get) >> consultar biblioteca
    - localhost/adicionarlivro (post) >> criar novos livros
    - localhost/livro/id (get) >> consultar livro específico
    - localhost/editarlivro/id (put) >> modificação de livros
    - localhost/apagarlivro/id (delete) >> deletar livros
04 - Quais recursos - Livros'''

from flask import Flask, jsonify, request
# flask - servidor
# jsonify - retornar no formato Json
# request - permite acessar os dados

API = Flask(__name__)

livros = [
    {
        "id": 1,
        "titulo": "O Senhor dos Anéis",
        "autor": "J.R.R Tolkien"
    },
    {
        "id": 2,
        "titulo": "Harry Potter",
        "autor": "J.K Howling"
    },
    {
        "id": 3,
        "titulo": "Hábitos Atômicos",
        "autor": "James Clear"
    }
]

# Consultar biblioteca
@API.route('/livros', methods = ['GET'])
def obter_livros():
    return jsonify(livros)

# Incluir novo livro
@API.route('/adicionarlivro', methods = ['POST'])
def incluir_livro():
    # Retornar informação enviada pelo usuário
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# Consultar por ID
@API.route('/livro/<int:id>', methods = ['GET'])
def obter_livro_id(id):
    for i in livros:
        if i.get('id') == id:
            return jsonify(i)
        
# Editar livro
@API.route('/editarlivro/<int:id>', methods = ['PUT'])
def editar_livro_id(id):
    # Retornar informação enviada pelo usuário
    edicao = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(edicao)
            return jsonify(livros[indice])

# Excluir livro
@API.route('/apagarlivro/<int:id>', methods = ['DELETE'])
def apagar_livro_id(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

API.run(port = 5000, host='localhost', debug=True)