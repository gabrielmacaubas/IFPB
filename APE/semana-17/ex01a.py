"""
Escreva uma função chamada vogal que receba uma letra e verifique se a letra é
uma vogal, retornando o valor True nesse caso, ou o valor False caso contrário.
"""
from ex01function import vogal

l = str(input("Letra: "))

if vogal(l, 0):
    print(f"Vogal = {vogal(l, 0)}")

else:
    print(f"Vogal = {vogal(l, 0)}")
