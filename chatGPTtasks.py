#TASK4TASK4TASK4TASK4TASK4TASK4TASK4TASK4TASK4TASK4TASK4TASK4TASK4TASK4TASK4TASK4TASK4TASK4TASK4TASK4TASK4TASK4TASK4TASK4
# class Pet():
#
#     def __init__(self, v_name, v_species):
#         self.name = v_name
#         self.species = v_species
#
#     def describe(self):
#         print(f'Имя питомца: {self.name}, вид: {self.species}')
#
# pet1 = Pet('Рекс', 'Собака')
# pet2 = Pet('Паша', 'Черепаха')
#
# pet1.describe()
# pet2.describe()
#
# class Dog(Pet):
#     species = "Dog"
#
#     def __init__(self, v_name, v_breed):
#         super().__init__(v_name, "Собака")
#         self.breed = v_breed
#
#     def bark(self):
#         print(f'Гаф, меня зовут {self.name}')
#
#     def describe(self):
#         print(f'Имя питомца: {self.name}, вид: {self.species}, порода: {self.breed}')
#
# pet3 = Dog('Миша', 'Дворняжка')
# pet3.describe()
# pet3.bark()

#TASK5TASK5TASK5TASK5TASK5TASK5TASK5TASK5TASK5TASK5TASK5TASK5TASK5TASK5TASK5TASK5TASK5TASK5TASK5TASK5TASK5TASK5TASK5TASK5
# class Book():
#
#     def __init__(self, v_title, v_author):
#         self.author = v_author
#         self.title = v_title
#
#     def book_info(self):
#         print(f'{self.title}, автор: {self.author}')
#
#     def __repr__(self):
#         return (f'{self.title}, автор: {self.author}')
#
# book1 = Book('"Процесс"', 'Ф. Кафка')
# book2 = Book('"Война и мир"', 'Л. Толстой')
# book1.book_info()
# book2.book_info()
#
# class Library():
#
#     def __init__(self):
#         self.books = []
#
#     def add_book(self, v_book):
#         self.books.append(v_book)
#
#     def remove_book(self, v_book):
#         if v_book in self.books:
#             self.books.remove(v_book)
#         else:
#             print(f'{v_book} не в библиотеке!')
#
#     def show_books(self):
#         print(self.books)
#
# lib_military = Library()
# lib_military.add_book(book1)
# lib_military.add_book(book2)
# lib_military.show_books()
#
# lib_military.remove_book(book1)
# lib_military.show_books()
#
# lib_military.remove_book('книга')
# lib_military.show_books()

#TASK6TASK6TASK6TASK6TASK6TASK6TASK6TASK6TASK6TASK6TASK6TASK6TASK6TASK6TASK6TASK6TASK6TASK6TASK6TASK6TASK6TASK6TASK6TASK6
#
# class Car():
#     wheels = 4
#
#     def __init__(self, v_brand, v_year):
#         self.brand = v_brand
#         self.year = v_year
#         self.location = 'Гараж'
#
#     def age(self):
#         return 2025 - int(self.year)
#
#     def car_info(self):
#         print(f'Эта {self.brand} {self.year} года выпуска. Она на ходу уже {self.age()} лет и находится в {self.location}.')
#
#     def drive(self, v_destination):
#         self.location = v_destination
#         print(self.location)
#
#
# car1 = Car('Тойота', 2003)
# print(car1.age())
# car1.car_info()
# car1.drive('Прокопьевск')
# car1.location
#
# car2 = Car('Лада', 1997)
# car3 = Car('Мерседес', 2000)
#
# def drive_all(cars, place):
#     for i in cars:
#         i.location = place
#
#
# drive_all([car1, car2, car3], 'Санкт-Петербург')
#
# car1.car_info()

#TASK7TASK7TASK7TASK7TASK7TASK7TASK7TASK7TASK7TASK7TASK7TASK7TASK7TASK7TASK7TASK7TASK7TASK7TASK7TASK7TASK7TASK7TASK7TASK7

# class Student():
#
#     def __init__(self, v_student_name, v_student_age):
#         self.name = v_student_name
#         self.age = v_student_age
#         self.grades = []
#         # self.avg = int
#
#     def add_grade(self, v_grade):
#         self.grades.append(v_grade)
#         print(f'Вы поставили {v_grade} студенту {self.name}')
#
#     def average_grade(self):
#         return sum(self.grades) / float(len(self.grades))
#         # self.avg = sum(self.grades) / len(self.grades)
#
#     def get_info(self):
#         print(f'Средний балл студента {self.name} - {self.average_grade()}. Его возраст {self.age}')
#         # print(f'Средний балл студента {self.name} - {self.avg}. Его возраст {self.age}')
#
# stud1 = Student('Юра', 22)
#
# stud1.add_grade(5)
# stud1.add_grade(4)
# stud1.add_grade(2)
# stud1.add_grade(5)
#
# stud1.get_info()

