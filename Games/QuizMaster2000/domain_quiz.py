class Quiz:
    def __init__(self,file_name,nr,difficulty):
        self._difficulty=difficulty
        self._nr=nr
        self._file_name=file_name

    def __str__(self):
        return str(self._difficulty)+" "+str(self._nr)+" "+str(self._file_name)

    @property
    def difficulty(self):
        return self._difficulty

    @property
    def nr(self):
        return self._nr

    @property
    def file_name(self):
        return self._file_name