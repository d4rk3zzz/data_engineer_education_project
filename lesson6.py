class Human:
    hands = 2
    legs = 2
    head = 1

    def __init__(self, h_name, h_age, h_location):
        self.name = h_name
        self.age = h_age
        self.location = h_location

    def get_info(self):
        print("Name:", self.name)
        print("Age is", self.age)
        print("Legs:", self.legs, "Hands:", self.hands, "Head:", self.head)
        print("Location is:", self.location)
    def __repr__(self):
        return f"{self.name} ({self.age} y.o.)"

    def move_to(self, location):
        self.location = location

class Child(Human):

    def __init__(self, h_name, h_age, h_location):
        super().__init__(h_name, h_age, h_location)
        self.grade = h_age - 6

    def get_info(self):
        super().get_info()
        print("Grade is", self.grade)

ch1 = Child ("Diana", 15, "Home")
# ch1.get_info()
ch2 = Child ("Gena", 14, "Home")
ch3 = Child ("Natasha", 16, "Home")
ch4 = Child ("Egor", 13, "Home")
ch5 = Child ("Andrey", 15, "Home")

class Bus():
    def __init__(self):
        self.passengers = []

    def add_passenger(self, add_pass):
        self.passengers.append(add_pass)
        add_pass.location = "Bus"

    def kick_passenger(self, kick_pass):
        self.passengers.remove(kick_pass)

    def get_info(self):
        print(self.passengers)

    def move_location(self, location):
        for i in self.passengers:
            i.move_to(location)

ch2.location = 0
bus1 = Bus()
bus1.add_passenger(ch2)
bus1.add_passenger(ch3)
bus1.add_passenger(ch4)
bus1.kick_passenger(ch3)
bus1.get_info()

ch2.get_info()