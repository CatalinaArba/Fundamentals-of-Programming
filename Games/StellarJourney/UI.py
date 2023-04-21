from Service import Service


class UI:
    def __init__(self, board):
        self._game = board
        self._game.place_stars()
        self._game.set_player1()
        for i in range(3):
            self._game.set_player2()


    def main(self):

        print(str(self._game))
        self._game.cheat()
        nr=3
        for i in range(8):
            for j in range(8):
                if self._game.get_cell(i,j)==1:
                    L = i
                    C = j


        while True:
            command = input("enter your command")
            if command == "exit":
                return
            elif command == "cheat":
                self._game.cheat()
                print(str(self._game))
                self._game.uncheat()
            else:
                try:
                    command_word, coordonates = command.split(maxsplit=1, sep=' ')
                    l = int(ord(coordonates[0]) - 65)
                    c = int(ord(coordonates[1]) - 48) - 1
                except ValueError as ve:
                    raise (ve)

                if not (0 <= l <= 7 and 0 <= c <= 7 and len(coordonates) == 2):
                    raise ValueError("Index out of table")
                else:
                    if command_word == "wrap":
                        if not self._game.verification_wrap(l, c):
                            raise ValueError("The coordonates are not valid!")
                        else:
                            L=l
                            C=c
                            continuee = self._game.wrap(l, c)
                            if continuee == 0:
                                print("Game over!")
                                return
                            elif continuee == 1:
                                print("The ship wasn't moved!")
                            else:
                                print(str(self._game))

                    elif command_word == "fire":
                        if not self._game.verification_fire(L,C,l, c):
                            raise ValueError("The coordonates are not valid!")
                        else:
                            if self._game.fire(l,c,nr):
                                nr=nr-1
                                if nr==0:
                                    print("You WON!")
                                    return
                                else:
                                    print("You fired a boat!")
                            else:
                                print("You didn't fire any boat! Try again!")
                            print(str(self._game))

                    else:
                        raise ValueError("Incorrect command")
