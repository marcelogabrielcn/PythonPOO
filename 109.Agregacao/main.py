from Classes import CarrinhoDeCompras, Produtos

carrinho = CarrinhoDeCompras()
print(carrinho)

p1 = Produtos('Lenço Desbravador', 20)
p2 = Produtos('iPhone 12', 4500)
p3 = Produtos('Fone de ouvido', 100)

carrinho.lista_produtos()
carrinho.inserir_produto(p1)
carrinho.lista_produtos()
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.lista_produtos()

print(carrinho.soma_total())
