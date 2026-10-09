"""Elementos de interfaz reutilizables: texto centrado y botones.

Es parte de la View: solo DIBUJA y responde "¿está este punto dentro
del botón?". No decide qué ocurre al pulsarlo (eso es del Controller).
"""

import pygame

import config


def draw_text(screen, font, text, color, center):
    """Dibuja texto centrado en el punto 'center'."""
    surface = font.render(text, True, color)
    screen.blit(surface, surface.get_rect(center=center))


class Button:
    def __init__(self, action, text, center, size=(260, 56)):
        self.action = action                 # identificador, p. ej. "play"
        self.text = text
        self.rect = pygame.Rect(0, 0, *size)
        self.rect.center = center

    def contains(self, pos):
        return self.rect.collidepoint(pos)

    def draw(self, screen, font, mouse_pos):
        hovered = self.contains(mouse_pos)
        color = config.DARK_RED if hovered else config.RED
        pygame.draw.ellipse(screen, color, self.rect)
        draw_text(screen, font, self.text, config.WHITE, self.rect.center)