
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, nev_floor):
        self.nev_floor = nev_floor
        if nev_floor < 1 or nev_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, nev_floor + 1):
                print(i)


h1 = House('ЖК Речной', 12)
h2 = House('ЖК Полевой', 6)

h1.go_to(9)
h2.go_to(7)
