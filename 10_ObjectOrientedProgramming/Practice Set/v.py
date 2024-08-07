"""
Write a class Train which has methods to book a ticket, 
get status (no of seats ) and get fare information of train running 
under Indian Railways
"""
class Train:
    def __init__(self):
        self.seats=78
        self.fare=190
    def bookTicket(self):
        self.seats-=1
    def getStatus(self):
        print(self.seats)
    def fareInfo(self):
        print(self.fare)

passenger1=Train()
passenger1.bookTicket()
passenger1.getStatus()
passenger1.fareInfo()