import os, csv
import crud_usuarios, crud_denuncias, crud_comentarios

def login():
    limpar()
    print("┌──────────────────────────────────┐")
    print("│              \033[0;32mLOGIN\033[0m               │")
    print("└──────────────────────────────────┘")
    email = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    with open("data/usuarios.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            if linha["nome"] == email and linha["senha"] == senha:
                limpar()
                print("Login efetuado com sucesso!")
                return linha["nome"]
    print("Email ou senha incorretos.")
    input("Pressione Enter para continuar...")
    limpar()
    return "Anonimo"

def verificar_arquivos():
    if not os.path.exists("data/"):
        os.makedirs("data/")
    
    if not os.path.exists("data/usuarios.csv"):
        with open("data/usuarios.csv", "w") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=["nome", "email", "senha", "id_usuario"])
            escritor.writeheader()
            escritor.writerow({"nome": "admin", "email": "safereport@gmail.com", "senha": "admin", "id_usuario": 1})
    
    if not os.path.exists("data/denuncias.csv"):
        with open("data/denuncias.csv", "w") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=["titulo", "descricao", "autor","id_denuncia"])
            escritor.writeheader()
    
    if not os.path.exists("data/comentarios.csv"):
        with open("data/comentarios.csv", "w") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=["comentario", "autor", "id_denuncia", "id_comentario"])
            escritor.writeheader()

def main():
    nome_do_usuario = "Anonimo"
    limpar()
    verificar_arquivos()
    while True:
        print("┌──────────────────────────────────┐")
        print("│         \033[0;32m</> \033[1;36mSafereport\033[0m           │")
        print("└──────────────────────────────────┘")
        print("Logado como:",nome_do_usuario)
        print("┌──────────────────────────────────┐")
        if nome_do_usuario == "Anonimo":
            print("│ 1. │ login                       │")
        else:
            print("│ 1. │ logout                      │")
        print("│ 2. │ Sigup                       │")
        if nome_do_usuario == "Anonimo":
            print("│ 3. │ \033[0;31mFazer denúncia\033[0m              │")
        else:
            print("│ 3. │ Fazer denúncia              │")
        if nome_do_usuario == "Anonimo":
            print("│ 4. │ \033[0;31mComentar em uma denúncia\033[0m    │")
        else:
            print("│ 4. │ Comentar em uma denúncia    │")
        print("│ 0. │ \033[0;31mSair\033[0m                        │")
        print("└──────────────────────────────────┘")

        escolha = input("Digite a opção desejada: ")

        if escolha == "1":
            limpar()
            if nome_do_usuario == "Anonimo":
                nome_do_usuario = login()
            else:
                nome_do_usuario = "Anonimo"
        elif escolha == "2":
            crud_usuarios.main()
        elif escolha == "3":
            if nome_do_usuario == "Anonimo":
                print("Você precisa estar logado para fazer uma denúncia.")
                input("Pressione Enter para continuar...")
                limpar()
            else:
                crud_denuncias.main(nome_do_usuario)
        elif escolha == "4":
            if nome_do_usuario == "Anonimo":
                print("Você precisa estar logado para comentar em uma denúncia.")
                input("Pressione Enter para continuar...")
                limpar()
            else:
                crud_comentarios.main(nome_do_usuario)
        elif escolha == "0":
            limpar()
            break
        else:
            limpar()
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