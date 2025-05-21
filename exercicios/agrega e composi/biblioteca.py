class Livro():
    def __init__(self, titulo, volume):
        self.titulo = titulo
        self.volume = volume

class Membro():
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

class Emprestimo():
    def __init__(self, livro, membro):
        self.livro_emprestado = livro
        self.membro = membro 

class Categoria():
    def __init__(self, nome_da_categoria):
        self.nome_da_categoria = nome_da_categoria



class Biblioteca():
    def __init__(self):
        self.categorias = []
        self.membros = []
        self.emprestimos = []
    
    def adicionar_membro(self, membro):
        self.membros.append(membro)

    def adicionar_categoria(self, nome_da_categoria):
        categoria = Categoria(nome_da_categoria)
        self.categorias.append(categoria)

    def adicionar_emprestimo(self, livro, membro):
        emprestimo = Emprestimo(livro, membro)
        self.emprestimos.append(emprestimo)
    

carvao = Livro("Espadachim de Carvão", 1)
membro1 = Membro("Jorge")
membro1.adicionar_livro(carvao)

biblioteca1 = Biblioteca()
biblioteca1.adicionar_membro(membro1)
biblioteca1.adicionar_categoria("Aventura")
biblioteca1.adicionar_emprestimo(carvao, membro1)
