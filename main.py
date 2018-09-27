from abc import ABC, abstractmethod

class Animal(ABC):
    name = None
    weight = 0

    def __init__(self, name, weight = 0):
        self.name = name
        self.weight = weight

    @abstractmethod
    def collect_stuff(self):
        pass

class Bird(Animal):

    def collect_stuff(self):
        print("collected eggs")
        super().collect_stuff()


class Ungulate(Animal):
    pass


class Goose(Bird):

    def voice(self):
        return "ga-ga-ga..."


class Chicken(Bird):

    def voice(self):
        return "ko-ko-ko..."


class Duck(Bird):

    def voice(self):
        return "krya-krya-krya..."


class Cow(Ungulate):

    def voice(self):
        return "muuuu..."

    def collect_stuff(self):
        print("received milk")
        super().collect_stuff()


class Sheep(Ungulate):

    def voice(self):
        return "beeee..."

    def collect_stuff(self):
        print("trimmed")
        super().collect_stuff()


class Goat(Ungulate):

    def voice(self):
        return "meeee..."

    def collect_stuff(self):
        print("received milk")
        super().collect_stuff()


total_weight = 0
ferma_dict = dict()
ferma_list = []


goose_0 = Goose("Gray", 3)
ferma_list.append(goose_0)

goose_1 = Goose("White", 2)
ferma_list.append(goose_1)

cow_0 = Cow("Man'ka", 400)
ferma_list.append(cow_0)

sheep_0 = Sheep("Barashek", 50)
ferma_list.append(sheep_0)

sheep_1 = Sheep("Barashek", 60)
ferma_list.append(sheep_1)

chicken_0 = Chicken("Ko-ko", 1)
ferma_list.append(chicken_0)

chicken_1 = Chicken("Kukareku", 2)
ferma_list.append(chicken_1)

goat_0 = Goat("Roga", 100)
ferma_list.append(goat_0)

goat_1 = Goat("Kopita", 120)
ferma_list.append(goat_1)

duck_0 = Duck("Kryakva", 2)
ferma_list.append(duck_0)


for x in ferma_list:
    x.collect_stuff()
    total_weight += x.__dict__["weight"]
    if x.__dict__["weight"] not in ferma_dict.keys():
        ferma_dict[x.__dict__["weight"]] = list()
        ferma_dict[x.__dict__["weight"]].append(x.__dict__["name"])

ferma_sort = sorted(ferma_dict.keys(), reverse = True)
print("общий вес животных: {},{} самое тяжелое животное".format(total_weight, ferma_dict[ferma_sort[0]]))