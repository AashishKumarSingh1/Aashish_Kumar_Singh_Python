# class -> train : method to book a ticket , get status(no. of seats ), get fare information

class Train_Booking:
    total_seat=1
    def __init__(self):
        # total_seat-=1
        pass
    
    def getStatus(self):
        print(f"The no . of seat left is : {Train_Booking.total_seat} ")

    def book(self):
        if Train_Booking.total_seat>0:
            Train_Booking.total_seat-=1
            print("Seat Booked!")
        else:
            print("All the sets are Booked!")

p1=Train_Booking()

p1.getStatus()
p1.book()
p1.getStatus()
p1.book()
