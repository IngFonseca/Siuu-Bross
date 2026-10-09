"""Nivel 3: Escalera al gol (fácil)."""

LEVEL = {
    "name": "Escalera al gol",
    "difficulty": "easy",
    "hint": "Sube por las plataformas hasta la portería",
    "width": 800,
    "start": (50, 340),
    "balls": [(600, 250)],
    "goal": (740, 170),
    "platforms": [
        (140, 350, 140, 20),
        (330, 310, 140, 20),
        (520, 270, 140, 20),
        (700, 230, 100, 20),
    ],
    "spikes": [
        (390, 290),
    ],
    "floor_spikes": [],
    "enemies": [
        {"x": 180, "y": 290, "patrol": (140, 280)},
        {"x": 540, "y": 210, "patrol": (520, 660)},
    ],
    "hearts": [(475, 250)],
    "moving_platforms": [],
    "time_limit": None,
}