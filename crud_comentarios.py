import os
import csv

def generate_id():
    with open("data/comentarios.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        linha = False
        for linha in leitor:
            pass
        if not linha:
            return 1
        return int(linha["id_comentario"]) + 1

def checar_denuncia(id_denuncia):
    with open("data/denuncias.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            if linha["id_denuncia"] == id_denuncia:
                return True
    return False

def create_comentario(nome_do_usuario):
    print("┌───────────────────────────────────┐")
    print("│      Criar um novo comentário     │")
    print("└───────────────────────────────────┘")
    comentario = input("Digite o comentário: ")
    autor = nome_do_usuario
    id_denuncia = input("Digite o ID da denúncia: ")
    if checar_denuncia(id_denuncia) == False:
        print("Denúncia não encontrada!")
        input("Pressione Enter para continuar...")
        limpar()
        return
    with open("data/comentarios.csv", "a") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["comentario", "autor", "id_denuncia", "id_comentario"])
        escritor.writerow({"comentario": comentario, "autor": autor, "id_denuncia": id_denuncia, "id_comentario": generate_id()})
    print("Comentário criado com sucesso!")
    input("Pressione Enter para continuar...")
    limpar()

def denuncia_por_id(id_denuncia):
    with open("data/denuncias.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            if linha["id_denuncia"] == id_denuncia:
                return linha["descricao"]

def read_comentarios():
    print("┌───────────────────────────────────────────────────────┐")
    print("│                  Comentários no sistema               │")
    print("└───────────────────────────────────────────────────────┘")
    print("┌─────────────────┬─────────────────┬───────────────────┐")
    print("│       ID        │    Comentário   │      Denuncia     │")
    print("├─────────────────┼─────────────────┼───────────────────┤")
    with open("data/comentarios.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            print("│",linha["id_comentario"]," "*(14-len(linha["id_comentario"])),"│",linha["comentario"]," "*(14-len(linha["comentario"])),"│",denuncia_por_id(linha["id_denuncia"])," "*(20-len(denuncia_por_id(linha["id_denuncia"]))),"│")
    print("└─────────────────┴─────────────────┴───────────────────┘")
    input("Pressione Enter para continuar...")
    limpar()

def update_comentario():
    print("┌───────────────────────────────────┐")
    print("│      Atualizar um comentário      │")
    print("└───────────────────────────────────┘")
    id_comentario = input("Digite o ID do comentário que deseja atualizar: ")
    comentario = input("Digite o novo comentário: ")
    with open("data/comentarios.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        comentarios = []
        for linha in leitor:
            if linha["id_comentario"] == id_comentario:
                linha["comentario"] = comentario
                print("Comentário atualizado com sucesso!")
            comentarios.append(linha)
    with open("data/comentarios.csv", "w") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["comentario", "autor", "id_denuncia", "id_comentario"])
        escritor.writeheader()
        for comentario in comentarios:
            escritor.writerow(comentario)

def delete_comentario():
    print("┌───────────────────────────────────┐")
    print("│       Excluir um comentário       │")
    print("└───────────────────────────────────┘")
    id_comentario = input("Digite o ID do comentário que deseja excluir: ")
    with open("data/comentarios.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        comentarios = []
        for linha in leitor:
            if linha["id_comentario"] == id_comentario:
                print("Comentário excluído com sucesso!")
            else:
                comentarios.append(linha)
    with open("data/comentarios.csv", "w") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["comentario", "autor", "id_denuncia", "id_comentario"])
        escritor.writeheader()
        for comentario in comentarios:
            escritor.writerow(comentario)

def main(nome_do_usuario):
    limpar()
    while True:
        print("┌──────────────────────────────────┐")
        print("│           COMENTARIOS            │")
        print("└──────────────────────────────────┘")
        print("┌──────────────────────────────────┐")
        print("│ 1. │ Comentar uma denuncia       │")
        print("│ 2. │ Ver Comentarios             │")
        print("│ 3. │ Editar comentario           │")
        print("│ 4. │ Deletar comentario          │")
        print("│ 0. │ \033[0;31mSair\033[0m                        │")
        print("└──────────────────────────────────┘")

        escolha = input("Digite a opção desejada: ")

        if escolha == "1":
            limpar()
            create_comentario(nome_do_usuario)
        elif escolha == "2":
            limpar()
            read_comentarios()
        elif escolha == "3":
            limpar()
            update_comentario()
        elif escolha == "4":
            limpar()
            delete_comentario()
        elif escolha == "0":
            limpar()
            break
        else:
            opcao_invalida

def opcao_invalida():  
    limpar()
    print("┌──────────────────────────────────────────────────────┐")
    print("│ \033[0;31mOpção inválida\033[0;0m. Por favor, escolha uma opção válida. │")
    print("└──────────────────────────────────────────────────────┘")

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main("Debug")