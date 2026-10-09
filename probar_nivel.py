"""Herramienta de desarrollo: lanza el juego directamente en un nivel.

Uso:  python probar_nivel.py 3
"""

import sys

import pygame

import config
from controllers.game_controller import GameController
from controllers.input_controller import InputController
from levels import LEVELS
from models.game_model import GameModel
from views.assets import Assets
from views.audio_view import AudioView
from views.game_view import GameView


def main():
    numero = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    if not 1 <= numero <= len(LEVELS):
        print(f"El nivel debe estar entre 1 y {len(LEVELS)}")
        return

    pygame.init()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption(f"{config.TITLE} - prueba del nivel {numero}")
    assets = Assets()

    model = GameModel()
    model.start_game()
    model.load_level(numero - 1)

    GameController(model, GameView(screen, assets), AudioView(assets),
                   InputController()).run()
    pygame.quit()


if __name__ == "__main__":
    main()