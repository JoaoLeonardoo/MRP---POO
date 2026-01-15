from models.empresa import Empresa



def listar_produtos_ui(empresa: Empresa):
    print("\n=== Lista de Produtos Cadastrados da empresa:", empresa.nome, "===")
    if not empresa.produtos_cadastrados:
        print("Nenhum produto final cadastrado.")
    else:
        for produto in empresa.produtos_cadastrados:
            print(f"- {produto.nome} (ID: {produto.codigo})")
    print("===============================================\n")