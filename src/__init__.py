from .config import DBConnection
from .entities import Alunos as AlunosModel


class AlunoRepository:

    def insert_aluno(self, name):
        with DBConnection() as db:
            new_aluno = AlunosModel(name=name)
            db.session.add(new_aluno)
            db.session.commit()
