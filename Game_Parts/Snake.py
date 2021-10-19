from operator import add
from itertools import repeat
from random import randint, choice

from pygame import Color

from Game_Parts.EVENTS import STEP_EVENT, EAT_APPLE


class Snake:
    START_LENGTH = 10
    HEAD_COLOR = Color("purple4")
    COLOR = Color("purple")
    MOVE_DIRECTION = {"down": (0, 1), "right": (1, 0), "up": (0, -1), "left": (-1, 0)}

    def __init__(self, board_size):
        self.board_size = board_size
        self._directions = list(repeat(choice(list(self.MOVE_DIRECTION.values())), self.START_LENGTH+1))
        self._head = randint(0, board_size[0]), randint(0, board_size[1])
        self._body = self.create_body(self._directions[0], [self._head], self.START_LENGTH)
        self.normalize_coords()

    def get_head(self) -> tuple:
        return self._head

    def create_body(self, direction: tuple, head: list, sections_number: int) -> list:
        if not sections_number:
            return head

        head.append(self.add_coord(head[-1], map(lambda x: -x, direction)))
        sections_number -= 1

        return self.create_body(direction, head, sections_number)

    def draw_on_board(self, board, clear_board: bool = True) -> None:
        if clear_board:
            board.clear()

        self._head = self._body[0]

        for x, y in self._body:
            if x == self._head[0] and y == self._head[1]:
                board[x][y] = (1, self.HEAD_COLOR)

            else:
                board[x][y] = (1, self.COLOR)

    def normalize_coords(self) -> None:
        for cell_number, cell_coord in enumerate(self._body):
            self._body[cell_number] = self.normalize_coord(cell_coord)

    def normalize_coord(self, cell_coord) -> tuple:
        return cell_coord[0] % self.board_size[0], cell_coord[1] % self.board_size[1]

    def update(self, event) -> None:
        if event.type == STEP_EVENT:
            for direction, cell in zip(self._directions, self._body):
                new_position = self.normalize_coord(self.add_coord(direction, cell))

                if new_position in self._body:
                    raise ValueError

                self._body[self._body.index(cell)] = new_position

            self._directions = self._directions[:1] + self._directions[:-1]

        elif event.type == EAT_APPLE:
            new_cell_direction = self._directions[-1]
            new_cell = self.add_coord(self._body[-1], map(lambda x: -x, new_cell_direction))
            self._body.append(new_cell)
            self._directions.append(new_cell_direction)

    def change_direction(self, direction_name: str) -> None:
        if self.normalize_coord(self.add_coord(self.MOVE_DIRECTION[direction_name], self._body[0])) not in self._body:
            self._directions[0] = self.MOVE_DIRECTION[direction_name]

    @staticmethod
    def add_coord(coord1, coord2):
        return tuple(map(add, coord1, coord2))
