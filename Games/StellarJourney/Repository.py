from texttable import Texttable


class Repository:
    def __init__(self):
        self._board = [[0 for i in range(0, 8)] for j in range(0, 8)]

    def __str__(self):
        t = Texttable()
        row = []

        for i in range(9):
            row.append(str(i))
        t.add_row(row)
        for i in range(8):
            row = []
            row.append(chr(65 + i))
            for j in range(8):
                if self._board[i][j] == 0 or self._board[i][j] == 2 :
                    row.append(" ")
                elif self._board[i][j] == 5:
                    row.append("*")
                elif self._board[i][j] == 1 :
                    row.append("E")
                elif self._board[i][j] == 3:
                    row.append("B")
            t.add_row(row)
        return t.draw()

    def set(self, l, c, nr):
        self._board[l][c] = int(nr)

    def get_cell(self, l, c):
        return self._board[l][c]

    def get_board(self):
        return self._board
