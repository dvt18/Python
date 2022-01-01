class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers=[]

    def add_passenger(self, name):
        if not self.open_seats():
            return False 
        self.passengers.append(name)    
        return True

    def open_seats(self):
        return self.capacity-len(self.passengers)


flight = Flight(3)


people = ["Dushyant", "Kunal", "Amaan", "Bharat","mahesh"]
for i in people:
    success= flight.add_passenger(i)
    if success:
        print(f"Added {i} to the flight successfully. ")
    else:
        print(f" SORRY!! No available seats for {i}. ")
