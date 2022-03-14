try:
    f = open("aula.txt")
    try:
        conteudo = f.read()
        print(conteudo)
    except FileNotFoundError:
        pass
    else:
        print("não ocorreu erro")
    finally:
        f.close()
except FileNotFoundError:
    print("Arquivo 'aula.txt' não encontrado")

print("fim")