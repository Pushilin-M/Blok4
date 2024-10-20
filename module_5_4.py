
class House:

    houses_histori = []

    def __new__(cls, *args, **kwargs):
        cls.houses_histori.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название : {self.name}, колличество этажей : {self.number_of_floors}'

    def __del__(self):
        print(f'{self.name} снесён, но останется в истории')


h1 = House('ЖК Речной', 10)
print(House.houses_histori)

h2 = House('ЖК Полевой', 20)
print(House.houses_histori)

h3 = House('ЖК Луговой', 25)
print(House.houses_histori)

del h2
del h3

print(House.houses_histori)
