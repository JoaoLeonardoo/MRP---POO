from models.insumo import Insumo
from models.produto_final import ProdutoFinal
from services.empresa_service import EmpresaService
from services.produto_service import ProdutoService

def criar_estrutura_ui(empresa):
   empresa_service = EmpresaService(empresa)
   produto_service = ProdutoService()

   print("\n--- CONFIGURAR ESTRUTURA ---")

   codigo_produto = input("Código do Produto: ")

   produto = empresa_service.buscar_produto(codigo_produto)
   if not produto:
      print("Produto não encontrado")
      return
   
   # Verifica se o produto permite estrutura
   pode_ter_estrutura = False
   
   if isinstance(produto, ProdutoFinal):
      pode_ter_estrutura = True
      tipo = "Produto Final"
   elif isinstance(produto, Insumo):
      # Se for insumo, pergunta se é composto
      resposta = input(f"O insumo '{produto.nome}' é composto? (S/N): ").upper()
      if resposta == "S":
         produto.eh_composto = True
         pode_ter_estrutura = True
         tipo = "Insumo Composto"
      else:
         print("Insumos simples não têm estrutura")
         return
   else:
      print("Tipo de produto não suporta estrutura")
      return
   
   if not pode_ter_estrutura:
      print("Este produto não permite estrutura")
      return

   print(f"\nConfigurando estrutura para: {produto.nome} ({tipo})")

   while True:
      print(f"\nEstrutura atual: {produto.estrutura}")
      
      codigo_componente = input("Código do Componente (ou '0' para finalizar): ")
      
      if codigo_componente == "0":
         break
      
      componente = empresa_service.buscar_produto(codigo_componente)
      if not componente:
         print("Componente não cadastrado.")
         continue
      
      # Verifica se o componente pode ser usado
      if isinstance(componente, ProdutoFinal):
         print("Produtos finais não podem ser usados como componentes")
         continue
      
      # Evita referência circular (componente não pode ser o próprio produto)
      if componente.codigo == produto.codigo:
         print("Um produto não pode ser componente de si mesmo")
         continue
      
      try:
         qtd = int(input(f"Quantidade de '{componente.nome}' para cada '{produto.nome}': "))
         
         if qtd <= 0:
            print("Quantidade deve ser maior que zero")
            continue
         
         try:
            # Usa o mesmo método para ambos os tipos
            produto_service.criar_estrutura(produto, componente, qtd)
            print(f"Componente '{componente.nome}' adicionado à estrutura!")
            
         except ValueError as e:
            print(f"Erro: {e}")
            
      except ValueError:
         print("Digite um número válido para a quantidade")
   
   print(f"\n✅ Estrutura de '{produto.nome}' finalizada!")
   print(f"Componentes: {produto.estrutura}")