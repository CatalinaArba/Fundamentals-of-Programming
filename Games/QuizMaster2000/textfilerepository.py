from domain import Question
from Repository import Repository
class TextFileRepository(Repository):
    def __init__(self,file_name,difficulty,nr):
        super().__init__()
        self._filename=file_name
        self._diffficulty=difficulty
        self._nr=nr
        ok=self._load()
        return ok

    def _load(self):
        f = open(self._filename, "rt")
        nr_q=0
        nr_difficulty=0
        for line in f.readlines():
            nr_q+=1
            data = line.split(maxsplit=6, sep=',')
            if data[6]==self._diffficulty:
                nr_difficulty+=1
        if nr_q!=self._nr:
            return 0
        if nr_difficulty<self._nr/2:
            return 0
        f.close()
        f=open(self._filename,"rt")
        for line in f.readlines():
            data=line.split(maxsplit=6,sep=',')
            question=Question(int(data[0]),data[1],data[2],data[3],data[4],int(data[5]),data[6])
            self.add(question)
        f.close()
        return 1

    def _save(self):
        f=open(self._filename,"wt")
        data=self.get_all()
        for q in data:
            text=""
            text+=q[0]+","+q[1]+","+q[2]+","+q[3]+","+q[4]+","+q[5]+","+q[6]+"\n"
            f.write(text)
        f.close()

    def add(self,question):
        super(TextFileRepository,self).add(question)
        self._save()
