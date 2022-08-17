from classes import *

c1 = Cliente('João', 39)
print(c1.nome)
c1.comprar()
#c1.estudar() Vai dar erro pois não pode usar essa função

a1 = Aluno('Gabriel', 23)
print(f'{a1.nome} tem {a1.idade} anos.')
a1.estudar()
a1.falar()
