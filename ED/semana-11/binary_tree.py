class BinaryTree:
  def em_ordem(self, arvore):
    if arvore != None:
      self.em_ordem(arvore.esq)
      print(arvore.dado, end='')  #Visita a raiz
      self.em_ordem(arvore.dir)