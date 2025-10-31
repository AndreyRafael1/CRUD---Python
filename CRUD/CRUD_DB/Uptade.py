import dataBase

def Uptade_User():
    #Buscar usuario
    User_name = str(input('Digite o nome do usuario que deseja alterar: '))
    User_name = dataBase.session.query(dataBase.usuario).filter_by(name=User_name).first()

    #Alterar usuario
    new_name = input('Digite o novo nome do usuario: ')
    User_name.name = new_name
    dataBase.session.add(User_name)
    dataBase.session.commit()
    
    print('Usuario alterado com sucesso!')