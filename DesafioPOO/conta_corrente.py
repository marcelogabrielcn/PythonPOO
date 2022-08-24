from DesafioPOO.conta import Conta


class ContaCorrente(Conta):
    def sacar(self, valor):
        if (self.saldo + 200) < valor:
            print('Saldo insuficiente. Foi utilizado limite extra')
            self.saldo -= valor
        if (self.saldo + 200) < valor:
            print('Mesmo com o limite extra o saldo está insuficiente.')
            return

        self.saldo -= valor
