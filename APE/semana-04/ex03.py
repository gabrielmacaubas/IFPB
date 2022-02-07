variable_1 = int(input("Variável inteira: "))
variable_2 = int(input("Variável inteira: "))
variable_1_copy = variable_1
variable_1 = variable_2
variable_2 = variable_1_copy

print(variable_1, variable_2)
