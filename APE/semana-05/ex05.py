sales = int(input("Valor total das vendas: "))
salary = (5 / 100) * sales
minimum_salary = 1100

if salary < minimum_salary:
    salary = minimum_salary
    print(salary)
else:
    print(salary)
