from services.empresa_service import EmpresaService
from models.insumo import Insumo
from models.produto_final import ProdutoFinal
from models.produto import Produto




def cadastrar_produto_ui(empresa):
   empresa_service = EmpresaService(empresa)


   # interface para efeturar o cadastro de produtos
   print("\n--- NOVO CADASTRO DE PRODUTO ---")

   codigo = input("Código identificador: ").strip()

   # validacoes
   if not codigo:
      print("O código não pode ser vazio.")
      return

   nome = input("Nome do produto: ").strip()

   if not nome:
      print("O nome nao pode ser vazio")
      return



   print("Selecione o tipo:")
   print(" [1] Insumo")
   print(" [2] Produto Final")

   # set, estrutura imutavel, para garantir que o sistema nao altere ela e que o usario escolha apenas as opcoes disponiveis
   opcoes = ("1", "2")

   tipo = str(input("Opção: "))

   if tipo not in opcoes:
      print("Escolha uma opcao valida")
      return

   if tipo == "1":
      produto = Insumo(codigo, nome)
   else:
      produto = ProdutoFinal(codigo, nome)

   cadastro = empresa_service.cadastrar_produto(produto)
   if cadastro:
      print(f"✅ Produto '{nome}' cadastrado com sucesso!")
   else:
      print(f"❌ Falha ao cadastrar produto '{nome}'.")
