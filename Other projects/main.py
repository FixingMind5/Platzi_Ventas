import sys
import csv
import os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'e-mail', 'position']
clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)


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
        if client['name'] != nombre_Cliente:
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
    _initialize_clients_from_storage()

    _print_welcome()
    command = input()

    if command == 'c':
        client = setData()
        add_cliente(client)
    elif command == 'l':
        list_clients()
    elif command == 'u':
        print('\n')
        client = setData()
        idClient = int(input("Client's id is: "))
        updateClient(idClient, client)
    elif command == 'd':
        idxClient = int(input("Set the index client: "))
        deleteClient(idxClient)
    elif command == 's':
        nombre_Cliente = input("What name do you wanna search? ")
        finder = searchClient(nombre_Cliente)

        if finder:
            print(" {} is in client's list".format(nombre_Cliente))
        else:
            print(" {} isn't in the client list, sorry :(".format(nombre_Cliente))


    else:
        print('Invalid command, type -h for help')

    _save_clients_to_storage()
