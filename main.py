clients = 'Pablo, Ricardo'

def _add_coma():
    global clients
    clients += ', '

def add_cliente(nombre_Cliente):
    global clients
    _add_coma()
    clients += nombre_Cliente

if __name__ == '__main__': 
    print(clients)
    add_cliente('Manolo')
    print(clients)
    add_cliente('Antonio')
    print(clients)
