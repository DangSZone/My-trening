class Figure:
    sides_count = 0

    def __init__(self, *data , **filled):
        self.__sides = []
        for i in data:
            if isinstance(i, tuple):
                self.__color = list(i)
            if isinstance(i, int):
                self.__sides.append(i)
        if len(self.__sides) != self.sides_count and len(self.__sides) != 1:
            self.__sides = [1] * self.sides_count
        self.filled = filled

    def get_color(self):
        return  self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and r <= 255:
            self.__color[0] = int(r)
        else:
            return print("Неверное значение red")
        if isinstance(g, int) and g <= 255:
            self.__color[1] = int(g)
        else:
            return print("Неверное значение green")
        if isinstance(b, int) and b <= 255:
            self.__color[2] = int(b)
        else:
            return print("Неверное значение blue")

    def set_color(self, r, g, b):
        self.__is_valid_color(r, g, b)

    def  __is_valid_sides(self,*args):
        list_sides = []
        for i in args:
            if isinstance(i, int) and i > 0:
                list_sides.append(i)
            else:
                return print('Error')
        if len(list_sides) == self.sides_count:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        P = None
        if self.sides_count == 1:
            return self.__sides[0]
        elif self.sides_count == 3:
            P += self.__sides[0:self.sides_count+1]
            return P
        elif self.sides_count == 12:
            P = 12 * self.__sides[0]
            self.P = P
            return P

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        else:
            print("Данные введены неверно")


class Circle(Figure):
    sides_count = 1

    def __radius(self):
        l = self._Figure__sides[0]
        self.r = round(l / (2 * 3.14), 2)
        return self.r

    def get_square(self):
        self.__radius()
        self.s = round(3.14 * (self.r ** 2), 2)
        return print(self.s)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        sides1 , sides2, sides3 = self._Figure__sides
        p = 0.5 * (sides1 + sides2 + sides3)
        s_triangle = round((p*((p-sides1)*(p - sides2)*(p - sides3))) ** 0.5, 2)
        return print(s_triangle)


class Cube(Figure):
    sides_count = 12

    def __init__(self, *data , **filled):
        super().__init__(*data , **filled)
        self._Figure__sides = self._Figure__sides * 12


    def get_square(self):
        cube_side = self._Figure__sides[0]
        s_cube = 6 * (cube_side ** 2)
        return print(s_cube)

    def get_volume(self):
        v = self._Figure__sides[0] ** 3
        return v




circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
