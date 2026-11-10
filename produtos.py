"""Cadastro e consulta de produtos (salvos em dados/produtos.json)."""
import json
import os

from entrada import ler_texto, ler_decimal, ler_inteiro, formatar_preco

ARQUIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dados", "produtos.json")


def carregar_produtos():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_produtos(produtos):
    os.makedirs(os.path.dirname(ARQUIVO), exist_ok=True)
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(produtos, f, ensure_ascii=False, indent=2)


def buscar_por_id(produtos, id_produto):
    for p in produtos:
        if p["id"] == id_produto:
            return p
    return None


def cadastrar_produto(produtos):
    print("\n--- Cadastro de produto ---")
    nome = ler_texto("Nome: ")
    preco = ler_decimal("Preco (R$): ")
    estoque = ler_inteiro("Quantidade em estoque: ", minimo=0)
    novo_id = max((p["id"] for p in produtos), default=0) + 1
    produtos.append({"id": novo_id, "nome": nome, "preco": preco, "estoque": estoque})
    salvar_produtos(produtos)
    print(f"Produto '{nome}' cadastrado com o codigo {novo_id}.")


def listar_produtos(produtos):
    print("\n--- Produtos disponiveis ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    print(f"{'Cod':<5}{'Nome':<28}{'Preco':>12}{'Estoque':>10}")
    for p in produtos:
        print(f"{p['id']:<5}{p['nome']:<28}{formatar_preco(p['preco']):>12}{p['estoque']:>10}")
