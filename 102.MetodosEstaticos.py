from random import randint


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(0, 500)
        return rand


p1 = Pessoa('Gabriel', 23)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

print(Pessoa.gera_id())
print(p1.gera_id())
p2 = Pessoa('João', 28)
print(p2.nome, p2.idade)
