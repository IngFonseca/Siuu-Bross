"""Dibujo del mundo de juego y del HUD.

Es parte de la View: solo LEE el GameModel. No cambia el estado del
juego, no lee el teclado y no hace display.flip() (eso lo hace el
Controller al final de cada frame).
"""

import math

import pygame

import config
from models.game_model import State
from views.screens_view import ScreensView
from views.ui import draw_text


class GameView:
    def __init__(self, screen, assets):
        self.screen = screen
        self.assets = assets
        self.screens = ScreensView(screen, assets)
        self.camera_x = 0   # desplazamiento horizontal del mundo

    # ------------------------------------------------------------------
    # Punto de entrada
    # ------------------------------------------------------------------
    def draw(self, model):
        state = model.state

        # Pantallas completas: no se ve el mundo de juego
        if state in (State.MENU, State.GAME_OVER, State.VICTORY):
            self.screens.draw(model)
            return

        # Mundo de juego (también debajo de la pausa y del nivel completado)
        self.camera_x = self.camera_for(model.player.rect.centerx, model.level.width)
        self.screen.blit(self.assets.background, (0, 0))
        self._draw_world(model)
        self._draw_hud(model)
        if state == State.PLAYING:
            self._draw_level_banner(model)

        if state in (State.PAUSED, State.LEVEL_COMPLETE):
            self.screens.draw(model)

    def button_at(self, state, pos):
        """Identificador del botón bajo 'pos' en la pantalla actual."""
        return self.screens.button_at(state, pos)

    # ------------------------------------------------------------------
    # Cámara
    # ------------------------------------------------------------------
    @staticmethod
    def camera_for(target_x, level_width):
        """Desplazamiento que mantiene a 'target_x' centrado en pantalla,
        sin salirse de los bordes del nivel."""
        return max(0, min(target_x - config.WIDTH // 2, level_width - config.WIDTH))

    # ------------------------------------------------------------------
    # Mundo
    # ------------------------------------------------------------------
    def _shift(self, rect):
        """Devuelve el rect desplazado según la cámara."""
        return rect.move(-self.camera_x, 0)

    def _draw_world(self, model):
        level = model.level
        player = model.player

        for platform in level.platforms:
            r = self._shift(platform)
            if r.right < 0 or r.left > config.WIDTH:
                continue
            pygame.draw.rect(self.screen, config.GRAY, r)
            pygame.draw.rect(self.screen, config.BLACK, r, 2)

        for moving in level.moving_platforms:
            r = self._shift(moving.rect)
            pygame.draw.rect(self.screen, config.PLATFORM_MOVING, r)
            pygame.draw.rect(self.screen, config.BLACK, r, 2)

        for spike in level.spikes:
            r = self._shift(spike)
            if r.right < 0 or r.left > config.WIDTH:
                continue
            points = [(r.x, r.bottom), (r.x + r.width // 2, r.top), (r.right, r.bottom)]
            pygame.draw.polygon(self.screen, config.RED, points)
            pygame.draw.polygon(self.screen, config.BLACK, points, 2)

        for heart in level.hearts:
            if not heart.taken:
                self.screen.blit(self.assets.heart, self._shift(heart.rect).topleft)

        self.screen.blit(self.assets.goal, self._shift(level.goal).topleft)

        for enemy in level.enemies:
            if enemy.alive:
                enemy_sprite = (self.assets.enemy_right if enemy.direction == 1
                                else self.assets.enemy_left)
                self.screen.blit(enemy_sprite, self._shift(enemy.rect).topleft)

        sprite = (self.assets.player_right if player.facing == 1
                  else self.assets.player_left)
        self.screen.blit(sprite, self._shift(player.rect).topleft)

        # Los balones se dibujan después para verse delante del jugador
        for ball in level.balls:
            self.screen.blit(self.assets.ball, self._shift(ball.rect).topleft)

    # ------------------------------------------------------------------
    # HUD
    # ------------------------------------------------------------------
    def _draw_hud(self, model):
        font = self.assets.font_text

        lines = [
            f"Nivel {model.level_number}/{model.total_levels}",
            f"Puntos: {model.score}",
            f"Balones: {model.level.balls_taken}/{model.level.balls_total}",
        ]
        for i, text in enumerate(lines):
            surface = font.render(text, True, config.BLACK)
            self.screen.blit(surface, (10, 10 + i * 24))

        for i in range(model.lives):
            self.screen.blit(self.assets.heart,
                             (config.WIDTH - 35 * (i + 1), 10))

        if model.time_left is not None:
            seconds = math.ceil(model.time_left)
            color = config.RED if seconds <= 10 else config.BLACK
            draw_text(self.screen, self.assets.font_button,
                      f"Tiempo: {seconds}", color, (config.WIDTH // 2, 25))

    def _draw_level_banner(self, model):
        """Nombre del nivel y pista durante los primeros 3 segundos."""
        if model.level_frames >= 3 * config.FPS:
            return
        cx = config.WIDTH // 2
        draw_text(self.screen, self.assets.font_button,
                  f"Nivel {model.level_number}: {model.level.name}", config.BLACK, (cx, 75))
        if model.level.hint:
            draw_text(self.screen, self.assets.font_text,
                      model.level.hint, config.BLACK, (cx, 105))