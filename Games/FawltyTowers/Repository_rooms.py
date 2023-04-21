class Repository_rooms:
    def __init__(self):
        self._rooms=[]

    def add_room(self,room):
        self._rooms.append(room)

    def get(self):
        return self._rooms

    def get_item(self,i):
        return self._rooms[i]

    def get_by_nr(self,nr):
        for i in self._rooms:
            if i.nr==nr:
                return i
        return None

