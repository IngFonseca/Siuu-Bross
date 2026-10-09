"""Carga de imágenes, fuentes y sonidos de Siuu.Bross.

Solo usa archivos que ya existen en assets/. El sprite del enemigo y
el del jugador mirando a la izquierda se derivan por código de cr7.png;
no se crea ningún archivo nuevo.

IMPORTANTE: crear Assets() solo después de pygame.display.set_mode(),
porque convert() y convert_alpha() necesitan la ventana.
"""

import pygame

import config


class Assets:
    def __init__(self):
        # ----- Imágenes -----
        self.background = self._load(config.IMG_BACKGROUND,
                                     (config.WIDTH, config.HEIGHT), alpha=False)
        self.terror = self._load(config.IMG_TERROR,
                                 (config.WIDTH, config.HEIGHT), alpha=False)
        self.ball = self._load(config.IMG_BALL, config.BALL_SIZE)
        self.goal = self._load(config.IMG_GOAL, config.GOAL_SIZE)
        self.heart = self._load(config.IMG_HEART, config.HEART_SIZE)

        # Jugador: el sprite original mira a la derecha
        self.player_right = self._load(config.IMG_PLAYER, config.PLAYER_SIZE)
        self.player_left = pygame.transform.flip(self.player_right, True, False)

        # Enemigo: el mismo sprite tintado de rojo (derivado por código)
        self.enemy_right = self._tint_red(self.player_right)
        self.enemy_left = self._tint_red(self.player_left)

        # ----- Fuentes -----
        self.font_title = pygame.font.SysFont(None, 60)
        self.font_text = pygame.font.SysFont(None, 28)
        self.font_button = pygame.font.SysFont(None, 40)

        # ----- Sonidos (la música se carga en audio_view) -----
        self.snd_ball = pygame.mixer.Sound(config.sound_path(config.SND_BALL))
        self.snd_goal = pygame.mixer.Sound(config.sound_path(config.SND_GOAL))
        self.snd_scream = pygame.mixer.Sound(config.sound_path(config.SND_SCREAM))

    @staticmethod
    def _load(filename, size, alpha=True):
        """Carga una imagen de assets/images y la escala a 'size'."""
        image = pygame.image.load(config.image_path(filename))
        image = image.convert_alpha() if alpha else image.convert()
        return pygame.transform.smoothscale(image, size)

    @staticmethod
    def _tint_red(surface):
        """Devuelve una copia de la imagen tintada de rojo."""
        tinted = surface.copy()
        tinted.fill((255, 70, 70, 255), special_flags=pygame.BLEND_RGBA_MULT)
        return tinted