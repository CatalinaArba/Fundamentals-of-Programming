import copy
from doman_letter import Letter

class Sentence:
    def __init__(self,sentence):
        self._sentence=[]
        for l in sentence:
            letter=Letter(copy.deepcopy(l))
            self._sentence.append(letter)

    def __len__(self):
        return len(self._sentence)

    def __str__(self):
        message=""
        for i in self._sentence:
            message+=str(i)
        return message

    def get_all(self):
        return self._sentence

    def get_index(self,index):
        return self._sentence[index]

    def set_item(self,index,value):
        letter=self.get_index(index)
        letter.set_visible(value)