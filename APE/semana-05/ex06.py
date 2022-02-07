name = str(input("nome: "))
concept = str(input("conceito: "))
recommendation = str()

if concept == "a":
    recommendation = "Fortemente recomendado"
elif concept == "b" or concept == "c":
    recommendation = "Recomendado"
else:
    recommendation = "Não recomendado"

print(recommendation)
