import dataBase

def Create_User():
    User_name = input('Digite o nome do usuario: ')
    User_password = int(input('Digite a senha do usuario (apenas numeros): '))

    user = dataBase.usuario(name=User_name, password=User_password)

    dataBase.session.add(user)
    dataBase.session.commit()
