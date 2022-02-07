entrada = input("Digite um caractere qualquer do teclado: ")
caractere = entrada.lower()
caractere_tipo = str()

if caractere >= "a" and caractere <= "z":
    if caractere == "a" or caractere == "e" or caractere == "i" or caractere == "o" or caractere == "u":
        caractere_tipo = "vogal"

    else:
        caractere_tipo = "consoante"

else:
    if caractere >= "0" and caractere <= "9":
        caractere_tipo = "numero"

    else:
        caractere_tipo = "caractere especial"

print(caractere_tipo)