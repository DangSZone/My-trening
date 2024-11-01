class Horse:

    x_distance = 0
    sound = 'Frr'

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    y_distance = 0
    sound ='I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(Eagle.sound)


pegi = Pegasus()

print(pegi.get_pos())

pegi.move(10, 15)
print(pegi.get_pos())

pegi.move(-5, 20)
print(pegi.get_pos())

pegi.voice()


