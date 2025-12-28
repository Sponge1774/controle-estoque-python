# ==============================================================================
# SISTEMA DE CONTROLE DE ESTOQUE E REGISTRO DE VENDAS
#
# Objetivo acadêmico:
# Aplicar princípios de lógica computacional utilizando:
# - Estruturas condicionais (if / elif / else)
# - Estruturas de repetição (while / for)
# - Estruturas de dados (dicionários e listas)
# - Modularização por funções
#
# Funcionalidades disponibilizadas:
# 1. Adicionar produtos ao estoque
# 2. Atualizar produtos existentes
# 3. Excluir produtos
# 4. Visualizar estoque
# 5. Registrar vendas vinculando cliente e produtos
# 6. Consultar histórico de vendas
# ==============================================================================


# ------------------------------------------------------------------------------
# 1. ESTRUTURAS DE DADOS
# ------------------------------------------------------------------------------

# Dicionário que representa o estoque
estoque = {}

# Lista que armazena todas as vendas realizadas
vendas = []


# ------------------------------------------------------------------------------
# 2. FUNÇÕES DE INTERFACE
# ------------------------------------------------------------------------------

def limpar_tela():
    """Melhora a visualização simulando limpeza do terminal."""
    print("\n" * 40)


def pausar():
    """Pausa o sistema até o usuário pressionar ENTER."""
    input("\nPressione ENTER para continuar...")


# ------------------------------------------------------------------------------
# 3. FUNÇÕES DO ESTOQUE
# ------------------------------------------------------------------------------

def adicionar_produto():
    limpar_tela()
    print("=== ADICIONAR PRODUTO ===")

    nome = input("Nome do produto: ").strip().title()

    if nome in estoque:
        print("Erro: Produto já cadastrado.")
        pausar()
        return

    try:
        preco = float(input("Preço (R$): "))
        quantidade = int(input("Quantidade inicial: "))

        if preco <= 0 or quantidade < 0:
            print("Erro: valores inválidos.")
            pausar()
            return

        estoque[nome] = {
            "preco": preco,
            "quantidade": quantidade
        }

        print("Produto cadastrado com sucesso.")

    except ValueError:
        print("Erro: informe valores numéricos válidos.")

    pausar()


def atualizar_produto():
    limpar_tela()
    print("=== ATUALIZAR PRODUTO ===")

    if not estoque:
        print("Estoque vazio.")
        pausar()
        return

    nome = input("Nome do produto: ").strip().title()

    if nome not in estoque:
        print("Produto não encontrado.")
        pausar()
        return

    try:
        novo_preco = float(input("Novo preço (R$): "))
        nova_quantidade = int(input("Nova quantidade: "))

        if novo_preco <= 0 or nova_quantidade < 0:
            print("Erro: valores inválidos.")
            pausar()
            return

        estoque[nome]["preco"] = novo_preco
        estoque[nome]["quantidade"] = nova_quantidade

        print("Produto atualizado com sucesso.")

    except ValueError:
        print("Erro: informe valores numéricos válidos.")

    pausar()


def excluir_produto():
    limpar_tela()
    print("=== EXCLUIR PRODUTO ===")

    if not estoque:
        print("Estoque vazio.")
        pausar()
        return

    nome = input("Nome do produto: ").strip().title()

    if nome in estoque:
        del estoque[nome]
        print("Produto excluído com sucesso.")
    else:
        print("Produto não encontrado.")

    pausar()


def visualizar_estoque():
    limpar_tela()
    print("=== ESTOQUE ATUAL ===")

    if not estoque:
        print("Estoque vazio.")
        pausar()
        return

    for nome, dados in estoque.items():
        print(f"Produto: {nome}")
        print(f"Preço: R$ {dados['preco']:.2f}")
        print(f"Quantidade: {dados['quantidade']}")
        print("-" * 30)

    pausar()


# ------------------------------------------------------------------------------
# 4. REGISTRO COMPLETO DE VENDAS
# ------------------------------------------------------------------------------

def registrar_venda():
    limpar_tela()
    print("=== REGISTRAR VENDA ===")

    if not estoque:
        print("Estoque vazio. Não é possível registrar vendas.")
        pausar()
        return

    cliente = input("Nome do cliente: ").strip().title()

    itens_venda = []
    valor_total = 0

    while True:
        produto = input("\nProduto (ou ENTER para finalizar): ").strip().title()

        if produto == "":
            break

        if produto not in estoque:
            print("Produto não encontrado.")
            continue

        try:
            quantidade = int(input("Quantidade: "))

            if quantidade <= 0:
                print("Quantidade inválida.")
                continue

            if quantidade > estoque[produto]["quantidade"]:
                print("Estoque insuficiente.")
                continue

            estoque[produto]["quantidade"] -= quantidade

            subtotal = quantidade * estoque[produto]["preco"]

            itens_venda.append({
                "produto": produto,
                "quantidade": quantidade,
                "preco_unitario": estoque[produto]["preco"],
                "subtotal": subtotal
            })

            valor_total += subtotal

        except ValueError:
            print("Informe um número válido.")

    if not itens_venda:
        print("Nenhum item informado. Venda cancelada.")
        pausar()
        return

    venda = {
        "cliente": cliente,
        "itens": itens_venda,
        "valor_total": valor_total
    }

    vendas.append(venda)

    print("\nVenda registrada com sucesso.")
    print(f"Cliente: {cliente}")
    print(f"Valor total: R$ {valor_total:.2f}")

    pausar()


# ------------------------------------------------------------------------------
# 5. CONSULTA DE VENDAS
# ------------------------------------------------------------------------------

def visualizar_vendas():
    limpar_tela()
    print("=== RELATÓRIO DE VENDAS ===")

    if not vendas:
        print("Nenhuma venda registrada.")
        pausar()
        return

    for i, venda in enumerate(vendas, start=1):
        print(f"\nVenda {i}")
        print(f"Cliente: {venda['cliente']}")
        print(f"Valor total: R$ {venda['valor_total']:.2f}")
        print("Itens:")

        for item in venda["itens"]:
            print(f"  - {item['produto']} | Qtd: {item['quantidade']} | Unit: {item['preco_unitario']:.2f} | Subtotal: {item['subtotal']:.2f}")

        print("-" * 40)

    pausar()


# ------------------------------------------------------------------------------
# 6. MENU PRINCIPAL
# ------------------------------------------------------------------------------

def menu():
    while True:
        limpar_tela()
        print("=== SISTEMA DE CONTROLE DE ESTOQUE ===")
        print("1 - Adicionar produto")
        print("2 - Atualizar produto")
        print("3 - Excluir produto")
        print("4 - Visualizar estoque")
        print("5 - Registrar venda")
        print("6 - Visualizar vendas")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            atualizar_produto()
        elif opcao == "3":
            excluir_produto()
        elif opcao == "4":
            visualizar_estoque()
        elif opcao == "5":
            registrar_venda()
        elif opcao == "6":
            visualizar_vendas()
        elif opcao == "7":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")
            pausar()


# ------------------------------------------------------------------------------
# 7. EXECUÇÃO
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    menu()
