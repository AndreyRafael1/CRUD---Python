import dataBase

def Read_User():
    print('Deseja listar todos os usuarios cadastrados?')
    esc = input('Digite 1 para sim ou 0 para não: ')

    if esc == '1':
        #busca geral no banco de dados
        User_list = dataBase.session.query(dataBase.usuario).all()
        for user in User_list:
            print(f'Nome: {user.name} | Senha: {user.password}')

    elif esc == '0':
        #busca especifica no banco de dados
        User_name = input('Digite o nome do usuario que deseja buscar: ')
        User_list = dataBase.session.query(dataBase.usuario).filter_by(name=User_name).all()
        print(f'Nome: {User_list[0].name} | Senha: {User_list[0].password}')

    else:
        print('Opção invalida!')
        exit()