from Domain import Reservation
from Repository import Repository
class TextFileRepository(Repository):
    def __init__(self):
        super().__init__()
        self._file_name="reservations.txt"
        self._load()

    def _load(self):
        f=open(self._file_name,"rt")
        for line in f.readlines():
            data=line.split(maxsplit=5,sep=',')
            id=int(data[0])
            nr=int(data[1])
            name=data[2]
            guests=int(data[3])

            dates_a=data[4].split(maxsplit=1,sep='.')
            ad=int(dates_a[0])
            am = int(dates_a[1])

            dates_d=data[5].split(maxsplit=1,sep='.')
            dd = int(dates_d[0])
            dm = int(dates_d[1])
            reservation=Reservation(id,nr,name,guests,ad,am,dd,dm)
            self.add(reservation)
        f.close()

    def _save(self):
        f=open(self._file_name,"wt")
        res=self.get()
        for i in res:
            text=""
            text+=str(i.id)+","+str(i.nr)+","+str(i.name)+","+str(i.guests)+","+str(i.ad)+"."+str(i.am)+","+str(i.dd)+"."+str(i.dm)+"\n"
            f.write(text)
        f.close()




    def add(self,reservation):
        super(TextFileRepository,self).add(reservation)
        self._save()

    def delete(self,reservation):
        super(TextFileRepository, self).delete(reservation)
        self._save()

