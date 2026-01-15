from models.produto import Produto

class Insumo(Produto):
   def __init__(self, codigo, nome, eh_composto=False):
      super().__init__(codigo, nome)
      self.eh_composto = eh_composto  # Novo atributo
      self.estrutura = []  # Adiciona estrutura para insumos compostos