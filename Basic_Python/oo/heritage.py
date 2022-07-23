class Car:
    def __init__(self):
        self.__velocity = 0

    @property
    def velocity(self):
        return self.__velocity

    def speedup(self):
        self.__velocity += 5
        return self.__velocity

    def break_(self):
        self.__velocity -= 5
        return self.__velocity


class Uno(Car):
    pass

class Ferrari(Car):
    def speedup(self):
        super().speedup()
        return super().speedup()

c1 = Ferrari()
print(c1.speedup())
print(c1.speedup())
print(c1.speedup())
print(c1.break_())
print(c1.break_())
print(c1.break_())
