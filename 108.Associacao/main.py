from Classes import Escritor, Caneta, Computador

escritor1 = Escritor('Fernando')
caneta1 = Caneta('Faber Castel')
pc1 = Computador()
escritor1.ferramenta = pc1
escritor1.ferramenta.escrever()

print(escritor1.nome)
print(caneta1.marca)
pc1.escrever()
