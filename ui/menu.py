from services.empresa_service import EmpresaService
from services.produto_service import ProdutoService
from services.estoque_service import EstoqueService

from ui.interfaces.cadastrar_produto import cadastrar_produto_ui
from ui.interfaces.criar_estrutura import criar_estrutura_ui
from ui.interfaces.produzir_produto import produzir_produto_ui
from ui.interfaces.gerenciar_estoque import gerenciar_estoque_ui
from ui.interfaces.listar_produtos import listar_produtos_ui
from ui.interfaces.consultar_produto import consultar_produto_ui


def menu_principal(empresa):
   while True:
      print("\n==============================")
      print("SISTEMA MRP -", empresa.nome)
      print("==============================")
      print("1 - Cadastrar Produto")
      print("2 - Criar Estrutura de Produto")
      print("3 - Produzir Produto")
      print("4 - Gerenciar Estoque")
      print("5 - Listar Produtos Cadastrados")
      print("6 - Consultar Produto")
      print("0 - Sair")

      opcao = input("Escolha: ")

      match opcao:
         case "1":
            cadastrar_produto_ui(empresa)

         case "2":
            criar_estrutura_ui(empresa)

         case "3":
            produzir_produto_ui(empresa)

         case "4":
            gerenciar_estoque_ui(empresa)

         case "5":
           listar_produtos_ui(empresa)

         case "6":
            consultar_produto_ui(empresa)

         case "0":
            print("\nEncerrando sistema... Até logo!")
            break

         case _:
            print("\nOpção inválida! Tente um número entre 0 e 6.")