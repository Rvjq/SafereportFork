import os
import csv

def generate_id():
    with open("data/usuarios.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        linha = False
        for linha in leitor:
            pass
        if not linha:
            return 1
        return int(linha["id_usuario"]) + 1

def checar_nome (nome):
    if nome == "":
        print("Nome não pode ser vazio")
        return True
    elif nome == "Anonimo":
        print("O nome \"Anonimo\" não pode ser usado")
        return True
    with open("data/usuarios.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            if linha["nome"] == nome:
                print("Esse Nome já existe em nosso sistema")
                return True
    return False

def create_conta():
    print("┌───────────────────────────────────┐")
    print("│        Criar uma nova conta       │")
    print("└───────────────────────────────────┘")
    nome = input("Digite seu nome: ")
    if checar_nome(nome):
        input("Pressione Enter para continuar...")
        limpar()
        return
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    with open("data/usuarios.csv", "a") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["nome", "email", "senha", "id_usuario"])
        escritor.writerow({"nome": nome, "email": email, "senha": senha, "id_usuario": generate_id()})
    print("Conta criada com sucesso!")
    input("Pressione Enter para continuar...")
    limpar()

def read_contas():
    print("┌───────────────────────────────────┐")
    print("│         Contas no sistema         │")
    print("└───────────────────────────────────┘")
    print("┌─────────────────┬─────────────────┐")
    print("│       ID        │       Nome      │")
    print("├─────────────────┼─────────────────┤")
    with open("data/usuarios.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            print("│",linha["id_usuario"]," "*(14-len(linha["id_usuario"])),"│",linha["nome"]," "*(14-len(linha["nome"])),"│")
    print("└─────────────────┴─────────────────┘")
    input("Pressione Enter para continuar...")
    limpar()

def update_senha():
    print("┌───────────────────────────────────┐")
    print("│         Alterar a senha           │")
    print("└───────────────────────────────────┘")
    nome_conta = input("Digite o nome da conta que deseja alterar a senha: ")
    antiga_senha = input("Digite a senha antiga: ")
    nova_senha = input("Digite a nova senha: ")
    with open("data/usuarios.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        contas = []
        for linha in leitor:
            if linha["nome"] == nome_conta and linha["senha"] == antiga_senha:
                linha["senha"] = nova_senha
                print("Senha alterada com sucesso!")
            contas.append(linha)
    with open("data/usuarios.csv", "w") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["nome", "email", "senha", "id_usuario"])
        escritor.writeheader()
        for conta in contas:
            escritor.writerow(conta)
    input("Pressione Enter para continuar...")
    limpar()

def delete_conta():
    print("┌───────────────────────────────────┐")
    print("│         Deletar uma conta         │")
    print("└───────────────────────────────────┘")
    id_conta = input("Digite o ID da conta que deseja deletar: ")
    with open("data/usuarios.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        contas = []
        for linha in leitor:
            if linha["id_usuario"] == id_conta:
                print("Conta de",linha["nome"],"deletada com sucesso!")
            else:
                contas.append(linha)
    with open("data/usuarios.csv", "w") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["nome", "email", "senha", "id_usuario"])
        escritor.writeheader()
        for conta in contas:
            escritor.writerow(conta)
    input("Pressione Enter para continuar...")
    limpar()

def main():
    limpar()
    while True:
        print("┌───────────────────────────────────┐")
        print("│           Autenticação            │")
        print("└───────────────────────────────────┘")
        print("┌───────────────────────────────────┐")
        print("│ 1. │ Criar um conta               │")
        print("│ 2. │ Procurar conta existente     │")
        print("│ 3. │ Alterar senha                │")
        print("│ 4. │ Deletar conta                │")
        print("│ 0. │ \033[0;31mSair\033[0m                         │")
        print("└───────────────────────────────────┘")

        escolha = input("Digite a opção desejada: ")

        if escolha == "1":
            limpar()
            create_conta()
        elif escolha == "2":
            limpar()
            read_contas()
        elif escolha == "3":
            limpar()
            update_senha()
        elif escolha == "4":
            limpar()
            delete_conta
        elif escolha == "0":
            limpar()
            break
        else:
            opcao_invalida()

def opcao_invalida():  
    limpar()
    print("┌──────────────────────────────────────────────────────┐")
    print("│ \033[0;31mOpção inválida\033[0;0m. Por favor, escolha uma opção válida. │")
    print("└──────────────────────────────────────────────────────┘")

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()