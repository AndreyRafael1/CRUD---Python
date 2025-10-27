UserList = []
while (True):
    print('''
    1- Adicionar usuario
    2- Remover usuario
    3- Listar usuarios
    4- Alterar usuario
    0- sair do programa
    ''')

    esc = int(input('Escolha uma das opções acima: '))
    if esc == 0:
        break

    elif esc == 1:
        name = str(input('Digite o nome do usuario: '))
        password = int(input('digite a senha do usuario: '))
        user = {
            'name' : name,
            'password' : password
        }
        UserList.append(user)

    elif esc == 2:
        for i, user in enumerate(UserList):
            print(f'indice:[{i}]:{user["name"]}')
        try: 
            esc = int(input('Escolha o indice a ser removido:'))
            UserList.pop(esc)
        except IndexError:
            print('Digite um indice existente')

    elif esc == 3:
        for i in range(len(UserList)):
            print(UserList[i])

    elif esc == 4:
        for i, user in enumerate(UserList):
            print(f'indice:[{i}]:{user["name"]}')
        

        try:

            idx = int(input('digite o usuario que deseja alterar: '))

            print(f'{UserList[idx]["name"]} : {UserList[idx]["password"]}')
            alt = int(input('oque deseja alterar: 1- nome | 2- senha: '))
            if alt == 1:
                newUser = str(input('digite o novo usuario: '))
                user[idx][name] = newUser

                print('usuario alterado com sucesso')
            elif alt == 2:
                newPassword = int(input('digite a nova senha: '))
                user[idx][password] = newPassword

                print('senha alterada com sucesso')
            else:
                print('escolha uma opção existente')

        except ValueError:
            print('Digite apenas números válidos.')
    else:
        print('escolha uma opção exitente')