from operator import add
from random import randint, choice


class Snake:
    MOVE_DIRECTION = {"down": (0, 1), "right": (1, 0), "up": (0, -1), "left": (-1, 0)}

    def __init__(self, board_size):
        self.direction = choice(list(self.MOVE_DIRECTION.values()))
        self.head = randint(0, board_size[0]), randint(0, board_size[1])
        self.body = self.create_body(self.direction, [self.head])

    def create_body(self, direction: tuple, head: list, sections_number: int = 3) -> list:
        if not sections_number:
            return head

        head.append(tuple(map(add, head[-1], direction)))
        sections_number -= 1

        return self.create_body(direction, head, sections_number)

    def draw(self, board):
        pass
