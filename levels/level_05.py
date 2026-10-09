"""Nivel 5: Foso de pinchos (medio)."""

LEVEL = {
    "name": "Foso de pinchos",
    "difficulty": "medium",
    "hint": "El suelo es mortal: ve de plataforma en plataforma",
    "width": 1560,
    "start": (50, 340),
    "balls": [(1140, 240)],
    "goal": (1490, 220),
    "platforms": [
        (290, 350, 130, 20),    # P1: tiene un pincho encima
        (500, 320, 60, 20),     # P2
        (640, 290, 60, 20),     # P3
        (780, 340, 120, 20),    # P4: enemigo
        (980, 300, 60, 20),     # P5
        (1120, 260, 60, 20),    # P6: el balón
        (1260, 330, 120, 20),   # P7: enemigo
        (1440, 280, 120, 20),   # P8: la portería
    ],
    "spikes": [
        (360, 330),
    ],
    "floor_spikes": [
        (260, 1560),
    ],
    "enemies": [
        {"x": 150, "y": 340, "patrol": (130, 250)},
        {"x": 800, "y": 280, "patrol": (780, 900)},
        {"x": 1280, "y": 270, "patrol": (1260, 1380)},
    ],
    "hearts": [],
    "moving_platforms": [],
    "time_limit": None,
}