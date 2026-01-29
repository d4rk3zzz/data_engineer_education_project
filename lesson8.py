class Warehouse():

    def __init__(self, nickname, capacity_of_warehouse):
        self.nickname = nickname
        self.__capacity_of_box = capacity_of_warehouse
        self.__list_of_boxes = []
        self.__list_of_bottles = []

    def __str__(self):
        return f'Warehouse {self.nickname}'

    def __repr__(self):
        return self.__str__()

    def get_info_of_wh(self):
        try:
            self.nickname / 2
            return f'Warehouse: {self.nickname}, have capacity {self.__capacity_of_box}, and next boxes: {self.__list_of_boxes}'
        except TypeError:
            print('Выбран не тот тип объекта')
        except Exception as e:
            print(e)

    def see_all_bottles(self):
        for i in self.__list_of_boxes:
            for l in i.get_info_of_bottles_list():
                if l not in self.__list_of_bottles:
                    self.__list_of_bottles.append(l)
        return self.__list_of_bottles

    def add_box(self, boxes):
        self.__list_of_boxes += [box for box in boxes if box not in self.__list_of_boxes]
        for i in boxes:
            try:
                i.warehouse = NEIZVESTNAYA_PEREMENNAYA
                i.warehouse = self
                for l in i.get_info_of_bottles_list():
                    l.warehouse = self
            except Exception as e:
                print(e)
        return self.__list_of_boxes

    def remove_box(self, removing_boxes):
        self.__list_of_boxes = [box for box in self.__list_of_boxes if box not in removing_boxes]
        for i in removing_boxes:
            try:
                box1 = 'string'
                i.warehouse = None
            except Exception as e:
                print(e)
        return self.__list_of_boxes

    def remove_bottle_from_wh(self, removing_bottle):
        self.__list_of_bottles = [bottle for bottle in self.__list_of_bottles if bottle not in removing_bottle]
        for i in removing_bottle:
            try:
                i = Box(2, 4, 6, 7)
                i.warehouse = None
                i.box = None
            except Exception as e:
                print(e)
        return self.__list_of_bottles, 'removed: ', removing_bottle

wh1 = Warehouse("УТЗ", 3)

class Box():

    def __init__(self, number, capacity_of_box):
        self.__number = number
        self.capacity_of_box = capacity_of_box
        self.__list_of_bottles = []
        self.warehouse = None

    def __str__(self):
        return f'Box№{self.__number}'

    def __repr__(self):
        return self.__str__()

    def get_info_of_box(self):
        try:
            print(adsa)
            return f'Box№{self.__number}, capacity is {self.capacity_of_box}, have next bottles: {self.__list_of_bottles}'
        except Exception as e:
            print(e)

    def get_info_of_bottles_list(self):
        return self.__list_of_bottles

    def add_bootle(self, bottles):
        self.__list_of_bottles += [bottle for bottle in bottles if bottle not in self.__list_of_bottles]
        for i in self.__list_of_bottles:
            try:
                i.add_bootle()
                i.box = self
            except Exception as e:
                print(e)
        return self.__list_of_bottles

    def remove_bottle(self, removing_bottles):
        self.__list_of_bottles = [bottle for bottle in self.__list_of_bottles if bottle not in removing_bottles]
        for i in removing_bottles:
            try:
                self.capacity_of_box / 0
                i.box = None
            except Exception as e:
                print(e)
        return self.__list_of_bottles

box1 = Box(1, 6)
box2 = Box(2, 12)
box3 = Box(3, 24)

class Bottle():

    def __init__(self, number, material, bottle_volume, drink_type):
        self.__number = number
        self.material = material
        self.bottle_volume = bottle_volume
        self.drink_type = drink_type
        self.box = None
        self.warehouse = None

    def __str__(self):
        return f'Bottle№{self.__number} - drink: {self.drink_type}'

    def __repr__(self):
        return self.__str__()

    def get_info_of_bottle(self):
        try:
            self.bottle_volume + "л"
            return f'Bottle№{self.__number}, {self.bottle_volume}, {self.drink_type}, {self.material}, {self.box}, {self.warehouse}'
        except Exception as e:
            print(e)

btl1 = Bottle(1, 'metal', 0.5, 'beer')
btl2 = Bottle(2, 'metal', 0.5, 'beer')
btl3 = Bottle(3, 'metal', 0.5, 'beer')
btl4 = Bottle(4, 'glass', 0.43, 'soda')
btl5 = Bottle(5, 'glass', 0.43, 'soda')
btl6 = Bottle(6, 'plastic', 1.45, 'cold tea')

# print(box1.add_bootle([btl1, btl2]))
# # print(box1.remove_bottle([btl1]))
# print(wh1.add_box([box1, box3]))
# # print(wh1.remove_box([box3]))
# #
# wh1.get_info_of_wh()
# box1.get_info_of_box()
# btl2.get_info_of_bottle()
# #
# wh1.remove_bottle_of_wh([btl2])
# #
# # wh1.get_info_of_wh()
# box1.get_info_of_box()
# # btl2.get_info_of_bottle()


print(btl1.get_info_of_bottle())
print('---------------------------------------------------------')
box1.add_bootle([btl1])
wh1.add_box([box1])
print(wh1.see_all_bottles())
print(btl1.get_info_of_bottle())
print('---------------------------------------------------------')
box1.remove_bottle([btl1])
print(btl1.get_info_of_bottle())
print('---------------------------------------------------------')
wh1.remove_bottle_from_wh([btl1])
print(btl1.get_info_of_bottle())
print(wh1.see_all_bottles())
wh1.remove_bottle_from_wh([btl1])