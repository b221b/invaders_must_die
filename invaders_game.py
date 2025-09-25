import pygame, controls
from gun import Gun


def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Invaders must die")
    bg_color = (0, 0, 0)

    gun = Gun(screen)

    while True:
        controls.events(gun)
        gun.update_gun()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()


if __name__ == "__main__":
    run()
