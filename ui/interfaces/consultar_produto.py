from services.empresa_service import EmpresaService

def consultar_produto_ui(empresa):
    empresa_service = EmpresaService(empresa)
    
    print("\n--- CONSULTAR PRODUTO ---")
    
    codigo = input("Código do produto: ").strip()
    
    produto = empresa_service.buscar_produto(codigo)
    if not produto:
        print("Produto não encontrado.")
        return
    
    estoque = 0
    if codigo in empresa.estoque.itens:
        estoque = empresa.estoque.itens[codigo]["quantidade"]
    
    print(f"\nProduto: {produto.nome}")
    print(f"Estoque: {estoque} unidades")
    
    if hasattr(produto, 'estrutura') and produto.estrutura:
        print("\nEstrutura:")
        for item in produto.estrutura:
            print(f"- {item.insumo.nome}: {item.quantidade} unidade(s)")
    elif hasattr(produto, 'estrutura'):
        print("\nEstrutura: Não definida")
    
    input("\nPressione Enter para voltar...")