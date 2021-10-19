import pygame

from Game_Parts import Game

from CONSTANTS import SIZE, FPS, BACKGROUND_COLOR


pygame.init()
SCREEN = pygame.display.set_mode(SIZE)
CLOCK = pygame.time.Clock()
RUNNING = True

GAME = Game()


if __name__ == "__main__":
    while RUNNING:
        SCREEN.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

            GAME.update(event)

        GAME.draw(SCREEN)

        pygame.display.flip()
        CLOCK.tick(FPS)

    pygame.quit()
