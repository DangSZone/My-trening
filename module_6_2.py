class Vehicle:

    __COLOR_VARIANTS = ['синий', "красный", "зелёный", 'серый', "белый", "черный"]

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__color = str(__color)
        self.__engine_power = int(__engine_power)

    def get_model(self):
        print(f'Модель: {self.__model}')
    def get_horsepower(self):
        print(f"Мощность: {self.__engine_power}")
    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        print('-----------')
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f"Владелец: {self.owner}")
        print('-----------')

    def set_color(self, new_color):
        self.new_color = str(new_color)
        for cv in self.__COLOR_VARIANTS:
            if str(cv.lower()) == self.new_color.lower():
                self.__color = cv.lower()
                print(f'Цвет успешно изменён на {new_color}')
                break
            elif len(cv) != len(self.__COLOR_VARIANTS):
                continue
            else:
                print(f'Нельзя сменить цвет на {new_color}')





class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5




vehicle1 = Sedan("Васёк", 'Mazda cx5', 'красный', 450)
vehicle2 = Sedan('Фёдор', 'Toyota Mark II', 'синий', 500)

vehicle2.print_info()

vehicle2.set_color("розовый")
vehicle2.set_color('черный')
vehicle2.owner = "Васёк"

vehicle2.print_info()




