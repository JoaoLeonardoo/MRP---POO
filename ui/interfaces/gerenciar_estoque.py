from services.estoque_service import EstoqueService

def resolve_estoque(acao: str):
   codigo = input(f"Insira o codigo do produto que você quer {acao}: ")
   quantidade = int(input(f"Insira a quantidade que voce deseja {acao}: "))

   return codigo, quantidade

def gerenciar_estoque_ui(empresa):
   while True:
      estoque_service = EstoqueService(empresa)

      print("\n--- GERENCIAR ESTOQUE ---")

      print("1 - Visualizar Estoque")
      print("2 - Adicionar itens ao Estoque")
      print("3 - Remover itens do Estoque")
      print("0 - Voltar ao Menu")

      opcao = str(input("Escolha: "))

      match opcao:
         case "1":
            estoque_service.listar()

         case "2":
            codigo, quantidade = resolve_estoque(acao="adicionar")
            estoque_service.adicionar(codigo, quantidade)

         case "3":
            codigo, quantidade = resolve_estoque(acao="remover")
            estoque_service.remover(codigo, quantidade)

         case "0":
            print("Voltando ao Menu...")
            return

         case _:
            print("\nOpção inválida! Tente um número entre 0 e 3.")
