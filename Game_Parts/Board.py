from pygame import Color, Rect, Surface
from pygame.draw import rect

from constants import BACKGROUND_COLOR


class Board:
    BORDER_COLOR = Color("white")
    CELL_SCALE = 0.04
    BORDER = 1

    def __init__(self, screen_size: tuple, margin: tuple = (0, 0), border_size: tuple = (24, 24)):
        self.width, self.height = border_size
        self.left_margin, self.top_margin = margin
        self._cell_size = round(screen_size[0] * self.CELL_SCALE)
        self._board = None
        self.init_board()

    def get_size(self) -> tuple:
        return self.width, self.height

    def init_board(self):
        self.clear()

    def clear(self) -> None:
        self._board = [[(0, BACKGROUND_COLOR) for _ in range(self.width)] for _ in range(self.height)]

    def __getitem__(self, item_index) -> list:
        return self._board[item_index]

    def __setitem__(self, key, value) -> None:
        self._board[key] = value

    def __len__(self) -> int:
        return len(self._board)

    def draw(self, surface) -> None:
        for i in range(self.height):
            for k in range(self.width):
                self.draw_cell(surface, k, i)

    def draw_cell(self, surface: Surface, x: int, y: int) -> None:
        full_cell_rectangle = Rect(self.left_margin + x * self._cell_size,
                                   self.top_margin + y * self._cell_size,
                                   self._cell_size, self._cell_size)

        cell_rectangle = Rect(self.left_margin + self.BORDER + x * self._cell_size,
                              self.top_margin + self.BORDER + y * self._cell_size,
                              self._cell_size - self.BORDER * 2, self._cell_size - self.BORDER * 2)

        rect(surface, self.BORDER_COLOR, full_cell_rectangle)
        rect(surface, self._board[x][y][1], cell_rectangle)
