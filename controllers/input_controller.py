"""Lectura del teclado y el ratón, traducida a acciones simples.

Es parte del Controller. Solo LEE la entrada del jugador: no decide qué
significa cada acción en cada pantalla (eso lo hace GameController) ni
modifica el Model.
"""

import pygame


class InputState:
    """Resumen de lo que hizo el jugador durante un frame."""

    def __init__(self):
        self.quit = False        # cerró la ventana
        self.direction = 0       # -1 izquierda, 0 quieto, 1 derecha
        self.jump = False        # mantiene pulsada una tecla de salto
        self.restart = False     # pulsó R
        self.pause = False       # pulsó P o ESC
        self.confirm = False     # pulsó ENTER
        self.any_key = False     # pulsó cualquier tecla
        self.click = None        # (x, y) del clic izquierdo, o None


class InputController:
    def poll(self):
        """Lee los eventos pendientes y el estado del teclado."""
        state = InputState()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.quit = True

            elif event.type == pygame.KEYDOWN:
                state.any_key = True
                if event.key == pygame.K_r:
                    state.restart = True
                elif event.key in (pygame.K_p, pygame.K_ESCAPE):
                    state.pause = True
                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    state.confirm = True

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                state.click = event.pos

        keys = pygame.key.get_pressed()
        left = keys[pygame.K_LEFT] or keys[pygame.K_a]
        right = keys[pygame.K_RIGHT] or keys[pygame.K_d]
        state.direction = int(right) - int(left)
        state.jump = bool(keys[pygame.K_SPACE] or keys[pygame.K_UP]
                          or keys[pygame.K_w])

        return state