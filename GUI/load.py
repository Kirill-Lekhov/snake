from pygame import Color

from constants import START_GAME, EAT_APPLE, BACK_TO_MAIN_MENU
from . import GameGUI, Label, Button, Counter, Stopwatch


def load_main_menu(screen_size: tuple, screen_background_color, pygame) -> GameGUI:
    width, height = screen_size
    gui = GameGUI()

    # screen height // 2 - number of elements * elements height
    top_margin = height // 2 - (2 * 50) // 1.5

    label_length = 200
    gui.add_element(Label((width//2 - label_length//2, top_margin, label_length, 50), "Snake Game", -1,
                          Color("purple")))

    button_length = 100
    gui.add_element(Button((width//2 - button_length//2, top_margin + 50, button_length, 50), "Start!", START_GAME,
                           pygame, Color("purple"), screen_background_color))

    return gui


def load_game_gui(screen_size: tuple) -> GameGUI:
    width, height = screen_size
    gui = GameGUI()

    # screen height // 2 - number of elements * elements height
    top_margin = height // 2 - (2 * 50) // 1.5

    counter_length = 200
    gui.add_element(Counter((400, top_margin, counter_length, 50), EAT_APPLE, -1, Color("purple")))

    stopwatch_length = 100
    gui.add_element(Stopwatch((400, top_margin + 50, stopwatch_length, 50), -1, Color("purple")))

    return gui


def load_end_game(screen_size: tuple, screen_background_color, pygame, score, time) -> GameGUI:
    width, height = screen_size
    gui = GameGUI()

    # screen height // 2 - number of elements * elements height
    top_margin = height // 2 - (3 * 50) // 1.5

    label_length = 200
    gui.add_element(Label((width // 2 - label_length // 2, top_margin, label_length, 50), f"Score: {score}", -1,
                          Color("purple")))
    gui.add_element(Label((width // 2 - label_length // 2, top_margin + 50, label_length, 50), f"Time: {time}", -1,
                          Color("purple")))

    button_length = 225
    gui.add_element(Button((width // 2 - button_length // 2, top_margin + 100, button_length, 50), "To main menu",
                           BACK_TO_MAIN_MENU, pygame, Color("purple"), screen_background_color))

    return gui

