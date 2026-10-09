"""Plataforma móvil.

Es parte del Model: se desplaza en línea recta (horizontal o vertical)
entre dos límites. No dibuja ni suena. Quien la usa (Level) se encarga
de arrastrar al jugador cuando está encima.
"""

import pygame


class MovingPlatform:
    def __init__(self, x, y, width, height, axis, span, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.axis = axis                    # "x" (horizontal) o "y" (vertical)
        self.start_limit, self.end_limit = span
        self.speed = speed
        self.direction = 1

    def update(self):
        """Avanza un paso y devuelve cuánto se movió: (dx, dy)."""
        old_x, old_y = self.rect.x, self.rect.y

        if self.axis == "x":
            self.rect.x += self.direction * self.speed
            if self.rect.right >= self.end_limit:
                self.rect.right = self.end_limit
                self.direction = -1
            elif self.rect.left <= self.start_limit:
                self.rect.left = self.start_limit
                self.direction = 1
        else:
            self.rect.y += self.direction * self.speed
            if self.rect.bottom >= self.end_limit:
                self.rect.bottom = self.end_limit
                self.direction = -1
            elif self.rect.top <= self.start_limit:
                self.rect.top = self.start_limit
                self.direction = 1

        return self.rect.x - old_x, self.rect.y - old_y