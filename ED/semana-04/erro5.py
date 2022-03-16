
def dividir(a, b):
    if b == 0:
        raise Exception("impossivel dividir")
    return a/b


def fproblema(var):
    raise ZeroDivisionError


try:
    fproblema(4)
except ArithmeticError:
    print('Erro na divisão')


print('Fim do Programa')