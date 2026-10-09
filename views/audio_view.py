"""Reproducción de música y efectos de sonido.

Es parte de la View: traduce los eventos del Model en sonidos. Usa
solo los audios que ya existen en assets/sounds/.
"""

import pygame

import config
from models import events


class AudioView:
    def __init__(self, assets):
        self.assets = assets

        # Evento del Model -> sonido existente. Los eventos que no están
        # aquí (jump, hurt, game_over) no tienen audio disponible.
        self._effects = {
            events.BALL_PICKED: assets.snd_ball,
            events.HEART_PICKED: assets.snd_ball,
            events.ENEMY_DEFEATED: assets.snd_ball,
            events.GOAL: assets.snd_goal,
            events.VICTORY: assets.snd_scream,
        }

    # ----- Música -----
    def play_music(self):
        """Inicia la música de fondo en bucle."""
        pygame.mixer.music.load(config.sound_path(config.SND_MUSIC))
        pygame.mixer.music.set_volume(config.MUSIC_VOLUME)
        pygame.mixer.music.play(-1)

    def set_paused(self, paused):
        """Baja el volumen de la música mientras el juego está en pausa."""
        volume = config.MUSIC_VOLUME_PAUSED if paused else config.MUSIC_VOLUME
        pygame.mixer.music.set_volume(volume)

    # ----- Efectos -----
    def play_events(self, event_list):
        """Reproduce el sonido de cada evento que tenga uno asignado."""
        for event in event_list:
            sound = self._effects.get(event)
            if sound is not None:
                sound.play()

    def stop_goal(self):
        """Corta el sonido del gol (al pasar de nivel)."""
        self.assets.snd_goal.stop()

    def stop_effects(self):
        """Corta todos los efectos que estén sonando (no la música)."""
        pygame.mixer.stop()