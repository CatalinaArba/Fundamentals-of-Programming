class UI:
    def __init__(self,controller):
        self._controller=controller

    def main(self):
        self.print_list()
        while True:
            n=int(input("Enter your command:"))
            if n==0:
                return
            if n==1:
                self.create1()
                self.print_list()
            if n==2:
                self.delete2()
                self.print_list()
            if n==3:
                self.available_rooms()
            if n==4:
                self.monthly_report()
            if n==5:
                self.daily()

    def print_list(self):
        reservations=self._controller.get_reservations()
        for i in reservations:
            print(str(i))

    def print_menu(self):
        print("0-Exit the program")
        print("1-Create a room reservation")
        print("2-Delete reservation")
        print("3-Show available rooms")
        print("4-Monthly report")

    def create1(self):
        name=input("Enter the family name:")
        room_type=int(input("Enter the room type(1/2/4):"))
        guests=int(input("Enter the number of guests:"))
        ad=int(input("Enter the arrival day:"))
        am = int(input("Enter the arrival mouth:"))
        dd = int(input("Enter the departure day:"))
        dm = int(input("Enter the departure mouth:"))
        if guests<1 or guests>4 :
            print("Error:invalid guest!")
        elif len(name)<1:
            print("Error:invalid name!")
        elif dm*100+dd<am*100+ad:
            print("Error:invalid dates!")
        else:
            ok=self._controller.create(name,room_type,guests,ad,am,dd,dm)
            if ok==1:
                print("The reservation was done successfully!")
            else:
                print("We couldn't do the reservation!")

    def delete2(self):
        n=int(input("Enter the reservation id:"))
        ok=self._controller.find_reservation_id(n)
        if ok==-1:
            print("Error:We couldn't delete a reservation that doesn't exist!")
        else:
            self._controller.delete_reservation(n)
            print("The reservation was deleted successfully!")

    def available_rooms(self):
        n=input("Enter the dates:")
        dates=n.split(maxsplit=1,sep="-")
        arrival=dates[0].split(maxsplit=1,sep=".")
        departure = dates[1].split(maxsplit=1, sep=".")
        list=self._controller.available_date(int(arrival[0]),int(arrival[1]),int(departure[0]),int(departure[1]))
        for i in list:
            print(str(i))
        if len(list)==0:
            print("There is no available room in that period!")

    def monthly_report(self):
        list=self._controller.monthly_report()
        for l in list:
            print(str(l[0]),l[1])

    def daily(self):
        message=self._controller.days_report()
        print(message)
