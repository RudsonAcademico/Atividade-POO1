class Livro():
    def __init__(self, titulo, autor, paginas=100):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

livro1 = Livro("Python Basico", "João Silva", 250)
livro2 = Livro("Aprendendo Lógica", "Maria Souza")
print(livro1.titulo, livro1.autor, livro1.paginas)
print(livro2.titulo, livro2.autor, livro2.paginas)
