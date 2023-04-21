class Ui:
    def __init__(self,sentence):
        self._sentence=sentence
        self._selected_sentence = 0

    def main(self):
        while True:

            self.print_menu()
            n=int(input("Enter your option:"))
            if n==0:
                return
            elif n==1:
                self.add()
            elif n==2:
                self.game()

            print(str(self._sentence))



    def print_menu(self):
        print("0-Exit the app")
        print("1-Add a new sentence")
        print("2-Start the game")

    def add(self):
        sentence=input("Enter the new sentence:")
        if not self._sentence.verification_new_sentence(sentence):
            print("Error:the entered sentence is not valid!")
        else:
            self._sentence.add(sentence)
            print("The sentence was added successfully! ")

    def game(self):

        self._selected_sentence=self._sentence.select_sentence()
        message=self._sentence.new_game()
        print(str(self._sentence))
        print(self._sentence.message())
        mistakes=0
        while True:
            if mistakes==7:
                self.Hangman(mistakes)
                print("You lost!")
                return
            elif self._sentence.win():
                print("You won!")
                self._sentence.reset_elements()
                return
            else:
                letter=input("Enter the letter:")
                ok=self._sentence.round(letter)
                if ok==0:
                    mistakes+=1
                print(self._sentence.message())
                self.Hangman(mistakes)

    def Hangman(self,nr):
        message = "Hangman"
        text=""
        for i in range(nr):
            text+=message[i]
        print(text)
