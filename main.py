"""Punto de entrada de Siuu.Bross.

Crea las piezas del MVC y las conecta. No contiene lógica de juego.

Ejecutar con:  python main.py
"""

import sys

import pygame

import config
from controllers.game_controller import GameController
from controllers.input_controller import InputController
from models.game_model import GameModel
from views.assets import Assets
from views.audio_view import AudioView
from views.game_view import GameView


def main():
    pygame.init()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption(config.TITLE)

    # Los recursos se cargan después de crear la ventana
    assets = Assets()

    model = GameModel()
    view = GameView(screen, assets)
    audio = AudioView(assets)
    controller = GameController(model, view, audio, InputController())

    controller.run()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()