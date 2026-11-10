"""Carrinho de compras e finalizacao do pedido."""
from entrada import ler_inteiro, formatar_preco
from produtos import buscar_por_id, salvar_produtos


def adicionar_ao_carrinho(produtos, carrinho):
    print("\n--- Adicionar ao carrinho ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    produto = buscar_por_id(produtos, ler_inteiro("Codigo do produto: ", minimo=1))
    if produto is None:
        print("Produto nao encontrado.")
        return
    ja_no_carrinho = next((i for i in carrinho if i["id"] == produto["id"]), None)
    qtd_atual = ja_no_carrinho["quantidade"] if ja_no_carrinho else 0
    disponivel = produto["estoque"] - qtd_atual
    if disponivel <= 0:
        print("Produto sem estoque disponivel.")
        return
    qtd = ler_inteiro(f"Quantidade (disponivel: {disponivel}): ", minimo=1, maximo=disponivel)
    if ja_no_carrinho:
        ja_no_carrinho["quantidade"] += qtd
    else:
        carrinho.append({"id": produto["id"], "quantidade": qtd})
    print(f"{qtd}x {produto['nome']} adicionado(s) ao carrinho.")


def calcular_total(produtos, carrinho):
    return sum(buscar_por_id(produtos, i["id"])["preco"] * i["quantidade"] for i in carrinho)


def ver_carrinho(produtos, carrinho):
    print("\n--- Carrinho ---")
    if not carrinho:
        print("O carrinho esta vazio.")
        return
    for i in carrinho:
        p = buscar_por_id(produtos, i["id"])
        subtotal = p["preco"] * i["quantidade"]
        print(f"{p['id']:<5}{p['nome']:<28}{i['quantidade']:>4} x {formatar_preco(p['preco']):>10} = {formatar_preco(subtotal):>11}")
    print(f"TOTAL: {formatar_preco(calcular_total(produtos, carrinho))}")


def remover_do_carrinho(produtos, carrinho):
    print("\n--- Remover do carrinho ---")
    if not carrinho:
        print("O carrinho esta vazio.")
        return
    ver_carrinho(produtos, carrinho)
    id_produto = ler_inteiro("Codigo do produto a remover: ", minimo=1)
    for i in carrinho:
        if i["id"] == id_produto:
            carrinho.remove(i)
            print("Item removido.")
            return
    print("Esse produto nao esta no carrinho.")


def finalizar_compra(produtos, carrinho):
    print("\n--- Finalizar compra ---")
    if not carrinho:
        print("O carrinho esta vazio.")
        return
    ver_carrinho(produtos, carrinho)
    confirma = input("Confirmar compra? (s/n): ").strip().lower()
    if confirma != "s":
        print("Compra cancelada.")
        return
    total = calcular_total(produtos, carrinho)
    for i in carrinho:
        buscar_por_id(produtos, i["id"])["estoque"] -= i["quantidade"]
    salvar_produtos(produtos)
    carrinho.clear()
    print(f"Compra realizada com sucesso! Total pago: {formatar_preco(total)}")
