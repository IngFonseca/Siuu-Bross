"""Bucle principal y coordinación entre Model, View y entrada.

Es parte del Controller. Decide qué hacer según el estado del juego,
pero no calcula física (eso es del Model) ni dibuja (eso es de la View).
"""

import pygame

import config
from models.game_model import State


class GameController:
    def __init__(self, model, view, audio, input_controller):
        self.model = model
        self.view = view
        self.audio = audio
        self.input = input_controller
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        """Bucle principal. Termina al cerrar la ventana o pulsar Salir."""
        self.audio.play_music()
        while self.running:
            entrada = self.input.poll()
            if entrada.quit:
                break

            self._handle_input(entrada)
            self.audio.play_events(self.model.pop_events())

            self.view.draw(self.model)
            pygame.display.flip()
            self.clock.tick(config.FPS)

    # ------------------------------------------------------------------
    # Entrada según el estado
    # ------------------------------------------------------------------
    def _handle_input(self, entrada):
        model = self.model
        state = model.state

        # ¿Hizo clic en algún botón de la pantalla actual?
        action = None
        if entrada.click is not None:
            action = self.view.button_at(state, entrada.click)

        if state == State.MENU:
            if action == "play" or entrada.confirm:
                model.start_game()
            elif action == "quit":
                self.running = False

        elif state == State.PLAYING:
            if entrada.pause:
                model.pause()
                self.audio.set_paused(True)
            else:
                if entrada.restart:
                    model.restart_level()
                model.update(entrada.direction, entrada.jump)

        elif state == State.PAUSED:
            if entrada.pause or action == "resume":
                model.resume()
                self.audio.set_paused(False)
            elif entrada.restart or action == "restart":
                model.restart_level()
                self.audio.set_paused(False)
            elif action == "menu":
                model.go_to_menu()
                self.audio.set_paused(False)

        elif state == State.LEVEL_COMPLETE:
            if entrada.any_key or action == "next":
                self.audio.stop_goal()
                model.next_level()

        elif state == State.GAME_OVER:
            if action == "retry" or entrada.confirm:
                model.retry_level()
            elif action == "menu":
                model.go_to_menu()

        elif state == State.VICTORY:
            if action == "menu" or entrada.confirm:
                self.audio.stop_effects()
                model.go_to_menu()