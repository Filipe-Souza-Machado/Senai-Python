import os

os.system("cls || clear")

def criar_biblioteca():
    livros = {}
    emprestimos = {}  # Dicionário para rastrear empréstimos
    return livros, emprestimos

def cadastrar_livro(livros, livro_id, titulo, autor):
    livros[livro_id] = {'titulo': titulo, 'autor': autor}

def consultar_livro(livros, livro_id):
    if livro_id in livros:
        return livros[livro_id]
    else:
        return "Livro não encontrado."

def registrar_emprestimo(livros, emprestimos, livro_id, usuario_id):
    if livro_id in livros:
        # Verifique se o livro já está emprestado
        if livro_id in emprestimos:
            return "Livro já emprestado."
        else:
            # Registre o empréstimo
            emprestimos[livro_id] = {'usuario_id': usuario_id}
            return "Empréstimo registrado com sucesso."
    else:
        return "Livro não encontrado."

def registrar_devolucao(livros, emprestimos, livro_id, usuario_id):
    if livro_id in livros:
        # Verifique se o livro está emprestado
        if livro_id in emprestimos:
            # Marque o livro como devolvido
            del emprestimos[livro_id]
            return "Devolução registrada com sucesso."
        else:
            return "Livro não está emprestado."
    else:
        return "Livro não encontrado."

def exibir_menu():
    print("=== Menu da Biblioteca ===")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Registrar Empréstimo")
    print("4. Registrar Devolução")
    print("0. Sair")

def executar(biblioteca):
    livros, emprestimos = biblioteca
    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            livro_id = int(input("ID do livro: "))
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            cadastrar_livro(livros, livro_id, titulo, autor)
            print("Livro cadastrado com sucesso!")
        elif opcao == 2:
            livro_id = int(input("ID do livro: "))
            print(consultar_livro(livros, livro_id))
        elif opcao == 3:
            livro_id = int(input("ID do livro: "))
            usuario_id = int(input("ID do usuário: "))
            print(registrar_emprestimo(livros, emprestimos, livro_id, usuario_id))
        elif opcao == 4:
            livro_id = int(input("ID do livro: "))
            usuario_id = int(input("ID do usuário: "))
            print(registrar_devolucao(livros, emprestimos, livro_id, usuario_id))
        elif opcao == 0:
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Exemplo de uso
biblioteca = criar_biblioteca()
executar(biblioteca)