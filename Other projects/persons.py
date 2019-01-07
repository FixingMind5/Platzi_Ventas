class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print("Hello World, jajaja fuck yeah... Oh sí, {} {}".format(
        self.name, self.age
        ))


if __name__ == '__main__':
    person = Person('Manuel', 18)

    print('Age: {}'.format(person.age))
    person.sayHello()
