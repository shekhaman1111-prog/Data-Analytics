# write a class train which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under indian railways.
# from random import randint

# class Train:
#     def __init__(self, trinno):
#         self.trainNo = trainNo

#     def book(self, fro, to):
#         print(f"tickit is booked in train no : {self.trainNo} from {fro} to {to}")
    
#     def getstatus(self):
#         print(f"train no : {self.trainNo} is running on time")

    
#     def getFare(self, fro, to):
#         print(f"tickit is fare in train no : {self.trainNo} from {fro} to {to} is {randint (222, 5555)}")
    
# t = Train(12399)
# t.book("Ramput", "jabalpur")

from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(
            f"Ticket fare in train no: {self.trainNo} "
            f"from {fro} to {to} is ₹{randint(222, 5555)}"
        )


t = Train(12399)

t.book("Rampur", "Jabalpur")
t.getStatus()
t.getFare("Rampur", "Jabalpur")