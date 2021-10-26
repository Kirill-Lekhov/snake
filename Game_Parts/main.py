from pygame import Surface
from pygame.event import Event

from .Apple import Apple
from .Board import Board
from .Snake import Snake
from .Controller import Controller

from EVENTS import EAT_APPLE, END_GAME


class Game:
    def __init__(self, pygame_instance, board_size: tuple, board_margin: tuple = (0, 0)):
        self._pygame_instance = pygame_instance
        self._is_running = True
        self._game_over = False
        self._controller = Controller()
        self._apple = Apple()
        self._board = Board(board_size, board_margin)
        self._snake = Snake(self._board.get_size())

        self._snake.draw_on_board(self._board, False)
        self._apple.replace(self._board)

    def update(self, event: Event) -> None:
        if self._is_running:
            move_direction_change = self._controller.process_event(event)

            if move_direction_change is not None:
                self._snake.change_direction(move_direction_change)

            try:
                self._snake.update(event)

            except ValueError:
                self._pygame_instance.event.post(Event(END_GAME))
                self._game_over = True
                self._is_running = False

            if self._snake.get_head() == self._apple.get_coord():
                self._pygame_instance.event.post(Event(EAT_APPLE))
                self._apple.replace(self._board)

    def draw(self, surface: Surface) -> None:
        self._snake.draw_on_board(self._board, True)
        self._apple.draw_on_board(self._board, False)
        self._board.draw(surface)

    def switch_game_running_state(self):
        self._is_running = not self._is_running
