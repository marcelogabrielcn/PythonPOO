class A:
    def __new__(cls, *args, **kwargs):
        print('Eu sou o New.')
        return super().__new__(cls)

    def __init__(self):
        print('Eu sou o init.')


a1 = A()
