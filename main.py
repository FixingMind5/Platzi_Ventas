clients = 'Pablo, Ricardo'

def _print_welcome():
    print(('*' * 17) + ('WELCOME PLATZERS') + ('*' * 17))
    print('*' * 50)
    print('What do u wanna do?')
    print('[C]reate client')
    print('[D]elete cilent')


def _add_coma():
    global clients
    clients += ', '


def list_clients():
    global clients
    print(clients)


def add_cliente(nombre_Cliente):
    global clients
    if nombre_Cliente not in clients:
        _add_coma()
        clients += nombre_Cliente
    else:
        print(nombre_Cliente + ' already exists')


if __name__ == '__main__':
    _print_welcome()
    command = input()
    str(command)

    if command == 'C':
        print('Nuevo cliente:')
        nombre_Cliente = input()
        str(nombre_Cliente)
        add_cliente(nombre_Cliente)
        list_clients()
    elif command == 'D':
        pass
    else:
        print('Invalid command, type -h for help')
