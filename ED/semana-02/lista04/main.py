from calculadora import Calculadora

print(f"+--------------+\n|         ")
ope = str(input("Operação: "))
val = float(input("Valor: "))
calc = Calculadora(ope, val)

print(f"\nOperação ==> {calc.operacao} e Valor ==> {calc.valor}\n")

while True:
    continuar = str(input("Deseja continuar (S/N) ")).upper()

    print("========================")

    if continuar == "S":
        calc.operacao = str(input("\nOperação: "))
        calc.valor = float(input("Valor: "))

        print(f"\noperação ==> {calc.operacao} e valor ==> {calc.valor}\n")

    elif continuar == "N":
        break
