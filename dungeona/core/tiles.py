import random

TILES = {
    "floor": ".",
    "wall": "#",
    "water": "~",
    "grass": "\"",
    "rock": "o",
    "air": " "
}


WEIGHTS = {
    "floor": 0.5,
    "wall": 0.2,
    "water": 0.1,
    "grass": 0.15,
    "rock": 0.05
}

def get_tile(rng: random.Random):
    tile_type = rng.choices(
        population=list(TILES.keys()),
        weights=list(WEIGHTS.values())
    )[0]
    return TILES[tile_type]
