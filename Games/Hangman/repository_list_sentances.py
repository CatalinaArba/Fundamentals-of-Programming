class ListSentences:
    def __init__(self):
        self._list=[]

    def add(self,sentence):
        self._list.append(sentence)

    def getall(self):
        return self._list

    def __str__(self):
        text = ""
        for i in self._list:
            for l in i:
                text += str(l)
            text+="\n"
        return text

    def __len__(self):
        return len(self._list)

    def lenght(self,index):
        return len(self._list[index])

    def set_visiblility(self,index,index2,value):
        self._list[index][index2].visible(value)

    def str_index(self,index):
        text=""
        for l in self._list[index]:
            text += str(l)
        return text

    def get_item(self,index):
        return self._list[index]

    def get_double_item(self,i,j):
        return self._list[i][j]