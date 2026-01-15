from models.insumo import Insumo
from models.empresa import Empresa



class EstoqueService():
   def __init__(self, empresa: Empresa):
      self.empresa = empresa

   def adicionar(self, produto_codigo, quantidade):
      if quantidade <= 0:
         print("A quantidade deve ser um inteiro positivo")
         return

      produto = None
      for produto_cadastrado in self.empresa.produtos_cadastrados:
         if produto_cadastrado.codigo == produto_codigo:
             produto = produto_cadastrado
             break

      if produto is None:
         print("Produto não encontrado")
         return

      itens = self.empresa.estoque.itens

      if produto.codigo in itens:
         itens[produto.codigo]["quantidade"] += quantidade
      else:
         itens[produto.codigo] = {
             "produto": produto,
             "quantidade": quantidade
         }



   def remover(self, produto_codigo, quantidade):
      if quantidade <= 0:
         print("A quantidade deve ser um inteiro positivo")
         return

      produto = None
      for produto_cadastrado in self.empresa.produtos_cadastrados:
         if produto_cadastrado.codigo == produto_codigo:
             produto = produto_cadastrado
             break

      if produto is None:
         print("Produto não encontrado")
         return

      itens = self.empresa.estoque.itens

      if produto.codigo not in itens:
         print("Produto não está no estoque")
         return

      if itens[produto.codigo]["quantidade"] < quantidade:
         print("Quantidade insuficiente em estoque")
         return

      itens[produto.codigo]["quantidade"] -= quantidade



   def listar(self):
      print("\n--- STATUS DO ESTOQUE ---")

      if not self.empresa.estoque.itens:
         print("Estoque vazio.")
         return

      for item in self.empresa.estoque.itens.values():
         tipo = "Insumo" if isinstance(item["produto"], Insumo) else "Prod. Final"
         print(
             f"{item['produto']} | "
             f"Tipo: {tipo} | "
             f"Qtd: {item['quantidade']}"
         )



   def obter_quantidade(self, produto):
      if produto.codigo in self.itens:
         return self.itens[produto.codigo]["quantidade"]
      return 0



   def definir_quantidade(self, produto_codigo, nova_qtd):
      if produto_codigo in self.itens:
         self.itens[produto_codigo]["quantidade"] = nova_qtd
         return True
      return False



   def deletar_do_estoque(self, codigo):
      if codigo in self.itens:
         del self.itens[codigo]
