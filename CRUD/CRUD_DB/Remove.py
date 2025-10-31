import dataBase

def Delete_User():
    User_name = str(input('Digite o nome do usuario que deseja remover: '))
    User_name = dataBase.session.query(dataBase.usuario).filter_by(name=User_name).first()

    dataBase.session.delete(User_name)
    dataBase.session.commit()

    print('Usuario removido com sucesso!')