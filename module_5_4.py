class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(self.name, "снесён, но он останется в истории")


House_1 = House('ЖК Горский', 18)
print(House.houses_history)

House_2 = House('Домик в деревне', 2)
print(House.houses_history)

House_3 = House('ТК "Северный"', 4)
print(House.houses_history)

del House_1
del House_2

print(House.houses_history)
