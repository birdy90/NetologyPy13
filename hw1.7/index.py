class Animal:
    title = 'животное'
    can_fly = False
    sound = ''

    def __init__(self):
        print('Создано: %s' % self.title)

    def make_sound(self):
        if not self.sound:
            return
        print('%s издает звук "%s"' % (self.title, self.sound))


class FlyingAnimal(Animal):
    title = 'летающее животное'
    can_fly = True


class Cow(Animal):
    title = 'корова'
    sound = 'муу'


class Goat(Animal):
    title = 'коза'
    sound = 'мее'


class Sheep(Animal):
    title = 'овца'
    sound = 'бее'


class Pig(Animal):
    title = 'свинья'
    sound = 'хрю'


class Duck(FlyingAnimal):
    title = 'утка'
    sound = 'кря'


class Hen(FlyingAnimal):
    title = 'курица'
    sound = 'куд-кудах'


class Goose(FlyingAnimal):
    title = 'гусь'
    sound = 'га... га'


animals = []
animals.append(Pig())
animals.append(Sheep())
animals.append(FlyingAnimal())
animals.append(Hen())
animals.append(Goose())

for animal in animals:
    animal.make_sound()
