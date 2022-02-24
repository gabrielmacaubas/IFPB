from calculadora import Calculadora

calc = Calculadora()
continuar = "S"

while True:
    print(f"""+{'-'*14}+
|{calc.registrador[1]:>14.2f}|
+{'-'*14}+
(+) somar
(-) subtrair
(/) dividir
(*) multiplicar
(r) resetar
(d) desfazer
{'-'*15}""")

    calc.operacao = str(input("Operação: ")).lower()

    if calc.operacao != "r" and calc.operacao != "d":
        calc.valor = float(input("Valor: "))
        calc.calcular()

    else:
        calc.calcular()

    print(f"""+{'-' * 14}+
|{calc.registrador[1]:>14.2f}|
+{'-' * 14}+""")

    continuar = str(input("\nDeseja continuar (S/N) ")).upper()

    print(f"{'='*30}\n")

    if continuar != "S":

        break

print("Calculadora encerrada!")
