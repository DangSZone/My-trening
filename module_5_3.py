class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors = self.number_of_floors + value
            return self

    def __radd__(self, value):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors = value + self.number_of_floors
        return self

    def __iadd__(self, value):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors += value
            return self


    def go_to(self, new_floor):
        new_floor = int(new_floor)
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, (new_floor + 1)):
                print(i)


h1 = House('Развитие', 18)
h2 = House("HELL", 9)

print(h1)
print(h2)

print(h1 == h2)

h2 = h2 + 9
print(h2)
print(h1 == h2)

h1 = 13 + h1
print(h1)

h2 += 13
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)


