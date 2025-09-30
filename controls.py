import pygame
import sys
from bullet import Bullet
from inv import Inv
import time


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

def update_bullets(screen, invs, bullets):
    # обновлять позиции пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, invs, True, True)
    if len(invs) == 0:
        bullets.empty()
        create_army(screen, invs)

def gun_kill(stats, screen, gun, invs, bullets):
    # столкновение пушки и армии
    stats.guns_left -= 1
    invs.empty()
    bullets.empty()
    create_army(screen, invs)
    gun.create_gun()
    time.sleep(1)

def update_invs(stats, screen, gun, invs, bullets):
    # обновляет позицию пришельцев
    invs.update()
    if pygame.sprite.spritecollideany(gun, invs):
        gun_kill(stats, screen, gun, invs, bullets)
    invs_check(stats, screen, gun, invs, bullets)

def invs_check(stats, screen, gun, invs, bullets):
    # проверка - добралась ли арми я до конца экрана?
    screen_rect = screen.get_rect()
    for inv in invs.sprites():
        if inv.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, invs, bullets)
            break

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
