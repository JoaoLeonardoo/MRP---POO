from flask import Flask, render_template, request, redirect, url_for, flash
from models.empresa import Empresa
from models.insumo import Insumo
from models.produto_final import ProdutoFinal
from services.empresa_service import EmpresaService
from services.estoque_service import EstoqueService
from services.produto_service import ProdutoService

app = Flask(__name__)
app.secret_key = "ifce_eng_comp_mrp"

empresa = None
e_service = None
est_service = None
p_service = ProdutoService()

@app.route('/setup', methods=['GET', 'POST'])
def setup():
    global empresa, e_service, est_service
    if request.method == 'POST':
        nome = request.form.get('nome_empresa')
        empresa = Empresa(nome)
        e_service = EmpresaService(empresa)
        est_service = EstoqueService(empresa)
        return redirect(url_for('home'))
    return render_template('setup.html')

@app.route('/')
def home():
    if not empresa: return redirect(url_for('setup'))
    return render_template('index.html', empresa=empresa)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    codigo = request.form.get('codigo').strip()
    nome = request.form.get('nome').strip()
    tipo = request.form.get('tipo')
    if e_service.buscar_produto(codigo):
        flash(f"Erro: Código {codigo} já existe!")
        return redirect(url_for('home'))
    p = Insumo(codigo, nome) if tipo == "1" else ProdutoFinal(codigo, nome)
    e_service.cadastrar_produto(p)
    flash(f"Produto '{nome}' cadastrado!")
    return redirect(url_for('home'))

@app.route('/editar', methods=['POST'])
def editar():
    cod_original = request.form.get('codigo_original')
    novo_nome = request.form.get('nome')
    novo_cod = request.form.get('codigo')
    novo_tipo = request.form.get('tipo')

    prod = e_service.buscar_produto(cod_original)
    if prod:
        # Se mudar o tipo, precisamos instanciar a classe correta
        tipo_atual = "1" if isinstance(prod, Insumo) else "2"
        if novo_tipo != tipo_atual:
            novo_obj = Insumo(novo_cod, novo_nome) if novo_tipo == "1" else ProdutoFinal(novo_cod, novo_nome)
            novo_obj.estrutura = getattr(prod, 'estrutura', [])
            empresa.produtos_cadastrados.remove(prod)
            empresa.produtos_cadastrados.append(novo_obj)
            prod = novo_obj
        else:
            prod.nome = novo_nome
            prod.codigo = novo_cod

        # Atualiza estoque se o código mudou
        if novo_cod != cod_original and cod_original in empresa.estoque.itens:
            empresa.estoque.itens[novo_cod] = empresa.estoque.itens.pop(cod_original)
        
        flash("Alterações salvas!")
    return redirect(url_for('home'))

@app.route('/editar_estoque_direto', methods=['POST'])
def editar_estoque_direto():
    codigo = request.form.get('codigo')
    try:
        nova_qtd = float(request.form.get('quantidade')) # Suporte a decimal
        if codigo in empresa.estoque.itens:
            empresa.estoque.itens[codigo]["quantidade"] = nova_qtd
        else:
            p = e_service.buscar_produto(codigo)
            if p: empresa.estoque.itens[codigo] = {"produto": p, "quantidade": nova_qtd}
        flash(f"Estoque de {codigo} atualizado.")
    except: flash("Valor inválido.")
    return redirect(url_for('home'))

@app.route('/vincular_estrutura', methods=['POST'])
def vincular_estrutura():
    pai = e_service.buscar_produto(request.form.get('pai_codigo'))
    filho = e_service.buscar_produto(request.form.get('filho_codigo'))
    try:
        qtd = float(request.form.get('quantidade'))
        if pai and filho:
            p_service.criar_estrutura(pai, filho, qtd)
            flash("Estrutura atualizada!")
    except Exception as e: flash(str(e))
    return redirect(url_for('home'))

@app.route('/produzir', methods=['POST'])
def produzir():
    codigo = request.form.get('codigo')
    try:
        qtd = float(request.form.get('quantidade'))
        prod = e_service.buscar_produto(codigo)
        if prod and p_service.realizar_producao(prod, qtd, est_service):
            flash(f"Produzido {qtd} de {prod.nome}")
        else: flash("Erro na produção ou falta de insumos.")
    except Exception as e: flash(f"Atenção: {str(e)}")
    return redirect(url_for('home'))

@app.route('/deletar/<codigo>')
def deletar(codigo):
    if e_service.excluir_produto(codigo): flash("Item removido.")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
