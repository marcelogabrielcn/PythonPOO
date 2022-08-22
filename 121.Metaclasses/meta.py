"""
Tudo em python é uma metaclass, inclusive classes
Metaclasses são classes que criam outras classes
type é uma metaclasse
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            print(f'Olá, você precisar criar o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisar ser um método, não atribuido em {name}')

        return type.__new__(mcs, name, bases, namespace)

class A(metaclass=Meta)
    def fala(self):
        self.b_fala()

class B(A):
    pass