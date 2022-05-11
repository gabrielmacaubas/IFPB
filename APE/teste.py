elementos = int(input("Quantidade de elementos: "))
vetor = [None] * elementos
vetorpython = []
# elementos = 5
# vetor = [None, None, None, None, None]

# maneira python adicionar
"""
print("adicionando via python")
for i in range(elementos):
    vetorpython.append(int(input(f"Digite o elemento [{i}]: ")))

print(vetorpython)
"""

# maneira python remover
"""
for i in range(elementos):
    vetorpython.pop()

print("Vetor python eliminado: ", vetorpython)
"""

# maneira programação remover
"""
for i in range(elementos):
    vetor[i] = None

print("Vetor eliminado: ", vetor)
"""

# maneira programação adicionar
for i in range(elementos):
    vetor[i] = int(input(f"Digite o elemento [{i}]: "))
    print("o índice", [i], "foi preenchido com", vetor[i])
    print(vetor)

j = elementos - 1

for i in range(elementos // 2):
    temp = vetor[i]
    vetor[i] = vetor[j]
    vetor[j] = temp
    j = j - 1

print(vetor)

# v = vetor[::-1]
