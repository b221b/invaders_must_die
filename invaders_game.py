import pygame, controls
from gun import Gun
from pygame.sprite import Group

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Invaders must die")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        bullets.update()
        controls.update(bg_color, screen, gun, bullets)

if __name__ == "__main__":
    run()
