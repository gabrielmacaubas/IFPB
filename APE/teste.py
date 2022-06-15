# questão

"""
Maria acabou de começar como estudante de pós-graduação em uma faculdade de medicina 
e precisa da sua ajuda para organizar um experimento de laboratório pelo qual ela é responsável.
 Ela quer saber, no final do ano, quantos animais foram usados ​​nesse laboratório 
 e qual a porcentagem de cada tipo de animal que é usado.

Este laboratório utiliza em particular três tipos de animais: 
rãs, ratos e coelhos. Para obter essas informações, 
ele sabe exatamente o número de experimentos que foram realizados,
 o tipo e a quantidade de cada animal utilizado em cada experimento.

Entrada
A primeira linha de entrada contém um inteiro N indicando o número de casos de teste a seguir.
 Cada caso de teste contém um inteiro Amount (1 ≤ Amount ≤ 15)
  que representa a quantidade de animal utilizada e um caractere Type (' C ', ' R ' ou ' S '),
   indicando o tipo de animal:
- C : C oelho ( coelho em português)
- R : R ato ( rato   em português)
- S : S apo ( sapo em português)

Resultado
Imprima o total de animais utilizados, o total de cada tipo de animal
 e o percentual de cada um em relação ao total de animais utilizados.
  O percentual deve ser impresso com 2 dígitos após a vírgula.

Amostra de entrada
10
10 C
6 R
15 S 
5 C
14 R
9 C
6 R
8 S
5 C
14 R
"""

# código calouro v2
"""

"""

# meu código

#mudanças de nomes de variáveis
experimentos = int(input('Digite o total de testes: '))
cont_coelhos = 0
cont_ratos = 0
cont_sapos = 0
animais_totais = 0

for i in range (experimentos):

    # adição de while true para permitir valores apenas entre 1 e 15
    while True:
        # separar a partir de split com parâmetro vazio para dividir a informação capturada pelo usuário 
        tokens = str(input('Digite quantos animais e a letra inicial do animal (ex: 10 r): ')).upper().split()
        # quantidade de animais é o penúltimo índice   
        quantidade_animal = int(tokens[-2])
        
        if 1 <= quantidade_animal <= 15:
            # enquanto o tipo do animal é o último índice
            animal = tokens[-1]

            break
        
        print("Digite uma quantidade válida.")

    if animal == 'C':
      # a soma é feita baseado na quantidade de animais, então o  '+=' soma as quantidades, não apenas 1.
        cont_coelhos += quantidade_animal
        animais_totais += quantidade_animal
    
    # mudança de if para elif
    elif animal == 'S':
        cont_sapos += quantidade_animal
        animais_totais += quantidade_animal

    # mudança de if para elif
    elif animal == 'R':
        cont_ratos += quantidade_animal
        animais_totais += quantidade_animal
    
# cálculo da porcentagem consertado
porc_coelhos = (cont_coelhos * 100)  / animais_totais
porc_ratos = (cont_ratos * 100) / animais_totais 
porc_sapos = (cont_sapos * 100) / animais_totais

# adição da exibição da quantidade
print(f'\nQuantidade de coelhos: {cont_coelhos} \nPorcentagem: {porc_coelhos:.2f}')
print(f'Quantidade de ratos: {cont_ratos} \nPorcentagem: {porc_ratos:.2f}')
print(f'Quantidade de sapos: {cont_sapos} \nPorcentagem de sapos: {porc_sapos:.2f}')
print(f'Total de animais: {animais_totais}')

# dúvida calouro

"""
Minha dúvida é se tem como uma mesma variável receber 
números e letras e como eu faria para separar e calcular 
depois
"""

# resposta da duvida

"""
Há sim, como feito no código acima. A entrada dos dados é 
transformada numa lista, onde um índice será a quantidade 
de animais (inteiro), e o outro será o tipo do animal (str). 
A separação é feita a partir da manipulação de strings, utilizando o split. Baseia-se no índice para calcular as porcentagens e quantidades.
"""
