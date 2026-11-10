
"""Mini E-commerce - ponto de entrada do programa (menu principal)."""

from entrada import ler_inteiro, formatar_preco
from produtos import carregar_produtos, cadastrar_produto, listar_produtos
from carrinho import (
    adicionar_ao_carrinho,
    ver_carrinho,
    remover_do_carrinho,
    finalizar_compra
)


def mostrar_menu():
    print("\n===== MINI E-COMMERCE =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Adicionar ao carrinho")
    print("4 - Ver carrinho")
    print("5 - Remover do carrinho")
    print("6 - Finalizar compra")
    print("7 - Buscar produto por nome")
    print("0 - Sair")


def buscar_produto_por_nome(produtos):
    print("\n--- Buscar produto por nome ---")
    termo = input("Digite o nome ou parte do nome: ").strip().lower()

    if not termo:
        print("Digite um nome para realizar a busca.")
        return

    encontrados = [
        p for p in produtos
        if termo in p["nome"].lower()
    ]

    if not encontrados:
        print("Nenhum produto encontrado.")
        return

    print(f"\n{len(encontrados)} produto(s) encontrado(s):")
    print(f"{'Cod':<5}{'Nome':<28}{'Preco':>12}{'Estoque':>10}")

    for p in encontrados:
        print(
            f"{p['id']:<5}{p['nome']:<28}"
            f"{formatar_preco(p['preco']):>12}"
            f"{p['estoque']:>10}"
        )


def main():
    produtos = carregar_produtos()
    carrinho = []

    while True:
        mostrar_menu()
        opcao = ler_inteiro("Escolha uma opcao: ", minimo=0, maximo=7)

        if opcao == 1:
            cadastrar_produto(produtos)
        elif opcao == 2:
            listar_produtos(produtos)
        elif opcao == 3:
            adicionar_ao_carrinho(produtos, carrinho)
        elif opcao == 4:
            ver_carrinho(produtos, carrinho)
        elif opcao == 5:
            remover_do_carrinho(produtos, carrinho)
        elif opcao == 6:
            finalizar_compra(produtos, carrinho)
        elif opcao == 7:
            buscar_produto_por_nome(produtos)
        else:
            print("Ate logo!")
            break


if __name__ == "__main__":
    main()

