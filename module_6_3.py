class Horse:

    def __init__(self, x_distance = 0, sound = "Frr"):
        self.x_distance = x_distance
        self.sound = sound
        super().__init__()


    def run(self, dx):
        self.x_distance += dx


class Eagle:

    def __init__(self, y_distance = 0, sound ='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)



pegi = Pegasus()

print(pegi.get_pos())

pegi.move(10, 15)
print(pegi.get_pos())

pegi.move(-5, 20)
print(pegi.get_pos())

pegi.voice()


