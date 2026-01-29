class Human():
    life = 1

    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age
        self.__location = 'Home'

    def __str__(self):
        return f'Class: {self.__class__.__name__}, name: {self.__name}, sex: {self.__sex}, age: {self.__age}, location: {self.__location}'

    def __repr__(self):
        return self.__str__()

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_sex(self, sex):
        self.__sex = sex

    def get_sex(self):
        return self.__sex

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_location(self, location):
        self.__location = location

    def get_location(self):
        return self.__location

    def get_stats(self):
        return self.__name, self.__sex, self.__age

hm1 = Human("Alex", "Male", 23)
# print(hm1.get_stats())
# hm1.set_name('Richard')
# print(hm1.get_stats())

class Child(Human):

    def __init__(self, name, sex, age, stage):
        super().__init__(name, sex, age)
        self.__stage = stage

    def __str__(self):
        return f"{super().__str__()}, stage:{self.__stage}"

    def set_stage(self, stage):
        self.__stage = stage

    def get_stats(self):
        return (*super().get_stats(), self.__stage)


ch1 = Child("Slava", "Male", 9, 3)
ch2 = Child("Andrey", "Male", 13, 7)
ch3 = Child("Egor", "Male", 10, 4)
ch4 = Child("Gena", "Male", 12, 6)
ch5 = Child("Natashka", "Female", 10, 4)

# print(ch1)
# print(ch2)
# print(ch3)
# print(ch4)
# print(ch5)

class Bus():
    wheels = 6

    def __init__(self, number):
        self.__passengers = []
        self.number = number

    def add_passenger(self, added_passengers):
        # self.__passengers.append(passenger)
        if type(added_passengers) is not list:
            added_passengers = [added_passengers]
        self.__passengers += [passenger for passenger in added_passengers if passenger not in self.__passengers]

    def kick_passenger(self, removable_passengers):
        # self.__passengers.remove(passenger)
        if type(removable_passengers) is not list:
            removable_passengers = [removable_passengers]
        self.__passengers = [passenger for passenger in self.__passengers if passenger not in removable_passengers]

    def get_passengers(self):
        return self.__passengers.copy()

    def change_location(self, new_location):
        for i in self.__passengers:
            i.set_location(new_location)

bus1 = Bus(563)

bus1.add_passenger([ch1, ch2, ch3, ch4])
bus1.add_passenger(ch5)
for _ in bus1.get_passengers():
    print(_)

print('-----------------------------')
bus1.change_location("Moscow")
bus1.kick_passenger([ch1])
for _ in bus1.get_passengers():
    print(_)

print('-----------------------------')
bus1.change_location("Saint-Petersburg")
bus1.kick_passenger(ch3)
bus1.kick_passenger([ch1])
for _ in bus1.get_passengers():
    print(_)