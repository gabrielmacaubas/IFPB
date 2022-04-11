
def alocar(quantidade):
  return[None] * quantidade

  def realocar(array, tamanho):
    assert tamanho > len(array)
    novos_elementos = tamanho - len(array)
    return array + [None] * novos_elementos