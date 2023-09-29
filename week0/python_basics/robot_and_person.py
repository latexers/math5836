class Robot:
    def __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w

    def sing(self):
        print("My name is " + self.name)


class CNN:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.isSitting = i

    def _down(self):
        print("My name is " + self.name)
    def _up(self):
        pass

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "aggressive", True)

p1.robot_owned = r2
p2.robot_owned = r1


p1.robot_owned.introduce_self()
