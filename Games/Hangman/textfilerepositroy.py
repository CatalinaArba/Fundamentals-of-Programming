import copy
import random
from doman_letter import Letter
from repository_list_sentances import ListSentences


class TextFileRepository(ListSentences):
    def __init__(self):
        super().__init__()
        self._filename = "sentence.txt"
        self._load()

    def _load(self):
        f = open(self._filename, "rt")
        for line in f.readlines():
            sentance = []
            nr = 1
            for l in line:
                if nr != len(line):
                    sentance.append(Letter(l))
                nr += 1
            nr += 1
            self.add(sentance)
        f.close()

    def _save(self):
        f = open(self._filename, "wt")
        sentances=self.getall()
        for line in sentances:
            text = ""
            for i in line:
                text += str(i)
            text += '\n'
            f.write(text)
        f.close()

    def add(self, item):
        super(TextFileRepository, self).add(item)
        self._save()

    def set_visiblility(self,index,index2,value):
        super(TextFileRepository, self).set_visiblility(index,index2,value)
        self._save()