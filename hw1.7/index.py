class Animal:
    type = 'животное'
    name = ''
    can_fly = False
    sound = ''

    def __init__(self, name='(забыли назвать)'):
        self.name = name
        print('Создано: %s' % self.__str__())

    def make_sound(self):
        if not self.sound:
            return
        print('%s издает звук "%s"' % (self.name, self.sound))

    def __str__(self):
        return '%s: %s' % (self.type, self.name)


class Mammal(Animal):
    type = 'млекопитающее'


class Bird(Animal):
    type = 'птица'
    can_fly = True


class Cow(Animal):
    type = 'корова'
    sound = 'муу'


class Goat(Animal):
    type = 'коза'
    sound = 'мее'


class Sheep(Animal):
    type = 'овца'
    sound = 'бее'


class Pig(Animal):
    type = 'свинья'
    sound = 'хрю'


class Duck(Bird):
    type = 'утка'
    sound = 'кря'


class Hen(Bird):
    type = 'курица'
    sound = 'куд-кудах'


class Goose(Bird):
    type = 'гусь'
    sound = 'га... га'


animals = [Pig('Марфа'), Cow('Зорька'),  Cow('Манька'), Bird(), Hen(), Goose('Потап')]

for animal in animals:
    animal.make_sound()
