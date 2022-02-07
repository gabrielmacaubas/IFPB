def vogal(letra, frase):
    vogais = "aâàáãeéiíoõôóuú"
    if frase == 0:
        if letra.lower() in vogais:
            return True

        else:
            return False

    else:
        cont = 0
        for l in frase:
            if l.lower() in vogais:
                cont += 1

        return cont
