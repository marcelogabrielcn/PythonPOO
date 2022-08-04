class BaseDeDados:
    def __init__(self):
        self.dados = {}
        self.__arquivos = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def apagar_clientes(self, id):
        del self.dados['clientes'][id]

    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

    def inserir_arquivos(self, id, nome):
        if 'arquivos' not in self.__arquivos:
            self.__arquivos['arquivos'] = {id: nome}
        else:
            self.__arquivos['arquivos'].update({id: nome})


bd = BaseDeDados()
bd2 = BaseDeDados()

bd2.inserir_arquivos(1, 'fotos')
bd2.__arquivos = 'alterar'

print(bd2.__arquivos)
print(bd2._BaseDeDados__arquivos)


bd.inserir_cliente(1, 'Marcelo')
bd.inserir_cliente(2, 'Gabriel')
bd.inserir_cliente(3, 'Ferreira')
bd.apagar_clientes(3)
bd.lista_clientes()
