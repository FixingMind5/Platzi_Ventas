import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'e-mail': 'pablo@gmail.com',
        'position': 'Software engineer'
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'e-mail': 'ricardo@facebook.com',
        'position': 'Data engineer'
    }
]

def _print_welcome():
    print(('*' * 17) + ('WELCOME PLATZERS') + ('*' * 17))
    print('*' * 50)
    print('-' * 50)
    print('-' * 14, 'WHAT DO U WANNA DO?', '-' * 15)
    print('-' * 17, '[c]reate client', '-' * 16)
    print('-' * 17, '[l]ist clients', '-' * 17)
    print('-' * 17, '[u]pdate client', '-' * 16)
    print('-' * 17, '[d]elete cilent', '-' * 16)
    print('-' * 17, '[s]earch client', '-' * 16)
    print('-' * 50)


def list_clients():
    global clients
    for idx, client in enumerate(clients):
        print(" {uid} | {name} : \n {company} | {email} | {position} ".format(
        uid = idx,
        name = client['name'],
        company = client['company'],
        email = client['e-mail'],
        position = client['position']
        )
    )


def add_cliente(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print(client, "already exists")


def updateClient(idClient, client):
    global clients
    sizeOf = int(len(clients))

    for i in range(sizeOf):
        if idClient == clients.index(clients[i]):
            clients[i] = client
            print('READY!!\n')
        elif idClient not in clients:
            print(idClient, "isn't in client's database")


def deleteClient(idxClient):
    global clients

    clients.remove(clients[idxClient])
    print('Ready!')


def searchClient(nombre_Cliente):
    global clients

    for client in clients:
        if client != nombre_Cliente:
            continue
        else:
            return True


def _getField(field_name):
    field = None

    while not field:
        field = input("What's the client {}? ".format(field_name))

    return field


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


def setData():
    client = {
        'name': _getField('name'),
        'company': _getField('company'),
        'e-mail': _getField('e-mail'),
        'position': _getField('position')
    }

    return client


if __name__ == '__main__':
    _print_welcome()
    command = input()

    if command == 'c':
        client = setData()
        add_cliente(client)
        list_clients()
    elif command == 'l':
        list_clients()
    elif command == 'u':
        list_clients()
        print('\n')
        client = setData()
        idClient = int(input("Client's id is: "))
        updateClient(idClient, client)
        list_clients()
    elif command == 'd':
        list_clients()
        idxClient = input("Set the index client: ")
        int(idxClient)
        deleteClient(idxClient)
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
