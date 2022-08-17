class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def falar(self):
        print(f'{self.nome} está falando...')
        # Todas as classes filhas podem usa essa função.

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} está comprando...')
    # Somente está classe pode usar essa função


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} vai começar estudar...')
        # Somente está classe pode usar essa função