def potencia(base:int, expoente:int)->int:
    """Calcula o resultado da base elevada ao expoente.
       Exemplo: potencia(2,3)  = 8
              potencia(10,2) = 100
    """
    resultado = 1
    for i in range(expoente):
        resultado *= base
    
    #
    #while(expoente >= 1):
    #    resultado *= base
    #    expoente -= 1

    return resultado

def potenciaRecursiva(base:int, expoente:int)->int:
    """Calcula o resultado da base elevada ao expoente, utilizando a técnica de recursividade
       Exemplo: potenciaRecursiva(2,3)  = 8
                potenciaRecursiva(10,2) = 100
        
       Passo-a-passo para construir uma solução recursiva:
       1) Identificar o padrão que permite calcular a potencia para a maioria dos casos.
          2^3: 2 * 2 * 2
          4^4: 4 * 4 * 4 * 4               <- Padrão de cálculo (desde que expoente > 0)
          3^1: 3
          5^5: 5 * 5 * 5 * 5 * 5
          10^0: qualquer número elevado a zero (expoente = 0), é 1 <- CASO BASE
       2) Determinar o CASO BASE:
          Caso Base: expoente = 0 : toda base elevada a zero é igual a 1
       3) Escreve a solução recursiva de modo que após sucessivas chamadas recursivas
          se alcance o CASO BASE
       4) Identificar as situações que não se encaixam no padrão ou
          até mesmo para validar o expoente
       Argumentos
       ===========
       base (int): 
           um número inteiro maior que zero
       expoente (int):
           um número inteiro maior que zero
    """
    # Prever a situação do caso base
    assert expoente >= 0,'Expoente não pode ser negativo'
    assert base > 0, 'Base não pode ser negativa'
    if expoente == 0:
        return 1
    else:
        mult = base * potenciaRecursiva(base, expoente-1)
        return mult



# programa principal
print(potencia(2,3))
print(potenciaRecursiva(15,30))
# teste da sua solução
# 1) testa logo o caso base
print(potenciaRecursiva(15,0))
# 2) testa o próximo caso padrão logo após o caso base
print(potenciaRecursiva(15,1))
# 3) testa o próximo caso padrão logo após o caso padrão anterior
print(potenciaRecursiva(15,2))

try:
    #print(potenciaRecursiva(15,-32))
    print(potenciaRecursiva(-15,2))
except AssertionError as ae:
    print('Erro: ',ae)
