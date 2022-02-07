"""
Faça um programa que leia a idade de várias pessoas visitantes de um show (a
leitura da idade 0 indicará o fim dos dados de entrada), calcule e exiba:
• A média de idade do público;
• A porcentagem de pessoas com idade entre 18 e 21 anos;
• Idade do visitante mais jovem.
"""
print("Digite a idade das pessoas visitantes do show.\nObs: para encerrar, digite a idade 0")

flag = 0
idade = int(input("Idade: "))
contador = int()
jovens = int()
idade_soma = idade
jovem = idade

while idade != flag:
    if idade < jovem:
        jovem = idade

    if 18 <= idade <= 21:
        jovens += 1

    idade = int(input("Idade: "))
    contador += 1
    idade_soma += idade


media = idade_soma / contador
porcentagem = (100 * jovens) / contador

print(f"Média de idade do público: {media:.0f}\nPorcentagem de pessoas com idade entre 18 e 21 anos: {porcentagem:.1f}%")
print(f"Idade do visitante mais jovem: {jovem} anos")
