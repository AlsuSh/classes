class Animals:
    name = None
    weight = 0

    def __init__(self, name, weight = 0):
        self.name = name
        self.weight = weight

    def feed(self):
        return "Fed..."


class Birds(Animals):

    def collect(self):
        return "Collected..."

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

    def milk(self):
        return "Good..."


class Sheep(Ungulates):

    def voice(self):
        return "beeee..."

    def shear(self):
        return "Trimmed..."


class Goat(Ungulates):

    def voice(self):
        return "meeee..."

    def milk(self):
        return "Good..."


total_weight = 0
ferma = dict()

def add_ferma(animal):
    if animal["weight"] not in ferma.keys():
        ferma[animal["weight"]] = list()
    ferma[animal["weight"]].append(animal["name"])
    return ferma
    # return ferma.append(animal)

goose_0 = Goose("Gray",3)
add_ferma(goose_0.__dict__)

goose_1 = Goose("White",2)
add_ferma(goose_1.__dict__)

cow_0 = Cow("Man'ka",400)
add_ferma(cow_0.__dict__)

sheep_0 = Sheep("Barashek",50)
add_ferma(sheep_0.__dict__)

sheep_1 = Sheep("Barashek",60)
add_ferma(sheep_1.__dict__)

chicken_0 = Chicken("Ko-ko",1)
add_ferma(chicken_0.__dict__)

chicken_1 = Chicken("Kukareku",2)
add_ferma(chicken_1.__dict__)

goat_0 = Goat("Roga",100)
add_ferma(goat_0.__dict__)

goat_1 = Goat("Kopita",120)
add_ferma(goat_1.__dict__)

duck_0 = Duck("Kryakva",2)
add_ferma(duck_0.__dict__)

print(ferma)
ferma_sort = sorted(ferma.keys(),reverse = True)
for x in ferma.keys():
    total_weight += x

print("общий вес животных: {},{} самое тяжелое животное".format(total_weight, ferma[ferma_sort[0]]))