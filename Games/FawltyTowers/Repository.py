class Repository:
    def __init__(self):
        self._reservations=[]



    def add(self,reservation):
        self._reservations.append(reservation)

    def index_reservation(self,id):
        i=0
        for res in self._reservations:
            if res.id==id:
                return i
            i+=1
        return -1

    def delete(self,reservation):
        index=self.index_reservation(reservation)
        self._reservations.pop(index)

    def get(self):
        return self._reservations

    def get_item(self,i):
        return self._reservations[i]