#TASK8TASK8TASK8TASK8TASK8TASK8TASK8TASK8TASK8TASK8TASK8TASK8TASK8TASK8TASK8TASK8TASK8TASK8TASK8TASK8TASK8TASK8TASK8TASK8
#
# class Passenger():
#
#     def __init__(self, v_name):
#         self.name = v_name
#         self.bus_number = 'Не в автобусе'
#
#     def __repr__(self):
#         return self.name
#
# pass1 = Passenger('Gena')
# pass2 = Passenger('Natasha')
# pass3 = Passenger('Ilya')
# pass4 = Passenger("Veronika")
#
#
# class Bus():
#
#     def __init__(self, v_number, v_capacity):
#         self.number = v_number
#         self._capacity = v_capacity
#         self.__passengers = []
#
#     def add_passenger(self, v_passenger):
#         if len(self.__passengers) < self._capacity:
#             self.__passengers.append(v_passenger)
#             v_passenger.bus_number = self.number
#         else:
#             print(f'Автобус переполнен!')
#
#     def remove_passenger(self, v_passenger):
#         if v_passenger in self.__passengers:
#             self.__passengers.remove(v_passenger)
#         elif len(self.__passengers) == 0:
#             print(f'Автобус пуст!')
#         else:
#             print(f'Данный человек не в автобусе!')
#
#     def get_passengers(self):
#         return self.__passengers
#
#     def get_info(self):
#         return (f'Автобус под номером {self.number}, заполнен на {len(self.__passengers)} из {self._capacity} мест. '
#                 f'Его пассажиры: {self.__passengers}')
#
# bus1 = Bus(563, 49)
# bus2 = Bus(119, 76)
#
# bus1.add_passenger(pass1)
# bus1.add_passenger(pass2)
#
# print(bus1.get_info())
#
# class SchoolBus(Bus):
#
#     def __init__(self, v_number, v_capacity):
#         super().__init__(v_number, v_capacity)
#
#     def announce(self):
#         return f'В автобусе {len(self.get_passengers())} пассажиров'
#
#     def transfer_passengers(self, other_bus):
#         passengers_to_move = other_bus.get_passengers().copy()
#         print(len(passengers_to_move))
#         print(self._capacity)
#         if len(passengers_to_move) <= self._capacity:
#             for i in passengers_to_move:
#                 self.add_passenger(i)
#                 i.bus_number = self.number
#                 other_bus.remove_passenger(i)
#
# schbus1 = SchoolBus(1, 13)
# schbus1.transfer_passengers(bus1)
#
# print(schbus1.get_info())
# print(bus1.get_info())
#
#TASK9TASK9TASK9TASK9TASK9TASK9TASK9TASK9TASK9TASK9TASK9TASK9TASK9TASK9TASK9TASK9TASK9TASK9TASK9TASK9TASK9TASK9TASK9TASK9

class Zoo():

    def __init__(self, v_name):
        self.name = v_name

class Animal(Zoo):

    def __init__(self, v_name, v_species):
        super().__init__(v_name)
        self._species = v_species
        self.__is_hungry = True

    def eat(self):
        self.__is_hungry = False
        print(f'Животное {self.name} поело.')

    def get_is_hungry(self):
        return self.__is_hungry

class Dog(Animal):

    def __init__(self, v_name):
        super().__init__(v_name, v_species='Собака')
        self._species = 'Собака'
        self.__is_hungry = True

    def eat(self):
        super().eat()
        print(f'Собака {self.name} проела.')

dog1 = Dog("Rex")
print(dog1.eat())


