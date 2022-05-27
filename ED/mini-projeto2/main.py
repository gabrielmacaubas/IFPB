from BinaryTree import BinaryTree


arvores = {}

# CARGA INICIAL

with open("db.txt", 'r', encoding='utf-8') as arquivo:
    
    db = arquivo.readlines()
    
    for line in db:
        url = line.strip("\n").rsplit('/')
        domain = url[0]
        
        if domain not in arvores:

            arvores[domain] = BinaryTree(line.strip("\n"))

        else:
            target = url[-2]
            new_data = url[-1]

            if arvores[domain].getNode(target).hasLeftChild():
                arvores[domain].addRight(target, new_data)
                
            else:
                arvores[domain].addLeft(target, new_data)

while True:
    tokens = input(">>>").lower().split()
    command = tokens[0]

    if command == "sair":
        break

    url = tokens[1]
    line = url.rsplit('/')
    domain = line[0]

    if command == "add":
        if domain not in arvores:
            arvores[domain] = BinaryTree(url)
        
        else:
            target = line[-2]
            new_data = line[-1]
            

            if arvores[domain].getNode(target).hasLeftChild():
                arvores[domain].addRight(target, new_data)
                
            else:
                arvores[domain].addLeft(target, new_data)
            """
            else:
                for i in range(len(line)-1):
                    sub_root = line[i+1]
                    a = arvores[domain].getNode(sub_root)
            """

    elif command == "viewtree":
        arvores[domain].viewtree()
    
    elif command == "match":
        if domain not in arvores:
            print(f"{domain} não é um endereço na árvore.")
            
        else: 

            match = arvores[domain].match(line)
            print(match)
            if match:
                print("\033[32m200 OK - Requisição bem-sucedida!\033[m")
            else:
                print("\033[31m400 Bad Request - Servidor não atendeu a requisição.\033[m")
    
print("\n---Encerramento do programa---")    
"""
        www.ifpb.edu.br                 url = [www.ifpb.edu.br, rc, p1, ed] 
    tsi                     rc

p1          p2           p1
        SO             ed
    proj1   proj2
"""
