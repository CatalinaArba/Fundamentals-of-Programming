import copy
import random
from Domain import Reservation


class Service:
    def __init__(self, rooms, reservations):
        self._rooms = rooms
        self._reservations = reservations

    def create(self, name, type, guests, ad, am, dd, dm):
        ok = 1
        while ok:
            id = random.randint(1000, 9999)
            if self._reservations.index_reservation(id) == -1:
                ok = 0
        list = self.find_type(type)
        for room in list:
            if self.find_reservation_nr(room, ad, am, dd, dm):
                self._reservations.add(Reservation(id, room, name, guests, ad, am, dd, dm))
                return 1
        return 0

    def find_type(self, type):
        rooms = self._rooms.get()
        list = []
        for room in rooms:
            if room.type == type:
                list.append(room.nr)

        return list

    def find_reservation_nr(self, nr, ad, am, dd, dm):
        res = self._reservations.get()
        for i in res:
            if i.nr == nr:
                if i.dm * 100 + i.dd >= am * 100 + ad and i.am * 100 + i.ad <= dm * 100 + dd:
                    return False
        return True

    def get_reservations(self):
        return self._reservations.get()

    def find_reservation_id(self, id):
        return self._reservations.index_reservation(id)

    def delete_reservation(self, n):
        self._reservations.delete(n)

    def available_date(self, ad, am, dd, dm):
        list = []
        for i in range(1, 6):
            if self.find_reservation_nr(i, ad, am, dd, dm):
                list.append(self._rooms.get_by_nr(i))
        return list

    def monthly_report(self):
        list = [[0, "January"], [0, "February"], [0, "March"], [0, "April"], [0, "May"], [0, "June"], [0, "July"],
                [0, "August"], [0, "September"], [0, "October"], [0, "November"], [0, "December"]]
        res = self._reservations.get()
        for r in res:
            if r.am == r.dm:
                nr = r.dd - r.ad
                list[r.am - 1][0] += nr
            else:
                if r.am % 2 == 1:  # luna cu 31 zile
                    nr1 = 32 - r.ad
                    nr2 = r.dd - 1
                    list[r.am - 1][0] += nr1
                    list[r.dm - 1][0] += nr2
                elif r.am == 0 and r.am != 2:
                    nr1 = 31 - r.ad
                    nr2 = r.dd - 1
                    list[r.am - 1][0] += nr1
                    list[r.dm - 1][0] += nr2
                elif r.am == 2:
                    nr1 = 29 - r.ad
                    nr2 = r.dd - 1
                    list[r.am - 1][0] += nr1
                    list[r.dm - 1][0] += nr2
        for i in range(12):
            for j in range(12):
                if list[i][0] > list[j][0]:
                    list[i], list[j] = list[j], list[i]

        # sorted(list, key=lambda x: x[0], reverse=True)
        return list

    def days_report(self):
        list = [[0, "Monday"], [0, "Tuesday"], [0, "Wednesday"], [0, "Thursday"], [0, "Friday"], [0, "Saturday"],
                [0, "Sunday"]]
        list2 = copy.deepcopy(list)
        message = ""
        d = 1
        m = 1
        day = 0
        ok = 1
        nr2=1
        while ok:
            if m == 12 and d==32 or m==13 :
                return message
            else:
                if m % 2 == 1 and d == 31:
                    m += 1
                    d = 1
                elif m % 2 == 0 and d == 30 and m != 2:
                    m += 1
                    d = 1
                elif m == 2 and d == 28:
                    m += 1
                    d = 1
                else:
                    d+=1

                nr = 0
                res = self._reservations.get()
                for r in res:
                    if r.am==m or r.dm==m:
                        if  r.am==r.dm and r.ad<=d<r.dd:
                            nr += 1
                        elif r.am!=r.dm:
                            if r.ad<=d and m==r.am or d<r.dd and m==r.dm:
                                nr += 1



                #print(d, m, day,nr)
                if day == 7:
                    message2=""
                    for i in range(7):
                        for j in range(7):
                            if list[i][0] > list[j][0]:
                                list[i], list[j] = list[j], list[i]
                    for i in range(7):
                        message +=str( list[i][1])+str(list[i][0])+" "
                    message += '\n'
                    #print(str(nr2),message2)
                    nr2+=1
                    day = 0
                    list = copy.deepcopy(list2)


                list[day][0] = nr
                day = day + 1

