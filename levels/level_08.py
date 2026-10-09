"""Nivel 8: La trampa (difícil)."""

LEVEL = {
    "name": "La trampa",
    "difficulty": "hard",
    "hint": "Aterriza en el punto exacto: los pinchos no perdonan",
    "width": 1840,
    "start": (50, 340),
    "balls": [(870, 310)],
    "goal": (1760, 340),
    "platforms": [
        (270, 350, 120, 20),    # A1: enemigo rápido
        (505, 320, 50, 20),     # A2: estrecha
        (675, 290, 50, 20),     # A3: estrecha
        (825, 330, 110, 20),    # A4: la trampa (pinchos en los dos extremos)
        (1410, 330, 50, 20),    # isla entre las dos plataformas móviles
    ],
    "spikes": [
        (825, 310),
        (915, 310),
    ],
    "floor_spikes": [
        (220, 1040),
        (1220, 1680),
    ],
    "enemies": [
        {"x": 120, "y": 340, "patrol": (120, 215)},
        {"x": 290, "y": 290, "patrol": (270, 390)},
        {"x": 1050, "y": 340, "patrol": (1040, 1130)},
        {"x": 1130, "y": 340, "patrol": (1130, 1220)},
        {"x": 1710, "y": 340, "patrol": (1700, 1830)},
    ],
    "hearts": [],
    "moving_platforms": [
        {"x": 1220, "y": 350, "w": 70, "h": 20, "axis": "x", "range": (1220, 1380)},
        {"x": 1490, "y": 350, "w": 70, "h": 20, "axis": "x", "range": (1490, 1680)},
    ],
    "time_limit": None,
}