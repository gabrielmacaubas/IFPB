from BinaryTree import BinaryTree


arvores = {}


with open('db.txt', 'r', encoding='utf-8') as arquivo:
    db = arquivo.readlines()
    
    for line in db:
        domain = line.strip("\n")
        if domain not in arvores:

            arvores[domain] = BinaryTree(line)

while True:
    write = input(">>>").lower().split()
    command = write[0]
    url = write[1]
    tokens = url.rsplit('/', 2)
    domain = tokens[0]

    if command == "add":
        if domain not in arvores:
            arvores[domain] = BinaryTree(command[1])
        
        else:
            target = tokens[-2]
            new_data = tokens[-1]

            if arvores[domain].getNode(target).hasLeftChild():
                arvores[domain].addRight(target, new_data)
                
            else:
                arvores[domain].addLeft(target, new_data)

    elif command == "viewtree":
        arvores[domain].preorderTraversal()

"""
        www.ifpb.edu.br

    tsi                 rc

p1      p2
            SO
        proj1   proj2
"""