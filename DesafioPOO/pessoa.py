class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self.nome

    @property
    def idade(self):
        return self.idade

    @nome.setter
    def nome(self, value):
        self._nome = value

    @idade.setter
    def idade(self, value):
        self._idade = value
