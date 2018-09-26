class Animals:
    name = None
    weight = 0

    def __init__(self, name, weight = 0):
        self.name = name
        self.weight = weight

    def collect_stuff(self):
        pass

class Birds(Animals):

    def collect_stuff(self):
        print("collected eggs")
        super().collect_stuff()


class Ungulates(Animals):
    pass


class Goose(Birds):

    def voice(self):
        return "ga-ga-ga..."


class Chicken(Birds):

    def voice(self):
        return "ko-ko-ko..."


class Duck(Birds):

    def voice(self):
        return "krya-krya-krya..."


class Cow(Ungulates):

    def voice(self):
        return "muuuu..."

    def collect_stuff(self):
        print("received milk")
        super().collect_stuff()



class Sheep(Ungulates):

    def voice(self):
        return "beeee..."

    def collect_stuff(self):
        print("trimmed")
        super().collect_stuff()


class Goat(Ungulates):

    def voice(self):
        return "meeee..."

    def collect_stuff(self):
        print("received milk")
        super().collect_stuff()


total_weight = 0
ferma_dict = dict()
ferma_list = []


def add_to_ferma(animal):
    if animal["weight"] not in ferma_dict.keys():
        ferma_dict[animal["weight"]] = list()
        ferma_dict[animal["weight"]].append(animal["name"])
    return ferma_dict


goose_0 = Goose("Gray", 3)
ferma_list.append(goose_0)
add_to_ferma(goose_0.__dict__)

goose_1 = Goose("White", 2)
ferma_list.append(goose_1)
add_to_ferma(goose_1.__dict__)

cow_0 = Cow("Man'ka", 400)
ferma_list.append(cow_0)
add_to_ferma(cow_0.__dict__)

sheep_0 = Sheep("Barashek", 50)
ferma_list.append(sheep_0)
add_to_ferma(sheep_0.__dict__)

sheep_1 = Sheep("Barashek", 60)
ferma_list.append(sheep_1)
add_to_ferma(sheep_1.__dict__)

chicken_0 = Chicken("Ko-ko", 1)
ferma_list.append(chicken_0)
add_to_ferma(chicken_0.__dict__)

chicken_1 = Chicken("Kukareku", 2)
ferma_list.append(chicken_1)
add_to_ferma(chicken_1.__dict__)

goat_0 = Goat("Roga", 100)
ferma_list.append(goat_0)
add_to_ferma(goat_0.__dict__)

goat_1 = Goat("Kopita", 120)
ferma_list.append(goat_1)
add_to_ferma(goat_1.__dict__)

duck_0 = Duck("Kryakva", 2)
ferma_list.append(duck_0)
add_to_ferma(duck_0.__dict__)

for x in ferma_list:
    x.collect_stuff()

ferma_sort = sorted(ferma_dict.keys(), reverse = True)
for x in ferma_dict.keys():
    total_weight += x

print("общий вес животных: {},{} самое тяжелое животное".format(total_weight, ferma_dict[ferma_sort[0]]))