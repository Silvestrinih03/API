python_version = "3.11.3"

# Iniciando banco de dados
from flask import Flask, Request, Response
    # Response - definir o tipo de resposta
from database.db import initialize_bd
from database.models import livros

API = Flask(__name__)

# Definir config do banco de dados
# API.config['MONGODB_SETTINGS'] = {'host': 'mongodb://localhost/API_Nicole'}
# Iniciar banco de dados
initialize_bd(API)

# Consultar biblioteca
@API.route('/livros', methods = ['GET'])
def obter_livros():
    tds_livros = livros.objects().to_json()
    return Response(tds_livros, mimetype="application/json", status=200)

# Incluir novo livro
@API.route('/adicionarlivro', methods = ['POST'])
def adicionar_livro():
    body = Request.get_json()
    tds_livros = livros(**body).save()
    id = tds_livros.id
    return {'id': str(id)}, 200

'''# Consultar por ID
@API.route('/livro/<int:id>', methods = ['GET'])
def obter_livro_id(id):
    for i in livros:
        if i.get('id') == id:
            return jsonify(i)'''
        
# Editar livro
@API.route('/editarlivro/<int:id>', methods = ['PUT'])
def editar_livro_id(id):
    body = Request.get_json()
    livros.objects.get(id=id).update(**body)
    return '', 200

# Excluir livro
@API.route('/apagarlivro/<int:id>', methods = ['DELETE'])
def apagar_livro_id(id):
    livros.objects.get(id=id).delete()
    return '', 200

API.run()