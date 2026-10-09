"""Nivel 4: El muro (medio)."""

LEVEL = {
    "name": "El muro",
    "difficulty": "medium",
    "hint": "Usa el escalón para saltar el muro. ¡La cámara te sigue!",
    "width": 1200,
    "start": (50, 340),
    "balls": [(1020, 320)],
    "goal": (1130, 340),
    "platforms": [
        (340, 350, 90, 20),     # escalón antes del muro
        (440, 300, 20, 100),    # el muro
        (980, 340, 100, 20),    # plataforma del balón
    ],
    "spikes": [],
    "floor_spikes": [
        (580, 660),             # foso corto
        (740, 920),             # foso largo (con plataforma móvil)
    ],
    "enemies": [
        {"x": 190, "y": 340, "patrol": (180, 320)},
        {"x": 480, "y": 340, "patrol": (470, 570)},
    ],
    "hearts": [],
    "moving_platforms": [
        {"x": 740, "y": 350, "w": 80, "h": 20, "axis": "x", "range": (740, 920)},
    ],
    "time_limit": None,
}