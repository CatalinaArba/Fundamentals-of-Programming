from domain import Question
from domain_quiz import Quiz
from textfilerepository import TextFileRepository
class Service:
    def __init__(self,repo,repo2):
        self._questions=repo
        self._quizes=repo2


    def add(self,parameters):
        data=parameters.split(maxsplit=6,sep=";")
        question=Question(int(data[0]),data[1],data[2],data[3],data[4],int(data[5]),data[6])
        self._questions.add(question)

    def create(self,parameters):
        data = parameters.split(maxsplit=2, sep=";")
        ok = TextFileRepository(data[0],int(data[1]),data[2])
        if ok==1:
            quiz = Quiz(data[0], data[1], data[2])
            self._quizes.add(quiz)
        return ok
