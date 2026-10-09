"""Pantallas del juego: menú, pausa, nivel completado, game over y victoria.

Es parte de la View: dibuja y sabe en qué botón se hizo clic, pero no
decide qué ocurre después (eso es del Controller).
"""

import pygame

import config
from models.game_model import State
from views.ui import Button, draw_text


class ScreensView:
    def __init__(self, screen, assets):
        self.screen = screen
        self.assets = assets
        cx = config.WIDTH // 2

        # Capa oscura semitransparente para pausa y nivel completado
        self._overlay = pygame.Surface((config.WIDTH, config.HEIGHT), pygame.SRCALPHA)
        self._overlay.fill((0, 0, 0, 160))

        # Botones de cada pantalla. El primer dato es el identificador
        # que el Controller recibirá cuando se haga clic.
        self._buttons = {
            State.MENU: [
                Button("play", "Jugar", (cx, 200)),
                Button("quit", "Salir", (cx, 270)),
            ],
            State.PAUSED: [
                Button("resume", "Continuar", (cx, 170)),
                Button("restart", "Reiniciar nivel", (cx, 240)),
                Button("menu", "Menú principal", (cx, 310)),
            ],
            State.LEVEL_COMPLETE: [
                Button("next", "Continuar", (cx, 335)),
            ],
            State.GAME_OVER: [
                Button("retry", "Reintentar nivel", (cx, 240)),
                Button("menu", "Menú principal", (cx, 310)),
            ],
            State.VICTORY: [
                Button("menu", "Menú principal", (cx, 350)),
            ],
        }

        self._drawers = {
            State.MENU: self._draw_menu,
            State.PAUSED: self._draw_paused,
            State.LEVEL_COMPLETE: self._draw_level_complete,
            State.GAME_OVER: self._draw_game_over,
            State.VICTORY: self._draw_victory,
        }

    # ------------------------------------------------------------------
    # Interfaz pública
    # ------------------------------------------------------------------
    def button_at(self, state, pos):
        """Devuelve el identificador del botón bajo 'pos', o None."""
        for button in self._buttons.get(state, []):
            if button.contains(pos):
                return button.action
        return None

    def draw(self, model):
        """Dibuja la pantalla correspondiente al estado del modelo."""
        drawer = self._drawers.get(model.state)
        if drawer is None:
            return
        drawer(model)

        mouse = pygame.mouse.get_pos()
        for button in self._buttons[model.state]:
            button.draw(self.screen, self.assets.font_button, mouse)

    # ------------------------------------------------------------------
    # Pantallas
    # ------------------------------------------------------------------
    def _text(self, font, text, color, y):
        draw_text(self.screen, font, text, color, (config.WIDTH // 2, y))

    def _draw_menu(self, model):
        self.screen.blit(self.assets.background, (0, 0))
        self._text(self.assets.font_title, "SIUU.BROSS", config.BLACK, 80)
        self._text(self.assets.font_text,
                   "Lleva el balón hasta la portería", config.BLACK, 125)
        self._text(self.assets.font_text,
                   "Flechas mover    ESPACIO saltar    R reiniciar    P pausa",
                   config.BLACK, 370)

    def _draw_paused(self, model):
        self.screen.blit(self._overlay, (0, 0))
        self._text(self.assets.font_title, "PAUSA", config.WHITE, 90)

    def _draw_level_complete(self, model):
        self.screen.blit(self._overlay, (0, 0))
        points = model.level_points
        self._text(self.assets.font_title, "¡GOOOOOOOOL!", config.WHITE, 40)
        self._text(self.assets.font_text,
                   f"Nivel {model.level_number} completado", config.WHITE, 80)

        lines = [
            f"Balones: +{points['balls']}",
            f"Enemigos: +{points['enemies']}",
            f"Gol: +{points['goal']}",
            f"Vidas restantes: +{points['lives']}",
        ]
        if points["time"] > 0:
            lines.append(f"Tiempo: +{points['time']}")

        y = 112
        for text in lines:
            self._text(self.assets.font_text, text, config.WHITE, y)
            y += 22
        self._text(self.assets.font_title, f"Total del nivel: {model.level_total}",
                   config.WHITE, y + 18)
        self._text(self.assets.font_text,
                   f"Puntos acumulados: {model.score}", config.GRAY, y + 50)
        self._text(self.assets.font_text,
                   "Presiona cualquier tecla para continuar", config.GRAY, 385)

    def _draw_game_over(self, model):
        self.screen.fill(config.BLACK)
        self._text(self.assets.font_title, "¡GAME OVER!", config.RED, 110)
        self._text(self.assets.font_text,
                   f"Te quedaste en el nivel {model.level_number}",
                   config.WHITE, 170)

    def _draw_victory(self, model):
        self.screen.blit(self.assets.terror, (0, 0))
        self._text(self.assets.font_text,
                   f"Puntuación final: {model.score}", config.WHITE, 25)