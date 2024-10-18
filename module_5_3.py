
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        isinstance(self.number_of_floors, int)

    def go_to(self, nev_floor):
        self.nev_floor = nev_floor
        if nev_floor < 1 or nev_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, nev_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название : {self.name}, колличество этажей : {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other

    def __lt__(self, other):
        return self.number_of_floors < other

    def __le__(self, other):
        return self.number_of_floors <= other

    def __gt__(self, other):
        return self.number_of_floors > other

    def __ge__(self, other):
        return self.number_of_floors >= other

    def __ne__(self, other):
        return self.number_of_floors != other

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Речной', 10)
h2 = House('ЖК Полевой', 20)

print()
print(h1)
print(h2)

print(h1 == h2)

h1 = h1 + 10

print(h1)
print(h1 == h2)

h1 += 10

print(h1)

h2 = 10 + h2

print(h2)

print(h1>h2)
print(h1>=h2)
print(h1<h2)
print(h1<=h2)
print(h1!=h2)
