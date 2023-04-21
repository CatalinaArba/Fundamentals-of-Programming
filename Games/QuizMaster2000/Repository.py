class Repository:
    def __init__(self):
        self._repo=[]

    def add(self,question):
        self._repo.append(question)

    def get_all(self):
        return self.get_all()