class Company():

    def __init__(self, number):
        self.number = number
        self.comp_regiments = []
        self.comp_soldiers = []

    def __repr__(self):
        return str(self.number)

    def __str__(self):
        return str(self.number)

class Regiment():

    def __init__(self, number):
        self.number = number
        self.reg_soldiers = []
        self.reg_company = None

    def __repr__(self):
        return str(self.number)

    def __str__(self):
        return str(self.number)

class Soldier():

    def __init__(self, name, dt):
        self.name = name
        self.dt = dt
        self.sold_regiment = None
        self.sold_company = None

    def __repr__(self):
        return f'{self.name}(a:{self.dt},r:{self.sold_regiment},c:{self.sold_company})'

    def __str__(self):
        return f'Sold name: {self.name}, dt:{self.dt}, reg:{self.sold_regiment}, comp:{self.sold_company}'