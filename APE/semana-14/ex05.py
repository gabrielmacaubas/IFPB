"""
Faça um programa que leia uma frase e a exiba com uma letra em cada linha.
"""
frase = str(input("Frase: "))
frase = frase.replace(" ", "")
for l in range(len(frase)):
    print(frase[l])
