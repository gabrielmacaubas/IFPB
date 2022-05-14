from BinaryTree import BinaryTree

arvore = BinaryTree("www.ifpb.edu.br")
fw = open("db.txt", "w")
fw.write("www.ifpb.edu.br")
fw.close()

def add(data):
    string = data.rsplit('/', 2)
    target = string[-2]
    new_data = string[-1]
    f = open("db.txt", "a")

    if arvore.getNode(target).hasLeftChild():
        arvore.addRight(target, new_data)
        f.write("\n")
        f.write(data)
        
    else:
        arvore.addLeft(target, new_data)
        f.write("\n")
        f.write(data)
  
    f.close()

    with open('db.txt', 'r', encoding='utf-8') as arquivo:
        db = arquivo.read()
        print(db)
    
    arquivo.close()

"""
        www.ifpb.edu.br

    tsi                 rc

p1      p2
"""
