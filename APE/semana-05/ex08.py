"""
Escreva um programa que tenha a funcionalidade de uma calculadora simples. O programa deve
solicitar a digitação de dois operandos e um operador (+ - x * / %) e deve imprimir ao resultado
da operação aritmética. Caso o usuário digite um operador inválido, o programa deve imprimir
"Operador desconhecido".
"""

operando_1 = int(input("Operando 1: "))
operando_2 = int(input("Operando 2: "))
operador = str(input("Operador: "))

if operador == "+":
    resultado = operando_1 + operando_2
elif operador == "-":
    resultado = operando_1 - operando_2
elif operador == "x":
    resultado = operando_1 * operando_2
elif operador == "/":
    resultado = operando_1 / operando_2
elif operador == "%":
    resultado = operando_1 % operando_2

print(resultado)