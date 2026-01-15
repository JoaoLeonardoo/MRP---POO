from models.estoque import Estoque
from models.empresa import Empresa
from models.produto import Produto

# ações que a empresa faz diretamente 
class EmpresaService():
   def __init__(self, empresa: Empresa):
      self.empresa = empresa

   def cadastrar_produto(self, produto: Produto):
      self.empresa.produtos_cadastrados.append(produto)
      return True

   def buscar_produto(self, codigo):
      for produto in self.empresa.produtos_cadastrados:
          if produto.codigo == codigo:
              return produto
      return None

   def excluir_produto(self, codigo):
      produto = self.buscar_produto(codigo)
      if produto:
          # Remove da lista de produtos cadastrados
          self.empresa.produtos_cadastrados.remove(produto)
          
          # Remove do dicionário de estoque se ele existir lá
          # Isso corrige o AttributeError: 'Estoque' object has no attribute 'remover_do_sistema'
          if codigo in self.empresa.estoque.itens:
              self.empresa.estoque.itens.pop(codigo)
          return True
      return False

   def listar_produtos(self):
      print("\n--- PRODUTOS CADASTRADOS ---")

      if not self.empresa.produtos_cadastrados: # verifica se a lista está vazia
         print("Nenhum produto cadastrado.")
         return

      for produto in self.empresa.produtos_cadastrados: # se a lista não estiver vazia, percorre e imprime os produtos
         print(f"Código: {produto.codigo} | Nome: {produto.nome}")
