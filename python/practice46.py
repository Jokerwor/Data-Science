#Can we change self to slf or can we can self to any name
#yes we can but usually we dont do it

from random import randint
class Train:
    def __init__(slf,trainNo):
        slf.trainNo = trainNo

    def book(slf,fro,to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")

    def getStatus(slf):
        print(f"Ticket no: {slf.trainNo} is running on time")

    def getFare(slf,fro,to):
        print(f"Ticket fare in train no: {slf.trainNo} from {fro} to {to} is: {randint(222,5555)}")

t = Train(12345)
t.book("Varanasi","Delhi")

t.getStatus()

t.getFare("Varanasi","Delhi")