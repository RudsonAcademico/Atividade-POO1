class Aluno:
    def __init__(self):
        self.__nome = ""
        self.__matricula = ""
        self.__media = 0

    @property
    def nome(self):
        return self.__nome
            
    @property
    def matricula(self):
        return self.__matricula
      
    @property
    def media(self):
        return self.__media
            
    @nome.setter
    def nome(self, nome):
        if not nome or nome == " ":
            print("Valor invalido pra nome")
            self.__nome = "Enzo"
        else:
            self.__nome = nome

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula


    @media.setter
    def media(self, media):
        if media < 0 or media > 100:
            print("Media invalida")
            self.__media = 0
        else:
            self.__media = media


aula = Aluno()
aula.matricula = 100231
aula.media = 90
aula.nome = "Steve"

print(f"O Aluno {aula.nome} com a matricula {aula.matricula}, esta com {aula.media} pontos de media")