# Roteiro Git/GitHub para o trabalho

Sugestao para 3 integrantes: **A**, **B** e **C**.

## Etapa 1 - Repositorio (um integrante faz, os outros acompanham)
1. A cria o repositorio no GitHub (ex.: `mini-ecommerce`) com README.md.
2. A convida B e C em Settings > Collaborators.
3. Todos clonam: `git clone URL_DO_REPOSITORIO` e abrem no VS Code (`code .`).
4. A envia estes arquivos na `main`:
   `git add .` -> `git commit -m "Adiciona primeira versao do e-commerce"` -> `git push`
5. B e C: `git pull` para receber o codigo.

## Etapa 3 - Branches (uma por integrante)
| Integrante | Branch | Tarefa |
|---|---|---|
| A | `feature/busca-produtos` | Busca por nome em `produtos.py` |
| B | `feature/pedidos` | Historico de pedidos em `carrinho.py` |
| C | `feature/clientes` | Cadastro de clientes (novo `clientes.py`) |

```bash
git switch -c feature/busca-produtos
# ...programar...
git status
git add .
git commit -m "Implementa busca de produtos por nome"
git push -u origin feature/busca-produtos
```
Depois abra um **Pull Request** no GitHub; outro integrante revisa e faz o merge na `main`.

## Etapa 5 - Conflito planejado
Os dois alteram **a mesma linha** do menu em `main.py`, em branches diferentes.

1. Partindo da `main` atualizada (`git switch main && git pull`):
   - **B**: `git switch -c fix/menu-b` e troque
     `print("\n===== MINI E-COMMERCE =====")` por `print("\n===== LOJA ONLINE =====")`.
     `git add . && git commit -m "Renomeia titulo do menu para LOJA ONLINE" && git push -u origin fix/menu-b`
   - **C**: `git switch main && git switch -c fix/menu-c` e troque a mesma linha por
     `print("\n===== MINI E-COMMERCE - MENU PRINCIPAL =====")`.
     `git add . && git commit -m "Detalha titulo do menu" && git push -u origin fix/menu-c`
2. Faca o merge de B na `main` (via Pull Request).
3. Tente integrar C: `git switch fix/menu-c` -> `git merge main`
   (ou atualize o PR de C). O Git avisara: `CONFLICT (content): Merge conflict in main.py`.
4. **Tire print** do aviso e do arquivo com os marcadores:
   ```
   <<<<<<< HEAD
   ...versao da sua branch...
   =======
   ...versao da main...
   >>>>>>> main
   ```
5. No VS Code, compare as duas versoes (Current x Incoming), **conversem** e decidam o texto final
   (ex.: `===== LOJA ONLINE - MENU PRINCIPAL =====`). Edite removendo os marcadores.
6. Rode `python main.py` para testar.
7. `git add main.py` -> `git commit -m "Resolve conflito no titulo do menu"` -> `git push`.
8. **Tire print** do resultado e anote a justificativa da decisao para o relatorio.

## Comandos uteis (tabela do enunciado)
`git status` | `git fetch` | `git switch nome` | `git merge nome` | `git log --oneline`

## Checklist de entrega
- [ ] Link do repositorio
- [ ] README.md completo (integrantes, execucao, funcionalidades)
- [ ] Historico de commits com todos os integrantes
- [ ] Branches e Pull Requests
- [ ] Prints do conflito e da resolucao
- [ ] Relatorio breve (tarefas, dificuldades, conflito, participacao de cada um)
- [ ] Apresentacao final
