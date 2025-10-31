from sqlalchemy import create_engine, Column, Integer, String, delete
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine('sqlite:///dataBase.db')
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class usuario(Base):    
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    password = Column(Integer)

    def __init__(self, name, password):
        self.name = name
        self.password = password

Base.metadata.create_all(db)