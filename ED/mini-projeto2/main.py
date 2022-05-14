from BinaryTree import BinaryTree


arvores = {}
#fw = open("db.txt", "w")
#fw.write("www.ifpb.edu.br")
#fw.close()


def add(data: str):
    insert(data)
    write(data)
        
def write(data):
    f = open("db.txt", "a")
    f.write("\n")
    f.write(data)
    f.close()

def insert(data: str):
    string = data.rsplit('/', 2)
    domain = string[0].split('.')
    
    if domain[1] not in arvores:
        arvores[domain[1]] = BinaryTree(data)
    
    else:
        target = string[-2]
        new_data = string[-1]

        if arvores[domain[1]].getNode(target).hasLeftChild():
            arvores[domain[1]].addRight(target, new_data)
            
        else:
            arvores[domain[1]].addLeft(target, new_data)

def viewtree(domain: str):
    
    with open('db.txt', 'r', encoding='utf-8') as arquivo:
        db = arquivo.readlines()

        for line in db:
            if line[:len(domain)] == domain:
                print(line)
    
    arquivo.close()


with open('db.txt', 'r', encoding='utf-8') as arquivo:
    db = arquivo.readlines()

    for line in db:
        insert(line)

arquivo.close()

"""
        www.ifpb.edu.br

    tsi                 rc

p1      p2
            SO
        proj1   proj2
"""