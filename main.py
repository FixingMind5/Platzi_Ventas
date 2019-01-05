import sys

clients = 'Pablo, Ricardo, '

def _print_welcome():
    print(('*' * 17) + ('WELCOME PLATZERS') + ('*' * 17))
    print('*' * 50)
    print('What do u wanna do?')
    print('---|[c]reate client')
    print('---|[l]ist clients')
    print('---|[u]pdate client')
    print('---|[d]elete cilent')
    print('---|[s]earch client')

def _add_coma():
    global clients
    clients += ', '


def list_clients():
    global clients
    print(clients)


def add_cliente(nombre_Cliente):
    global clients
    if nombre_Cliente not in clients:
        clients += nombre_Cliente
        _add_coma()
    else:
        print(nombre_Cliente + ' already exists')


def updateClient(nombre_Cliente, nuevoCliente):
    global clients
    if nombre_Cliente in clients:
        clients = clients.replace(nombre_Cliente, nuevoCliente)
    else:
        print(nuevoCliente, "isn't in client database")


def deleteClient(nombre_Cliente):
    global clients
    if nombre_Cliente in clients:
        clients = clients.replace(nombre_Cliente, '')
        print('Ready!')
    else:
        print(nombre_Cliente, "didn't exists")


def searchClient(nombre_Cliente):
    global clients

    client_list = clients.split(', ')

    for client in client_list:
        if client != nombre_Cliente:
            continue
        else:
            return True


def _get_client():
    nombre_Cliente = None

    while not nombre_Cliente:
        nombre_Cliente = input("Nuevo cliente: ")

        if nombre_Cliente == 'exit':
            nombre_Cliente = None
            break

    if not nombre_Cliente:
        sys.exit()

    return nombre_Cliente


if __name__ == '__main__':
    _print_welcome()
    command = input()

    if command == 'c':
        nombre_Cliente = _get_client()
        add_cliente(nombre_Cliente)
        list_clients()
    elif command == 'l':
        list_clients()
    elif command == 'u':
        nombre_Cliente = input('Actual client name is: ')
        nuevoCliente = input("New client\'s name is: ")
        updateClient(nombre_Cliente, nuevoCliente)
        list_clients()
    elif command == 'd':
        nombre_Cliente = input("Who's the victim? ")
        deleteClient(nombre_Cliente)
        list_clients()
    elif command == 's':
        nombre_Cliente = input("What name do you wanna search? ")
        finder = searchClient(nombre_Cliente)

        if finder:
            print(" {} is in client's list".format(nombre_Cliente))
        else:
            print(" {} isn't in the client list, sorry :(".format(nombre_Cliente))


    else:
        print('Invalid command, type -h for help')
