List_users = []

def Addition ():
    name = str(input('Digite o nome do usuario: '))
    password = int(input('digite a senha do usuario: '))
    user = {
        'Username' : name,
        'Password' : password
    }
    List_users.append(user)

def Remove():
    for i, user in enumerate(List_users):
        print(f'indice:[{i}]:{user["name"]}')
    try: 
        esc = int(input('Escolha o indice a ser removido:'))
        List_users.pop(esc)
    except IndexError:
        print('Digite um indice existente')

def Update():
    for i, user in enumerate(List_users):
            print(f'indice:[{i}]:{user["name"]}')
        

    try:

        idx = int(input('digite o usuario que deseja alterar: '))

        print(f'{List_users[idx]["name"]} : {List_users[idx]["password"]}')
        alt = int(input('oque deseja alterar: 1- nome | 2- senha: '))
        if alt == 1:
            new_User = str(input('digite o novo usuario: '))
            user[idx]['Username']  = new_User

            print('usuario alterado com sucesso')
        elif alt == 2:
            new_Password = int(input('digite a nova senha: '))
            user[idx]['Password'] = new_Password

            print('senha alterada com sucesso')
        else:
            print('escolha uma opção existente')

    except ValueError:
        print('Digite apenas números válidos.')

def Read():
    try:
        for i in range(len(List_users)):
            print(List_users[i])
    except IndexError:
        print('Lista vazia')


while True:    
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
        Addition()

    elif esc == 2:
        Remove()

    elif esc == 3:
        Read()

    elif esc == 4:
        Update()