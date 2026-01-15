from models.insumo import Insumo

class ItemEstrutura:
   def __init__(self, insumo, quantidade):
      self.insumo = insumo
      self.quantidade = quantidade

   def __str__(self):
      return f"{self.insumo.nome} (Qtd: {self.quantidade})"

   def __repr__(self):
      return self.__str__()
