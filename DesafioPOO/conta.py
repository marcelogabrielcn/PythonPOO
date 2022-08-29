from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do depósito precisa ser numérico.')

        self.saldo += valor

    def detalhes(self):
        print(f'Agência: {self.agencia}'
              f'Conta: {self.conta}'
              f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente. Foi utilizado limite extra')
            self.saldo -= valor
        if (self.saldo + self.limite) < valor:
            print('Mesmo com o limite extra o saldo está insuficiente.')
            return

        self.saldo -= valor


class ContaPoupanca(Conta):

    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()
