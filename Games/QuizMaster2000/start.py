from Repository import Repository
from textfilerepository import TextFileRepository
from repository_quiz import RepositoryQuiz
from service import Service
from UI import Ui
repo=TextFileRepository()
repo2=RepositoryQuiz()
service=Service(repo,repo2)
ui=Ui(service)
Ui.main(ui)
