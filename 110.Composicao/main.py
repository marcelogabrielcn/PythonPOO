from classes import Cliente

cliente1 = Cliente('Gabriel', 23)
cliente1.inserir_endereco('São Paulo', 'SP')
print(cliente1.nome)
cliente1.lista_enderecos()
print()

cliente2 = Cliente('Luis', 28)
cliente2.inserir_endereco('Salvador', 'BA')
cliente2.inserir_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('Lais', 39)
cliente3.inserir_endereco('Belo Horizonte', 'MG')
print(cliente3.nome)
cliente3.lista_enderecos()
print()
