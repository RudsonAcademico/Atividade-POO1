class Turma:
    def __init__(self, *alunos):
        """
        Cria turmas com um numero variavel de alunos mas não permite a listagem de alunos com nomes repetidos 
        """
        self.alunos = list(alunos)

turma1 = Turma("Ana", "Bruno","Carlos")
turma2 = Turma("Larissa")


print(turma1.alunos)
print(turma2.alunos)