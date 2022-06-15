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