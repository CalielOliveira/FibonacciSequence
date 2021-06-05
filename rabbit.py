# rabbits class

class Rabbit:
    # age in months
    age = 0

    def __init__(self):
        self.newborn = True
        self.giving_birth = False

    def add_month(self):
        self.age += 1
        if self.age >= 2:
            self.giving_birth = True
