class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @nome.setter
    def nome(self, value):
        self._nome = value

    @idade.setter
    def idade(self, value):
        self._idade = value
