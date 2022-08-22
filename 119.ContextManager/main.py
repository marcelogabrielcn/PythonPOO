arquivo = open('aqruivo1', 'w')
arquivo.write('Teste de escrita')
arquivo.close()

# Existe um modo mais fácil de abrir e fechar arquivos, para garantir o processo

with open('arquivo2', 'w') as texto:
    texto.write('Teste de escrita2')

