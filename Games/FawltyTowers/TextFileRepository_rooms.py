from Repository_rooms import Repository_rooms
from Domain_rooms import Room
class TextFileRepositoryRoom(Repository_rooms):
    def __init__(self):
        super().__init__()
        self._file_name="rooms.txt"
        self._load()

    def _load(self):
        f=open(self._file_name,"rt")
        for line in f.readlines():
            data=line.split(maxsplit=1,sep=',')
            nr=int(data[0])
            type=int(data[1])
            room=Room(nr,type)
            self.add_room(room)
        f.close()

    def add_room(self,room):
        super(TextFileRepositoryRoom,self).add_room(room)
