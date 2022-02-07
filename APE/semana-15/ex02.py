"""
Faça um programa que leia uma frase e a exiba criptografada. O método de
criptografia será baseado na seguinte regra: trocar alguns caracteres por outros,
conforme a tabela abaixo:

CARACTER ORIGINAL    CARACTER CRIPTOGRAFADO

    A                   branco
    E                   U
    I                   O
    O                   I
    U                   E
    branco              A

Exemplo: "BOA NOITE" criptografado fica "BI ANIOTU"
"""
frase = str(input("Frase:\n")).upper()
frase_cripto = str()
for c in frase:
    if c == "A":
        frase_cripto += " "
    elif c == "E":
        frase_cripto += "U"
    elif c == "I":
        frase_cripto += "O"
    elif c == "O":
        frase_cripto += "I"
    elif c == "U":
        frase_cripto += "E"
    elif c == " ":
        frase_cripto += "A"
    else:
        frase_cripto += c

print(f"\nFrase criptografada:\n{frase_cripto}")
