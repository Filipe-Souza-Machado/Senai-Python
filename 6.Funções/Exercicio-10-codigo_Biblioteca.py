import os;

os.system("cls || clear");

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.emprestimos = {}  # Dicionário para rastrear empréstimos

    def cadastrar_livro(self, livro_id, titulo, autor):
        self.livros[livro_id] = {'titulo': titulo, 'autor': autor}

    def consultar_livro(self, livro_id):
        if livro_id in self.livros:
            return self.livros[livro_id]
        else:
            return "Livro não encontrado."

    def registrar_emprestimo(self, livro_id, usuario_id):
        if livro_id in self.livros:
            # Verifique se o livro já está emprestado
            if livro_id in self.emprestimos:
                return "Livro já emprestado."
            else:
                # Registre o empréstimo
                self.emprestimos[livro_id] = {'usuario_id': usuario_id}
                return "Empréstimo registrado com sucesso."
        else:
            return "Livro não encontrado."

    def registrar_devolucao(self, livro_id, usuario_id):
        if livro_id in self.livros:
            # Verifique se o livro está emprestado
            if livro_id in self.emprestimos:
                # Marque o livro como devolvido
                del self.emprestimos[livro_id]
                return "Devolução registrada com sucesso."
            else:
                return "Livro não está emprestado."
        else:
            return "Livro não encontrado."

    def exibir_menu(self):
        print("=== Menu da Biblioteca ===")
        print("1. Cadastrar Livro")
        print("2. Consultar Livro")
        print("3. Registrar Empréstimo")
        print("4. Registrar Devolução")
        print("0. Sair")

    def executar(self):
        while True:
            self.exibir_menu()
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                livro_id = int(input("ID do livro: "))
                titulo = input("Título do livro: ")
                autor = input("Autor do livro: ")
                self.cadastrar_livro(livro_id, titulo, autor)
                print("Livro cadastrado com sucesso!")
            elif opcao == 2:
                livro_id = int(input("ID do livro: "))
                print(self.consultar_livro(livro_id))
            elif opcao == 3:
                livro_id = int(input("ID do livro: "))
                usuario_id = int(input("ID do usuário: "))
                print(self.registrar_emprestimo(livro_id, usuario_id))
            elif opcao == 4:
                livro_id = int(input("ID do livro: "))
                usuario_id = int(input("ID do usuário: "))
                print(self.registrar_devolucao(livro_id, usuario_id))
            elif opcao == 0:
                print("Encerrando o sistema. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")

# Exemplo de uso
biblioteca = Biblioteca()
biblioteca.executar()
