from pygame import Surface
from pygame.event import Event

from .Apple import Apple
from .Board import Board
from .Snake import Snake


class Game:
    def __init__(self):
        _is_running = True
        _apple = Apple()
        _board = Board()
        _snake = Snake(_board.get_size())

    def update(self, event: Event) -> None:
        pass

    def draw(self, surface: Surface) -> None:
        pass
