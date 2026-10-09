"""Nivel jugable: convierte los datos de levels/ en objetos con colisiones.

Es parte del Model. No dibuja ni suena: solo responde preguntas como
"¿toca el jugador un pincho?" o "¿llegó a la portería con los balones?".
"""

import pygame

import config
from models.enemy import Enemy
from models.moving_platform import MovingPlatform


class Ball:
    """Un balón recogible. Cuando se recoge, sigue al jugador."""

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, *config.BALL_SIZE)
        self.taken = False


class Heart:
    """Un corazón recogible: da una vida extra."""

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, *config.HEART_SIZE)
        self.taken = False


class Level:
    def __init__(self, data):
        self.name = data["name"]
        self.difficulty = data["difficulty"]
        self.hint = data.get("hint", "")
        self.width = data["width"]
        self.start = data["start"]
        self.time_limit = data.get("time_limit")

        self.platforms = [pygame.Rect(*p) for p in data["platforms"]]
        self.goal = pygame.Rect(*data["goal"], *config.GOAL_SIZE)
        self.balls = [Ball(x, y) for (x, y) in data["balls"]]
        self.hearts = [Heart(x, y) for (x, y) in data.get("hearts", [])]
        self.spikes = self._build_spikes(data)
        self.enemies = self._build_enemies(data)
        self.moving_platforms = self._build_moving_platforms(data)

    def _build_enemies(self, data):
        """Crea los enemigos. Velocidad: la del campo 'speed' si existe;
        si no, la que corresponde a la dificultad del nivel."""
        default_speed = config.ENEMY_SPEED[self.difficulty]
        return [
            Enemy(e["x"], e["y"], e["patrol"], e.get("speed", default_speed))
            for e in data.get("enemies", [])
        ]

    def _build_moving_platforms(self, data):
        """Crea las plataformas móviles (misma regla de velocidad)."""
        default_speed = config.PLATFORM_SPEED[self.difficulty]
        return [
            MovingPlatform(m["x"], m["y"], m["w"], m["h"], m["axis"],
                           m["range"], m.get("speed", default_speed))
            for m in data.get("moving_platforms", [])
        ]

    @staticmethod
    def _build_spikes(data):
        """Pinchos sueltos + tramos de pinchos en el suelo."""
        size = config.SPIKE_SIZE
        spikes = [pygame.Rect(x, y, size, size) for (x, y) in data["spikes"]]
        for x_from, x_to in data["floor_spikes"]:
            for x in range(x_from, x_to, size):
                spikes.append(pygame.Rect(x, config.HEIGHT - size, size, size))
        return spikes

    # ----- Sólidos -----
    @property
    def solids(self):
        """Rects contra los que el jugador choca: plataformas fijas y móviles."""
        return self.platforms + [m.rect for m in self.moving_platforms]

    # ----- Plataformas móviles -----
    def update_platforms(self, player):
        """Mueve las plataformas y arrastra al jugador si va encima.

        Debe llamarse ANTES de actualizar al jugador en cada frame."""
        pr = player.rect
        for platform in self.moving_platforms:
            mr = platform.rect
            riding = (player.on_ground
                      and pr.bottom == mr.top
                      and pr.right > mr.left
                      and pr.left < mr.right)

            dx, dy = platform.update()

            if riding:
                pr.x += dx
                pr.y += dy
            elif pr.colliderect(mr):
                # La plataforma empuja al jugador en su dirección de avance
                if platform.axis == "x":
                    if dx > 0:
                        pr.left = mr.right
                    else:
                        pr.right = mr.left
                else:
                    if dy < 0:
                        pr.bottom = mr.top
                    else:
                        pr.top = mr.bottom

    # ----- Enemigos -----
    def update_enemies(self):
        for enemy in self.enemies:
            enemy.update()

    # ----- Pinchos -----
    def touches_spikes(self, rect):
        return any(rect.colliderect(s) for s in self.spikes)

    # ----- Corazones -----
    def touching_hearts(self, rect):
        """Corazones aún sin recoger que toca rect."""
        return [h for h in self.hearts
                if not h.taken and rect.colliderect(h.rect)]

    # ----- Balones -----
    @property
    def balls_total(self):
        return len(self.balls)

    @property
    def balls_taken(self):
        return sum(1 for b in self.balls if b.taken)

    @property
    def all_balls_taken(self):
        return self.balls_taken == self.balls_total

    def collect_balls(self, rect):
        """Marca como recogidos los balones que toca rect.
        Devuelve cuántos balones nuevos se recogieron."""
        picked = 0
        for ball in self.balls:
            if not ball.taken and rect.colliderect(ball.rect):
                ball.taken = True
                picked += 1
        return picked

    def carry_balls(self, player_rect):
        """Los balones recogidos acompañan al jugador."""
        n = 0
        for ball in self.balls:
            if ball.taken:
                ball.rect.x = player_rect.x + 10 + n * 8
                ball.rect.y = player_rect.y + 30
                n += 1

    # ----- Portería -----
    def reached_goal(self, rect):
        """True si el jugador toca la portería con todos los balones."""
        return self.all_balls_taken and rect.colliderect(self.goal)