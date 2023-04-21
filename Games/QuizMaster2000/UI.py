class Ui:
    def __init__(self,service):
        self._controller=service

    def main(self):
        while True:
            n=input("Enter your command:")
            command_word,parameters=n.split(maxsplit=1,sep=' ')
            if command_word=="add":
                self.add(parameters)
            elif command_word=="start":
                pass
            elif command_word=="create":
                self.create(parameters)
            elif command_word=="exit":
                return
            else:
                print("Error:invalid command!")

    def add(self,parameters):
        self._controller.add(parameters)

    def create(self,parameters):
        try:
            data = parameters.split(maxsplit=2, sep=";")
            self._controller.create(parameters)
        except ValueError as ve:
            print(ve)

