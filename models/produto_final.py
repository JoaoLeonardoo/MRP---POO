from models.produto import Produto

class ProdutoFinal(Produto):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.estrutura = [] #insumos necessários para produzir o produto final

    def __str__(self):
        return f"{self.codigo} - {self.nome}"
