from sqlalchemy import Column, String, Integer
from src.config import Base


class Alunos(Base):
    __tablename__ = "aluno"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self) -> str:
        return f"Alunos [name={self.name}]"
