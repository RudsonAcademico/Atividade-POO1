class Livro():
    def __init__(self, titulo, autor, isbn, copias_totais):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.copias_totais = copias_totais
        self.__copias_disponiveis = 0
        self.__emprestimos = []

        def get_emprestimos(self):
            return self.__emprestimos
        
        def emprestar(self):
            if self.get_disponibilidade()>0:
                self.__emprestimo.append("Livro")
                return "Livro emprestado"
            else:
                print(f"Não há livro disponivel para emprestimo")

        def devolver(self, emprestimo):
            self.__emprestimos.remove(emprestimo)

        def get_disponibilidade(self):
            return self.copias_totais - len(self.__emprestimo)

