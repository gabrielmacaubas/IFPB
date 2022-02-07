"""
Faça um programa que leia os seguintes dados de um conjunto de alunos:
matrícula, nome e as duas notas que ele obteve em suas avaliações. A
condição de parada será a digitação de uma matrícula igual 0 (zero). O
programa deverá mostrar, para cada aluno, as seguintes informações:
matrícula, nome, média e situação (aprovado, se a média for igual ou superior
a 7 e, reprovado, se a média for inferior a 7).
"""
print("Informe os dados dos alunos. Para encerrar, digite a matrícula 0.")

flag = 0
matricula = int(input("Matrícula: "))

while matricula != flag:
    nome = str(input("Nome: "))
    nota_1 = int(input("1ª Nota: "))
    nota_2 = int(input("2ª Nota: "))
    media = (nota_1 + nota_2) / 2

    print(f"\nMatrícula: {matricula}\nNome: {nome}\nMédia: {(nota_1 + nota_2) / 2}")

    if media >= 7:
        print("Situação: Aprovado")

    else:
        print("Situação: Reprovado")

    matricula = int(input("\nMatrícula: "))

print("Fim do Programa.")
