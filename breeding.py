# breeding place

from rabbit import Rabbit


class Breeding:
    month = 0
    total_rabbits = []

    def __init__(self):
        self.total_rabbits.append(Rabbit())
        self.rabbits_per_month = {0: len(self.total_rabbits)}

    def add_rabbit(self):
        self.total_rabbits.append(Rabbit())

    def register_rabbits(self):
        self.rabbits_per_month[self.month] = len(self.total_rabbits)

    def add_month(self):
        self.month += 1
        new_rabbits = 0

        for rabbit in self.total_rabbits:
            rabbit.add_month()
            if rabbit.giving_birth:
                new_rabbits += 1

        for _ in range(new_rabbits):
            self.add_rabbit()

        self.register_rabbits()
