"""
10) Um material radioativo denominado invictus, quando em contato com o oxigênio,
perde metade de sua massa a cada 50 segundos. Faça um função recursiva que receba
uma quantidade de massa do invictus, em gramas, e exiba o tempo (em segundos)
necessário para que sua massa se torne menor que 0,8 g. A função também deve
retornar o o valor 

11) Perde metade da massa a cada 50 s
12) exibir o tempo em segundos em que a massa fica maior que 0,8 g
"""

def invictus(massa: float)->int:
    assert massa > 0, 'A massa dele ser um valor real positivo'
    # caso base
    if massa < 0.8:
        return 0
    else:
        return 50 + invictus(massa/2)


def checkDescendente(L):
    if len(L) < 2:
        return True
    return L[0] >= L[1] and checkDescendente(L[1:])


def bolhaRecursiva(array):
    executaBolha(array,len(array))

def executaBolha(array,size):
    troca = False
    for j in range(size-1):
        if (array[j] > array[j+1] ):
            temp = array[j]
            array[j] = array[j+1] # Efetua a troca
            array[j+1] = temp
            troca = True
    if (troca):      # Houve troca
        executaBolha(array,size-1)

#main
array = [25,36,12,8,54,15,33]
bolhaRecursiva(array, len(array))
#array = sorted(array,reverse=True)
print(array)
try:
    print(checkDescendente(array))
    print(invictus(-300))
except AssertionError as ae:
    print('Erro ', ae)