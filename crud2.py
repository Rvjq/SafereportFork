import os
import csv

def generate_id():
    with open("data/denuncias.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        linha = False
        for linha in leitor:
            pass
        if not linha:
            return 1
        return int(linha["id_denuncia"]) + 1

def create_denuncia(nome_de_usuario):
    print("┌───────────────────────────────────┐")
    print("│      Criar uma nova denúncia      │")
    print("└───────────────────────────────────┘")
    titulo = input("Digite o título da denúncia: ")
    descricao = input("Digite a descrição da denúncia: ")
    autor = nome_de_usuario
    with open("data/denuncias.csv", "a") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["titulo", "descricao", "autor","id_denuncia"])
        escritor.writerow({"titulo": titulo, "descricao": descricao, "autor": autor, "id_denuncia": generate_id()})
    print("Denúncia criada com sucesso!")
    input("Pressione Enter para continuar...")
    limpar()

def read_denuncias():
    print("┌───────────────────────────────────────────────────────┐")
    print("│                   Denúncias no sistema                │")
    print("└───────────────────────────────────────────────────────┘")
    print("┌─────────────────┬─────────────────┬───────────────────┐")
    print("│       ID        │      Título     │      Denuncia     │")
    print("├─────────────────┼─────────────────┼───────────────────┤")
    with open("data/denuncias.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            print("│",linha["id_denuncia"]," "*(14-len(linha["id_denuncia"])),"│",linha["titulo"]," "*(14-len(linha["titulo"])),"│",linha["descricao"]," "*(20-len(linha["descricao"])),"│")
    print("└─────────────────┴─────────────────┴───────────────────┘")
    input("Pressione Enter para continuar...")
    limpar()

def update_denuncia():
    print("┌───────────────────────────────────┐")
    print("│      Atualizar uma denúncia       │")
    print("└───────────────────────────────────┘")
    id_denuncia = input("Digite o ID da denúncia que deseja atualizar: ")
    titulo = input("Digite o novo título da denúncia: ")
    descricao = input("Digite a nova descrição da denúncia: ")
    with open("data/denuncias.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        denuncias = []
        for linha in leitor:
            if linha["id_denuncia"] == id_denuncia:
                linha["titulo"] = titulo
                linha["descricao"] = descricao
                print("Denúncia atualizada com sucesso!")
            denuncias.append(linha)
    with open("data/denuncias.csv", "w") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["titulo", "descricao", "autor","id_denuncia"])
        escritor.writeheader()
        for denuncia in denuncias:
            escritor.writerow(denuncia)
    input("Pressione Enter para continuar...")
    limpar()

def delete_denuncia():
    print("┌───────────────────────────────────┐")
    print("│       Excluir uma denúncia        │")
    print("└───────────────────────────────────┘")
    id_denuncia = input("Digite o ID da denúncia que deseja excluir: ")
    with open("data/denuncias.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        denuncias = []
        for linha in leitor:
            if linha["id_denuncia"] == id_denuncia:
                print("Denúncia excluída com sucesso!")
            else:
                denuncias.append(linha)
    with open("data/denuncias.csv", "w") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["titulo", "descricao", "autor","id_denuncia"])
        escritor.writeheader()
        for denuncia in denuncias:
            escritor.writerow(denuncia)
    
    # Excluindo comentários relacionados à denúncia
    with open("data/comentarios.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        comentarios = []
        for linha in leitor:
            if linha["id_denuncia"] == id_denuncia:
                print("Comentário excluído com sucesso!")
            else:
                comentarios.append(linha)
    with open("data/comentarios.csv", "w") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["comentario", "autor", "id_denuncia", "id_comentario"])
        escritor.writeheader()
        for comentario in comentarios:
            escritor.writerow(comentario)
    
    input("Pressione Enter para continuar...")
    limpar()

def main(nome_do_usuario):
    limpar()
    while True:
        print("┌──────────────────────────────────┐")
        print("│            DENUNCIAS             │")
        print("└──────────────────────────────────┘")
        print("┌──────────────────────────────────┐")
        print("│ 1. │ Criar denúncia              │")
        print("│ 2. │ Ver denúncias               │")
        print("│ 3. │ Atualizar denúncia          │")
        print("│ 4. │ Excluir denúncia            │")
        print("│ 0. │ \033[0;31mSair\033[0m                        │")
        print("└──────────────────────────────────┘")

        escolha = input("Digite a opção desejada: ")

        if escolha == "1":
            limpar()
            create_denuncia(nome_do_usuario)
        elif escolha == "2":
            limpar()
            read_denuncias()
        elif escolha == "3":
            limpar()
            update_denuncia()
        elif escolha == "4":
            limpar()
            delete_denuncia()
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
    main("Debug")