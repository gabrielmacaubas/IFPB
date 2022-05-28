from BinaryTree import BinaryTree
import pathlib

path = pathlib.Path(__file__).parent.resolve()
arvores = {}

def add(url):
    domain = url[0]

    if domain not in arvores:
        arvores[domain] = BinaryTree(url[0])

    else:
        target = url[:-1]
        new_data = url[-1]
        current_node = arvores[domain].match(target)

        if current_node:
            
            if current_node.hasLeftChild():
                arvores[domain].addRight(current_node, new_data)
            else:
                arvores[domain].addLeft(current_node, new_data)


# CARGA INICIAL

with open(str(path)+'/db.txt', 'r', encoding='utf-8') as arquivo: 
    db = arquivo.readlines()
    
    for line in db:
        url = line.strip("\n").rsplit('/')
        add(url)

while True:
    tokens = input("\n>>>").lower().split()
    print()
    command = tokens[0]

    if command == "sair":
        break

    url = tokens[1].rsplit('/')
    domain = url[0]

    if command == "add":
        add(url)

    elif command == "viewtree":
        arvores[domain].viewtree()
    
    elif command == "match":
        if domain not in arvores:
            print(f"{domain} não é um endereço na árvore.")
            
        else: 
            match = arvores[domain].match(url)

            if match:
                print("\033[32m200 OK - Requisição bem-sucedida!\033[m")
            else:
                print("\033[31m400 Bad Request - Servidor não atendeu a requisição.\033[m")
    
print("\n---Encerramento do programa---")    
"""
        www.ifpb.edu.br          url = [www.ifpb.edu.br, tsi] 
    tsi                     rc

p1          p2           p1
        SO             ed
    proj1   proj2
"""
