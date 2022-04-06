"""
Escreva um programa que leia o nome e o sexo (M ou F) de uma pessoa e exiba a mensagem
"Olá, Sr. Fulano!" ou "Olá, Sra. Fulana!", de acordo com o sexo da pessoa. Obs: Fulano e Fulana
são nomes exemplos.
"""

name = input("nome: ")
sex = input("sexo: ").upper()

if sex == "M":
    print(f"Olá, Sr. {name}")

elif sex == "F":
    print(f"Olá, Sra. {name}")

else:
    pronoun = input("Como você gostaria de ser chamado(a), senhor ou senhora?").lower()

    if pronoun == "senhor" or pronoun == "Senhor":
        print(f"Olá, Sr. {name}")

    else:
        print(f"Olá, Sra. {name}")
