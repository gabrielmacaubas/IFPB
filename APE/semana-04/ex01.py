name = str(input("Nome: "))
sold_cars = int(input("Carros vendidos: "))
sale_value = float(input("Valor total das vendas: "))
emp_salary = (200 * sold_cars) + 1000 + ((5 / 100) * sale_value)

print(name, emp_salary)
