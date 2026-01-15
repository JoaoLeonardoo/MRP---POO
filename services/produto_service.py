from models.produto_final import ProdutoFinal
from models.item_estrutura import ItemEstrutura
from models.insumo import Insumo

class ProdutoService():
   
   def realizar_producao(self, produto_final, qtd_desejada, estoque_service):
      if not isinstance(produto_final, ProdutoFinal):
         raise TypeError("Este item não é um Produto Final")

      if not produto_final.estrutura:
         raise ValueError("Este produto não tem estrutura cadastrada")

      pode_produzir = True
      for item in produto_final.estrutura:
         necessario = item.quantidade * qtd_desejada
         
         produto_insumo = item.insumo
         disponivel = 0
         if produto_insumo.codigo in estoque_service.empresa.estoque.itens:
            disponivel = estoque_service.empresa.estoque.itens[produto_insumo.codigo]["quantidade"]
         
         if disponivel < necessario:
            print(f"Falta Insumo: {item.insumo.nome} (Precisa: {necessario}, Tem: {disponivel})")
            pode_produzir = False

      if pode_produzir:
         for item in produto_final.estrutura:
            estoque_service.remover(item.insumo.codigo, item.quantidade * qtd_desejada)
         
         estoque_service.adicionar(produto_final.codigo, qtd_desejada)
         
         print(f"Sucesso: {qtd_desejada} unidade(s) de '{produto_final.nome}' produzidas!")
         return produto_final
      
      print("Produção cancelada: estoque insuficiente")
      return None

   def criar_estrutura(self, produto, insumo, quantidade: int):
      if quantidade <= 0:
         raise ValueError("Quantidade inválida")

      for item in produto.estrutura:
         if item.insumo.codigo == insumo.codigo:
            raise ValueError("Este insumo já está na estrutura do produto")

      produto.estrutura.append(ItemEstrutura(insumo, quantidade))