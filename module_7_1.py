class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'product.txt'
    __file = open(__file_name)


    def get_products(self):
        return self.__file.read()

    def add(self, *product):
        __file = open(self.__file_name)
        for j in product:
            for i in __file:
                if j.__str__() in i:
                    print(f'product {j.name} just has in Shop')
                    break
                elif j.__str__() not in i:
                    continue
            else:
                __file_app = open(self.__file_name, 'a')
                __file_app.write(f"{j.name}, {j.weight}, {j.category}\n")



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Orange', 10.2, 'Fruits')

s1.add(p1,p2,p3)
s1.add(p4)
print(s1.get_products())


