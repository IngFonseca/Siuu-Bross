"""Nivel 9: Contrarreloj (difícil)."""

LEVEL = {
    "name": "Contrarreloj",
    "difficulty": "hard",
    "hint": "Tres balones y 60 segundos. ¡No te detengas!",
    "width": 2000,
    "start": (50, 340),
    "balls": [(470, 130), (1085, 300), (1585, 300)],
    "goal": (1930, 340),
    "platforms": [
        (430, 150, 120, 20),    # H1: primer balón (con enemigo)
        (610, 190, 60, 20),     # H2
        (920, 350, 50, 20),     # piedra 1
        (1070, 320, 50, 20),    # piedra 2: segundo balón
        (1210, 350, 50, 20),    # piedra 3
        (1570, 320, 50, 20),    # isla: tercer balón
    ],
    "spikes": [],
    "floor_spikes": [
        (250, 700),
        (880, 1260),
        (1400, 1760),
    ],
    "enemies": [
        {"x": 450, "y": 90, "patrol": (430, 550)},
        {"x": 770, "y": 340, "patrol": (760, 880)},
        {"x": 1290, "y": 340, "patrol": (1270, 1400)},
        {"x": 1790, "y": 340, "patrol": (1770, 1880)},
        {"x": 1880, "y": 340, "patrol": (1880, 1990)},
    ],
    "hearts": [(1330, 340)],
    "moving_platforms": [
        {"x": 280, "y": 380, "w": 80, "h": 20, "axis": "y", "range": (150, 400)},
        {"x": 1400, "y": 350, "w": 70, "h": 20, "axis": "x", "range": (1400, 1540)},
        {"x": 1650, "y": 350, "w": 70, "h": 20, "axis": "x", "range": (1650, 1760)},
    ],
    "time_limit": 60,
}