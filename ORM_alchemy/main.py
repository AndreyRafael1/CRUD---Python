from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

#Criando uma conexão com o banco de dados SQLite
#db é o nome da variável que representa a conexão com o banco de dados
db = create_engine('sqlite:///teste.db')

#criando uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=db)
session = Session() #conferir letra maiuscula e minuscula


base = declarative_base()  #base para criar as classes que representam as tabelas do banco de dados

#as tabelas do banco de dados serão representadas por classes que herdam de 'base'
class Usuario(base):
    #referecia o nome da tabela no banco de dados
    __tablename__ = 'usuarios'


    #a coluna é definida pelo nome da coluna e o tipo de dado
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    senha = Column(Integer)

    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha




class Livro(base):
    __tablename__ = 'livros'


    id = Column(Integer,primary_key=True, autoincrement=True)
    titulo = Column(String)
    #chave estrangeira referenciando a tabela usuario
    dono = Column(ForeignKey('usuarios.id'))

    def __init__(self, titulo, dono):
        self.titulo = titulo
        self.dono = dono


base.metadata.create_all(db)  #criando as tabelas no banco de dados