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

# flask - servidor
# jsonify - retornar no formato Json
# request - permite acessar os dados
from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "O Senhor dos Anéis",
        "author": "J.R.R Tolkien"
    },
    {
        "id": 2,
        "title": "Harry Potter",
        "author": "J.K Rowling"
    },
    {
        "id": 3,
        "title": "Hábitos Atômicos",
        "author": "James Clear"
    }
]

# Retorna todos os livros
@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(books)

# Retorna um livro específico pelo ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    book = next((book for book in books if book["id"] == id), None)
    if book is not None:
        return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# Adiciona um novo livro
@app.route('/books', methods=['POST'])
def add_book():
    book = request.get_json()
    if "id" not in book:
        return jsonify({"message": "ID is required"}), 400
    books.append(book)
    return jsonify(books), 201

# Atualiza um livro existente
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next(())

@app.route('/deletebook/<int:id>', methods = ['DELETE'])
def delete_book_id(id):
    for indice, book in enumerate(books):
        if book.get('id') == id:
            del books[indice]
    return jsonify(books)

@app.run(port = 5000, host='localhost', debug=True)