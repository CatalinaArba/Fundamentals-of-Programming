from textfilerepositroy import TextFileRepository
from  UI import Ui
from service import Service
sentence=TextFileRepository()
service=Service(sentence)
ui=Ui(service)
Ui.main(ui)
"""
anna has apples
patricia has pears
cars are fast
planes are quick
the quick brown fox jump over the lazy dog
"""