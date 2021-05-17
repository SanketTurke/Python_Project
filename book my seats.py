from threading import *


class bookMySeats():
    def __init__(self, availableSeats):
        self.availableseats = availableSeats
        self.l = Lock()

    def buy(self,SeatsRequired):
        self.l.acquire()
        if (self.availableseats>=SeatsRequired):
            print("Seats Available Are",self.availableseats)
            print("Seat confirmed")
            print("Payment Received")
            print("printing the ticket..")
            self.availableseats -= SeatsRequired

        else:
            print("sorry. no seats available")
            self.l.release()


obj = bookMySeats(10)
t = Thread(target=obj.buy,args=(3,))
t.start()


t1 = Thread(target=obj.buy,args=(4,))
t1.start()


t2 = Thread(target=obj.buy,args=(3,))
t2.start()
