class Animal:

    alive = True
    fed = False

    def __init__(self,name):
        self.name = name


class Mammal(Animal):
    edible = True
    def eat(self,food):
        pass

class Predator(Animal):

    def eat(self, food):
        if food == cucumber_RICK:
            self.alive = False
            print(f'{self.name} был убит {cucumber_RICK.name}, потому что не на того напал. Будет знать!')
        else:
            if food.edible == True:
                self.fed = True
                print(f'{self.name} съел {food.name} и теперь сыт')
            else:
                self.alive = False
                self.fed = None
                print(f"{self.name} отравился и погиб из-за {food.name}")



class Plant:

    edible = False

    def __init__(self, name):
        self.name = name

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

#Объекты класса Flower:
crows_eye = Flower('Вороний глаз')
cikuta = Flower('Цикута')
weh = Flower('Вех')

#Объекты класса Fruit:
peach = Fruit('Пепсик')
watermelon = Fruit("АбуБз")
dragon_fruit = Fruit("ДрагонФрут")

#Объекты класса Mammal:
kangaroo = Mammal("Руу")
guinea_pig = Mammal("Юпитер")
elephant = Mammal("Рик")

#Объекты класса Predator:
wolverine = Predator('Логан')
hedgehog = Predator('Шедов')
lion = Predator('Ливи')
cucumber_RICK = Predator('Огурчик РИК')

print(lion.alive)
print(lion.name)
lion.eat(cucumber_RICK)
print(lion.alive)

print(guinea_pig.name)
print(hedgehog.name)
print(watermelon.name)
print(cikuta.name)

print(wolverine.alive)
print(wolverine.fed)

wolverine.eat(watermelon)
print(wolverine.fed)
wolverine.eat(cikuta)
print(wolverine.alive)
print(wolverine.fed)






