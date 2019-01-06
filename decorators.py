PASSWORD = '12345'


def passRequired(func):
    def wrapper():
        password = input('Password is: ')

        if password == PASSWORD:
            return func()
        else:
            print("la contraseña es incorrecta.")

    return wrapper

def capName(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.capitalize()

    return wrapper

"""Para decir a qué función vas a llamar.
Arriba, la función que la llamará.
La función de abajo es func()"""
@passRequired
def needsPass():
    print("La contraseña es correcta")

@capName
def sayName(name):
    return "hola {}".format(name)


if __name__ == '__main__':
    print(sayName("manolo"))
