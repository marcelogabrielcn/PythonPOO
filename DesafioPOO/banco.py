class Banco:
    def __init__(self):
        self.agencias = [1010, 1020, 1030, 1040]
        self.clientes = []
        self.contas = []

    def inserir_clintes(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return None

        if cliente.conta not in self.contas:
            return None

        if cliente.conta.agencia not in self.agencias:
            return None

        return True
