bits = int(input("Bits: "))
nota_50 = bits // 50
nota_10 = (bits % 50) // 10
nota_5 = (bits % 10) // 5
nota_1 = (bits % 5) // 1

print(f"- {nota_50} nota de B$ 50")
print(f"- {nota_10} notas de B$ 10")
print(f"- {nota_5} notas de B$ 5")
print(f"- {nota_1} notas de B$ 1")
