"""Nivel 10: La final (difícil)."""

LEVEL = {
    "name": "La final",
    "difficulty": "hard",
    "hint": "Tres balones, 90 segundos y todo lo que has aprendido",
    "width": 2560,
    "start": (50, 340),
    "balls": [(1220, 120), (1665, 330), (1985, 280)],
    "goal": (2480, 340),
    "platforms": [
        (260, 350, 70, 20),     # escalón del muro 1
        (340, 280, 20, 120),    # muro 1 (alto)
        (370, 350, 70, 20),
        (640, 350, 70, 20),     # escalón del muro 2
        (720, 290, 20, 110),    # muro 2
        (750, 350, 70, 20),
        (940, 100, 40, 20),     # repisa del corazón difícil
        (1180, 140, 100, 20),   # H1: primer balón (con enemigo)
        (1340, 180, 50, 20),    # H2
        (1610, 350, 130, 20),   # C1: segundo balón, pinchos en los extremos
        (1820, 330, 50, 20),    # C2
        (1970, 300, 50, 20),    # C3: tercer balón
    ],
    "spikes": [
        (1610, 330),
        (1720, 330),
    ],
    "floor_spikes": [
        (1000, 1500),
        (1600, 2120),
        (2240, 2440),
    ],
    "enemies": [
        {"x": 470, "y": 340, "patrol": (470, 600)},
        {"x": 860, "y": 340, "patrol": (860, 980)},
        {"x": 1200, "y": 80, "patrol": (1180, 1280)},
        {"x": 1510, "y": 340, "patrol": (1500, 1600)},
        {"x": 2130, "y": 340, "patrol": (2120, 2240)},
        {"x": 2450, "y": 340, "patrol": (2440, 2560)},
    ],
    "hearts": [(945, 70)],
    "moving_platforms": [
        {"x": 1020, "y": 380, "w": 80, "h": 20, "axis": "y", "range": (140, 400)},
        {"x": 2240, "y": 350, "w": 70, "h": 20, "axis": "x", "range": (2240, 2440)},
    ],
    "time_limit": 90,
}