import pygame

from Game_Parts import Game

from CONSTANTS import SIZE, FPS, BACKGROUND_COLOR
from Game_Parts.EVENTS import STEP_EVENT


pygame.init()
SCREEN = pygame.display.set_mode(SIZE)
CLOCK = pygame.time.Clock()
RUNNING = True

pygame.time.set_timer(STEP_EVENT, 250)

GAME = Game(pygame, SIZE)


if __name__ == "__main__":
    while RUNNING:
        SCREEN.fill(BACKGROUND_COLOR)

        events = sorted(pygame.event.get(), key=lambda x: x.type)

        for event in events:
            if event.type == pygame.QUIT:
                RUNNING = False

            GAME.update(event)

        GAME.draw(SCREEN)

        pygame.display.flip()
        CLOCK.tick(FPS)

    pygame.quit()
