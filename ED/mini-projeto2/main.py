from BinaryTree import BinaryTree


arvores = {}

# CARGA INICIAL
with open('db.txt', 'r', encoding='utf-8') as arquivo:
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

    elif command == "viewtree":
        arvores[domain].viewtree()

"""
        www.ifpb.edu.br

    tsi                 rc

p1      p2
            SO
        proj1   proj2
"""
