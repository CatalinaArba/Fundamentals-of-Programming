import random
import random


class Service:
    def __init__(self, board):
        self._board = board

    def __str__(self):
        return str(self._board)

    def set(self, l, c, v):
        self._board.set(l, c, v)

    def place_stars(self):
        nr = 0  # numbers of stars
        while nr != 10:
            line = random.randint(0, 7)
            column = random.randint(0, 7)
            if self.verifications_coodonates(line, column):
                nr += 1
                self.set(line, column, 5)
        return

    def verifications_coodonates(self, l, c):
        for i in range(0, 8):
            for j in range(0, 8):
                b = self._board.get_cell(i, j)
                if b == 5:
                    if (l == i and c == j) or (l == i and c == j - 1) or (l == i and c == j + 1) or (
                            l == i - 1 and c == j) or (l == i + 1 and c == j) or ((l == i - 1 and c == j - 1)) or (
                            l == i - 1 and c == j + 1) or (l == i + 1 and c == j - 1) or (l == i + 1 and c == j + 1):
                        return False
        return True

    def set_player1(self):
        while True:
            line = random.randint(0, 7)
            column = random.randint(0, 7)
            if self._board.get_cell(line, column) == 0:
                print(line,column)
                self._board.set(line, column, 1)
                return

    def set_player2(self):
        while True:
            line = random.randint(0, 7)
            column = random.randint(0, 7)
            ok = 1
            if self._board.get_cell(line, column) == 0:
                for i in range(line - 1, line + 2):
                    for j in range(column - 1, column + 2):
                        if i >= 0 and j >= 0 and i != j and i <= 7 and j <= 7:
                            if not (self._board.get_cell(i, j) == 1 or self._board.get_cell(i, j) == 0):
                                ok = 0
            if ok == 1:
                self.set(line, column, 2)
                return

    def cheat(self):
        for i in range(8):
            for j in range(8):
                if self._board.get_cell(i, j) == 2:
                    self._board.set(i, j, 3)

    def uncheat(self):
        for i in range(8):
            for j in range(8):
                if self._board.get_cell(i, j) == 3:
                    self._board.set(i, j, 2)

    def wrap(self, l, c):
        if self._board.get_cell(l, c) == 3 or self._board.get_cell(l,c)==2:
            return 0
        if self._board.get_cell(l, c) == 5:
            return 1  # not moved
        else:
            for i in range(8):
                for j in range(8):
                    if self._board.get_cell(i, j) == 1:
                        self._board.set(i, j, 0)
            self._board.set(l, c, 1)
            return 2

    def verification_wrap(self, l, c):
        for i in range(8):
            for j in range(8):
                if self._board.get_cell(i, j) == 1:
                    if l == i or c == j or l + c == i + j or l - c == i - j:
                        return True
                    return False

    def verification_fire(self, i, j, l, c):
        if (l == i and c == j) or (l == i and c == j - 1) or (l == i and c == j + 1) or (l == i - 1 and c == j) or (
                l == i + 1 and c == j) or ((l == i - 1 and c == j - 1)) or (
                l == i - 1 and c == j + 1) or (l == i + 1 and c == j - 1) or (l == i + 1 and c == j + 1):
            return True
        return False

    def fire(self,l,c,nr):
        if self._board.get_cell(l,c)==3 or self._board.get_cell(l,c)==2:
            for i in range(8):
                for j in range(8):
                    if self.get_cell(i,j)==2 or self.get_cell(i,j)==3:
                        self._board.set(i,j,0)
            for i in range(nr-1):
                self.set_player2()
            return True
        return False

    def get_cell(self,l,c):
        return self._board.get_cell(l,c)
