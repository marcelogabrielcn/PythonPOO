class Arquivo:

    def __init__(self, arquivo, modo):
        print('Abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('return arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando arquivo')
        self.arquivo.close()


with Arquivo('Teste1', 'w') as arquivo:
    arquivo.write('Alguma coisa qualquer...')
