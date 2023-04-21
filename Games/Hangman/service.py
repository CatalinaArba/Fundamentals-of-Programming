import random

from doman_letter import Letter
from repository import Sentence


class Service:
    def __init__(self, list):
        # self._sentence = sentence
        self._selected_sentence = 0
        self._list = list

    def __str__(self):
        return  str(self._sentence)

    def verification_new_sentence(self, s):
        if len(s) < 3:
            print("len")
            return False
        list1 = list(s)
        nr_words = 0
        last_space = -1
        nr = 1
        for i in list1:
            if i == ' ':
                if last_space == -1:
                    v = nr
                    nr_words = 1
                else:
                    nr_words += 1
                    v = nr - last_space
                if v < 3:
                    print(nr)
                    return False
                last_space = nr

            nr += 1

        list1 = self._list.getall()
        nr = 0
        for i in list1:
            if self._list.str_index(nr) == s:
                return False
            nr += 1
        return True

    def add(self, s):
        """
        Add a new sentence to the list
        :param s:
        :return:
        """
        sentence = []
        for l in s:
            sentence.append(Letter(l))
        self._list.add(s)

    def select_sentence(self):
        max = len(self._list)
        nr = random.randint(0, max - 2)
        self._selected_sentence = nr
        self._sentence = Sentence(self._list.get_item(nr))
        return nr

    def new_game(self):
        i = self._selected_sentence
        # print(self._sentence.str_index(self._selected_sentence))
        max = len(self._sentence)  # how many letters in the sentamce
        for j in range(max):
            element = self._list.get_double_item(i, j)
            if element.letter==' ':
                self._sentence.set_item(j, 1)
            if j != 0:
                before = self._list.get_double_item(i, j - 1)
                if str(before) == ' ':
                    self._sentence.set_item( j, 1)
            else:
                self._sentence.set_item( j, 1)

            if j != max - 1:
                next = self._list.get_double_item(i, j + 1)
                if str(next) == " ":
                    self._sentence.set_item( j, 1)
            else:
                self._sentence.set_item( j, 1)


        self.message()

    def round(self,letter):
        max = len(self._sentence)  # how many letters in the sentamce
        ok=0
        for j in range(max):
            element=self._sentence.get_index(j)
            if str(element)==letter:
                self._sentence.set_item(j, 1)
                ok=1
        return ok

    def win(self):
        max = len(self._sentence)
        for j in range(max):
            element=self._sentence.get_index(j)
            if element.visible==0:
                return False
        return True

    def reset_elements(self):
        max = len(self._sentence)
        for j in range(max):
            element = self._sentence.get_index(j)
            element.set_visible(0)

    def message(self):
        message = ""
        i = self._selected_sentence
        max = len(self._sentence)  # how many letters in the sentamce
        for j in range(max):
            element = self._sentence.get_index(j)
            if element.visible == 1:
                message += str(element)
            else:
                message += "_"
        return message
