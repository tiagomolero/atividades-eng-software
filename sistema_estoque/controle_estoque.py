from datetime import datetime

# Armazena o histórico das movimentações
historico = []

# Produtos cadastrados e suas quantidades em estoque
estoque = {
    "Teclado": 10,
    "Mouse": 15,
    "Monitor": 5
}

# Solicita e valida a data da movimentação
def solicitar_data():
    while True:
        data = input("Data (DD/MM/AAAA): ").strip()

        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            print("Data inválida! Use o formato DD/MM/AAAA.")

# Registra a entrada de produtos no estoque
def registrar_entrada():
    print("\n=== ENTRADA DE PRODUTOS ===")

    for produto in estoque:
        print(f"- {produto}")

    produto = input("\nDigite o nome do produto: ").strip().title()

    if produto not in estoque:
        print("Produto não cadastrado!")
        return

    try:
        quantidade = int(input("Quantidade recebida: "))

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero!")
            return

    except ValueError:
        print("Digite uma quantidade válida!")
        return

    data = solicitar_data()

    responsavel = input("Nome do responsável: ").strip()

    if not responsavel:
        print("O nome do responsável é obrigatório!")
        return

    estoque[produto] += quantidade

    historico.append({
        "tipo": "Entrada",
        "produto": produto,
        "quantidade": quantidade,
        "data": data,
        "responsavel": responsavel
    })

    print(f"\nEntrada registrada em {data}!")
    print(f"Estoque atualizado de {produto}: {estoque[produto]} unidades.")

# Registra a saída de produtos do estoque
def registrar_saida():
    print("\n=== SAÍDA DE PRODUTOS ===")

    for produto in estoque:
        print(f"- {produto}")

    produto = input("\nDigite o nome do produto: ").strip().title()

    if produto not in estoque:
        print("Produto não cadastrado!")
        return

    try:
        quantidade = int(input("Quantidade retirada: "))

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero!")
            return

    except ValueError:
        print("Digite uma quantidade válida!")
        return

    if quantidade > estoque[produto]:
        print("Estoque insuficiente!")
        return

    data = solicitar_data()
    responsavel = input("Nome do responsável: ").strip()

    if not responsavel:
        print("O nome do responsável é obrigatório!")
        return

    estoque[produto] -= quantidade

    historico.append({
        "tipo": "Saída",
        "produto": produto,
        "quantidade": quantidade,
        "data": data,
        "responsavel": responsavel
    })

    print(f"\nSaída registrada em {data}!")
    print(f"Responsável: {responsavel}")
    print(f"Estoque restante de {produto}: {estoque[produto]} unidades.")

# Exibe os produtos e suas quantidades disponíveis
def consultar_estoque():
    print("\n=== ESTOQUE ATUAL ===")

    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade} unidades")

# Exibe o histórico de entradas e saídas
def consultar_historico():
    print("\n=== HISTÓRICO DE MOVIMENTAÇÕES ===")

    if not historico:
        print("Nenhuma movimentação registrada.")
        return

    for movimento in historico:
        print(f"\nTipo: {movimento['tipo']}")
        print(f"Produto: {movimento['produto']}")
        print(f"Quantidade: {movimento['quantidade']}")
        print(f"Data: {movimento['data']}")
        print(f"Responsável: {movimento['responsavel']}")
        print("-" * 30)

def main():
    while True:
        print("\n=== CONTROLE DE ESTOQUE ===")
        print("1 - Entrada de produtos")
        print("2 - Saída de produtos")
        print("3 - Consultar estoque")
        print("4 - Histórico de movimentações")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            registrar_entrada()
        elif opcao == "2":
            registrar_saida()
        elif opcao == "3":
            consultar_estoque()
        elif opcao == "4":
            consultar_historico()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()