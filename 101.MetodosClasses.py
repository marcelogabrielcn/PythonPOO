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


p2 = Pessoa.por_ano_nascimento('Marcelo', 1999)
print(p2)
print(p2.nome, p2.idade)
p2.get_ano_nascimento()

# p1 = Pessoa('Gabriel', 23)
# p1.get_ano_nascimento()
