from binary_tree_exception import BinaryTreeException
class Node:
  def __init__(self, dado = None):
    self.__dado = dado
    self.__esq = None
    self.__dir = None
  
# get
  @property
  def dado(self):
    return self.__dado
  
# set
  @dado.setter
  def dado(self, novo):
    self.__dado = novo
  
# get
  @property
  def esq(self):
    return self.__esq
  
# set
  @esq.setter
  def esq(self, novo):
    if self.__esq != None:
      raise BinaryTreeException("Nó esquerdo já existe")
    self.__esq = novo

# get
  @property
  def dir(self):
    return self.__dir
  
# set
  @esq.setter
  def dir(self, novo):
    if self.__dir != None:
      raise BinaryTreeException("Nó direito já existe")
    self.__dir = novo