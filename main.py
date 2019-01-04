clients = 'Pablo, Ricardo'

def _print_welcome():
    print('BIENVENIDOS VISITANTES')
    print('*' * 50)

def _add_coma():
    global clients
    clients += ', '


def list_clients():
    global clients
    print(clients)


def add_cliente(nombre_Cliente):
    global clients
    _add_coma()
    clients += nombre_Cliente


if __name__ == '__main__':
    _print_welcome()
    list_clients()
    add_cliente('Manolo')
    list_clients()
    add_cliente('Antonio')
    list_clients()