# 22/01/2026
#
# TASK1TASK1TASK1TASK1TASK1TASK1TASK1TASK1TASK1TASK1TASK1TASK1TASK1TASK1TASK1TASK1TASK1TASK1TASK1TASK1TASK1TASK1TASK1TASK1
#
# a = int(input("Введите целое число: "))
# b = float(input("Введите дробное число: "))
#
# print(a+b, a-b, a*b, a/b)
# TASK2
#
# string = str(input("Введите текст:"))
# vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
# counter_a = 0
# counter_b = 0
# for i in string.lower():
#     if i.isalpha():
#         if i in vowels:
#             counter_a += 1
#         else:
#             counter_b += 1
#
# print("Гласных букв во введённом тексте:", counter_a)
# print("Согласных букв во введённом тексте:", counter_b)
#
#
# TASK 3
# l_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# d_num = {}
#
# for i in l_num:
#     d_num[i] = i * i
#
# print(d_num)
#
#
# TASK 4
# a = float(input("Введите число: "))
#
# if a > 0:
#     print(a, "положительное число")
# elif a == 0:
#     print("Вы ввели ноль")
# else:
#     print(a, "отрицательное число")
#
#
# TASK 5
#
# fib_num1 = 0
# fib_num2 = 1
#
# while fib_num1 < 100:
#     print(fib_num1, end=" ")
#     fib_num1, fib_num2 = fib_num2, fib_num1+fib_num2
#
#
# TASK 6
# def squares(a, b, c, d, e):
#     l_numb = []
#     l_numb.append(a ** 2)
#     l_numb.append(b ** 2)
#     l_numb.append(c ** 2)
#     l_numb.append(d ** 2)
#     l_numb.append(e ** 2)
#     return l_numb
#
# print(squares(1, 2, 3, 4 ,5))
#
#
# TASK 7
# class Person():
#     life = 1
#
#     def __init__(self, v_name, v_age):
#         self.name = v_name
#         self.age = v_age
#
#     def greet(self):
#         return f'Hello {self.name}!'
#
# pers1 = Person("Alex", 27)
# print(pers1.greet())
#
#
# TASK 8
# class Person():
#     life = 1
#
#     def __init__(self, v_name, v_age):
#         self.name = v_name
#         self.age = v_age
#
#     def greet(self):
#         return f'Hello {self.name}!'
#
# class Employee(Person):
#
#     def __init__(self, v_name, v_age, v_position):
#         super().__init__(v_name, v_age)
#         self.position = v_position
#
#     def work(self):
#         return f'Я работаю на должности {self.position.lower()}'
#
# emp1 = Employee("Erik", 28, "Шофёр")
# print(emp1.work())
#
#
# TASK 9
# class BankAccount():
#
#     def __init__(self, v_owner):
#         self.owner = v_owner
#         self.__balance = 0
#
#     def deposit_balance(self, v_sum):
#         self.__balance += v_sum
#         return f'Вы пополнини баланс {self.owner} на {v_sum} единиц. Сейчас баланс равен {self.__balance} единиц'
#
#     def get_balance(self):
#         return f'Сейчас баланс равен {self.__balance} единиц'
#
# bacc1 = BankAccount("Alex")
# print(bacc1.deposit_balance(600))
# print(bacc1.deposit_balance(300))
# print(bacc1.get_balance())
#
#
# TASK 10
# class Library():
#
#     def __init__(self):
#         self.list_of_books = []
#
#     def add_book(self, v_book):
#         self.list_of_books.append(v_book)
#
#     def del_book_of_title(self, v_deleting_title):
#         l_deleted = False
#         l_not_deleted = []
#         for book in self.list_of_books:
#             if v_deleting_title.lower() in book.title.lower():
#                 l_deleted = True
#             else:
#                 l_not_deleted.append(book)
#         if not l_deleted:
#             return False
#         else:
#             self.list_of_books = l_not_deleted
#
#     def see_all_books(self):
#         return self.list_of_books
#
#     def find_book_of_author_name(self, v_finding_author):
#         l_of_finded_books = []
#         for book in self.list_of_books:
#             if v_finding_author.lower() in book.author.lower():
#                 l_of_finded_books.append(book)
#         if not l_of_finded_books:
#             return False
#         else:
#             return l_of_finded_books
#
# class Book():
#
#     def __init__(self, v_title, v_author, v_year):
#         self.title = v_title
#         self.author = v_author
#         self.year = v_year
#
#     def __str__(self):
#         return f"{self.title} — {self.author} ({self.year})"
#
#     def __repr__(self):
#         return self.__str__()
#
# lib_military = Library()
# book1 = Book("Пикник на обочине", "Братья Стругацкие", 1972)
# book2 = Book("Метро 2033", "Дмитрий Глуховский", 2005)
# book3 = Book("Метро 2034", "Дмитрий Глуховский", 2009)
# lib_military.add_book(book1)
# lib_military.add_book(book2)
# lib_military.add_book(book3)
# print(lib_military.list_of_books)
# print()
#
# lib_military.del_book_of_title("Пикник")
# print(lib_military.list_of_books)
# print()
#
# print(lib_military.find_book_of_author_name("Стругацкие"))

