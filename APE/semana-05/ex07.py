weight = float(input("Peso: "))
height = float(input("Altura: "))
BMI = weight / (height**2)
obesity = str()

if BMI < 26:
    obesity = "Normal"
else:
    if BMI < 30:
        obesity = "Obesidade"
    else:
        obesity = "Obeso Mórbido"

print(BMI)
print(obesity)
