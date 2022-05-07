ingresso_m = 50
ingresso_f = 20
qtd_m = int()
qtd_f = int()

while True:
    nome = input("Nome: ")

    if nome.upper() == "FIM":
        break

    sexo = input("Sexo (M/F): ").upper()

    if sexo == "M":
        qtd_m += 1

    else:
        qtd_f += 1

total_pessoas = qtd_m + qtd_f
porcentagem_m = (qtd_m / total_pessoas) * 100
porcentagem_f = (qtd_f / total_pessoas) * 100
total_arrecadado = (qtd_m * ingresso_m) + (qtd_f * ingresso_f)

print(f"\nPorcentagem de homens: {porcentagem_m:.1f}%")
print(f"Porcentagem de mulheres: {porcentagem_f:.1f}%")
print(f"Total arrecadado: R${total_arrecadado:.2f}")
