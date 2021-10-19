from pygame import Color, Rect
from pygame.draw import rect

from CONSTANTS import BACKGROUND_COLOR


class Board:
    BORDER_COLOR = Color("white")
    CELL_SCALE = 0.04
    BORDER = 1
    TOP, LEFT = 50, 0
    WIDTH, HEIGHT = 24, 24

    def __init__(self):
        self.cell_size = round(self.WIDTH * self.CELL_SCALE)
        self.board = [[0 for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        self.timer = 0

    def get_size(self):
        return self.WIDTH, self.HEIGHT

    def render(self, surface):
        for i in range(self.HEIGHT):
            for k in range(self.WIDTH):
                self.draw_cell(surface, k, i)

    def draw_cell(self, surface, x, y):
        full_cell_rectangle = Rect(self.LEFT + x * self.cell_size,
                                   self.TOP + y * self.cell_size,
                                   self.cell_size, self.cell_size)
        cell_rectangle = Rect(self.LEFT + x * (self.cell_size - self.BORDER),
                              self.TOP + y * (self.cell_size - self.BORDER),
                              self.cell_size, self.cell_size)

        rect(surface, self.BORDER_COLOR, full_cell_rectangle)
        rect(surface, BACKGROUND_COLOR, cell_rectangle)
