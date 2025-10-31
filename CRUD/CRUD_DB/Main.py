import dataBase, Create, Uptade, Remove, Read

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
        Create.Create_User()

    elif esc == 2:
        Remove.Delete_User()

    elif esc == 3:
        Read.Read_User()

    elif esc == 4:
        Uptade.Uptade_User()