# Regras banco de dados
from db import db
class livros(db.Document):
    id = db.int(required=True, unique=True)
    titulo = db.str(required=True)
    autor = db.str(required=True)