name = str(input("nome: "))
sex = str(input("sexo: "))

if sex == "masculino":
    print(f"Olá, Sr. {name}")
elif sex == "feminino":
    print(f"Olá, Sra. {name}")
else:
    pronoum = str(input("Como você gostaria de ser chamado(a), senhor ou senhora?"))
    if pronoum == "senhor":
        print(f"Olá, Sr. {name}")
    else:
        print(f"Olá, Sra. {name}")
