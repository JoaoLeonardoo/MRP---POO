# Sistema MRP - Controle de Manufatura (POO)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap">
  <img src="https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white" alt="Render">
</p>

## Sobre o Sistema
Este projeto é um sistema de **MRP (Material Requirements Planning)** simplificado, desenvolvido como conclusão da disciplina de Programação Orientada a Objetos (POO) no curso de **Engenharia da Computação - IFCE**.

A ideia central é permitir que o usuário cadastre o catálogo de itens de sua empresa (Insumos e Produtos Finais) e estabeleça uma **Estrutura de Itens (BOM)**. Por exemplo, em uma marcenaria, uma mesa seria o produto final e a madeira/parafusos seriam os insumos. Ao realizar uma ordem de produção, o sistema verifica automaticamente a disponibilidade dos insumos no estoque: se houver saldo suficiente, ele desconta os componentes e adiciona o produto acabado ao inventário de forma automatizada.

Embora o Python não seja a linguagem convencional para grandes sistemas ERP web de alto tráfego, este projeto foi fundamental para treinar a lógica de negócios, a organização de camadas de software e a aplicação prática de conceitos como Herança, Composição e Encapsulamento.

## Funcionalidades Implementadas
- **Controle Decimal:** Suporte total para quantidades fracionadas (ex: 0.25 unidades), essencial para insumos medidos em kg ou litros.
- **Produção Flexível:** O sistema permite produzir qualquer item que possua uma estrutura cadastrada, eliminando travas rígidas de tipo.
- **Gestão de Inventário:** Edição rápida de nomes, códigos e quantidades de estoque diretamente na interface web.
- **Validação de Dados:** Prevenção de códigos duplicados e tratamento de erros através de pop-ups (Flashed Messages), evitando falhas brutas no servidor.
- **Deploy Automático:** Configurado para rodar no Render.com através de `Gunicorn` e `Procfile`.

## Onde está?
O sistema está hospedado e pode ser testado no link abaixo:
👉 **[https://mrp-poo.onrender.com](https://mrp-poo.onrender.com)** *(Nota: Por estar em um plano gratuito, o primeiro carregamento pode levar cerca de 30-50 segundos para o servidor "acordar").*

## Organização dele
- `models/`: Definições das classes base (Produto, Insumo, Estoque).
- `services/`: Lógica de processamento e regras de manufatura.
- `templates/`: Interface web responsiva desenvolvida com Jinja2 e Bootstrap.
- `app.py`: Controlador das rotas Flask e integração dos serviços.

## A mas se eu quiser testar no meu computador?
1. Clone o repositório: `git clone https://github.com/JoaoLeonardoo/MRP---POO.git`
2. Instale as dependências: `pip install -r requirements.txt`
3. Inicie o servidor: `python app.py`
4. Acesse: `http://127.0.0.1:5000`

---
<p align="center"> Desenvolvido por João Leonardo </p>
