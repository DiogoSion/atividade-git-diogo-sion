nomes = []

def criar(nome):
    nomes.append(nome)
    print(f"Nome '{nome}' adicionado.")

def listar():
    print("Lista de nomes:")
    for nome in nomes:
        print(nome)

def atualizar(antigo, novo):
    if antigo in nomes:
        index = nomes.index(antigo)
        nomes[index] = novo
        print(f"Nome '{antigo}' atualizado para '{novo}'.")
    else:
        print(f"Nome '{antigo}' não encontrado.")

def deletar(nome):
    if nome in nomes:
        nomes.remove(nome)
        print(f"Nome '{nome}' removido.")
    else:
        print(f"Nome '{nome}' não encontrado.")

if __name__ == "__main__":
    while True:
        print("\nOperações: criar, listar, atualizar, deletar, sair")
        operacao = input("Escolha uma operação: ").strip().lower()

        if operacao == "criar":
            nome = input("Digite o nome para adicionar: ")
            criar(nome)
        elif operacao == "listar":
            listar()
        elif operacao == "atualizar":
            antigo = input("Nome atual: ")
            novo = input("Novo nome: ")
            atualizar(antigo, novo)
        elif operacao == "deletar":
            nome = input("Nome para remover: ")
            deletar(nome)
        elif operacao == "sair":
            break
        else:
            print("Operação inválida!")
