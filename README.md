# Mini E-commerce

Sistema de e-commerce em Python para terminal, desenvolvido em equipe na disciplina
**Design Profissional** (Universidade Positivo) usando Git e GitHub.

## Integrantes
- Nome 1 (@Brunaocoding)
- Nome 2 (@fslipe17)
- Nome 3 (@rissinhu)

## Como executar
Requisito: Python 3.8 ou superior.

```bash
git clone URL_DO_REPOSITORIO
cd ecommerce
python main.py
```

## Funcionalidades (versao 1)
| Opcao | Funcionalidade |
|-------|----------------|
| 1 | Cadastrar produto (nome, preco, estoque) |
| 2 | Listar produtos |
| 3 | Adicionar produto ao carrinho (valida estoque) |
| 4 | Ver carrinho e total |
| 5 | Remover item do carrinho |
| 6 | Finalizar compra (baixa o estoque) |
| 0 | Sair |

Os produtos ficam salvos em `dados/produtos.json`.

## Validacoes
- Campos de texto nao podem ficar vazios.
- Preco deve ser numerico e maior que zero (aceita virgula).
- Quantidades devem ser inteiras e nao podem exceder o estoque.
- Opcoes do menu so aceitam numeros validos.

## Estrutura
```
main.py       -> menu principal
entrada.py    -> leitura e validacao de dados
produtos.py   -> cadastro e consulta de produtos
carrinho.py   -> carrinho e finalizacao da compra
dados/        -> produtos.json (persistencia)
```

## Evolucao planejada
- [ ] Busca de produtos por nome
- [ ] Cadastro de clientes
- [ ] Historico de pedidos
- [ ] Cupons de desconto
- [ ] Relatorio de vendas
