entrada = input('digite uma string: ')
numero_rep = input('digite a quantidade de vezes que as vogais vão se repetir: ')

for letra in entrada:
  if letra.lower() in 'aeiou':
    print(letra * numero_rep) 

  else:
    print(letra)