from random import randint

from pygame import Color


class Apple:
    def __init__(self):
        self._color = Color("red")
        self.x, self.y = randint(0, 24), randint(0, 24)

    def replace(self, board) -> None:
        pass

    def __get__(self, instance, owner=None) -> dict:
        return {"color": self._color, "coord": (self.x, self.y)}
