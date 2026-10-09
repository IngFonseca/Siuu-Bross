"""Configuración global de Siuu.Bross.

Aquí viven todas las constantes del juego. Ningún otro archivo
debe tener números "mágicos" ni rutas escritas a mano.
"""

import os
import sys

# ---------------------------------------------------------------
# Rutas (absolutas, funcionan sin importar desde dónde se ejecute)
# ---------------------------------------------------------------
if getattr(sys, "frozen", False):
    BASE_DIR = sys._MEIPASS          # ejecutable creado con PyInstaller
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "assets", "images")
SOUNDS_DIR = os.path.join(BASE_DIR, "assets", "sounds")


def image_path(nombre):
    """Devuelve la ruta completa de una imagen en assets/images."""
    return os.path.join(IMAGES_DIR, nombre)


def sound_path(nombre):
    """Devuelve la ruta completa de un sonido en assets/sounds."""
    return os.path.join(SOUNDS_DIR, nombre)


# ---------------------------------------------------------------
# Ventana
# ---------------------------------------------------------------
TITLE = "Siuu.Bross"
WIDTH = 800
HEIGHT = 400
FPS = 60

# ---------------------------------------------------------------
# Física y jugador
# ---------------------------------------------------------------
GRAVITY = 0.8
JUMP_FORCE = -12
PLAYER_SPEED = 5
PLAYER_SIZE = (40, 60)
PLAYER_START = (50, 300)

# ---------------------------------------------------------------
# Tamaños de los objetos del juego
# ---------------------------------------------------------------
BALL_SIZE = (20, 20)
GOAL_SIZE = (50, 60)
HEART_SIZE = (30, 30)
SPIKE_SIZE = 20
ENEMY_SIZE = (40, 60)

# ---------------------------------------------------------------
# Vidas
# ---------------------------------------------------------------
INITIAL_LIVES = 3
MAX_LIVES = 5

# ---------------------------------------------------------------
# Puntuación
# ---------------------------------------------------------------
SCORE_BALL = 100
SCORE_GOAL = 500
SCORE_ENEMY = 200
SCORE_PER_LIFE = 100      # bonus por cada vida restante al terminar el nivel
SCORE_PER_SECOND = 10     # bonus por cada segundo sobrante (niveles con tiempo)

# ---------------------------------------------------------------
# Enemigos: velocidad según la dificultad del nivel (px por frame)
# ---------------------------------------------------------------
ENEMY_SPEED = {
    "easy": 1,
    "medium": 2,
    "hard": 3,
}

PLATFORM_SPEED = {
    "easy": 1,
    "medium": 2,
    "hard": 3,
}

# ---------------------------------------------------------------
# Colores
# ---------------------------------------------------------------
WHITE = (255, 255, 255)
GRAY = (120, 120, 120)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
DARK_RED = (150, 0, 0)
PLATFORM_MOVING = (90, 90, 160)

# ---------------------------------------------------------------
# Nombres de archivos de recursos (todos existen ya en assets/)
# ---------------------------------------------------------------
IMG_BACKGROUND = "fondo.png"
IMG_PLAYER = "cr7.png"
IMG_BALL = "balon.png"
IMG_GOAL = "porteria.png"
IMG_HEART = "corazon.png"
IMG_TERROR = "terror.png"

SND_MUSIC = "musica_fondo.mp3"
SND_BALL = "sonido_balon.wav"
SND_GOAL = "sonido_gol.wav"
SND_SCREAM = "grito.mp3"

MUSIC_VOLUME = 0.5
MUSIC_VOLUME_PAUSED = 0.15