"""Enemigo patrullero.

Es parte del Model: se mueve de un lado a otro entre dos límites y sabe
si el jugador lo está pisando. No dibuja ni suena.
"""

import pygame

import config


class Enemy:
    def __init__(self, x, y, patrol, speed):
        self.rect = pygame.Rect(x, y, *config.ENEMY_SIZE)
        self.left_limit, self.right_limit = patrol
        self.speed = speed
        self.direction = 1          # 1 = derecha, -1 = izquierda
        self.alive = True

    def update(self):
        """Avanza un paso y da la vuelta al llegar a un límite."""
        if not self.alive:
            return
        self.rect.x += self.direction * self.speed
        if self.rect.right >= self.right_limit:
            self.rect.right = self.right_limit
            self.direction = -1
        elif self.rect.left <= self.left_limit:
            self.rect.left = self.left_limit
            self.direction = 1

    def is_stomped_by(self, player):
        """True si el jugador cae sobre la parte superior del enemigo.

        Debe estar cayendo y haber penetrado poco: así se distingue un
        pisotón de un choque lateral."""
        falling = player.vel_y > 0
        penetration = player.rect.bottom - self.rect.top
        return falling and penetration <= max(12, int(player.vel_y) + 6)