import pygame
import sys
from bullet import Bullet
from inv import Inv

def events(screen, gun, bullets):
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # вправо
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # вправо
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False


def update(bg_color, screen, gun, invs, bullets):
    # обновление экрана
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    invs.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    # обновлять позиции пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_invs(invs):
    # обновляет позицию пришельцев
    invs.update()

def create_army(screen, invs):
    # создание армии клонов
    inv = Inv(screen)
    inv_width = inv.rect.width
    number_inv_x = int((700 - 2 * inv_width) / inv_width)
    inv_height = inv.rect.height
    number_inv_y = int((800 - 100 - 2 * inv_height) / inv_height)

    for row_number in range(number_inv_y - 3):
        for inv_number in range(number_inv_x):
            inv = Inv(screen)
            inv.x = inv_width + (inv_width * inv_number)
            inv.y = inv_width + (inv_width * row_number)
            inv.rect.x = inv.x
            inv.rect.y = inv.rect.height + inv.rect.height * row_number
            invs.add(inv)