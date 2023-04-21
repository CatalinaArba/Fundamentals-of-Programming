class Room:
    def __init__(self,nr,type):
        self._nr=nr
        self._type=type

    def __str__(self):
        return "Room number:"+str(self.nr)+" Room type:"+str(self._type)

    @property
    def nr(self):
        return self._nr

    @property
    def type(self):
        return self._type
