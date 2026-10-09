"""Nivel 6: El ascensor (medio)."""

LEVEL = {
    "name": "El ascensor",
    "difficulty": "medium",
    "hint": "Sube con el ascensor, recoge el balón y baja por el otro",
    "width": 1400,
    "start": (50, 340),
    "balls": [(940, 100)],
    "goal": (1300, 340),
    "platforms": [
        (340, 120, 60, 20),     # repisa del corazón escondido
        (560, 200, 120, 20),    # U1: enemigo
        (760, 160, 100, 20),    # U2: enemigo
        (900, 120, 100, 20),    # U3: el balón
    ],
    "spikes": [],
    "floor_spikes": [
        (420, 1120),
    ],
    "enemies": [
        {"x": 580, "y": 140, "patrol": (560, 680)},
        {"x": 770, "y": 100, "patrol": (760, 860)},
    ],
    "hearts": [(355, 90)],
    "moving_platforms": [
        {"x": 420, "y": 380, "w": 80, "h": 20, "axis": "y", "range": (180, 400)},
        {"x": 1040, "y": 160, "w": 80, "h": 20, "axis": "y", "range": (120, 400)},
    ],
    "time_limit": None,
}