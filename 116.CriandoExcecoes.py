class TratativaDeError(Exception):
    pass


def testar():
    raise TratativaDeError('Errado!')


try:
    testar()
except TratativaDeError as Error:
    print(f'Erro: {Error}')
