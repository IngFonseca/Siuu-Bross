"""Lista ordenada de niveles del juego.

Para agregar un nivel nuevo:
  1. Crea levels/level_XX.py con un diccionario LEVEL.
  2. Impórtalo aquí y añádelo a LEVELS, en el orden de juego.
"""

from levels.level_01 import LEVEL as LEVEL_01
from levels.level_02 import LEVEL as LEVEL_02
from levels.level_03 import LEVEL as LEVEL_03
from levels.level_04 import LEVEL as LEVEL_04
from levels.level_05 import LEVEL as LEVEL_05
from levels.level_06 import LEVEL as LEVEL_06
from levels.level_07 import LEVEL as LEVEL_07
from levels.level_08 import LEVEL as LEVEL_08
from levels.level_09 import LEVEL as LEVEL_09
from levels.level_10 import LEVEL as LEVEL_10

LEVELS = [
    LEVEL_01,
    LEVEL_02,
    LEVEL_03,
    LEVEL_04,
    LEVEL_05,
    LEVEL_06,
    LEVEL_07,
    LEVEL_08,
    LEVEL_09,
    LEVEL_10,
]