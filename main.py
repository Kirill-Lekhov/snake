import pygame

from GUI.load import load_main_menu, load_game_gui, load_end_game
from Game_Parts import Game

from CONSTANTS import SIZE, FPS, BACKGROUND_COLOR, SNAKE_STEP_DELAY
from EVENTS import STEP_EVENT, START_GAME, TIMER_UPDATE, END_GAME, BACK_TO_MAIN_MENU


pygame.init()
pygame.display.set_caption("PyGame Snake 1.0.0")
pygame.display.set_icon(pygame.image.load("game_logo.png"))
SCREEN = pygame.display.set_mode(SIZE)
CLOCK = pygame.time.Clock()
RUNNING = True

pygame.time.set_timer(STEP_EVENT, SNAKE_STEP_DELAY)
pygame.time.set_timer(TIMER_UPDATE, 1000)

GAME = None
GUI = load_main_menu(SIZE, BACKGROUND_COLOR, pygame)


if __name__ == "__main__":
    while RUNNING:
        SCREEN.fill(BACKGROUND_COLOR)

        events = sorted(pygame.event.get(), key=lambda x: x.type)

        for event in events:
            if event.type == pygame.QUIT:
                RUNNING = False

            if event.type == START_GAME:
                GUI = load_game_gui(SIZE)
                GAME = Game(pygame, (400, 400))

            elif event.type == END_GAME:
                states = GUI.get_state()
                GUI = load_end_game(SIZE, BACKGROUND_COLOR, pygame, *states)
                GAME = None

            elif event.type == BACK_TO_MAIN_MENU:
                GUI = load_main_menu(SIZE, BACKGROUND_COLOR, pygame)

            GUI.update(event)

            if GAME is not None:
                GAME.update(event)

        GUI.draw(SCREEN)

        if GAME is not None:
            GAME.draw(SCREEN)

        pygame.display.flip()
        CLOCK.tick(FPS)

    pygame.quit()
