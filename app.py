from flask import Flask, request
from src import AlunoRepository


app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return "Olá mundo!!"

@app.route("/insert", methods=["POST"])
def insert():
    print("Chamada")
    aluno_repository = AlunoRepository()
    body = request.json
    print("Por enquanto tudo certo")
    aluno_repository.insert_aluno(body["name"])
    return 'OK'
