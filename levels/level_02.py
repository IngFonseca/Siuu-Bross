"""Nivel 2: El primer rival (fácil)."""

LEVEL = {
    "name": "El primer rival",
    "difficulty": "easy",
    "hint": "Salta sobre los enemigos para derrotarlos",
    "width": 800,
    "start": (50, 340),
    "balls": [(540, 330)],
    "goal": (730, 340),
    "platforms": [
        (500, 350, 100, 20),
        (620, 310, 80, 20),
    ],
    "spikes": [],
    "floor_spikes": [
        (600, 720),
    ],
    "enemies": [
        {"x": 250, "y": 340, "patrol": (250, 450)},
    ],
    "hearts": [],
    "moving_platforms": [],
    "time_limit": None,
}