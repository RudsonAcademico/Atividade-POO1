class Livro():
    def __init__(self, titulo, volume):
        self.titulo = titulo
        self.volume = volume

class Membro():
    def __init__(self, nome):
        self.nome = nome

class Emprestimo():
    def __init__(self, livro, data_do_emprestimo):
        self.livro_emprestado = livro
        self.data = data_do_emprestimo

class Categoria():
    def __init__(self):
        self.livros_na_categoria = []
    
    def adicionar_na_categoria(self, livro):
        self.livros_na_categoria.append(livro)


class Biblioteca():
    def __init__(self):
        self.categorias = []
        self.membros = []
        self.emprestimos = []
    
    def adicionar_membro(self, nome_do_membro):
        membro = Membro(nome_do_membro)
        self.membros.append(membro)

    def adicionar_categoria(self, nome_da_categoria):
        categoria = Categoria(nome_da_categoria)
        self.categorias.append(categoria)

    def adicionar_emprestimo(self, livro, data_do_emprestimo):
        emprestimo = Emprestimo(livro, data_do_emprestimo)
        self.emprestimos.append(emprestimo)
    
