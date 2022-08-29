from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()
cliente1 = Cliente('Marcelo', 23)
cliente2 = Cliente('Lucas', 25)
cliente3 = Cliente('Felipe', 21)

conta1 = ContaPoupanca(1030, 928948, 0)
conta2 = ContaCorrente(1010, 267298, 1000)
conta3 = ContaPoupanca(1010, 834754, 23542)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_clintes(cliente2)
banco.inserir_conta(conta2)

if banco.autenticar(cliente2):
    cliente1.conta.depositar(2000)
    cliente1.conta.sacar(200)
else:
    print('Cliente não autenticado.')
