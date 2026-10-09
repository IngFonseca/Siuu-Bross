"""Jugador (CR7): posición, velocidad, salto y colisiones con sólidos.

Es parte del Model: usa pygame.Rect solo como geometría. No dibuja,
no suena y no lee el teclado.
"""

import pygame

import config
from models import events


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, *config.PLAYER_SIZE)
        self.vel_y = 0.0
        self.on_ground = False
        self.facing = 1  # 1 = mira a la derecha, -1 = a la izquierda

    def reset(self, x, y):
        """Devuelve al jugador a una posición inicial, quieto."""
        self.rect.topleft = (x, y)
        self.vel_y = 0.0
        self.on_ground = False
        self.facing = 1

    def jump(self):
        """Salta si está en el suelo. Devuelve True si saltó."""
        if self.on_ground:
            self.vel_y = config.JUMP_FORCE
            self.on_ground = False
            return True
        return False

    def bounce(self):
        """Pequeño rebote tras pisar a un enemigo."""
        self.vel_y = config.JUMP_FORCE * 0.6
        self.on_ground = False

    def move_x(self, direction, solids, world_width):
        """Mueve en horizontal (-1, 0 o 1) y resuelve choques laterales."""
        dx = direction * config.PLAYER_SPEED
        if dx == 0:
            return
        self.facing = 1 if dx > 0 else -1
        self.rect.x += dx

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > world_width:
            self.rect.right = world_width

        for solid in solids:
            if self.rect.colliderect(solid):
                if dx > 0:
                    self.rect.right = solid.left
                else:
                    self.rect.left = solid.right

    def move_y(self, solids, floor_y=config.HEIGHT):
        """Aplica gravedad, mueve en vertical y resuelve choques."""
        self.vel_y += config.GRAVITY
        dy = int(round(self.vel_y))
        self.rect.y += dy

        # Techo de la pantalla
        if self.rect.top < 0:
            self.rect.top = 0
            self.vel_y = 0.0

        # Choques con plataformas: se resuelven según la dirección real
        for solid in solids:
            if self.rect.colliderect(solid):
                if dy > 0:            # cayendo: aterriza encima
                    self.rect.bottom = solid.top
                elif dy < 0:          # subiendo: se golpea la cabeza
                    self.rect.top = solid.bottom
                self.vel_y = 0.0

        # Suelo del escenario
        if self.rect.bottom >= floor_y:
            self.rect.bottom = floor_y
            self.vel_y = 0.0

        # ¿Está apoyado? Se comprueba con una "sonda" de 1 px hacia abajo
        probe = self.rect.move(0, 1)
        self.on_ground = (
            self.rect.bottom >= floor_y
            or any(probe.colliderect(s) for s in solids)
        )

    def update(self, direction, want_jump, solids, world_width):
        """Un paso de física. Devuelve la lista de eventos ocurridos."""
        occurred = []
        if want_jump and self.jump():
            occurred.append(events.JUMP)
        self.move_x(direction, solids, world_width)
        self.move_y(solids)
        return occurred