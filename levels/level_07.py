"""Nivel 7: Doble balón (medio)."""

LEVEL = {
    "name": "Doble balón",
    "difficulty": "medium",
    "hint": "Recoge los dos balones y vuelve a la portería",
    "width": 1700,
    "start": (50, 340),
    "balls": [(875, 320), (1590, 320)],
    "goal": (130, 340),
    "platforms": [
        (240, 350, 70, 20),     # escalón izquierdo del muro 1
        (320, 290, 20, 110),    # muro 1
        (350, 350, 70, 20),     # escalón derecho del muro 1
        (840, 340, 90, 20),     # plataforma del primer balón
        (1350, 350, 70, 20),    # escalón izquierdo del muro 2
        (1430, 290, 20, 110),   # muro 2
        (1460, 350, 70, 20),    # escalón derecho del muro 2
        (1540, 340, 120, 20),   # plataforma del segundo balón
    ],
    "spikes": [],
    "floor_spikes": [
        (590, 790),
        (1090, 1290),
    ],
    "enemies": [
        {"x": 140, "y": 340, "patrol": (130, 235)},
        {"x": 450, "y": 340, "patrol": (440, 570)},
        {"x": 960, "y": 340, "patrol": (950, 1070)},
        {"x": 1560, "y": 280, "patrol": (1540, 1660)},
    ],
    "hearts": [],
    "moving_platforms": [
        {"x": 590, "y": 350, "w": 90, "h": 20, "axis": "x", "range": (590, 790)},
        {"x": 1090, "y": 350, "w": 90, "h": 20, "axis": "x", "range": (1090, 1290)},
    ],
    "time_limit": None,
}