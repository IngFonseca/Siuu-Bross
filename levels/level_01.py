"""Nivel 1: Calentamiento (fácil).

Enseña a moverse, saltar, recoger el balón y marcar. El suelo tiene
dos fosos de pinchos: el primero es corto y se salta directamente;
el segundo es demasiado ancho y obliga a usar la plataforma.

Solo datos: este archivo no importa pygame ni contiene lógica.
"""

LEVEL = {
    "name": "Calentamiento",
    "difficulty": "easy",
    "hint": "Usa las flechas para moverte y ESPACIO para saltar",
    "width": 800,
    "start": (50, 340),
    "balls": [(220, 330)],
    "goal": (730, 340),
    "platforms": [
        (180, 350, 100, 20),   # lleva el balón: hay que saltar para cogerlo
        (500, 350, 100, 20),   # piedra de paso sobre el segundo foso
    ],
    "spikes": [],
    "floor_spikes": [
        (340, 400),            # foso corto (60 px): se salta directamente
        (480, 620),            # foso largo (140 px): hay que usar la plataforma
    ],
    "enemies": [],
    "hearts": [],
    "moving_platforms": [],
    "time_limit": None,
}