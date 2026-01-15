from models.estoque import Estoque

class Empresa:
   def __init__(self, nome: str):
      self.nome = nome
      self.produtos_cadastrados = [] #lista de instâncias de Produto
      self.estoque = Estoque()
