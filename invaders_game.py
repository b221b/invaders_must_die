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
    inv = Group()
    controls.create_army(screen, inv)

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, inv, bullets)
        controls.update_bullets(bullets)
        controls.update_invs(inv)

if __name__ == "__main__":
    run()
