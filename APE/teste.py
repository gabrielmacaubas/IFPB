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

# código calouro v1

tamanho = str(input('Digite o total de testes: '))
coelhos = 0
ratos = 0
sapos = 0
contcoelhos = 0
contratos = 0
contsapos = 0
animais = 0
for i in range (len(tamanho)):
  animais = str(input('Digite quantos animais e a letra inicial do animal (ex: 10 r): '))
  if [i-1] == 'c':
    contcoelhos += int(1)
    animais += int(1)
  if [i-1] == 's':
    contsapos += int(1)
    animais += int(1)
  if [i-1] == 'r':
    contratos += int(1)
    animais += int(1)

portcoelhos = animais / contcoelhos * 100
porcratos = animais / contratos * 100
porcsapos = animais / contsapos * 100

print(f'porcentagem de coelhos: {protcoelhos:.2f}')
print(f'porcentagem de ratos: {protratos:.2f}')
print(f'porcentagem de sapos: {protsapos:.2f}')
print(f'Total de animais: {animais}')

# código calouro v2

tamanho = int(input('Digite o total de testes: '))
contcoelhos = 0
contratos = 0
contsapos = 0
animais = 0
for i in range (tamanho):
  animais = str(input('Digite quantos animais e a letra inicial do animal (ex: 10 r): '))
  if [i-1] == 'c':
    contcoelhos += 1
    animais += 1
  if [i-1] == 's':
    contsapos += 1
    animais += 1
  if [i-1] == 'r':
    contratos += 1
    animais += 1
print(contratos)
print(contcoelhos)
print(contsapos)
print(animais)

porccoelhos = animais / contcoelhos * 100
porcratos = animais / contratos * 100
porcsapos = animais / contsapos * 100

print(f'porcentagem de coelhos: {porccoelhos:.2f}')
print(f'porcentagem de ratos: {porcratos:.2f}')
print(f'porcentagem de sapos: {porcsapos:.2f}')
print(f'Total de animais: {animais}')

# meu código

# duvida calouro

"""
Minha dúvida é se tem como uma mesma variável receber números e letras e como eu faria para separar e calcular depois
"""

# resposta da duvida

"""
"""
