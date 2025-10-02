import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Invaders must die")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inv = Group()
    controls.create_army(screen, inv)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, inv, bullets)
            controls.update_bullets(screen, stats, sc, inv, bullets)
            controls.update_invs(stats, screen, sc, gun, inv, bullets)

if __name__ == "__main__":
    run()
