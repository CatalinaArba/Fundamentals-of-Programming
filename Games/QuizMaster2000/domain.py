class Question:
    def __init__(self,id,text,a,b,c,correct,difficulty):
        self._id=id
        self._text=text
        self._a=a
        self._b=b
        self._c=c
        self._correct=correct
        self._difficulty=difficulty

    def __str__(self):
        return str(self._id)+". "+str(self._text)+":"+str(self._a)+" "+str(self._b)+" "+str(self._c)+" "+str(self._difficulty)

    @property
    def id(self):
        return self._id

    @property
    def text (self):
        return self._text

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    @property
    def correct(self):
        return self._correct

    @property
    def difficulty(self):
        return self._difficulty