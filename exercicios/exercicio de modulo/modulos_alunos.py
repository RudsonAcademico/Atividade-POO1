class Turma():
    def __init__(self, *alunos):
        """
        Cria turmas com um numero variavel de alunos mas não permite a listagem de alunos com nomes repetidos 
        """
        self.alunos = list(alunos)
    
    def listar(self):
        """"
        Exibe a lista de alunos linha por linha
        """
        for aluno in self.alunos:
            print(aluno)

turma1 = Turma("Ana", "Bruno","Carlos")
turma2 = Turma("Larissa")


turma1.listar()
turma2.listar()