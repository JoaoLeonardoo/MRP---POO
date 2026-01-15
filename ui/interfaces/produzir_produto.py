from services.empresa_service import EmpresaService
from services.produto_service import ProdutoService
from services.estoque_service import EstoqueService

def produzir_produto_ui(empresa):
   empresa_service = EmpresaService(empresa)
   produto_service = ProdutoService()
   estoque_service = EstoqueService(empresa)
   
   print("\n--- ORDEM DE PRODUÇÃO ---")

   codigo = input("Código do Produto Final: ")

   produto = empresa_service.buscar_produto(codigo)
   if not produto:
      print("Produto nao encontrado")
      return

   quantidade = int(input("Quantidade a produzir: "))
   if quantidade <= 0:
      print("Quantidade deve ser um número inteiro positivo.")
      return

   produto = produto_service.realizar_producao(produto, quantidade, estoque_service)

   if produto:
      print(f"Produto '{produto.nome}' produzido com sucesso!!!")