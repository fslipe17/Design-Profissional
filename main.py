"""Mini E-commerce - ponto de entrada do programa (menu principal)."""
from entrada import ler_inteiro
from produtos import carregar_produtos, cadastrar_produto, listar_produtos
from carrinho import (adicionar_ao_carrinho, ver_carrinho,
                      remover_do_carrinho, finalizar_compra)


def mostrar_menu():
    print("\n===== MINI E-COMMERCE =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Adicionar ao carrinho")
    print("4 - Ver carrinho")
    print("5 - Remover do carrinho")
    print("6 - Finalizar compra")
    print("0 - Sair")


def main():
    produtos = carregar_produtos()
    carrinho = []
    while True:
        mostrar_menu()
        opcao = ler_inteiro("Escolha uma opcao: ", minimo=0, maximo=6)
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
        else:
            print("Ate logo!")
            break


if __name__ == "__main__":
    main()
