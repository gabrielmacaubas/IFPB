entrada = input("Digite um caractere qualquer do teclado: ")
caractere = entrada.lower()
caractere_tipo = str()

if "a" <= caractere <= "z":
    if caractere == "a" or caractere == "e" or caractere == "i" or caractere == "o" or caractere == "u":
        caractere_tipo = "vogal"

    else:
        caractere_tipo = "consoante"

elif "0" <= caractere <= "9":
    caractere_tipo = "numero"

else:
    caractere_tipo = "caractere especial"

print(caractere_tipo)
